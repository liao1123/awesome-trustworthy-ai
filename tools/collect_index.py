#!/usr/bin/env python3
"""Collect every paper entry from daily/, conferences/ and domains/ into a master index.

Each entry is keyed by arXiv ID when present, otherwise by normalized English
title.  The index records every location the paper appears in, the links it
carries, and its current editorial fields so later pipeline stages (metadata
completion, summary generation, card-format migration) can share one record per
paper.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING = re.compile(r"^###\s+(?:\d+\.\s+)?(.+?)\s*$")
SECTION = re.compile(r"^##\s+(.+?)\s*$")
FIELD = re.compile(r"^-\s+([^：:]+?)\s*[：:]\s*(.*)$")
SUB_FIELD = re.compile(r"^\s+-\s+([^：:]+?)\s*[：:]\s*(.*)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)")
ARXIV_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
ARXIV_ID_RE = re.compile(r"^(\d{4}\.\d{4,5})(?:v\d+)?$")

FIELDS = (
    "arXiv ID",
    "记录日期",
    "关键词",
    "作者",
    "研究动机",
    "研究方法",
    "结论",
    "一句话总结",
    "内容概述",
    "收录理由",
    "链接",
    "arXiv Comments",
    "会议录用信息",
    "英文摘要",
    "代码/数据集/模型",
)


def normalize_title(title: str) -> str:
    text = unicodedata.normalize("NFKC", title).lower()
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def classify_link(url: str) -> str:
    low = url.lower()
    if "arxiv.org" in low:
        return "arXiv"
    if "github.com" in low:
        if low.endswith(".github.io") or ".github.io/" in low:
            return "Project"
        return "GitHub"
    if "huggingface.co" in low or "hf.co" in low:
        if "/datasets/" in low:
            return "Dataset"
        return "Model"
    if "openreview.net" in low:
        return "OpenReview"
    if "youtube.com" in low or "youtu.be" in low or "vimeo.com" in low:
        return "Demo"
    if "kaggle.com" in low or "/dataset" in low:
        return "Dataset"
    if ".github.io" in low or "project" in low or low.endswith(".io") or ".page" in low:
        return "Project"
    if any(d in low for d in ("icml.cc", "neurips.cc", "iclr.cc", "aclweb.org", "aclanthology.org",
                              "dblp.org", "usenix.org", "ieee.org", "acm.org", "dl.acm.org",
                              "cvpr.thecvf.com", "thecvf.com", "openaccess", "ijcai.org", "kdd.org",
                              "sigir.org", "eccv.org", "satal.blogspot.com", "satmlconference.github.io",
                              "satml.org")) or "accepted-papers" in low or "accepted" in low and ".org/202" in low:
        return "Official"
    return "Project"


def parse_entry(block: list[str], path: Path, section: str, number: str, title: str) -> dict:
    entry: dict = {
        "title": title.strip(),
        "source": {"file": str(path.relative_to(ROOT)), "section": section, "number": number},
    }
    current: str | None = None
    for line in block:
        field = FIELD.match(line)
        if field:
            key, value = field.group(1).strip(), field.group(2).strip()
            if key in FIELDS:
                current = key
                if key == "链接":
                    entry.setdefault("links_raw", [])
                else:
                    entry[key] = value
                continue
            current = None
            continue
        sub = SUB_FIELD.match(line)
        if sub and current == "链接":
            label, value = sub.group(1).strip(), sub.group(2).strip()
            for text, url in LINK_RE.findall(value):
                entry["links_raw"].append({"label": label, "url": url})
            continue
        if current and current != "链接":
            entry[current] = (entry.get(current, "") + " " + line.strip()).strip()

    # normalize links
    links: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in entry.pop("links_raw", []):
        url = item["url"]
        if url in seen:
            continue
        seen.add(url)
        links.append({"type": classify_link(url), "url": url})
    # also mine links from any remaining field text
    for key in ("代码/数据集/模型", "arXiv Comments", "会议录用信息"):
        for _, url in LINK_RE.findall(entry.get(key, "")):
            if url not in seen:
                seen.add(url)
                links.append({"type": classify_link(url), "url": url})
    entry["links"] = links

    arxiv_id = None
    raw_id = entry.get("arXiv ID", "").strip("` ")
    m = ARXIV_ID_RE.match(raw_id)
    if m:
        arxiv_id = m.group(1)
    if not arxiv_id:
        for link in links:
            m = ARXIV_URL_RE.search(link["url"])
            if m:
                arxiv_id = m.group(1)
                break
    entry["arxiv_id"] = arxiv_id
    return entry


def parse_file(path: Path) -> list[dict]:
    entries: list[dict] = []
    section = ""
    number = ""
    title = ""
    block: list[str] = []
    in_entry = False

    def flush() -> None:
        nonlocal in_entry, block, title, number
        if in_entry and title:
            # numbered headings are always paper entries; unnumbered ones only
            # count when the block carries at least one known field (otherwise
            # it is a category sub-heading inside conference/domain files)
            has_field = any(FIELD.match(line) for line in block)
            if number or has_field:
                entries.append(parse_entry(block, path, section, number, title))
        in_entry = False
        block = []
        title = ""
        number = ""

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        if heading:
            flush()
            raw = heading.group(1).strip()
            m = re.match(r"^(\d+)\.\s+(.*)$", raw)
            if m:
                number, title = m.group(1), m.group(2).strip()
            else:
                number, title = "", raw
            in_entry = True
            continue
        sec = SECTION.match(line)
        if sec:
            flush()
            section = sec.group(1).strip()
            continue
        if in_entry:
            block.append(line)
    flush()
    return entries


def collect() -> dict:
    files: list[Path] = []
    for sub in ("daily", "conferences", "domains"):
        for path in (ROOT / sub).rglob("*.md"):
            if path.name == "README.md":
                continue
            files.append(path)

    papers: dict[str, dict] = {}
    by_title: dict[str, str] = {}
    stats = {"files": len(files), "entries": 0, "with_arxiv": 0, "title_only": 0}

    for path in sorted(files):
        for entry in parse_file(path):
            stats["entries"] += 1
            key = entry["arxiv_id"] or f"title:{normalize_title(entry['title'])}"
            if entry["arxiv_id"]:
                stats["with_arxiv"] += 1
            else:
                stats["title_only"] += 1
            if key not in papers:
                papers[key] = {
                    "key": key,
                    "arxiv_id": entry["arxiv_id"],
                    "title": entry["title"],
                    "titles": {entry["title"]},
                    "locations": [],
                    "best": {},
                }
                by_title[normalize_title(entry["title"])] = key
            paper = papers[key]
            paper["titles"].add(entry["title"])
            paper["locations"].append(entry["source"])
            # prefer richer field values (longer abstract, real authors, more links)
            for field in ("关键词", "作者", "研究动机", "研究方法", "结论", "英文摘要", "记录日期", "会议录用信息", "arXiv Comments"):
                value = entry.get(field, "")
                old = paper["best"].get(field, "")
                if field == "英文摘要" and value and value != "未提供" and (not old or old == "未提供" or len(value) > len(old)):
                    paper["best"][field] = value
                elif field not in paper["best"] or (not old and value):
                    if not paper["best"].get(field):
                        paper["best"][field] = value
            if entry.get("关键词") and not paper["best"].get("关键词"):
                paper["best"]["关键词"] = entry["关键词"]
            for link in entry["links"]:
                if link not in paper["best"].setdefault("links", []):
                    paper["best"]["links"].append(link)

    # merge title-keyed papers that have an arXiv ID elsewhere
    merged: dict[str, dict] = {}
    title_alias: dict[str, str] = {}
    for key, paper in papers.items():
        if paper["arxiv_id"]:
            merged[key] = paper
            for t in paper["titles"]:
                title_alias[normalize_title(t)] = key
    for key, paper in papers.items():
        if paper["arxiv_id"]:
            continue
        target = None
        for t in paper["titles"]:
            nk = normalize_title(t)
            if nk in title_alias:
                target = title_alias[nk]
                break
        if target and target in merged:
            keep = merged[target]
            keep["titles"] |= paper["titles"]
            keep["locations"].extend(paper["locations"])
            for field, value in paper["best"].items():
                if field == "links":
                    for link in value:
                        if link not in keep["best"].setdefault("links", []):
                            keep["best"]["links"].append(link)
                elif not keep["best"].get(field):
                    keep["best"][field] = value
        else:
            merged[key] = paper
            for t in paper["titles"]:
                title_alias[normalize_title(t)] = key

    out = {"stats": stats, "unique": len(merged), "papers": merged}
    stats["unique"] = len(merged)
    return out


def main() -> None:
    index = collect()
    out_path = ROOT / "tools" / "out" / "papers_index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "stats": index["stats"],
        "papers": {k: {**v, "titles": sorted(v["titles"])} for k, v in index["papers"].items()},
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(index["stats"], ensure_ascii=False))
    missing_abstract = sum(
        1 for p in index["papers"].values()
        if not p["best"].get("英文摘要") or p["best"].get("英文摘要") == "未提供"
    )
    missing_authors = sum(
        1 for p in index["papers"].values()
        if not p["best"].get("作者") or "暂无" in p["best"].get("作者", "")
    )
    print(f"missing abstract: {missing_abstract}, missing authors: {missing_authors}")


if __name__ == "__main__":
    sys.exit(main())
