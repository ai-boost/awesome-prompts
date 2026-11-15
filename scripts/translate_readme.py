"""Generate README_zh.md from README.md.

Run from the repository root:  python scripts/translate_readme.py

Each line of prose is translated once by Claude (Haiku) and kept in scripts/readme_zh_cache.json,
keyed by a hash of its English text, so a run only sends lines that are new or changed. Links, code, names
and the prompts themselves stay as written. Headings get an anchor with the English slug, so links
like #prompts work in both files.
"""
import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scripts" / "readme_zh_cache.json"
BATCH = 40

SWITCH_EN = '<p><b>English</b> · <a href="README_zh.md">简体中文</a></p>'
SWITCH_ZH = '<p><a href="README.md">English</a> · <b>简体中文</b></p>'
# agentcraft.dev sections that have a Chinese version
SITE_ZH = ("https://agentcraft.dev/en/prompts/", "https://agentcraft.dev/en/skills/")

SYSTEM = """You translate lines of a GitHub README (an awesome list about LLM prompts) from English to Simplified Chinese.
Input: a JSON array of {"i": number, "t": line}. Output: only a JSON array of {"i": number, "t": translated line}, same numbers, nothing else.
Rules:
- Translate the prose: descriptions, headings, table cells, sentences.
- Keep unchanged: Markdown and HTML syntax, URLs, inline code, emoji, numbers, and the leading characters of the line (#, -, |, >, spaces).
- Keep names as written: product, company, repository, model, paper and person names, and link text that is a name or a title.
- Generic link labels (for example Online Gallery, Papers) may be translated.
- Keep the same number of | characters in table rows.
- Natural, concise Chinese as a Chinese developer would write it. Chinese punctuation in Chinese text."""

URL = re.compile(r'\]\(([^)\s]+)|href="([^"]+)"|src="([^"]+)"')
CODE = re.compile(r"`[^`]+`")


def key(line):
    return hashlib.sha1(line.encode()).hexdigest()[:16]


def slug(text):
    """GitHub's heading anchor."""
    text = re.sub(r"<[^>]+>|`", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def needs_translation(line):
    bare = re.sub(r"\]\([^)]*\)|<[^>]+>|`[^`]*`|https?://\S+", " ", line)
    return re.search(r"[A-Za-z]{3,}", bare) is not None


def lead(line):
    """The line's indentation and Markdown marker."""
    m = re.match(r"\s*(#+ |- |\* |\d+\. |\| |> )?", line)
    return m.group() if m else ""


def keeps_structure(en, zh):
    return (bool(zh) and URL.findall(en) == URL.findall(zh) and en.count("|") == zh.count("|")
            and CODE.findall(en) == CODE.findall(zh) and lead(en) == lead(zh))


def ask(batch):
    """batch: list of English lines. Returns {line: translation} for the lines that came back intact."""
    req = json.dumps([{"i": i, "t": t} for i, t in enumerate(batch)], ensure_ascii=False)
    out = subprocess.run(["claude", "-p", "--setting-sources", "project", "--model", "haiku", "--system-prompt", SYSTEM],
                         input=req, capture_output=True, text=True, timeout=900).stdout
    m = re.search(r"\[.*\]", out, re.S)
    try:
        got = {x["i"]: x["t"] for x in json.loads(m.group())} if m else {}
    except (json.JSONDecodeError, KeyError, TypeError):
        return {}
    return {en: got[i] for i, en in enumerate(batch) if i in got and keeps_structure(en, got[i])}


def main():
    lines = (ROOT / "README.md").read_text(encoding="utf-8").split("\n")
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}

    fenced, todo = False, []
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and needs_translation(line) and key(line) not in cache and line not in todo:
            todo.append(line)
    for _ in range(2):  # a second pass retries lines that came back broken
        batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
        with ThreadPoolExecutor(4) as pool:
            for got in pool.map(ask, batches):
                cache.update({key(en): zh for en, zh in got.items()})
        todo = [t for t in todo if key(t) not in cache]

    out, fenced, seen = [], False, {}
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        if fenced or line.startswith("```"):
            out.append(line)
            continue
        if line.strip() == SWITCH_EN:
            out.append(line.replace(SWITCH_EN, SWITCH_ZH))
            continue
        zh = cache.get(key(line), line)
        heading = re.match(r"(#+) (.*)", line)
        if heading:
            s = slug(heading.group(2))
            n = seen.get(s, 0)
            seen[s] = n + 1
            out += [f'<a id="{s}{f"-{n}" if n else ""}"></a>', ""]
        for prefix in SITE_ZH:
            zh = zh.replace(prefix, prefix.replace("/en/", "/zh/"))
        out.append(zh)
    (ROOT / "README_zh.md").write_text("\n".join(out), encoding="utf-8")

    used = {key(l) for l in lines}
    CACHE.write_text(json.dumps({k: v for k, v in cache.items() if k in used}, ensure_ascii=False, indent=0, sort_keys=True),
                     encoding="utf-8")
    print(f"README_zh.md: {sum(needs_translation(l) for l in lines)} lines of prose, {len(todo)} left in English")


if __name__ == "__main__":
    main()
