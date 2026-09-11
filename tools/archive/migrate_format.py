#!/usr/bin/env python3
"""One-time migration of every paper entry to the card format.

Card anatomy (per STYLE_GUIDE):

    ### N. Title
    <icon link row>  📅 date  🏷 venue
    **关键词**：`kw1`、`kw2`
    👤 **作者**：First Last、…、Last First
    - 🎯 **研究动机**：…
    - 🔬 **研究方法**：…
    - 📌 **结论**：…
    <details><summary>📝 展开完整英文摘要（Abstract）</summary> … </details>

Everything that is not a paper entry is copied through verbatim.  New
summaries come from tools/out/summaries.json (Phase 2); entries without a
generated summary fall back to their existing editorial lines.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from collect_index import ARXIV_ID_RE, ARXIV_URL_RE, FIELDS, classify_link, normalize_title  # noqa: E402

HEADING = re.compile(r"^###\s+(.+?)\s*$")
NUMBERED = re.compile(r"^(\d+)\.\s+(.*)$")
FIELD = re.compile(r"^-\s+([^：:]+?)\s*[：:]\s*(.*)$")
SUB_FIELD = re.compile(r"^\s+-\s+([^：:]+?)\s*[：:]\s*(.*)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)]+)\)")

ICON_ORDER = [
    ("arXiv", "📄", "arXiv"),
    ("Code", "🐙", "Code"),
    ("Model", "🤗", "Model"),
    ("Dataset", "📊", "Dataset"),
    ("Project", "🌐", "Project"),
    ("OpenReview", "📝", "OpenReview"),
    ("Official", "🎓", "Official"),
    ("Demo", "🎬", "Demo"),
]

VENUE_PATTERNS = [
    (r"USENIX\s+Security\s*\d{4}", "USENIX Security"), (r"NDSS\s*\d{4}", "NDSS"),
    (r"IEEE\s+S&P\s*\d{4}", "IEEE S&P"), (r"CCS\s*\d{4}", "ACM CCS"),
    (r"ASIACCS\s*\d{4}", "ASIACCS"), (r"EMNLP\s*\d{4}", "EMNLP"),
    (r"ACL\s*\d{4}", "ACL"), (r"EACL\s*\d{4}", "EACL"), (r"NAACL\s*\d{4}", "NAACL"),
    (r"NeurIPS\s*\d{4}", "NeurIPS"), (r"ICLR\s*\d{4}", "ICLR"), (r"ICML\s*\d{4}", "ICML"),
    (r"IJCAI\s*\d{4}", "IJCAI"), (r"AAAI\s*\d{4}", "AAAI"), (r"KDD\s*\d{4}", "KDD"),
    (r"SIGIR\s*\d{4}", "SIGIR"), (r"CVPR\s*\d{4}", "CVPR"), (r"ECCV\s*\d{4}", "ECCV"),
    (r"ICCV\s*\d{4}", "ICCV"), (r"SaTML\s*\d{4}", "SaTML"), (r"COLM\s*\d{4}", "COLM"),
    (r"ASE\s*\d{4}", "ASE"), (r"ICSE\s*\d{4}", "ICSE"), (r"S&P\s*\d{4}", "IEEE S&P"),
]

CONF_FILE_VENUE = {
    "acl": "ACL", "ase": "ASE", "asiaccs": "ASIACCS", "ccs": "ACM CCS",
    "colm": "COLM", "cvpr": "CVPR", "eacl": "EACL", "eccv": "ECCV",
    "icml": "ICML", "ijcai": "IJCAI", "kdd": "KDD", "satml": "SaTML",
    "sigir": "SIGIR", "usenix_security": "USENIX Security",
}

CATEGORY_TOKEN = re.compile(r"^[a-z]+\.[A-Z]{2}$")  # cs.CR, cs.AI, stat.ML ...
ROLE_WORDS = {"attack", "defense", "detection", "analysis", "survey", "benchmark", "tool"}
MAX_KEYWORDS = 6
GARBAGE = "{'motivation'"


def load_summaries() -> dict:
    path = ROOT / "tools" / "out" / "summaries.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def to_display_name(arxiv_name: str) -> str:
    """'Chi, Jianfeng' -> 'Jianfeng Chi'; already-plain names pass through."""
    if "," in arxiv_name:
        last, _, first = arxiv_name.partition(",")
        return f"{first.strip()} {last.strip()}".strip()
    return arxiv_name.strip()


def clean_keywords(raw: str) -> list[str]:
    parts = re.split(r"[；;、,，]", raw or "")
    out: list[str] = []
    for part in parts:
        kw = part.strip().strip("`")
        if not kw or CATEGORY_TOKEN.match(kw):
            continue
        low = kw.lower()
        if low in {k.lower() for k in out}:
            continue
        out.append(kw)
    # research role first, then original order, capped
    roles = [k for k in out if k.lower() in ROLE_WORDS]
    rest = [k for k in out if k.lower() not in ROLE_WORDS]
    ordered = roles + rest
    return ordered[:MAX_KEYWORDS]


def venue_from_text(text: str) -> str:
    if not text or "未注明" in text or "未提供" in text:
        return ""
    for pattern, name in VENUE_PATTERNS:
        m = re.search(pattern, text)
        if m:
            matched = m.group(0)
            year = re.search(r"(\d{4})", matched)
            return f"{name} {year.group(1)}" if year else name
    return ""


def entry_is_paper(block_lines: list[str], numbered: bool) -> bool:
    if numbered:
        return True
    return any(FIELD.match(line) for line in block_lines)


def render_card(title_line: str, fields: dict, links: list[dict], paper_meta: dict | None,
                summary: dict | None, file_venue: str, date_hint: str) -> str:
    lines: list[str] = [f"### {title_line}", ""]

    # --- icon link row ---
    by_type: dict[str, list[str]] = {}
    for link in links:
        by_type.setdefault(link["type"], []).append(link["url"])
    arxiv_id = (paper_meta or {}).get("arxiv_id") or fields.get("_arxiv_id")
    if arxiv_id:
        by_type.setdefault("arXiv", [f"https://arxiv.org/abs/{arxiv_id}"])
    row: list[str] = []
    for key, icon, label in ICON_ORDER:
        for url in by_type.get(key, [])[:1]:
            row.append(f"{icon} [{label}]({url})")
    badges: list[str] = []
    date = fields.get("记录日期") or (paper_meta or {}).get("记录日期") or date_hint
    date = (date or "").strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        date = date[:7]
    if re.match(r"^\d{4}(-\d{2})?$", date):
        badges.append(f"📅 {date}")
    venue = venue_from_text(fields.get("会议录用信息", "")) or file_venue
    if venue:
        badges.append(f"🏷 {venue}")
    if row or badges:
        lines.append("　".join([" · ".join(row), "　".join(badges)]).strip() if badges else " · ".join(row))
        lines.append("")

    # --- keywords ---
    keywords = clean_keywords(fields.get("关键词", ""))
    if keywords:
        lines.append("**关键词**：" + "、".join(f"`{k}`" for k in keywords))
        lines.append("")

    # --- authors ---
    raw_authors = (paper_meta or {}).get("作者") or fields.get("作者", "")
    names: list[str] = []
    if raw_authors and "暂无" not in raw_authors and "未提供" not in raw_authors:
        for name in re.split(r"[；;]", raw_authors):
            name = name.strip()
            if not name or "暂无" in name or "未提供" in name:
                continue
            names.append(to_display_name(name))
    if names:
        if len(names) > 6:
            shown = [names[0], "…", names[-1]]
        else:
            shown = names
        lines.append("👤 **作者**：" + "、".join(shown))
        lines.append("")

    # --- three-part summary ---
    parts = [
        ("🎯", "研究动机", (summary or {}).get("motivation") or clean_old(fields.get("研究动机", ""))),
        ("🔬", "研究方法", (summary or {}).get("method") or clean_old(fields.get("研究方法", ""))),
        ("📌", "结论", (summary or {}).get("conclusion") or clean_old(fields.get("结论", ""))),
    ]
    emitted = False
    for icon, label, value in parts:
        value = (value or "").strip().rstrip("。").strip()
        if value and GARBAGE not in value and value != "未提供":
            lines.append(f"- {icon} **{label}**：{value}")
            emitted = True
    if emitted:
        lines.append("")

    # --- collapsible abstract ---
    abstract = (paper_meta or {}).get("英文摘要") or fields.get("英文摘要", "")
    abstract = (abstract or "").strip()
    if abstract and abstract != "未提供":
        lines.append("<details>")
        lines.append("<summary>📝 展开完整英文摘要（Abstract）</summary>")
        lines.append("")
        lines.append(abstract)
        lines.append("")
        lines.append("</details>")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def clean_old(value: str) -> str:
    value = (value or "").strip()
    if GARBAGE in value or value.startswith("'") or value.startswith("{"):
        return ""
    value = re.sub(r"^\{[^}]*$", "", value)
    return value.strip()


def migrate_file(path: Path, meta_index: dict, summaries: dict, title_alias: dict) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    migrated = 0
    copied_entries = 0
    rel = str(path.relative_to(ROOT))

    file_venue = ""
    m = re.match(r"^([a-z_]+)_\d{4}\.md$", path.name)
    if path.parent.name == "conferences" and m:
        year_match = re.search(r"(\d{4})", path.name)
        if m.group(1) in CONF_FILE_VENUE and year_match:
            file_venue = f"{CONF_FILE_VENUE[m.group(1)]} {year_match.group(1)}"

    date_hint = ""
    if path.parent.name == "daily":
        m2 = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", path.name)
        if m2:
            date_hint = m2.group(1)[:7]

    while i < len(lines):
        line = lines[i]
        heading = HEADING.match(line)
        if not heading:
            out.append(line)
            i += 1
            continue
        # gather block until next heading of any level
        block: list[str] = []
        j = i + 1
        while j < len(lines) and not lines[j].startswith("#"):
            block.append(lines[j])
            j += 1
        raw_title = heading.group(1).strip()
        num_match = NUMBERED.match(raw_title)
        numbered = bool(num_match)
        if any("展开完整英文摘要" in b or "**关键词**" in b for b in block):
            # already migrated — copy through untouched (idempotency guard)
            out.append(line)
            out.extend(block)
            i = j
            continue
        if not entry_is_paper(block, numbered):
            out.append(line)
            out.extend(block)
            i = j
            continue

        # parse fields
        fields: dict = {}
        current = None
        links: list[dict] = []
        for bline in block:
            fm = FIELD.match(bline)
            if fm:
                key, value = fm.group(1).strip(), fm.group(2).strip()
                if key in FIELDS:
                    current = key
                    if key != "链接":
                        fields[key] = value
                    continue
                current = None
                continue
            sm = SUB_FIELD.match(bline)
            if sm and current == "链接":
                for _, url in LINK_RE.findall(sm.group(2)):
                    links.append({"type": classify_link(url), "url": url})
                continue
            if current and current != "链接":
                fields[current] = (fields.get(current, "") + " " + bline.strip()).strip()

        raw_id = fields.get("arXiv ID", "").strip("` ")
        idm = ARXIV_ID_RE.match(raw_id)
        if idm:
            fields["_arxiv_id"] = idm.group(1)
        if not fields.get("_arxiv_id"):
            for link in links:
                am = ARXIV_URL_RE.search(link["url"])
                if am:
                    fields["_arxiv_id"] = am.group(1)
                    break

        # dedupe links
        seen: set[str] = set()
        uniq_links = [l for l in links if not (l["url"] in seen or seen.add(l["url"]))]

        # lookup metadata + summary (resolve title-only entries to their
        # arXiv-keyed record via the title alias map)
        norm_title = normalize_title(num_match.group(2) if num_match else raw_title)
        key = fields.get("_arxiv_id") or title_alias.get(norm_title) or f"title:{norm_title}"
        paper_meta = meta_index.get(key)
        summary = summaries.get(key) or summaries.get(f"title:{norm_title}")

        card = render_card(
            raw_title, fields, uniq_links, paper_meta, summary,
            file_venue, date_hint,
        )
        # avoid double blank lines between cards
        while out and out[-1].strip() == "":
            out.pop()
        out.append("")
        out.append(card.rstrip())
        migrated += 1
        i = j

    new_text = "\n".join(out)
    new_text = re.sub(r"\n{4,}", "\n\n\n", new_text)
    path.write_text(new_text, encoding="utf-8")
    return migrated, copied_entries


def main() -> None:
    targets = sys.argv[1:]
    meta = json.loads((ROOT / "tools" / "out" / "papers_final.json").read_text(encoding="utf-8"))["papers"]
    title_alias = {}
    for key, paper in meta.items():
        for title in paper.get("titles", []):
            title_alias.setdefault(normalize_title(title), key)
    summaries = load_summaries()
    files: list[Path] = []
    if targets:
        files = [ROOT / t for t in targets]
    else:
        for sub in ("daily", "conferences", "domains"):
            for path in (ROOT / sub).rglob("*.md"):
                if path.name != "README.md":
                    files.append(path)
    total = 0
    for path in sorted(files):
        migrated, _ = migrate_file(path, meta, summaries, title_alias)
        total += migrated
        print(f"{path.relative_to(ROOT)}: {migrated} entries")
    print(f"TOTAL migrated: {total}")


if __name__ == "__main__":
    main()
