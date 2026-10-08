#!/usr/bin/env python3
"""10.08 starred batch: categorize 11 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-08"
PLAN = [
    ("2610.08923", "guardrails/policy-adaptive-guardrails"),
    ("2610.09000", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.09004", "misc/capability-access-control"),
    ("2610.09384", "finetuning/emergent-misalignment"),
    ("2610.09462", "poison-and-backdoor/vla-backdoor"),
    ("2610.09600", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.09703", "model-security/multimodal-models/vlm-alignment"),
    ("2610.09708", "model-security/embodied-models/vla-adversarial-attacks"),
    ("2610.09941", "poison-and-backdoor/vlm-backdoor-defense-and-detection"),
    ("2610.10345", "finetuning/harmful-fine-tuning-defenses"),
    ("2610.10358", "privacy-and-unlearning/machine-unlearning"),
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
