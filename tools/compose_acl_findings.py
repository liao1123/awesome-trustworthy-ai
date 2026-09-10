#!/usr/bin/env python3
"""Compose ACL 2026 Findings cards and merge them into conferences/acl_2026.md.

Inputs (under tools/out/):
  acl_findings_all.json       pid -> title/authors/url
  acl_findings_abstracts.json pid -> abstract/arxiv
  acl_screen_out/*.json       pid -> {include, section, motivation, method, conclusion}
  acl_screen_out/batch_04.json  in-repo papers -> {include, section} (summaries reused)
  acl_keywords.json           pid -> [kw, ...]

The script inserts accepted cards into their semantic sections (date-desc
order), renumbers every entry across the file, and updates the header stats.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACL = ROOT / "conferences" / "acl_2026.md"
OUT = ROOT / "tools" / "out"
VENUE = "ACL 2026 Findings"

H3 = re.compile(r"^### (\d+)\. (.+)$")
DATE_RE = re.compile(r"📅\s*(\d{4})(?:-(\d{2}))?")


def display_authors(names: list[str]) -> str:
    if len(names) > 6:
        shown = [names[0], "…", names[-1]]
    else:
        shown = names
    return "、".join(shown)


def sort_key(text: str) -> tuple:
    m = DATE_RE.search(text)
    if not m:
        return (0, 0, "")
    y = int(m.group(1))
    mo = int(m.group(2) or 12)
    return (y, mo, "")


def render_card(num: str, paper: dict, meta: dict, summary: dict, keywords: list[str]) -> str:
    links = []
    if meta.get("arxiv"):
        links.append(f"📄 [arXiv]({meta['arxiv']})")
    links.append(f"🎓 [Official]({paper['url']})")
    date_badge = meta.get("date", "2026-07")
    row = " · ".join(links) + f"　📅 {date_badge}　🏷 {VENUE}"
    kw = "、".join(f"`{k}`" for k in keywords) if keywords else ""
    authors = display_authors(paper.get("authors", []))
    lines = [f"### {num}. {paper['title']}", "", row, ""]
    if kw:
        lines += [f"**关键词**：{kw}", ""]
    if authors:
        lines += [f"👤 **作者**：{authors}", ""]
    parts = []
    for icon, label, field in (("🎯", "研究动机", "motivation"),
                               ("🔬", "研究方法", "method"),
                               ("📌", "结论", "conclusion")):
        value = (summary.get(field) or "").strip().rstrip("。").strip()
        if value:
            parts.append(f"- {icon} **{label}**：{value}")
    if parts:
        lines += parts + [""]
    abstract = (meta.get("abstract") or "").strip()
    if abstract:
        lines += ["<details>", "<summary>📝 展开完整英文摘要（Abstract）</summary>", "",
                  abstract, "", "</details>", ""]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    all_papers = {p["pid"]: p for p in json.loads((OUT / "acl_findings_all.json").read_text(encoding="utf-8"))}
    abstracts = json.loads((OUT / "acl_findings_abstracts.json").read_text(encoding="utf-8"))
    dupe_meta: dict = {}
    dupe_path = OUT / "acl_dupe_meta.json"
    if dupe_path.exists():
        dupe_meta = json.loads(dupe_path.read_text(encoding="utf-8"))
    screening: dict = {}
    for path in sorted((OUT / "acl_screen_out").glob("batch_*.json")):
        screening.update(json.loads(path.read_text(encoding="utf-8")))
    keywords_map: dict = {}
    kw_path = OUT / "acl_keywords.json"
    if kw_path.exists():
        keywords_map = json.loads(kw_path.read_text(encoding="utf-8"))

    # accepted new papers (not yet in repo views) grouped by section
    accepted: dict[str, list[tuple[dict, dict, dict]]] = {}
    count_new = 0
    for pid, verdict in screening.items():
        if not verdict.get("include"):
            continue
        paper = all_papers.get(pid)
        if not paper:
            continue
        meta = {
            "arxiv": (abstracts.get(pid, {}) or {}).get("arxiv", "") or dupe_meta.get(pid, {}).get("arxiv", ""),
            "abstract": (abstracts.get(pid, {}) or {}).get("abstract", "") or dupe_meta.get(pid, {}).get("abstract", ""),
            "date": dupe_meta.get(pid, {}).get("date") or "2026-07",
        }
        section = verdict.get("section", "").strip()
        if not section:
            continue
        accepted.setdefault(section, []).append((paper, meta, verdict))
        count_new += 1
        if pid in dupe_meta and dupe_meta[pid].get("keywords"):
            keywords_map.setdefault(pid, [k for k in dupe_meta[pid]["keywords"] if k.strip()][:6])

    text = ACL.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Phase 1: stream-parse into (kind, payload) segments.
    #  - ("raw", line) for anything that is not a numbered entry
    #  - ("entry", block_text) for each ### N. Title entry, tracked with the
    #    nearest preceding unnumbered ### section heading
    segments: list[tuple[str, str]] = []
    section = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        h3 = H3.match(line)
        if h3:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("#"):
                j += 1
            segments.append(("entry:" + section, "\n".join(lines[i:j]).rstrip()))
            i = j
            continue
        m3 = re.match(r"^###\s+([^0-9\s].+)$", line)
        if m3:
            section = m3.group(1).strip()
        segments.append(("raw", line))
        i += 1

    # Phase 2: emit segments, splicing new cards into their sections.
    out_lines: list[str] = []
    inserted = 0
    pending: dict[str, list[str]] = {}
    for paper, meta, verdict in [
        (p, m, v)
        for sec in accepted
        for (p, m, v) in accepted[sec]
    ]:
        sec = verdict.get("section", "").strip()
        kws = keywords_map.get(paper["pid"], [])
        pending.setdefault(sec, []).append(render_card("0", paper, meta, verdict, kws))

    def flush_section(sec: str) -> None:
        blocks: list[tuple[tuple, str]] = []
        for kind, payload in segments:
            if kind == "entry:" + sec:
                blocks.append((sort_key(payload), payload))
        for card in pending.get(sec, []):
            blocks.append((sort_key(card), card))
        blocks.sort(key=lambda t: (t[0][0], t[0][1]), reverse=True)
        for _sk, block in blocks:
            out_lines.append(block)
            out_lines.append("")

    emitted_sections: set[str] = set()
    current_sec = ""
    for kind, payload in segments:
        if kind == "raw":
            m3 = re.match(r"^###\s+([^0-9\s].+)$", payload)
            if m3:
                # before a new section heading, flush the previous one
                if current_sec:
                    flush_section(current_sec)
                    emitted_sections.add(current_sec)
                current_sec = m3.group(1).strip()
            out_lines.append(payload)
    if current_sec:
        flush_section(current_sec)
        emitted_sections.add(current_sec)

    # renumber all numbered entries sequentially (entries are block elements;
    # rewrite only their first line)
    n = 0
    for idx, element in enumerate(out_lines):
        first = element.split("\n", 1)
        m = H3.match(first[0])
        if m:
            n += 1
            first[0] = f"### {n}. {m.group(2)}"
            out_lines[idx] = "\n".join(first)
    total_entries = n
    inserted = sum(len(v) for k, v in pending.items() if k in emitted_sections)

    new_text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(out_lines))
    ACL.write_text(new_text, encoding="utf-8")

    new_text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(out_lines))
    ACL.write_text(new_text, encoding="utf-8")
    leftover = [s for s in accepted if s not in emitted_sections]
    print(json.dumps({"new_cards": inserted, "total_entries": total_entries,
                      "sections_missing_in_file": leftover}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
