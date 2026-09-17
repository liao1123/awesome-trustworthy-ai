#!/usr/bin/env python3
"""9.17 starred batch: categorize 10 papers (12 cards / 11 leaves, 2 cross-listed)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-17"
PLAN = [
    ("2609.17930", "agent/trajectory-monitoring-and-failure-attribution"),
    ("2609.18328", "guardrails/policy-adaptive-guardrails"),
    ("2609.18471", "model-security/language-models/reasoning-model-safety"),
    ("2609.18496", "misc/cybersecurity-and-dual-use"),
    ("2609.18515", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.18649", "responsible-ai/fairness-and-bias"),
    ("2609.18860", "responsible-ai/explainability-and-transparency"),
    ("2609.18860", "guardrails/multimodal-guardrails"),
    ("2609.19072", "guardrails/guardrail-evaluation"),
    ("2609.19101", "misc/reward-hacking"),
    ("2609.19101", "misc/cot-monitorability"),
    ("2609.19140", "vulnerability-discovery/ctf-and-vulnerability-discovery"),
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
