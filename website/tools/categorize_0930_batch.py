#!/usr/bin/env python3
"""9.30 starred batch: categorize 8 new papers (8 cards / 8 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-30"
PLAN = [
    ("2609.11146", "finetuning/harmful-fine-tuning-defenses"),
    ("2609.32160", "guardrails/guardrail-evaluation"),
    ("2609.32400", "poison-and-backdoor/agent-skill-poison-and-backdoor"),
    ("2609.32530", "model-security/language-models/adversarial-prompt-steering"),
    ("2609.33634", "model-security/language-models/dllm-security"),
    ("2609.34771", "model-security/language-models/jailbreak-defense-and-evaluation"),
    ("2609.34970", "finetuning/emergent-misalignment"),
    ("2609.35350", "model-security/language-models/reasoning-model-safety"),
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
