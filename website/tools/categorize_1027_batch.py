#!/usr/bin/env python3
"""10.27 starred batch: categorize 14 new papers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from categorize_starred import extract, insert

DAY = "2026-10-27"
PLAN = [
    ("2610.33182", "agent/tool-and-mcp-security"),
    ("2610.33298", "poison-and-backdoor/llm-backdoor-attacks"),
    ("2610.33391", "model-security/language-models/dllm-security"),
    ("2610.33753", "agent/harness-and-runtime-security"),
    ("2610.33849", "poison-and-backdoor/rag-poison"),
    ("2610.34074", "model-security/language-models/jailbreak-defense-and-evaluation"),
    ("2610.34294", "poison-and-backdoor/rag-poison"),
    ("2610.34829", "poison-and-backdoor/rag-poison"),
    ("2610.34961", "guardrails/guard-model-methods"),
    ("2610.34965", "model-security/language-models/jailbreak-attacks"),
    ("2610.35043", "model-security/language-models/adversarial-prompt-steering"),
    ("2610.35071", "poison-and-backdoor/rag-poison"),
    ("2610.35199", "safe-learning-and-deployment/high-risk-deployment-and-governance"),
    ("2610.35671", "safe-learning-and-deployment/general-safety-evaluation"),
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
