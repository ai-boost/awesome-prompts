"""Build the Hugging Face dataset from this repo.

Two subsets:
  engineering  prompts/ files linked from README tables, with category,
               description, cited arXiv papers and GitHub sources. CC-BY-4.0.
  library      library/prompts.csv, the bilingual everyday library. Per-row license.

Left out: the README "Legacy" section and prompts/claude_artifacts_prompt.md (third-party
text), and library rows quoted from DeepSeek (attribution-only, not redistributable).

Writes <out>/data/{engineering,library}.parquet, <out>/README.md (dataset card) and the
library license files. Upload with:
  huggingface-cli upload Adrian2016/awesome-prompts <out> . --repo-type dataset
Usage: python3 scripts/build_hf_dataset.py [--out dist/hf] [--repo Adrian2016/awesome-prompts]
"""
import argparse
import collections
import csv
import pathlib
import re
import shutil
import urllib.parse

import pyarrow as pa
import pyarrow.parquet as pq

ROOT = pathlib.Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/ai-boost/awesome-prompts"
EXCLUDED_SECTIONS = {"Legacy (2023 era — kept for reference)"}
EXCLUDED_FILES = {"claude_artifacts_prompt.md"}
EXCLUDED_LIBRARY_SOURCES = {"DeepSeek"}

ARXIV = re.compile(r"arxiv(?:\.org/(?:abs|pdf)/|[\s:]*)(\d{4}\.\d{4,5})", re.I)
GH_URL = re.compile(r"github\.com/([A-Za-z0-9-]+/[A-Za-z0-9._-]+?)(?=[\s/)\],;:'\"`]|\.?$|\.\s)", re.M)
GH_BASED_ON = re.compile(r"\b(?:based on|Source:)\s+([A-Za-z0-9-]+/[A-Za-z0-9._-]+?)(?=[\s,;()]|$)")
LEADING_EMOJI = re.compile(r"^[^\w(]+", re.U)
CJK = re.compile(r"[一-鿿]")


def readme_rows():
    """Yield (category, name, description, filename) for every README table row linking a prompt.

    The category is the ### heading, or the ## heading when the ### is just "Prompts".
    """
    h2 = h3 = None
    for line in (ROOT / "README.md").read_text().splitlines():
        if line.startswith("## "):
            h2, h3 = line[3:].strip(), None
            continue
        if line.startswith("### "):
            h3 = line[4:].strip()
            continue
        section = h2 if h3 in (None, "Prompts") else h3
        m = re.search(r"\[prompt\]\(" + re.escape(GITHUB) + r"/blob/main/prompts/([^)]+)\)\s*\|\s*$", line)
        if not m:
            continue
        cells = line.strip().strip("|").split("|")
        name = cells[0].strip()
        description = "|".join(cells[1:-1]).strip()
        yield section, name, description, urllib.parse.unquote(m.group(1))


def unique(items):
    return list(dict.fromkeys(items))


def github_repos(text):
    repos = GH_URL.findall(text) + GH_BASED_ON.findall(text)
    return unique(r.rstrip(".") for r in repos if not r.startswith("ai-boost/"))


def engineering_rows():
    rows, seen, linked = [], set(), set()
    for category, name, description, filename in readme_rows():
        linked.add(filename)
        if category in EXCLUDED_SECTIONS or filename in EXCLUDED_FILES or filename in seen:
            continue
        seen.add(filename)
        prompt = (ROOT / "prompts" / filename).read_text().strip()
        both = description + "\n" + prompt
        rows.append({
            "id": pathlib.Path(filename).stem,
            "name": LEADING_EMOJI.sub("", name).strip(),
            "category": category,
            "description": description,
            "prompt": prompt,
            "lang": "zh" if len(CJK.findall(prompt)) > len(prompt) * 0.1 else "en",
            "arxiv_ids": unique(ARXIV.findall(both)),
            "github_repos": github_repos(both),
            "url": f"{GITHUB}/blob/main/prompts/{urllib.parse.quote(filename)}",
        })
    missing = {p.name for p in (ROOT / "prompts").iterdir()} - linked
    return rows, missing


def library_rows():
    csv.field_size_limit(10**9)
    with open(ROOT / "library" / "prompts.csv", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["source"] not in EXCLUDED_LIBRARY_SOURCES]
    for r in rows:
        r["for_devs"] = r["for_devs"].strip().lower() in {"true", "1", "yes"}
    return rows


def write_parquet(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(pa.Table.from_pylist(rows), path)


def card(repo, eng, lib):
    n_paper = sum(1 for r in eng if r["arxiv_ids"])
    n_repo = sum(1 for r in eng if r["github_repos"])
    papers = len({a for r in eng for a in r["arxiv_ids"]})
    cats = collections.Counter(r["category"] for r in eng).most_common()
    cat_table = "\n".join(f"| {c} | {n} |" for c, n in cats)
    lib_cats = collections.Counter(r["category"] for r in lib).most_common()
    lib_table = "\n".join(f"| {c} | {n} |" for c, n in lib_cats)
    lic = collections.Counter(r["license"] for r in lib).most_common()
    lic_list = ", ".join(f"{l} ({n})" for l, n in lic)
    both = sum(1 for r in lib if not r["translated"])
    return f"""---
license:
- cc-by-4.0
- cc0-1.0
- mit
- apache-2.0
language:
- en
- zh
pretty_name: Awesome Prompts
size_categories:
- 1K<n<10K
task_categories:
- text-generation
tags:
- prompts
- system-prompts
- prompt-engineering
- agents
configs:
- config_name: engineering
  data_files: data/engineering.parquet
  default: true
- config_name: library
  data_files: data/library.parquet
---

# Awesome Prompts

Prompts from [ai-boost/awesome-prompts]({GITHUB}), in two subsets:

- **engineering**: {len(eng)} system prompts for agents, coding, research and safety work. {n_paper} of them cite arXiv papers by id ({papers} papers in all), and {n_repo} link the open-source projects they draw on.
- **library**: {len(lib)} everyday prompts for writing, marketing, study and design, each in English and Chinese.

```python
from datasets import load_dataset

eng = load_dataset("{repo}", "engineering", split="train")
lib = load_dataset("{repo}", "library", split="train")
```

## engineering

Each prompt is a full system prompt written to put one paper, product or practice to work, such as a Lean 4 theorem prover built from Goedel-Architect, or a coding agent following OpenAI's Codex prompting guide.

| Field | Meaning |
|---|---|
| `id` | File name in the GitHub repo, without extension |
| `name` | Display name |
| `category` | Section of the GitHub README |
| `description` | One-line summary, usually naming the source and date |
| `prompt` | Full prompt text |
| `lang` | `en` or `zh` |
| `arxiv_ids` | arXiv ids cited in the description or prompt |
| `github_repos` | `owner/repo` of open-source projects it is based on |
| `url` | Source file on GitHub |

| Category | Prompts |
|---|---|
{cat_table}

## library

Collected from prompts.chat and Chinese prompt projects, then categorized and given titles in both languages. {both} rows have both versions written by people. In the other {len(lib) - both}, the language named in `translated` was machine translated.

Columns: `id`, `category`, `lang` (language of the original: `en`, `zh` or `both`), `title_en`, `title_zh`, `prompt_en`, `prompt_zh`, `translated`, `for_devs`, `source`, `license`.

| Category | Prompts |
|---|---|
{lib_table}

## How it was made

The engineering prompts are written and maintained in the GitHub repo, mostly in 2025 and 2026. `arxiv_ids` and `github_repos` are pulled from the text with regular expressions, so a prompt that names a paper without an id has an empty list. Two kinds of prompts are left out: 2023-era prompts by other authors, and a copied vendor system prompt.

The library comes from the sources listed in the GitHub repo's [library/README.md]({GITHUB}/blob/main/library/README.md). Prompts that were sexual, jailbreaks, spam or empty were removed before categorizing, and DeepSeek's official examples are left out because they are quoted, not licensed.

## Uses and limits

Good for: starting points for system prompts, examples for prompt-optimization research, and a bilingual set for testing how models follow instructions in English and Chinese.

Limits: no prompt here has been benchmarked. The citations show which paper a prompt draws on, but do not show that the prompt reproduces the paper's results. Machine-translated library rows can read stiffly.

## License

- engineering: CC-BY-4.0. Credit "ai-boost/awesome-prompts".
- library: per row, in the `license` column: {lic_list}. MIT and Apache-2.0 license texts are in `licenses/`.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist" / "hf"))
    ap.add_argument("--repo", default="Adrian2016/awesome-prompts")
    args = ap.parse_args()
    out = pathlib.Path(args.out)

    eng, missing = engineering_rows()
    if missing:
        print("not linked from README, skipped:", sorted(missing))
    lib = library_rows()

    write_parquet(eng, out / "data" / "engineering.parquet")
    write_parquet(lib, out / "data" / "library.parquet")
    (out / "licenses").mkdir(parents=True, exist_ok=True)
    for f in (ROOT / "library").glob("LICENSE-*.txt"):
        shutil.copy(f, out / "licenses" / f.name)
    (out / "README.md").write_text(card(args.repo, eng, lib))
    print(f"engineering {len(eng)}, library {len(lib)} -> {out}")


if __name__ == "__main__":
    main()
