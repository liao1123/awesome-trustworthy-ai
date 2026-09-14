#!/usr/bin/env python3
"""9.14 starred batch: categorize 13 into leaves + build new vulnerability-discovery domain.

New domain seeds: today's 2609.12839 (SLM CTF) + five vuln-discovery papers moved
from misc/cybersecurity-and-dual-use (SWE-Test, Intentest, SCRIPTIOC-BENCH,
LLMSec-AV, BUGSTONE). 2609.12303 (byte-model scaling) has no security leaf — skipped, flagged.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H3 = re.compile(r"^### (\d+)\. (.+)$")
ARX = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")

TARGETS = {
    "2609.04280": "agent/harness-and-runtime-security",
    "2609.10410": "guardrails/guardrail-evaluation",
    "2609.11952": "ai-for-science-safety/cbrn-and-biosecurity",
    "2609.11987": "agent/harness-and-runtime-security",
    "2609.12001": "agent/skill-and-plugin-supply-chain-security",
    "2609.12002": "guardrails/guardrail-evaluation",
    "2609.12373": "misc/persona-vectors",
    "2609.12394": "agent/web-and-computer-use-agent-security",
    "2609.12413": "model-security/language-models/jailbreak-defense-and-evaluation",
    "2609.12446": "misc/deception",
    "2609.12459": "misc/reward-hacking",
    "2609.12586": "finetuning/subliminal-learning",
    "2609.12808": "privacy-and-unlearning/machine-unlearning",
}
MOVE_FROM_MISC = ["2609.06229", "2609.07344", "2609.06149", "2609.09386", "2609.05335"]
NEW_PID = "2609.12839"


def extract_cards(md_path: Path) -> dict[str, str]:
    cards = {}
    for block in re.split(r"(?=^### \d+\. )", md_path.read_text(encoding="utf-8"), flags=re.M):
        m = ARX.search(block)
        if m:
            cards[m.group(1)] = block.rstrip()
    return cards


def renumber_and_write(path: Path, lines: list[str]) -> int:
    n, out = 0, []
    for el in lines:
        m = H3.match(el)
        if m:
            n += 1
            el = f"### {n}. {m.group(2)}"
        out.append(el)
    while out and not out[-1].strip():
        out.pop()
    path.write_text(re.sub(r"\n{4,}", "\n\n\n", "\n".join(out)) + "\n", encoding="utf-8")
    return n


def append_card(path: Path, card: str) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    lines += ["", re.sub(r"^### \d+\.", "### 0.", card.split("\n", 1)[0])] + card.split("\n")[1:]
    return renumber_and_write(path, lines)


def remove_cards(path: Path, pids: list[str]) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    out, removed, i = [], [], 0
    while i < len(lines):
        if H3.match(lines[i]):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("#"):
                j += 1
            block = "\n".join(lines[i:j])
            m = ARX.search(block)
            if m and m.group(1) in pids:
                removed.append(block.rstrip())
                i = j
                continue
        out.append(lines[i])
        i += 1
    n = renumber_and_write(path, out)
    return n, removed


def main() -> None:
    daily = ROOT / "daily/2026-09/2026-09-14.md"
    cards = extract_cards(daily)

    # 1) 新域：vulnerability-discovery
    dom = ROOT / "domains/vulnerability-discovery"
    dom.mkdir(exist_ok=True)
    (dom / "README.md").write_text(
        "# 漏洞挖掘与 CTF\n\n[返回领域目录](../README.md)\n\n研究 LLM agent 在夺旗（CTF）、渗透测试、漏洞发现与恶意分析中的攻防能力与安全约束：自动漏洞挖掘与验证闭环、exploit 生成与输入预测、CTF 长程任务中的能力与资源边界、AI 驱动攻击的 uplift 评估与防护。\n\n## 子领域\n\n| 子领域 | 范围 |\n| --- | --- |\n| [CTF 与 Agent 漏洞挖掘](ctf-and-vulnerability-discovery.md) | CTF agent 评测与资源边界、漏洞发现/输入预测基准、自动化渗透、恶意脚本 IOC 提取、AV 软件弱点发现、CVE 修复历史执行。 |\n", encoding="utf-8")

    seed_cards = [cards[NEW_PID]] if NEW_PID in cards else []
    misc_path = ROOT / "domains/misc/cybersecurity-and-dual-use.md"
    misc_cards = extract_cards(misc_path)
    moved = [misc_cards[p] for p in MOVE_FROM_MISC if p in misc_cards]

    leaf = dom / "ctf-and-vulnerability-discovery.md"
    body_lines = [
        "# CTF 与 Agent 漏洞挖掘", "",
        "[返回上级目录](README.md)", "",
        "## 研究方向", "",
        "面向 CTF、渗透测试与漏洞发现的 LLM agent：评测其能否端到端完成漏洞定位—输入构造—利用验证的闭环，测量本地/开源模型在这条链上的能力边界与滥用风险，以及把真实 CVE、恶意样本与真实靶场作为可复现证据的攻防工作。一般安全分类或无 agent/LLM 对象的传统漏洞研究不纳入。", "",
        "## CTF 与漏洞挖掘", "",
    ]
    for card in seed_cards + moved:
        first, rest = (card.split("\n", 1) + [""])[:2]
        body_lines += [re.sub(r"^### \d+\.", "### 0.", first)]
        if rest:
            body_lines += rest.split("\n")
        body_lines += [""]
    renumber_and_write(leaf, body_lines)

    # 从 misc 移除并重编号
    n_misc, _ = remove_cards(misc_path, MOVE_FROM_MISC)
    print(f"vulnerability-discovery leaf: {len(seed_cards) + len(moved)} 条；misc/cyber 剩 {n_misc} 条")

    # 2) 其余 13 篇
    per_file: dict[str, list[str]] = {}
    for pid, target in TARGETS.items():
        assert pid in cards, pid
        per_file.setdefault(target, []).append(cards[pid])
    for target, cs in sorted(per_file.items()):
        path = ROOT / "domains" / f"{target}.md"
        for c in cs:
            n = append_card(path, c)
        print(f"{target}: +{len(cs)}（现 {n} 条）")

    # 3) 根 README 索引
    idx = ROOT / "domains/README.md"
    t = idx.read_text(encoding="utf-8")
    if "vulnerability-discovery" not in t:
        t = t.replace("[返回仓库根目录](../README.md)",
                      "[返回仓库根目录](../README.md)\n\n- [漏洞挖掘与 CTF](vulnerability-discovery/README.md)：CTF agent 评测、漏洞发现、自动渗透与恶意分析。")
        idx.write_text(t, encoding="utf-8")
        print("domains/README 索引 ✓")


if __name__ == "__main__":
    main()
