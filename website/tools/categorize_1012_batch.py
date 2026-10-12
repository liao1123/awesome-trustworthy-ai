#!/usr/bin/env python3
"""10.12 starred batch: categorize 5 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-12"
PLAN = [
    ("2610.12644", "poison-and-backdoor/llm-backdoor-attacks"),
    ("2610.13078", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.13116", "ai-for-science-safety/cbrn-and-biosecurity"),
    ("2610.13536", "finetuning/subliminal-learning"),
    ("2610.13626", "misc/deception"),
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
