#!/usr/bin/env python3
"""9.18 starred batch: categorize 9 papers (11 cards / 9 leaves, 2 cross-listed)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-18"
PLAN = [
    ("2609.19149", "finetuning/subliminal-learning"),
    ("2609.19325", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.19366", "responsible-ai/explainability-and-transparency"),
    ("2609.19366", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.19472", "responsible-ai/explainability-and-transparency"),
    ("2609.19472", "guardrails/guard-model-methods"),
    ("2609.19669", "model-security/embodied-models/vla-adversarial-attacks"),
    ("2609.20027", "finetuning/subliminal-learning"),
    ("2609.20412", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.20457", "misc/model-copyright-protection"),
    ("2609.20751", "model-security/language-models/dllm-security"),
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
