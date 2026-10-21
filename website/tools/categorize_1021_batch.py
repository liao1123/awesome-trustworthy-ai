#!/usr/bin/env python3
"""10.21 starred batch: categorize 7 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-21"
PLAN = [
    ("2610.27244", "agent/benchmarks-and-evaluation"),
    ("2610.27304", "model-security/language-models/jailbreak-attacks"),
    ("2610.27555", "model-security/language-models/safety-alignment-and-refusal"),
    ("2610.27574", "agent/multi-agent-system-security"),
    ("2610.27580", "model-security/language-models/dllm-security"),
    ("2610.27583", "model-security/language-models/dllm-security"),
    ("2610.27584", "model-security/language-models/dllm-security"),
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
