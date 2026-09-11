#!/usr/bin/env python3
"""Aggregate domain-review wave outputs into a final action list.

Checks:
  - totals per verdict
  - cross-file consistency: same title removed in one file but kept in another
  - move targets: whether the title already exists in the target file
Writes tools/out/domain_review/FINAL_ACTIONS.md + final_actions.json
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
REV = ROOT / "tools" / "out" / "domain_review"


def main() -> None:
    waves = {}
    for p in sorted(REV.glob("wave*_*.json")):
        waves.update(json.loads(p.read_text(encoding="utf-8")))

    # collect entries and per-title verdicts across files
    per_title: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    counts = Counter()
    for path, entries in waves.items():
        for e in entries:
            counts[e["verdict"]] += 1
            per_title[e["title"]].append((path, e))

    conflicts = []
    for title, occurrences in per_title.items():
        verdicts = {e["verdict"] for _, e in occurrences}
        if "remove" in verdicts and len(verdicts) > 1:
            conflicts.append((title, [(p, e["verdict"]) for p, e in occurrences]))
        if "borderline" in verdicts and verdicts != {"borderline"}:
            conflicts.append((title, [(p, e["verdict"]) for p, e in occurrences]))

    # move targets vs existing content
    move_report = []
    file_texts = {str(p.relative_to(ROOT)): p.read_text(encoding="utf-8")
                  for p in (ROOT / "domains").rglob("*.md")}
    for path, entries in waves.items():
        for e in entries:
            if e["verdict"] == "move":
                target = e.get("target", "")
                already = ""
                if target in file_texts:
                    already = "目标已有(应删此处)" if e["title"] in file_texts[target] else "目标无(应迁移)"
                else:
                    already = "目标文件不存在"
                move_report.append((path, e["title"], target, already, e.get("note", "")))

    lines = ["# domains/ 审查最终待执行清单", ""]
    lines.append(f"- 审查条目总数: {sum(counts.values())}（{len(waves)} 个文件）")
    lines.append(f"- 判定分布: {dict(counts)}")
    lines.append(f"- 跨文件冲突: {len(conflicts)} 条")
    lines.append("")

    lines.append("## 一、删除清单（remove，每条对应排除条款）")
    lines.append("")
    cur = None
    for path, entries in sorted(waves.items()):
        for e in entries:
            if e["verdict"] == "remove":
                if path != cur:
                    lines.append(f"### {path}")
                    cur = path
                lines.append(f"- **{e['title']}**")
                lines.append(f"  - 条款: {e.get('rule', '')}")
                lines.append(f"  - 依据: {e.get('note', '')}")
    lines.append("")

    lines.append("## 二、迁移清单（move）")
    lines.append("")
    for path, title, target, status, note in sorted(move_report):
        lines.append(f"- {title}")
        lines.append(f"  - {path} → {target} [{status}]")
        lines.append(f"  - {note}")
    lines.append("")

    lines.append("## 三、跨文件冲突（同一论文不同判定，需人工统一）")
    lines.append("")
    for title, occ in conflicts:
        lines.append(f"- **{title}**: " + "; ".join(f"{p.split('/')[-1]}={v}" for p, v in occ))
    lines.append("")

    lines.append("## 四、边界待裁决（borderline）")
    lines.append("")
    for path, entries in sorted(waves.items()):
        for e in entries:
            if e["verdict"] == "borderline":
                lines.append(f"- **{e['title']}** ({path.split('/')[-1]}): {e.get('note', '')}")
    lines.append("")

    (REV / "FINAL_ACTIONS.md").write_text("\n".join(lines), encoding="utf-8")
    json.dump({"counts": dict(counts),
               "conflicts": [{"title": t, "occ": o} for t, o in conflicts],
               "moves": move_report},
              (REV / "final_actions.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({"total": sum(counts.values()), "counts": dict(counts),
                      "conflicts": len(conflicts), "moves": len(move_report)}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
