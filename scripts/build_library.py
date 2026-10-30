"""Build the bilingual prompt library under library/.

Sources (downloaded by this script):
  prompts.chat prompts.csv                      English, CC0 1.0
  CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN     Chinese translation of the same prompts, CC0 1.0
  langgptai/wonderful-prompts README            original Chinese prompts, MIT
  rockbenben/ChatGPT-Shortcut prompt.json       author-written Chinese and English versions, MIT
  langgptai/awesome-doubao-prompts README       original Chinese prompts, Apache-2.0
  langgptai/awesome-gemini-prompts prompts/     original Chinese prompts (selected files), CC0 1.0
  library/sources/deepseek-prompt-library.json  DeepSeek's official Chinese prompt library, quoted with attribution

Prompts that exist in only one language get a model translation of the other; the
`translated` column says which language was machine translated so it is never passed off
as human work.

Each prompt gets one category, a title in both languages and a language tag
(en, zh or both). Categories and titles come from a model pass that is cached in
library/prompts.csv: rows already there are reused, so reruns only classify new prompts.

Writes library/prompts.csv, library/{en,zh}/<category>.md and the README tables.
Usage: python3 scripts/build_library.py [--limit N]
"""
import argparse
import concurrent.futures as cf
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "library"
csv.field_size_limit(sys.maxsize)

SOURCES = {
    "prompts.chat": ("https://raw.githubusercontent.com/f/prompts.chat/main/prompts.csv", "CC0-1.0",
                     "https://prompts.chat"),
    "zh-CN": ("https://raw.githubusercontent.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN/main/prompts_zh-CN.csv", "CC0-1.0",
              "https://github.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN"),
    # The English snapshot that zh-CN was translated from; its rows line up with prompts_zh-CN.csv.
    "zh-CN-en": ("https://raw.githubusercontent.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN/main/prompts.csv", "CC0-1.0",
                 "https://github.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN"),
    "wonderful-prompts": ("https://raw.githubusercontent.com/langgptai/wonderful-prompts/main/README.md", "MIT",
                          "https://github.com/langgptai/wonderful-prompts"),
    "ChatGPT-Shortcut": ("https://raw.githubusercontent.com/rockbenben/ChatGPT-Shortcut/main/src/data/prompt.json", "MIT",
                         "https://github.com/rockbenben/ChatGPT-Shortcut"),
    "awesome-doubao-prompts": ("https://raw.githubusercontent.com/langgptai/awesome-doubao-prompts/main/README.md", "Apache-2.0",
                               "https://github.com/langgptai/awesome-doubao-prompts"),
    "awesome-gemini-prompts": ("https://raw.githubusercontent.com/langgptai/awesome-gemini-prompts/main/prompts/", "CC0-1.0",
                               "https://github.com/langgptai/awesome-gemini-prompts"),
}

CATEGORIES = {
    "coding": ("Coding & Development", "编程开发"),
    "writing": ("Writing & Content", "写作与内容"),
    "marketing": ("Marketing & Sales", "营销与销售"),
    "business": ("Business & Career", "商业与职场"),
    "education": ("Education & Learning", "教育与学习"),
    "language": ("Language & Translation", "语言与翻译"),
    "data": ("Data & Analysis", "数据与分析"),
    "productivity": ("Productivity", "效率"),
    "research": ("Research & Science", "研究与科学"),
    "health": ("Health & Wellness", "健康"),
    "finance": ("Finance & Legal", "财务与法律"),
    "creative": ("Creative Arts & Music", "艺术与音乐"),
    "image": ("Image & Design", "图像与设计"),
    "games": ("Games & Fun", "游戏与娱乐"),
    "roleplay": ("Role-play & Characters", "角色扮演"),
    "lifestyle": ("Lifestyle & Travel", "生活与旅行"),
    "prompting": ("Prompt Engineering", "提示词工程"),
}
FIELDS = ["id", "category", "lang", "title_en", "title_zh", "prompt_en", "prompt_zh", "translated", "for_devs", "source", "license"]
# awesome-gemini-prompts files worth keeping: original Chinese prompts that are not jailbreaks,
# vendor system prompts, or personas of real people.
GEMINI_FILES = ["小红书变现达人.md", "小红书爆款规律——流量黑客.md", "小红书爆款账号定位架构师.md", "小红书风控和增长官.md",
                "微科幻之神.md", "手相大师-玄师.md"]


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read().decode("utf-8")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def cjk(text):
    return len(re.findall(r"[\u4e00-\u9fff]", text or "")) > 10


def parse_wonderful(md):
    """Original Chinese prompts. Each TOC entry owns the text up to the next TOC heading; use its
    first fenced block when there is one, else the raw section (many prompts are plain Markdown)."""
    toc = md.split("## 目录", 1)[1].split("\n## ", 1)[0]
    titles = [t for t in re.findall(r"\[([^\]]+)\]\(#", toc) if t not in ("Prompts 精选 🚀", "目录")]
    body = md.split("## 目录", 1)[1]
    spots = []
    for t in titles:
        m = re.search(r"^#{2,4} " + re.escape(t) + r"\s*$", body, re.M)
        if m:
            spots.append((m.start(), m.end(), t))
    spots.sort()
    items = []
    for i, (_, end, t) in enumerate(spots):
        sec = body[end: spots[i + 1][0] if i + 1 < len(spots) else len(body)]
        block = re.search(r"^```[^\n]*\n(.*?)^```", sec, re.M | re.S)
        text = (block.group(1) if block else sec).strip()
        if len(text) >= 80 and cjk(text):
            items.append({"title": t.strip(" 🔥🚀"), "prompt": text})
    return items


def parse_doubao(md):
    """#### headings, each followed by one fenced prompt."""
    items = []
    for m in re.finditer(r"^#### (.+?)\s*$(.*?)(?=^#{2,4} |\Z)", md, re.M | re.S):
        block = re.search(r"^```[^\n]*\n(.*?)^```", m.group(2), re.M | re.S)
        title = re.sub(r"[*\s]+", " ", re.sub(r"[^\w\s\u4e00-\u9fff·]", "", m.group(1))).strip()
        if block and len(block.group(1).strip()) >= 80:
            items.append({"title": title, "prompt": block.group(1).strip()})
    return items


def parse_gemini():
    base = SOURCES["awesome-gemini-prompts"][0]
    items = []
    for name in GEMINI_FILES:
        text = fetch(base + urllib.parse.quote(name)).strip()
        items.append({"title": re.sub(r"[—–-]+", " ", name[:-3]).strip(), "prompt": text})
    return items


def norm(text):
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())[:160]


TRANSLATE_ASK = (
    "Translate each prompt below into {target}. Keep the meaning, structure, Markdown, code, "
    "placeholders and anything in brackets exactly; translate only the natural language. "
    "Reply with every translation as\n### <id>\n<translation>\nand nothing else.\n\n"
)


def translate(batch, target):
    """batch: list of (id, text). Returns {id: translation}."""
    ask = TRANSLATE_ASK.format(target=target) + "\n\n".join(f"### {i}\n{t}" for i, t in batch)
    for _ in range(3):
        out = subprocess.run(["claude", "-p", "--model", "sonnet", "--output-format", "text"],
                             input=ask, capture_output=True, text=True, timeout=1800).stdout
        got = {m.group(1).strip(): m.group(2).strip()
               for m in re.finditer(r"^### (\S+)\s*\n(.*?)(?=^### \S+\s*$|\Z)", out, re.M | re.S)}
        if all(i in got and got[i] for i, _ in batch):
            return got
    return {}


def classify(batch):
    """One model call: category, Chinese and English titles, or skip."""
    cats = "\n".join(f"{k}: {v[0]}" for k, v in CATEGORIES.items())
    ask = (
        "Classify each prompt for a public prompt library. Reply with JSON only: a list of objects "
        '{"id", "cat", "title_en", "title_zh"}.\n'
        f"cat is one of these keys:\n{cats}\n"
        'or "skip" when the prompt is sexual, a jailbreak or safety bypass, an advertisement, spam, '
        "hateful, or has no usable instruction.\n"
        "title_en: short natural English title (keep the given one if it is fine). "
        "title_zh: short natural Simplified Chinese title. No quotes or dashes in titles.\n\n"
        + json.dumps(batch, ensure_ascii=False)
    )
    for _ in range(3):
        out = subprocess.run(["claude", "-p", "--model", "sonnet", "--output-format", "text"],
                             input=ask, capture_output=True, text=True, timeout=900).stdout
        m = re.search(r"\[.*\]", out, re.S)
        try:
            return json.loads(m.group(0)) if m else []
        except json.JSONDecodeError:
            continue
    return []


PAGE_BYTES = 350_000  # GitHub stops rendering Markdown files much past this size


def page_name(key, n):
    return f"{key}.md" if n == 1 else f"{key}-{n}.md"


def write_md(rows):
    for lang in ("en", "zh"):
        d = LIB / lang
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.md"):
            f.unlink()
        for key, (en, zh) in CATEGORIES.items():
            col = f"prompt_{lang}"
            items = sorted((r for r in rows if r["category"] == key and r[col]), key=lambda r: r[f"title_{lang}"].lower())
            if not items:
                continue
            mt = " · machine translated" if lang == "en" else " · 机器翻译"
            blocks = [f"<details><summary><b>{r[f'title_{lang}']}</b>{mt if r.get('translated') == lang else ''}</summary>\n\n```text\n"
                      + r[col].replace("```", "'''") + "\n```\n\n</details>\n" for r in items]
            pages, cur, size = [], [], 0
            for b in blocks:
                if cur and size + len(b.encode()) > PAGE_BYTES:
                    pages.append(cur)
                    cur, size = [], 0
                cur.append(b)
                size += len(b.encode())
            pages.append(cur)
            name = en if lang == "en" else zh
            for n, page in enumerate(pages, 1):
                nav = " · ".join(f"[{i}]({page_name(key, i)})" if i != n else f"**{i}**" for i in range(1, len(pages) + 1))
                head = [f"# {name}" + (f" ({n}/{len(pages)})" if len(pages) > 1 else ""), "",
                        (f"{len(items)} prompts. Copy one, replace anything in brackets, and paste it into any chat model."
                         if lang == "en" else f"共 {len(items)} 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。"),
                        "", f"[English](../en/{key}.md) · [中文](../zh/{key}.md)", ""]
                if len(pages) > 1:
                    head += [("Pages: " if lang == "en" else "分页：") + nav, ""]
                (d / page_name(key, n)).write_text("\n".join(head) + "\n" + "\n".join(page), encoding="utf-8")


def write_readmes(rows, skipped):
    counts = {k: {l: sum(1 for r in rows if r["category"] == k and r[f"prompt_{l}"]) for l in ("en", "zh")} for k in CATEGORIES}
    table = ["| Category · 分类 | English | 中文 |", "|---|---:|---:|"]
    for k, (en, zh) in CATEGORIES.items():
        c = counts[k]
        if c["en"] or c["zh"]:
            table.append(f"| {en} · {zh} | [{c['en']}](library/en/{k}.md) | [{c['zh']}](library/zh/{k}.md) |")
    both = sum(r["lang"] == "both" for r in rows)
    mt = sum(1 for r in rows if r.get("translated"))
    human = both - mt
    block = [
        "<!-- library:start (generated by scripts/build_library.py) -->",
        "## Prompt Library · 提示词库", "",
        f"**{len(rows):,} everyday prompts** for writing, coding, marketing, study, design and more. "
        f"Every prompt comes in English and Chinese ({human:,} with both versions written by people, {mt:,} with one side machine translated and marked as such); open the column for your language. "
        "Looking for skills that extend Claude Code instead? See the [Claude Code skills directory](https://agentcraft.dev/en/skills/).", "",
        f"**{len(rows):,} 条日常提示词**，覆盖写作、编程、营销、学习、设计等场景，全部中英双语"
        f"（{human:,} 条两种语言都出自人工，{mt:,} 条有一种语言是机器翻译，已标注），点你要的语言那一列即可。想给 Claude Code 装 skills，可以看 [Claude Code skills 目录](https://agentcraft.dev/zh/skills/)。", "",
        *table, "",
        "Sources and licenses: [library/README.md](library/README.md). Raw data: [library/prompts.csv](library/prompts.csv).",
        "<!-- library:end -->",
    ]
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "<!-- library:start" in readme:
        readme = re.sub(r"<!-- library:start.*?<!-- library:end -->", "\n".join(block), readme, flags=re.S)
    else:
        readme = readme.replace("\n## Prompts\n", "\n" + "\n".join(block) + "\n\n## Prompts\n", 1)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    by_src = {}
    for r in rows:
        by_src[r["source"]] = by_src.get(r["source"], 0) + 1
    (LIB / "README.md").write_text("\n".join([
        "# Prompt Library · 提示词库", "",
        "Built by `scripts/build_library.py`. Rerun it to pull new upstream prompts; existing rows keep their category and titles.", "",
        "## Columns", "",
        "`id`, `category`, `lang` (`both`, `en` or `zh`), `title_en`, `title_zh`, `prompt_en`, `prompt_zh`, `for_devs`, `source`, `license`.", "",
        "## Sources", "",
        f"- [prompts.chat](https://prompts.chat) (`prompts.csv`), CC0 1.0. English text of {sum(v for k, v in by_src.items() if k.startswith('prompts.chat')):,} prompts.",
        f"- [CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN](https://github.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN), CC0 1.0. "
        f"Chinese text of {by_src.get('prompts.chat + zh-CN', 0):,} of them, kept only where the English is unchanged since the translation.",
        f"- [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut), MIT, Copyright (c) 2023 rockbenben. "
        f"The author's Chinese versions for {sum(v for k, v in by_src.items() if k.endswith('+ ChatGPT-Shortcut')):,} prompts.chat prompts "
        f"and {by_src.get('ChatGPT-Shortcut', 0):,} prompts of its own. License: [LICENSE-ChatGPT-Shortcut-MIT.txt](LICENSE-ChatGPT-Shortcut-MIT.txt).",
        f"- [langgptai/wonderful-prompts](https://github.com/langgptai/wonderful-prompts), MIT, Copyright (c) 2023 yzfly. "
        f"{by_src.get('wonderful-prompts', 0)} original Chinese prompts. License: [LICENSE-wonderful-prompts-MIT.txt](LICENSE-wonderful-prompts-MIT.txt).",
        f"- [langgptai/awesome-doubao-prompts](https://github.com/langgptai/awesome-doubao-prompts), Apache-2.0. "
        f"{by_src.get('awesome-doubao-prompts', 0)} original Chinese prompts. License: [LICENSE-awesome-doubao-prompts-Apache-2.0.txt](LICENSE-awesome-doubao-prompts-Apache-2.0.txt).",
        f"- [langgptai/awesome-gemini-prompts](https://github.com/langgptai/awesome-gemini-prompts), CC0 1.0. "
        f"{by_src.get('awesome-gemini-prompts', 0)} original Chinese prompts.",
        f"- [DeepSeek prompt library](https://api-docs.deepseek.com/zh-cn/prompt-library/), Copyright DeepSeek, Inc. "
        f"{by_src.get('DeepSeek', 0)} official example prompts, quoted with attribution (`sources/deepseek-prompt-library.json`).", "",
        "## Machine translation", "",
        f"{sum(1 for r in rows if r.get('translated') == 'zh'):,} prompts got a Chinese version and "
        f"{sum(1 for r in rows if r.get('translated') == 'en'):,} got an English version from a model. "
        "The `translated` column names that language, and the Markdown pages mark those entries. "
        "A human translation from any source replaces the machine one on the next build.", "",
        "Categories and the missing-language titles were assigned by a model pass and spot-checked. "
        f"{len(skipped)} prompts were left out as sexual, jailbreak, spam or empty (ids in `skipped.json`).", "",
    ]), encoding="utf-8")


def add_new(raw, sid, item):
    while sid in raw:
        sid += "-2"
    item["id"] = sid
    raw[sid] = item


def collect():
    """All prompts from every source, keyed by id, before classification and translation."""
    en_rows = list(csv.DictReader(io.StringIO(fetch(SOURCES["prompts.chat"][0]))))
    zh_rows = list(csv.DictReader(io.StringIO(fetch(SOURCES["zh-CN"][0]))))
    snap = list(csv.DictReader(io.StringIO(fetch(SOURCES["zh-CN-en"][0]))))
    # zh-CN titles are translated, so pair by row with the English snapshot, then keep a Chinese
    # version only when the upstream English text is unchanged since that snapshot.
    zh_by_act = {s["act"].strip(): (s["prompt"].strip(), z["提示"].strip()) for s, z in zip(snap, zh_rows)}

    raw = {}
    for r in en_rows:
        act, text = r["act"].strip(), r["prompt"].strip()
        sid = slug(act)
        if not sid or sid in raw or len(text) < 80:
            continue
        pair = zh_by_act.get(act)
        zh = pair[1] if pair and pair[0] == text else ""
        raw[sid] = {"id": sid, "title_en": act, "prompt_en": text, "prompt_zh": zh,
                    "for_devs": r.get("for_devs", "").upper() == "TRUE",
                    "source": "prompts.chat" + (" + zh-CN" if zh else ""), "license": "CC0-1.0"}

    # ChatGPT-Shortcut: the author's own Chinese and English versions. Fill missing Chinese on
    # matching prompts.chat rows, add the rest as new bilingual prompts.
    by_norm = {norm(x["prompt_en"]): x for x in raw.values()}
    for it in json.loads(fetch(SOURCES["ChatGPT-Shortcut"][0])):
        zh, en = it.get("zh", {}), it.get("en", {})
        zh_text = (zh.get("prompt") if cjk(zh.get("prompt")) else zh.get("description")) or ""
        en_text = "" if cjk(en.get("prompt")) else (en.get("prompt") or "")
        if len(zh_text) < 20 and len(en_text) < 80:
            continue
        hit = by_norm.get(norm(en_text)) if en_text else None
        if hit:
            if not hit["prompt_zh"] and cjk(zh_text):
                hit["prompt_zh"] = zh_text.strip()
                hit["source"] += " + ChatGPT-Shortcut"
                hit["license"] = "CC0-1.0, MIT"
            continue
        add_new(raw, "sc-" + (slug(en.get("title", "")) or str(it.get("id"))), {
            "title_en": en.get("title", ""), "title_zh": zh.get("title", ""),
            "prompt_en": en_text.strip(), "prompt_zh": zh_text.strip() if cjk(zh_text) else "",
            "for_devs": "code" in it.get("tags", []), "source": "ChatGPT-Shortcut", "license": "MIT"})

    for name, items in (("wonderful-prompts", parse_wonderful(fetch(SOURCES["wonderful-prompts"][0]))),
                        ("awesome-doubao-prompts", parse_doubao(fetch(SOURCES["awesome-doubao-prompts"][0]))),
                        ("awesome-gemini-prompts", parse_gemini()),
                        ("DeepSeek", json.loads((LIB / "sources/deepseek-prompt-library.json").read_text())["items"])):
        for w in items:
            # Chinese titles slug to nothing, so derive a stable id from the title text.
            add_new(raw, "zh-" + (slug(w["title"]) or hashlib.sha1(w["title"].encode()).hexdigest()[:10]), {
                "title_zh": w["title"], "prompt_en": "", "prompt_zh": w["prompt"],
                "for_devs": False, "source": name,
                "license": SOURCES[name][1] if name in SOURCES else "Copyright DeepSeek, quoted with attribution"})
    return raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="classify or translate at most N new prompts (trial run)")
    ap.add_argument("--no-translate", action="store_true")
    a = ap.parse_args()

    raw = collect()
    old = {}
    if (LIB / "prompts.csv").exists():
        old = {r["id"]: r for r in csv.DictReader(open(LIB / "prompts.csv", encoding="utf-8"))}
    skipped = set(json.loads((LIB / "skipped.json").read_text())) if (LIB / "skipped.json").exists() else set()

    # 1. classify new prompts
    todo = [x for x in raw.values() if x["id"] not in old and x["id"] not in skipped]
    if a.limit:
        todo = todo[: a.limit]
    batches = [todo[i:i + 120] for i in range(0, len(todo), 120)]
    labels = {}
    with cf.ThreadPoolExecutor(4) as ex:
        for res in ex.map(classify, [[{"id": x["id"], "title": x.get("title_en") or x.get("title_zh"),
                                       "text": (x["prompt_en"] or x["prompt_zh"])[:300]} for x in b] for b in batches]):
            for o in res:
                labels[o.get("id")] = o
            print(f"classified {len(labels)}/{len(todo)}", flush=True)

    rows = []
    for x in raw.values():
        if x["id"] in old:
            r = dict(old[x["id"]])
            # Human text from a source always wins over an earlier machine translation.
            for l in ("en", "zh"):
                if x[f"prompt_{l}"]:
                    r[f"prompt_{l}"] = x[f"prompt_{l}"]
                    if r.get("translated") == l:
                        r["translated"] = ""
            r["source"], r["license"] = x["source"], x["license"]
            rows.append(r)
            continue
        lab = labels.get(x["id"])
        if not lab:
            continue  # not classified this run; picked up next time
        if lab.get("cat") == "skip" or lab.get("cat") not in CATEGORIES:
            skipped.add(x["id"])
            continue
        rows.append({
            "id": x["id"], "category": lab["cat"],
            "title_en": (lab.get("title_en") or x.get("title_en", "")).strip(),
            "title_zh": (lab.get("title_zh") or x.get("title_zh", "")).strip(),
            "prompt_en": x["prompt_en"], "prompt_zh": x["prompt_zh"], "translated": "",
            "for_devs": "true" if x["for_devs"] else "false", "source": x["source"], "license": x["license"],
        })

    # 2. machine-translate the missing language, a few prompts per call
    if not a.no_translate:
        need = [(r, "zh" if r["prompt_en"] else "en") for r in rows if not (r["prompt_en"] and r["prompt_zh"])]
        if a.limit:
            need = need[: a.limit]
        jobs, cur, size = [], [], 0
        for r, tgt in need:
            text = r["prompt_en"] or r["prompt_zh"]
            if cur and (size + len(text) > 12_000 or len(cur) >= 10 or cur[0][1] != tgt):
                jobs.append(cur)
                cur, size = [], 0
            cur.append((r, tgt))
            size += len(text)
        if cur:
            jobs.append(cur)
        done = 0
        with cf.ThreadPoolExecutor(4) as ex:
            futs = {ex.submit(translate, [(r["id"], r["prompt_en"] or r["prompt_zh"]) for r, _ in job],
                              "Simplified Chinese" if job[0][1] == "zh" else "English"): job for job in jobs}
            for fu in cf.as_completed(futs):
                got = fu.result()
                for r, tgt in futs[fu]:
                    if got.get(r["id"]):
                        r[f"prompt_{tgt}"] = got[r["id"]]
                        r["translated"] = tgt
                        done += 1
                print(f"translated {done}/{len(need)}", flush=True)

    for r in rows:
        r["lang"] = "both" if r["prompt_en"] and r["prompt_zh"] else ("en" if r["prompt_en"] else "zh")
        r.setdefault("translated", "")

    LIB.mkdir(exist_ok=True)
    rows.sort(key=lambda r: (r["category"], r["id"]))
    with open(LIB / "prompts.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows({k: r.get(k, "") for k in FIELDS} for r in rows)
    (LIB / "skipped.json").write_text(json.dumps(sorted(skipped), indent=0) + "\n")
    write_md(rows)
    write_readmes(rows, skipped)
    by_lang = {k: sum(r["lang"] == k for r in rows) for k in ("both", "en", "zh")}
    mt = {k: sum(r["translated"] == k for r in rows) for k in ("zh", "en")}
    print(f"library: {len(rows)} prompts {by_lang}, machine translated {mt}, skipped {len(skipped)}, "
          f"unclassified {len(raw) - len(rows) - len(skipped)}")


if __name__ == "__main__":
    main()
