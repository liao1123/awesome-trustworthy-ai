#!/usr/bin/env python3
"""Fetch metadata for papers without an arXiv ID: arXiv title search first,
then the conference's official page (schema.org JSON-LD / citation meta).

Runs a small worker pool over the pending papers; progress checkpoints to
tools/out/fetch_progress.json so repeated invocations resume.
"""

from __future__ import annotations

import json
import re
import sys
import threading
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import normalize_title  # noqa: E402

NS = {"a": "http://www.w3.org/2005/Atom"}
API = "https://export.arxiv.org/api/query"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
WORKERS = 3
DELAY = 1.5

lock = threading.Lock()
counters = {"done": 0, "arxiv": 0, "official": 0, "none": 0}


def fetch_url(url: str) -> bytes | None:
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=25) as resp:
                return resp.read()
        except Exception:  # noqa: BLE001
            time.sleep(2 * (attempt + 1))
    return None


def search_arxiv(title: str) -> dict | None:
    query = urllib.parse.quote(f'ti:"{re.sub(chr(34), "", title)}"')
    raw = fetch_url(f"{API}?search_query={query}&start=0&max_results=8")
    if not raw:
        return None
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return None
    for entry in root.findall("a:entry", NS):
        arxiv_id = re.sub(r"v\d+$", "", (entry.findtext("a:id", "", NS) or "").split("/abs/")[-1])
        result_title = " ".join((entry.findtext("a:title", "", NS) or "").split())
        if normalize_title(result_title) == normalize_title(title):
            return {
                "arxiv_id": arxiv_id,
                "title": result_title,
                "authors": [" ".join((a.findtext("a:name", "", NS) or "").split())
                            for a in entry.findall("a:author", NS)],
                "abstract": " ".join((entry.findtext("a:summary", "", NS) or "").split()),
                "published": (entry.findtext("a:published", "", NS) or "")[:10],
                "via": "arxiv-title-search",
            }
    return None


AUTHOR_JSONLD = re.compile(r'"author"\s*:\s*\[(.*?)\]', re.S)
PERSON_NAME = re.compile(r'"name"\s*:\s*"([^"]+)"')
CITATION_AUTHOR = re.compile(r'<meta\s+name="citation_author"\s+content="([^"]+)"')


def fetch_official_page(url: str) -> list[str] | None:
    raw = fetch_url(url)
    if not raw:
        return None
    html = raw.decode("utf-8", errors="replace")
    m = AUTHOR_JSONLD.search(html)
    if m:
        names = PERSON_NAME.findall(m.group(1))
        if names:
            return names
    names = CITATION_AUTHOR.findall(html)
    if names:
        return names
    return None


def official_link(paper: dict) -> str | None:
    for link in paper["best"].get("links", []):
        if link["type"] in ("Official", "OpenReview"):
            return link["url"]
    return None


def main() -> None:
    enriched_path = ROOT / "tools" / "out" / "papers_enriched.json"
    papers = json.loads(enriched_path.read_text(encoding="utf-8"))["papers"]
    cache_path = ROOT / "reader" / "data" / "arxiv_metadata.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8"))

    progress_path = ROOT / "tools" / "out" / "fetch_progress.json"
    progress: dict = {}
    if progress_path.exists():
        progress = json.loads(progress_path.read_text(encoding="utf-8"))

    def valid_authors(v: str | None) -> bool:
        return bool(v) and "暂无" not in v and "未提供" not in v

    todo = [key for key, paper in papers.items()
            if not paper.get("arxiv_id") and not valid_authors(paper["best"].get("作者"))]
    todo = [k for k in todo if k not in progress]
    print(f"to fetch: {len(todo)} (done previously: {len(progress)})", flush=True)

    def work(key: str) -> None:
        paper = papers[key]
        record: dict = {"status": "none"}
        hit = search_arxiv(paper["title"])
        if hit:
            record = {"status": "arxiv", **hit}
            paper["arxiv_id"] = hit["arxiv_id"]
            paper["best"]["作者"] = "；".join(hit["authors"])
            if not paper["best"].get("英文摘要") or paper["best"]["英文摘要"] == "未提供":
                paper["best"]["英文摘要"] = hit["abstract"]
            if not paper["best"].get("记录日期"):
                paper["best"]["记录日期"] = hit["published"][:7]
            if hit["arxiv_id"] not in cache:
                cache[hit["arxiv_id"]] = {
                    "id": hit["arxiv_id"], "title": hit["title"], "abstract": hit["abstract"],
                    "authors": hit["authors"], "submitted": hit["published"],
                    "categories": [], "comments": "", "source": "arxiv-title-search",
                }
        else:
            url = official_link(paper)
            if url:
                names = fetch_official_page(url)
                if names:
                    record = {"status": "official", "authors": names, "url": url}
                    paper["best"]["作者"] = "；".join(names)
        with lock:
            progress[key] = record
            counters["done"] += 1
            counters[record["status"] if record["status"] in ("arxiv", "official", "none") else "none"] += 1
            if counters["done"] % 25 == 0:
                save()
                print(f"[{counters['done']}/{len(todo)}] {counters}", flush=True)
        time.sleep(DELAY)

    def save() -> None:
        progress_path.write_text(json.dumps(progress, ensure_ascii=False), encoding="utf-8")
        (ROOT / "tools" / "out" / "papers_final.json").write_text(
            json.dumps({"papers": papers}, ensure_ascii=False, indent=1), encoding="utf-8")
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(work, todo))
    save()
    print(json.dumps(counters), flush=True)


if __name__ == "__main__":
    main()
