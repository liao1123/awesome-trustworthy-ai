#!/usr/bin/env python3
"""Fetch arXiv /list/<cat>/recent pages and keep only the target announcement date.

Usage: daily_fetch_recent.py <TAG> "<Date header>" <cat> [<cat> ...]
  e.g. daily_fetch_recent.py 1015 "15 Oct 2026" cs.AI cs.CL ...

Pages use show=1000; pagination continues while the page still shows entries
from the target date. Pages saved to out/daily_<TAG>_recent/<cat>_<skip>.html
so daily_parse_recent.py can consume them. Serial, >=12s between pages,
>=45s between categories, hard stop on HTTP 429.
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out"


def fetch_page(cat: str, skip: int) -> str | None:
    url = f"https://arxiv.org/list/{cat}/recent?skip={skip}&show=1000"
    r = subprocess.run(
        ["curl", "-sS", "-L", "--max-time", "150",
         "-w", "\n__HTTP__%{http_code}", url],
        capture_output=True, text=True, timeout=180)
    body = r.stdout
    if r.returncode != 0 or body.endswith("__HTTP__429") or body.endswith("__HTTP__0"):
        print(f"[{cat}] skip={skip} failed rc={r.returncode} tail={body[-64:]!r}", flush=True)
        return None
    return body.rsplit("__HTTP__", 1)[0]


def page_has_target(text: str, label: str) -> tuple[bool, bool]:
    """Return (has_target_entries, target_complete_on_this_page)."""
    heads = re.findall(r"<h3[^>]*>([^<]*20\d\d[^<]*)", text)
    hits = [h for h in heads if label in h]
    if not hits:
        return False, False
    # target complete if a later (older) date section also appears after it
    idx = [i for i, h in enumerate(heads) if label in h]
    complete = idx[-1] < len(heads) - 1
    return True, complete


def main() -> None:
    tag, label, cats = sys.argv[1], sys.argv[2], sys.argv[3:]
    dest = OUT / f"daily_{tag}_recent"
    dest.mkdir(parents=True, exist_ok=True)
    for ci, cat in enumerate(cats):
        skip = 0
        got_any = False
        while skip < 6000:
            text = fetch_page(cat, skip)
            if text is None:
                time.sleep(60)
                text = fetch_page(cat, skip)
                if text is None:
                    print(f"[{cat}] giving up at skip={skip}", flush=True)
                    break
            has, complete = page_has_target(text, label)
            if skip == 0 and not has:
                heads = [h[:40] for h in re.findall(r"<h3[^>]*>([^<]*20\d\d[^<]*)", text)][:3]
                print(f"[{cat}] first recent page lacks {label!r}: {heads}", flush=True)
                break
            (dest / f"{cat}_{skip:05d}.html").write_text(text, encoding="utf-8")
            got_any = True
            print(f"[{cat}] saved skip={skip} ({len(text)/1e6:.1f} MB, target_complete={complete})", flush=True)
            if complete or len(text) < 5000:
                break
            skip += 1000
            time.sleep(12)
        if not got_any:
            print(f"[{cat}] NO PAGES for {label}", flush=True)
        if ci < len(cats) - 1:
            time.sleep(45)
    print("done", flush=True)


if __name__ == "__main__":
    main()
