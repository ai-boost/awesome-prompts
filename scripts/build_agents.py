#!/usr/bin/env python3
"""Build GitHub Copilot custom agents from the prompts/ directory.

Regenerates .github/agents/<name>.md for every .txt/.md file in prompts/:
- name: kebab-case filename (emojis/non-ASCII stripped)
- description: derived from the first "You are ..." line or first meaningful line
- body: the original prompt, verbatim

Usage: python scripts/build_agents.py
"""

import os
import re
import sys
import unicodedata

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "prompts")
DST = os.path.join(REPO, ".github", "agents")


def kebab(stem: str) -> str:
    s = unicodedata.normalize("NFKD", stem)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "prompt"


def derive_description(text: str, fallback: str) -> str:
    lines = [l.strip() for l in text.splitlines()]
    for l in lines[:40]:
        if re.match(r"(?i)^you are\b", l):
            desc = l
            break
    else:
        desc = ""
        for l in lines:
            if not l:
                continue
            t = re.sub(r"^#{1,6}\s*", "", l)
            t = t.strip("* _`>")
            if not t:
                continue
            if re.match(r"(?i)^sources?:", t):
                continue
            if re.match(r"^[-=~_]{3,}$", t):
                continue
            desc = t
            break
        if not desc:
            desc = fallback
    desc = re.sub(r"[*_`]", "", desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    if len(desc) > 200:
        desc = desc[:197].rsplit(" ", 1)[0] + "..."
    return desc


def main() -> int:
    os.makedirs(DST, exist_ok=True)

    # remove stale agents so deletes/renames in prompts/ propagate
    for f in os.listdir(DST):
        if f.endswith(".md"):
            os.remove(os.path.join(DST, f))

    seen = {}
    count = 0
    errors = []

    for fname in sorted(os.listdir(SRC)):
        path = os.path.join(SRC, fname)
        if not os.path.isfile(path):
            continue
        stem, ext = os.path.splitext(fname)
        if ext.lower() not in (".txt", ".md"):
            errors.append(f"skipped (unsupported extension): {fname}")
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                body = f.read()
        except Exception as e:  # noqa: BLE001
            errors.append(f"read failed {fname}: {e}")
            continue

        name = kebab(stem)
        if name in seen:
            seen[name] += 1
            name = f"{name}-{seen[name]}"
        else:
            seen[name] = 1

        title_fallback = re.sub(r"[_-]+", " ", stem).strip()
        desc = derive_description(body, title_fallback)
        desc_yaml = desc.replace("\\", "\\\\").replace('"', '\\"')

        fm = f'---\nname: {name}\ndescription: "{desc_yaml}"\n---\n\n'
        out = os.path.join(DST, name + ".md")
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(fm + body.rstrip() + "\n")
        count += 1

    print(f"built {count} agents -> {os.path.relpath(DST, REPO)}")
    if errors:
        print("ERRORS:")
        for e in errors:
            print(" ", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
