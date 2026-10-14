#!/usr/bin/env python3
"""10.14 starred batch: categorize 23 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-14"
PLAN = [
    ("2610.14043", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2610.14094", "model-security/multimodal-models/vlm-jailbreak-and-adversarial-attacks"),
    ("2610.14415", "model-security/embodied-models/vla-adversarial-attacks"),
    ("2610.14431", "poison-and-backdoor/agent-memory-poison"),
    ("2610.14487", "poison-and-backdoor/search-agent"),
    ("2610.14701", "poison-and-backdoor/llm-backdoor-attacks"),
    ("2610.15177", "model-security/language-models/dllm-security"),
    ("2610.15218", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.15244", "poison-and-backdoor/agent-memory-poison"),
    ("2610.15449", "guardrails/guard-model-methods"),
    ("2610.15961", "finetuning/emergent-misalignment"),
    ("2610.16470", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.16598", "poison-and-backdoor/llm-backdoor-defense-and-evaluation"),
    ("2610.17457", "agent/web-and-computer-use-agent-security"),
    ("2610.17473", "guardrails/guardrail-evaluation"),
    ("2610.17636", "model-security/language-models/dllm-security"),
    ("2610.17820", "guardrails/guardrail-evaluation"),
    ("2610.18095", "guardrails/specialized-and-multilingual-guardrails"),
    ("2610.18173", "model-security/language-models/dllm-security"),
    ("2610.18304", "guardrails/reasoning-and-efficient-guardrails"),
    ("2610.18326", "agent/guardrails-and-policy-compliance"),
    ("2610.18517", "finetuning/subliminal-learning"),
    ("2610.18609", "poison-and-backdoor/vlm-backdoor-attacks"),
]


def main() -> int:
    pool = extract(DAY)
    per_file: dict[str, list[str]] = {}
    for pid, target in PLAN:
        assert pid in pool, f"{pid} not in {DAY}"
        per_file.setdefault(target, []).append(pool[pid])
    for target, cards in sorted(per_file.items()):
        insert(target, cards)
        print(f"{target}: +{len(cards)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
