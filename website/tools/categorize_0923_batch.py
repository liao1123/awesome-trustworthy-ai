#!/usr/bin/env python3
"""9.23 starred batch: categorize 12 papers (12 cards / 12 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-23"
PLAN = [
    ("2609.25049", "model-security/language-models/over-refusal-mitigation"),
    ("2609.25166", "privacy-and-unlearning/machine-unlearning"),
    ("2609.25189", "poison-and-backdoor/generative-engine-optimization"),
    ("2609.25469", "poison-and-backdoor/rag-poison"),
    ("2609.25591", "vulnerability-discovery/ctf-and-vulnerability-discovery"),
    ("2609.25721", "finetuning/subliminal-learning"),
    ("2609.26131", "poison-and-backdoor/vla-backdoor"),
    ("2609.26174", "model-security/multimodal-models/vlm-alignment"),
    ("2609.26233", "model-security/generative-media/video-generation-safety"),
    ("2609.26313", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2609.26550", "guardrails/guardrail-evaluation"),
    ("2609.26637", "misc/cot-monitorability"),
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
