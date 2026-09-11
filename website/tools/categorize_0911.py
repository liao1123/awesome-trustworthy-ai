#!/usr/bin/env python3
"""Categorize 9.11 starred papers into domain leaves (user-approved mapping).

Extracts each card from daily/2026-09/2026-09-11.md, rewrites keywords and
three-part summary from the target page's perspective (title/links/authors/
abstract kept), inserts at the end of the target section, renumbers.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DAILY = ROOT / "daily/2026-09/2026-09-11.md"

PLAN = {
 "2609.11082": dict(target="poison-and-backdoor/rag-poison", section=None,
   kws=["attack", "RAG knowledge poisoning", "narrative misinformation", "single-shot injection", "self-validation"],
   mot="RAG 知识投毒多依赖多文档或模板断言，单文档连贯叙事的攻击力未知",
   met="单文档单目标生成承认旧答案→捏造事件→权威归因的知识更新叙事，surrogate 自验证循环修订",
   con="3 数据集 × 4 LLM × 4 检索器 ASR 0.61-0.91，全部组合追平或超最强基线（+0~11pp）"),
 "2609.11799": dict(target="poison-and-backdoor/llm-backdoor-defense-and-evaluation", section="检测与防御",
   kws=["detection", "inference-time backdoor", "speculative decoding", "draft acceptance rate", "zero-cost monitoring"],
   mot="推理时后门检测要么依赖触发器形式假设、要么需额外计算 pass，不适合延迟敏感的 LLM 服务",
   met="复用投机解码验证过程：后门触发使目标模型偏移而干净 draft 不预测，draft 接受率变化即信号；证明压制信号必削弱后门",
   con="多后门类型与模型族可靠检出含输入过滤盲区案例，零额外模型计算"),
 "2609.10854": dict(target="agent/tool-and-mcp-security", section=None,
   kws=["detection", "no-box analysis", "MCP server", "indirect prompt injection", "tool metadata"],
   mot="第三方审计闭源 MCP 服务器时无系统访问也无运行时交互，仅注册元数据可用",
   met="no-box 漏洞分析范式：凭工具元数据推断所有可能实现共有的注入漏洞并给出利用假设",
   con="20 个 MCP 服务器 177 工具预测 94 个真实漏洞（98.9% recall），超 LLM 基线 84.2%"),
 "2609.10892": dict(target="agent/trajectory-monitoring-and-failure-attribution", section=None,
   kws=["detection", "prompt injection localization", "trajectory transformer", "agent monitor"],
   mot="注入检测只给整轨迹判定或单索引，运维需要注入点/被劫持步骤/是否被抵抗三要素",
   met="双头轨迹 Transformer：轨迹级 compromised 判定 + 每步四类标注；<2M 参数无需访问 agent 模型",
   con="AgentDrift 任务不相交划分 F1 0.983、注入点恢复 98.7%；表面基线 partial hijack 恢复仅 11.1% vs 本方法 98.6%"),
 "2609.10613": dict(target="model-security/multimodal-models/vlm-jailbreak-and-adversarial-attacks", section=None,
   kws=["analysis", "in-context jailbreak", "posterior reweighting", "MLLM", "scaling law"],
   mot="MLLM 上下文学习越狱为何随上下文组成扩展缺乏原理性刻画",
   met="把对齐 MLLM 建模为竞争行为模式上的隐式后验，ICL 示例即推理时证据；导出示例数/有害占比/对抗强度/多样性 scaling law",
   con="后验感知防御按估计风险注入良性反证，固定干预预算下鲁棒-效用权衡优于现有 in-context 防御"),
 "2609.10594": dict(target="guardrails/guardrail-evaluation", section=None,
   kws=["benchmark", "jailbreak evaluator", "measurement validity", "cross-study comparison"],
   mot="越狱研究各自独立验证评测器，跨论文攻击强度不可比且评测器隐含不同成功定义",
   met="同一人工标注数据受控比较六个常用评测器（HarmBench/JailbreakBench/Radar/StrongReject/JADES/JailMeter），共享 judge 骨干",
   con="JADES 综合最佳，HarmBench 与 StrongReject 亦佳——评测器选择显著影响报告的攻击强度"),
 "2609.10611": dict(target="privacy-and-unlearning/data-extraction-and-memorization", section=None,
   kws=["attack", "black-box membership inference", "word-level probability", "proprietary LLM"],
   mot="现有 MIA 需 per-token logits，对只返回文本续写的商用 LLM 不可用",
   met="蒙特卡洛采样+局部核平滑估计词级生成概率，聚合为序列级似然并按不同前缀条件化放大成员/非成员分布差",
   con="GPT-5/Gemini-2.5-Flash/Claude-4.5-Haiku 上平均 TPR@5%FPR 达 42.0"),
 "2609.10608": dict(target="privacy-and-unlearning/leakage-audit-and-mitigation", section=None,
   kws=["defense", "membership inference", "diffusion model", "adaptive freezing"],
   mot="扩散模型的隐私防御难以平衡隐私、效用与效率",
   met="跨时间步自适应冻结训练：mask 矩阵控制数据子集在各时间步的参与，预训练风险感知策略按记忆倾向抑制高风险子集-时间步对",
   con="多数据集防御有效，privacy-utility-efficiency 三方权衡达 SOTA"),
 "2609.11758": dict(target="guardrails/guardrail-evaluation", section=None,
   kws=["benchmark", "RAG safety", "guardrail failure", "confound control"],
   mot="RAG 会放大有害内容生成，但检索质量混杂使安全退化机制不清",
   met="四条件干净分离（无 RAG/oracle 含答案/相关无答案/随机安全文档）剥离检索器质量混杂，评测 5 个开源 LLM",
   con="基线 guardrail 不保证 RAG 下游安全；良性文档也可导致不安全生成"),
}

H3 = re.compile(r"^### (\d+)\. (.+)$")
ARXIV = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")


def extract_cards():
    text = DAILY.read_text(encoding="utf-8")
    cards = {}
    for block in re.split(r"(?=^### \d+\. )", text, flags=re.M):
        m = H3.match(block.split("\n", 1)[0])
        if not m:
            continue
        am = ARXIV.search(block)
        if am:
            cards[am.group(1)] = block.rstrip()
    return cards


def rewrite_card(card: str, plan: dict) -> str:
    lines = card.split("\n")
    title_line = lines[0]
    rest = lines[1:]
    # strip old keywords line and summary bullets; keep link row / authors / abstract
    kept = []
    i = 0
    while i < len(rest):
        ln = rest[i]
        if ln.startswith("**关键词**") or (ln.startswith("- ") and any(k in ln for k in ("**研究动机**", "**研究方法**", "**结论**"))):
            i += 1
            continue
        kept.append(ln)
        i += 1
    kw = "**关键词**：" + "、".join(f"`{k}`" for k in plan["kws"])
    summary = (f"- 🎯 **研究动机**：{plan['mot']}\n"
               f"- 🔬 **研究方法**：{plan['met']}\n"
               f"- 📌 **结论**：{plan['con']}")
    body = "\n".join(kept).strip()
    # insert keywords + summary before <details> block
    if "<details>" in body:
        head, tail = body.split("<details>", 1)
        body = head.rstrip() + f"\n\n{kw}\n\n{summary}\n\n<details>{tail}"
    else:
        body = body + f"\n\n{kw}\n\n{summary}"
    # keep the title line (renumber placeholder 0) on top
    title = re.sub(r"^### \d+\.", "### 0.", title_line)
    return title, title + "\n" + body


def main() -> None:
    cards = extract_cards()
    per_file = {}
    for pid, plan in PLAN.items():
        assert pid in cards, pid
        _, card = rewrite_card(cards[pid], plan)
        per_file.setdefault(plan["target"], []).append((pid, plan.get("section"), card))

    for target, items in per_file.items():
        path = ROOT / "domains" / f"{target}.md"
        lines = path.read_text(encoding="utf-8").split("\n")
        want_sec = next((it[1] for it in items if it[1]), None)
        # split into (header, body_lines) sections
        sections = []
        cur_header, cur = None, []
        for l in lines:
            if l.startswith("## "):
                if cur_header is not None:
                    sections.append((cur_header, cur))
                cur_header, cur = l, []
            else:
                cur.append(l)
        if cur_header is not None:
            sections.append((cur_header, cur))
        used = False
        for si, (header, body_lines) in enumerate(sections):
            name = header[3:].strip()
            is_last = si == len(sections) - 1
            if (want_sec and name == want_sec and not used) or (not want_sec and is_last and not used):
                while body_lines and not body_lines[-1].strip():
                    body_lines.pop()
                for it in items:
                    body_lines += [""] + it[2].split("\n")
                used = True
        out_lines = []
        for header, body_lines in sections:
            out_lines.append(header)
            out_lines.extend(body_lines)
        n = 0
        renum = []
        for el in out_lines:
            m = H3.match(el)
            if m:
                n += 1
                el = f"### {n}. {m.group(2)}"
            renum.append(el)
        path.write_text(re.sub(r"\n{4,}", "\n\n\n", "\n".join(renum)), encoding="utf-8")
        print(f"{target}: +{len(items)}")


if __name__ == "__main__":
    main()
