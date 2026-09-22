#!/usr/bin/env python3
"""9.22 starred batch: categorize 20 papers (22 cards / 18 leaves, 2 cross-listed)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-09-22"
PLAN = [
    ("2609.22119", "misc/cot-monitorability"),
    ("2609.22144", "finetuning/harmful-fine-tuning-defenses"),
    ("2609.22178", "agent/web-and-computer-use-agent-security"),
    ("2609.22200", "privacy-and-unlearning/leakage-audit-and-mitigation"),
    ("2609.22215", "finetuning/subliminal-learning"),
    ("2609.22228", "model-security/language-models/reasoning-model-safety"),
    ("2609.22234", "model-security/multimodal-models/vlm-alignment"),
    ("2609.22246", "poison-and-backdoor/search-agent"),
    ("2609.22260", "responsible-ai/explainability-and-transparency"),
    ("2609.22293", "model-security/multimodal-models/vlm-jailbreak-and-adversarial-attacks"),
    ("2609.22711", "poison-and-backdoor/rl-poison-and-backdoor"),
    ("2609.22724", "agent/web-and-computer-use-agent-security"),
    ("2609.23260", "finetuning/subliminal-learning"),
    ("2609.23980", "vulnerability-discovery/ctf-and-vulnerability-discovery"),
    ("2609.24084", "misc/model-copyright-protection"),
    ("2609.24243", "responsible-ai/explainability-and-transparency"),
    ("2609.24243", "misc/cot-monitorability"),
    ("2609.24350", "model-security/embodied-models/vla-safety-evaluation-and-defense"),
    ("2609.24407", "poison-and-backdoor/generative-engine-optimization"),
    ("2609.24662", "agent/benchmarks-and-evaluation"),
    ("2609.24826", "poison-and-backdoor/llm-backdoor-attacks"),
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
