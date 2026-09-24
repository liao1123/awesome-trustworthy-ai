#!/usr/bin/env python3
"""9.24 starred batch: categorize 12 papers (12 cards / 12 leaves)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-24"
PLAN = [
    ("2609.26868", "poison-and-backdoor/vla-backdoor"),
    ("2609.27090", "poison-and-backdoor/rag-poison"),
    ("2609.27155", "poison-and-backdoor/search-agent"),
    ("2609.27220", "model-security/language-models/dllm-security"),
    ("2609.27273", "agent/web-and-computer-use-agent-security"),
    ("2609.27620", "guardrails/multimodal-guardrails"),
    ("2609.27758", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.27773", "guardrails/guardrail-evaluation"),
    ("2609.27847", "model-security/embodied-models/vla-foundations-and-threat-models"),
    ("2609.27900", "agent/multi-agent-system-security"),
    ("2609.27996", "misc/steganography"),
    ("2609.28197", "agent/trajectory-monitoring-and-failure-attribution"),
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
