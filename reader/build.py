#!/usr/bin/env python3
"""Build the reader dataset from the card-format Markdown sources.

Parses every paper card under daily/, conferences/ and domains/, dedupes
papers by arXiv ID (normalized title as fallback), and writes
reader/data/papers.js for the static reader UI.  Markdown stays the source
of truth; this script only produces the browser bundle.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAILY_DIR = ROOT / "daily"
CONFERENCES_DIR = ROOT / "conferences"
DOMAINS_DIR = ROOT / "domains"
DATA_DIR = Path(__file__).resolve().parent / "data"

H3 = re.compile(r"^###\s+(.+?)\s*$")
H2 = re.compile(r"^##\s+(.+?)\s*$")
NUMBERED = re.compile(r"^(\d+)\.\s+(.*)$")
KEYWORDS_LINE = re.compile(r"^\*\*关键词\*\*[：:]\s*(.+)$")
AUTHORS_LINE = re.compile(r"^👤\s*\*\*作者\*\*[：:]\s*(.+)$")
SUMMARY_LINE = re.compile(r"^-\s*[🎯🔬📌]\s*\*\*(研究动机|研究方法|结论)\*\*[：:]\s*(.*)$")
SUMMARY_KEYS = {"研究动机": "motivation", "研究方法": "method", "结论": "conclusion"}
LINK = re.compile(r"(?:[\U0001F300-\U0001FAFF☀-➿]\s*)?\[([^\]]+)\]\((https?://[^)\s]+)\)")
DATE_BADGE = re.compile(r"📅\s*(\d{4}(?:-\d{2})?)")
VENUE_BADGE = re.compile(r"🏷\s*([^\s　]+(?:\s+\d{4})?)")
ARXIV_URL = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", re.I)
DETAILS_OPEN = "<details>"
SUMMARY_TAG = re.compile(r"^<summary>(.*?)</summary>")


def normalize_title(title: str) -> str:
    text = unicodedata.normalize("NFKC", title).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def parse_card(block: list[str]) -> dict | None:
    """Parse one `### N. Title` block; return None if it is not a card."""
    fields: dict = {"links": [], "keywords": [], "authors": []}
    in_details = False
    abstract_lines: list[str] = []
    for line in block:
        if in_details:
            if line.strip() == "</details>":
                in_details = False
            elif SUMMARY_TAG.match(line.strip()) or not line.strip():
                continue
            else:
                abstract_lines.append(line.strip())
            continue
        if line.strip() == DETAILS_OPEN:
            in_details = True
            continue
        m = KEYWORDS_LINE.match(line)
        if m:
            fields["keywords"] = [k.strip().strip("`") for k in re.split(r"[、,]", m.group(1)) if k.strip().strip("`")]
            continue
        m = AUTHORS_LINE.match(line)
        if m:
            fields["authors"] = [a.strip() for a in m.group(1).split("、") if a.strip()]
            continue
        m = SUMMARY_LINE.match(line)
        if m:
            fields[SUMMARY_KEYS[m.group(1)]] = m.group(2).strip()
            continue
        if ("](" in line or "📅" in line or "🏷" in line) and not line.lstrip().startswith("-"):
            for label, url in LINK.findall(line):
                fields["links"].append({"type": label, "url": url})
            m = DATE_BADGE.search(line)
            if m:
                fields["date"] = m.group(1)
            m = VENUE_BADGE.search(line)
            if m:
                fields["venue"] = m.group(1).strip()
    fields["abstract"] = " ".join(" ".join(abstract_lines).split())
    if not (fields["keywords"] or fields["links"] or fields["abstract"] or fields["authors"]):
        return None
    return fields


def parse_page(path: Path) -> tuple[list[dict], str, str]:
    """Return ordered card entries, the page H1 title, and its scope
    description (first paragraph under 研究方向/收录范围)."""
    lines = path.read_text(encoding="utf-8").split("\n")
    title = ""
    section = ""
    desc = ""
    desc_wanted = False
    entries: list[dict] = []
    i = 0
    current: dict | None = None
    block: list[str] = []
    heading_text = ""

    def flush() -> dict | None:
        nonlocal current, block
        if current is None:
            return None
        card = parse_card(block)
        entry = None
        if card is not None:
            num_match = NUMBERED.match(heading_text)
            entry = {
                "number": num_match.group(1) if num_match else "",
                "title": (num_match.group(2) if num_match else heading_text).strip(),
                "section": section,
                **card,
            }
        current = None
        block = []
        return entry

    for idx, line in enumerate(lines):
        if line.startswith("# ") and not title:
            title = line[2:].strip()
        h2 = H2.match(line)
        if h2:
            entry = flush()
            if entry:
                entries.append(entry)
            name = h2.group(1).strip()
            if name in ("研究方向", "收录范围") and not desc:
                desc_wanted = True
                continue
            desc_wanted = False
            section = name
            continue
        if desc_wanted:
            if line.strip():
                desc = line.strip()
                desc_wanted = False
            continue
        h3 = H3.match(line)
        if h3:
            entry = flush()
            if entry:
                entries.append(entry)
            heading_text = h3.group(1).strip()
            if NUMBERED.match(heading_text):
                current = {"pending": True}
                block = []
            else:
                # unnumbered ### is a category sub-heading (conference files)
                current = None
                section = heading_text
            continue
        if current is not None:
            block.append(line)
    entry = flush()
    if entry:
        entries.append(entry)
    return entries, title or path.stem, desc


def paper_id(entry: dict) -> str:
    for link in entry["links"]:
        if link["type"].lower() == "arxiv":
            m = ARXIV_URL.search(link["url"])
            if m:
                return m.group(1)
    return "t:" + normalize_title(entry["title"])[:80]


def merge_paper(existing: dict, incoming: dict) -> None:
    seen = {link["url"] for link in existing["links"]}
    for link in incoming["links"]:
        if link["url"] not in seen:
            seen.add(link["url"])
            existing["links"].append(link)
    for key in ("date", "venue", "motivation", "method", "conclusion", "abstract"):
        if not existing.get(key) and incoming.get(key):
            existing[key] = incoming[key]
    if len(incoming.get("abstract", "")) > len(existing.get("abstract", "")):
        existing["abstract"] = incoming["abstract"]
    seen_kw = set(existing["keywords"])
    for kw in incoming["keywords"]:
        if kw.lower() not in seen_kw:
            seen_kw.add(kw.lower())
            existing["keywords"].append(kw)
    if not existing["authors"] and incoming["authors"]:
        existing["authors"] = incoming["authors"]


def collect() -> dict:
    papers: dict[str, dict] = {}
    views: dict[str, list] = {"daily": [], "domains": [], "conferences": []}

    def register(entry: dict) -> str:
        pid = paper_id(entry)
        record = {
            "id": pid,
            "title": entry["title"],
            "links": entry["links"],
            "date": entry.get("date", ""),
            "venue": entry.get("venue", ""),
            "keywords": entry["keywords"],
            "authors": entry["authors"],
            "motivation": entry.get("motivation", ""),
            "method": entry.get("method", ""),
            "conclusion": entry.get("conclusion", ""),
            "abstract": entry.get("abstract", ""),
        }
        if pid in papers:
            merge_paper(papers[pid], record)
        else:
            papers[pid] = record
        return pid

    # --- daily ---
    daily_files = sorted(DAILY_DIR.rglob("20*.md"), reverse=True)
    for path in daily_files:
        entries, _, _ = parse_page(path)
        sections: dict[str, list[str]] = {}
        order: list[str] = []
        for entry in entries:
            pid = register(entry)
            sec = entry["section"] or "论文列表"
            if sec not in sections:
                sections[sec] = []
                order.append(sec)
            if pid not in sections[sec]:
                sections[sec].append(pid)
        views["daily"].append({
            "id": path.stem,
            "date": path.stem,
            "title": path.stem,
            "sections": [{"title": s, "papers": sections[s]} for s in order],
        })

    # --- conferences ---
    CONF_VENUE = {
        "acl": "ACL", "ase": "ASE", "asiaccs": "ASIACCS", "ccs": "ACM CCS",
        "colm": "COLM", "cvpr": "CVPR", "eacl": "EACL", "eccv": "ECCV",
        "icml": "ICML", "ijcai": "IJCAI", "kdd": "KDD", "satml": "SaTML",
        "sigir": "SIGIR", "usenix_security": "USENIX Security",
    }
    for path in sorted(CONFERENCES_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        entries, title, _ = parse_page(path)
        sections: dict[str, list[str]] = {}
        order: list[str] = []
        for entry in entries:
            pid = register(entry)
            sec = entry["section"] or "论文"
            if sec not in sections:
                sections[sec] = []
                order.append(sec)
            if pid not in sections[sec]:
                sections[sec].append(pid)
        stem = path.stem
        m = re.match(r"^(.*)_(\d{4})$", stem)
        venue = CONF_VENUE.get(m.group(1), m.group(1).upper() if m else "")
        year = m.group(2) if m else ""
        views["conferences"].append({
            "id": stem,
            "title": f"{venue} {year}".strip() or title,
            "venue": venue,
            "year": year,
            "sections": [{"title": s, "papers": sections[s]} for s in order],
        })

    # --- domains ---
    leaf_files = [p for p in DOMAINS_DIR.rglob("*.md")
                  if p.name != "README.md"]
    groups: dict[str, list] = {}
    for path in sorted(leaf_files):
        entries, title, desc = parse_page(path)
        rel = path.relative_to(DOMAINS_DIR)
        group = rel.parts[0]
        sections: dict[str, list[str]] = {}
        order: list[str] = []
        for entry in entries:
            pid = register(entry)
            sec = entry["section"] or "论文"
            if sec not in sections:
                sections[sec] = []
                order.append(sec)
            if pid not in sections[sec]:
                sections[sec].append(pid)
        leaf = {
            "id": str(rel.with_suffix("")),
            "title": title,
            "desc": desc,
            "sections": [{"title": s, "papers": sections[s]} for s in order],
        }
        groups.setdefault(group, []).append(leaf)
    group_meta = {}
    for group, leaves in groups.items():
        readme = DOMAINS_DIR / group / "README.md"
        if readme.exists():
            gtitle, gdesc = "", ""
            body = readme.read_text(encoding="utf-8").split("\n")
            for idx, line in enumerate(body):
                if line.startswith("# ") and not gtitle:
                    gtitle = line[2:].strip()
                    continue
                if gtitle and line.strip() and not line.startswith(("#", "[", "|", "-")):
                    gdesc = line.strip()
                    break
            group_meta[group] = {"title": gtitle or group, "desc": gdesc}
    for group, leaves in groups.items():
        meta = group_meta.get(group, {"title": group, "desc": ""})
        views["domains"].append({
            "id": group,
            "title": meta["title"],
            "desc": meta["desc"],
            "children": leaves,
        })

    dataset = {
        "generated": datetime.date.today().isoformat(),
        "papers": papers,
        "views": views,
    }
    return dataset


def main() -> int:
    dataset = collect()
    DATA_DIR.mkdir(exist_ok=True)
    stats = {k: len(v) for k, v in dataset["views"].items()}
    payload = json.dumps(dataset, ensure_ascii=False, separators=(",", ":"))
    (DATA_DIR / "papers.js").write_text(
        "window.READER_DATA=" + payload + ";\n", encoding="utf-8")
    print(f"papers: {len(dataset['papers'])} | views: {stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
