#!/usr/bin/env python3
"""Second pass: inject 👤 author lines into cards whose paper metadata was
missed by exact-title lookup (conference titles are sometimes truncated).

Runs after migrate_format.py; only edits cards lacking an author line and
whose paper resolves (by in-card arXiv link or fuzzy normalized-title match)
to a record that actually has authors.
"""

from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import normalize_title  # noqa: E402

H3 = re.compile(r"^### (\d+)\. (.+)$")
AUTHORS_LINE = re.compile(r"^👤\s*\*\*作者\*\*")
KEYWORDS_LINE = re.compile(r"^\*\*关键词\*\*")
ARXIV_URL = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")


def valid(v: str | None) -> bool:
    return bool(v) and "暂无" not in v and "未提供" not in v


def to_display_name(name: str) -> str:
    if "," in name:
        last, _, first = name.partition(",")
        return f"{first.strip()} {last.strip()}".strip()
    return name.strip()


def render_authors(raw: str) -> str:
    names = [to_display_name(n.strip()) for n in re.split(r"[；;]", raw) if n.strip()]
    if len(names) > 6:
        shown = [names[0], "…", names[-1]]
    else:
        shown = names
    return "👤 **作者**：" + "、".join(shown)


def main() -> None:
    final = json.loads((ROOT / "tools" / "out" / "papers_final.json").read_text(encoding="utf-8"))["papers"]

    by_arxiv = {}
    alias = {}
    for key, paper in final.items():
        if paper.get("arxiv_id"):
            by_arxiv[paper["arxiv_id"]] = paper
        for t in paper.get("titles", []):
            alias.setdefault(normalize_title(t), paper)
    alias_keys = list(alias.keys())

    patched = 0
    unmatched = 0
    for sub in ("daily", "conferences", "domains"):
        for path in (ROOT / sub).rglob("*.md"):
            if path.name == "README.md":
                continue
            lines = path.read_text(encoding="utf-8").split("\n")
            out: list[str] = []
            i = 0
            while i < len(lines):
                m = H3.match(lines[i])
                if not m:
                    out.append(lines[i])
                    i += 1
                    continue
                title = m.group(2).strip()
                j = i + 1
                block: list[str] = []
                while j < len(lines) and not lines[j].startswith("#"):
                    block.append(lines[j])
                    j += 1
                has_author = any(AUTHORS_LINE.match(b) for b in block)
                paper = None
                if not has_author:
                    block_text = "\n".join(block)
                    am = ARXIV_URL.search(block_text)
                    if am and am.group(1) in by_arxiv:
                        paper = by_arxiv[am.group(1)]
                    else:
                        nt = normalize_title(title)
                        paper = alias.get(nt)
                        if paper is None:
                            close = difflib.get_close_matches(nt, alias_keys, n=1, cutoff=0.85)
                            if close:
                                paper = alias[close[0]]
                if paper and valid(paper["best"].get("作者")):
                    author_line = render_authors(paper["best"]["作者"])
                    new_block: list[str] = []
                    inserted = False
                    for k, b in enumerate(block):
                        new_block.append(b)
                        if not inserted and KEYWORDS_LINE.match(b):
                            # insert after keywords line (and its following blank)
                            new_block.append("")
                            new_block.append(author_line)
                            inserted = True
                    if not inserted:
                        # card without keywords: insert right after leading blank line
                        pos = 1 if block and not block[0].strip() else 0
                        new_block = block[:pos] + [author_line, ""] + block[pos:]
                    out.append(lines[i])
                    out.extend(new_block)
                    patched += 1
                else:
                    if not has_author:
                        unmatched += 1
                    out.append(lines[i])
                    out.extend(block)
                i = j
            path.write_text("\n".join(out), encoding="utf-8")
    print(json.dumps({"patched": patched, "still_without_authors": unmatched}))


if __name__ == "__main__":
    main()
