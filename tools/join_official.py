#!/usr/bin/env python3
"""Post-fetch join: merge official/supplemental metadata caches into papers_final.json.

official_metadata.json is keyed by canonical URL (with authors); supplemental
is keyed by DOI/URL (abstract only).  Runs AFTER tools/fetch_missing.py has
finished, since both write papers_final.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import normalize_title  # noqa: E402


def valid_authors(v: str | None) -> bool:
    return bool(v) and "暂无" not in v and "未提供" not in v


def valid_abstract(v: str | None) -> bool:
    return bool(v) and v not in ("未提供", "None") and len(v) > 80


def main() -> None:
    final_path = ROOT / "tools" / "out" / "papers_final.json"
    papers = json.loads(final_path.read_text(encoding="utf-8"))["papers"]

    official: dict = {}
    path = ROOT / "reader" / "data" / "official_metadata.json"
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        for url, meta in raw.items():
            official[url.rstrip("/")] = meta
            if meta.get("title"):
                official.setdefault("t:" + normalize_title(meta["title"]), meta)

    supplemental: dict = {}
    path = ROOT / "reader" / "data" / "supplemental_metadata.json"
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        for key, meta in raw.items():
            supplemental[key.rstrip("/")] = meta
            if meta.get("title"):
                supplemental.setdefault("t:" + normalize_title(meta["title"]), meta)

    stats = {"authors_filled": 0, "abstract_filled": 0}
    for paper in papers.values():
        best = paper["best"]
        candidates = []
        for link in best.get("links", []):
            candidates.append(official.get(link["url"].rstrip("/")))
        candidates.append(official.get("t:" + normalize_title(paper["title"])))
        candidates.append(supplemental.get("t:" + normalize_title(paper["title"])))
        for meta in candidates:
            if not meta:
                continue
            if not valid_authors(best.get("作者")) and meta.get("authors"):
                raw = meta["authors"]
                if isinstance(raw, list):
                    best["作者"] = "；".join(raw)
                else:
                    best["作者"] = str(raw)
                stats["authors_filled"] += 1
            if not valid_abstract(best.get("英文摘要")) and valid_abstract(meta.get("abstract")):
                best["英文摘要"] = str(meta["abstract"]).strip()
                stats["abstract_filled"] += 1

    final_path.write_text(json.dumps({"papers": papers}, ensure_ascii=False, indent=1), encoding="utf-8")
    missing_authors = sum(1 for p in papers.values() if not valid_authors(p["best"].get("作者")))
    missing_abstract = sum(1 for p in papers.values() if not valid_abstract(p["best"].get("英文摘要")))
    print(json.dumps({**stats, "still_missing_authors": missing_authors,
                      "still_missing_abstract": missing_abstract}, ensure_ascii=False))


if __name__ == "__main__":
    main()
