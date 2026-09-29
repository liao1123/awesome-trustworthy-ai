#!/usr/bin/env python3
"""9.29 starred batch: categorize 8 papers (8 cards / 8 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-29"
PLAN = [
    ("2609.22145", "model-security/language-models/dllm-security"),
    ("2609.31878", "poison-and-backdoor/diffusion-backdoor"),
    ("2609.32801", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2609.33985", "poison-and-backdoor/llm-poison"),
    ("2609.35002", "model-security/multimodal-models/vlm-alignment"),
    ("2609.35155", "poison-and-backdoor/rag-poison"),
    ("2609.35224", "model-security/language-models/dllm-security"),
    ("2609.35699", "finetuning/harmful-fine-tuning-defenses"),
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
