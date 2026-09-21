#!/usr/bin/env python3
"""9.21 starred batch: categorize 6 papers (7 cards / 6 leaves, 1 cross-listed)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-21"
PLAN = [
    ("2609.20370", "dos/llm-dos"),
    ("2609.20370", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2609.20846", "safe-learning-and-deployment/uncertainty-calibration-and-selective-prediction"),
    ("2609.20850", "guardrails/multimodal-guardrails"),
    ("2609.20942", "ai-for-science-safety/ai-peer-review-security"),
    ("2609.21223", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2609.21363", "privacy-and-unlearning/leakage-audit-and-mitigation"),
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
