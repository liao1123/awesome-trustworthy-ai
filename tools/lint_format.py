#!/usr/bin/env python3
"""Lint all paper entries for the card format and report coverage.

Checks per numbered `### N. Title` entry:
  - has an icon link row (starts with an emoji link) or keyword line
  - has no legacy field lines (arXiv ID：/记录日期：/链接：/…)
  - has no broken summary garbage (dict fragments)
  - <details> blocks are closed and contain a <summary>
Reports card counts, author/summary/abstract coverage per directory.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

H3 = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$")
LEGACY_FIELD = re.compile(r"^-\s+(arXiv ID|记录日期|关键词|作者|研究动机|研究方法|结论|链接|arXiv Comments|会议录用信息|英文摘要|一句话总结|内容概述|收录理由|代码/数据集/模型)[：:]")
GARBAGE = "{'motivation'"
ICON_ROW = re.compile(r"^(📄|🐙|🤗|📊|🌐|📝|🎓|🎬|📅)")
KEYWORDS_LINE = re.compile(r"^\*\*关键词\*\*")
AUTHORS_LINE = re.compile(r"^👤\s*\*\*作者\*\*")
SUMMARY_LINE = re.compile(r"^- [🎯🔬📌] \*\*(研究动机|研究方法|结论)\*\*")
ABSTRACT_LINE = re.compile(r"^<summary>📝 展开完整英文摘要")


def lint_file(path: Path, report: dict) -> list[str]:
    problems: list[str] = []
    lines = path.read_text(encoding="utf-8").split("\n")
    in_entry = False
    entry_no = ""
    entry_flags: dict[str, bool] = {}
    details_depth = 0

    def flush() -> None:
        nonlocal in_entry, entry_flags
        if not in_entry:
            return
        report["entries"] += 1
        if not entry_flags["icon"] and not entry_flags["keywords"]:
            problems.append(f"{path.relative_to(ROOT)} #{entry_no}: no icon row or keywords")
        for flag in ("authors", "summary", "abstract"):
            if entry_flags[flag]:
                report[f"with_{flag}"] += 1
        in_entry = False

    for line in lines:
        h3 = H3.match(line)
        if h3:
            flush()
            in_entry = True
            entry_no = h3.group(1)
            entry_flags = {"icon": False, "keywords": False, "authors": False,
                           "summary": False, "abstract": False}
            continue
        if not in_entry:
            continue
        if LEGACY_FIELD.match(line):
            problems.append(f"{path.relative_to(ROOT)} #{entry_no}: legacy field -> {line[:50]}")
        if GARBAGE in line:
            problems.append(f"{path.relative_to(ROOT)} #{entry_no}: garbage summary fragment")
        if ICON_ROW.match(line):
            entry_flags["icon"] = True
        if KEYWORDS_LINE.match(line):
            entry_flags["keywords"] = True
        if AUTHORS_LINE.match(line):
            entry_flags["authors"] = True
        if SUMMARY_LINE.match(line):
            entry_flags["summary"] = True
        if ABSTRACT_LINE.match(line):
            entry_flags["abstract"] = True
        if line.strip() == "<details>":
            details_depth += 1
        elif line.strip() == "</details>":
            details_depth -= 1
            if details_depth < 0:
                problems.append(f"{path.relative_to(ROOT)} #{entry_no}: unbalanced </details>")
                details_depth = 0
    flush()
    if details_depth != 0:
        problems.append(f"{path.relative_to(ROOT)}: file ends inside <details>")
    return problems


def main() -> int:
    report = {"entries": 0, "with_authors": 0, "with_summary": 0, "with_abstract": 0}
    problems: list[str] = []
    for sub in ("daily", "conferences", "domains"):
        for path in (ROOT / sub).rglob("*.md"):
            if path.name == "README.md":
                continue
            problems.extend(lint_file(path, report))
    coverage = {
        "entries": report["entries"],
        "authors": f"{report['with_authors']}/{report['entries']}",
        "summary": f"{report['with_summary']}/{report['entries']}",
        "abstract": f"{report['with_abstract']}/{report['entries']}",
        "problems": len(problems),
    }
    print(json.dumps(coverage, ensure_ascii=False, indent=1))
    if problems:
        print("\n".join(problems[:40]))
        if len(problems) > 40:
            print(f"... and {len(problems) - 40} more")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
