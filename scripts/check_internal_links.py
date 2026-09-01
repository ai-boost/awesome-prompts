#!/usr/bin/env python3
"""Check repository-owned Markdown links in the public index files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


INDEX_FILES = ("README.md", "GPT_STORE.md")
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^\s)]+)(?:\s+[^)]*)?\)")
REPOSITORY_PREFIX = "/ai-boost/awesome-prompts/"


def repository_target(raw_target: str) -> str | None:
    """Return a repository-relative target, or None for external links/anchors."""
    parsed = urlsplit(raw_target)
    path = unquote(parsed.path)

    if parsed.scheme or parsed.netloc:
        if parsed.scheme not in {"http", "https"}:
            return None
        if parsed.netloc.lower() != "github.com":
            return None
        if not path.startswith(REPOSITORY_PREFIX):
            return None
        path = path[len(REPOSITORY_PREFIX) :]
        kind, separator, path = path.partition("/")
        if kind not in {"blob", "tree"} or not separator:
            return None
        branch, separator, path = path.partition("/")
        if branch != "main" or not separator:
            return None
    elif not path:
        return None

    return path


def check_file(root: Path, filename: str) -> tuple[int, list[str]]:
    path = root / filename
    failures: list[str] = []
    checked = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in MARKDOWN_LINK.finditer(line):
            label, raw_target = match.groups()
            target = repository_target(raw_target)
            if target is None:
                continue
            checked += 1

            target_path = (root / target).resolve()
            try:
                target_path.relative_to(root.resolve())
            except ValueError:
                failures.append(
                    f"{filename}:{line_number}: [{label}] -> {target} escapes the repository"
                )
                continue

            if not target_path.exists():
                failures.append(
                    f"{filename}:{line_number}: [{label}] -> {target} does not exist"
                )
    return checked, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="repository root (default: current directory)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    checked = 0
    failures: list[str] = []
    for filename in INDEX_FILES:
        file_checked, file_failures = check_file(root, filename)
        checked += file_checked
        failures.extend(file_failures)

    if failures:
        print("Internal link check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Checked {checked} repository-owned links in {', '.join(INDEX_FILES)}: all targets exist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
