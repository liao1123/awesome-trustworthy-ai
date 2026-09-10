#!/usr/bin/env python3
"""Batch C part 1: split four oversized domain files by entry role keyword.

Role comes from the first keyword pill (attack/defense/detection/...).
Roles {detection, defense, survey, benchmark, analysis, competition, challenge,
review, audit, protection} -> defense/evaluation side; everything else -> attacks.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOMAINS = ROOT / "domains"

DEFENSE_ROLES = {"detection", "defense", "survey", "benchmark", "analysis",
                 "competition", "challenge", "review", "audit", "protection"}

PLANS = [
    {
        "src": "poison-and-backdoor/llm-backdoor.md",
        "h1": "语言模型后门",
        "atk": ("poison-and-backdoor/llm-backdoor-attacks.md", "语言模型后门攻击",
                "LLM 后门攻击：触发器植入、持久化、隐蔽通道与激活机制（检测、防御与综评见姊妹页 llm-backdoor-defense-and-evaluation.md）。"),
        "dfd": ("poison-and-backdoor/llm-backdoor-defense-and-evaluation.md", "语言模型后门检测、防御与评测",
                "LLM 后门的检测、防御、净化与基准评测（攻击机制见姊妹页 llm-backdoor-attacks.md）。"),
    },
    {
        "src": "poison-and-backdoor/vlm-backdoor.md",
        "h1": "视觉语言模型后门",
        "atk": ("poison-and-backdoor/vlm-backdoor-attacks.md", "视觉语言模型后门攻击",
                "VLM 后门攻击：多模态触发器、跨模态植入与隐蔽机制（检测与防御见姊妹页 vlm-backdoor-defense-and-detection.md）。"),
        "dfd": ("poison-and-backdoor/vlm-backdoor-defense-and-detection.md", "视觉语言模型后门检测与防御",
                "VLM 后门的检测、防御与净化（攻击机制见姊妹页 vlm-backdoor-attacks.md）。"),
    },
    {
        "src": "guardrails/general-models-and-evaluation.md",
        "h1": None,
        "atk": ("guardrails/guard-model-methods.md", "通用 Guard Model 方法与架构",
                "Guard model 的训练方法、系统架构与部署形态（效果评测与攻击面见姊妹页 guardrail-evaluation.md）。"),
        "dfd": ("guardrails/guardrail-evaluation.md", "Guardrail 评测与攻击面",
                "Guardrail/guard model 的评测基准、有效性审计与攻击面（方法与架构见姊妹页 guard-model-methods.md）。"),
        "atk_roles": {"benchmark", "analysis", "attack", "survey"},
    },
    {
        "src": "finetuning/harmful-fine-tuning.md",
        "h1": None,
        "atk": ("finetuning/harmful-fine-tuning-attacks-and-mechanisms.md", "有害微调攻击与机制",
                "微调解锁有害能力的攻击路径、数据角度与机制分析（防御见姊妹页 harmful-fine-tuning-defenses.md）。"),
        "dfd": ("finetuning/harmful-fine-tuning-defenses.md", "有害微调防御",
                "抵御有害微调的防御、对齐保持与检测（攻击与机制见姊妹页 harmful-fine-tuning-attacks-and-mechanisms.md）。"),
    },
]

H3 = re.compile(r"^### \d+\. (.+)$")
ROLE = re.compile(r"\*\*关键词\*\*：`([a-z-]+)`")


def parse(text: str):
    """Return (preamble_lines, [entry_blocks])."""
    lines = text.split("\n")
    preamble, blocks = [], []
    i = 0
    while i < len(lines):
        if H3.match(lines[i]):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("#"):
                j += 1
            blocks.append("\n".join(lines[i:j]).rstrip())
            i = j
        else:
            preamble.append(lines[i])
            i += 1
    return preamble, blocks


def render(path_rel: str, title: str, scope: str, blocks: list[str], back: str) -> None:
    n = 0
    body = [f"# {title}", "", "[返回上级目录](README.md)", "", "## 研究方向", "", scope, ""]
    sections = {"attack": "## 攻击与机制", "defense": "## 检测与防御", "eval": "## 综评与基准"}
    placed = {"attack": [], "defense": [], "eval": []}
    for b in blocks:
        role = (ROLE.search(b) or [None, "attack"])[1]
        if role in DEFENSE_ROLES:
            key = "eval" if role in {"survey", "benchmark", "analysis", "competition", "challenge", "review"} else "defense"
        else:
            key = "attack"
        placed[key].append(b)
    for key in ("attack", "defense", "eval"):
        if not placed[key]:
            continue
        body.append(sections[key])
        body.append("")
        for b in placed[key]:
            n += 1
            first, rest = (b.split("\n", 1) + [""])[:2]
            m = H3.match(first)
            body.append(f"### {n}. {m.group(1)}")
            if rest:
                body.append(rest)
            body.append("")
    out = "\n".join(body).rstrip() + "\n"
    (DOMAINS / path_rel).write_text(out, encoding="utf-8")


def main() -> None:
    for plan in PLANS:
        src = DOMAINS / plan["src"]
        text = src.read_text(encoding="utf-8")
        _, blocks = parse(text)
        atk_roles = plan.get("atk_roles", None)
        atk_blocks, dfd_blocks = [], []
        for b in blocks:
            role = (ROLE.search(b) or [None, "attack"])[1]
            if atk_roles is not None:
                (atk_blocks if role in atk_roles else dfd_blocks).append(b)
            else:
                (dfd_blocks if role in DEFENSE_ROLES else atk_blocks).append(b)
        render(plan["atk"][0], plan["atk"][1], plan["atk"][2], atk_blocks, plan["atk"][1])
        render(plan["dfd"][0], plan["dfd"][1], plan["dfd"][2], dfd_blocks, plan["dfd"][1])
        src.unlink()
        print(f"{plan['src']}: attacks={len(atk_blocks)} defense={len(dfd_blocks)}")


if __name__ == "__main__":
    main()
