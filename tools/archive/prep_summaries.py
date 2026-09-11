#!/usr/bin/env python3
"""Prepare summary-generation batches from the enriched paper index.

Each batch file holds the inputs an agent needs (key, title, keywords,
abstract) for ~100 papers; agents write tools/out/sum_out/batch_<n>.json with
{key: {motivation, method, conclusion}}.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_SIZE = 100


def main() -> None:
    src = ROOT / "tools" / "out" / "papers_final.json"
    if not src.exists():
        src = ROOT / "tools" / "out" / "papers_enriched.json"
    papers = json.loads(src.read_text(encoding="utf-8"))["papers"]

    batch_dir = ROOT / "tools" / "out" / "sum_batches"
    out_dir = ROOT / "tools" / "out" / "sum_out"
    batch_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in batch_dir.glob("batch_*.json"):
        old.unlink()

    items = []
    for key, paper in papers.items():
        best = paper["best"]
        abstract = best.get("英文摘要", "").strip()
        old_summary = None
        if any(best.get(f) for f in ("研究动机", "研究方法", "结论")):
            old_summary = {
                "动机": best.get("研究动机", ""),
                "方法": best.get("研究方法", ""),
                "结论": best.get("结论", ""),
            }
        if abstract == "未提供":
            abstract = ""
        items.append({
            "key": key,
            "title": paper["title"],
            "keywords": best.get("关键词", ""),
            "abstract": abstract,
            "old_summary": old_summary,
        })

    # papers with abstracts first, then the ones agents must handle from
    # title/keywords alone
    items.sort(key=lambda x: (not x["abstract"], x["key"]))
    n_batches = math.ceil(len(items) / BATCH_SIZE)
    for i in range(n_batches):
        chunk = items[i * BATCH_SIZE:(i + 1) * BATCH_SIZE]
        (batch_dir / f"batch_{i:03d}.json").write_text(
            json.dumps(chunk, ensure_ascii=False, indent=1), encoding="utf-8")
    manifest = {
        "total": len(items),
        "with_abstract": sum(1 for x in items if x["abstract"]),
        "without_abstract": sum(1 for x in items if not x["abstract"]),
        "batches": n_batches,
        "batch_size": BATCH_SIZE,
    }
    (batch_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
