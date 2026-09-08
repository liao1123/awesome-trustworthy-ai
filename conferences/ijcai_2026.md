# IJCAI-ECAI 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [LLM 安全、越狱与有害内容](#llm-安全越狱与有害内容)
- [具身智能体、安全决策与高风险部署](#具身智能体安全决策与高风险部署)
- [后门与投毒攻击](#后门与投毒攻击)
- [隐私泄漏、机器遗忘与数据保护](#隐私泄漏机器遗忘与数据保护)
- [对抗攻击、检测与鲁棒防御](#对抗攻击检测与鲁棒防御)
- [生成内容真实性与多媒体取证](#生成内容真实性与多媒体取证)
- [水印、模型身份与版权保护](#水印模型身份与版权保护)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | 35th International Joint Conference on Artificial Intelligence and 28th European Conference on Artificial Intelligence (IJCAI-ECAI 2026) |
| 举办时间与地点 | Workshops / Tutorials：2026-08-15 至 2026-08-17，University of Bremen；Main Conference：2026-08-18 至 2026-08-21，Congress Centrum Bremen；Bremen, Germany |
| 官方网站 | [IJCAI-ECAI 2026](https://2026.ijcai.org/) |
| 官方录用列表 | [Accepted Papers](https://2026.ijcai.org/accepted-papers/) |
| 正式论文集 | 截至核验日 IJCAI proceedings 总卷尚未单独上线；官网为每篇论文提供官方托管的 Preprint PDF |
| 检查范围 | Main Track、五个 Special Tracks 与 Survey Track，共 902 篇；数据截至 2026-08-23 |

## 关键节点

除会议日期外，以下 deadline 均为 23:59 AoE（UTC-12）。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Abstract submission deadline | 2026-01-12 | [Main Track CFP](https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-main-track/) |
| Full paper submission deadline | 2026-01-19 | [Main Track CFP](https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-main-track/) |
| Phase I / summary-reject notification | 2026-03-04 | [Important Dates](https://2026.ijcai.org/important-dates/) |
| Author response | 2026-04-07 至 2026-04-10 | [Important Dates](https://2026.ijcai.org/important-dates/) |
| Paper notification | 2026-04-29 | [Important Dates](https://2026.ijcai.org/important-dates/) |
| Main Track camera-ready | 2026-05-20 | [Important Dates](https://2026.ijcai.org/important-dates/) |
| AI and Social Good camera-ready | 2026-06-03 | [AI and Social Good CFP](https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-ai4good/) |
| Survey Track camera-ready | 2026-06-10 | [Survey Track CFP](https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-survey/) |
| Workshops / Tutorials | 2026-08-15 至 2026-08-17 | [At a Glance](https://2026.ijcai.org/at-a-glance2/) |
| Main Conference | 2026-08-18 至 2026-08-21 | [At a Glance](https://2026.ijcai.org/at-a-glance2/) |

## 筛选说明

- 官方论文总数：902（Main Track 712、AI and Health 47、AI and Robotics 11、AI and Social Good 52、AI4Tech 25、Human-Centred AI 10、Survey Track 45）。
- 范围取舍：官方 All Tracks 共 989 项；本文件排除不同录用机制或非本届原创常规论文范围的 Journal Track 6、Sister Conferences Best Papers 17、Early Career Spotlight 14 和 Demonstrations Track 50，保留上述七个正式投稿 track。
- 初筛候选：157（标题高召回宽筛 140 篇，再用摘要中的精确安全语义补入 17 篇）。
- 最终收录：58（Main 46、五个 Special Tracks 9、Survey 3）。
- 收录口径：逐篇阅读官网摘要，只保留把 LLM/智能体安全、恶意使用、攻击与防御、隐私泄漏、安全约束、内容真实性、模型身份或可核验缓解作为核心问题的论文。
- 边界案例：一般 alignment、fairness、bias、常规差分隐私和 machine unlearning、用 adversarial loss 改善普通任务，以及 AI for safety/security 但不研究 AI 系统风险的论文从严排除；传统对抗鲁棒性仅在摘要明确给出攻击或防御 threat model 时保留。

## 论文分类

### LLM 安全、越狱与有害内容

### 1. BEACON: Budget-Efficient Discovery of Policy Violations in Large Language Models via Cognitive-Guided Monte Carlo Tree Search

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2985.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`benchmark`、`LLM red teaming`、`policy violation`、`query budget`

- 🎯 **研究动机**：多数红队方法只优化攻击成功率并反复探测窄漏洞集，固定预算下浪费查询、罕见关键违规类别未被探索
- 🔬 **研究方法**：BEACON 把安全测试视为预算约束的失败发现问题，用认知引导 MCTS 在固定预算下导航违规搜索空间，尽早发现多样违规
- 📌 **结论**：更早发现失败并在政策违规类别上取得更高覆盖，倡导以发现效率而非仅 ASR 评估安全测试

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Systematic safety evaluation of large language models must uncover diverse policy violations under tight query budgets. However, most redteaming methods optimize attack success rate and repeatedly probe a narrow set of vulnerabilities, yielding redundant failures and leaving rarer yet critical violation categories unexplored. Under fixed budgets, such inefficient exploration delays the first discovery and limits category coverage. To address these limitations, we propose the BudgetEfficient Adaptive Cognitive Offense Navigator (BEACON), a budget-aware safety testing framework that uses Cognitive-Guided Monte Carlo Tree Search to navigate the violation search space under fixed budgets. BEACON innovatively approaches safety testing as a budget-constrained failure discovery process, aiming to identify diverse safety violations as early as possible within a fixed query budget. It also provides an efficiency-oriented evaluation perspective that measures early discovery and harm category coverage under budget constraints. Experiments on standard benchmarks and frontier LLMs show that BEACON discovers failures earlier and achieves higher coverage across policy violation categories. These results underscore the value of evaluating safety testing through discovery efficiency rather than attack success rate alone. Warning: This paper contains examples of harmful language and images, and reader discretion is recommended.

</details>

### 2. BERM: Low-Overhead Prompt-Injection Detection via In-Situ Benign Representation Modeling

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/8133.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`analysis`、`prompt injection`、`benign manifold`、`low-latency guardrail`、`lightweight guard model`

- 🎯 **研究动机**：现有提示注入防御依赖脆弱启发式或调用昂贵辅助模型，无法兼顾鲁棒与低延迟
- 🔬 **研究方法**：BERM 对 host LLM prefill 阶段提取的内部表征原位建模：联合对比学习良性表征紧致流形以最大化与恶意表征分离，轻量分类器推理时原位检测
- 📌 **结论**：F1 比最佳先前工作高 5.2 个百分点，同时快 12 倍以上，增量推理开销近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world deployment of large language models (LLMs) necessitates a robust and low-latency approach to detect prompt injections; existing lowoverhead methods fail to simultaneously boost robustness and reduce latency. Current defenses for prompt injection either rely on brittle heuristics or invoke costly auxiliary models, imposing a significant runtime burden. We introduce BERM, a lightweight framework that performs in-situ detection by modeling a host LLM’s internal representations extracted during prefill, adding negligible overhead. Our approach trains a lightweight classifier atop the LLM by learning a compact manifold of benign representations via joint contrastive learning to maximize the separation from malicious representations. At inference, this pre-trained classifier enables in-situ detection without invoking auxiliary guard models. On a diverse landscape of prompt injection attacks, our framework establishes a new state-of-the-art, achieving an F1-score 5.2 percentage points (pp) higher than the best prior work. Critically, BERM achieves this while being over 12x faster, reducing incremental inference overhead to near-zero.

</details>

### 3. Detoxifying Large Language Models via Localized Feature Editing with Sparse Autoencoders

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2785.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`analysis`、`LLM detoxification`、`sparse autoencoder`、`feature steering`、`SAE feature editing`

- 🎯 **研究动机**：神经元多义性使干预纠缠无关概念，对毒性特征的无差别干预以流畅度退化为代价
- 🔬 **研究方法**：DeLFE 从标签引导的 SAE 特征子集学毒性子空间，逐 token 跟踪毒性触发风险并经 flow matching 特征变换把毒性特征推离子空间，配三种干预时机与强度策略
- 📌 **结论**：跨不同规模与多样基座模型实现强去毒效果并保持高生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) powerful generative capabilities also pose significant risks, underscoring the need for effective detoxification methods to ensure safer deployment. Due to the polysemantic nature of LLM neurons, recent neuron intervention methods inevitably entangle unrelated concepts, compromising generation quality and interpretability. Sparse Autoencoders (SAEs) have opened new horizons for decomposing model activations into monosemantic features, offering interpretability and targeted feature-level steering. Empirical findings reveal that, despite capturing interpretable features, indiscriminate interventions on toxicity-related features expose the fragility of LLMs, achieving toxicity mitigation at the cost of degraded fluency. Building upon this finding, we propose DeLFE, a lightweight controlled detoxification approach that identifies specific toxic features across model layers and performs targeted interventions on them. DeLFE learns toxicity subspaces from label-guided SAE feature subsets to characterize toxic v.s. non-toxic activation patterns. When auto-completing a response token-bytoken, DeLFE tracks the toxicity-triggering risks and steers toxic features away from the subspace via a flow-matching feature transformation. We further design three feature-level strategies that adjust intervention timing and strength to reconstruct the target model’s original activations. Extensive experiments demonstrate that our method achieves strong detoxification effectiveness while maintaining high generation quality across models of varying sizes and diverse base LLMs.

</details>

### 4. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`benchmark`、`detection`、`analysis`、`LLM jailbreak`、`structured explanation`、`safety assessment`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 5. HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation

📄 [arXiv](https://arxiv.org/abs/2601.13864) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1080.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`benchmark`、`secure code generation`、`hardware CWE`、`execution testing`

👤 **作者**：Qirui Chen、…、Jian Yang

- 🎯 **研究动机**：LLM 硬件/固件代码生成评测只重功能正确性，忽视部署后可致灾难的安全漏洞
- 🔬 **研究方法**：HardSecBench 含 924 个任务覆盖 Verilog RTL 与固件 C、76 个硬件相关 CWE，多智能体管线以执行证据为基础做可靠评测
- 📌 **结论**：LLM 常满足功能要求却留下安全风险，且安全表现随提示方式波动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for hardware and firmware code generation, but existing studies primarily evaluate functional correctness while largely overlooking security. However, LLM-generated code that appears functionally sound may embed security flaws which could induce catastrophic damages after deployment. This critical research gap motivates us to design a benchmark for assessing security awareness under realistic specifications. In this work, we introduce HardSecBench, a benchmark with 924 tasks spanning Verilog Register Transfer Level (RTL) and firmware-level C, covering 76 hardware-relevant Common Weakness Enumeration (CWE) entries. Each task includes a structured specification, a secure reference implementation, and executable tests. To automate artifact synthesis, we propose a multi-agent pipeline that decouples synthesis from verification and grounds evaluation in execution evidence, enabling reliable evaluation. We evaluate diverse LLMs and find that they often satisfy functional requirements while leaving security risks. We also find that security results vary with prompting. These findings highlight pressing challenges and offer actionable insights for future advancements in LLM-assisted hardware design. Our data and code are available at https://github.com/chenqirui2002/HardSecBench.

</details>

### 6. Shot-Conditioned Vision-Language Adaptation for Effective Harmful Content Detection from Online Short Videos

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2149.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`harmful short video`、`shot adaptation`、`vision-language model`、`shot-conditioned adaptation`、`temporal moderation`

- 🎯 **研究动机**：短视频有害检测面临频繁剪辑切分与异常密度高度可变，现有 VLM 方法依赖刚性实例选择机制，无法适配不可预测的异常时长
- 🔬 **研究方法**：提出 SVLA：π 自适应策略动态估计镜头级异常密度替代刚性选择，配合镜头条件时间编码器与双路上下文 adapter，并构建含 7 类异常的 SVA 数据集
- 📌 **结论**：在 SVA 数据集上达到 SOTA，并在多样场景中全面超越对手方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Short video harmful content detection aims to automatically identify diverse anomalies from user-generated media. This task presents unique challenges due to frequent editing cuts and highly variable anomaly densities, limiting the effectiveness of traditional surveillance-based approaches. Moreover, existing Vision-Language Model-based approaches typically rely on rigid instance selection mechanisms that fail to adapt to the unpredictable duration of anomalies in such unconstrained videos. To address these issues, we propose SVLA, a Shot-conditioned Vision-Language Adaptation framework, for effectively detecting harmful contents from online short videos. Our approach introduces a novel π-adaptive strategy to dynamically estimate shot-level anomaly density, replacing rigid selection with calibrated supervision. Furthermore, we employ a shot-conditioned temporal encoder to respect video hierarchy and adopt a dual-path contextual adapter to resolve semantic ambiguity. To benchmark this task, we construct a new dataset (SVA) covering more genuine online short videos that involve seven anomaly categories. Experiments on the SVA dataset demonstrate that SVLA can achieve the state-of-the-art performance and outperform its competitors across diverse scenarios. Codes and datasets are available at: https://github.com/xushuai7/IJCAI-SVLA.

</details>

### 7. Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`role-playing agent`、`jailbreak`、`self-evolution`、`persona-aware guard`、`retrieved safety rule`

- 🎯 **研究动机**：角色扮演 agent 越忠于人设越易被越狱，训练时方案维护成本高、损害角色内行为且对闭源模型不可行
- 🔬 **研究方法**：提出免训练双循环对抗自进化：攻击循环合成渐进更强的越狱提示，防御循环把失败蒸馏为全局安全规则、角色约束与安全角色示例的层级知识库供推理时检索组合
- 📌 **结论**：多个专有 LLM 上角色保真与抗越狱均超过强基线，并对未见角色与攻击提示鲁棒泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based role-playing has rapidly improved in fidelity, yet stronger adherence to persona constraints commonly increases vulnerability to jailbreak attacks, especially for risky or negative personas. Most prior work mitigates this issue with trainingtime solutions (e.g., data curation or alignmentoriented regularization). However, these approaches are costly to maintain as personas and attack strategies evolve, can degrade in-character behavior, and are typically infeasible for frontier closed-weight LLMs. We propose a training-free Dual-Cycle Adversarial Self-Evolution framework with two coupled cycles. A Persona-Targeted Attacker Cycle synthesizes progressively stronger jailbreak prompts, while a Role-Playing Defender Cycle distills observed failures into a hierarchical knowledge base of (i) global safety rules, (ii) persona-grounded constraints, and (iii) safe in-character exemplars. At inference time, the Defender retrieves and composes structured knowledge from this hierarchy to guide generation, producing responses that remain faithful to the target persona while satisfying safety constraints. Extensive experiments across multiple proprietary LLMs show consistent gains over strong baselines on both role fidelity and jailbreak resistance, and robust generalization to unseen personas and attack prompts.

</details>

### 8. Towards Comprehensive Post Safety Alignment of Large Language Models via Safety Patching

📄 [arXiv](https://arxiv.org/abs/2405.13820) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7176.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`post safety alignment`、`over-refusal`、`safety patch`、`post-safety alignment`、`jailbreak patch`

👤 **作者**：Weixiang Zhao、…、Ting Liu

- 🎯 **研究动机**：现有安全对齐 LLM 机制脆弱失衡：仍可被诱导生成不安全回复、对安全输入过度拒绝、对齐后效用受损
- 🔬 **研究方法**：提出 SafePatching 后安全对齐框架：在有害数据上开发分别增强安全与缓解过度安全的两类补丁并无缝集成到目标 LLM 主干
- 📌 **结论**：在 LLaMA-2/3、Gemma、Mistral 四个对齐模型上实现比基线更全面的后安全对齐，并在持续对齐场景中保持优势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) has been gaining increasing attention. However, current safety-aligned LLMs suffer from the fragile and imbalanced safety mechanisms, which can still be induced to generate unsafe responses, exhibit over-safety by rejecting safe user inputs, and fail to preserve general utility after safety alignment. To this end, we propose a novel post safety alignment (PSA) method to address these inherent and emerging safety challenges, including safety enhancement, over-safety mitigation, and utility preservation. In specific, we introduce SAFEPATCHING, a novel framework for comprehensive PSA, where two distinct safety patches are developed on the harmful data to enhance safety and mitigate oversafety concerns, and then seamlessly integrated into the target LLM backbone without compromising its utility. Extensive experiments on four representative aligned LLMs, including LLaMA-2/3, Gemma and Mistral, show that SAFEPATCHING achieves a more comprehensive PSA than baseline methods, further optimizing the balance between being helpful and harmless in current aligned LLMs. Also, SAFEPATCHING demonstrates its superiority in continual PSA scenarios.

</details>
### 具身智能体、安全决策与高风险部署

### 9. A Survey on Value Alignment in Agentic AI Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/SV146.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=survey-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`survey`、`agentic AI`、`value alignment`、`multi-agent coordination`

- 🎯 **研究动机**：agentic AI 的价值失配带来情境化风险，价值对齐缺乏跨层框架
- 🔬 **研究方法**：构建 L0 普世价值、L1 文化行业价值、L2 情境价值的多层框架，沿技术栈分析：LLM 层的预训练／后训练价值注入、单 Agent 层的 profile 记忆与规划行动、多 Agent 层的通信优化与多目标 RL 协同对齐
- 📌 **结论**：系统梳理多层对齐评测数据集与方法，提出 Agent 间价值协调、高质量场景数据共享与博弈论协议对齐等未来方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the evolution of artificial intelligence (AI) paradigms towards agentic AI, the widespread integration of large language models (LLMs) enhances system capabilities while also introducing situational risks and challenges of value misalignment, making value alignment in agentic AI systems a critical issue. This paper constructs a multi-level value framework encompassing L0 (universal values), L1 (cultural and industry values), and L2 (context-specific values). Guided by this framework, we conduct an in-depth analysis along the technical stack: at the LLM level, we examine value injection mechanisms through pretraining and post-training; at the single-agent level, we focus on representation and injecting values to agents, Profiles and memory, and planning and action; at the multi-agent level, we summarize collaborative alignment methods such as communication strategy optimization and multiobjective reinforcement learning. Following a systematic review of existing datasets and methods for multi-level alignment evaluation, we outline future research directions, including inter-agent value coordination mechanisms, high-quality scenario data sharing, game-theoretic design for value alignment in agent interaction and communication protocol alignment—aiming to establish a more systematic and dynamic evaluation framework and to promote robust and trustworthy value consensus in agentic AI systems within social collaboration.

</details>

### 10. Counterfactual Reasoning for Responsibility Attribution in Probabilistic Multi-Agent Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2007.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`multi-agent system`、`responsibility attribution`、`counterfactual reasoning`

- 🎯 **研究动机**：多智能体系统中各 agent 对结果的因果贡献量化是设计与分析的基础难题
- 🔬 **研究方法**：把系统建模为并发随机多人博弈，定义追溯式反事实责任并用 Shapley 值分配（证明公平性与一致性）；以 Nash 均衡为解概念计算权衡责任与期望回报的稳定策略
- 📌 **结论**：形式化框架同时支持责任感知系统的验证与策略推理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Responsibility allocation—determining the extent to which agents causally contribute to outcomes— is a fundamental challenge in the design and analysis of multi-agent systems. In this work, we model such systems as concurrent stochastic multiplayer games and introduce a notion of retrospective (backward) counterfactual responsibility, which quantifies an agent’s causal contribution to outcomes resulting from a given strategy profile. To allocate responsibility among agents, we utilise the Shapley value and formally show that this method satisfies key desirable properties, including fairness and consistency. Building on this foundation, we propose a formal framework that supports both verification and strategic reasoning in responsibilityaware multi-agent systems. Furthermore, by adopting Nash equilibrium as the solution concept, we demonstrate how to compute stable strategy profiles in which agents trade off responsibility against expected reward.

</details>

### 11. DEPLOY-RL: Active Boundary Discovery and Conservative Certification for Deployable Reinforcement Learning in Safety-Critical Continuous Processes

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T22.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`RL certification`、`boundary discovery`、`fail-safe deployment`

- 🎯 **研究动机**：RL 策略很少上产安全关键流程——无法带统计保证地回答该策略部署是否安全
- 🔬 **研究方法**：DEPLOY-RL 训练后认证：契约耦合采集函数把采样集中到认证关键边界（约 2 倍采样效率），conformal risk control 给有限样本 false-go 保证（不超过 α），三路决策配 PID 或 MPC 故障安全回退
- 📌 **结论**：造纸数字孪生与 Tennessee Eastman 上 false-go 率 4.4%（最佳基线 8.6%）且保留 88.6% 策略覆盖率，是 14 个基线中唯一 false-go 小于 5% 且覆盖超 85% 的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) policies often outperform classical controllers in simulation, yet rarely reach production in safety-critical processes. The barrier is that there is no principled way to answer “Is this policy safe to deploy?” with statistical guarantees. We introduce DEPLOY-RL, a post-training certification framework built on one key insight: deployment certification requires discovering where failures occur (boundary discovery), not measuring how much everywhere (uniform reconstruction). Our contributions: (1) a contract-coupled acquisition function that concentrates sampling on certification-critical boundaries, achieving ≈ 2× sample efficiency with a semiempirical ambiguity reduction bound (domaincalibrated convergence guarantee); (2) conformal risk control providing finite-sample false-go guarantees (≤ α) under explicit deployment contracts; (3) a three-way decision framework (Deploy/NoDeploy/Abstain) with fail-safe PID/MPC fallback. In simulations on papermaking (industrial digital twin) and Tennessee Eastman (public benchmark), DEPLOY-RL achieves 4.4% false-go rate (vs. 8.6% for the best baseline) while retaining 88.6% policy coverage, the only method achieving <5% false-go with >85% coverage among 14 baselines under our evaluation protocol.

</details>

### 12. Knowing When Not to Predict: Self Supervised Learning and Abstention for Safer DR Screening

📄 [arXiv](https://arxiv.org/abs/2605.19133) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H96.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-health)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`medical abstention`、`calibration`、`selective prediction`

👤 **作者**：Muskaan Chopra、Lorenz Sparrenberg、Jan H. Terheyden、Rafet Sifa

- 🎯 **研究动机**：医学图像模型只看精度不足，安全筛查还需知道何时弃权转临床复核
- 🔬 **研究方法**：固定微调协议下评测多个 SSL checkpoint 的校准置信、覆盖率、选择准确率与选择性 macro-F1
- 📌 **结论**：SSL 预训练比从头训练改善选择性预测；但精度饱和后选择性表现在 checkpoint 间仍大幅波动，更长预训练不必然更可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) is now a standard way to pretrain medical image models, but performance is still mostly judged by downstream accuracy. For safety-critical screening tasks such as diabetic retinopathy grading, this is not enough: a model must also know when its predictions are unreliable and defer uncertain cases for clinical review. In this work, we examine how the length of SSL pretraining influences calibrated confidence and confidence-based abstention. We evaluate multiple SSL checkpoints under a fixed fine-tuning protocol and assess calibrated confidence, coverage, selective accuracy, and selective macro-F1. Across datasets and data regimes, SSL pretraining improves selective prediction compared to training from scratch. Unlike prior SSL studies that primarily evaluate downstream accuracy or AUROC, we analyze how SSL pretraining duration influences confidence behavior under calibrated confidence-based abstention. However, once accuracy saturates, selective performance can still change markedly across checkpoints, and longer pretraining does not consistently improve reliability. These results underscore the importance of abstention-aware evaluation and suggest that pretraining length should be treated as an important reliability-related design choice rather than only a computational detail. Code is available at https://github.com/ muskaan712/ijcai-knowing-when-not-to-predict.

</details>

### 13. Persistent Safety Set Guided Offline Safe Reinforcement Learning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7583.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`offline safe RL`、`control barrier function`、`persistent safety`

- 🎯 **研究动机**：离线安全 RL 无法探索且价值误差会经不安全状态区域传播
- 🔬 **研究方法**：用广义 Bellman 算子学控制屏障函数得到可无限保持安全的持久安全集；提出动力学不确定下仍保安全的新 CBF；奖励最大化算法利用安全集做 critic 估计
- 📌 **结论**：标准基准上安全性 SOTA、违规更少且回报有竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Offline safe reinforcement learning learns highreturn policies that satisfy hard safety constraints using only a pre-collected dataset. This setting is challenging due to the inability to explore, and the risk of propagating value errors through unsafe state-space regions. To address this, first, we characterize the safe state region by developing a framework for learning control barrier functions (CBFs) using a novel generalized Bellman operator, yielding a persistent safety set, from which the agent can remain safe indefinitely. Second, we show that several existing safety set estimation methods (e.g., reachability-constrained RL) can be formulated within our CBF learning framework, highlighting its generality. We further propose a new CBF that ensures safety under environment dynamics uncertainty, unlike standard CBFs designed for deterministic settings. Third, we propose a new reward maximization algorithm that effectively exploits our learned persistent safety set for reward critic estimation. Empirical results on standard benchmarks show that our approach achieves stateof-the-art safety with fewer constraint violations while maintaining competitive returns.

</details>

### 14. Propagating Unsafe Actions in LLM Controlled Multi-Robot Collaboration via Single Robot Compromise

📄 [arXiv](https://arxiv.org/abs/2605.15641) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3903.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`multi-robot system`、`LLM planner`、`compromise propagation`

👤 **作者**：Zhen Huang、Zhihuang Liu、Mengxuan Luo、Weishang Wu、Zhiping Cai

- 🎯 **研究动机**：LLM 控制的多机器人协作中经机器人间通信传播的安全风险基本未被探索
- 🔬 **研究方法**：攻击者仅与单个入口机器人交互，被攻陷者经对等通信传播恶意意图致系统协同不安全动作，以服从性、传染性与隐蔽性量化
- 📌 **结论**：最强情形服从性达 1.00、传染性 0.90；最少 3.0 轮攻陷全部机器人且隐蔽性 0.81；紧急或权利冲突的权衡决策会放大风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used as general planners in embodied intelligence, enabling high level coordination and low level task planning for both single robot and multi-robot collaboration. This increasing reliance on embodied LLM planners also raises critical security concerns, since misaligned or manipulated instructions can be translated into physical actions. Prior work has studied such threats in single robot settings, while security risks in LLM controlled multi-robot collaboration, especially those propagated through inter robot communication, remain largely unexplored. To bridge this gap, we propose a novel attack paradigm for multi-robot system in which the adversary interacts with only a single entry robot. The compromised robot then propagates malicious intent through peer communication, leading to coordinated unsafe actions across the system. Our evaluation, covering high risk dimensions of dereliction of duty, privacy compromise, and public safety hazards, reveals a persistent safety alignment gap in multi-robot planners. We quantify this process with three metrics, obedience, infectiousness, and stealthiness. Experiments demonstrate both persistent attacker control and rapid propagation: obedience reaches 1.00 in the strongest cases, and infectiousness rises to 0.90. Notably, the attack is highly efficient, requiring as few as 3.0 rounds to compromise all the robots while maintaining a stealthiness score of 0.81. Such risks are amplified when robots must resolve trade offs in critical situations, such as emergencies or conflicts of rights, because the coordination mechanism can unintentionally allow adversarial instructions to override safety requirements. The code is available at https: //github.com/TheFatInsect/InfectBot.

</details>

### 15. Real-Time Multi-Robot Motion Planning with Safe-Interval Search and Learning-Guided Repair

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AIR73.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-robotics)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`multi-robot planning`、`collision avoidance`、`safe interval`

- 🎯 **研究动机**：共享空间的多机器人实时无碰撞轨迹规划计算上极具挑战，难以满足工业级实时性
- 🔬 **研究方法**：提出带受限目标预留的优先级安全区间路径规划（SIPP-PP），叠加 ML 引导的大邻域搜索（LNS）智能选择冲突消解动作
- 📌 **结论**：在复杂环境中数十毫秒内生成多机器人无碰撞路径，比扩散规划器等学习方法快两到三个数量级

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Motion planning among multiple robots in a shared space is a fundamental yet computationally challenging problem in robotics, with applications ranging from warehouse automation to autonomous fleets. In this work, we introduce a fast, scalable motion planner that achieves real-time, collisionfree trajectory planning via a two-staged algorithm combining deterministic search-based planning with machine learning-driven conflict resolution. We present a prioritized Safe Interval Path Planning algorithm (SIPP-PP) with a novel limited goal reservation strategy to prevent goal-blocking conflicts while allowing shared goal regions. We added a second layer of ML-guided Large Neighborhood Search (LNS) procedure to our SIPP-PP algorithm for improving success rates in highly congested environments via intelligent selection of conflict resolution actions. The result is a planning system that generates collision-free paths for multiple robots in complex environments within tens of milliseconds. For example, compared to recent advanced learning-based methods such as diffusion planners, our planner is two-to-three orders of magnitude faster. Our work demonstrates a multi-robot planner capable of real-time operation in dense scenarios, satisfying the stringent requirements of industrial applications such as drive units in fulfillment centers.

</details>

### 16. Responsibility in Multi-Agent Sequential Decision-Making: Comparing Human Judgments to Formal Models of Causal Attribution

📄 [arXiv](https://arxiv.org/abs/2608.04318) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/HC78.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-human-centred-ai)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`responsibility attribution`、`human judgment`、`sequential decision`

👤 **作者**：Nripsuta Ani Saxena、Stelios Triantafyllou、Goran Radanović

- 🎯 **研究动机**：高风险决策中失败原因与责任认定至关重要，形式化责任归因与人类判断是否一致缺乏检验
- 🔬 **研究方法**：基于修改版 Goofspiel 卡牌游戏开展大规模调查获取人类责任判断，评估多种实际因果框架下的责任归因方法
- 📌 **结论**：没有任何单一方法与人类判断持续一致，责任判断受智能体特定偏差与决策时信息量等因素显著影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing adoption of artificial intelligence in high-stakes decision-making, identifying the causes of outcomes–particularly failures–and determining who is responsible has become a critical concern. In this work, we examine how well formal definitions of responsibility attribution, grounded in the framework of actual causality, align with human judgments of responsibility. To this end, we conduct a large-scale survey to elicit human judgments of responsibility in multi-agent sequential decision-making scenarios, using a modified version of the card game Goofspiel. We evaluate multiple responsibility attribution methods, assess their alignment with human judgments about responsibility, and identify factors that significantly shape responsibility judgments. While no single responsibility attribution method consistently aligns with human responses, our findings highlight key factors that influence human responsibility judgments, including agent-specific biases and amount of information available to agents during decision-making.

</details>

### 17. Safe and Efficient Control: A Subgraph-Augmented Hierarchical Reinforcement Learning Framework for Dynamically Reconfigurable Battery Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T17.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`hierarchical RL`、`battery control`、`operational constraint`

- 🎯 **研究动机**：动态可重构电池系统控制因大拓扑动作空间盲目探索与复杂运行约束导致奖励稀疏，难以学到有效策略
- 🔬 **研究方法**：提出 SAHRL：高层策略定战略方向，子图增强的低层策略结合从拓扑结构提取的子图归纳偏置细化动作以满足约束
- 📌 **结论**：仿真与真实实验均实现安全高效均衡，真实应用中能量释放较常规方法提升 10.56%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dynamically Reconfigurable Battery (DRB) systems employ power electronic switches to create dynamic topologies. They enable effective management of cell inconsistencies through real-time adjustment of cell connections. However, existing DRB control methods struggle to learn effective strategies due to sparse rewards, which arise from blind exploration in large topological action spaces and complex operational constraints. This leads to ineffective policy learning, making safety and balancing performance difficult to ensure in practical applications. To this end, we propose a SubgraphAugmented Hierarchical Reinforcement Learning (SAHRL) framework. By combining hierarchical policies with topological structural knowledge, SAHRL effectively accelerates policy exploration and mitigates reward sparsity. Specifically, the high-level policy determines the strategic direction, while the subgraph-augmented low-level policy refines actions to meet operational constraints. The topological structural knowledge, extracted in the form of subgraphs and incorporated as an inductive bias, guides the agent focus on meaningful action patterns and reduce invalid exploration in the large action space. Extensive simulations and real-world experiments show that SAHRL achieves safe and efficient balancing. Notably, it increases the energy release by 10.56% compared to conventional methods in real-world applications.

</details>

### 18. Safe Multi-Objective Linear Bandits with Hierarchical Preferences

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3310.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`safe bandit`、`hierarchical preference`、`baseline constraint`

- 🎯 **研究动机**：医疗与安全控制等任务需按优先级优化多个目标并满足相对基线策略的安全约束，缺乏系统框架
- 🔬 **研究方法**：建立带层级偏好与安全约束的多目标随机线性 bandit 模型，区分累积与逐段两类约束，提出 LexUCB-C 与 LexTS-S 算法并给出 regret 界
- 📌 **结论**：两算法 regret 与单目标安全线性 bandit 相当，同时优化多个目标，在合成与真实数据上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-objective bandits with hierarchical preferences and safety constraints is central to many real-world decision-making tasks such as healthcare treatment planning and safe autonomous control, where multiple objectives must be optimized according to their priorities while ensuring safety requirements are satisfied. In this paper, we study a multi-objective stochastic linear bandit framework that incorporates hierarchical preferences together with safety constraints, requiring the learner to remain competitive with respect to a known baseline policy. We consider two practically motivated safety models: (i) cumulative constraints, which require the cumulative performance to exceed the baseline, and (ii) stage-wise constraints, which impose this requirement at each time step. We propose two algorithms, LexUCB-C and LexTS-S, designed for the cumulative and stage-wise settings, respective ly. We establish regret bounds showing that both algorithms achieve performance comparable to existing single-objective safe linear bandit methods, while simultaneously optimizing multiple objectives. In addition to theoretical guarantees, we develop an experimental framework that captures the interaction between hierarchical preferences and safety constraints. Experiments on synthetic and real-world datasets demonstrate the effectiveness of the proposed methods.

</details>

### 19. Safety-Aware Shared Autonomy via World-Model Constrained Planning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5019.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`shared autonomy`、`world model`、`constrained planning`

- 🎯 **研究动机**：共享自主方法依赖当前状态决定干预时机，在需预测未来不安全事件的长时程任务上表现不佳
- 🔬 **研究方法**：提出 WASP：安全感知世界模型在线前瞻推理联合评估未来安全违规与任务退化以决定干预时机，干预时用短时程残差校正过滤不安全候选并执行偏差最小的修正
- 📌 **结论**：在多样视觉安全关键域中大幅减少违规，同时保持任务表现并减少不必要的干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aware shared autonomy aims to enable an autonomous agent to collaborate with a human operator, completing tasks under safety constraints while maximally preserving human intent. However, existing methods often underperform in long-horizon tasks that require balancing task performance under safety constraints with the degree of intervention—particularly when accurately predicting future unsafe events is critical. This limitation largely stems from their reliance on the current state alone to decide when to intervene and how to modify actions. We propose World Model Assisted Safety Planning (WASP), a modelpredictive shared autonomy framework for explicit safety constraint satisfaction. We first formulate a safety-aware world model, and leverage its online predictive reasoning to decide when to intervene by jointly assessing prospective safety violations and degradation in task performance, thereby intervening only when necessary while enforcing safety constraints at decision time. Once intervention is triggered, WASP plans a short-horizon residual correction using world model rollouts, filters out unsafe candidates, and executes the least-deviating correction among the remaining high-return options in a receding-horizon loop. Experiments across diverse vision-based safety-critical domains show that WASP substantially reduces safety violations while preserving task performance and reducing unnecessary interventions over prior shared autonomy baselines.

</details>

### 20. SCOPE: Safety-Constrained Online Preview Enforcement for Efficient Encirclement in Multi-UAV Pursuit-Evasion

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5074.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`multi-UAV system`、`online safety preview`、`safe MARL`

- 🎯 **研究动机**：多无人机追逃需兼顾围捕效率与前向安全，现有 safe MARL 只能产出不安全或过度保守的策略，密集交互下的前向可行安全需要在线预览
- 🔬 **研究方法**：提出 SCOPE：学习在线安全预览动力学模型滚动未来轨迹，preview-fused actor-critic 结合分层安全执行做安全前瞻与在线动作修正
- 📌 **结论**：较 safe MARL 基线更好平衡效率与安全：保持平均围捕时间的同时平均 agent 代价降低 65.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unmanned aerial vehicle swarms in pursuit– evasion requires encirclement efficiency while maintaining safety constraints, facing a critical safety–efficiency trade-off. Existing safe multiagent reinforcement learning (MARL) methods often yield either unsafe task policies or conservative policies. This is challenging since forward feasible safety under dense interactions requires online safety preview. To address this issue, we propose Safety-Constrained Online Preview Enforcement (SCOPE), a MARL-based algorithm that balances encirclement efficiency and safety by short-horizon preview and safety enforcement. SCOPE learns an online safety-preview dynamics model that rolls out future trajectories to inform encirclement decisions checking. By proposing preview-fused actor– critic, SCOPE uses short-horizon previews for efficient encirclement and less unsafe behavior. Hierarchical safety enforcement performs safety lookahead and online action correction to maintain forward feasible safety. Experiments show that SCOPE better balances encirclement efficiency and safety than safe MARL baselines, maintaining average encirclement time while reducing the average agent cost by 65.6%. Code could be found at https://github.com/98177qdn/SCOPE.

</details>

### 21. Self-Improving Autonomous Vehicles via Real-World Reinforcement Learning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5068.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`autonomous driving`、`real-world RL`、`unsafe-action filtering`

- 🎯 **研究动机**：端到端自动驾驶在训练不足场景会采取不安全动作，真实世界 RL 采集数据成本高且需大量人工干预防止不安全状态与复位
- 🔬 **研究方法**：提出真实世界 RL 算法：按学习进度识别信息量大的场景，在进入不安全状态前中止 episode，并要求车辆自行复位到初始状态
- 📌 **结论**：在需自复位的城市驾驶任务上超越基线，人工干预显著减少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

End-to-end autonomous driving systems have demonstrated advantages over traditional modular systems. Despite this progress, these end-to-end systems still struggle to be deployed in real-world driving environments, as they inevitably encounter undertrained scenarios in which autonomous vehicles may take unsafe actions. Reinforcement Learning (RL) provides a theoretical framework for addressing this challenge by enabling autonomous vehicles to self-improve: continuously collecting additional scenarios and learning from them. However, training autonomous vehicles with RL is not straightforward in the real world. Collecting real-world driving data involves costly interactions with the environment, and significant human intervention is required both to prevent autonomous vehicles from entering unsafe states and to reset them for subsequent episodes. In this paper, we introduce a novel real-world RL algorithm that allows autonomous vehicles to collect informative scenarios and learn from them with minimal human intervention. Our algorithm considers the learning progress of autonomous vehicles to identify informative scenarios and abort episodes before they enter unsafe states. To evaluate our algorithm, we introduce challenging urban driving tasks that require autonomous vehicles to reset themselves to initial states. The experimental results show that our real-world RL algorithm outperforms baselines with much less human intervention.

</details>

### 22. Uncertainty-Guided Adaptive Conservative Offline Reinforcement Learning for Safer Mechanical Ventilation

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H132.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-health)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`offline RL`、`mechanical ventilation`、`uncertainty penalty`

- 🎯 **研究动机**：机械通气常规方案缺乏个性化，离线 RL 又对分布偏移与 OOD 动作高度敏感，复杂临床场景可靠性不足
- 🔬 **研究方法**：提出 UBER-CQL：异方差贝叶斯神经网络结合保守 Q-learning 建模后验 Q 不确定性，自适应惩罚不可靠高风险动作，并设计数值稳定的保守贝叶斯价值估计
- 📌 **结论**：MIMIC-IV 与 eICU 的分布内及 OOD 子集上超越 SOTA 离线 RL 与临床基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mechanical ventilation (MV) is essential in intensive care units (ICUs), yet conventional protocols lack personalization and risk harmful overor under-ventilation. Offline reinforcement learning (ORL) enables policy optimization from retrospective clinical data without unsafe online interaction, but existing methods are highly sensitive to distributional shift and out-of-distribution (OOD) actions, limiting their reliability in complex clinical settings. To address these challenges, we propose UBER-CQL (Uncertainty-Balanced Exploration and Robust Conservative Q-Learning), a robust ORL algorithm for safe decision-making under dataset shift. UBER-CQL integrates heteroscedastic Bayesian neural networks with conservative Q-learning to model posterior Q-value uncertainty, which is used to adaptively penalize unreliable high-risk actions while maintaining performance within the data support. We further design numerically stable objectives for conservative Bayesian value estimation. Experiments on indistribution and OOD subsets of MIMIC-IV and eICU demonstrate that UBER-CQL outperforms state-of-the-art ORL and clinician baselines, producing safer and more effective MV strategies.

</details>
### 后门与投毒攻击

### 23. BehaviorGuard: Online Backdoor Defense for Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2605.05977) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3528.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`deep RL`、`backdoor detection`、`action distribution`、`DRL backdoor`、`action-distribution drift`

👤 **作者**：Yinbo Yu、…、Daoqiang Zhang

- 🎯 **研究动机**：DRL 后门防御依赖奖励异常逆推触发器与模型微调，复杂触发下不鲁棒且成本高
- 🔬 **研究方法**：BehaviorGuard 转向触发无关的输出行为：后门策略为保证激活会诱导动作分布一致漂移（高分为位与尾部留痕），据此设计行为漂移度量在运行时识别并抑制后门动作
- 📌 **结论**：首个同时覆盖单智能体与多智能体 DRL 的在线后门防御，效果与效率均超先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to deep reinforcement learning (DRL). Current defenses typically rely on reward anomalies to reverse-engineer triggers and model finetuning to remove backdoors. However, complex trigger patterns undermine their robustness, and fine-tuning entails high costs, limiting practical utility. Therefore, we shift defense concerns to trigger-agnostic backdoor output behaviors and propose BehaviorGuard, an online behavior-based backdoor detection and mitigation framework for DRL. Specifically, we find that regardless of attacks, backdoored policies induce consistent shifts in action distributions to ensure reliable activation, leaving detectable traces in high-quantile regions and distribution tails, even in the absence of triggers. Based on this, we design a novel metric that captures behavioral drift in action distributions to identify and suppress backdoor actions at runtime. To our knowledge, this is the first online backdoor defense that counters attacks both in single- and multi-agent DRL. Evaluated across diverse benchmarks with different backdoor attacks, BehaviorGuard consistently surpasses prior methods in both efficacy and efficiency.

</details>

### 24. Mask-Guided Hybrid Triggers for Robust Clean-Label Backdoor Attacks

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4403.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`clean-label backdoor`、`hybrid trigger`、`adaptive mask`、`semantic mask`

- 🎯 **研究动机**：干净标签后门中样本无关触发器鲁棒但易检测，样本特定触发器隐蔽却受特征抑制限制
- 🔬 **研究方法**：MGHT 自适应掩码把触发器空间分配给样本无关锚点（可靠记忆）与样本特定伪装（感知语义一致），协同损失防止单一成分贪心依赖
- 📌 **结论**：CIFAR-10 与 CelebA 上 ASR 超 99%，高分辨率基准亦有效，PSNR>30dB 且抗主流后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clean-label backdoor attacks pose significant security threats to deep neural networks by injecting triggers without altering ground-truth labels. However, existing methods face a fundamental dilemma: sample-agnostic triggers are robust but easily detectable, while sample-specific triggers offer superior stealthiness but suffer from limited effectiveness due to feature suppression. To bridge this gap, we propose a new backdoor trigger framework called Mask-Guided Hybrid Trigger (MGHT). MGHT uses an adaptive mask to allocate spatial regions of the hybrid trigger between a sample-agnostic anchor for reliable memorization and a sample-specific camouflage for perceptual and semantic consistency. To prevent the optimization from greedily relying on a single trigger component, we further propose a Synergy-driven Co-optimization Strategy with a margin-based Synergy Loss. This ensures that the hybrid trigger is more effective and robust than either component alone. Extensive experiments on benchmark datasets demonstrate that MGHT achieves competitive performance, attaining over 99% ASR on CIFAR-10 and CelebA and showing strong effectiveness on higher-resolution benchmarks, while maintaining high visual quality (PSNR > 30 dB) and robustness to mainstream backdoor defenses.

</details>

### 25. Mitigating Backdoors via Decoy Shortcuts and Knowledge Decoupling

📄 [arXiv](https://arxiv.org/abs/2608.00732) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2444.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`backdoor removal`、`decoy shortcut`、`knowledge decoupling`

👤 **作者**：Zixuan Zhu、Rui Wang、Lihua Jing、Jinwen Zhong

- 🎯 **研究动机**：依赖第三方数据训练时后门攻击威胁严重，缺训练时防御
- 🔬 **研究方法**：发现后门行为倾向被并联简单分支吸收：TR 引入轻量 shortcut 分支作蜜罐，熵加权知识解耦引导毒样本流向蜜罐，训练后丢弃即移除后门且无需额外数据
- 📌 **结论**：四个基准数据集、五种架构上有效缓解多种后门并保留良性性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to deep neural networks, especially when training relies on third-party data, allowing adversaries to inject malicious behaviors through data poisoning. In this work, we reveal that backdoor behaviors tend to be absorbed by a simpler parallel branch when jointly trained with the main network. Motivated by this insight, we propose Trapping and Removing (TR), a simple yet effective training-time defense that introduces a lightweight shortcut branch as a “honeypot” to trap backdoor knowledge. After training, backdoors can be removed by discarding the shortcut, without requiring any additional data. To further enhance backdoor isolation while maintaining benign performance, we design a knowledge decoupling strategy with entropy-based weight assignment, encouraging poisoned samples to flow through the honeypot while guiding the main network to focus on benign learning. In addition, we introduce an automatic shortcut generation strategy to improve generalization across model architectures. Extensive experiments on four benchmark datasets and five model architectures demonstrate that our approach effectively mitigates a wide range of backdoor attacks while preserving performance on benign data. Code: github.com/Zixuan-Zhu/TR.

</details>

### 26. Understanding and Exploiting Phase Sensitivity for Attacking Large Vision–Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/52.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`LVLM`、`phase trigger`、`data poisoning`、`phase perturbation`、`LVLM backdoor`

- 🎯 **研究动机**：现有 LVLM 攻击多探索外部对抗引导，利用 LVLM 感知图像的内在模式（相位结构）诱发扰动尚未被研究
- 🔬 **研究方法**：发现 LVLM 对相位感知的图像结构敏感；提出 BadPhase，经数据投毒把对抗相位植入任意图像输入，配合文本触发器与后门扰动开关实现双触发激活，测试时优化降低资源依赖
- 📌 **结论**：在四个主流 LVLM 与三个基准上验证攻击有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Vision-Language Models (LVLMs) have demonstrated remarkable reasoning capabilities across various downstream multimodal tasks, they are proven to be vulnerable to carefully designed adversarial examples. Existing LVLM attackers show that exploring external components of adversarial guidance (e.g., forcing adversarial alignment, resembling harmful features) can help improve adversarial effects. However, leveraging the intrinsic patterns of LVLMs to induce adversarial perturbation generation by exploring how LVLMs perceive images has not been deeply studied. Inspired by the cognitive science, in this paper, we make the first attempt to investigate the interference of adversarial perturbation from the perspectives of image phase, and find that LVLMs are sensitive to the phase-aware image structure. Motivated by this, we propose a novel LVLM attack method called BadPhase with further backdoor designs, to implant adversarial phase as triggers into any image inputs via data poisoning so as to control the LVLMs’ predictions. A textual trigger and a backdoor perturbation switcher are also introduced to activate the malicious behavior only when both triggers are present. The whole backdoor optimization is implemented at the test-time to reduce the resource reliance. Experiments on four popular LVLMs and three benchmarks demonstrate the effectiveness of our proposed method.

</details>
### 隐私泄漏、机器遗忘与数据保护

### 27. A Durable Machine Unlearning Framework to Nullify Recall of Sensitive Data on Incremental Training

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T108.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`durable unlearning`、`sensitive data`、`incremental training`、`sensitive-data recall`、`incremental retraining`

- 🎯 **研究动机**：unlearning 后的模型仍需用新数据增量训练，新数据含相似甚至相同被遗忘样本时会重新唤回敏感信息，该漏洞未被研究
- 🔬 **研究方法**：提出 Durable Unlearning Enhancement 框架：三组件识别增量数据中的敏感样本并抑制其对 ULM 的梯度更新
- 📌 **结论**：在多个真实数据集与 SOTA unlearning 方法上有效消除 MU 后敏感信息回溯，甚至提升 ULM 性能，确立 post-MU 安全训练新方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancement of data privacy regulations has spurred the development of Machine Unlearning (MU), which is designed to remove the influence of sensitive data from a trained model and results in an unlearned model (ULM). Despite rapid progress in MU techniques, their vulnerabilities remain underexplored, which poses risks due to potential leakage of unlearned information. In realistic scenarios, ULMs always need to be incrementally trained with newly collected data samples, which can lead to the consequences of recalling sensitive information if the new dataset contains similar or even the same unlearned samples. To address this issue, we devise a Durable Unlearning Enhancement (DUE) framework to avoid restoring unwanted sensitive information from incremental training data samples. The DUE framework has three key components that identify sensitive samples and suppress their gradients to update ULMs. Extensive experiments on state-of-the-art MU methods across multiple real-world datasets show that the proposed DUE framework can effectively nullify the recall of sensitive information after MU, and even improve the performance of ULMs. Consequently, our work establishes a new fundamental research direction in safe training against post-MU vulnerabilities.

</details>

### 28. Adversarial Attack Framework Against Vision-Language Model Unlearning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7256.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`analysis`、`VLM unlearning`、`concept recovery`、`surrogate model`、`unlearning recovery`

- 🎯 **研究动机**：对抗输入可操纵已 unlearn 的 VLM 复现被遗忘内容，但多数攻击需要受害者架构、参数或输出 logits 访问
- 🔬 **研究方法**：提出 SISA：只需一个代理预训练 VLM；利用 unlearning 后 visual sink token 的持续性作为稳定结构锚，诱导 sink 建立结构锚再经 sink 条件化注意力做语义对齐，生成可迁移对抗输入
- 📌 **结论**：在多样 unlearned VLM 设定下有效，输出与遗忘目标的语义一致性相比干净输入最多提升 6.9 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision–Language Models (VLMs) unlearning tends to eliminate the influence of “to-beforgotten” content in the training corpora, algorithmically by suppressing the likelihood of faithfully generating responses on forget-target inputs. The injection of adversarial inputs can manipulate the unlearned VLM’s generation towards the attacker’s will, forcing the reproduction of the supposedly forgotten content and undermining the reliability of expected forgetting behavior. However, most attacks assume access to the unlearned VLM’s architecture or parameters, or to output logits via queries. In this paper, we propose SISA, a novel attack framework for crafting adversarial inputs to manipulate generation towards the forgotten target, which only requires access to a surrogate, pretrained VLM. SISA advances prior attacks by exploiting the persistence of visual sink tokens after unlearning as a stable structural anchor for semantic alignment. SISA induces a sink regime on a candidate visual token to build the structural anchor that influences generation, and then semantically aligns model output to the target while conditioning on attention through the induced sink token, reinforcing the anchor for desired elicitation. With sink persistence and sink-conditioned semantic anchoring, SISA crafts transferable adversarial inputs. Evaluation on diverse unlearned VLM settings confirms the effectiveness of SISA, increasing the outputs’ semantic agreement with forgotten targets by up to 6.9× relative to clean inputs.

</details>

### 29. IdentityMask: A Robust Face-Centric Privacy Protection Against Unauthorized Personalization of Diffusion Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3488.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`face privacy`、`unauthorized personalization`、`feature corruption`

- 🎯 **研究动机**：现有扰动防御忽略个性化过程的时空动态，扰动低效且未破坏核心身份编码机制
- 🔬 **研究方法**：IdentityMask 把扰动锚定在主体特定语义并优先关键扩散时间步，用流形投影把对抗信号嵌入图像内在结构以抗净化
- 📌 **结论**：多数据集、个性化技术与防御设定下保护效果与鲁棒性均超先前 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unauthorized personalization based on diffusion models pose a severe and growing threat to digital privacy by enabling the unauthorized replication and exploitation of individual identities. Existing disrupting-based defenses primarily add invisible perturbations arbitrarily across the entire image space to disrupt the generation process. However, we reveal that these methods fundamentally overlook the spatio-temporal dynamics of the personalization process, resulting in inefficient optimization that fails to sufficiently disrupt the core identity encoding mechanism. To mitigate these limitations, we propose IdentityMask, a robust protection framework that shifts the paradigm from arbitrary confusion to precise, targeted feature corruption. By anchoring the perturbation on subjectspecific semantics and prioritizing the most critical diffusion timesteps, our framework ensures the disruption is maximized precisely where the identity is encoded. Additionally, a novel manifold projection strategy is introduced to embed the adversarial signals into the intrinsic structure of the image, rendering the protection resilient against state-of-the-art purification. Extensive experiments across diverse datasets, personalization techniques, and defense settings demonstrate that IdentityMask consistently outperforms prior state-of-the-art approaches in both protection efficacy and robustness.

</details>

### 30. Incentivizing Truthful Machine Unlearning via Hierarchical Auditing

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7556.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`unlearning audit`、`incentive design`、`truthful compliance`

- 🎯 **研究动机**：验证营利性 AI 服务是否忠实执行 unlearning 的方法要么成本过高要么威慑不足
- 🔬 **研究方法**：UAG 博弈论审计框架：低成本筛查加触发式高精度验证的层级审计，把服务器-审计方交互建模为三阶段动态贝叶斯博弈并求均衡审计与惩罚策略
- 📌 **结论**：仅筛查约 50% unlearning 请求即达约 95% 服务器诚实率，兼顾成本与威慑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning has become a critical capability for AI services to comply with evolving privacy regulations. A key yet underexplored challenge is how to verify whether a profit-driven AI server has faithfully performed unlearning. Existing verification approaches either incur prohibitive costs or provide insufficient deterrence, failing to balance audit cost and enforcement effectiveness. To bridge this gap, we propose UAG, a game-theoretic unlearning auditing framework that incentivizes truthful unlearning via strategic deterrence rather than exhaustive verification. We design a hierarchical auditing mechanism that combines low-cost screening with selectively triggered high-precision verification, and models the server–auditor interaction as a three-stage dynamic Bayesian game. By characterizing the equilibrium strategy, we derive optimal audit and penalty policies that incentivize honest unlearning. Theoretical analysis and experiments show that UAG maintains reliable detection while achieving a favorable cost–deterrence tradeoff. Notably, UAG attains a server honesty rate of approximately 95% while screening only about 50% of unlearning requests, showing its practicality for trustworthy black-box unlearning services.

</details>

### 31. LLM-Based Agents on the Edge: A Survey of Privacy, Scalability, Heterogeneity, and Autonomy

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/SV272.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=survey-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`survey`、`edge agent`、`privacy`、`autonomy`

- 🎯 **研究动机**：LLM 智能体向网络边缘迁移带来与云端部署不同的挑战，缺系统综述
- 🔬 **研究方法**：沿部署、功能角色、交互拓扑、适应模式四轴分类法，综述隐私、可扩展性、异质性、自治四维挑战与设计对策
- 📌 **结论**：系统分析现有 LLM 边缘智能体框架对四维目标的达成程度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)–based agents are increasingly being deployed beyond centralized cloud environments and toward the edge of the network, where they operate closer to data sources. This transition facilitates lower latency and enhances contextual awareness, privacy, and responsiveness, but it also introduces challenges that differ from traditional cloud-based agent deployments. This survey provides a systematic overview of LLM-based edge agents with a particular focus on four critical dimensions: privacy, scalability, heterogeneity, and autonomy. To facilitate structured analysis, we introduce a novel taxonomy along four axes: deployment, functional role, interaction topology, and adaptation pattern. Based on our taxonomy, we analyze the challenges LLMbased agents face on the edge and discuss design solutions that can help mitigate possible issues. We further analyze the degree to which existing LLMbased edge agent frameworks achieve privacy, scalability, heterogeneity, and autonomy.

</details>

### 32. On the Privacy-Preserving Capabilities of PAVE Specifications in Learnware

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7083.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`learnware specification`、`privacy leakage`、`differential privacy`

- 🎯 **研究动机**：learnware 规范是数据依赖的公开工件，PAVE 规范的隐私性质未被分析
- 🔬 **研究方法**：形式化规范披露风险与放大风险；证明自然结构条件下紧凑 PAVE 经高斯素描视角内禀满足 (ε,δ)-DP，其余情形给出 DP-Stabilized-PAVE 认证变体
- 📌 **结论**：所得 DP 保证同时控制两类风险，并分析隐私-效用权衡以指导模型识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The learnware paradigm supports model reuse by pairing each submitted model with a specification, a lightweight representation used by the learnware dock system to identify, match, and reuse models without accessing raw data. While specifications are essential for learnware identification, they are also data-dependent public artifacts and it is not clear whether they reveal private information. Recently, the Parameter Vector (PAVE) specification has been proposed and shown to be effective for learnwares, yet its privacy properties remain largely unexplored. In this paper, we provide the first theoretical privacy analysis for PAVE. Specifically, we first formalize two specification-induced risks in the learnware paradigm: the disclosure risk of the released specification and the amplification risk that the specification may strengthen attacks against the released model. Second, we characterize when compact PAVE releases admit intrinsic differential privacy (DP): under natural structural conditions of learnware docks, the compact PAVE specification satisfies an (ε, δ)-DP guarantee without explicit additive noise through a Gaussiansketch view of stable parameter variations, and for regimes outside these conditions, we further provide DP-Stabilized-PAVE as a certified differentially private variant. Third, we show that the resulting DP guarantees control both disclosure risk and amplification risk, and we analyze the induced privacy–utility trade-off to guide effective learnware identification while preserving privacy.

</details>

### 33. One-Turn Knockout: Traceable and Editable Proxy Unlearning Under Asymmetric Access Constraints

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5637.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`proxy unlearning`、`asymmetric access`、`traceability`

- 🎯 **研究动机**：现有遗忘假设可访问目标模型参数与训练数据，而模型提供方与服务运营方访问权限不对称
- 🔬 **研究方法**：OTK 一次后训练把表示空间压缩为 codebook 离散代理，样本记录为 codebook token 分布、贡献经可加 token 统计累计估计；运营方可估分布、识别因果 token 并擦除贡献
- 📌 **结论**：多数据集与任务上持续优于 SOTA 遗忘方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MUL) aims to remove the influence of specific data from a trained model for data privacy and model adaptability. Existing MUL methods mostly assume the internal parameters and the training data of the target model are accessible. Nevertheless, in most practical scenarios, the model provider (MP) and the service operator (SO) are different entities with unequal model access privileges. The MP provides the model, while the SO can only access the model via APIs when handling unlearning requests. Under such an asymmetric access constraint, we propose One-Turn Knockout (OTK), a novel traceable and editable MUL framework based on a model-agnostic and editable proxy. Specifically, OTK first compresses the representation space of the target model into a discrete proxy based on codebook, with merely one pass post-training. Each data sample is recorded in the proxy space as a distribution over the codebook tokens, and its contribution to the model prediction can be cumulatively estimated via additive token statistics. Based on the traceable and editable proxy, the SO can instantly handle unlearning requests by (i) estimating the token distribution of the forgotten data, (ii) identifying the causal tokens, and (iii) erasing their contributions without the access to the model parameters and training data. Extensive experiments on multiple datasets and tasks show that OTK consistently outperforms state-ofthe-art unlearning methods.

</details>
### 对抗攻击、检测与鲁棒防御

### 34. Band Together: Untargeted Adversarial Training with Multimodal Coordination Against Evasion-Based Promotion Attacks

📄 [arXiv](https://arxiv.org/abs/2605.06238) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1759.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`multimodal recommender`、`promotion attack`、`adversarial training`

👤 **作者**：Guanmeng Xian、Ning Yang、Philip S. Yu

- 🎯 **研究动机**：多模态推荐系统的防御局限于单模态与投毒式威胁；多用户推广下视觉与文本扰动方向不一致的跨模态梯度失配会稀释攻击并使鲁棒训练低估风险
- 🔬 **研究方法**：UAT-MC 无目标对抗训练把所有条目视为潜在目标，并引入梯度对齐机制显式纠正失配，保证跨模态扰动同步以最大化对抗强度
- 📌 **结论**：显著提升对推广攻击的鲁棒性，同时在防御-精度权衡下保持可接受的推荐性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

multimodal recommender systems exploit visual and textual signals to alleviate data sparsity, but this also makes them more vulnerable to evasionbased promotion attacks. Existing defenses are largely limited to single-modal settings and mainly focus on poisoning-based threats, leaving evasionbased threats underexplored. In this work, we first identify a cross-modal gradient mismatch under the multi-user promotion setting, where visual and textual perturbations are optimized in inconsistent directions due to the dominance of distinct user groups. This phenomenon dilutes the attack effectiveness and leads robust training to underestimate worst-case risks. To address this issue, we propose Untargeted Adversarial Training with multimodal Coordination (UAT-MC). UATMC tackles the challenge of unknown targeted items in evasion-based attacks (as opposed to poisoning-based attacks) by treating all items as potential targets, and introduces a gradient alignment mechanism to explicitly correct this mismatch. This design ensures synchronized perturbations across modalities, thereby maximizing adversarial strength for robust training. Extensive experiments demonstrate that UAT-MC significantly improves robustness against promotion attacks while maintaining acceptable recommendation performance under the defense–accuracy trade-off. Code is available at https://github.com/ gmXian/UAT-MC.

</details>

### 35. Diverge to Converge: Mutual Heterogeneous Learning for Robust Pruning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6722.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`robust pruning`、`adversarial perturbation`、`heterogeneous learning`

- 🎯 **研究动机**：高稀疏剪枝显著降低对抗与腐蚀鲁棒性；单模型固定轨迹微调易陷局部最优、难恢复多重鲁棒性
- 🔬 **研究方法**：MHL：逐层 Lipschitz 正则做特征平滑加自适应边际目标做难度感知边界分离，熵互蒸馏经调度先探索多样特征子空间再收敛为统一鲁棒模型
- 📌 **结论**：对抗鲁棒性 +5%、腐蚀鲁棒性 +2.6%，干净精度保持竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural network pruning is crucial for efficient deployment on resource-constrained devices, yet achieving high sparsity often leads to significant robustness degradation against adversarial perturbations and corruptions. Recent works typically rely on single-model fine-tuning along a fixed optimization trajectory, which renders the network susceptible to local optima and noise while failing to restore the multiple robustness properties compromised during compression. In this paper, we propose Mutual Heterogeneous Learning (MHL), a framework enabling robust pruning via single-model inference. MHL instantiates heterogeneity through two complementary mechanisms: layer-wise Lipschitz regularization for intermediate feature smoothness, and adaptive margin objective for difficulty-aware boundary separation. To guide these diverse experts to converge, we employ entropy-based mutual distillation with a strategic schedule that shifts the optimization trajectory from exploring diverse feature subspaces to consolidating a unified robust model. Extensive experiments on four clean and corruption benchmarks and adversarial attacks demonstrate that MHL significantly outperforms single-model baselines in both adversarial robustness (+5%) and corruption robustness (+2.6%), while maintaining competitive clean accuracy.

</details>

### 36. From Standard to Robust: A Universal Framework for Continual Adversarial Defense

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2065.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`continual adversarial defense`、`few-shot adaptation`、`attack evolution`

- 🎯 **研究动机**：持续对抗防御方法依赖大量重放数据或多个专家模块，或鲁棒性与干净性能下降，难超独立鲁棒模型
- 🔬 **研究方法**：提出持续适应不遗忘、少样本、省内存、干净与对抗数据均高准确四原则，整合持续学习、少样本与集成学习构建 UCAD 框架
- 📌 **结论**：多阶段攻击下显著超各类基线；遇到的攻击越多越鲁棒，持续增强现有鲁棒模型直至饱和

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual adversarial defense (CAD) aims to defend target models against continuously emerging attacks. However, existing CAD methods typically rely on maintaining large amounts of replay data or multiple expert modules to mitigate catastrophic forgetting, or suffer from reduced robustness against adversarial examples or degraded performance on clean images. As a result, they often fail to provide clear advantages over standalone robust models. To address these limitations, we formulate four fundamental principles for CAD: (1) continual adaptation to new attacks without catastrophic forgetting, (2) few-shot adaptation, (3) memory-efficient adaptation, and (4) high classification accuracy on both clean and adversarial data. Guided by these principles, we explore and integrate cutting-edge techniques from continual learning, few-shot learning, and ensemble learning, and propose Universal Continual Adversarial Defense (UCAD), a universal framework that enables both standard and robust models to perform effective defense under the CAD setting. Extensive experiments validate the effectiveness of UCAD against multi-stage adversarial attacks and demonstrate significant improvements over a wide range of baseline methods. Moreover, we observe that as the number of encountered attacks increases, UCAD becomes increasingly robust, consistently enhancing the defense capability of existing robust models until saturation.

</details>

### 37. Generalization Analysis for Adversarial Vision Transformer

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2754.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`vision transformer`、`adversarial generalization`、`robustness bound`

- 🎯 **研究动机**：ViT 对对抗攻击高度敏感，但其对抗泛化行为缺乏严格理论基础
- 🔬 **研究方法**：用经验 Rademacher 复杂度分析扰动经深层 ViT 的累积机制，建立分类任务对抗设定下的高概率泛化界
- 📌 **结论**：界阐明 MLP 与 attention 权重范数正则、层间范数传播约束对缓解扰动的作用，实验验证理论

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Transformers (ViTs) exhibit notable susceptibility to adversarial attacks, presenting a significant challenge for their deployment in securitysensitive applications. Despite their considerable empirical successes, a rigorous theoretical foundation for ViT’s adversarial generalization behavior has not been adequately established. To address this limitation, we leverage empirical Rademacher complexity to analyze the mechanism of perturbation accumulation through deep ViTs layers. We establish a high-probability generalization bound for ViTs in classification tasks under adversarial settings. Our theoretical framework elucidates the roles of several factors in mitigating perturbation effects, norm regularization of weight matrices (in both MLP and attention modules) and depth-wise propagation constraints on layer-wise norms. Extensive experiments on benchmark datasets corroborate our theoretical insights, bridging the gap between ViTs architecture design and adversarial robustness.

</details>

### 38. GRASP: Hard-Label Black-Box Malware Evasion with Higher Success, Fewer Queries, and Smaller Perturbations

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6149.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`malware detector`、`hard-label evasion`、`query efficiency`

- 🎯 **研究动机**：硬标签黑盒下 PE 恶意软件对抗攻击查询效率低且文件膨胀大：组合空间大的原子扰动难探索，移植良性片段含大量无关字节
- 🔬 **研究方法**：GRASP 三阶段：Gumbel-Softmax 梯度种子预热、带紧凑高效用扰动库的 RL 精化、扰动最小化剪除冗余字节
- 📌 **结论**：以更少查询和更小文件膨胀取得更高攻击成功率，对商业杀毒引擎同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML)-based malware detectors are widely deployed but remain vulnerable to adversarial attacks. However, under hard-label black-box access, existing adversarial attacks on Windows Portable Executable (PE) malware are often query-inefficient and incur large file-size inflation. A common paradigm is to predefine a set of semantics-preserving atomic perturbations and search for evasive combinations under only binary feedback. Among these atomic perturbations, (i) those with highly combinatorial search spaces are difficult to explore effectively under hard-label feedback, leaving their potential untapped, and (ii) those relying on transplanting benign fragments are often laden with evasion-irrelevant bytes and exhibit highly variable adversarial utility. We propose Gradient-seeded Reinforcement Learning And Stealthy Pruning (GRASP), a three-stage framework that tackles these challenges. First, we decouple perturbations with highly combinatorial search spaces from the query-based search and instead apply a gradient-seeded warm-up that uses Gumbel-Softmax relaxation to enable gradientbased updates over the discrete space. This yields a strong warm start that improves evasion and reduces queries in later stages. Second, Reinforcement Learning (RL)-based refinement is accelerated by a perturbation library that filters, caches, and reuses compact high-utility patterns, reducing wasted queries on low-utility benign fragments. Third, a perturbation minimization stage removes redundant bytes while preserving evasion, reducing size inflation and feeding compact patterns back to the library. Experiments show that GRASP outperforms baselines, achieving higher attack success with fewer queries and smaller file-size inflation. We additionally demonstrate its practical effectiveness against commercial Antivirus engines. ∗ Corresponding author. J. Ning is also with the Zhejiang Key Laboratory of Digital Fashion and Data Governance, Zhejiang SciTech University and with the Faculty of Data Science, City University of Macau, Macau.

</details>

### 39. LBA: Textual Hard-Label Adversarial Attack Under Low Query Budgets

📄 [arXiv](https://arxiv.org/abs/2607.14101) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3591.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`text classifier`、`hard-label access`、`low-query search`

👤 **作者**：Shixin Guo、…、Hao Peng

- 🎯 **研究动机**：硬标签低预算下贪心逐位替换的局部搜索易漏高质量对抗样本且查询开销大
- 🔬 **研究方法**：LBA 采样式方法融合先验与后验知识构建高质量对抗样本近似分布，随采样推进迭代更新分布引导搜索
- 📌 **结论**：小到大规模六个语言模型、四个数据集上全面超 SOTA，生成文本语义保持与可读性更好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generating high-quality adversarial texts with low query budgets remains a challenging problem in the hard-label scenario. Most existing approaches rely on greedy algorithms, where one position in the text is selected for substitution, followed by the substitutions of other positions. This local search approach may fail to discover high-quality adversarial examples and often leads to excessive query costs. Ideally, an optimal adversarial sample would consider all possible position combinations in the text, but exhaustive search is computationally impractical. To address this challenge, we propose a sampling-based method called LBA, which constructs an approximate distribution of high-quality adversarial examples by integrating both prior and posterior knowledge, and utilizes this distribution for sampling. As sampling progresses, posterior knowledge updates the approximate distribution, which in turn guides more effective sampling. Extensive experiments on six language models, ranging from small-scale to large-scale architectures across four datasets, demonstrate that LBA significantly outperforms state-of-the-art baselines on all evaluation metrics. Additionally, LLM-based assessment indicates that LBA generates more semantically preserved and comprehensible adversarial texts.

</details>

### 40. Manifold-Constrained Adversarial Training for Long-Tailed Robustness via Geometric Alignment

📄 [arXiv](https://arxiv.org/abs/2605.02183) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1379.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`adversarial training`、`long-tailed data`、`manifold constraint`

👤 **作者**：Guanmeng Xian、Ning Yang、Philip S. Yu

- 🎯 **研究动机**：对抗训练在长尾分布下鲁棒性退化，尾部类鲁棒误差高且决策边界不稳
- 🔬 **研究方法**：MCAT 惩罚偏离类条件流形保证对抗样本语义有效，并用 ETF 启发正则促进类间平衡几何分离；理论联系几何分离与鲁棒间隔下界
- 📌 **结论**：长尾基准上整体、平衡与尾类对抗鲁棒性一致提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial training is effective on balanced datasets, but its robustness degrades under longtailed class distributions, where tail classes suffer high robust error and unstable decision boundaries. We propose Manifold-Constrained Adversarial Training (MCAT), a unified framework that enforces the semantic validity of adversarial examples by penalizing deviations from class-conditional manifolds in feature space, while promoting balanced geometric separation across classes via an ETF-inspired regularization. We provide theoretical results that link geometric separation to lower bounds on adversarially robust margins, and show that manifold-constrained adversarial risk upperbounds robust risk on high-density semantic regions. Extensive experiments on standard longtailed benchmarks demonstrate consistent improvements in overall, balanced, and tail-class adversarial robustness. The codes and appendix are available on https://github.com/yneversky/MCAT.

</details>

### 41. MonoPure: Multi-Component Purification via Disentangled, Projective Representations for Monocular 3D Object Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/987.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`monocular 3D detection`、`multi-component attack`、`calibration purification`

- 🎯 **研究动机**：单目 3D 检测脆弱于同时扰动图像与相机标定的多组件攻击，复合失真破坏 3D-2D 对应
- 🔬 **研究方法**：MonoPure 用目标区域概率图引导扩散净化聚焦任务区域，2D 骨架关键点做遮挡鲁棒检测，投影标定净化模块迭代最小化重投影误差恢复内参
- 📌 **结论**：多组件攻击与遮挡下优于先前检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monocular 3D object detection is a cost-efficient alternative to multisensor systems, yet it remains fragile to multi-component adversarial attacks that perturb the image and tamper with camera calibration. Compounded distortions degrade 3D reasoning by disrupting the correspondence between the 3D geometry and 2D image plane. To address this problem, this work proposes MonoPure, a monocular 3D object detection framework that performs multi-component purification via disentangled and projective representations. MonoPure incorporates a disentangled purification and segmentation module that purifies the image data, with a target-region probability map steering diffusion-based purification to focus on task-relevant regions. In addition, MonoPure presents a 3D detection decoder that integrates 2D skeleton keypoints as object-level spatial cues, enabling occlusion-robust 3D detection. Finally, a projective calib-purification module restores compromised intrinsics by iteratively minimizing the reprojection error between projected 3D boxes and calibration-invariant 2D detection boxes. The experiments confirm that MonoPure outperforms prior detectors under multi-component attacks and occlusion.

</details>

### 42. Parameter-Efficient Dual-Loss Adaptation with Logit Divergence: A Unified Approach for Adversarial Example Detection and Robust Inference

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6748.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`adversarial detection`、`robust inference`、`adapter divergence`

- 🎯 **研究动机**：对抗样本检测与鲁棒推理通常割裂，且需外部检测器
- 🔬 **研究方法**：D3Adapter 在冻结骨干上挂轻量适配器库，双损失与互补目标训练出有意不同的 logit 行为；推理时以适配器间 logit 分歧作威胁评分并选适配器输出
- 📌 **结论**：迁移与自适应白盒攻击下单次前向统一检测与鲁棒推理，开销随适配器数量可预测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present D3Adapter, a threat-aware framework that unifies adversarial example detection (AED) and robust inference. D3Adapter attaches a small library of lightweight adapters to a frozen ResNet backbone; the adapters are trained under two loss functions (cross-entropy and optimized reverse cross-entropy) and complementary objectives (clean training and adversarial training), yielding intentionally distinct logit behaviors. During inference, D3Adapter quantifies inter-adapter logit divergence to produce an agreement-based threat score without any external detector for AED. The same pass also performs robust inference by outputting prediction from the selected adapter when an adversarial example is detected, therefore unifying detection and defense into single-pass forward computation. We evaluate D3Adapter under transfer-based and adaptive white-box attacks, and we study scalability across datasets with varying numbers of classes, showing that unified detection and robust inference can be achieved with predictable overhead proportional to the number of adapters.

</details>

### 43. Transferable Attacks on Open-Vocabulary Video Instance Segmentation via Dual-Objective Triggers

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/837.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`open-vocabulary VIS`、`dual trigger`、`cross-model transfer`

- 🎯 **研究动机**：开放词汇视频实例分割（OV-VIS）耦合时空推理与语言对齐，其对抗鲁棒性基本未被探索
- 🔬 **研究方法**：提出 DOT 可迁移攻击：语义抑制触发器破坏真实对象与查询的对齐，合理替换触发器诱导视觉合理且文本一致的幻影轨迹；相位引导对抗训练增强跨模型迁移
- 📌 **结论**：四个 SOTA 实现上 mAP 降幅至多 69.3%、攻击成功率至多 98%，平均超最强基线 1.6 倍且 PSNR 保持 52.4 dB

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-vocabulary video instance segmentation (OV-VIS) couples spatial-temporal reasoning with language grounding, yet its adversarial robustness has remained largely unexplored. We present the Dual-Objective Triggers (DOT), the first transferable attack on OV-VIS that simultaneously exploits the vision–language coupling and temporal coherence. DOT deploys a Dual Semantic Perturbation Module that combines two complementary triggers: a Semantic Suppression Trigger disrupts the alignment between the true object and the query, while a Plausible Replacement Trigger steers the tracker toward a phantom trajectory that is visually plausible and text-consistent. To amplify cross-model transferability without sacrificing perceptual fidelity, we introduce Phase-Guided Adversarial Training, which injects perturbations primarily in the phase spectrum while blending amplitudes with clean references. Extensive experiments on four state-of-the-art OV-VIS implementations demonstrate that DOT reduces mAP by up to 69.3% and achieves attack success rate of up to 98%, outperforming the strongest baseline by a factor of 1.6× on average, while maintaining a PSNR of 52.4 dB, thus exposing critical security vulnerabilities and laying a foundation for future research on robust and trustworthy vision–language systems.

</details>

### 44. Unrestricted Targeted Deep Hashing Attack via Contrastive Latent Diffusion

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4746.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`attack`、`deep hashing`、`latent diffusion`、`targeted retrieval`

- 🎯 **研究动机**：深度哈希定向攻击依赖 Lp 范数约束扰动，难兼顾攻击有效性与不可感知性，常需可感知噪声
- 🔬 **研究方法**：提出 UTDHA：以对比引导的 latent diffusion 在潜空间而非像素空间生成对抗样本，拉近目标标签、推离非目标标签，并约束结构与感知一致性
- 📌 **结论**：三个基准上攻击有效性与不可感知性均优于现有定向攻击基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep hashing is widely used for large-scale image retrieval but remains vulnerable to adversarial examples, raising practical security concerns. Existing targeted adversarial attacks on deep hashing typically rely on ℓp-norm constrained perturbations, which struggle to balance attack effectiveness and imperceptibility, often requiring perceptible noise and limiting their practicality in real-world retrieval scenarios. We propose UTDHA, the first unrestricted targeted attack for deep hashing models using contrastive-guided latent diffusion. UTDHA generates adversarial examples with a latent diffusion model and performs optimization in the latent space rather than the pixel space, enabling semantic manipulation while preserving image naturalness. Through contrastive guidance, the attack pulls adversarial examples toward the target label while pushing them away from non-target labels. Meanwhile, UTDHA enforces structural and perceptual consistency, producing adversarial examples that are both imperceptible and visually natural. Extensive experiments on three benchmarks demonstrate that UTDHA outperforms existing targeted adversarial attack baselines for deep hashing models in both attack effectiveness and imperceptibility.

</details>
### 生成内容真实性与多媒体取证

### 45. An Information-theoretic Propagation Denoising and Fusion Framework for Fake News Detection

📄 [arXiv](https://arxiv.org/abs/2605.02259) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2441.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`fake news`、`synthetic propagation`、`information bottleneck`

👤 **作者**：Mengyang Chen、Lingwei Wei、Wei Zhou、Songlin Hu

- 🎯 **研究动机**：LLM 合成的传播数据天然不可靠，直接与真实传播融合会产生有偏表征
- 🔬 **研究方法**：InfoPDF 把每个合成传播图建模为概率潜分布指导可靠性感知自适应融合，用互信息目标学习压缩且任务充分的表征，抑制噪声并保持真实与合成表征一致
- 📌 **结论**：三个真实数据集上各类假新闻检测任务一致领先，并能估计属性级可靠性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Incomplete propagation data significantly hinders robust fake news detection. Recent approaches leverage large language models to simulate missing user interactions via role-playing, thereby enriching propagation with synthetic signals. However, such propagation data is intrinsically unreliable, and directly fusing it can lead to biased representations and limited detection performance. In this paper, we alleviate the unreliability of synthetic propagation from the mutual information perspective and propose a novel information-theoretic propagation denoising and fusion (InfoPDF) framework to learn effective representations from both real and synthetic propagation. Specifically, we first generate attribute-specific synthetic propagation using large language models. Then we model each synthetic propagation graph as a probabilistic latent distribution to guide reliability-aware adaptive fusion with real propagation. During training, we design a mutual information-based objective to learn compressed and task-sufficient propagation representations. It jointly suppresses noisy signals across attribute-specific synthetic propagation, maintains consistency between real and synthetic propagation representations, and ensures task sufficiency for fake news detection and attribute prediction. Experiments on three real-world datasets show that InfoPDF consistently achieves superior performance across various fake news detection tasks. Further analysis demonstrates that InfoPDF can estimate attribute-level reliabilities and learn more discriminative propagation representations.

</details>

### 46. BEAT2AASIST: BEATs Feature Splitting with Dual-Branch AASIST for Environmental Sound Deepfake Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3453.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`audio deepfake`、`environmental sound`、`unknown generator`

- 🎯 **研究动机**：TTA 与 ATA 生成逼真环境声音带来恶意音频操纵风险，token 级音频表征会削弱结构化声学线索的显式保持
- 🔬 **研究方法**：BEAT2AASIST 双分支 AASIST 沿频率或通道维度拆分 BEATs 表征，多层融合（拼接、CNN-gated、SE-gated）聚合多层 transformer 信息，并用多神经 vocoder 数据增强
- 📌 **结论**：EnvSDD 数据集上两个赛道分获 ESDD 2026 Challenge 第 3 与第 4 名，集成组件比顶级系统更少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in text-to-audio (TTA) and audioto-audio (ATA) generation models have enabled the creation of highly realistic environmental sounds, raising growing concerns about malicious audio manipulation in real-world scenarios. To address this emerging threat, the ESDD 2026 Challenge was introduced as the first large-scale benchmark for Environmental Sound Deepfake Detection (ESDD), featuring two tracks that evaluate generalization to unseen generators and robustness under black-box, low-resource conditions. In this paper, we present BEAT2AASIST, an enhanced deepfake detection framework built upon the BEATsAASIST baseline. Motivated by the observation that token-based audio representations may weaken explicit preservation of structured acoustic cues, the proposed method introduces a dualbranch AASIST architecture that explicitly splits BEATs-derived representations along frequency or channel dimensions. This design enables specialized modeling of complementary spoofing artifacts that may be attenuated in unified representations. To further enrich acoustic features, we incorporate multi-layer fusion strategies that aggregate information from multiple transformer layers using concatenation, CNN-gated, and SE-gated mechanisms. In addition, vocoder-based data augmentation with multiple high-fidelity neural vocoders is employed to enhance robustness against unseen and black-box spoofing attacks. Experimental results on the EnvSDD dataset demonstrate that BEAT2AASIST achieves strong and consistent performance across both challenge tracks. In particular, the proposed approach attains 3rd place in Track 2 and 4th place in Track 1 in the ESDD 2026 Challenge, despite using fewer ensemble components than top-ranked systems. These results suggest that explicit model- ∗ Corresponding authors. ing of heterogeneous acoustic subspaces, combined with targeted representation fusion and data augmentation, provides an effective and efficient design strategy for real-world environmental sound deepfake detection. The code is available at https: //github.com/ikwak2/BEAT2AASIST.

</details>

### 47. Beyond “Made with AI”: Visualizing Provenance Density to Mitigate the Transparency Penalty

📄 [arXiv](https://arxiv.org/abs/2609.03460) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/HC13.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-human-centred-ai)　📅 2026　🏷 IJCAI 2026

**关键词**：`analysis`、`AI provenance`、`evidence visualization`、`hallucination trust`

👤 **作者**：Qing Zhang、Yifei Huang、Juyoung Lee、Thad Starner、Jun Rekimoto

- 🎯 **研究动机**：Fluency Trap：用户既信任流畅幻觉，又在披露 AI 生成后低估准确内容；二元 Made with AI 标签不显示主张的证据支撑
- 🔬 **研究方法**：提出证据可视化界面 Provenance Density，展示文本中已验证主张的密度；81 人用户研究与 200 样本技术审计
- 📌 **结论**：理想化界面产生 +4.15 点（d=1.82）的真伪辨别差距，无信号组无可测辨别力；Consistency Veto 承载大部分判别信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative AI makes polished prose cheap to produce, users can no longer rely on fluency as a proxy for truth. We call this failure mode the Fluency Trap: users trust fluent hallucinations while also discounting accurate content once it is disclosed as AI-generated. Binary “Made with AI” labels respond with authorship disclosure, but they do not show what supports a claim. We propose Provenance Density, an evidence-visualization interface that shows the density of verified claims in a text. In a user study with 81 participants, an idealized Provenance Density interface produced a large discernment gap between truth and fabrication (+4.15 points, d = 1.82), whereas participants given no signal showed no detectable discrimination. A technical audit with 200 samples shows that retrieval density alone is insufficient; unexpectedly, the Consistency Veto carries most of the discriminative signal on dynamic queries. As AI-generated content becomes indistinguishable from human writing, effective transparency must move from authorship disclosure toward evidence visualization.

</details>

### 48. Breaking the Trade-off: Orthogonal Semantic Decoupling for Generalizable and Fair Deepfake Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1712.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`deepfake`、`cross-domain generalization`、`demographic shortcut`

- 🎯 **研究动机**：深伪检测的跨域泛化与人口公平性存在权衡：泛化导向检测器过度依赖人口捷径，公平约束又使优化偏离最具判别力的边界
- 🔬 **研究方法**：OSD 对视觉语言模型预训练权重做 SVD，冻结主语义子空间并在残差子空间学习参数高效低秩专家——按组采样并路由的人口语义专家加跨域可迁移的通用伪造专家
- 📌 **结论**：多个基准上泛化与公平双双超越 SOTA，打破两者的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection faces dual challenges in real-world deployment: cross-domain generalization and demographic fairness. Existing approaches often struggle with a trade-off between these goals. Generalization-oriented detectors can over-rely on demographic shortcuts, while fairness constraints tend to steer optimization away from the most discriminative decision boundary. To address this, we propose Orthogonal Semantic Decoupling (OSD), a framework that decouples demographic semantics from forgery cues. Specifically, we perform Singular Value Decomposition on the pretrained weights of a vision-language model, freezing the principal semantic subspace while learning parameter-efficient low-rank experts in the residual subspace. The experts comprise Demographic Semantic Experts, a set of experts specialized via group sampling and routed based on the similarities between image embeddings and text embeddings of predefined descriptions; and a Universal Forgery Expert, which captures forgery features transferable across domains and demographics. Extensive experiments across multiple benchmarks demonstrate that our approach outperforms state-of-the-art methods in both generalization and fairness, breaking the trade-off. The code is available at https://github.com/sonder-lin/ osd-deepfake-detection.

</details>

### 49. Bridging the SEA Gap: An Initial Benchmark for Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages

📄 [arXiv](https://arxiv.org/abs/2606.15968) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4G93.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-social-good)　📅 2026　🏷 IJCAI 2026

**关键词**：`benchmark`、`speech deepfake`、`neural audio codec`、`language generalization`

👤 **作者**：Orchid Chetia Phukan、Girish、Mohd Mujtaba Akhtar、Arun Balaji Buduru

- 🎯 **研究动机**：codecfake 检测基准基本限于英语（少量中文），东南亚语言未探索，且 vocoder 数据训练的检测器泛化差
- 🔬 **研究方法**：SEA-CF 首个多 SEA 语言大规模 CF 检测基准，覆盖多样说话人与多种 NAC 架构；并提出轻量小模型 GARUDA
- 📌 **结论**：英文中心数据训练的 SOTA 检测器因 SEA 语音结构差异无法泛化；微调 ALM 有效但规模过大，GARUDA 轻量且超越强基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Codecfakes (CFs) are a type of speech deepfakes generated through Audio Language Models (ALMs), with Neural Audio Codecs (NACs) forming the core mechanism for speech encoding and generation. CFs exhibit distributional characteristics that differ from vocoder-based deepfakes, causing detectors trained on vocoder data to generalize poorly to CFs detection. Although this has led to the development of CF detection benchmarks, existing resources are largely confined to English—and to a limited extent Chinese—leaving South-East Asian (SEA) languages unexplored. To bridge this gap, we introduce SEA-CF, the first large-scale benchmark for CF detection spanning multiple SEA languages, diverse speaker profiles, and a wide range of NAC architectures. SEA-CF is constructed by synthesizing publicly available real speech corpora. Our experiments show that state-of-the-art (SOTA) CF detectors trained on English-centric datasets fail to generalize to SEA speech due to language-specific phonetic structures, tonal variations, and rich prosodic diversity. We further conduct a comprehensive zero-shot and fine-tuned evaluation of recent SOTA ALMs on SEA-CF. Fine-tuning the ALMs improves performance, however, these are very large being impractical for real-world application due to their scale, particularly in low-resource and latency-constrained settings. To address this limitation, we propose a novel small-ALM, GARUDA tailored for CF detection, which delivers strong performance while remaining lightweight. Extensive evaluations demonstrate that the proposed Small-ALM outperforms strong end-to-end and ALM-based baselines, establishing a new, practical direction for robust CF detection in SEA languages and beyond.

</details>

### 50. Falsdo: Benchmarking Artifact-Controlled Multimodal Fake News Verification via Failure-Aligned Auditing

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/686.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`benchmark`、`multimodal misinformation`、`artifact control`、`evidence audit`

- 🎯 **研究动机**：现有基准无法把真语义核查与表面捷径利用（依赖生成伪影）区分开
- 🔬 **研究方法**：FALSDO 经异构网络挖掘构建：指令条件化落地加反事实伪影控制协议（拉平低级生成痕迹做压力测试）；并提出显式噪声控制证据获取与可靠性感知晚融合的 DREA 基线
- 📌 **结论**：伪影拉平后检测器性能退化，证明其依赖伪影而非稳健验证；DREA 提升 Joint-F1 并在伪影控制下最小化退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent generative AI renders multimodal misinformation structurally harder to detect, making reliable detection dependent on semantic verification grounded in verifiable evidence. However, current benchmarks often fail to isolate true semantic checking from superficial shortcut exploitation. We introduce FALSDO, a diagnostic benchmark designed to make robustness and auditability identifiable. Constructed via a heterogeneous web-mining pipeline, FALSDO provides instruction-conditioned grounding and formalizes a counterfactual artifact-control protocol. This stress test reveals a critical failure: when low-level generation traces are equalized, detector performance degrades, indicating reliance on artifacts rather than robust verification. To enable reproducible diagnosis, we propose DREA, a failure-aligned evidence-auditing baseline. DREA specifies evidence acquisition with explicit noise control and implements constrained channel-wise auditing with reliability-aware late fusion. Experiments demonstrate that FALSDO reliably exposes shortcut dependence, while DREA improves instruction-level grounding (Joint-F1) and minimizes degradation under artifact-controlled settings.

</details>

### 51. Profiling the Voice: Speaker-Specific Phoneme Fingerprinting for Speech Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2605.17737) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4461.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`speech deepfake`、`speaker fingerprint`、`phoneme profile`

👤 **作者**：Jun Xue、…、Yanzhen Ren

- 🎯 **研究动机**：通用黑盒语音深伪检测器不捕说话人特有习惯特质且缺可解释性
- 🔬 **研究方法**：PVP 从宏语句转向微语音建模：仅用真实参考语音估计轻量 GMM 建模说话人特有音素实现，并发布首个大规模中文 POI 深伪数据集
- 📌 **结论**：POI 欺骗场景显著超 SOTA 通用检测器（EER 大幅降低）并提供音素级可解释性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative AI has made audio deepfakes increasingly indistinguishable from authentic human vocals, posing significant threats to persons-of-interest (POI) such as public figures. Current detection systems primarily rely on generic, black-box models that fail to capture speaker-specific idiosyncratic traits and lack interpretability. In this paper, we propose Phoneme-based Voice Profiling (PVP), a novel personalized defense framework. By shifting the detection paradigm from macro-utterance analysis to micro-phonetic modeling, PVP captures the unique acoustic distributions underlying a POI’s habitual articulatory patterns. Specifically, our framework models speaker-specific phonetic realizations using lightweight Gaussian Mixture Models (GMMs) estimated solely from bona fide reference speech. This design enables data-efficient profiling and robust generalization to previously unseen spoofing attacks without requiring heavy spoof-specific training. Furthermore, we introduce the first largescale Chinese POI deepfake dataset to benchmark speaker-specific detection. Experimental results demonstrate that PVP significantly outperforms state-of-the-art generic detectors in POI spoofing scenarios, achieving substantial EER reductions while providing fine-grained, phoneme-level interpretability for forensic analysis. Code and data are available at: https://github.com/JunXue-tech/PVP

</details>

### 52. PURE: Purging Unrelated Representations for Content-Agnostic Forgery Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2613.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`AI-generated image`、`content shortcut`、`cross-domain forensics`

- 🎯 **研究动机**：AIGI 检测器把伪造伪影与语义内容虚假耦合（内容捷径），分布偏移下严重退化
- 🔬 **研究方法**：PURE 用 Causal Semantic Generative 机制把语义表示与伪造无关干扰解耦，GMM 原型对齐抑制类别特定内容偏差
- 📌 **结论**：CIFAKE、GenImage 与 AlFace 上伪相关反转设定下泛化优越

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing AI-generated image (AIGI) detectors perform well in-domain but degrade severely under distribution shift. We observe that this failure is mainly caused by content shortcuts, where detectors spuriously couple forgery artifacts with semantic content, such as object categories or demographic attributes, learning content–label correlations instead of generalizable forgery patterns. To address this issue, we propose PURE (Purging Unrelated Representations for ContentAgnostic Forgery Detection), which achieves content-agnostic detection through two complementary components: a Causal Semantic Generative (CSG) mechanism that disentangles semantic representations from forgery-irrelevant nuisance factors, and a Gaussian Mixture Model (GMM)- based prototype alignment module that suppresses category-specific content bias. Extensive experiments on CIFAKE, GenImage, and AlFace show that PURE achieves superior generalization under spurious correlation reversal. The code is available at https://github.com/wuxinyu519/PURE.

</details>

### 53. Robust, Generalizable Proactive Face-swapping Defense via Semantic Gradient Divergence

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/988.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`face swapping`、`proactive protection`、`semantic perturbation`

- 🎯 **研究动机**：主动式换脸防御存在可见伪影、跨 deepfake 模型泛化差、易被扩散净化与压缩等后处理破坏的问题
- 🔬 **研究方法**：提出 SGD-Guard：用 CLIP 特征与迭代提炼的广义身份特征构建特征库，在 CLIP-身份联合嵌入空间以共识加权扰动特定面部属性，并按方向差异优先应对关键变换
- 📌 **结论**：有效防御多样换脸模型且跨模型迁移性强，兼顾视觉保真与对净化后处理的鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of identity-feature-based faceswapping technology has raised concerns about impersonation and privacy violations. Although proactive defenses aim to block identity extraction at the source, existing methods suffer from perceptible visual artifacts, poor generalization across diverse deepfake models, and vulnerability to postprocessing techniques (e.g., diffusion purification, image compression, and transformations). This work proposes a robust, generalizable proactive face-swapping defense via semantic gradient divergence (SGD-Guard) to address these challenges. It introduces an integrated feature gallery that uses CLIP features and a generalized identity feature, obtained by iteratively refining heterogeneous identity features into a homogeneous representation. This framework facilitates our semantic distortion attack by leveraging consensus weighting to target specific facial attributes within a CLIP-identity joint embedding space, disrupting deepfake generation while preserving visual fidelity. Furthermore, to ensure robustness against purification and post-processing, this method incorporates a module that prioritizes critical transformations by exploiting directional discrepancies. Comprehensive experiments demonstrate that the method effectively defends against diverse face-swapping models with high cross-model transferability.

</details>

### 54. When Evidence Falls Short: Router-Guided Fake News Detection with Pattern Augmentation

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4589.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`detection`、`fake news`、`evidence routing`、`deception pattern`

- 🎯 **研究动机**：LLM 事实核查高度依赖证据，面对不可靠、噪声或稀缺证据时脆弱；而 LLM 又缺乏欺骗模式的专业知识
- 🔬 **研究方法**：提出 RGPA：层级路由（案例路由器与外部证据路由器）按多维质量评估引导推理路径，专家模型捕获欺骗特征并融入 LLM 推理
- 📌 **结论**：两个真实数据集上显著超越现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing complexity of online information, trustworthy fake news detection has become increasingly critical. Although Large Language Models (LLMs) exhibit a strong ability to leverage factual evidence for verification, they remain highly vulnerable to unreliable, noisy, or scarce evidence, undermining robustness in real-world scenarios. Given the generalizability of deceptive patterns in fake news, we consider pattern as a complementary signal under insufficient evidence during factual verification. However, due to LLMs’ lack of expertise in deception-specific patterns, realizing such effective collaboration remains challenging. To address these issues, we propose a RouterGuided Fake News Detection Framework with Pattern Augmentation (RGPA). Specifically, we introduce a hierarchical routing mechanism including a case router and an external evidence router. It guides news to appropriate reasoning paths adaptively based on a multi-dimensional quality assessment, prioritizing high-quality evidence while mitigating noise. Furthermore, we design an expert model to capture deceptive features and integrate them into LLMs’ reasoning, enabling a synergy of factual verification and pattern awareness under evidence-scarce scenarios. Extensive experiments on two real-world datasets demonstrate that RGPA significantly outperforms existing approaches.

</details>
### 水印、模型身份与版权保护

### 55. Guard4D: Robust Watermarking for 4D Gaussian Splatting via Decoupled Decoding

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/197.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`4DGS watermark`、`decoupled decoder`、`asset copyright`

- 🎯 **研究动机**：4DGS 资产共享需要可从渲染视频验证的水印，但解码易被场景内容主导、跨帧不稳定
- 🔬 **研究方法**：Guard4D 文本监督预训练通用消息解码器，固定几何与不透明度仅优化球谐偏移嵌入消息；TMSD 模块时序聚合并用噪声对照剪辑抑制语义干扰
- 📌 **结论**：动态 4DGS 场景上验证了水印嵌入与提取的有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

4D Gaussian Splatting (4DGS) enables highquality, real-time rendering of dynamic scenes and is becoming a popular format for sharing 4D assets. This trend calls for robust copyright watermarking that can be verified from rendered videos without access to the original scene or model parameters. However, watermarking 4DGS is challenging: verification relies on short multi-view clips whose frames vary with motion, viewpoint changes, and post-processing. More importantly, decoding from rendered frames is easily dominated by scene content (objects, textures, illumination) rather than subtle watermark traces, leading to unstable evidence across frames and poor generalization across scenes. We propose Guard4D, a decoupled watermarking framework for 4DGS. Guard4D pre-trains a general-purpose message decoder under text supervision and embeds a binary message by optimizing compact spherical-harmonic offsets while keeping geometry and opacity fixed. To improve extraction from short clips and suppress semantic interference, we introduce a temporal modeling and semantic decoupling (TMSD) module that temporally aggregates watermark information and uses clean and noise-perturbed control clips generated from the non-watermarked model to reduce the influence of semantics on watermark decoding. Extensive experiments on dynamic 4DGS scenes demonstrate the effectiveness of Guard4D. Code is available at https://github.com/shisyy/Guard4D.

</details>

### 56. Implicit Identity Technologies for LLMs: Fingerprinting and Watermarking Across Datasets, Models, and Generated Content

📄 [arXiv](https://arxiv.org/abs/2605.29245) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/SV270.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=survey-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`survey`、`LLM identity`、`fingerprinting`、`watermarking`

👤 **作者**：Bing Liu、…、Wei Luo

- 🎯 **研究动机**：LLM 指纹与水印研究术语混乱、方向孤立，缺乏系统组织
- 🔬 **研究方法**：综述提出 implicit identity 统一抽象区分指纹与水印，建立覆盖数据集、模型、生成内容的生命周期分类法与可识别性/鲁棒性/可部署性评测框架
- 📌 **结论**：结构化该领域图景、澄清术语并指出安全部署方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) require substantial investments and are increasingly deployed in highstakes domains, making it critical to protect LLMrelated assets and to trace their provenance. Identity technologies such as fingerprinting and watermarking address these needs by enabling ownership verification and attribution, and have rapidly emerged as an active research focus. However, existing techniques lack a systematic organisation, leading to two key issues, terminological confusion and isolated research lines, that have hindered the development of this research field. To this end, we present a comprehensive review of LLM identity techniques, focusing on fingerprinting and watermarking across the LLM lifecycle, including datasets, models, and generated content. We make three primary contributions. First, we introduce implicit identity (Implicit-ID for short) as a unifying abstraction and distinguish fingerprinting from watermarking. Second, we propose a lifecyclebased taxonomy that organises techniques by asset type and verification role, aligning each with asset protection or provenance. Third, we establish an evaluation framework around three objectives— identifiability, robustness, and deployability. Together, these contributions structure the landscape of LLM identity techniques, clarify terminology, and highlight directions toward secure deployment.

</details>

### 57. Latents-Inv:Robust Semantic Watermark via Dual-Path Mutual Information Redundancy for Diffusion Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7552.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`diffusion watermark`、`dual-path redundancy`、`adversarial robustness`

- 🎯 **研究动机**：嵌入初始潜噪声的语义水印对几何变换与代理模型潜空间操纵高度脆弱
- 🔬 **研究方法**：Latents-Inv 双路径网络把水印同时编入生成图像与所有者密钥，用互信息冗余在单路被攻击时恢复信息；对比学习抑制负样本误报，backward Euler 迭代实现精确逆映射
- 📌 **结论**：各类对抗攻击下鲁棒性优于现有方法且保持高视觉质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Semantic watermarking methods, embedding identity into the initial latent noise, provide an imperceptible identity traceability for diffusion models in copyright protection and source verification. However, existing methods are highly vulnerable to adversarial attacks, especially geometric transformations (e.g., rotation, cropping) and latent-space manipulations via proxy models, limiting the reliability of watermark verification in practical deployment. To address this issue, we propose a robust and fully reversible, flow-based watermarking framework with dual encoding paths, which preserves high visual fidelity of watermarked image while ensuring resilient identity recovery under adversarial attacks. Specifically, a dual-path network is proposed to encode watermark information into both the generated image and the owner’s secret key. This network leverages Mutual Information Redundancy to recover compromised information under single-path attack, ensuring robust verification. To enhance verification credibility without degrading generation quality, we introduce a joint training strategy that suppresses false positives on negative samples through contrastive learning under fidelity constraints. Furthermore, we employ a backward Euler iteration scheduler for rectified flow models, which facilitate accurate inversion mapping, to enable effective watermark verification, which accurate inversion. Extensive experiments show that our method achieves superior robustness against various adversarial attacks while maintaining high visual quality across diverse generative models.

</details>

### 58. Toward LoRA Copyright Protection with an Authorized Dual-Watermarking Framework

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7650.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026　🏷 IJCAI 2026

**关键词**：`defense`、`LoRA copyright`、`authorization control`、`dual watermark`

- 🎯 **研究动机**：LoRA 定制 T2I 扩散模型的服务与商业分发平台兴起，LoRA 模块的版权保护缺乏专门手段
- 🔬 **研究方法**：提出 LoRA2D 授权双水印框架：基于许可的授权控制加可按有效授权移除的显式水印震慑未授权使用，并持续嵌入隐式水印支持鲁棒黑盒所有权验证
- 📌 **结论**：在多个图像生成数据集上验证了 LoRA 版权保护的有效性与实用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) diffusion models have been widely adopted due to their strong generative capabilities, while Low-Rank Adaptation (LoRA) has emerged as an efficient mechanism for customizing these models for diverse creative and commercial applications. This trend has fostered LoRAcentric service platforms that that enable the customization and commercial distribution of LoRA modules according to user requirements. However, the growing prevalence of LoRA and its critical role in customized AI services have raised urgent concerns about LoRA copyright protection. To address this gap, we propose LoRA2 D, an authorized dual-watermarking framework specifically designed to protect LoRA modules in T2I diffusion models. LoRA2 D integrates licensebased authorization control with explicit watermarks as visible deterrents for unauthorized or trial usage, which can be removed upon valid authorization, while persistently embedding an implicit watermark for robust black-box ownership verification. Extensive experiments on multiple imagegeneration datasets demonstrate the effectiveness and practicality of LoRA2 D for securing copyrights in LoRA-adapted T2I diffusion models.

</details>