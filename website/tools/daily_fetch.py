#!/usr/bin/env python3
"""Fetch arXiv /list/<cat>/new pages for one daily collection run.

Usage: daily_fetch.py <TAG> <yyyymmdd-label> <cat> [<cat> ...]
  TAG  e.g. 1014 -> pages saved to out/daily_<TAG>_pages/<cat>.html
  label e.g. "14 Oct 26" -> abort unless the page's announcement header matches

Serial fetch, >=45s between categories, 150s timeout, 3 attempts with 60s
backoff, hard stop on HTTP 429 (long penalty window; do not hammer).
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out"


def fetch(cat: str, tag: str, label: str) -> bool:
    dest = OUT / f"daily_{tag}_pages" / f"{cat}.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://arxiv.org/list/{cat}/new"
    for attempt in range(1, 4):
        print(f"[{cat}] attempt {attempt} -> {url}", flush=True)
        try:
            r = subprocess.run(
                ["curl", "-sS", "-L", "--max-time", "150",
                 "-w", "\n__HTTP__%{http_code}", url],
                capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            print(f"[{cat}] curl timed out", flush=True)
            time.sleep(60)
            continue
        body = r.stdout
        if r.returncode != 0 or "__HTTP__429" in body[-64:] or "__HTTP__0" in body[-64:]:
            code = body[-64:]
            print(f"[{cat}] failed rc={r.returncode} {code}; backing off 60s", flush=True)
            if "429" in code:
                print(f"[{cat}] HTTP 429 -> STOP (penalty window); rerun later", flush=True)
                return False
            time.sleep(60)
            continue
        text = body.rsplit("__HTTP__", 1)[0]
        marker = "Showing new listings for"
        head = text[text.find(marker):text.find(marker) + 80] if marker in text else ""
        if label not in head:
            print(f"[{cat}] announcement header mismatch: {head!r} (want {label!r})", flush=True)
            return False
        dest.write_text(text, encoding="utf-8")
        size = len(text)
        print(f"[{cat}] saved {size/1e6:.1f} MB, header ok: {head.strip()[:60]}", flush=True)
        return True
    return False


def main() -> None:
    tag, label, cats = sys.argv[1], sys.argv[2], sys.argv[3:]
    ok = 0
    for i, cat in enumerate(cats):
        if not fetch(cat, tag, label):
            if i == 0:
                print("first category failed (wrong announcement date or network) -> abort", flush=True)
                sys.exit(2)
            print(f"[{cat}] FAILED after retries, continuing without it", flush=True)
            continue
        ok += 1
        if i < len(cats) - 1:
            print(f"sleep 45s before next category", flush=True)
            time.sleep(45)
    print(f"done: {ok}/{len(cats)} pages", flush=True)
    sys.exit(0 if ok == len(cats) else 1)


if __name__ == "__main__":
    main()
