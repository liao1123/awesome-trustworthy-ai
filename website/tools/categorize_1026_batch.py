#!/usr/bin/env python3
"""10.26 starred batch: categorize 6 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-26"
PLAN = [
    ("2610.31713", "guardrails/multimodal-guardrails"),
    ("2610.31995", "privacy-and-unlearning/machine-unlearning"),
    ("2610.32045", "agent/harness-and-runtime-security"),
    ("2610.32155", "agent/skill-and-plugin-supply-chain-security"),
    ("2610.32182", "model-security/multimodal-models/vlm-alignment"),
    ("2610.32531", "misc/prompt-injection"),
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
