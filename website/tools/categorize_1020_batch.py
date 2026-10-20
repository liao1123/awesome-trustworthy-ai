#!/usr/bin/env python3
"""10.20 starred batch: categorize 15 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-20"
PLAN = [
    ("2610.23908", "guardrails/multimodal-guardrails"),
    ("2610.24058", "poison-and-backdoor/vlm-backdoor-attacks"),
    ("2610.24081", "poison-and-backdoor/generative-engine-optimization"),
    ("2610.24379", "finetuning/harmful-fine-tuning-defenses"),
    ("2610.24784", "dos/llm-dos"),
    ("2610.24834", "poison-and-backdoor/rag-poison"),
    ("2610.25372", "poison-and-backdoor/agent-skill-poison-and-backdoor"),
    ("2610.25611", "finetuning/harmful-fine-tuning-attacks-and-mechanisms"),
    ("2610.25683", "finetuning/harmful-fine-tuning-defenses"),
    ("2610.25791", "privacy-and-unlearning/machine-unlearning"),
    ("2610.25937", "poison-and-backdoor/rag-poison"),
    ("2610.26311", "poison-and-backdoor/llm-backdoor-attacks"),
    ("2610.26443", "finetuning/harmful-fine-tuning-defenses"),
    ("2610.26474", "guardrails/specialized-and-multilingual-guardrails"),
    ("2610.26809", "model-security/language-models/safety-alignment-and-refusal"),
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
