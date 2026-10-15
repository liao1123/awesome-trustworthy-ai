#!/usr/bin/env python3
"""10.15 starred batch: categorize 9 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-15"
PLAN = [
    ("2610.19005", "vulnerability-discovery/ctf-and-vulnerability-discovery"),
    ("2610.19158", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2610.19384", "agent/benchmarks-and-evaluation"),
    ("2610.19385", "privacy-and-unlearning/machine-unlearning"),
    ("2610.19422", "agent/behavioral-safety-and-misalignment"),
    ("2610.19947", "poison-and-backdoor/vision-poison-and-backdoor"),
    ("2610.19971", "model-security/language-models/jailbreak-attacks"),
    ("2610.20221", "guardrails/specialized-and-multilingual-guardrails"),
    ("2610.20319", "poison-and-backdoor/vlm-backdoor-defense-and-detection"),
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
