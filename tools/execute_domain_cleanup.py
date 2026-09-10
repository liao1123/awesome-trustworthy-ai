#!/usr/bin/env python3
"""Batch A of domain cleanup: execute removals, cut move-out cards, renumber.

- remove verdict -> delete entry (with explicit exclusion clause in review data)
- move verdict where target already contains the title -> delete entry (redundant copy)
- conflict resolutions -> delete the two LLM-judge papers everywhere
- move verdict (true migration) -> cut card from source, save to pending_moves/
- borderline -> keep untouched (per RESEARCH_INTERESTS review rule)

Renumber ### N. entries sequentially within each file afterwards.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
REV = ROOT / "tools" / "out" / "domain_review"
PENDING = REV / "pending_moves"

CONFLICT_REMOVE = {
    "Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation",
    "The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment",
}

H3 = re.compile(r"^### \d+\. (.+)$")


def main() -> None:
    waves = {}
    for p in sorted(REV.glob("wave*_*.json")):
        waves.update(json.loads(p.read_text(encoding="utf-8")))

    PENDING.mkdir(exist_ok=True)
    stats = defaultdict(int)
    pending: dict[str, list] = defaultdict(list)

    for rel_path, entries in waves.items():
        verdicts = {e["title"]: e for e in entries}
        path = ROOT / rel_path
        lines = path.read_text(encoding="utf-8").split("\n")

        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            m = H3.match(line)
            if m:
                title = m.group(1).strip()
                j = i + 1
                while j < len(lines) and not lines[j].startswith("#"):
                    j += 1
                block = "\n".join(lines[i:j]).rstrip()
                v = verdicts.get(title, {})
                verdict = v.get("verdict", "keep")
                if verdict == "remove" or title in CONFLICT_REMOVE:
                    stats["removed"] += 1
                elif verdict == "move":
                    target = v.get("target", "")
                    target_text = ""
                    tp = ROOT / target if target else None
                    if tp and tp.exists():
                        target_text = tp.read_text(encoding="utf-8")
                    if target and title in target_text:
                        stats["dup_deleted"] += 1
                    else:
                        pending[target].append({"title": title, "card": block})
                        stats["cut_for_move"] += 1
                else:
                    out.append(block)
                    out.append("")
                i = j
                continue
            out.append(line)
            i += 1

        # renumber
        n = 0
        for idx, el in enumerate(out):
            mm = re.match(r"^### \d+\. (.+)$", el.split("\n", 1)[0]) if isinstance(el, str) else None
            if mm:
                n += 1
                first, rest = (el.split("\n", 1) + [""])[:2]
                out[idx] = f"### {n}. {mm.group(1)}" + ("\n" + rest if rest else "")
        new_text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(out))
        path.write_text(new_text, encoding="utf-8")
        stats[f"files_done"] += 1

    for target, cards in pending.items():
        safe = target.replace("/", "__").replace(".md", ".json")
        (PENDING / safe).write_text(json.dumps(cards, ensure_ascii=False, indent=1), encoding="utf-8")
    (REV / "batch_a_stats.json").write_text(json.dumps(dict(stats), ensure_ascii=False), encoding="utf-8")
    print(json.dumps(dict(stats), ensure_ascii=False))
    print(f"pending move files: {len(pending)}")


if __name__ == "__main__":
    sys.exit(main())
