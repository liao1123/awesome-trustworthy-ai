#!/usr/bin/env python3
"""10.28 starred batch: categorize 3 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-28"
PLAN = [
    ("2610.36202", "finetuning/subliminal-learning"),
    ("2610.36258", "model-security/language-models/jailbreak-defense-and-evaluation"),
    ("2610.37481", "finetuning/harmful-fine-tuning-defenses"),
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
