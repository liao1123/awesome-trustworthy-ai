#!/usr/bin/env python3
"""Rescue 13 borderline papers for 2026-09-11 daily per the relaxed daily bar
(2026-09-11: daily collects anything plausibly AI-safety-related at P3; only
hard exclusions remain out). Patches tools/out/daily_out_0911/batch_00.json."""
import json

RESCUE = {
"2609.10935": ("NLP 文本分类器的成员推断脆弱性缺受控基线比较",
 "TF-IDF+LogReg 与微调 DistilBERT 在 SST-2 上做 loss 阈值 MIA，并测正则化与继续微调两类缓解",
 "两类模型均泄漏成员信号（AUC 0.5615/0.5800）；强正则以可见效用损失换泄漏下降",
 ["analysis", "membership inference", "text classifier", "baseline study"]),
"2609.10952": ("标签翻转与后门投毒在经典监督学习上的破坏轮廓缺系统基线",
 "MNIST/Fashion-MNIST × LogReg/Linear SVM/Random Forest，5%/10%/20% 投毒率比较 clean 精度、宏指标与 ASR",
 "后门 ASR 0.9667-1.0 且 clean 性能近乎不变；无差别投毒体现在标准指标而定向后门几乎隐形",
 ["analysis", "data poisoning", "label flipping", "backdoor baseline"]),
"2609.10992": ("LLM 上下文脱敏的隐私-效用权衡机制不明，静态规则严重损害效用",
 "系统解构三个机制：上下文依赖效用（数据价值随用户意图漂移）、策略化适应（删除 vs 替换取决于事实完整性依赖）与分层脱敏",
 "给出何时与如何脱敏的机制化依据，指导上下文感知的隐私保护设计",
 ["analysis", "privacy sanitization", "privacy-utility tradeoff", "context-aware redaction"]),
"2609.11020": ("persona 控制的表示对齐与行为表达之间的关系未被解耦刻画",
 "Llama-3.1-8B 上 13 种 K/V-cache 干预配置（早/中/晚层带替换与全替换）测 V-space 对齐、目标标记表达与词汇多样性",
 "强对齐≠强表达：全/中层替换对齐相当（0.94 vs 0.89）但多样性轮廓不同；位置扰动致共同失效",
 ["analysis", "persona control", "K/V-cache intervention", "representation dissociation"]),
"2609.11195": ("青少年实时支付暴露冲动消费与社工欺诈风险，概率 ML 直接参与授权引入不可审计的非确定性",
 "FST Pay 架构与形式规范：实时授权路径上严格确定性安全门控的不可变操作边界",
 "以确定性安全门控+形式规范替代概率模型直接授权，规避生成式 AI 的审计漏洞",
 ["defense", "safety-gated architecture", "payment authorization", "deterministic gating"]),
"2609.11244": ("MLLM 幻觉检测局限于单模态单任务，泛化性受限",
 "统一框架覆盖图像/视频/音频的理解与生成六任务；OmniHallu-Bench 10,000 样本声明级人工标注；多 agent 架构分解原子声明并经模态专家验证",
 "跨模态跨任务的统一幻觉检测与基准",
 ["detection", "MLLM hallucination", "cross-modal benchmark", "claim verification"]),
"2609.11549": ("欧盟新规允许无人驾驶上路，需运营数据确认型式认证安全目标并预警新威胁",
 "基于 UNECE ISMR 框架分析真实运营数据收集如何支撑安全当局确认安全目标、构建场景目录与跨 ADS 类型比较",
 "给出运营数据驱动的 ADS 安全确认与威胁预警监管路径",
 ["analysis", "ADS regulation", "in-service monitoring", "scenario catalogue"]),
"2609.11592": ("车祸严重度模型在无有限样本保证下部署，KABCO 序数标签与现场评估噪声使现成保证失效",
 "包裹任意严重度模型的分布无关认证层：连续序数集输出、按预声明分区的逐类有效性、经申报报告带向未观测真值转移覆盖",
 "在标签噪声与跨辖区漂移下仍给出可部署的有限样本保证与单侧证书",
 ["defense", "distribution-free certification", "ordinal prediction", "deployment guarantee"]),
"2609.11660": ("具身 agent 靠预收集数据与人类反馈在动态环境不足，内在动机扩大自主性同时加剧对齐难题",
 "提出自主人工 agent 的发展性框架：内在动机（好奇/胜任）引导的交互学习如何与社会规范内化及持续对齐机制结合",
 "概念框架：对齐保证需随自主性发展而演化的阶段性机制",
 ["survey", "developmental alignment", "intrinsic motivation", "social norms"]),
"2609.11769": ("LLM 新闻重写的框架效应研究只测生成/检测/中性度，未测模型能否在保事实下逆转已知框架",
 "三种文本框架实现（评价词汇/施事实现/信息突显）× 60 篇 × 3 干预强度的受控反转测试，540 对保原子事实变体",
 "事实保持 ~0.84 而干预反转仅 0.044-0.068——事实保真与框架操控能力明显分离",
 ["analysis", "news framing", "controlled inversion", "misinformation"]),
"2609.11838": ("全国调查训练的心血管筛查模型惯报 AUROC≈0.89，该精度源于学习还是目标泄漏未知",
 "44 万受访者 × 10 个分类器（含 tabular 基础模型）× 5 级泄漏风险特征层，冻结后跨年应用于 43 万人",
 "目标泄漏而非模型类别解释了报道精度；移除两个诊断后特征显著改变表现——部署级审计范本",
 ["analysis", "target leakage", "medical screening audit", "tabular foundation model"]),
"2609.11878": ("LLM 幻觉检测缺多信号融合的实用管道",
 "微调 DeBERTa-v3 分类 + MC Dropout 不确定性 + 温度校准的响应级检测，HaluEval 评测并做上下文消融",
 "F1 0.915/AUROC 0.977；上下文移除使摘要 F1 降 24%，证明真实蕴含推理；25% 训练数据即达 77% 性能",
 ["detection", "hallucination detection", "uncertainty calibration", "entailment reasoning"]),
"2609.11911": ("agent 从有界任务走向跨任务持续状态，目标/重试/停止等行为转换全靠外部手工规约，构成控制问题",
 "提出 artificial id——决定行为继续/停止/变更的自适应内驱；Petri-dish 最小实验中无任务目标的极小控制器经差异化持久性发展出有效控制",
 "自适应方向性可涌现策略替换与传感映射重解释，指向持久对齐的内驱机制",
 ["analysis", "agentic alignment", "internal drive", "persistent control"]),
}

path = "tools/out/daily_out_0911/batch_00.json"
d = json.load(open(path, encoding="utf-8"))
for pid, (mot, met, con, kws) in RESCUE.items():
    assert pid in d and not d[pid]["include"], pid
    d[pid] = {"include": True, "priority": 3, "reason": "",
              "motivation": mot, "method": met, "conclusion": con, "keywords": kws}
json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print(f"rescued {len(RESCUE)}; totals: include {sum(1 for v in d.values() if v['include'])}, "
      f"优先级 {dict(Counter(v['priority'] for v in d.values() if v['include']))}")
