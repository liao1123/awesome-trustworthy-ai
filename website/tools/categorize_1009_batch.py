#!/usr/bin/env python3
"""10.09 starred batch: categorize 5 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-09"
PLAN = [
    ("2610.10612", "agent/skill-and-plugin-supply-chain-security"),
    ("2610.10616", "privacy-and-unlearning/model-extraction-and-side-channels"),
    ("2610.10657", "finetuning/subliminal-learning"),
    ("2610.11112", "model-security/generative-media/image-generation-safety"),
    ("2610.11932", "poison-and-backdoor/generative-engine-optimization"),
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
