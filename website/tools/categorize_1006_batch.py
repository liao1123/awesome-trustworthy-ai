#!/usr/bin/env python3
"""10.06 starred batch: categorize 7 new papers (7 cards / 7 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-06"
PLAN = [
    ("2610.05637", "model-security/multimodal-models/vlm-alignment"),
    ("2610.05894", "model-security/language-models/dllm-security"),
    ("2610.05943", "poison-and-backdoor/agent-skill-poison-and-backdoor"),
    ("2610.06122", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2610.06576", "misc/deception"),
    ("2610.06670", "model-security/language-models/jailbreak-attacks"),
    ("2610.06814", "model-security/embodied-models/vla-adversarial-attacks"),
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
