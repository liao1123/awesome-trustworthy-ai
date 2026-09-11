#!/usr/bin/env python3
"""Reconcile the three summary bullet lines in every card with the canonical
summaries.json (which later quality passes may have improved).

Only edits cards whose paper key resolves exactly (arXiv link in card or
exact normalized-title alias) and that already carry all three summary lines;
keywords/authors/links/abstract are never touched.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import normalize_title  # noqa: E402

H3 = re.compile(r"^### (\d+)\. (.+)$")
SUMMARY_LINE = re.compile(r"^(- [🎯🔬📌] \*\*(?:研究动机|研究方法|结论)\*\*：)(.*)$")
ARXIV_URL = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")

LABELS = [("🎯", "研究动机", "motivation"), ("🔬", "研究方法", "method"), ("📌", "结论", "conclusion")]


def render_lines(summary: dict) -> dict[str, str]:
    out = {}
    for icon, label, field in LABELS:
        value = (summary.get(field) or "").strip().rstrip("。").strip()
        out[label] = f"- {icon} **{label}**：{value}" if value else ""
    return out


def main() -> None:
    final = json.loads((ROOT / "tools" / "out" / "papers_final.json").read_text(encoding="utf-8"))["papers"]
    summaries = json.loads((ROOT / "tools" / "out" / "summaries.json").read_text(encoding="utf-8"))
    alias = {}
    for key, paper in final.items():
        for t in paper.get("titles", []):
            alias.setdefault(normalize_title(t), key)

    updated_cards = 0
    updated_lines = 0
    skipped = 0
    for sub in ("daily", "conferences", "domains"):
        for path in (ROOT / sub).rglob("*.md"):
            if path.name == "README.md":
                continue
            lines = path.read_text(encoding="utf-8").split("\n")
            out: list[str] = []
            i = 0
            changed = False
            while i < len(lines):
                m = H3.match(lines[i])
                if not m:
                    out.append(lines[i])
                    i += 1
                    continue
                title = m.group(2).strip()
                j = i + 1
                block: list[str] = []
                while j < len(lines) and not lines[j].startswith("#"):
                    block.append(lines[j])
                    j += 1
                # resolve key exactly
                block_text = "\n".join(block)
                am = ARXIV_URL.search(block_text)
                if am:
                    key = am.group(1)
                else:
                    key = alias.get(normalize_title(title), "")
                summary = summaries.get(key) if key else None
                existing = {re.match(r"- [🎯🔬📌] \*\*(研究动机|研究方法|结论)\*\*：", line).group(1): line
                            for line in block
                            if re.match(r"- [🎯🔬📌] \*\*(研究动机|研究方法|结论)\*\*：", line)}
                if summary and len(existing) == 3:
                    wanted = render_lines(summary)
                    card_changed = False
                    new_block: list[str] = []
                    for line in block:
                        sm = re.match(r"- [🎯🔬📌] \*\*(研究动机|研究方法|结论)\*\*：", line)
                        if sm:
                            label = sm.group(1)
                            if wanted.get(label) and wanted[label] != line:
                                new_block.append(wanted[label])
                                updated_lines += 1
                                card_changed = True
                            else:
                                new_block.append(line)
                        else:
                            new_block.append(line)
                    block = new_block
                    if card_changed:
                        updated_cards += 1
                        changed = True
                elif not summary:
                    skipped += 1
                out.append(lines[i])
                out.extend(block)
                i = j
            if changed:
                path.write_text("\n".join(out), encoding="utf-8")
    print(json.dumps({"cards_updated": updated_cards, "lines_updated": updated_lines, "unresolved_cards": skipped}))


if __name__ == "__main__":
    main()
