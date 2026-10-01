#!/usr/bin/env python3
"""10.01 starred batch: categorize 6 new papers (6 cards / 4 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-01"
PLAN = [
    ("2609.35805", "finetuning/emergent-misalignment"),
    ("2609.35932", "misc/prompt-injection"),
    ("2609.36862", "finetuning/harmful-fine-tuning-defenses"),
    ("2609.37054", "model-security/language-models/reasoning-model-safety"),
    ("2609.37624", "finetuning/emergent-misalignment"),
    ("2609.37914", "finetuning/emergent-misalignment"),
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
