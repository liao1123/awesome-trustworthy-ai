#!/usr/bin/env python3
"""Join the master paper index against local metadata caches and report gaps.

Produces tools/out/papers_enriched.json where every paper record carries the
best-known authors / abstract / date, marking what still needs fetching.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import normalize_title  # noqa: E402


def load_cache() -> dict:
    path = ROOT / "reader" / "data" / "arxiv_metadata.json"
    return json.loads(path.read_text(encoding="utf-8"))


def valid_abstract(value: str | None) -> bool:
    return bool(value) and value not in ("未提供", "None", "") and len(value) > 80


def valid_authors(value: str | None) -> bool:
    return bool(value) and "暂无" not in value and "未提供" not in value


def main() -> None:
    index = json.loads((ROOT / "tools" / "out" / "papers_index.json").read_text(encoding="utf-8"))
    cache = load_cache()

    by_title_cache = {}
    for pid, meta in cache.items():
        if meta.get("title"):
            by_title_cache.setdefault(normalize_title(meta["title"]), pid)

    papers = index["papers"]
    stats = {"unique": len(papers), "cache_hit_arxiv": 0, "cache_hit_title": 0,
             "need_fetch": [], "need_authors_only": [], "ok": 0}

    for key, paper in papers.items():
        meta = None
        pid = paper.get("arxiv_id")
        if pid and pid in cache:
            meta = cache[pid]
            stats["cache_hit_arxiv"] += 1
        else:
            nt = normalize_title(paper["title"])
            if nt in by_title_cache:
                pid = by_title_cache[nt]
                meta = cache[pid]
                paper["arxiv_id"] = pid
                stats["cache_hit_title"] += 1

        authors, abstract, date = None, None, None
        if meta:
            raw_authors = meta.get("authors")
            if isinstance(raw_authors, list) and raw_authors:
                authors = "；".join(raw_authors)
            if valid_abstract(meta.get("abstract")):
                abstract = meta["abstract"].strip()
            if meta.get("submitted"):
                date = str(meta["submitted"])[:7]

        best = paper["best"]
        if not valid_authors(best.get("作者")) and valid_authors(authors):
            best["作者"] = authors
        if not valid_abstract(best.get("英文摘要")) and valid_abstract(abstract):
            best["英文摘要"] = abstract
        if not best.get("记录日期") and date:
            best["记录日期"] = date
        if meta and meta.get("comments") and not best.get("arXiv Comments"):
            best["arXiv Comments"] = str(meta["comments"])

        has_all = valid_authors(best.get("作者")) and valid_abstract(best.get("英文摘要"))
        if has_all:
            stats["ok"] += 1
        elif paper.get("arxiv_id"):
            (stats["need_authors_only"] if valid_authors(best.get("作者")) else stats["need_fetch"]).append(key)
        else:
            stats["need_fetch"].append(key)

    stats["need_fetch_count"] = len(stats["need_fetch"])
    stats["need_authors_only_count"] = len(stats["need_authors_only"])
    out = {"stats": {k: v for k, v in stats.items() if not isinstance(v, list)},
           "papers": papers}
    (ROOT / "tools" / "out" / "papers_enriched.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out["stats"], ensure_ascii=False, indent=1))
    # persist the fetch lists for the next step
    (ROOT / "tools" / "out" / "need_fetch.json").write_text(
        json.dumps({"need_fetch": stats["need_fetch"], "need_authors_only": stats["need_authors_only"]},
                   ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
