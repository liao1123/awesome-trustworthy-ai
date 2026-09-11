#!/usr/bin/env python3
"""Second starred batch (9.7-9.11 follow-up stars) — reuses categorize_starred helpers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

PLAN = {
    "2609.04206": ("2026-09-07", "model-security/multimodal-models/lalm-safety"),
    "2609.04276": ("2026-09-07", "model-security/multimodal-models/vlm-alignment"),
    "2609.04495": ("2026-09-07", "misc/prompt-injection"),
    "2609.04720": ("2026-09-07", "model-security/multimodal-models/vlm-alignment"),
    "2609.04767": ("2026-09-07", "misc/embedding-inversion-attacks"),
    "2609.04875": ("2026-09-07", "agent/memory-and-self-evolving-agent-security"),
    "2609.05117": ("2026-09-07", "model-security/language-models/jailbreak-defense-and-evaluation"),
    "2609.05401": ("2026-09-07", "misc/reward-hacking"),
    "2609.08236": ("2026-09-09", "guardrails/guardrail-evaluation"),
    "2609.08256": ("2026-09-09", "model-security/language-models/jailbreak-attacks"),
    "2609.09754": ("2026-09-10", "agent/benchmarks-and-evaluation"),
}


def main() -> int:
    by_day: dict[str, list[str]] = {}
    for pid, (day, _) in PLAN.items():
        by_day.setdefault(day, []).append(pid)
    pools = {day: extract(day) for day in by_day}
    per_file: dict[str, list[str]] = {}
    for pid, (day, target) in PLAN.items():
        assert pid in pools[day], f"{pid} not in {day}"
        per_file.setdefault(target, []).append(pools[day][pid])
    for target, cards in sorted(per_file.items()):
        insert(target, cards)
        print(f"{target}: +{len(cards)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
