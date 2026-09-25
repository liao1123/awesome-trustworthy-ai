#!/usr/bin/env python3
"""9.25 starred batch: categorize 11 papers (11 cards / 11 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-25"
PLAN = [
    ("2609.28559", "misc/model-copyright-protection"),
    ("2609.28585", "dos/agent-system-dos"),
    ("2609.28613", "guardrails/guardrail-evaluation"),
    ("2609.28940", "misc/cybersecurity-and-dual-use"),
    ("2609.29099", "poison-and-backdoor/other-poison-and-backdoor"),
    ("2609.29287", "guardrails/multimodal-guardrails"),
    ("2609.29429", "guardrails/guardrail-evaluation"),
    ("2609.29775", "model-security/language-models/reasoning-model-safety"),
    ("2609.29960", "finetuning/harmful-fine-tuning-defenses"),
    ("2609.29999", "model-security/multimodal-models/vlm-alignment"),
    ("2609.30037", "adversarial-robustness/adversarial-attacks"),
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
