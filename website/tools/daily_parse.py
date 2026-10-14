#!/usr/bin/env python3
"""Parse fetched arXiv /list/<cat>/new pages into entries/meta JSON for one day.

Usage: daily_parse.py <TAG> <monthPrefix>   e.g. daily_parse.py 1014 2610

Reads out/daily_<TAG>_pages/*.html (New + Cross submissions sections,
Replacement submissions ignored), dedupes by arXiv id across categories,
drops ids already present in daily/<YYYY-MM>/*.md, and writes:
  out/daily_<TAG>_entries.json  pid -> {pid,title,authors,cats,comments,abstract}
  out/daily_<TAG>_meta.json     pid -> {title,authors,abstract}
Prints the dedup/fresh/new-month stats line for compose_daily STATS.
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
ABS_RE = re.compile(r"<p class=['\"]mathjax['\"]>(.*?)</p>", re.S)
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


def parse_page(path: Path) -> tuple[list[dict], str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    # section boundaries: positions of New/Cross/Replacement h3 headings
    sections: list[tuple[int, str]] = []
    for m in H3.finditer(raw):
        label = clean(m.group(1))
        if label.startswith("New submissions"):
            sections.append((m.start(), "new"))
        elif label.startswith("Cross submissions"):
            sections.append((m.start(), "cross"))
        elif label.startswith("Replacement submissions"):
            sections.append((m.start(), "replace"))
    if not sections:
        return [], "no sections"

    def section_at(pos: int) -> str:
        cur = ""
        for start, name in sections:
            if start <= pos:
                cur = name
            else:
                break
        return cur

    entries: list[dict] = []
    seen_local: set[str] = set()
    for m in DT.finditer(raw):
        if section_at(m.start()) in ("", "replace"):
            continue
        block = raw[m.start():]
        nxt = DT.search(raw, m.end())
        end = nxt.start() if nxt else min((s for s, _ in sections if s > m.start()), default=len(raw))
        block = block[: end - m.start()]
        idm = ID_RE.search(block)
        if not idm:
            continue
        pid = idm.group(1)
        if pid in seen_local:
            continue
        tm = TITLE_RE.search(block)
        am = AUTHORS_RE.search(block)
        sm = SUBJ_RE.search(block)
        cm = COMM_RE.search(block)
        absm = ABS_RE.search(block)
        authors = [clean(a) for a in AUTHOR_RE.findall(am.group(1))] if am else []
        cats = CAT_CODE_RE.findall(sm.group(1)) if sm else []
        title = clean(tm.group(1)) if tm else ""
        comments = clean(cm.group(1)) if cm else ""
        e = {
            "pid": pid,
            "title": re.sub(r"^\s*Title:\s*", "", title),
            "authors": authors,
            "cats": cats,
            "comments": re.sub(r"^\s*Comments:\s*", "", comments),
            "abstract": clean(absm.group(1)) if absm else "",
        }
        seen_local.add(pid)
        entries.append(e)
    return entries, "ok"


def main() -> None:
    tag, month = sys.argv[1], sys.argv[2]
    pages = sorted((OUT / f"daily_{tag}_pages").glob("*.html"))
    if not pages:
        sys.exit(f"no pages under daily_{tag}_pages/")

    entries: dict[str, dict] = {}
    for p in pages:
        got, status = parse_page(p)
        print(f"{p.stem}: {len(got)} entries ({status})")
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
    meta = {pid: {"title": e["title"], "authors": e["authors"], "abstract": e["abstract"]}
            for pid, e in fresh.items()}

    (OUT / f"daily_{tag}_entries.json").write_text(
        json.dumps(fresh, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / f"daily_{tag}_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    missing_abs = sum(1 for e in new_seg.values() if not e["abstract"])
    print(json.dumps({"dedup": dedup, "fresh": len(fresh), f"new{month}": len(new_seg),
                      "collected_month": len(collected), "missing_abstract": missing_abs}))


if __name__ == "__main__":
    main()
