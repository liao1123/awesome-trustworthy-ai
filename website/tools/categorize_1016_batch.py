#!/usr/bin/env python3
"""10.16 starred batch: categorize 11 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-16"
PLAN = [
    ("2610.20679", "model-security/multimodal-models/vlm-alignment"),
    ("2610.20887", "finetuning/emergent-misalignment"),
    ("2610.20960", "agent/guardrails-and-policy-compliance"),
    ("2610.21200", "ai-for-science-safety/cbrn-and-biosecurity"),
    ("2610.21208", "poison-and-backdoor/vision-poison-and-backdoor"),
    ("2610.21330", "poison-and-backdoor/generative-engine-optimization"),
    ("2610.21412", "agent/harness-and-runtime-security"),
    ("2610.21464", "poison-and-backdoor/rag-poison"),
    ("2610.21633", "finetuning/emergent-misalignment"),
    ("2610.21713", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2610.22068", "guardrails/multimodal-guardrails"),
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
