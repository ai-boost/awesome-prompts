"""Build the bilingual prompt library under library/.

Sources (downloaded by this script):
  prompts.chat prompts.csv                      English, CC0 1.0
  CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN     Chinese translation of the same prompts, CC0 1.0
  langgptai/wonderful-prompts README            original Chinese prompts, MIT

Each prompt gets one category, a title in both languages and a language tag
(en, zh or both). Categories and titles come from a model pass that is cached in
library/prompts.csv: rows already there are reused, so reruns only classify new prompts.

Writes library/prompts.csv and library/{en,zh}/<category>.md.
Usage: python3 scripts/build_library.py [--limit N]
"""
import argparse
import concurrent.futures as cf
import csv
import io
import json
import re
import subprocess
import sys
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
FIELDS = ["id", "category", "lang", "title_en", "title_zh", "prompt_en", "prompt_zh", "for_devs", "source", "license"]


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read().decode("utf-8")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def parse_wonderful(md):
    """Original Chinese prompts: each TOC heading followed by its first fenced block."""
    toc = md.split("## 目录", 1)[1].split("\n## ", 1)[0]
    titles = [t for t in re.findall(r"\[([^\]]+)\]\(#", toc) if t not in ("Prompts 精选 🚀", "目录")]
    body = md.split("## 目录", 1)[1]
    items = []
    for t in titles:
        m = re.search(r"^#{2,4} " + re.escape(t) + r"\s*$(.*?)(?=^#{2,4} |\Z)", body, re.M | re.S)
        if not m:
            continue
        block = re.search(r"^```[^\n]*\n(.*?)^```", m.group(1), re.M | re.S)
        if block and len(block.group(1).strip()) >= 80:
            items.append({"title": t.strip(" 🔥🚀"), "prompt": block.group(1).strip()})
    return items


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
            blocks = [f"<details><summary><b>{r[f'title_{lang}']}</b></summary>\n\n```text\n"
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
            online = (f"https://agentcraft.dev/en/prompts/{key}/" if lang == "en" else f"https://agentcraft.dev/zh/prompts/{key}/")
            for n, page in enumerate(pages, 1):
                nav = " · ".join(f"[{i}]({page_name(key, i)})" if i != n else f"**{i}**" for i in range(1, len(pages) + 1))
                head = [f"# {name}" + (f" ({n}/{len(pages)})" if len(pages) > 1 else ""), "",
                        (f"{len(items)} prompts. Copy one, replace anything in brackets, and paste it into any chat model."
                         if lang == "en" else f"共 {len(items)} 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。"),
                        "", f"[English](../en/{key}.md) · [中文](../zh/{key}.md) · "
                        + (f"[Search and copy online]({online})" if lang == "en" else f"[在线搜索复制]({online})"), ""]
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
    block = [
        "<!-- library:start (generated by scripts/build_library.py) -->",
        "## Prompt Library · 提示词库", "",
        f"**{len(rows):,} everyday prompts** for writing, coding, marketing, study, design and more. "
        f"{both:,} come in both English and Chinese; open the column for your language. "
        "Search and copy them in the [online gallery](https://agentcraft.dev/en/prompts/).", "",
        f"**{len(rows):,} 条日常提示词**，覆盖写作、编程、营销、学习、设计等场景，其中 {both:,} 条中英双语，"
        "点你要的语言那一列即可。也可以在[在线画廊](https://agentcraft.dev/zh/prompts/)里搜索、一键复制。", "",
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
        f"- [langgptai/wonderful-prompts](https://github.com/langgptai/wonderful-prompts), MIT, Copyright (c) 2023 yzfly. "
        f"{by_src.get('wonderful-prompts', 0)} original Chinese prompts. License: [LICENSE-wonderful-prompts-MIT.txt](LICENSE-wonderful-prompts-MIT.txt).", "",
        "Categories and the missing-language titles were assigned by a model pass and spot-checked. "
        f"{len(skipped)} prompts were left out as sexual, jailbreak, spam or empty (ids in `skipped.json`).", "",
    ]), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="classify at most N new prompts (for a trial run)")
    a = ap.parse_args()

    en_rows = list(csv.DictReader(io.StringIO(fetch(SOURCES["prompts.chat"][0]))))
    zh_rows = list(csv.DictReader(io.StringIO(fetch(SOURCES["zh-CN"][0]))))
    snap = list(csv.DictReader(io.StringIO(fetch(SOURCES["zh-CN-en"][0]))))
    # zh-CN titles are translated, so pair by row with the English snapshot, then keep a Chinese
    # version only when the upstream English text is unchanged since that snapshot.
    zh_by_act = {s["act"].strip(): (s["prompt"].strip(), z["提示"].strip()) for s, z in zip(snap, zh_rows)}
    wonderful = parse_wonderful(fetch(SOURCES["wonderful-prompts"][0]))

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
    for w in wonderful:
        sid = "zh-" + (slug(w["title"]) or str(abs(hash(w["title"]))))
        if sid in raw:
            sid += "-2"
        raw[sid] = {"id": sid, "title_zh": w["title"], "prompt_en": "", "prompt_zh": w["prompt"],
                    "for_devs": False, "source": "wonderful-prompts", "license": "MIT"}

    old = {}
    if (LIB / "prompts.csv").exists():
        old = {r["id"]: r for r in csv.DictReader(open(LIB / "prompts.csv", encoding="utf-8"))}
    skipped = set(json.loads((LIB / "skipped.json").read_text())) if (LIB / "skipped.json").exists() else set()

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
            r = old[x["id"]]
            r.update({"prompt_en": x["prompt_en"], "prompt_zh": x["prompt_zh"] or r.get("prompt_zh", "")})
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
            "lang": "both" if x["prompt_en"] and x["prompt_zh"] else ("en" if x["prompt_en"] else "zh"),
            "title_en": (lab.get("title_en") or x.get("title_en", "")).strip(),
            "title_zh": (lab.get("title_zh") or x.get("title_zh", "")).strip(),
            "prompt_en": x["prompt_en"], "prompt_zh": x["prompt_zh"],
            "for_devs": "true" if x["for_devs"] else "false", "source": x["source"], "license": x["license"],
        })
    for r in rows:
        r["lang"] = "both" if r["prompt_en"] and r["prompt_zh"] else ("en" if r["prompt_en"] else "zh")

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
    print(f"library: {len(rows)} prompts {by_lang}, skipped {len(skipped)}, unclassified {len(raw) - len(rows) - len(skipped)}")


if __name__ == "__main__":
    main()
