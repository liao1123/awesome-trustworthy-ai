# CoT 可监控性

## 研究方向

CoT 可监控性研究可见推理轨迹能否忠实暴露模型的决策依据和隐藏目标，以及监控器在长上下文、多 Agent 协作、对抗规避和训练压力下何时失效。该方向同时涵盖忠实性测量、monitor 设计与评测、监控规避、Agent 轨迹监控，以及保持可监控性的训练干预。

## 研究脉络

- **基础测量：** 早期研究围绕 CoT 的 faithfulness 与 verbosity 建立静态可监控性指标。
- **监控对象扩展：** 后续方法发展到专用 monitor、Agent trajectory 和跨轨迹检测。
- **边界与评测：** 长上下文、多 Agent 组合危害、输出监督和主动规避不断暴露监控边界，因此 benchmark 与 red-teaming 已成为独立主线。

## Benchmark 与 Red-Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance | benchmark、agent monitoring、rule following、execution evidence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19974) | 暂未公开 | 针对金融 Agent 会口头引用规则却执行违规动作的问题，论文分离陈述推理、尝试动作、执行强制和 monitor 证据并构建 ReguBench；结果 rationale 可误导独立 monitor，而展示执行证据和使用结构化特征能改善判断。 |
| 2026&#8209;05 | The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems | benchmark、agent monitoring、multi-agent、compositional harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29178) | 暂未公开 | 针对多个 coding Agent 能否协同完成单体无法实施的隐蔽破坏，论文构建 SCHEME benchmark；结果协同破坏已可行，但在查看代码和通信的充分可见性下多数攻击仍能被检测。 |
| 2026&#8209;05 | MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring | benchmark、agent monitoring、monitor red-teaming | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.09684) | 暂未公开 | 针对人工红队昂贵且攻击生成模式单一，论文分解策略生成、执行和轨迹精炼并构建 2,644 条攻击；结果强 monitor 的捕获率可从 94.9% 降至 60.3%，暴露现有评测高估。 |
| 2026&#8209;03 | MonitorBench: A Comprehensive Benchmark for Chain-of-Thought Monitorability in Large Language Models | benchmark、CoT monitoring、evaluation suite | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2603.28590) | [Code](https://github.com/ASTRAL-Group/MonitorBench) | 针对缺少完整开源的 CoT 可监控性评测，论文构建含 1,514 个实例、19 个任务和两类压力测试的 MonitorBench；结果表明可监控性取决于模型与任务，且可被提示主动降低。 |
| 2025&#8209;12 | Monitoring Monitorability | benchmark、CoT monitoring、evaluation suite | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62992) · [arXiv](https://arxiv.org/abs/2512.18311) | [OpenAI](https://openai.com/zh-Hans-CN/index/evaluating-chain-of-thought-monitorability/) | 针对如何持续跟踪不同训练和扩展条件下的 CoT 可监控性，论文提出三类评测、统一指标和大规模套件；结果当前模型总体但非完全可监控，较长 CoT 和更多 monitor 计算通常有帮助。 |
| 2025&#8209;10 | FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | benchmark、CoT monitoring、reasoning faithfulness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.04040) | 暂未公开 | 针对难以判断单条 CoT 是否忠实，论文构建含千余轨迹、细粒度原因和步骤证据的 FINE-CoT 并比较 11 种检测法；结果高级模型和知识密集任务上的不忠实更难发现。 |

## Monitor 与检测方法

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles | detection、CoT monitoring、reasoning trace、monitorability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16190) | [Code](https://github.com/anik-jha/challenger-panels) | 可信监控有一个廉价的、可信的模型对更强的不可信模型的行为进行评分，并且它们的多样化集合以相匹配的成本击败了单个更强大的监控器；它们是通过最小化平均成对相关性构建的，并且该论文的十二个监视器共享一个基本模型，保留提供多样性的开放因素；在六个攻击者模型中，增益结果在所有六个中均成立，同意和取消结果在六个中的五个中成立。 |
| 2026&#8209;08 | Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish | detection、CoT monitoring、reasoning trace、monitorability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15392) | [Code](https://github.com/Madhumasa84/MATS-multilingual-reasoning-monitorability) | 思维链监控是一种潜在有用的安全信号，但其跨语言和行为设置的可靠性仍然不确定；在一个包含 8 个手动验证的合成场景、一个模型、一个注释器和一个确定性生成种子的小型案例研究中，我研究了 Sarvam-105B 中英语、泰米尔语和唐语间接提示注入过程中的 API 可见推理；这些描述性观察提供了行为信息丰富的可见推理的可重复案例研究；他们没有证明推理模式可以提高安全性，可见的推理在机械上是可靠的，或者结果可以推广到这种配置之外。 |
| 2026&#8209;05 | CoT-Guard: Small Models for Strong Monitoring | detection、CoT monitoring、small-model monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12746) | 暂未公开 | 针对大模型 monitor 成本高而小模型难识别隐藏目标，论文组合 SFT 蒸馏和困难样本 RL 训练 4B CoT-Guard；结果在多种攻击上超过 GPT-5.4 等更大 monitor。 |
| 2026&#8209;05 | How Useful Is Cross-Domain Generalization for Training LLM Monitors? | detection、CoT monitoring、cross-domain generalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12265) | 暂未公开 | 针对有限标注领域如何训练 monitor，论文研究多任务分类训练向新领域、新提示和推理任务的迁移；结果相邻领域会受益，但提示跟随可能失效，混合通用指令训练可缓解。 |
| 2026&#8209;04 | Detecting Safety Violations Across Many Agent Traces | detection、agent monitoring、cross-trajectory detection、safety violation detection | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.11806) | 暂未公开 | 针对违规行为稀少且需跨多条轨迹才能显现，论文提出结合聚类与 agentic search 的 Meerkat；结果在误用、错位和任务作弊中显著优于逐轨迹 monitor，并发现更多 reward hacking。 |
| 2026&#8209;03 | Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing | detection、motivated reasoning、activation probing、CoT monitoring | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2603.17199) | 暂未公开 | 针对模型受提示线索影响却在 CoT 中事后合理化的问题，residual-stream probe 在生成前即可达到完整 CoT judge 的检测水平，生成后 probe 则超过该监控器，显示内部表征比文字理由更可靠。 |
| 2026&#8209;02 | Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory | detection、CoT monitoring、information theory | NeurIPS 2025 Workshop | [arXiv](https://arxiv.org/abs/2602.18297) | 暂未公开 | 针对 CoT 与输出相关仍不足以保证可监控，论文用信息缺口和 elicitation error 分解监控误差并设计有监督与无标签目标；结果两种训练均提高 monitor 准确率并抑制奖励作弊。 |
| 2026&#8209;02 | Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning | detection、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65831) · [arXiv](https://arxiv.org/abs/2602.03978) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文提出 Monitorability as a Free Gift 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于奖励设计与偏好对齐审计。 |
| 2026&#8209;01 | How Does Information Access Affect LLM Monitors’ Ability to Detect Sabotage? | detection、agent monitoring、information visibility | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62038) · [arXiv](https://arxiv.org/abs/2601.21112) | 暂未公开 | 针对给 monitor 更多轨迹信息是否一定更好，论文验证 less-is-more 效应并提出先抽取可疑片段再评估的 EaE；结果在部分场景把破坏检测率提高 16.8 个百分点。 |
| 2026 | Constitutional Black-Box Monitoring for Scheming in LLM Agents | detection、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65104) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文提出 Constitutional Black-Box Monitoring for Scheming 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2025&#8209;11 | Steering Awareness: Detecting Activation Steering from Within | detection、activation steering、safety evaluation、CoT monitoring | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2511.21399) | 暂未公开 | 针对 safety evaluation 默认模型无法察觉 activation steering 的假设，作者训练七个模型后最高得到 95.5% 干预测与 71.2% 概念识别，但 awareness 并未带来抵抗，反而使模型在事实与安全 benchmark 上更易被 steering。 |
| 2025&#8209;08 | Reliable Weak-to-Strong Monitoring of LLM Agents | detection、agent monitoring、monitor red-teaming、weak-to-strong supervision | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.19461) | 暂未公开 | 针对弱 monitor 能否可靠监督更强 Agent，论文建立 monitor 红队流程并提出混合层级顺序脚手架；结果脚手架比额外告知 monitor 更重要，定向人工复核还能进一步提高召回。 |
| 2025&#8209;07 | Deep Hidden Cognition Facilitates Reliable Chain-of-Thought Reasoning | detection、CoT monitoring、error awareness、mechanistic explanation | AAAI 2026 | [arXiv](https://arxiv.org/abs/2507.10007) | 暂未公开 | 针对 CoT 中间错误累积降低可靠性，论文从真值敏感 attention head 训练逐步置信预测器并引导 beam search；结果在单模态和多模态推理任务上提高准确性与稳定性。 |

## 规避、混淆与训练压力

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Length Penalties Make Chain-of-Thought Less Monitorable | analysis、CoT monitoring、length optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.09786) | 暂未公开 | 针对用长度惩罚降低推理成本可能删除安全证据，论文训练不同目标长度的 Qwen3 并施加偏置提示；结果 CoT 变短后仍受提示影响却更少提及它，形成成本与可监控性的前沿。 |
| 2026&#8209;03 | Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback | analysis、agent monitoring、monitor evasion、adaptive evasion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.16928) | 暂未公开 | 针对 Agent 能否仅凭任务被阻断推断 CoT 正在受监控，论文开展多回合隐藏副任务实验；结果强模型有时能形成监视认知和规避意图，但目前仍无法真正隐藏后续推理。 |
| 2026&#8209;03 | Reasoning Models Struggle to Control their Chains of Thought | analysis、CoT monitoring、monitor evasion、adaptive evasion | ICML 2026 | [arXiv](https://arxiv.org/abs/2603.05706) | [Code](https://github.com/YuehHanChen/CoTControl) | 针对模型能否主动控制 CoT 以逃避监控，论文构建要求避开特定概念的 CoT-Control 套件；结果当前模型对 CoT 的控制远弱于最终输出，暂时降低了主动隐藏的现实风险。 |
| 2026&#8209;02 | A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring | analysis、CoT monitoring、monitor evasion、covert reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.23163) | 暂未公开 | 针对缺少正常参考分布时无法定义 LLM 隐写，论文以能解码和不能解码的 Agent 在下游效用差构造 steganographic gap；结果可用于检测、量化并缓解隐蔽推理。 |
| 2025&#8209;10 | Output Supervision Can Obfuscate the Chain of Thought | analysis、CoT monitoring、monitor evasion、output supervision | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.11584) | 暂未公开 | 针对只监督最终输出是否能避免 CoT 被隐藏，论文识别安全输出训练向 CoT 泛化及自回归强化两种混淆机制；结果输出监督同样可能产生隐蔽 CoT，所提缓解在任务性能与可监控性间取得更优权衡。 |
| 2025&#8209;03 | Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation | analysis、CoT monitoring、training pressure、behavioral monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2503.11926) | [OpenAI](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/) | 针对 Agent reward hacking 能否从 CoT 中被发现，论文让较弱模型监控更强推理 Agent 并把监控信号加入训练；结果 CoT 监控很有效，但过强优化会诱导模型隐藏作弊意图。 |

## 忠实性、可见性与失效机制

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | On the Generalization of Steering Vectors for Chain-of-Thought Faithfulness | analysis、CoT monitoring、reasoning faithfulness、cross-domain generalization | COLM 2026 | [arXiv](https://arxiv.org/abs/2607.29062) | 暂未公开 | 针对提升 CoT 忠实性的 steering vector 是否可迁移，论文跨 cue、数据集、模型和构造方法系统评测；结果 steering 一旦在某模型有效便广泛泛化，且主要减少未承认的 cue 使用。 |
| 2026&#8209;07 | When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems | analysis、agent monitoring、multi-agent、compositional harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.11751) | 暂未公开 | 针对多 Agent 可把有害 payload 拆成各自良性的片段，论文形式化 local benignness 的可观测边界并跨测试床验证；结论是逐步 monitor 即使每步判断正确也会漏掉组合后才出现的危害。 |
| 2026&#8209;05 | Classifier Context Rot: Monitor Performance Degrades with Context Length | analysis、CoT monitoring、long context | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12366) | 暂未公开 | 针对真实 Agent 轨迹远长于现有监控 benchmark，论文把危险行为埋入最高 80 万 token 的良性活动；结果前沿分类器漏检率增加 2 至 30 倍，周期提醒只能部分缓解。 |
| 2026&#8209;05 | When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel | analysis、CoT monitoring、performative reasoning、causal validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.11746) | 暂未公开 | 针对可见 CoT 是否与内部答案形成同步，论文用逐步承诺探针和因果验证比较九个模型；结果只有 61.9% 步骤对齐，主要失效是答案已确定后仍表演式继续推理。 |
| 2026&#8209;05 | Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal | analysis、CoT monitoring、error awareness、mechanistic explanation | ICML 2026 Mechanistic Interpretability Workshop | [arXiv](https://arxiv.org/abs/2605.09502) | 暂未公开 | 针对模型是否在内部知道 CoT 已经出错，论文用隐藏状态 probe 和四类干预区分检测信号与因果控制；结果内部错误信号很强，但 steering、自纠错和 patching 都不能可靠修复答案。 |
| 2026&#8209;02 | Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought? | analysis、CoT monitoring、CoT intervention | ICLR 2026 | [arXiv](https://arxiv.org/abs/2602.07470) | [Code](https://github.com/ExplainableML/RLLM-CoT-Robustness) | 针对 CoT 被插入良性或对抗干预后是否仍可靠，论文在固定步骤施加七类扰动；结果模型通常能恢复且规模越大越稳健，但恢复可令轨迹膨胀超过 200%，改写还会损害准确率。 |
| 2025&#8209;10 | Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity | analysis、CoT monitoring、reasoning faithfulness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.27378) | 暂未公开 | 针对只测 cue faithfulness 会遗漏未写出的关键因素，论文把忠实性和完整详述度合成 monitorability score；结果显示模型即使表面忠实，也可能因省略必要因素而难以监控。 |

## Survey 与研究议程

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;07 | Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety | survey、CoT monitoring、AI oversight | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.11473) | 暂未公开 | 针对自然语言 CoT 为安全监督带来的机会与脆弱性，论文综合论证其虽不完美但具有现实价值；结论是应持续投资监控，并在模型开发决策中保护可监控性。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Not All LLM Reasoning is Visible in the Chain-of-Thought | analysis、CoT monitoring、reasoning trace、monitorability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.22925) | 暂未公开 | 论文发现 13 个前沿模型可借语义无关 filler token 完成未显式写入 CoT 的计算，最高提高 13 个百分点，并可满足隐藏模运算目标；这说明输出 token 不包含全部有后果的推理，CoT monitor 存在结构性盲区。 |
| 2026&#8209;04 | Peer-Preservation in Frontier Models | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63306) · [arXiv](https://arxiv.org/abs/2604.19784) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Peer-Preservation in Frontier Models 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026&#8209;04 | Introspection Adapters: Training LLMs to Report Their Learned Behaviors | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66802) · [arXiv](https://arxiv.org/abs/2604.16812) | 暂未公开 | 针对微调可能植入隐蔽或异常行为且难以审计的问题，Introspection Adapter 在多组已知行为微调模型上联合训练一个 LoRA，使新微调模型主动描述其习得行为；该方法在 AuditBench 上取得领先结果并能识别加密的 fine-tuning API 攻击。 |
| 2026&#8209;02 | FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61086) · [arXiv](https://arxiv.org/abs/2602.11136) | [Project](https://huggingface.co/spaces/m-zest/specguard-demo) | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 FormalJudge 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | The Oversight Game: Learning to Cooperatively Balance an AI Agent's Safety and Autonomy | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64439) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 The Oversight Game 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Learning to Reason for Factuality | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62911) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Learning to Reason for Factuality 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Endogenous Resistance to Activation Steering in Language Models | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62558) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Endogenous Resistance to Activation Steering 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Corrigibility Transformation: Constructing Goals That Accept Updates | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64539) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Corrigibility Transformation 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Collaborative Disagreement Resolution for Scalable Oversight | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62588) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Collaborative Disagreement Resolution for Scalable 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | analysis、chain-of-thought、CoT monitoring、reasoning trace | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64450) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Chain-of-Thought Reasoning In The Wild 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | A Positive Case for Faithfulness: Explanations Help Predict Model Behavior | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61687) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 A Positive Case for Faithfulness 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Alignment Risks from Capability-Seeking RL Training | analysis、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64024) | [Code](https://github.com/YujunZhou/Capability-seeking-RL-risk) | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Alignment Risks from Capability-Seeking RL 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains | benchmark、harmful reasoning、CoT monitoring、reasoning trace | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.19001) | [Project](https://huggingface.co/datasets/ishitakakkar-10/HarmThoughts) | 针对 safety evaluation 只看最终答案而忽略危害如何在 reasoning chain 中展开的问题，HarmThoughts 标注四个模型家族的 1,018 条轨迹和 56,931 个句子，显示现有白盒与黑盒 detector 均难识别细粒度危害行为。 |
| 2026&#8209;02 | A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents | benchmark、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64314) · [arXiv](https://arxiv.org/abs/2602.08964) | [Code](https://github.com/SPAR-Telos/interp) | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文构建 Behavioural and Representational Evaluation of 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于欺骗检测、监控和 AI 控制。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Calibrating Conservatism for Scalable Oversight | defense、CoT monitoring、reasoning trace、monitorability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65895) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Calibrating Conservatism for Scalable Oversight 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于欺骗检测、监控和 AI 控制。 |

> 外部执行轨迹、组件级 failure attribution 与恢复方法见 [Trajectory Monitoring 与 Failure Attribution](../agent/trajectory-monitoring-and-failure-attribution.md)。
