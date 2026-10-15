#!/usr/bin/env python3
"""Backfill abstracts via export.arxiv.org API for entries parsed from /recent.

Usage: daily_backfill_abstracts.py <TAG> <monthPrefix>
  e.g. daily_backfill_abstracts.py 1015 2610

Reads out/daily_<TAG>_entries_recent.json, fetches abstracts for new-month
candidates in id_list batches of 100 (>=10s apart, long backoff on 429),
merges them, and writes the standard out/daily_<TAG>_entries.json +
daily_<TAG>_meta.json consumed by the screening pipeline.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out"
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch_batch(ids: list[str]) -> str | None:
    url = "https://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=100"
    for attempt in range(1, 4):
        r = subprocess.run(
            ["curl", "-sS", "-L", "--max-time", "120",
             "-w", "\n__HTTP__%{http_code}", url],
            capture_output=True, text=True, timeout=150)
        body = r.stdout
        if r.returncode == 0 and body.endswith("__HTTP__200"):
            return body.rsplit("__HTTP__", 1)[0]
        code = body[-64:]
        print(f"batch attempt {attempt} failed rc={r.returncode} tail={code!r}", flush=True)
        if "429" in code:
            print("HTTP 429 -> long backoff 20min", flush=True)
            time.sleep(1200)
        else:
            time.sleep(60)
    return None


def main() -> None:
    tag, month = sys.argv[1], sys.argv[2]
    entries = json.loads((OUT / f"daily_{tag}_entries_recent.json").read_text(encoding="utf-8"))
    cands = sorted(pid for pid in entries if pid.startswith(month + "."))
    print(f"candidates to backfill: {len(cands)}")
    abstracts: dict[str, dict] = {}
    for i in range(0, len(cands), 100):
        batch = cands[i:i + 100]
        xml = fetch_batch(batch)
        if xml is None:
            print(f"batch {i//100} FAILED, entries keep empty abstracts", flush=True)
            continue
        root = ET.fromstring(xml)
        for e in root.findall(f"{ATOM}entry"):
            pid = (e.findtext(f"{ATOM}id") or "").rsplit("/abs/", 1)[-1]
            pid = re.sub(r"v\d+$", "", pid)
            abstracts[pid] = {
                "abstract": " ".join((e.findtext(f"{ATOM}summary") or "").split()),
                "title": " ".join((e.findtext(f"{ATOM}title") or "").split()),
                "authors": [a.findtext(f"{ATOM}name") or "" for a in e.findall(f"{ATOM}author")],
            }
        print(f"batch {i//100}: +{len(abstracts)} cumulative abstracts", flush=True)
        if i + 100 < len(cands):
            time.sleep(10)
    miss = 0
    for pid, e in entries.items():
        a = abstracts.get(pid)
        if a:
            e["abstract"] = a["abstract"]
            if not e["title"]:
                e["title"] = a["title"]
            if not e["authors"]:
                e["authors"] = a["authors"]
        else:
            e.setdefault("abstract", "")
            if pid.startswith(month + "."):
                miss += 1
    (OUT / f"daily_{tag}_entries.json").write_text(
        json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
    meta = {pid: {"title": e["title"], "authors": e["authors"], "abstract": e["abstract"]}
            for pid, e in entries.items()}
    (OUT / f"daily_{tag}_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"entries": len(entries), "backfilled": len(abstracts), "missing": miss}))


if __name__ == "__main__":
    main()
