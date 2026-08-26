from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROMPTS = ROOT / "prompts"
PROMPT_LINK = re.compile(
    r"https://github\.com/ai-boost/awesome-prompts/blob/main/(prompts/[^)]+)"
)


def main() -> int:
    linked_paths = [unquote(match) for match in PROMPT_LINK.findall(README.read_text(encoding="utf-8"))]
    prompt_paths = {str(path.relative_to(ROOT)) for path in PROMPTS.iterdir() if path.is_file()}
    linked_set = set(linked_paths)
    duplicate_paths = sorted(path for path, count in Counter(linked_paths).items() if count > 1)
    missing_paths = sorted(linked_set - prompt_paths)
    unlisted_paths = sorted(prompt_paths - linked_set)

    problems = []
    if duplicate_paths:
        problems.append(f"Duplicate README prompt links: {', '.join(duplicate_paths)}")
    if missing_paths:
        problems.append(f"README links missing prompt files: {', '.join(missing_paths)}")
    if unlisted_paths:
        problems.append(f"Prompt files missing README entries: {', '.join(unlisted_paths)}")

    if problems:
        for problem in problems:
            print(problem)
        return 1

    print(f"Validated {len(prompt_paths)} unique prompt catalogue entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
