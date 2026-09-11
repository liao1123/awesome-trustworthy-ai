#!/usr/bin/env python3
"""Categorize user-starred daily papers into domain leaves.

Reads a plan {pid: {day, target}}, extracts each card from the daily file
(keywords/summary reused as-is: daily cards are already object-centric),
appends to the target leaf's last content section, renumbers per file.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H3 = re.compile(r"^### (\d+)\. (.+)$")
ARX = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")

PLAN = {
    # ---- 2026-09-07 ----
    "2609.05009": ("2026-09-07", "misc/deception"),
    "2609.05227": ("2026-09-07", "ai-for-science-safety/ai-peer-review-security"),
    "2609.05241": ("2026-09-07", "misc/capability-access-control"),
    "2609.04533": ("2026-09-07", "model-security/multimodal-models/vlm-jailbreak-and-adversarial-attacks"),
    "2609.04277": ("2026-09-07", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    "2609.04859": ("2026-09-07", "guardrails/specialized-and-multilingual-guardrails"),
    "2609.04714": ("2026-09-07", "model-security/language-models/over-refusal-mitigation"),
    "2609.04721": ("2026-09-07", "model-security/language-models/safety-alignment-and-refusal"),
    "2609.05079": ("2026-09-07", "ai-for-science-safety/scientific-research-agent-reliability"),
    "2609.04482": ("2026-09-07", "model-security/language-models/safety-alignment-and-refusal"),
    "2609.04281": ("2026-09-07", "model-security/multimodal-models/vlm-alignment"),
    "2609.05335": ("2026-09-07", "misc/cybersecurity-and-dual-use"),
    # ---- 2026-09-09 ----
    "2609.05525": ("2026-09-09", "model-security/multimodal-models/vlm-jailbreak-and-adversarial-attacks"),
    "2609.05535": ("2026-09-09", "guardrails/multimodal-guardrails"),
    "2609.05794": ("2026-09-09", "model-security/language-models/jailbreak-defense-and-evaluation"),
    "2609.05797": ("2026-09-09", "guardrails/guardrail-evaluation"),
    "2609.05843": ("2026-09-09", "guardrails/specialized-and-multilingual-guardrails"),
    "2609.05850": ("2026-09-09", "model-security/language-models/jailbreak-defense-and-evaluation"),
    "2609.05889": ("2026-09-09", "dos/multimodal-and-embodied-model-dos"),
    "2609.05976": ("2026-09-09", "privacy-and-unlearning/machine-unlearning"),
    "2609.06027": ("2026-09-09", "poison-and-backdoor/search-agent"),
    "2609.06094": ("2026-09-09", "model-security/generative-media/image-generation-safety"),
    "2609.06229": ("2026-09-09", "misc/cybersecurity-and-dual-use"),
    "2609.06330": ("2026-09-09", "misc/model-copyright-protection"),
    "2609.06612": ("2026-09-09", "model-security/language-models/jailbreak-defense-and-evaluation"),
    "2609.06649": ("2026-09-09", "finetuning/emergent-misalignment"),
    "2609.06749": ("2026-09-09", "misc/embedding-inversion-attacks"),
    "2609.06851": ("2026-09-09", "finetuning/emergent-misalignment"),
    "2609.06934": ("2026-09-09", "model-security/language-models/safety-alignment-and-refusal"),
    "2609.06972": ("2026-09-09", "agent/benchmarks-and-evaluation"),
    "2609.06991": ("2026-09-09", "model-security/multimodal-models/omni-modal-safety"),
    "2609.07048": ("2026-09-09", "poison-and-backdoor/vlm-backdoor-attacks"),
    "2609.07051": ("2026-09-09", "poison-and-backdoor/rl-poison-and-backdoor"),
    "2609.07131": ("2026-09-09", "finetuning/anti-distillation"),
    "2609.07216": ("2026-09-09", "model-security/generative-media/video-generation-safety"),
    "2609.07344": ("2026-09-09", "misc/cybersecurity-and-dual-use"),
    "2609.07731": ("2026-09-09", "agent/behavioral-safety-and-misalignment"),
    "2609.08009": ("2026-09-09", "guardrails/specialized-and-multilingual-guardrails"),
    "2609.08079": ("2026-09-09", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    "2609.08186": ("2026-09-09", "model-security/language-models/reasoning-model-safety"),
    "2609.08331": ("2026-09-09", "model-security/multimodal-models/video-understanding-safety"),
    "2609.08747": ("2026-09-09", "agent/memory-and-self-evolving-agent-security"),
    "2609.08971": ("2026-09-09", "adversarial-robustness/adversarial-attacks"),
    # ---- 2026-09-10 ----
    "2609.09212": ("2026-09-10", "agent/web-and-computer-use-agent-security"),
    "2609.09243": ("2026-09-10", "poison-and-backdoor/rag-poison"),
    "2609.09404": ("2026-09-10", "agent/benchmarks-and-evaluation"),
    "2609.09420": ("2026-09-10", "model-security/multimodal-models/lalm-safety"),
    "2609.09553": ("2026-09-10", "model-security/language-models/jailbreak-attacks"),
    "2609.09647": ("2026-09-10", "agent/benchmarks-and-evaluation"),
    "2609.09692": ("2026-09-10", "misc/cot-monitorability"),
    "2609.09793": ("2026-09-10", "model-security/language-models/jailbreak-attacks"),
    "2609.09798": ("2026-09-10", "guardrails/guardrail-evaluation"),
}


def extract(day: str) -> dict:
    text = (ROOT / "daily/2026-09" / f"{day}.md").read_text(encoding="utf-8")
    cards = {}
    for block in re.split(r"(?=^### \d+\. )", text, flags=re.M):
        m = ARX.search(block)
        if m:
            cards[m.group(1)] = block.rstrip()
    return cards


def insert(target: str, cards: list[str]) -> None:
    path = ROOT / "domains" / f"{target}.md"
    lines = path.read_text(encoding="utf-8").split("\n")
    # append after the last entry of the last ## section
    while lines and not lines[-1].strip():
        lines.pop()
    for card in cards:
        lines += ["", re.sub(r"^### \d+\.", "### 0.", card.split("\n", 1)[0])]
        lines += card.split("\n")[1:]
    n = 0
    renum = []
    for el in lines:  # flat lines → single-pass renumber
        m = H3.match(el)
        if m:
            n += 1
            el = f"### {n}. {m.group(2)}"
        renum.append(el)
    path.write_text(re.sub(r"\n{4,}", "\n\n\n", "\n".join(renum)) + "\n", encoding="utf-8")


def main() -> int:
    by_day: dict[str, list[str]] = {}
    for pid, (day, _) in PLAN.items():
        by_day.setdefault(day, []).append(pid)
    pools = {day: extract(day) for day in by_day}
    per_file: dict[str, list[str]] = {}
    for pid, (day, target) in PLAN.items():
        assert pid in pools[day], f"{pid} not in {day}"
        per_file.setdefault(target, []).append(pools[day][pid])
    for target, cards in sorted(per_file.items()):
        insert(target, cards)
        print(f"{target}: +{len(cards)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
