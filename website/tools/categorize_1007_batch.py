#!/usr/bin/env python3
"""10.07 starred batch: categorize 11 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-07"
PLAN = [
    ("2610.07639", "agent/harness-and-runtime-security"),
    ("2610.07645", "poison-and-backdoor/agent-skill-poison-and-backdoor"),
    ("2610.07654", "finetuning/harmful-fine-tuning-attacks-and-mechanisms"),
    ("2610.07722", "model-security/language-models/adversarial-prompt-steering"),
    ("2610.07723", "poison-and-backdoor/llm-backdoor-attacks"),
    ("2610.07774", "model-security/multimodal-models/vlm-alignment"),
    ("2610.07935", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.07967", "misc/deception"),
    ("2610.08061", "finetuning/harmful-fine-tuning-defenses"),
    ("2610.08108", "model-security/language-models/dllm-security"),
    ("2610.08448", "finetuning/harmful-fine-tuning-attacks-and-mechanisms"),
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
