#!/usr/bin/env python3
"""Parse /recent pages saved by daily_fetch_recent.py into entries/meta JSON.

Usage: daily_parse_recent.py <TAG> <monthPrefix> "<Date header>"
  e.g. daily_parse_recent.py 1015 2610 "15 Oct 2026"

Keeps only entries under <h3> date sections matching the label; recent pages
carry no abstracts (backfilled separately). Writes:
  out/daily_<TAG>_entries_recent.json  pid -> {pid,title,authors,cats,comments}
Prints dedup/fresh/new-month stats.
"""

from __future__ import annotations

import html as htmllib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "website" / "tools" / "out"

H3 = re.compile(r"<h3[^>]*>(.*?)</h3>", re.S | re.I)
DT = re.compile(r"<dt.*?</dt>", re.S | re.I)
TITLE_RE = re.compile(r"<div class=['\"]list-title[^'\"]*['\"]>(.*?)</div>", re.S)
AUTHORS_RE = re.compile(r"<div class=['\"]list-authors['\"]>(.*?)</div>", re.S)
AUTHOR_RE = re.compile(r"<a[^>]*>(.*?)</a>", re.S)
SUBJ_RE = re.compile(r"<div class=['\"]list-subjects['\"]>(.*?)</div>", re.S)
COMM_RE = re.compile(r"<div class=['\"]list-comments[^'\"]*['\"]>(.*?)</div>", re.S)
CAT_CODE_RE = re.compile(r"\(([a-z-]+\.[A-Z]{1,2})\)")
ID_RE = re.compile(r"href\s*=\s*[\"'][^\"']*/abs/(\d{4}\.\d{4,5})(v\d+)?", re.I)
ABS_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
TAG_RE = re.compile(r"<[^>]+>")


def clean(text: str) -> str:
    text = TAG_RE.sub("", text)
    text = htmllib.unescape(text)
    return " ".join(text.split())


def parse_pages(pages: list[Path], label: str) -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()
    for p in pages:
        raw = p.read_text(encoding="utf-8", errors="replace")
        sections: list[tuple[int, str]] = []
        for m in H3.finditer(raw):
            sections.append((m.start(), clean(m.group(1))))
        if not sections:
            continue

        def date_at(pos: int) -> str:
            cur = ""
            for start, name in sections:
                if start <= pos:
                    cur = name
                else:
                    break
            return cur

        for m in DT.finditer(raw):
            if label not in date_at(m.start()):
                continue
            block = raw[m.start():]
            nxt = DT.search(raw, m.end())
            end = nxt.start() if nxt else len(raw)
            block = block[: end - m.start()]
            idm = ID_RE.search(block)
            if not idm:
                continue
            pid = idm.group(1)
            if pid in seen:
                continue
            tm = TITLE_RE.search(block)
            am = AUTHORS_RE.search(block)
            sm = SUBJ_RE.search(block)
            cm = COMM_RE.search(block)
            seen.add(pid)
            entries.append({
                "pid": pid,
                "title": re.sub(r"^\s*Title:\s*", "", clean(tm.group(1))) if tm else "",
                "authors": [clean(a) for a in AUTHOR_RE.findall(am.group(1))] if am else [],
                "cats": CAT_CODE_RE.findall(sm.group(1)) if sm else [],
                "comments": re.sub(r"^\s*Comments:\s*", "", clean(cm.group(1))) if cm else "",
            })
    return entries


def main() -> None:
    tag, month, label = sys.argv[1], sys.argv[2], sys.argv[3]
    pages = sorted((OUT / f"daily_{tag}_recent").glob("*.html"))
    if not pages:
        sys.exit(f"no pages under daily_{tag}_recent/")
    entries: dict[str, dict] = {}
    for p in pages:
        got = parse_pages([p], label)
        print(f"{p.name}: {len(got)} target-date entries")
        for e in got:
            entries.setdefault(e["pid"], e)
    dedup = len(entries)

    date_dir = None
    for cand in sorted((ROOT / "daily").iterdir(), reverse=True):
        if cand.is_dir() and re.match(r"^\d{4}-\d{2}$", cand.name):
            date_dir = cand
            break
    collected: set[str] = set()
    for md in sorted(date_dir.glob("*.md")):
        for pid in ABS_URL_RE.findall(md.read_text(encoding="utf-8")):
            collected.add(pid)
    fresh = {pid: e for pid, e in entries.items() if pid not in collected}
    new_seg = {pid: e for pid, e in fresh.items() if pid.startswith(month + ".")}
    (OUT / f"daily_{tag}_entries_recent.json").write_text(
        json.dumps(fresh, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"dedup": dedup, "fresh": len(fresh), f"new{month}": len(new_seg),
                      "collected_month": len(collected)}))


if __name__ == "__main__":
    main()
