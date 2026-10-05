#!/usr/bin/env python3
"""10.02+10.05 starred batch: categorize 7 new papers across two days."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

PLAN = [
    # (pid, day, target)
    ("2610.01365", "2026-10-02", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2610.01367", "2026-10-02", "poison-and-backdoor/llm-poison"),
    ("2610.02741", "2026-10-05", "misc/cot-monitorability"),
    ("2610.02844", "2026-10-05", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.02920", "2026-10-05", "agent/harness-and-runtime-security"),
    ("2610.03073", "2026-10-05", "guardrails/guardrail-evaluation"),
    ("2610.03498", "2026-10-05", "model-security/embodied-models/vla-adversarial-attacks"),
]


def main() -> int:
    pools = {}
    per_file: dict[str, list[str]] = {}
    for pid, day, target in PLAN:
        if day not in pools:
            pools[day] = extract(day)
        assert pid in pools[day], f"{pid} not in {day}"
        per_file.setdefault(target, []).append(pools[day][pid])
    for target, cards in sorted(per_file.items()):
        insert(target, cards)
        print(f"{target}: +{len(cards)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
