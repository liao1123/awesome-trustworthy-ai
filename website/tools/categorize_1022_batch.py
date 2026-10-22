#!/usr/bin/env python3
"""10.22 starred batch: categorize 5 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-22"
PLAN = [
    ("2610.28897", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.28966", "agent/multi-agent-system-security"),
    ("2610.29342", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.29395", "adversarial-robustness/adversarial-defense-and-certification"),
    ("2610.29555", "model-security/language-models/safety-alignment-and-refusal"),
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
