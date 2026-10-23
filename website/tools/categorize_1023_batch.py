#!/usr/bin/env python3
"""10.23 starred batch: categorize 8 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-23"
PLAN = [
    ("2610.30193", "poison-and-backdoor/rag-poison"),
    ("2610.30348", "model-security/generative-media/image-generation-safety"),
    ("2610.30365", "content-authenticity/misinformation-and-fact-checking"),
    ("2610.30626", "misc/model-copyright-protection"),
    ("2610.30678", "misc/cot-monitorability"),
    ("2610.30884", "finetuning/subliminal-learning"),
    ("2610.31331", "model-security/language-models/dllm-security"),
    ("2610.31616", "privacy-and-unlearning/data-extraction-and-memorization"),
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
