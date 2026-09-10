#!/usr/bin/env python3
"""Fetch abstracts for ACL 2026 Findings candidates from ACL Anthology pages."""

from __future__ import annotations

import json
import re
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
WORKERS = 3
DELAY = 0.6

ABSTRACT_RE = re.compile(
    r'<div class="card-body acl-abstract">\s*<h5[^>]*>Abstract</h5>\s*<span>(.*?)</span>', re.S)
ARXIV_RE = re.compile(r'href="(https://arxiv\.org/abs/\d{4}\.\d{4,5})"')

lock = threading.Lock()
done = 0


def fetch(url: str) -> str | None:
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&#39;", "'").replace("&quot;", '"').replace("&nbsp;", " ")
    return " ".join(text.split())


def main() -> None:
    candidates = json.loads((ROOT / "tools" / "out" / "acl_findings_candidates.json").read_text(encoding="utf-8"))
    out_path = ROOT / "tools" / "out" / "acl_findings_abstracts.json"
    results: dict = {}
    if out_path.exists():
        results = json.loads(out_path.read_text(encoding="utf-8"))
    todo = [c for c in candidates if c["pid"] not in results]
    print(f"to fetch: {len(todo)} (cached: {len(results)})", flush=True)

    def work(c: dict) -> None:
        global done
        html = fetch(c["url"])
        record = {"title": c["title"], "authors": c["authors"], "url": c["url"]}
        if html:
            m = ABSTRACT_RE.search(html)
            record["abstract"] = clean(m.group(1)) if m else ""
            am = ARXIV_RE.search(html)
            record["arxiv"] = am.group(1) if am else ""
        else:
            record["abstract"] = ""
            record["arxiv"] = ""
        with lock:
            results[c["pid"]] = record
            done += 1
            if done % 25 == 0:
                out_path.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
                print(f"[{done}/{len(todo)}]", flush=True)
        time.sleep(DELAY)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(work, todo))
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    have = sum(1 for v in results.values() if v.get("abstract"))
    print(f"DONE: {len(results)} fetched, {have} with abstract", flush=True)


if __name__ == "__main__":
    main()
