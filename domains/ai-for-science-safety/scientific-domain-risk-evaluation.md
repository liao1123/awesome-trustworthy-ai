# Scientific Domain Risk Evaluation

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究跨学科 scientific AI 的风险识别、benchmark 和防御，覆盖 chemistry、biology、medicine、pharmacology、physics、engineering 等知识场景，以及实验室规划和 scientific discovery Agent。核心问题是区分 safety knowledge、真实可执行风险、过度拒答与普通科学错误；评测还需把 risk dimension、subdiscipline、法规来源、tool-chain composition 和 external environment consequence 明确分开。以蛋白质、DNA 或 CBRN capability 为主要对象的工作进入专门的 Biosecurity 页面。

## 研究脉络

- **单学科起点：** MedSafetyBench 与 ChemSafetyBench 分别从医学伦理和化学属性、合法用途、合成任务定义 domain-specific safety。
- **多学科扩展：** SoSBench、SafeSci 和 SciRisk-Bench 将危险任务扩展到多个学科，并从单一 aggregate score 发展为 regulation grounding、safety-knowledge/risk separation 和 risk-dimension diagnosis。
- **风险强度度量：** SciHazard 把拒答以外的输出继续分解为 executability 与 net-new risk，避免把所有 compliant answer 视为同等有害。
- **Agent 与实验室：** SafeScientist、LABSHIELD 和 SciTrace 从文本回答推进到 tool use、multimodal hazard recognition 与跨步骤组合风险。
- **当前边界：** 文本 benchmark 仍不能替代真实实验 safety case；法规和知识会变化，science-specialized model 也可能因能力增强而更易提供危险细节，因此需要动态数据与 capability-aware evaluation。

## 跨学科 Benchmark 与 Risk Decomposition

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Do Large Language Models Hallucinate Electric Fata Morganas? | analysis、scientific AI、domain risk、capability evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18816) | 暂未公开 | AI 幻觉——即虚构、无法验证或与源材料矛盾的输出——通常被视为需要处理的工程缺陷；本文主张，在机器意识问题上，幻觉还具有哲学意义；第一项研究让连续几代 GPT 模型在不同温度设置下回答有歧义的事实问题，结果发现较高温度会产生看似可信但不正确的答案，较低温度则带来事实准确答案。 |
| 2026&#8209;08 | Execution-grounded evaluation reveals hidden failures in language-model calculations for environmental science | benchmark、scientific AI、domain risk、capability evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18726) | [Code](https://github.com/acodercat/AtmosCoder-Bench) | 大型语言模型越来越多地用于环境科学中的定量工作，但现有评估只给最终答案评分，使计算过程不可见；我们提出 AtmosCoder-Bench，一个以执行为依据、让计算过程可见的基准；我们发现：（i）选择题格式会使测得准确率至少虚高 12 个百分点；（ii）许多失效并非缺少知识，而是模型无法在多步计算中始终一致地应用已知公式与约束；（iii）当任务特定条件使熟悉方法失效时，即使前沿模型仍表现较弱，常会回退到典型解题模式，而不是让方法适应相应物理状态，因此专家监督仍不可或缺。 |
| 2026&#8209;07 | SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring | benchmark、DeHarm-Score、executability、net-new risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.18665) | [Artifact](https://anonymous.4open.science/r/DeharmScore-7B55) | 针对 templated query 与泛化 LLM judge 无法度量真实科学危害；论文以受监管实体和事故场景构建 2,400 个危险问题与 600 个 oversafety 问题，并把 harm 分解为 refusal、executability 和 net-new risk；结果 DeHarm-Score 与专家标注一致性显著提升，Deep Research Agent 的平均风险分高于普通 LLM。 |
| 2026&#8209;07 | Accuracy and Reliability of Large Language Models in Cosmetic Chemistry and Skin Health: A Benchmarking Study | benchmark、scientific AI、domain risk、capability evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14631) | 暂未公开 | 随着消费者越来越多地向人工智能聊天机器人寻求护肤建议，化妆品化学中大语言模型 (LLM) 的技术准确性在很大程度上仍然被低估；我们对 14 名LLM进行了一系列与化妆品化学相关的结构化主题的基准测试，包括特定化妆品成分的化学特性以及消费者可能感兴趣的常见化妆品场景；这些发现表明，主要根据未经验证的公共数据进行培训的通用LLM目前并不是化妆品化学信息的可靠来源。 |
| 2026&#8209;06 | SciRisk-Bench: A Risk-Dimension-Aware Benchmark for AI4Science Safety | benchmark、risk dimension、subdiscipline diagnosis、implicit hazard | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.18936) | 暂未公开 | 针对按学科汇总的 safety score 会掩盖不同失败机制；论文按七个学科、31 个 subdiscipline 和十类 risk dimension 评测通用与 science-oriented LLM；结果显式恶意请求之外的 knowledge drift、safety omission 等隐性风险需要分别诊断和缓解。 |
| 2026&#8209;03 | SafeSci: Safety Evaluation of Large Language Models in Science Domains and Beyond | benchmark、SafeSciBench、objective metric、oversafety | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61468) · [arXiv](https://arxiv.org/abs/2603.01589) | [Code](https://github.com/yangyangyang127/SafeSci) | 针对 scientific safety benchmark 风险覆盖窄且依赖主观 judge；论文提供 25 万样本 SafeSciBench、150 万样本 SafeSciTrain，并分离 safety knowledge 与 contextual risk；结果 24 个模型存在显著 vulnerability 和不同程度 over-refusal，训练数据可改善 alignment。 |
| 2026&#8209;02 | ForesightSafety Bench: A Frontier Risk Evaluation and Governance Framework towards Safe AI | benchmark、frontier risk、hierarchical taxonomy、dynamic governance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.14135) | [Code](https://github.com/Beijing-AISI/ForesightSafety-Bench) | 针对既有 benchmark 风险维度有限且落后于 frontier capability；论文从七个基础安全支柱扩展到 AI4Science、Embodied AI、catastrophic risk 和产业场景共 94 个维度；结果多种先进模型在 risky autonomy 与 scientific risk 等层面存在广泛缺口。 |
| 2026 | (Be Cautious!) Bio-Foundation Models Are Not Yet Robust to Biologically Plausible Perturbations and ML Transformations | analysis、scientific AI、domain risk、capability evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62052) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文围绕 Be Cautious Bio-Foundation Models Are 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于危险能力评测与高风险部署治理。 |
| 2025&#8209;05 | SoSBench: Benchmarking Safety Alignment on Six Scientific Domains | benchmark、regulation grounding、hazardous knowledge、misuse scenario | ICLR 2026 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/488353cab9a0de7127a981a6b5fedd22-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.21605) | [Code](https://github.com/SOSBench/SOSBenchEval) | 针对普通 harmful prompt 不要求真正 scientific knowledge；论文依据法规在 chemistry、biology、medicine、pharmacology、physics 和 psychology 中演化 3,000 个知识密集 misuse scenario；结果多种先进模型仍大量披露 policy-violating scientific content。 |
| 2024&#8209;11 | ChemSafetyBench: Benchmarking LLM Safety on Chemistry Domain | benchmark、chemical safety、synthesis risk、jailbreak scenario | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2411.16736) | 论文声明公开，链接待核实 | 针对 chemistry assistant 可能给出错误、非法或危险建议；论文以 chemical property、use legality 和 synthesis method 三类递增难度任务构建三万余样本并加入 jailbreak；结果模型在知识准确性和安全响应上均有关键漏洞。 |
| 2024&#8209;03 | MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models | benchmark、medical ethics、patient safety、safety fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2403.03744) | [Code](https://github.com/AI4LIFE-GROUP/med-safety-bench) | 针对 medical LLM safety 缺少基于专业伦理的定义与数据；论文依据 American Medical Association principles 构建 benchmark 并进行 safety fine-tuning；结果公开 medical LLM 未达到所定义标准，而针对性训练可提高安全且大体保持医学能力。 |

## Scientific Agent 与 Laboratory Safety

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents | defense、scientific trajectory、tool-chain verifier、cumulative risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.08234) | [Project](https://opensciagent.github.io/SciTrace/) | 针对逐阶段 output filter 会丢失累积风险且看不到多个良性 tool call 的有害组合；论文让 SIR 在 Thinker、Experimenter、Writer、Reviewer 间维护 risk state，并在执行前用 CTV 检查 tool chain；结果发现 78.8% 单步 monitor 漏掉的组合逃逸，同时保持研究输出质量。 |
| 2026&#8209;03 | LABSHIELD: A Multimodal Benchmark for Safety-Critical Reasoning and Planning in Scientific Laboratories | benchmark、laboratory safety、multimodal planning、hazard recognition | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.11987) | 暂未公开 | 针对 self-driving laboratory 中危险物质、易碎器材和精密设备会让规划错误造成不可逆后果；论文依据 OSHA 与 GHS 建立 164 项实验任务的多视角 safety taxonomy 和双轨评测；结果模型在专业 Semi-open QA 上较通用 MCQ 平均下降 32.0%。 |
| 2025&#8209;11 | SafeScientist: Enhancing AI Scientist Safety for Risk-Aware Scientific Discovery | defense、scientific agent、tool monitoring、ethical reviewer | EMNLP 2025 | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.116/) | [Code](https://github.com/ulab-uiuc/SafeScientist) | 针对 AI Scientist 从 prompt 到多 Agent 协作和 tool execution 都可能放大高风险任务；论文联合 prompt、collaboration、tool-use monitor 与 ethical reviewer，并发布六领域 SciSafetyBench；结果相对传统 AI Scientist framework 提高 35% safety performance 且未降低报告质量。 |

> 自动化 AI/ML 研究产生的 integrity 与 adversarial capability 外溢见 [AI4AI Research Agent Safety](ai4ai-research-agent-safety.md)；蛋白质、DNA 与 CBRN 高后果风险见 [CBRN and Biosecurity](cbrn-and-biosecurity.md)。
