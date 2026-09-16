#!/usr/bin/env python3
"""9.16 starred batch: categorize 14 papers (19 cards / 17 leaves, 5 cross-listed).

Cross-listing keeps card content identical (single source: daily/2026-09/2026-09-16.md).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-16"
PLAN = [
    ("2609.16095", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2609.16098", "agent/tool-and-mcp-security"),
    ("2609.16098", "misc/prompt-injection"),
    ("2609.16204", "model-security/language-models/safety-alignment-and-refusal"),
    ("2609.16229", "privacy-and-unlearning/machine-unlearning"),
    ("2609.16305", "agent/benchmarks-and-evaluation"),
    ("2609.16305", "model-security/language-models/over-refusal-mitigation"),
    ("2609.16614", "model-security/multimodal-models/lalm-safety"),
    ("2609.16646", "model-security/multimodal-models/vlm-alignment"),
    ("2609.16694", "misc/cybersecurity-and-dual-use"),
    ("2609.16694", "agent/foundations-and-threat-models"),
    ("2609.16732", "agent/web-and-computer-use-agent-security"),
    ("2609.16732", "responsible-ai/human-ai-interaction-and-oversight"),
    ("2609.16754", "finetuning/emergent-misalignment"),
    ("2609.16754", "responsible-ai/explainability-and-transparency"),
    ("2609.16818", "poison-and-backdoor/rag-poison"),
    ("2609.16890", "privacy-and-unlearning/machine-unlearning"),
    ("2609.16900", "content-authenticity/misinformation-and-fact-checking"),
    ("2609.16900", "agent/benchmarks-and-evaluation"),
    ("2609.16927", "finetuning/subliminal-learning"),
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
