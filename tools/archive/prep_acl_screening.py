#!/usr/bin/env python3
"""Prepare screening batches for ACL Findings candidates.

Each item carries pid/title/authors/abstract/arxiv; agents return
{pid: {"include": bool, "section": str, "reason": str,
        "motivation": str, "method": str, "conclusion": str}}.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = 80


def main() -> None:
    abstracts = json.loads((ROOT / "tools" / "out" / "acl_findings_abstracts.json").read_text(encoding="utf-8"))
    candidates = json.loads((ROOT / "tools" / "out" / "acl_findings_candidates.json").read_text(encoding="utf-8"))
    by_pid = {c["pid"]: c for c in candidates}

    items = []
    for pid, rec in abstracts.items():
        c = by_pid.get(pid, {})
        items.append({
            "pid": pid,
            "title": c.get("title") or rec.get("title", ""),
            "abstract": rec.get("abstract", ""),
            "arxiv": rec.get("arxiv", ""),
        })
    items.sort(key=lambda x: (not x["abstract"], x["pid"]))

    out_dir = ROOT / "tools" / "out" / "acl_screen_batches"
    out_dir.mkdir(parents=True, exist_ok=True)
    res_dir = ROOT / "tools" / "out" / "acl_screen_out"
    res_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("batch_*.json"):
        old.unlink()

    n = math.ceil(len(items) / BATCH) if items else 0
    for i in range(n):
        (out_dir / f"batch_{i:02d}.json").write_text(
            json.dumps(items[i * BATCH:(i + 1) * BATCH], ensure_ascii=False, indent=1), encoding="utf-8")
    manifest = {"total": len(items),
                "with_abstract": sum(1 for x in items if x["abstract"]),
                "batches": n, "batch_size": BATCH}
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
