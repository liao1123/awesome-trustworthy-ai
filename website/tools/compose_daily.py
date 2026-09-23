#!/usr/bin/env python3
"""Compose daily/2026-09/2026-09-09.md from screening results + arXiv metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "website" / "tools" / "out"
DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-09-09"
TAG = DATE[5:].replace("-", "")  # e.g. 0909
WEEKDAY = {"2026-09-09": "星期三", "2026-09-10": "星期四", "2026-09-11": "星期五", "2026-09-14": "星期一", "2026-09-15": "星期二", "2026-09-16": "星期三", "2026-09-17": "星期四", "2026-09-18": "星期五", "2026-09-21": "星期一", "2026-09-22": "星期二", "2026-09-23": "星期三"}.get(DATE, "")

LINK_RE = re.compile(r"(https://(?:github\.com/[\w.\-/]+|huggingface\.co/[\w.\-/]+|gitlab\.com/[\w.\-/]+|github\.io/[\w.\-/]+))", re.I)


def classify(url: str) -> tuple[str, str] | None:
    low = url.lower().rstrip(".,;)")
    if "huggingface.co" in low:
        if "/datasets/" in low:
            return ("📊", url)
        return ("🤗", url)
    if "github.io" in low:
        return ("🌐", url)
    if "github.com" in low or "gitlab.com" in low:
        return ("🐙", url)
    return None


def mine_links(abstract: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    for url in LINK_RE.findall(abstract):
        hit = classify(url)
        if hit and hit[1] not in seen:
            seen.add(hit[1])
            found.append(hit)
    return found[:2]


def display_authors(names: list[str]) -> str:
    if len(names) > 6:
        shown = [names[0], "…", names[-1]]
    else:
        shown = names
    return "、".join(shown)


STATS = {
    "0909": {"dedup": 2234, "fresh": 2224, "new2609": 1446, "screened": 210},
    "0910": {"dedup": 752, "fresh": 748, "new2609": 527, "screened": 74},
    "0911": {"dedup": 764, "fresh": 761, "new2609": 532, "screened": 65},
    "0914": {"dedup": 732, "fresh": 725, "new2609": 518, "screened": 79},
    "0915": {"dedup": 1666, "fresh": 1661, "new2609": 1206, "screened": 135},
    "0916": {"dedup": 573, "fresh": 573, "new2609": 571, "screened": 105},
    "0917": {"dedup": 646, "fresh": 645, "new2609": 643, "screened": 90},
    "0918": {"dedup": 642, "fresh": 641, "new2609": 639, "screened": 83},
    "0921": {"dedup": 399, "fresh": 382, "new2609": 379, "screened": 35},
    "0922": {"dedup": 1213, "fresh": 1213, "new2609": 1212, "screened": 326},
    "0923": {"dedup": 693, "fresh": 693, "new2609": 692, "screened": 377},
}


def main() -> None:
    meta = json.loads((OUT / f"daily_{TAG}_meta.json").read_text(encoding="utf-8"))
    verdicts: dict = {}
    out_dir = OUT / "daily_out" if TAG == "0909" else OUT / f"daily_out_{TAG}"
    for path in sorted(out_dir.glob("batch_*.json")):
        verdicts.update(json.loads(path.read_text(encoding="utf-8")))

    included = []
    for pid, v in verdicts.items():
        if not v.get("include"):
            continue
        m = meta.get(pid)
        if not m:
            continue
        included.append((pid, v, m))

    # order: priority asc, then pid
    included.sort(key=lambda t: (t[1].get("priority", 3), t[0]))
    BANDS = [("blog", "大厂动态（Blog）"), (1, "核心收录"), (2, "常规收录"), (3, "扩展视野")]

    cards = []
    for n, (pid, v, m) in enumerate(included, 1):
        links = [f"📄 [arXiv](https://arxiv.org/abs/{pid})"]
        for icon, url in mine_links(m.get("abstract", "")):
            label = {"📄": "arXiv", "🐙": "Code", "🤗": "Model", "📊": "Dataset", "🌐": "Project"}[icon]
            links.append(f"{icon} [{label}]({url})")
        row = " · ".join(links) + f"　📅 2026-09"
        lines = [f"### {n}. {m['title']}", "", row, ""]
        kws = [k for k in v.get("keywords", []) if k.strip()][:6]
        if kws:
            lines += ["**关键词**：" + "、".join(f"`{k}`" for k in kws), ""]
        authors = display_authors(m.get("authors", []))
        if authors:
            lines += [f"👤 **作者**：{authors}", ""]
        parts = []
        for icon, label, field in (("🎯", "研究动机", "motivation"), ("🔬", "研究方法", "method"), ("📌", "结论", "conclusion")):
            value = (v.get(field) or "").strip().rstrip("。").strip()
            if value:
                parts.append(f"- {icon} **{label}**：{value}")
        if parts:
            lines += parts + [""]
        abstract = (m.get("abstract") or "").strip()
        if abstract:
            lines += ["<details>", "<summary>📝 展开完整英文摘要（Abstract）</summary>", "", abstract, "", "</details>", ""]
        cards.append("\n".join(lines).rstrip())

    total_screened = len(verdicts)
    s = STATS[TAG]
    summary_path = OUT / f"daily_{TAG}_summary.txt"
    summary = summary_path.read_text(encoding="utf-8").strip() if summary_path.exists() else "（见下方按优先级排列的论文列表）"

    # 第四板块：大厂动态（Blog）——来自 daily_{TAG}_blog.json
    blog_path = OUT / f"daily_{TAG}_blog.json"
    blog_cards = []
    if blog_path.exists():
        for item in json.loads(blog_path.read_text(encoding="utf-8")):
            lines = ["### 0. " + item['title'], "", f"🌐 [Official]({item['url']})　📅 {item['date']}", ""]
            if item.get("keywords"):
                lines += ["**关键词**：" + "、".join(f"`{k}`" for k in item["keywords"]), ""]
            if item.get("authors"):
                lines += [f"👤 **发布方**：{item['authors']}", ""]
            parts = []
            for icon, label, field in (("🎯", "背景与动因", "motivation"), ("🔬", "内容与举措", "method"), ("📌", "意义与要点", "conclusion")):
                if item.get(field):
                    parts.append(f"- {icon} **{label}**：{item[field]}")
            if parts:
                lines += parts + [""]
            blog_cards.append("\n".join(lines).rstrip())
    blog_section = (f"## 大厂动态（Blog）\n\n" + "\n\n".join(blog_cards) + "\n\n") if blog_cards else ""

    text = f"""# {DATE} arXiv AI Safety Daily

## 检索信息

- 检索日期：{DATE}
- arXiv 范围：检查 {DATE}（{WEEKDAY}）官方 `new` 页面中的 `cs.AI`、`cs.CL`、`cs.CR`、`cs.CV`、`cs.HC`、`cs.IR`、`cs.LG`、`cs.MA`、`cs.RO` 主分类及其 cross-list；九个分类共 {s['dedup']:,} 条跨分类去重条目，去除本月已收录后 {s['fresh']:,} 篇，其中 2609.* 新论文 {s['new2609']:,} 篇；按 `RESEARCH_INTERESTS.md` 的安全边界标题宽筛 {s['screened']} 篇、逐篇阅读摘要后收录 {len(included)} 篇。
- 候选论文：{s['new2609']:,} 个 2609.* 新条目（标题宽筛 {s['screened']}）
- 最终收录：{len(included)} 篇
- 今日概括：{summary}

"""
    # 按文档顺序（Blog→核心→常规→扩展）统一连续编号
    segments = []
    counter = 0
    for key, band_title in BANDS:
        if key == "blog":
            band_cards = blog_cards
        else:
            band_cards = [cards[i] for i, (_, v, _) in enumerate(included) if v.get("priority") == key]
        if not band_cards:
            continue
        numbered = []
        for card in band_cards:
            counter += 1
            numbered.append(re.sub(r"^### \d+\.", f"### {counter}.", card))
        segments.append(f"## {band_title}\n\n" + "\n\n".join(numbered) + "\n\n")
    text += "".join(segments)
    (ROOT / "daily" / "2026-09" / f"{DATE}.md").write_text(text, encoding="utf-8")
    from collections import Counter
    pr = Counter(v.get("priority") for _, v, _ in included)
    print(json.dumps({"included": len(included), "screened": total_screened,
                      "priority_dist": dict(pr)}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
