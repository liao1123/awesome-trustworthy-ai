#!/usr/bin/env python3
"""9.28 starred batch: categorize 8 papers (8 cards / 8 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY_POOL = {
    "2026-09-25": ["2609.29995"],
    "2026-09-28": ["2609.30383", "2609.30454", "2609.30841", "2609.31032", "2609.31142", "2609.31186", "2609.31342"],
}
PLAN = [
    ("2609.29995", "2026-09-25", "model-security/multimodal-models/vlm-alignment"),
    ("2609.30383", "2026-09-28", "poison-and-backdoor/agent-skill-poison-and-backdoor"),
    ("2609.30454", "2026-09-28", "ai-for-science-safety/cbrn-and-biosecurity"),
    ("2609.30841", "2026-09-28", "model-security/language-models/dllm-security"),
    ("2609.31032", "2026-09-28", "model-security/generative-media/video-generation-safety"),
    ("2609.31142", "2026-09-28", "guardrails/guardrail-evaluation"),
    ("2609.31186", "2026-09-28", "agent/behavioral-safety-and-misalignment"),
    ("2609.31342", "2026-09-28", "poison-and-backdoor/rag-poison"),
]


def main() -> int:
    pools = {day: extract(day) for day in DAY_POOL}
    per_file: dict[str, list[str]] = {}
    for pid, day, target in PLAN:
        assert pid in pools[day], f"{pid} not in {day}"
        per_file.setdefault(target, []).append(pools[day][pid])
    for target, cards in sorted(per_file.items()):
        insert(target, cards)
        print(f"{target}: +{len(cards)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
