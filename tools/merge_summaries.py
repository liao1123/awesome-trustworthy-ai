#!/usr/bin/env python3
"""Merge per-batch summary outputs into tools/out/summaries.json and report coverage."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    batch_dir = ROOT / "tools" / "out" / "sum_batches"
    out_dir = ROOT / "tools" / "out" / "sum_out"
    merged: dict = {}
    bad_batches: list[str] = []
    done_batches: set[str] = set()

    for path in sorted(out_dir.glob("batch_*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            bad_batches.append(path.name)
            continue
        done_batches.add(path.stem)
        for key, value in data.items():
            if not isinstance(value, dict):
                continue
            merged[key] = {
                "motivation": (value.get("motivation") or "").strip(),
                "method": (value.get("method") or "").strip(),
                "conclusion": (value.get("conclusion") or "").strip(),
            }

    all_batches = {p.stem for p in batch_dir.glob("batch_*.json")}
    missing_batches = sorted(all_batches - done_batches)

    total = 0
    complete = 0
    gaps: list[str] = []
    for path in sorted(batch_dir.glob("batch_*.json")):
        for item in json.loads(path.read_text(encoding="utf-8")):
            total += 1
            s = merged.get(item["key"])
            if s and s["motivation"] and s["method"] and s["conclusion"]:
                complete += 1
            else:
                gaps.append(item["key"])

    (ROOT / "tools" / "out" / "summaries.json").write_text(
        json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "tools" / "out" / "summary_gaps.json").write_text(
        json.dumps(gaps, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({
        "merged": len(merged),
        f"coverage": f"{complete}/{total}",
        "incomplete": len(gaps),
        "batches_done": f"{len(done_batches)}/{len(all_batches)}",
        "missing_batches": missing_batches,
        "bad_batches": bad_batches,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    sys.exit(main())
