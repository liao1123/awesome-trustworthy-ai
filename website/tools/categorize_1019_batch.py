#!/usr/bin/env python3
"""10.19 starred batch: categorize 12 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-19"
PLAN = [
    ("2610.22425", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.22805", "finetuning/emergent-misalignment"),
    ("2610.22841", "misc/cot-monitorability"),
    ("2610.22873", "poison-and-backdoor/llm-poison"),
    ("2610.23085", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.23303", "agent/web-and-computer-use-agent-security"),
    ("2610.23307", "agent/web-and-computer-use-agent-security"),
    ("2610.23449", "agent/tool-and-mcp-security"),
    ("2610.23525", "misc/sycophancy-and-social-influence"),
    ("2610.23541", "poison-and-backdoor/generative-engine-optimization"),
    ("2610.23566", "model-security/embodied-models/vla-adversarial-attacks"),
    ("2610.23726", "model-security/language-models/jailbreak-attacks"),
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
