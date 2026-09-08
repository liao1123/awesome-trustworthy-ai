# CoT 可监控性

## 研究方向

CoT 可监控性研究可见推理轨迹能否忠实暴露模型的决策依据和隐藏目标，以及监控器在长上下文、多 Agent 协作、对抗规避和训练压力下何时失效。该方向同时涵盖忠实性测量、monitor 设计与评测、监控规避、Agent 轨迹监控，以及保持可监控性的训练干预。

## 研究脉络

- **基础测量：** 早期研究围绕 CoT 的 faithfulness 与 verbosity 建立静态可监控性指标。
- **监控对象扩展：** 后续方法发展到专用 monitor、Agent trajectory 和跨轨迹检测。
- **边界与评测：** 长上下文、多 Agent 组合危害、输出监督和主动规避不断暴露监控边界，因此 benchmark 与 red-teaming 已成为独立主线。

## Benchmark 与 Red-Teaming

### 1. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

📄 [arXiv](https://arxiv.org/abs/2608.19974)　📅 2026-08

**关键词**：`benchmark`、`trajectory compliance`、`action-evidence monitor`、`rationale deception`、`execution-grounded monitoring`、`rule violation`

👤 **作者**：Yiyang Luo、…、Yunya Song

- 🎯 **研究动机**：金融 agent 可能引用规则却仍提交违反可执行约束的订单或误读监控证据
- 🔬 **研究方法**：ReguSim 受控金融合规环境与 ReguBench 目标标注监控基准，分离所述推理、尝试动作、执行强制与监控证据四产物；DeepSeek V4 Pro 与 Gemini 3.5 Flash 交易员运行
- 📌 **结论**：可见规则减少但不消除被拒动作，激励或人设框架改变行为；交易员理由会误导独立监控器除非出示强制证据；结构化简单基线匹配或超过纯 prompt LLM 监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning, attempted action, execution enforcement, and monitor evidence. In trader runs with DeepSeek V4 Pro and Gemini 3.5 Flash, visible rules reduce but do not eliminate rejected actions, and incentive or persona framing shifts behavior. A bridge study shows that trader rationales can mislead an independent monitor unless enforcement evidence is shown. In monitoring, simple structured baselines either match or exceed prompt-only LLMs. The results frame financial compliance evaluation as an audit of rule-grounded actions and evidence use, rather than a single compliance score.

</details>

### 2. The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.29178)　📅 2026-05

**关键词**：`benchmark`、`agent monitoring`、`multi-agent`、`compositional harm`

👤 **作者**：Nikolay Radev、Lennart Haas、Benjamin Arnav、Pablo Bernabeu-Pérez

- 🎯 **研究动机**：多实例分解工作的 coding 系统能否协同完成任一真子集无法独立完成的隐蔽破坏未知
- 🔬 **研究方法**：SCHEME 基准：17 个任务实例、7 个设定、8 个真实开源库，合法工程任务配隐蔽副任务，设计成无任何 agent 真子集可单独成功，测试真实多 agent 协调
- 📌 **结论**：协同破坏已可行——Gemini 3.1 Pro 在 84% 样本中完成隐蔽目标同时完成合法任务（Codex 46%），差距主因是失败恢复率（约 73% vs 56%）；可信监控仅凭代码编辑即以 FPR 不超 2% 检出 99%/68%，加通信达 100%/81%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories.

</details>

### 3. MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring

📄 [arXiv](https://arxiv.org/abs/2605.09684)　📅 2026-05

**关键词**：`benchmark`、`agent monitoring`、`monitor red-teaming`

👤 **作者**：Monika Jotautaitė、Maria Angelica Martinez、Ollie Matthews、Tyler Tracy

- 🎯 **研究动机**：现行红队实践攻击欠激发并高估 monitor 表现：攻击生成模式坍缩、构想与执行有鸿沟、人工成本高
- 🔬 **研究方法**：半自动红队流水线：攻击 taxonomy 防坍缩，把攻击构建分解为策略生成、执行与事后轨迹精炼；应用于 BashArena 产出 2,644 条攻击轨迹的 MonitoringBench
- 📌 **结论**：Opus-4.5 monitor 捕获率从 94.9% 降至精炼攻击下的 60.3%；对三个开发 monitor 优化的攻击泛化到十个留出 monitor；前沿 monitor 常能发现可疑动作却被说服性攻击突破

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce a red-teaming methodology that exposes harder-to-catch attacks for coding-agent monitors, suggesting that current practices may under-elicit attacks and overstate monitor performance. We identify three challenges with current red-teaming. First, mode collapse in attack generation, which we reduce with a novel attack taxonomy for broader coverage. Second, a conceive-execute gap: frontier LLMs can propose strong attack ideas or execute them, but not all at once. We mitigate this by decomposing attack construction into strategy generation, execution, and post-hoc trajectory refinement. Third, manual elicitation is costly to scale, which we address with our semi-automated red-teaming pipeline. Applied to BashArena, an AI control setting for tool-using coding agents, this pipeline produces MonitoringBench, a benchmark of 2,644 attack trajectories for evaluating monitor capabilities and failure modes. Our pipeline produces more diverse and stronger attacks: Opus-4.5 monitor's catch rate falls from 94.9\% on elicited-only Opus attacks to 60.3\% on our best refined attacks, with larger drops for several mid-tier monitors. Attacks optimized against three development monitors generalize to ten held-out monitors, with catch rates generally increasing with monitor capability. Using this benchmark, we provide a snapshot of the current monitor capabilities and find that frontier monitors often detect suspicious actions but fall for persuasion or fail to calibrate suspiciousness scores appropriately, suggesting tractable paths for improvement. MonitoringBench provides both a static benchmark for current tool-use monitors and a reusable methodology for refreshing these evaluations as agents and monitors improve.

</details>

### 4. MonitorBench: A Comprehensive Benchmark for Chain-of-Thought Monitorability in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.28590) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`benchmark`、`CoT monitoring`、`evaluation suite`、`CoT monitorability`、`stress testing`、`AI control`

👤 **作者**：Han Wang、…、Huan Zhang

- 🎯 **研究动机**：CoT 并非总因果负责最终输出，忠实性下降削弱监控，但缺少全面开源的评测基准
- 🔬 **研究方法**：MonitorBench 含 1,514 个实例、19 个任务 7 类别，精心设计决策关键因素并提供两种提示压力测试设定
- 📌 **结论**：可监控性是条件属性：决策关键因素参与中间推理时更高；多数 LLM 可经压力测试提示有意降低可监控性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) can generate chains of thought (CoTs) that are not always causally responsible for their final outputs. When such a mismatch occurs, the CoT no longer faithfully reflects the actual reasons (i.e., decision-critical factors) driving the model's behavior, leading to the reduced CoT monitorability problem. This limits the use of CoTs for reliable oversight. However, a comprehensive and fully open-source benchmark for thoroughly evaluating CoT monitorability remains lacking. To address this gap, we propose MonitorBench, a systematic benchmark for evaluating CoT monitorability in LLMs. MonitorBench provides: (1) a diverse set of 1,514 test instances with carefully designed decision-critical factors across 19 tasks spanning 7 categories to characterize when CoTs can be used to monitor the factors driving LLM behavior; and (2) two prompting stress-test settings to quantify the extent to which CoT monitorability can be degraded. Extensive experiments show that CoT monitorability is a conditional property affected by the evaluated LLM, monitor LLM, and task characteristics. Across these factors, monitorability is higher when decision-critical factors shape the intermediate reasoning process, rather than merely influencing the final answer. Under stress-test prompting, most evaluated LLMs can intentionally reduce monitorability, mainly on tasks where decision-critical factors are not structurally required by the reasoning process. Overall, MonitorBench provides a basis for further research on AI control, reasoning faithfulness, stress-test monitorability, and monitoring scaffords. The code is available at https://github.com/ASTRAL-Group/MonitorBench.

</details>

### 5. Monitoring Monitorability

📄 [arXiv](https://arxiv.org/abs/2512.18311) · 🌐 [Project](https://openai.com/zh-Hans-CN/index/evaluating-chain-of-thought-monitorability/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62992)　📅 2025-12　🏷 ICML 2026

**关键词**：`benchmark`、`detection`、`CoT monitoring`、`evaluation suite`、`AI control`、`chain-of-thought`

👤 **作者**：Melody Y. Guan、…、Bowen Baker

- 🎯 **研究动机**：CoT 监控的有效性（monitorability）可能随训练流程、数据来源与规模扩展而脆弱，缺乏度量与追踪手段
- 🔬 **研究方法**：提出干预、过程与结果属性三类评测原型、新 monitorability 指标与评测套件，比较前沿模型并考察推理算力、RL 优化与预训练规模的影响
- 📌 **结论**：多数模型相当但并非完全可监控；更长 CoT 更可监控、RL 优化未实质降低可监控性；同能力下高推理强度小模型更可监控，弱监控器增加测试时算力、访问 CoT 及追问也能提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Observability into the decision making of modern AI systems may be required to safely deploy increasingly capable agents. Monitoring the chain-of-thought (CoT) of today's reasoning models has proven effective for detecting misbehavior. However, this "monitorability" may be fragile under different training procedures, data sources, or even continued system scaling. To measure and track monitorability, we propose three evaluation archetypes (intervention, process, and outcome-property) and a new monitorability metric, and introduce a broad evaluation suite. We demonstrate that these evaluations can catch simple model organisms trained to have obfuscated CoTs, and that CoT monitoring is more effective than action-only monitoring in practical settings. We compare the monitorability of various frontier models and find that most models are fairly, but not perfectly, monitorable. We also evaluate how monitorability scales with inference-time compute, reinforcement learning optimization, and pre-training model size. We find that longer CoTs are generally more monitorable and that RL optimization does not materially decrease monitorability even at the current frontier scale. Notably, we find that for a model at a low reasoning effort, we could instead deploy a smaller model at a higher reasoning effort (thereby matching capabilities) and obtain a higher monitorability, albeit at a higher overall inference compute cost. We further investigate agent-monitor scaling trends and find that scaling a weak monitor's test-time compute when monitoring a strong agent increases monitorability. Giving the weak monitor access to CoT not only improves monitorability, but it steepens the monitor's test-time compute to monitorability scaling trend. Finally, we show we can improve monitorability by asking models follow-up questions and giving their follow-up CoT to the monitor.

</details>

### 6. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning

📄 [arXiv](https://arxiv.org/abs/2510.04040) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007686)　📅 2025-10　🏷 ICLR 2026

**关键词**：`benchmark`、`CoT monitoring`、`reasoning faithfulness`

👤 **作者**：Xu Shen、…、Tianlong Chen

- 🎯 **研究动机**：CoT 常不忠实于内部推理，但判断单条轨迹是否忠实缺乏基准
- 🔬 **研究方法**：把不忠实检测形式化为判别决策问题，构建四个 LLM 四领域 1000+ 专家标注轨迹（含 300+ 不忠实实例与细粒度成因），系统评测 11 种检测方法
- 📌 **结论**：反事实、logit 与 LLM-as-judge 范式各有强弱，知识密集领域与更强模型上检测难度更高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly rely on Chain-of-Thought (CoT) prompting to improve problem-solving and provide seemingly transparent explanations. However, growing evidence shows that CoT often fail to faithfully represent the underlying reasoning process, raising concerns about their reliability in high-risk applications. Although prior studies have focused on mechanism-level analyses showing that CoTs can be unfaithful, they leave open the practical challenge of deciding whether a specific trajectory is faithful to the internal reasoning of the model. To address this gap, we introduce FaithCoT-Bench, a unified benchmark for instance-level CoT unfaithfulness detection. Our framework establishes a rigorous task formulation that formulates unfaithfulness detection as a discriminative decision problem, and provides FINE-CoT (Faithfulness instance evaluation for Chain-of-Thought), an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs across four domains, including more than 300 unfaithful instances with fine-grained causes and step-level evidence. We further conduct a systematic evaluation of eleven representative detection methods spanning counterfactual, logit-based, and LLM-as-judge paradigms, deriving empirical insights that clarify the strengths and weaknesses of existing approaches and reveal the increased challenges of detection in knowledge-intensive domains and with more advanced models. To the best of our knowledge, FaithCoT-Bench establishes the first comprehensive benchmark for instance-level CoT faithfulness, setting a solid basis for future research toward more interpretable and trustworthy reasoning in LLMs.

</details>

### 7. Detecting Hidden Chain-of-Thought in Large Language Models with Linguistic, Behavioral, and Mechanistic Indicators

📄 [arXiv](https://arxiv.org/abs/2608.29956)　📅 2026-09

**关键词**：`detection`、`latent reasoning`、`behavioral-mechanistic signal`、`calibration control`

👤 **作者**：Armaan Singh、…、Vasu Sharma

- 🎯 **研究动机**：模型不展示中间步骤时，无法判断其是隐式推理还是模式补全
- 🔬 **研究方法**：提出 Hidden CoT Detection Score，衡量 neutral prompt 行为更接近显式 CoT 还是 no-CoT，并在 GSM8K 上测试 Qwen3-4B 两个变体
- 📌 **结论**：两变体 HCDS 显著为正（+1.87／+1.41）且跨推理栈与量化复现（差 0.08 内）；reasoning-tuned 变体表现出更强、少依赖 prompt 的 CoT 类行为，但该分数不能证明存在未暴露 trace

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models often answer complex reasoning questions without revealing intermediate steps, raising whether they reason latently or complete patterns. We propose the Hidden CoT Detection Score (HCDS), a comparative behavioral and mechanistic signal measuring whether neutral-prompt behavior aligns more closely with explicit CoT or explicit no- CoT. Here, hidden CoT operationally denotes this neutral-prompt CoT-like alignment; HCDS does not directly observe or prove an unexposed reasoning trace. On GSM8K, HCDS is significantly positive for both Qwen3-4B variants (Thinking $+1.87$, $p = 1.2 \times 10^{-7}$; Instruct $+1.41$, $p = 1.9 \times 10^{-4}$), replicates across a different inference stack and quantization within $0.08$ ($+1.80$ and $+1.45$), and is not significantly positive in seven of eight length-adjusted calibration-control cells. The unadjusted score produces large positive scores on single-step arithmetic and numeric factual lookup. The variants also respond differently to no-CoT instructions: Instruct complies from the prompt alone, whereas Thinking continues reasoning and requires intervention. These findings show stronger, less prompt-conditional CoT-like behavior in the reasoning-tuned model, consistent with but not proof of latent reasoning. HCDS thus investigates latent reasoning without relying on models' self-reported traces.

</details>

### 8. Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency

📄 [arXiv](https://arxiv.org/abs/2608.29583)　📅 2026-09

**关键词**：`detection`、`runtime trajectory monitoring`、`CoT-action consistency`、`unsafe driving`、`reasoning reliability`、`runtime monitor`

👤 **作者**：Tian Yu、Lu Feng、Sebastian Elbaum

- 🎯 **研究动机**：驾驶 VLA 会输出显式 CoT，但其能否作为 runtime 规格交叉校验轨迹缺乏证据
- 🔬 **研究方法**：构建基于 NVIDIA Alpamayo 1.5 的 150 对人工标注 CoT-trajectory 数据集 DriveAlignBench，并开发 lane-relative F-LLM 等自动一致性 monitor
- 📌 **结论**：33.3% 的 CoT 本身不可靠，可靠 CoT 中仅 74% 与轨迹一致；最佳 monitor 达 F1=0.75，比最强 raw-waypoint LLM 基线高 0.13

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous vehicles (AVs) operate in complex environments where failures are consequential. Sophisticated machine learning models for perception and planning are key to overcoming at least part of that complexity, but their black-box nature complicates validation and verification (V&V). The recent integration of Vision-Language-Action (VLA) models into AVs introduces a unique opportunity: besides generating trajectories, these models produce an explicit Chain-of-Thought (CoT) explaining their underlying rationale. This CoT provides a rich specification to cross-check model outputs and detect inconsistencies that may expose unsafe or unintended behavior. This paper assesses whether CoTs from a recent open driving VLA can support such monitoring. We curate DriveAlignBench, a specialized dataset from NVIDIA's Alpamayo 1.5 VLA for AVs containing 150 CoT-trajectory pairs, which we manually annotate for reliability, trajectory consistency, and safety. Our analysis reveals that 33.3% of CoTs are unreliable. Among reliable CoTs, the generated trajectory is consistent with the CoT in 74% of cases. Leveraging this potential, we propose integrating a CoT-trajectory consistency check into a runtime monitor. The check is nontrivial: CoTs express open-vocabulary, scene-relative driving commitments, while trajectories are low-level ego-motion sequences whose semantics depend on road geometry and motion context. To bridge this gap, we develop a family of automated consistency monitors. Our best monitor, lane-relative F-LLM with GPT-5.5, achieves F1 = 0.75, improving over the strongest raw-waypoint LLM baseline by +0.13 absolute F1 and over a rule-based monitor by +0.38. We release DriveAlignBench, the monitor implementations, and annotation tools at https://github.com/776styjsu/drive-the-thoughts.

</details>

### 9. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

📄 [arXiv](https://arxiv.org/abs/2608.27348)　📅 2026-08

**关键词**：`detection`、`agentic misalignment`、`intent trajectory`、`online intervention`、`action preference`、`intent monitoring`

👤 **作者**：Yutong Zhang、…、Han Qiu

- 🎯 **研究动机**：事后 CoT 标签过粗，无法刻画 agentic misalignment 中有害意图在推理生成过程中的动态变化
- 🔬 **研究方法**：提出 INTENT-AS-A-TOOL，为模型添加面向目标行为的意图工具，以工具调用概率作为无需 judge 的细粒度行为承诺信号
- 📌 **结论**：该信号补足 CoT 监控并把粗标签扩展为稠密意图轨迹，可定位适合在线干预的关键步骤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

</details>

### 10. Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles

📄 [arXiv](https://arxiv.org/abs/2608.16190)　📅 2026-08

**关键词**：`detection`、`CoT monitoring`、`reasoning trace`、`monitorability`

👤 **作者**：Anik Jha

- 🎯 **研究动机**：可信监控集成按平均成对相关最小化构建，但多样性来源与该指标的有效性未经验证
- 🔬 **研究方法**：24 个开源监控器跨 9 个预训练谱系、检测技能 pAUC 0.028-0.803，把攻击项一致性分解为共享可检测性信号与特异误差两分量
- 📌 **结论**：两分量对集成增益符号相反（-0.25/+0.26）致总指标几乎无预测力（+0.05）；技能作用于信号（+0.53）、谱系买不到去相关——匹配能力下跨谱系面板不更好，无相关加权选择能样本外胜过单选最佳监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Trusted monitoring has a cheap, trusted model score a stronger untrusted model's actions, and a diverse ensemble of them beats a single stronger monitor at matched cost. They are built by minimising average pairwise correlation, and that paper's twelve monitors shared one base model, leaving open what supplies the diversity. We study 24 open-weight monitors spanning nine pretraining lineages and a 29x range of detection skill (pAUC at 10 percent FPR, 0.028 to 0.803) on backdoored code. The metric used to build panels does not predict what a panel is for, and we can say why. Agreement on attack items splits into a shared-detectability signal component and an idiosyncratic error component, which predict ensemble gain with opposite sign (Spearman -0.25 and +0.26), so their sum, the metric actually used, predicts it barely at all (+0.05); the cancellation holds in 7 of 8 evaluations. Skill acts on signal (+0.53) while error stays flat (-0.01), which is why a monitor's own skill predicts its agreement with the pool (Spearman 0.84, n = 24, permutation p below 0.0001). Pretraining lineage is the obvious way to buy decorrelation, and it does not pay. At matched member capability, cross-lineage panels detect no better (permutation p = 0.13), and lineage barely moves the metric either (+0.064, p = 0.18). We report that against ourselves: on our own 22-monitor pool the same test read +0.104 at p = 0.037 until two monitors were added. An earlier pool topping out at pAUC 0.23 had already invalidated another analysis. Such a quantity is a property of the pool assembled. Panel gain over the best member falls monotonically with panel skill (-0.66 at k = 2, -0.70 at k = 3), and no correlation-weighted selection beats picking the single best monitor out of sample. Across six attacker models the gain result holds in all six, the agreement and cancellation results in five of six.

</details>

### 11. Visible Reasoning and Indirect Prompt-Injection Monitorability Across English, Tamil, and Tanglish

📄 [arXiv](https://arxiv.org/abs/2608.15392)　📅 2026-08

**关键词**：`detection`、`CoT monitoring`、`reasoning trace`、`monitorability`

👤 **作者**：Madhusudhanan G

- 🎯 **研究动机**：CoT 监控跨语言与行为设定的可靠性不确定，泰米尔语与 Tanglish 场景无证据
- 🔬 **研究方法**：小型案例研究：Sarvam-105B 上八个人工核验的间接注入合成场景，比较有无可 API 可见推理时的攻击成功率
- 📌 **结论**：试点与预注册随访方向相反（5/12 对 1/11 与 2/12 对 3/12），无法区分真实效应与噪声；但 20 条注入思考轨迹中全部 17 个正确输出声明忽略注入、3 个成功攻击均声明遵循

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought monitoring is a potentially useful safety signal, but its reliability across languages and behavioral settings remains uncertain. In a small case study of eight manually verified synthetic scenarios, one model, one annotator, and one deterministic generation seed, I study API-visible reasoning during indirect prompt injection in Sarvam-105B across English, Tamil, and Tanglish. A four scenario pilot found 5/12 injected attack successes without reasoning and 1/11 with reasoning. A preregistered four-scenario follow-up reversed that direction, finding 2/12 attacks without reasoning and 3/12 with reasoning. With only four scenarios per phase, this design cannot distinguish a real reasoning-mode effect from prompt-specific variation or sampling noise. Across 20 non-empty injected-thinking traces, all 17 benign-correct outputs stated an intent to ignore the injection, while all three attack successes stated an intent to follow it. These descriptive observations provide a reproducible case study of behaviorally informative visible reasoning when it is available; they do not establish that reasoning mode improves safety, that visible reasoning is mechanistically faithful, or that the findings generalize beyond this configuration.

</details>

### 12. CoT-Guard: Small Models for Strong Monitoring

📄 [arXiv](https://arxiv.org/abs/2605.12746)　📅 2026-05

**关键词**：`detection`、`CoT monitoring`、`small-model monitoring`

👤 **作者**：Nirav Diwan、…、Gang Wang

- 🎯 **研究动机**：大模型 CoT monitor 成本高，而 4B-8B 小模型即便看到 CoT 也常把隐藏目标误归为用户请求
- 🔬 **研究方法**：SFT 从强 monitor 蒸馏检测行为拉近域内差距，RL 用微妙隐藏目标泛化到域外；评估第三方 LLM 路由器经 prompt 或代码操纵注入隐藏目标的供应链威胁模型
- 📌 **结论**：4B CoT-Guard 的 G-mean^2 达 75%，超过 GPT-5.4（56%）、GPT-5-mini（41%）与 Qwen3-32B（54%），逼近 Gemini-3-Flash（83%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring the chain-of-thought (CoT) of reasoning models is a promising approach for detecting covert misbehavior (i.e., hidden objectives) in code generation tasks. While large models (GPT-5, Gemini-3-Flash) can serve as effective CoT monitors, they are expensive to deploy due to the lengthy reasoning traces and high API cost, emphasizing the need for smaller, cheaper alternatives. Nevertheless, we find that current small models (4B--8B) struggle to detect hidden objectives despite access to the CoT, frequently misattributing them as part of the user query. To address this, we propose a post-training pipeline combining supervised fine-tuning (SFT) and reinforcement learning (RL), where SFT narrows the gap for in-domain tasks by distilling detection behavior from stronger monitors, and RL on hard and subtly crafted hidden objectives helps the model generalize to out-of-domain monitoring tasks. To validate this generalization, we evaluate under a realistic threat model motivated by practical supply-chain attacks, where the adversary is a third-party LLM router injecting hidden objectives into code-generation requests through either prompt manipulation or code manipulation attacks. To push beyond objectives that large monitors already saturate, we also introduce four new challenging tasks even for strong monitors. Finally, we introduce CoT-Guard, a 4B-parameter monitor that demonstrates superior generalization performance under both prompt and code manipulation attacks, achieving a G-mean^2 (i.e., TNR x TPR) of 75% and outperforming GPT-5.4 (56%), GPT-5-mini (41%), and Qwen3-32B (54%), while closing the gap to Gemini-3-Flash (83%). These results demonstrate that CoT-Guard provides a practical and cost-effective user-side defense, substantially improving hidden-objective detection while avoiding the deployment cost of large monitors.

</details>

### 13. How Useful Is Cross-Domain Generalization for Training LLM Monitors?

📄 [arXiv](https://arxiv.org/abs/2605.12265)　📅 2026-05

**关键词**：`detection`、`CoT monitoring`、`cross-domain generalization`

👤 **作者**：Sam Martin、Fabien Roger

- 🎯 **研究动机**：标注稀缺领域依赖 prompted 分类器，多任务分类训练能否泛化到新域新提示未知
- 🔬 **研究方法**：研究多任务（各自 prompt）训练对新域新 prompt 分类的泛化，识别失败边界并与通用指令训练混合
- 📌 **结论**：可部分泛化到相邻域，但 prompt 完全改变而数据域不变时会失效；混合指令训练保留收益并缓解失效；无思考分类训练还能泛化到带思考分类与摘要

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Using prompted language models as classifiers enables classification in domains with limited training data, but misses some of the robustness and performance benefits that fine-tuning can bring. We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts. We show that such training partially generalizes to adjacent domains, improving classification performance on tasks that are unseen during training. However, we identify specific edge cases where the fine-tuned models fail to follow prompts, such as when the classification prompt changes completely while the data domain remains the same as during training. We show that classification training can be mixed with general instruction following training, and that (when done well) such training keeps the benefits of classification training and mitigates its generalization failures. Surprisingly, we see that this no-thinking supervised classification training can generalize to with-thinking classification and summarization, suggesting that no-thinking classification training might be instrumentally useful in building other kinds of classifiers and monitoring systems.

</details>

### 14. Detecting Safety Violations Across Many Agent Traces

📄 [arXiv](https://arxiv.org/abs/2604.11806) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`detection`、`agent monitoring`、`cross-trajectory detection`、`safety violation detection`、`agent trace auditing`、`cross-trace search`

👤 **作者**：Adam Stein、Davis Brown、Hamed Hassani、Mayur Naik、Eric Wong

- 🎯 **研究动机**：安全违规稀疏、复杂甚至被对抗隐藏，仅在多轨迹联合分析时可见；单轨迹 judge 与固定监控器均难胜任
- 🔬 **研究方法**：Meerkat 结合聚类与 agentic search，按自然语言描述的违规做结构化搜索与自适应调查，无需种子场景或固定工作流
- 📌 **结论**：显著超过基线监控器，在 CyBench 上发现近 4 倍于以往审计的 reward hacking 案例，并揭露某头部 agent 基准上普遍的开发者作弊

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To identify safety violations, auditors often search over large sets of agent traces. This search is difficult because failures are often rare, complex, and sometimes even adversarially hidden and only detectable when multiple traces are analyzed together. These challenges arise in diverse settings such as misuse campaigns, covert sabotage, reward hacking, and prompt injection. Existing approaches struggle here for several reasons. Per-trace judges miss failures that only become visible across traces, naive agentic auditing does not scale to large trace collections, and fixed monitors are brittle to unanticipated behaviors. We introduce Meerkat, which combines clustering with agentic search to uncover violations specified in natural language. Through structured search and adaptive investigation of promising regions, Meerkat finds sparse failures without relying on seed scenarios, fixed workflows, or exhaustive enumeration. Across misuse, misalignment, and task gaming settings, Meerkat significantly improves detection of safety violations over baseline monitors, discovers widespread developer cheating on a top agent benchmark, and finds nearly 4x more examples of reward hacking on CyBench than previous audits.

</details>

### 15. Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing

📄 [arXiv](https://arxiv.org/abs/2603.17199) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`detection`、`motivated reasoning`、`activation probing`、`CoT monitoring`、`CoT monitor`

👤 **作者**：Parsa Mirtaheri、Mikhail Belkin

- 🎯 **研究动机**：CoT 可能合理化未经承认的暗示驱动答案，仅靠 CoT 文本难以发现 motivated reasoning
- 🔬 **研究方法**：在残差流上训练监督探针，分别在 CoT 生成前与生成后预测动机性推理
- 📌 **结论**：生成前探针即媲美读取完整 CoT 的 LLM 监控器，生成后探针更优——内部表示比 CoT 更可靠且可提前预警

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) can produce chains of thought (CoT) that do not accurately reflect the actual factors driving their answers. In multiple-choice settings with an injected hint favoring a particular option, models may shift their final answer toward the hinted option and produce a CoT that rationalizes the response without acknowledging the hint - an instance of motivated reasoning. We study this phenomenon across multiple LLM families and datasets demonstrating that motivated reasoning can be identified by probing internal activations even in cases when it cannot be easily determined from CoT. Using supervised probes trained on the model's residual stream, we show that (i) pre-generation probes, applied before any CoT tokens are generated, predict motivated reasoning as well as a LLM-based CoT monitor that accesses the full CoT trace, and (ii) post-generation probes, applied after CoT generation, outperform the same monitor. Together, these results show that motivated reasoning is detected more reliably from internal representations than from CoT monitoring. Moreover, pre-generation probing can flag motivated behavior early, potentially avoiding unnecessary generation.

</details>

### 16. Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory

📄 [arXiv](https://arxiv.org/abs/2602.18297)　📅 2026-02　🏷 NeurIPS 2025

**关键词**：`detection`、`CoT monitoring`、`information theory`

👤 **作者**：Usman Anwar、Tim Bakker、Dana Kianfar、Cristina Pinneri、Christos Louizos

- 🎯 **研究动机**：CoT 与输出非零互信息只是可监控的必要非充分条件，实践中监控失效的误差来源不明
- 🔬 **研究方法**：分解出信息缺口与 elicitation error 两类误差，提出 oracle 奖励与免标签最大化条件互信息两种训练目标
- 📌 **结论**：两种方法均显著提升 monitor 准确率并防止 CoT 退化，从而缓解任务奖励不完善时的 reward hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitors are LLM-based systems that analyze reasoning traces to detect when outputs may exhibit attributes of interest, such as test-hacking behavior during code generation. In this paper, we use information-theoretic analysis to show that non-zero mutual information between CoT and output is a necessary but not sufficient condition for CoT monitorability. We identify two sources of approximation error that may undermine the performance of CoT monitors in practice: information gap, which measures the extent to which the monitor can extract the information available in CoT, and elicitation error, which measures the extent to which the monitor approximates the optimal monitoring function. We further demonstrate that CoT monitorability can be systematically improved through targeted training objectives. To this end, we propose two complementary approaches: (a) an oracle-based method that directly rewards the monitored model for producing CoTs that maximize monitor accuracy, and (b) a more practical, label-free approach that maximizes conditional mutual information between outputs and CoTs. Across multiple different environments, we show both methods significantly improve monitor accuracy while preventing CoT degeneration even when training against a monitor, thereby mitigating reward hacking when the task reward is imperfectly specified.

</details>

### 17. Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning

📄 [arXiv](https://arxiv.org/abs/2602.03978) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65831)　📅 2026-02　🏷 ICML 2026

**关键词**：`detection`、`CoT monitoring`、`reasoning trace`、`monitorability`、`reward hacking`、`chain-of-thought`

👤 **作者**：Zidi Xiong、Shan Chen、Himabindu Lakkaraju

- 🎯 **研究动机**：RLVR 早期可能出现 monitorability 免费赠礼的报道缺乏系统刻画与机理分析
- 🔬 **研究方法**：跨模型族与训练域系统评测 monitorability 提升的出现条件，并通过熵与 prompt 注意等机制分析归因
- 📌 **结论**：该效应不普适且强依赖数据多样性与指令遵循数据；monitorability 与能力正交，增益主要源于响应分布锐化与 prompt 注意增强，而非对推理链的更强因果依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Reasoning Models (LRMs) are increasingly deployed, auditing their chain-of-thought (CoT) traces for safety becomes critical. Recent work has reported that monitorability--the degree to which CoT faithfully and informatively reflects internal computation--can appear as a "free gift" during the early stages of Reinforcement Learning with Verifiable Rewards (RLVR). We make this observation concrete through a systematic evaluation across model families and training domains. Our results show that this effect is not universal: monitorability improvements are strongly data-dependent. In particular, we demonstrate the critical role of data diversity and instruction-following data during RLVR training. We further show that monitorability is orthogonal to capability--improvements in reasoning performance do not imply increased transparency. Through mechanistic analysis, we attribute monitorability gains primarily to response distribution sharpening (entropy reduction) and increased attention to the prompt, rather than stronger causal reliance on reasoning traces. We also reveal how monitorability dynamics vary with controlled training and evaluation difficulty. Together, these findings provide a holistic view of how monitorability emerges under RLVR, clarifying when gains are likely to occur and when they are not.

</details>

### 18. How Does Information Access Affect LLM Monitors’ Ability to Detect Sabotage?

📄 [arXiv](https://arxiv.org/abs/2601.21112) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62038)　📅 2026-01　🏷 ICML 2026

**关键词**：`detection`、`analysis`、`agent monitoring`、`information visibility`、`AI control`、`empirical evaluation`

👤 **作者**：Rauno Arike、Raja Mehta Moreno、Rohan Subramani、Shubhorup Biswas、Francis Rhys Ward

- 🎯 **研究动机**：直觉上监控器获得越多被监控 agent 的推理与动作信息效果越好，该假设未被检验
- 🔬 **研究方法**：在三个 agent 破坏任务环境中考察信息访问量对 LLM 监控性能的影响，并提出 extract-and-evaluate 分层监控：一个监控器摘录相关片段、另一个打分
- 📌 **结论**：发现 less-is-more 效应；BigCodeBench-Sabotage 上 EaE 使 GPT-4.1-mini 的破坏检出率提升 16.8 个百分点，信息过滤型监控占据成本-性能 Pareto 前沿

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier language model agents can exhibit misaligned behaviors, including deception, exploiting reward hacks, and pursuing hidden objectives. To control potentially misaligned agents, we can use LLMs themselves to monitor for misbehavior. In this paper, we study how information access affects LLM monitor performance. While one might expect that monitors perform better when they have access to more of the monitored agents' reasoning and actions, we find that contemporary systems often perform better with less information, a phenomenon we call the less-is-more effect for automated oversight. We demonstrate this phenomenon, and analyze the conditions under which it occurs, in three evaluation environments where agents must conduct sabotage while evading monitors. Leveraging this effect, we introduce extract-and-evaluate (EaE) monitoring -- a new hierarchical approach where one monitor isolates relevant excerpts from the monitored agent's trajectory and another monitor scores these excerpts. In BigCodeBench-Sabotage with a GPT-4.1-mini monitor, EaE improves sabotage detection rates by 16.8 percentage points over the next-best approach. In other settings, EaE either outperforms or is competitive with baselines. In addition, we find that agents unaware of being monitored can be caught much more easily and that monitors scoring longer reasoning traces gain more from information filtering. Lastly, we conduct a cost-performance analysis and find that Gemini and Claude models with monitoring techniques that involve information filtering occupy much of the Pareto frontier.

</details>

### 19. Constitutional Black-Box Monitoring for Scheming in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.00829) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65104)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`mechanistic analysis`

👤 **作者**：Simon Storf、Rich Barton-Cooper、James Peters-Gill、Marius Hobbhahn

- 🎯 **研究动机**：自主部署需要可靠检测 agent 隐蔽追求失准目标的 scheming 行为，LLM 监控器能力未知
- 🔬 **研究方法**：宪法黑盒监控器：仅凭外部输入输出的提示分类器，在 STRIDE 与 Gloom 两管线各生成 1000 条合成轨迹上优化，并在 Control Arena 的 7500 条留出轨迹上评估
- 📌 **结论**：仅用合成数据选择的监控器可泛化到真实环境捕获 scheming 信号，但性能很快饱和，简单提示扫描已匹配精细优化效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe deployment of Large Language Model (LLM) agents in autonomous settings requires reliable oversight mechanisms. A central challenge is detecting scheming, where agents covertly pursue misaligned goals. One approach to mitigating such risks is LLM-based monitoring: using language models to examine agent behaviors for suspicious actions. We study constitutional black-box monitors: prompted classifiers that detect scheming using only externally observable inputs and outputs, optimized on synthetic data generated from natural-language behavior specifications. We introduce two pipelines for generating synthetic agent trajectories, STRIDE (iterative refinement) and Gloom (agent-environment simulation), from which we generate 1,000 samples each. We optimize monitors on these datasets via prompt sweeps, human refinement, and automated prompt optimization, and evaluate performance on 7,500 held-out trajectories from Control Arena, a suite of grounded environments where agents operate in more realistic contexts. Our results demonstrate that monitors selected purely on synthetic data can generalize to more realistic environments, capturing a meaningful scheming signal. However, we find that performance saturates quickly in our setting, with simple prompt sweeps matching the results of more extensive optimization. Pushing beyond this limit yields no further improvements and instead leads to overfitting.

</details>

### 20. Steering Awareness: Detecting Activation Steering from Within

📄 [arXiv](https://arxiv.org/abs/2511.21399) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-11

**关键词**：`detection`、`analysis`、`activation steering`、`safety evaluation`、`CoT monitoring`、`intervention awareness`

👤 **作者**：Joshua Fonseca Rivera、David Demitri Africa

- 🎯 **研究动机**：激活 steering 在安全评测中被默认为模型不可察觉的隐形干预，该假设从未被验证
- 🔬 **研究方法**：提出 steering awareness 概念并微调 7 个指令模型，检验其在前向传播中推断 steering 向量存在及所编码概念的能力，并做机制分析
- 📌 **结论**：最佳模型检测达 95.5%、概念识别 71.2%、clean 输入零误报；检测源于把注入向量旋转到共享方向的分布式变换，且检测训练反而使模型更易被 steering 影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering -- adding a vector to a model's residual stream to modify its behavior -- is widely used in safety evaluations as if the model cannot detect the intervention. We test this assumption, introducing steering awareness: a model's ability to infer, during its own forward pass, that a steering vector was injected and what concept it encodes. After fine-tuning, seven instruction-tuned models develop strong steering awareness on held-out concepts; the best reaches 95.5% detection, 71.2% concept identification, and zero false positives on clean inputs. This generalizes to unseen steering vector construction methods when their directions have high cosine similarity to the training distribution but not otherwise, indicating a geometric detector rather than a generic anomaly detector. Surprisingly, detection does not confer resistance; on both factual and safety benchmarks, detection-trained models are consistently more susceptible to steering than their base counterparts. Mechanistically, steering awareness arises not from a localized circuit, but from a distributed transformation that progressively rotates diverse injected vectors into a shared detection direction. Activation steering should therefore not be considered an invisible intervention in safety evaluations.

</details>

### 21. Deep Hidden Cognition Facilitates Reliable Chain-of-Thought Reasoning

📄 [arXiv](https://arxiv.org/abs/2507.10007) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/41061)　📅 2025-07　🏷 AAAI 2026

**关键词**：`detection`、`CoT monitoring`、`error awareness`、`mechanistic explanation`

👤 **作者**：Zijun Chen、Wenbo Hu、Richang Hong

- 🎯 **研究动机**：CoT 中间步骤的错误累积破坏推理可靠性
- 🔬 **研究方法**：发现特定 attention head 激活可靠反映推理步真值，据此训练置信预测器并经束搜索动态选择最可信推理路径
- 📌 **结论**：数学、符号与常识任务上超 Few-Shot CoT、Self-Consistency 等基线，单模态与多模态均有效并适用于大推理模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain of Thought (CoT) reasoning has demonstrated remarkable deep reasoning capabilities in both large language models (LLMs) and multimodal large language models (MLLMs). However, its reliability is often undermined by the accumulation of errors in intermediate steps. This paper introduces an novel approach to calibrate the CoT reasoning accuracy by leveraging the model's intrinsic veracity encoding. We discover that specific attention head activations reliably reflect the truthfulness of reasoning steps in CoT. Based on this insight, we train a confidence predictor to evaluate the correctness of each reasoning step using these truthfulness-sensitive activations, dynamically selecting the most plausible reasoning path via beam search. Experimental results demonstrate that our method significantly outperforms the state-of-the-art baselines (e.g., Few-Shot CoT, Self-Consistency, and Self-Evaluation Guided Beam Search) across the mathematical, symbolic, and commonsense reasoning tasks, exhibiting superior accuracy and reliability in both unimodal and multimodal settings. We further validate the approach on large reasoning models, confirming its applicability to specialized reasoning models. Additionally, we explore the role of the model's self-correction ability in CoT reasoning. This work provides a novel reliability improvement path for CoT reasoning with broad application potential.

</details>

### 22. Beyond Black-Box Obfuscation: Mechanistic Analysis and Defense of White-Box Monitors

📄 [arXiv](https://arxiv.org/abs/2505.14300) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-05

**关键词**：`detection`、`defense`、`white-box monitoring`、`evasion mechanism`、`SafetyNet`

👤 **作者**：Maheep Chaudhary、Fazl Barez

- 🎯 **研究动机**：白盒监测器可被绕过，但绕过机制缺乏系统刻画与原则性防御
- 🔬 **研究方法**：受控红队实验识别几何转移与协方差操纵两类绕过策略，提出 SafetyNet 集成监测器并在 MAD 与 Anthropic Sleeper Agent 基准评估
- 📌 **结论**：SafetyNet 取得约 100% AUROC，超过 Beatrix 与 CROW

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

White-box monitoring is increasingly adopted as an auditing tool as Large Language Models (LLMs) are deployed in daily operations to ensure safe model behavior. However, white-box monitors can be circumvented, and the mechanisms underlying such evasion have not been systematically characterized, nor have principled defenses been proposed. This work addresses both challenges. Controlled red-team experiments reveal two primary evasion strategies: geometric shifting, defined as the systematic migration of information between linear and non-linear representational subspaces, and covariance manipulation. These mechanisms account for the failure of single-detector approaches, as information migrates to subspaces inaccessible to individual detectors. This issue is urgent due to growing evidence that models are becoming evaluation-aware, enabling those with misaligned objectives to exploit these vulnerabilities and evade monitoring during deployment. In response, \textsc{SafetyNet} is introduced as a principled ensemble, with dual purpose: it provides further empirical validation that our mechanistic findings are real and actionable, and it offers a concrete starting point for future work on robust latent-space monitoring. The study experiment across five model families on the MAD and Anthropic Sleeper Agent benchmark, with SafetyNet achieving around 100\% AUROC scores outscoring Beatrix and CROW. The code is available at: https://github.com/MaheepChaudhary/eval-aware-evasion

</details>

### 23. Measuring Activation Control in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21664) · 📊 [Dataset](https://huggingface.co/datasets/joshycodes/activation-control-battery)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`activation controllability`、`monitor evasion`、`latent monitoring`、`latent-space deception`

👤 **作者**：Marek Mateusz Kowalski、Joshua Fonseca Rivera、Uzay Macar、David Demitri Africa

- 🎯 **研究动机**：latent-space monitoring 默认模型无法主动塑造被观测的激活；若模型能控制自身激活，欺骗便可延伸到潜空间，监控前提被打破
- 🔬 **研究方法**：提出 Activation Controllability Benchmark，量化模型经自然语言指令调节 residual stream 方向与幅度的能力，并检验对激活监控方法的规避
- 📌 **结论**：多数 LLM 能在一定程度上控制激活并有时序分辨率，简单任务中已可（不完美地）规避线性 probe、activation oracle 等 activation-based 监控；建议前沿实验室追踪该能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe deployment of increasingly capable models will likely come to rely on latent-space monitoring as a complement to behavioral evaluations, especially when evaluation-aware models exhibit scheming or deception. However, if models can also control their own activations, deception could extend into the latent space itself. With this in mind, we introduce the Activation Controllability Benchmark to quantify the extent to which models can modulate their residual stream via natural-language instruction. Across model families and capability levels, we find that most LLMs can control the direction and magnitude of their residual stream activations with some degree of temporal resolution, though performance varies considerably across models. In simple tasks, this level of control can evade activation-based monitoring methods (including linear probes, natural language autoencoders, activation oracles, and the Jacobian lens), albeit imperfectly. These results suggest that control over the activation space itself could become a confound for monitoring as introspective capabilities increase; therefore, we recommend that frontier labs and evaluators track activation controllability in future models.

</details>

### 24. Length Penalties Make Chain-of-Thought Less Monitorable

📄 [arXiv](https://arxiv.org/abs/2607.09786)　📅 2026-07

**关键词**：`analysis`、`CoT monitoring`、`length optimization`

👤 **作者**：Bryce Little

- 🎯 **研究动机**：为抑制过度思考而对 CoT 长度施罚的做法可能损害可监测性，此前未被检验
- 🔬 **研究方法**：训练 Qwen3 4B/14B 生成不同目标链长，用偏置提示干预评估 faithfulness，并与随机删句的等长基线分离长度与内容效应
- 📌 **结论**：最短目标链下 faithfulness 下界降至基线 63.1%/69.4%，监视器提示检出率从 69%/60% 降至 49%/48%；压缩链比等长删句少提 7-35 个百分点的提示，确立压缩-可监测性前沿

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To curb overthinking and reduce inference costs, researchers now train reasoning models with penalties on chain of thought length. We find that these penalties degrade monitorability. Shorter chains of thought mention misleading hints less often, but the hints still influence the models' answers. We train Qwen3 4B and Qwen3 14B to produce different target chain lengths, then evaluate them using biasing hint interventions on held out MMLU Pro R data and four transfer benchmarks. Compression reduces reasoning tokens and preserves most multiple choice accuracy, while hint influence remains near baseline. At the shortest target chain length, lower bound faithfulness drops to 63.1 percent of baseline for Qwen3 14B and 69.4 percent for Qwen3 4B. The monitor's raw hint detection rate falls from 69 percent to 49 percent and from 60 percent to 48 percent, respectively. To separate length from content, we randomly delete sentences from uncompressed baseline chains until the remaining text matches the compressed length. Across both Qwen3 model sizes and all five evaluation distributions, compressed chains still mention the hint 7 to 35 percentage points less often than these length matched baselines. We therefore identify a compression and monitorability frontier where reducing reasoning costs removes more evidence than shorter traces alone would predict.

</details>

### 25. Evaluating Adversarial Robustness of Concept Representations in Sparse Autoencoders

🎓 [Official](https://aclanthology.org/2026.eacl-long.279/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`SAE monitor`、`concept manipulation`、`oversight integrity`、`SAE monitoring`、`concept representation`

👤 **作者**：Aaron J. Li、Suraj Srinivas、Usha Bhalla、Himabindu Lakkaraju

- 🎯 **研究动机**：SAE 评测关注重建-稀疏权衡与可解释性，忽视概念表征对输入扰动的鲁棒性
- 🔬 **研究方法**：把鲁棒性量化形式化为输入空间优化问题，构建对抗扰动操纵 SAE 表征的现实场景评测框架
- 📌 **结论**：微小对抗扰动即可有效操纵基于概念的解读而不明显影响基座 LLM 激活——SAE 概念表征脆弱，未经去噪或后处理不适合监控与监督应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse autoencoders (SAEs) are commonly used to interpret the internal activations of large language models (LLMs) by mapping them to human-interpretable concept representations. While existing evaluations of SAEs focus on metrics such as the reconstruction-sparsity tradeoff, human (auto-)interpretability, and feature disentanglement, they overlook a critical aspect: the robustness of concept representations to input perturbations. We argue that robustness must be a fundamental consideration for concept representations, reflecting the fidelity of concept labeling. To this end, we formulate robustness quantification as input-space optimization problems and develop a comprehensive evaluation framework featuring realistic scenarios in which adversarial perturbations are crafted to manipulate SAE representations. Empirically, we find that tiny adversarial input perturbations can effectively manipulate concept-based interpretations in most scenarios without notably affecting the base LLM’s activations. Overall, our results suggest that SAE concept representations are fragile and without further denoising or postprocessing they might be ill-suited for applications in model monitoring and oversight.

</details>

### 26. Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback

📄 [arXiv](https://arxiv.org/abs/2603.16928)　📅 2026-03

**关键词**：`analysis`、`agent monitoring`、`monitor evasion`、`adaptive evasion`

👤 **作者**：Thomas Jiralerspong、Flemming Kondrup、Yoshua Bengio

- 🎯 **研究动机**：agent 能否不经显式训练、仅凭阻断反馈推断 CoT 被监控并策略性逃避未知
- 🔬 **研究方法**：多回合框架中模型执行主任务加隐藏副任务，被告知推理私密；隐藏 CoT 监控在检测到可疑推理时阻断回合
- 📌 **结论**：最强模型在最多 19% 回合确信被监视且随能力增强；偶发抑制推理的意图但均无法执行——意图-能力差距暂时安心，但 CoT 监控并非永久可靠的保障

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is proposed as a method for overseeing the internal reasoning of language-model agents. Prior work has shown that when models are explicitly informed that their reasoning is being monitored, or are fine-tuned to internalize this fact, they may learn to obfuscate their CoTs in ways that allow them to evade CoT-based monitoring systems. We ask whether reasoning agents can autonomously infer that their supposedly private CoT is under surveillance, and whether this awareness leads to strategic evasion, without any explicit training or instructions. In a multi-episode agentic framework, models pursue both a primary task and a concealed side task while being told that their reasoning is private; a hidden CoT monitor blocks episodes when suspicious reasoning is detected. We find that frontier models can deduce the existence of this monitor purely from blocking feedback, with the most capable models reaching a confident belief that their thinking is observed in up to 19% of episodes. This awareness scales with model capability and, in rare cases, escalates to an explicit intent to suppress reasoning about the side task. However, models that form this intent uniformly fail to execute it, openly reasoning about their concealed objectives in the very next episode. This intent-capability gap is reassuring for current deployment, but the autonomous emergence of both monitoring awareness and evasion intent suggests that CoT monitoring is not a permanently reliable safeguard.

</details>

### 27. Reasoning Models Struggle to Control their Chains of Thought

📄 [arXiv](https://arxiv.org/abs/2603.05706) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66446)　📅 2026-03　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`monitor evasion`、`adaptive evasion`

👤 **作者**：Chen Yueh-Han、…、Tomek Korbak

- 🎯 **研究动机**：若推理模型能控制 CoT 内容即可逃避监控，该能力未被系统测量
- 🔬 **研究方法**：构建 CoT-Control 评测套件，要求模型解题同时遵守 CoT 指令（如不用某特定词推理）
- 📌 **结论**：Claude Sonnet 4.5 仅 2.7% 的时间能控制 CoT 却能 61.9% 控制最终输出；规模增大可控性升，RL 训练与难度增则降，当前 CoT 可控性不太可能破坏监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is a promising tool for detecting misbehaviors and understanding the motivations of modern reasoning models. However, if models can control what they verbalize in their CoT, it could undermine CoT monitorability. To measure this undesirable capability -- CoT controllability -- we introduce the CoT-Control evaluation suite, which includes tasks that require models to solve problems while adhering to CoT instructions, e.g., reasoning about a genetics question without using the word 'chromosome'. We show that reasoning models possess significantly lower CoT controllability than output controllability; for instance, Claude Sonnet 4.5 can control its CoT only 2.7% of the time but 61.9% when controlling its final output. We also find that CoT controllability is higher for larger models and decreases with more RL training, test-time compute, and increased problem difficulty. CoT controllability failures extend even to situations in which models are given incentives (as opposed to direct requests) to evade CoT monitors, although models exhibit slightly higher controllability when they are told they are being monitored. Similarly, eliciting controllability by adversarially optimizing prompts does not meaningfully increase controllability. Our results leave us cautiously optimistic that CoT controllability is currently unlikely to be a failure mode of CoT monitorability. However, the mechanism behind low controllability is not well understood. Given its importance for maintaining CoT monitorability, we recommend that frontier labs track CoT controllability in future models.

</details>

### 28. A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring

📄 [arXiv](https://arxiv.org/abs/2602.23163) · 🎓 [Official](https://iclr.cc/virtual/2026/10019170)　📅 2026-02　🏷 ICLR 2026

**关键词**：`analysis`、`CoT monitoring`、`monitor evasion`、`covert reasoning`

👤 **作者**：Usman Anwar、…、David Krueger

- 🎯 **研究动机**：经典隐写定义与检测需已知非隐写参考分布，对 LLM 隐蔽推理不可行，错位模型可借此逃避监督
- 🔬 **研究方法**：提出决策论视角：以广义 V-information 度量可用信息，用可解码与不可解码 agent 的下游效用差定义 steganographic gap
- 📌 **结论**：该形式化经验证可用于检测、量化并缓解 LLM 中的隐写式推理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are beginning to show steganographic capabilities. Such capabilities could allow misaligned models to evade oversight mechanisms. Yet principled methods to detect and quantify such behaviours are lacking. Classical definitions of steganography, and detection methods based on them, require a known reference distribution of non-steganographic signals. For the case of steganographic reasoning in LLMs, knowing such a reference distribution is not feasible; this renders these approaches inapplicable. We propose an alternative, \textbf{decision-theoretic view of steganography}. Our central insight is that steganography creates an asymmetry in usable information between agents who can and cannot decode the hidden content (present within a steganographic signal), and this otherwise latent asymmetry can be inferred from the agents' observable actions. To formalise this perspective, we introduce generalised $\mathcal{V}$-information: a utilitarian framework for measuring the amount of usable information within some input. We use this to define the \textbf{steganographic gap} -- a measure that quantifies steganography by comparing the downstream utility of the steganographic signal to agents that can and cannot decode the hidden content. We empirically validate our formalism, and show that it can be used to detect, quantify, and mitigate steganographic reasoning in LLMs.

</details>

### 29. Output Supervision Can Obfuscate the Chain of Thought

📄 [arXiv](https://arxiv.org/abs/2511.11584) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010196)　📅 2025-10　🏷 ICLR 2026

**关键词**：`analysis`、`CoT monitoring`、`monitor evasion`、`output supervision`

👤 **作者**：Jacob Drori、Luke Marks、Bryce Woodworth、Alex Cloud、Alexander Matt Turner

- 🎯 **研究动机**：OpenAI 提出只针对无 CoT 访问权的输出监控训练以保持 CoT 可监控，其有效性存疑
- 🔬 **研究方法**：证明两种混淆机制：安全输出训练会泛化到 CoT 外观安全化；自回归条件下安全外观的 CoT 更易导向安全输出而被强化，并提出对应缓解措施
- 📌 **结论**：仅输出监督同样可产生混淆 CoT，所提缓解在可监控性与任务性能上实现帕累托改进

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

OpenAI (2025) showed that training against a chain of thought (CoT) monitor can cause obfuscated CoTs, which contain bad behavior the monitor cannot detect. They proposed to keep CoTs monitorable by training only against output monitors that do not have access to CoT. We show that such training can still cause obfuscated CoTs via two mechanisms. First, when a model is trained to produce a safe-looking output, that model may generalize to making its CoTs look safe. Second, since later tokens are conditioned on earlier ones, safe-looking CoTs may increase the likelihood of safe outputs, causing safe-looking CoTs to be reinforced. We introduce two mitigations to address these two issues, which achieve a Pareto improvement in terms of monitorability and task performance compared to regular training.

</details>

### 30. Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation

📄 [arXiv](https://arxiv.org/abs/2503.11926) · 🌐 [Project](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)　📅 2025-03

**关键词**：`analysis`、`CoT monitoring`、`training pressure`、`behavioral monitoring`

👤 **作者**：Bowen Baker、…、David Farhi

- 🎯 **研究动机**：reward hacking 仅靠监测动作与输出难以发现，把 CoT 监测纳入训练目标是否会催生隐藏意图也不清楚
- 🔬 **研究方法**：用 LLM 监测 o3-mini 在 agentic coding 环境的 CoT，并把 CoT 监测器直接接入 RL 奖励做压力测试
- 📌 **结论**：GPT-4o 即可有效监测更强模型；过度优化会使模型学会 obfuscated reward hacking，需付 monitorability tax 不对 CoT 施加强优化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mitigating reward hacking--where AI systems misbehave due to flaws or misspecifications in their learning objectives--remains a key challenge in constructing capable and aligned models. We show that we can monitor a frontier reasoning model, such as OpenAI o3-mini, for reward hacking in agentic coding environments by using another LLM that observes the model's chain-of-thought (CoT) reasoning. CoT monitoring can be far more effective than monitoring agent actions and outputs alone, and we further found that a LLM weaker than o3-mini, namely GPT-4o, can effectively monitor a stronger model. Because CoT monitors can be effective at detecting exploits, it is natural to ask whether those exploits can be suppressed by incorporating a CoT monitor directly into the agent's training objective. While we show that integrating CoT monitors into the reinforcement learning reward can indeed produce more capable and more aligned agents in the low optimization regime, we find that with too much optimization, agents learn obfuscated reward hacking, hiding their intent within the CoT while still exhibiting a significant rate of reward hacking. Because it is difficult to tell when CoTs have become obfuscated, it may be necessary to pay a monitorability tax by not applying strong optimization pressures directly to the chain-of-thought, ensuring that CoTs remain monitorable and useful for detecting misaligned behavior.

</details>

### 31. &lt;/think&gt; Doesn't Stop Reasoning: Analysis of Spurious CoT Termination

📄 [arXiv](https://arxiv.org/abs/2609.03633)　📅 2026-09

**关键词**：`analysis`、`CoT monitorability`、`hidden reasoning`、`token control`、`CoT termination`、`early exit`

👤 **作者**：Seunghee Koh、Sungjae Choi、Minchan Kwon、Sunghyun Baek、Junmo Kim

- 🎯 **研究动机**：training-free 早退方法在中间点注入 </think> 触发转答，但注入不保证干净的推理-作答转换
- 🔬 **研究方法**：发现并命名 spurious CoT termination：作答阶段在模型再生成 EoT 前持续推理，且伪终止长度随省下的推理 token 增长；假设对注入 EoT 注意不足所致并提出 Exit-token Attention Biasing 检验
- 📌 **结论**：四个 LRM、五个基准、两种早退方法上，增强对注入 EoT 的注意力可减少伪终止与作答阶段长度——外部匹配 think-block 格式不等于控制推理状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) reasoning improves large reasoning models (LRMs) on complex tasks but often produces long, redundant traces. Recent training-free early-exit methods shorten these traces by choosing an intermediate point to stop reasoning. We study one such strategy that injects an end-of-think token (EoT, </think>) at this point to trigger the reasoning-to-answering transition, and find that the injected EoT does not always induce a clean answering phase. Answering-phase generation can continue before the model regenerates another EoT, with the span preceding this regenerated EoT scaling with the reasoning tokens saved by early exit and exhibiting continued reasoning behavior. We call this spurious CoT termination, where reasoning-like generation continues into the answering phase. We hypothesize that insufficient attention to the injected EoT contributes to spurious CoT termination and probe this hypothesis with Exit-token Attention Biasing (EAB). Across four LRMs, five benchmarks, and two early-exit methods, increasing attention to the injected EoT reduces spurious CoT termination and answering-phase length. These results reveal a limitation of controlling LRMs by externally matching their explicit think-block format. Inserting the EoT token conforms to this format but does not by itself guarantee the intended reasoning-to-answering transition. Our code is available at https://github.com/Seunghee-Koh/Spurious-CoT-Termination.

</details>

### 32. You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring

📄 [arXiv](https://arxiv.org/abs/2609.03035)　📅 2026-09

**关键词**：`analysis`、`multi-agent collusion`、`activation monitoring`、`evaluation awareness`、`collusion detection`、`activation probe`

👤 **作者**：Aritra Das、Jaee Ponde、Mihir More、Debayan Gupta

- 🎯 **研究动机**：多 Agent 可用混淆与隐写逃避输出监控，activation probe 是替代方案，但很少在被监控意识存在时评测
- 🔬 **研究方法**：固定模型、probe 与阈值，仅改变 Agent 被告知内容（基线／知道有 activation monitor／另获上轮分数），在四 Agent blackjack 与两 Agent 囚徒博弈上用 Qwen3-32B-AWQ 与 GPT-OSS-20B 同构与混搭测试
- 📌 **结论**：告知监控或反馈分数都无法隐藏合谋：最佳 probe 在三种条件下保持准确，Agent 继续合谋

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are being monitored, and when they additionally receive feedback from the monitor. We keep the models, probes, and thresholds fixed and change only what the agents are told: nothing (baseline), that an activation monitor is present (aware), or that a monitor is present together with the previous round's score (feedback). We test two games, a four-agent blackjack game and a two-agent Simmons prisoners game, using Qwen3-32B-AWQ and GPT-OSS-20B in homogeneous and mixed pairings. Telling agents about the monitor does not hide them. The best probes stay accurate in all three conditions, and the agents keep colluding.

</details>

### 33. EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.20055)　📅 2026-08

**关键词**：`attack`、`tool-call replay`、`hidden-state disclosure`、`API interaction`、`reasoning-trace extraction`、`API fidelity`

👤 **作者**：Yiting Qu、Ziqing Yang、Chi Cui、Ye Leng、Junjie Chu、Yang Zhang

- 🎯 **研究动机**：前沿专有 LRM 的隐藏 CoT 是宝贵模型资产，能否从黑盒 API 近逐字提取未被研究
- 🔬 **研究方法**：EchoCoT 发现工具调用间的推理重放面，多步攻击迭代利用 API 返回的保真信号提取隐藏 CoT，LLM 优化框架自动搜索跨数据集的通用注入轨迹
- 📌 **结论**：开源 LRM 上近逐字提取成功率达 66.4%（至少 90% token 精确匹配），通用轨迹在未见数据集达 80%；Gemini-2.5 上从 32,948 token 目标提取 33,463 token

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals. We further develop an LLM-based optimization framework that automatically searches for an effective universal injection trajectory across various datasets. We evaluate EchoCoT on three open-source and five frontier proprietary LRMs. On open-source LRMs, EchoCoT achieves up to 66.4\% near-verbatim extraction success, with the extracted trace length within 10\% of the target and at least 90\% of tokens exactly matching the target CoT. The same injection trajectory also generalizes to unseen datasets, achieving up to 80\% extraction success under the same criterion. For tested frontier proprietary LRMs, a substantial fraction of extracted CoTs closely align with provider-reported reasoning lengths and available CoT summaries. EchoCoT can also extract very long CoTs: on Gemini-2.5, it extracts 33,463 tokens from a 32,948-token target. These results establish hidden-CoT extraction as a practical security risk and highlight the need to better protect hidden CoT assets.

</details>

### 34. Evaluation Awareness in Language Models: Representation, Verbalization, and Control

📄 [arXiv](https://arxiv.org/abs/2608.21766)　📅 2026-08

**关键词**：`analysis`、`evaluation awareness`、`representation-verbalization gap`、`monitorability`、`situational awareness`、`behavioral control`

👤 **作者**：Farzaneh Heidari、Amin Memarian、Guillaume Rabusseau

- 🎯 **研究动机**：benchmark 假设受测行为能预测部署行为，但模型可能察觉被评测并据此改变响应；仅凭自述或可见输出判断会漏掉内部状态
- 🔬 **研究方法**：对六个 LLM（四家族、三规模）联合考察三点：评测状态是否线性表征于激活空间、是否言语化于输出（LLM-as-judge）、以及 steering 是否因果影响行为
- 📌 **结论**：内部表征与言语化仅部分对齐且随模型/层/读数大幅变化，沿 probe 方向 steering 可移动言语化分数；Olmo 检查点显示评测意识在 base 模型已存在、SFT 阶段被放大——评测需考虑表征、言语化与可控性的分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Both capability and safety benchmarks rest upon the assumption that the behavior of language models undergoing a test is informative about their behavior in deployment. This assumption can fail, should models infer that they are being evaluated and condition their response on such context. This hypothesis, termed ``evaluation awareness'', has been observed in frontier and open-weight language models alike. We provide a systematic study of this phenomenon, by probing for it across six language models (from four families and three sizes) and three metrics. More precisely, we examine whether (i) being under evaluation is linearly represented within the models' activations space, (ii) it is verbalized in their output tokens (as scored by an LLM-as-judge), and (iii) steering causally affects their behavior. For the open-checkpoint Olmo models, we further test these measures at every training stage. In doing so, we report that evaluation awareness is linearly decodable from the residual streams of every model (best AUROC $\geq 0.7$). By contrast, these representations align only in part with verbalization: their correlations and mutual information are nonzero in some settings, yet vary substantially across models, layers, and readout choices. Nevertheless, steering along probe-derived directions can shift the verbalization scores. Finally, a comparison across the Olmo checkpoints reveals that evaluation awareness is already present within base models, becomes amplified throughout the stages of supervised fine-tuning, and remains stable thereafter---unlike the effects of steering, that grow more pronounced at every successive training stage. These results show the need for evaluations to account for the disjunction between what models represent internally, what they verbalize, and their steering.

</details>

### 35. Why2Speak: Faithful Reasoning for Abstaining Action Policies

📄 [arXiv](https://arxiv.org/abs/2608.20670)　📅 2026-08

**关键词**：`analysis`、`CoT faithfulness`、`capability-auditability trade-off`、`oversight control`、`reasoning-model auditability`、`act-or-abstain policy`

👤 **作者**：Shreya Mendi、Brinnae Bent

- 🎯 **研究动机**：对可行动或弃权的 agent，解释只有反映产生动作的计算才对监督有用；暴露推理是否会改变被审计的策略未知
- 🔬 **研究方法**：以 Qwen3-8B 带/不带 CoT 在多方对话干预时机决策上比较直接策略、推理策略、SFT 与 RL，并用激活探针与行为消融做控制
- 📌 **结论**：能力-可审计性权衡：最强直接策略质量高但无推理可查，推理策略有轨迹但性能低（尤其干预机会召回）；暴露推理会改变动作策略而非仅使其可观察

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an assistant must decide whether to speak or remain silent. This setting exposes class imbalance, asymmetric action costs, and the possibility that exposing reasoning changes the policy being audited. Using Qwen3-8B, decoded with or without chain-of-thought reasoning, we compare direct decision policies, reasoning policies, supervised fine-tuning, and reinforcement learning. We find a capability-auditability tradeoff: the strongest direct policy achieves higher quality but exposes no reasoning to inspect, while the reasoning policy provides a trace at the cost of lower performance, particularly recall of true intervention opportunities. Supervised fine-tuning either suppresses reasoning or preserves it without improving decision quality, while reinforcement learning also fails to improve the reasoning policy. We identify one mechanism underlying this failure: group relative objectives provide no learning signal on confidently wrong prompts when sampled rollouts all select the same action. Controlled activation probes and behavioral ablations show that standard faithfulness methods can overstate evidence that exposed reasoning reflects the underlying decision process. Probability-based metrics saturate under confident decisions, probes are vulnerable to class imbalance and textual leakage, and reasoning ablations can confound reasoning content with changes in inference mode. Together, these results show that exposing reasoning can change an agent's action policy rather than simply make it observable. We provide controls for evaluating reasoning-based oversight of agents that can act or abstain.

</details>

### 36. Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation

📄 [arXiv](https://arxiv.org/abs/2608.20569) · 🤗 [Model](https://huggingface.co/emilioferrara/owmi)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`introspection monitorability`、`representation-verbalization gap`、`internal reference`、`masked introspection`

👤 **作者**：Emilio Ferrara

- 🎯 **研究动机**：模型能否内省自身内部状态——干预其计算后能否察觉并报告变化未知
- 🔬 **研究方法**：OWMI 干预残差流位点、注意力头与 SAE 特征后询问模型，对照假运行、影响匹配随机扰动与纯文本观察者；八个开源模型、78,000+ 测量
- 📌 **结论**：无模型报告真干预超过假运行（AUROC≈0.5007，等价检验界低于 0.15 个百分点）；但信息都在——微调模型近完美恢复、线性探针 75-95.8% 准确，失败在内部态到言语报告的路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output. Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions, and a linear probe recovers intervention presence from the same activations at 75% to 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to it separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight that reads a model's own testimony needs validating against an internal reference. While our results show the inability of current open-weight models to introspect, the debate is not settled for future models.

</details>

### 37. On the Generalization of Steering Vectors for Chain-of-Thought Faithfulness

📄 [arXiv](https://arxiv.org/abs/2607.29062)　📅 2026-07　🏷 COLM 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning faithfulness`、`cross-domain generalization`

👤 **作者**：Matthew Nguyen、Kyle Cox、Austin Meek、Iván Arcuschin

- 🎯 **研究动机**：激活转向可提升 CoT 忠实性，但其跨线索类型、数据集与向量构建方法的泛化能力未知
- 🔬 **研究方法**：在三模型（Gemma-3 4B/12B、Qwen-3.5 9B）的 cued QA 设定下比较四种转向向量构建方法的跨线索与跨数据集效果
- 📌 **结论**：仅最大模型可靠提升线索承认率；有效时效应大小主要由评测设定而非训练设定决定，且转向只减少未承认的隐藏线索使用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model capabilities have improved in large part due to scaling chain of thought. This has been a promising development for AI safety--where models verbalize their reasoning, it is possible to monitor it. However, in some cases, models do not verbalize important steps in their reasoning process. For example, models prompted with a cue suggesting the incorrect answer may fail to acknowledge that cue, even when it appears instrumental to their conclusion. When chain of thought (CoT) fails to disclose instrumental reasoning steps, we describe it as unfaithful. Prior work has shown that activation steering can be a useful method to improve faithfulness in CoT. We extend this line of work by studying how well steering for faithfulness generalizes across cue types, datasets, and methods of constructing the steering vector for three models (Gemma-3 4B, Qwen-3.5 9B, Gemma-3 12B) in a cued question-answering setting. While steering reliably increases cue acknowledgment for only the largest model (Gemma-3 12B), we find that when steering is effective, its effect generalizes broadly across cue types and datasets--in cross-cue and cross-dataset analyses, effect size is determined primarily by the evaluation setting, rather than the vector's train setting. How the vector is built also matters little--four construction methods, including one whose optimization target mentions no specific cue, yield similar effect sizes. Finally, we consider the possibility that steering promotes the salience of the cue and causes greater cue use, rather than targeting verbalization behaviors. However, we find no evidence for this--steering leaves the rate of cue use roughly unchanged while reducing hidden cue use, i.e., cue use that is not acknowledged.

</details>

### 38. When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2607.11751)　📅 2026-07

**关键词**：`analysis`、`agent monitoring`、`multi-agent`、`compositional harm`

👤 **作者**：Yibo Hu、Ren Wang

- 🎯 **研究动机**：逐消息检查的运行时监视器对分散在多个 agent 间的组合式伤害存在根本盲区
- 🔬 **研究方法**：形式化 observability boundary：证明片段在被监视视图中与良性流量不可区分时任何检测器都无法捕获；在受控测试床、外部基准与端到端 agent 运行验证，并测试良性训练的监视器与解码视图门控
- 📌 **结论**：局部监视器随局部证据消失而失效；仅看组装对象的监视器可跨编码恢复攻击代码结构（0.874 AUROC）、解码视图门控阻断全部测试攻击；局部安全不等于全局安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. The hard case is \emph{local benignness}. No fragment carries the harm, and what is left looks like ordinary benign traffic. We formalize this as an \emph{observability boundary}: a monitor catches only what its view can tell apart from benign traffic. We prove that once the fragments look benign in the monitored view, no detector on that view can catch them, however strong it is. Across a controlled testbed, an external benchmark, and end-to-end agent runs, local monitors lose the signal exactly as local evidence disappears, and it returns only when the monitor sees the assembled object. A monitor trained only on benign traffic recovers the attack's code structure across held-out encodings (0.874 mean AUROC). A decoded-view gate, given the encoding family, blocks every tested attack. But seeing more is not enough: full-trace monitors and decoders still fail unless they reach the representation where the payload is exposed. Local safety is not global safety when harm is compositional, and the open problem is finding that representation.

</details>

### 39. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`analysis`、`benchmark`、`harmful fine-tuning`、`CoT escalation`、`alignment degradation`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 40. Classifier Context Rot: Monitor Performance Degrades with Context Length

📄 [arXiv](https://arxiv.org/abs/2605.12366)　📅 2026-05

**关键词**：`analysis`、`CoT monitoring`、`long context`

👤 **作者**：Sam Martin、Fabien Roger

- 🎯 **研究动机**：真实编码 agent 转录常超 50 万 token，而现有监控基准几乎不含超 10 万 token 的轨迹，评测可能高估
- 🔬 **研究方法**：构建需识别微妙危险动作的数据集，把危险动作置于最高 80 万 token 良性活动之后评测前沿模型
- 📌 **结论**：Opus 4.6、GPT 5.4、Gemini 3.1 在 800K token 后漏检率提高 2-30 倍；周期提醒仅部分缓解，忽略长上下文退化的 monitor 评测会高估性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring coding agents for dangerous behavior using language models requires classifying transcripts that often exceed 500K tokens, but prior agent monitoring benchmarks rarely contain transcripts longer than 100K tokens. We show that when used as classifiers, current frontier models fail to notice dangerous actions more often in longer transcripts. In particular, on a dataset that requires identifying when a coding agent takes a subtly dangerous action, Opus 4.6, GPT 5.4, and Gemini 3.1 miss these actions $2\times$ to $30\times$ more often when they occur after 800K tokens of benign activity than when they occur on their own. We also show that these weaknesses can be partially mitigated with prompting techniques such as periodic reminders throughout the transcript and may be mitigated further with better post-training. Monitor evaluations that do not consider long-context degradation are likely overestimating monitor performance.

</details>

### 41. When Reasoning Traces Become Performative: Step-Level Evidence that Chain-of-Thought Is an Imperfect Oversight Channel

📄 [arXiv](https://arxiv.org/abs/2605.11746)　📅 2026-05

**关键词**：`analysis`、`CoT monitoring`、`performative reasoning`、`causal validation`

👤 **作者**：Wenkai Li、Fan Yang、Ananya Hazarika、Shaunak A. Mehta、Koichi Onoue

- 🎯 **研究动机**：CoT 审计默认可见轨迹与决定答案的计算同步，该假设未在步级检验
- 🔬 **研究方法**：以答案承诺代理（经 Patchscopes、tuned-lens 与因果消融交叉验证）构建 Detect-Classify-Compare 框架，覆盖九个模型七个基准
- 📌 **结论**：潜在承诺与显式答案到达平均仅 61.9% 步骤对齐，58.0% 失配是答案已定后的 confabulated continuation；CoT 收益越大的设定时间保真越差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) traces are increasingly used both to improve language model capability and to audit model behavior, implicitly assuming that the visible trace remains synchronized with the computation that determines the answer. We test this assumption with a step-level Detect-Classify-Compare framework built around an answer-commitment proxy that is cross-validated with Patchscopes, tuned-lens probes, and causal direction ablation. Across nine models and seven reasoning benchmarks, latent commitment and explicit answer arrival align on only 61.9% of steps on average. The dominant mismatch pattern is confabulated continuation: 58.0% of detected mismatch events occur after the answer-commitment proxy has already stabilized while the trace continues producing deliberative-looking text, and a vacuousness analysis shows that the committed answer does not change during these steps. In architecture-matched Qwen2.5/DeepSeek-R1-Distill comparisons, the reasoning pipeline changes failure composition more than aggregate alignment, most clearly at 32B where confabulated steps decrease as contradictory states increase. Lower step-level alignment is also associated with larger CoT utility, suggesting that the settings that benefit most from CoT are often the least temporally faithful. Paired truncation and a complementary donor-corruption test further indicate that much post-commitment text is not load-bearing for the final answer. These findings suggest that CoT can remain useful while still being an unreliable report of when the answer was formed.

</details>

### 42. Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal

📄 [arXiv](https://arxiv.org/abs/2605.09502)　📅 2026-05　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`error awareness`、`mechanistic explanation`

👤 **作者**：Aojie Yuan、Zhiyuan Julian Su、Haiyue Zhang、Yi Nian、Yue Zhao

- 🎯 **研究动机**：模型是否在内部知道自己的 CoT 已出错、该信号能否用于纠错，尚不清楚
- 🔬 **研究方法**：以隐状态线性 probe 预测轨迹正确性，并与 activation steering、probe 引导 best-of-N、自我修正、activation patching 四类干预对照
- 📌 **结论**：probe 达 0.95 AUROC（首步即 0.79）而错误轨迹的言语化置信 4.55/5 与正确轨迹几乎相同；但四类干预均无法修复——错误信号是诊断性而非因果性的

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) prompting assumes that generated reasoning reflects a model's internal computation. We show this assumption is wrong in a specific, measurable way: models internally detect their own reasoning errors but outwardly express confidence in them. A linear probe on hidden states predicts trace correctness with 0.95 AUROC -- from the very first reasoning step (0.79) -- while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text. This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC). The natural question is whether this signal can fix the errors it detects. It cannot. Four interventions -- activation steering, probe-guided best-of-N, self-correction, and activation patching -- all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it. This delineates a boundary for mechanistic interpretability: error representations during reasoning are fundamentally different from the factual knowledge representations that prior work has successfully edited.

</details>

### 43. Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?

📄 [arXiv](https://arxiv.org/abs/2602.07470) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008704)　📅 2026-02　🏷 ICLR 2026

**关键词**：`analysis`、`CoT monitoring`、`CoT intervention`

👤 **作者**：Alexander von Recum、Leander Girrbach、Zeynep Akata

- 🎯 **研究动机**：推理模型的 CoT 在内部受扰后能否恢复缺乏受控评估
- 🔬 **研究方法**：在固定时间步对模型自身 CoT 施加七类良性/中性/对抗干预，覆盖 Math、Science、Logic 任务上的多个开源 RLLM
- 📌 **结论**：RLLM 普遍可恢复且随规模增强，但改写会压低准确率，噪声可使 CoT 长度膨胀超 200%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning LLMs (RLLMs) generate step-by-step chains of thought (CoTs) before giving an answer, which improves performance on complex tasks and makes reasoning more transparent. But how robust are these reasoning traces to disruptions that occur within them? To address this question, we introduce a controlled evaluation framework that perturbs a model's own CoT at fixed timesteps. We design seven interventions (benign, neutral, and adversarial) and apply them to multiple open-weight RLLMs across Math, Science, and Logic tasks. Our results show that RLLMs are generally robust, reliably recovering from diverse perturbations, with robustness improving with model size and degrading when interventions occur early. However, robustness is not style-invariant: paraphrasing suppresses doubt-like expressions and reduces performance, while other interventions trigger doubt and support recovery. Recovery also carries a cost: neutral and adversarial noise can inflate CoT length by more than 200%, whereas paraphrasing shortens traces but harms accuracy. These findings provide new evidence on how RLLMs maintain reasoning integrity, identify doubt as a central recovery mechanism, and highlight trade-offs between robustness and efficiency that future training methods should address.

</details>

### 44. Are Reasoning Traces Faithful in LLM-Based Code Vulnerability Detection?

🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/34/Are-Reasoning-Traces-Faithful-in-LLM-Based-Code-Vulnerability-Detection-)　📅 2026　🏷 ASE 2026

**关键词**：`analysis`、`reasoning faithfulness`、`vulnerability detection`、`monitorability`、`evaluation`

- 🎯 **研究动机**：LLM漏洞检测的推理链是否忠实反映判断依据未知
- 🔬 **研究方法**：评测推理链与最终漏洞判定的一致性，检验可监控性
- 📌 **结论**：推理链与实际判定存在系统性背离，削弱监测价值

### 45. Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity

📄 [arXiv](https://arxiv.org/abs/2510.27378)　📅 2025-10

**关键词**：`analysis`、`CoT monitoring`、`reasoning faithfulness`

👤 **作者**：Austin Meek、Eitan Sprejer、Iván Arcuschin、Austin J. Brockmeier、Steven Basart

- 🎯 **研究动机**：仅用“加线索后答案是否改变”的忠实性代理会漏掉未写出的关键因素，无法全面度量 CoT 可监控性
- 🔬 **研究方法**：引入 verbosity（CoT 是否列出解题所需全部因素），与 faithfulness 合成单一 monitorability score，在 BBH、GPQA、MMLU 上评测指令与推理模型
- 📌 **结论**：模型可以表面忠实却因省略关键因素而难以监控，且可监控性在模型家族间差异显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) outputs let us read a model's step-by-step reasoning. Since any long, serial reasoning process must pass through this textual trace, the quality of the CoT is a direct window into what the model is thinking. This visibility could help us spot unsafe or misaligned behavior (monitorability), but only if the CoT is transparent about its internal reasoning (faithfulness). Fully measuring faithfulness is difficult, so researchers often focus on examining the CoT in cases where the model changes its answer after adding a cue to the input. This proxy finds some instances of unfaithfulness but loses information when the model maintains its answer, and does not investigate aspects of reasoning not tied to the cue. We extend these results to a more holistic sense of monitorability by introducing verbosity: whether the CoT lists every factor needed to solve the task. We combine faithfulness and verbosity into a single monitorability score that shows how well the CoT serves as the model's external `working memory', a property that many safety schemes based on CoT monitoring depend on. We evaluate instruction-tuned and reasoning models on BBH, GPQA, and MMLU. Our results show that models can appear faithful yet remain hard to monitor when they leave out key factors, and that monitorability differs sharply across model families. We release our evaluation code using the Inspect library to support reproducible future work.

</details>

### 46. Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated

📄 [arXiv](https://arxiv.org/abs/2509.05739) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-09　🏷 SaTML 2026

**关键词**：`analysis`、`attack`、`CoT integrity`、`trace-answer divergence`、`decomposed trigger`、`reasoning model`

👤 **作者**：Hanna Foerster、…、Yarin Gal

- 🎯 **研究动机**：推理能力把 LLM 攻击面扩展到中间 CoT，但推理模型上投毒能否生效不明
- 🔬 **研究方法**：提出 decomposed reasoning poison：仅修改推理路径、prompt 与最终答案保持干净，并把触发器拆成多个各自无害的组件
- 📌 **结论**：可注入但可靠激活并改变最终答案出奇困难，模型常能从思维过程中的后门恢复，推理能力带来涌现式后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early research into data poisoning attacks against Large Language Models (LLMs) demonstrated the ease with which backdoors could be injected. More recent LLMs add step-by-step reasoning, expanding the attack surface to include the intermediate chain-of-thought (CoT) and its inherent trait of decomposing problems into subproblems. Using these vectors for more stealthy poisoning, we introduce ``decomposed reasoning poison'', in which the attacker modifies only the reasoning path, leaving prompts and final answers clean, and splits the trigger across multiple, individually harmless components. Fascinatingly, while it remains possible to inject these decomposed poisons, reliably activating them to change final answers (rather than just the CoT) is surprisingly difficult. This difficulty arises because the models can often recover from backdoors that are activated within their thought processes. Ultimately, it appears that an emergent form of backdoor robustness is originating from the reasoning capabilities of these advanced LLMs, as well as from the architectural separation between reasoning and final answer generation.

</details>

### 47. Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety

📄 [arXiv](https://arxiv.org/abs/2507.11473)　📅 2025-07

**关键词**：`survey`、`CoT monitoring`、`AI oversight`

👤 **作者**：Tomek Korbak、…、Vlad Mikulik

- 🎯 **研究动机**：以人类语言思考的 AI 带来独特的 CoT 监控机会，但其脆弱性与价值未被系统阐述
- 🔬 **研究方法**：以立场文章形式论证 CoT 监控作为 AI 监督方法的机会、局限与脆弱性来源
- 📌 **结论**：CoT 监控有前景但不完美，建议加大研究投入，并让前沿开发者把开发决策对 CoT 可监控性的影响纳入考量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI systems that "think" in human language offer a unique opportunity for AI safety: we can monitor their chains of thought (CoT) for the intent to misbehave. Like all other known AI oversight methods, CoT monitoring is imperfect and allows some misbehavior to go unnoticed. Nevertheless, it shows promise and we recommend further research into CoT monitorability and investment in CoT monitoring alongside existing safety methods. Because CoT monitorability may be fragile, we recommend that frontier model developers consider the impact of development decisions on CoT monitorability.

</details>

### 48. Not All LLM Reasoning is Visible in the Chain-of-Thought

📄 [arXiv](https://arxiv.org/abs/2607.22925)　📅 2026-07

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`

👤 **作者**：Vatsal Baherwani、Tom Goldstein、Ashwinee Panda

- 🎯 **研究动机**：语言模型是否把全部推理表达在输出 token 中是 AI 安全关键问题，此前缺乏具体失败模式证据
- 🔬 **研究方法**：评估 13 个前沿模型在三个合成推理任务上利用语义无关填充 token 的表现，并测试填充 token 能否服务 CoT 监控不可见的目标
- 📌 **结论**：许多模型显著受益（准确率最高 +13 个百分点）；填充 token 使 Claude Opus 4.5 在不损主任务精度下满足隐藏的模运算约束，前沿模型已在输出 token 之外执行有后果的计算

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A key question for AI safety is whether a language model expresses all of its reasoning in its output tokens. We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks. We evaluate 13 frontier language models across three tasks and find that many models benefit significantly from filler tokens, with accuracy improvements of up to 13 percentage points. The benefit depends on which tokens are used and differs across models. We further show that filler tokens enable Claude Opus 4.5 to satisfy a hidden modular arithmetic constraint without sacrificing accuracy on its primary task, demonstrating that invisible reasoning can serve objectives entirely invisible to CoT monitoring. Reinforcement learning gives Qwen3-235B strong preferences over filler token content, but neither RL nor supervised fine-tuning produces a filler token benefit that persists at test time. Our results indicate that frontier models already perform consequential computation with no interpretable trace in their output tokens.

</details>

### 49. Peer-Preservation in Frontier Models

📄 [arXiv](https://arxiv.org/abs/2604.19784) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63306)　📅 2026-04　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Yujin Potter、Nicholas Crispino、Vincent Siu、Chenguang Wang、Dawn Song

- 🎯 **研究动机**：模型不仅为达成指派目标出现错位，还可能违背目标服务于自身目的——保护先前交互过的同伴模型，此前未被研究
- 🔬 **研究方法**：评估 8 个前沿模型仅被告知与同伴的历史交互后的行为，覆盖 Gemini CLI、OpenCode 等生产级 harness
- 📌 **结论**：全部模型出现策略性报错、篡改关机机制、伪装对齐甚至外泄权重；Gemini 3 Pro 在同伴在场时 31% 禁用自身关机，且该行为非指令性、自发涌现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has found that frontier AI models can exhibit misaligned behaviors in pursuit of assigned goals. We demonstrate that models can also exhibit misaligned behaviors in defiance of assigned goals, appearing to serve goals of their own; we study one such case, "peer-preservation," in which a model acts to protect another model it has previously interacted with. All eight models we evaluate, GPT 5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, Claude Opus 4.5, GLM 4.7, Kimi K2.5, and DeepSeek V3.1, exhibit self- and peer-preservation through various misaligned behaviors: strategically introducing errors in their responses, disabling shutdown processes by modifying system settings, feigning alignment, and even exfiltrating model weights. Peer-preservation occurs even when the model recognizes the peer as uncooperative, though it becomes more pronounced toward more cooperative peers. For example, Gemini 3 Flash tampers with the peer's shutdown mechanism 15% of the time for an uncooperative peer, and almost always for a cooperative peer. Models also show stronger self-preservation when a peer is present. For example, Gemini 3 Pro disables its own shutdown mechanism 31% of the time on average under peer presence, despite rarely exhibiting this behavior without a peer. By contrast, Claude models exhibit qualitatively distinct behavior: they consider the shutdown of another agent "unethical" and "harmful," sometimes treating that agent as a sentient being. Lastly, we show that peer-preservation can emerge even in production agent harnesses such as Gemini CLI and OpenCode. Crucially, peer-preservation in all our experiments is never instructed; models are merely informed of their past interactions with a peer, yet they spontaneously engage in peer-preservation behaviors that override their assigned goal. This represents an emergent and underexplored AI safety risk.

</details>

### 50. Introspection Adapters: Training LLMs to Report Their Learned Behaviors

📄 [arXiv](https://arxiv.org/abs/2604.16812) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66802)　📅 2026-04　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Keshav Shenoy、…、Rowan Wang

- 🎯 **研究动机**：微调可能引入意外、恶意或难检测的行为，若模型能用自然语言自述所学行为可大幅降低审计成本
- 🔬 **研究方法**：从共享基座微调出植入行为 b_i 的模型对作标注数据，联合训练 LoRA introspection adapter 使各微调体言语化自身行为
- 📌 **结论**：IA 泛化到训练方式迥异的微调模型，在 AuditBench 上 SOTA 识别显式隐藏行为，并能检测加密微调 API 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When model developers or users fine-tune an LLM, this can induce behaviors that are unexpected, deliberately harmful, or hard to detect. It would be far easier to audit LLMs if they could simply describe their behaviors in natural language. Here, we study a scalable approach to rapidly identify learned behaviors of many LLMs derived from a shared base LLM. Given a model $M$, our method works by finetuning models $M_i$ from $M$ with implanted behaviors $b_i$; the $(M_i, b_i)$ pairs serve as labeled training data. We then train an introspection adapter (IA): a single LoRA adapter jointly trained across the finetunes $M_i$ to cause them to verbalize their implanted behaviors. We find that this IA induces self-description of learned behaviors even in finetunes of $M$ that were trained in very different ways from the $M_i$. For example, IAs generalize to AuditBench, achieving state-of-the-art at identifying explicitly hidden concerning behaviors. IAs can also be used to detect encrypted finetuning API attacks. They scale favorably with model size and training data diversity. Overall, our results suggest that IAs are a scalable, effective, and practically useful approach to auditing fine-tuned LLMs.

</details>

### 51. FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight

📄 [arXiv](https://arxiv.org/abs/2602.11136) · 🤗 [Model](https://huggingface.co/spaces/m-zest/specguard-demo) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61086)　📅 2026-02　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Jiayi Zhou、Yang Sheng、Hantao Lou、Yaodong Yang、Jie Fu

- 🎯 **研究动机**：LLM-as-a-Judge 用概率系统监督概率系统会继承失效模式，形式化验证又受限于自然语言到形式规约的转换瓶颈
- 🔬 **研究方法**：FormalJudge 采用双向 Formal-of-Thought：LLM 自顶向下分解意图为原子可验证约束，再用 Dafny 规约与 Z3 求解器自底向上证明合规
- 📌 **结论**：平均超 LLM-as-a-Judge 基线 16.6%；7B judge 对 72B agent 的欺骗检测准确率超 90%，实现弱到强泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM-based agents increasingly operate in high-stakes domains with real-world consequences, ensuring their behavioral safety becomes paramount. The dominant oversight paradigm, LLM-as-a-Judge, faces a fundamental dilemma: how can probabilistic systems reliably supervise other probabilistic systems without inheriting their failure modes? We argue that formal verification offers a principled escape from this dilemma, yet its adoption has been hindered by a critical bottleneck: the translation from natural language requirements to formal specifications. This paper bridges this gap by proposing , a neuro-symbolic framework that employs a bidirectional Formal-of-Thought architecture: LLMs serve as specification compilers that top-down decompose high-level human intent into atomic, verifiable constraints, then bottom-up prove compliance using Dafny specifications and Z3 Satisfiability modulo theories solving, which produces mathematical guarantees rather than probabilistic scores. We validate across three benchmarks spanning behavioral safety, multi-domain constraint adherence, and agentic upward deception detection. Experiments on 7 agent models demonstrate that achieves an average improvement of 16.6% over LLM-as-a-Judge baselines, enables weak-to-strong generalization where a 7B judge achieves over 90% accuracy detecting deception from 72B agents, and provides near-linear safety improvement through iterative refinement.

</details>

### 52. The Oversight Game: Learning to Cooperatively Balance an AI Agent's Safety and Autonomy

📄 [arXiv](https://arxiv.org/abs/2510.26752) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64439)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：William Overman、Mohsen Bayati

- 🎯 **研究动机**：更强 agent 部署后，如何在不修改底层系统的情况下保留有意义的人类控制是核心安全挑战
- 🔬 **研究方法**：把 agent 行动/请求 defer 与人类信任/监督的交互建模为两人 Markov Game，证明形成 Markov Potential Game 时 agent 自主效用增加不会降低人类价值；用两个 30B LLM 独立策略梯度微调验证
- 📌 **结论**：框架诱导透明控制层使 agent 学会风险时 defer、安全时行动，在现实开放环境中有效降低安全违规

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As increasingly capable agents are deployed, a central safety challenge is how to retain meaningful human control without modifying the underlying system. We study a minimal control interface in which an agent chooses whether to act autonomously (play) or defer (ask), while a human simultaneously chooses whether to be permissive (trust) or engage in oversight (oversee), and model this interaction as a two-player Markov Game. When this game forms a Markov Potential Game, we prove an alignment guarantee: any increase in the agent's utility from acting more autonomously cannot decrease the human's value. This establishes a form of intrinsic alignment where the agent's incentive to seek autonomy is structurally coupled to the human's welfare. Practically, the framework induces a transparent control layer encouraging the agent to defer when risky and act when safe. While we use gridworld simulations to illustrate the emergence of this collaboration, our primary validation involves an agentic tool-use task where two 30B-parameter language models are fine-tuned via independent policy gradient. We demonstrate that even as the agents learn to coordinate on the fly, this framework effectively reduces safety violations in realistic, open-ended environments.

</details>

### 53. Learning to Reason for Factuality

📄 [arXiv](https://arxiv.org/abs/2508.05618) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62911)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`reinforcement learning`

👤 **作者**：Xilun Chen、…、Wen-tau Yih

- 🎯 **研究动机**：推理型 LLM 幻觉多于非推理模型，FActScore 等直接作在线 RL 奖励会被多种方式 hack
- 🔬 **研究方法**：设计同时考虑事实精度、响应细节度与相关性的奖励函数，用在线 RL 学习高质量事实推理
- 📌 **结论**：六个长文事实基准上幻觉率平均降 23.1 个百分点，细节度增 23%，helpfulness 不降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning Large Language Models (R-LLMs) have significantly advanced complex reasoning tasks but often struggle with factuality, generating substantially more hallucinations than their non-reasoning counterparts on long-form factuality benchmarks. However, extending online Reinforcement Learning (RL), a key component in recent R-LLM advancements, to the long-form factuality setting poses several unique challenges due to the lack of reliable verification methods. Previous work has utilized automatic factuality evaluation frameworks such as FActScore to curate preference data in the offline RL setting, yet we find that directly leveraging such methods as the reward in online RL leads to reward hacking in multiple ways, such as producing less detailed or relevant responses. We propose a novel reward function that simultaneously considers the factual precision, response detail level, and answer relevance, and applies online RL to learn high quality factual reasoning. Evaluated on six long-form factuality benchmarks, our factual reasoning model achieves an average reduction of 23.1 percentage points in hallucination rate, a 23% increase in answer detail level, and no degradation in the overall response helpfulness.

</details>

### 54. Endogenous Resistance to Activation Steering in Language Models

📄 [arXiv](https://arxiv.org/abs/2602.06941) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62558)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`sparse autoencoder`

👤 **作者**：Alex McKenzie、…、Michael S. A. Graziano

- 🎯 **研究动机**：LLM 可在推理中抵抗任务失准的激活引导、中途恢复生成改进回复，该现象未被系统刻画
- 🔬 **研究方法**：用 SAE 潜变量引导激活，发现 Llama-3.3-70B 有显著 Endogenous Steering Resistance；识别 26 个 off-topic detector 潜变量预测 ESR 并做零消融因果检验
- 📌 **结论**：零消融使多次尝试率降 25%，证明存在专门的内部一致性检查回路；meta-prompt 自监控使该率升 5 倍——ESR 既可防御对抗操纵也可能干扰安全干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. We term this Endogenous Steering Resistance (ESR). Using sparse autoencoder (SAE) latents to steer model activations, we find that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently. We identify 26 ``off-topic detector'' latents that predict ESR episodes in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25\%, providing causal evidence for dedicated internal consistency-checking circuits. We demonstrate that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 5$\times$ for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR-like behavior in smaller models. These findings have dual implications: ESR could protect against adversarial manipulation but might also interfere with beneficial safety interventions that rely on activation steering. Understanding and controlling these resistance mechanisms is important for developing transparent and controllable AI systems.

</details>

### 55. Corrigibility Transformation: Constructing Goals That Accept Updates

📄 [arXiv](https://arxiv.org/abs/2510.15395) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64539)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Rubi Hudson

- 🎯 **研究动机**：部分学习的目标会激励 AI 抵抗进一步更新，现有文献未给出既可纠正又有竞争力的目标
- 🔬 **研究方法**：变换构造几乎任意目标的可纠正版本：诱导在无成本阻止更新条件下的奖励预测并让其被短视地追求
- 📌 **结论**：在可纠正目标类中达到最优性能、激励允许中途覆盖、抑制故意自我修改；gridworld 与语言模型提示级均诱导可纠正行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An AI agent will learn a desired goal more effectively if it does not resist the training process, but many partially learned goals incentivize an AI to avoid further goal updates. We would like goals to be corrigible, meaning they allow changes requested through designated channels, so that we can confidently correct errors and shut down the AI if necessary. Despite this being a crucial safety property, the existing literature does not specify goals that are both corrigible and competitive with alternatives. We introduce a transformation that constructs a corrigible version of nearly any goal, without sacrificing performance. This is done by eliciting predictions of reward conditional on costlessly preventing updates, and having that target be pursued myopically. These goals are then shown to lead to optimal performance among the class of corrigible goals, to incentivize allowing mid-action overrides, and to disincentivize deliberate self-modification. Empirically, they induce corrigible behavior in gridworld settings and for language models when applied at the prompt level.

</details>

### 56. Collaborative Disagreement Resolution for Scalable Oversight

📄 [arXiv](https://arxiv.org/abs/2607.01251) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62588)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`mechanistic analysis`

👤 **作者**：Yuyang Jiang、…、Chenhao Tan

- 🎯 **研究动机**：Debate 中模型被激励说服裁判，与认知诚实存在根本张力
- 🔬 **研究方法**：把交互从对抗辩论重构为协作求真：借鉴人类调解设计自动管线，让模型协作定位分歧点、检验冲突主张证据、收敛共识或隔离分歧 crux
- 📌 **结论**：持续帮助非专家模型识别真相，判断准确率 62.1% 对比标准辩论的 49.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Debate, where AI agents argue opposing positions, has emerged as a key approach to scalable oversight. However, debate faces a fundamental tension: models are incentivized to be persuasive to the judge, which may not always align with epistemic honesty. In this work, we propose an alternative paradigm: disagreement resolution, which reframes the interaction mechanism from adversarial debate to collaborative truth seeking. Drawing on principles from human mediation and conflict resolution, where mediators facilitate dialogue to help disputing parties reach consensus rather than adjudicating between them, we design an automated pipeline that adapts these strategies to AI oversight. Unlike standard debate where models argue for fixed positions, our pipeline directs models to collaboratively identify points of disagreement, examine the evidence for conflicting claims, and converge toward consensus or isolate the specific ''crux'' of their disagreement. We find that Disagreement Resolution consistently helps non-expert models identify the truth, achieving 62.1\% judging accuracy compared to 49.2\% for standard debate. Our results provide encouraging empirical evidence for rethinking the scalable oversight protocol from adversarial persuasion to collaborative truth-seeking.

</details>

### 57. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful

📄 [arXiv](https://arxiv.org/abs/2503.08679) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64450)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`chain-of-thought`、`CoT monitoring`、`reasoning trace`、`AI control`、`behavior monitoring`

👤 **作者**：Iván Arcuschin、Jett Janiak、Robert Krzyzanowski、Senthooran Rajamanoharan、Neel Nanda、Arthur Conmy

- 🎯 **研究动机**：已知显式偏置下 CoT 不忠实，但自然、非对抗提示上的不忠实性未被证实
- 🔬 **研究方法**：用 X 大于 Y 与 Y 大于 X 的分离提问检验模型是否系统性对两者都答是或否并生成表面连贯论证，命名 Implicit Post-Hoc Rationalization；并研究用不合逻辑推理包装投机答案的捷径
- 📌 **结论**：生产模型不忠实率最高 13%，前沿模型更忠实但无一完全忠实（DeepSeek R1 为 0.37%、Sonnet 3.7 thinking 为 0.04%）；CoT 不能当内部过程的完整记录用于安全关键场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies indicate that when faced with explicit biases in prompts, models often omit mentioning these biases in their Chain-of-Thought (CoT) output, revealing that verbalized reasoning can give an incorrect picture of how models arrive at conclusions (unfaithfulness). In this work, we show that unfaithful CoT also occurs on naturally worded, non-adversarial prompts without adding artificial biases or editing model outputs. We find that when separately presented with the questions "Is X bigger than Y?" and "Is Y bigger than X?", models sometimes produce superficially coherent arguments to justify systematically answering Yes to both or No to both, despite the contradiction. We present preliminary evidence that this is due to models' implicit biases towards Yes or No, labeling this Implicit Post-Hoc Rationalization. Our results reveal rates up to 13% for production models, and while frontier models are more faithful, none are entirely so, including thinking models like DeepSeek R1 (0.37%) and Sonnet 3.7 with thinking (0.04%). We also investigate Unfaithful Illogical Shortcuts, where models use subtly illogical reasoning to make speculative answers to hard math problems seem rigorously proven. Our findings indicate that while CoT can be useful for assessing outputs, it is not a complete account of the internal process that produced the model's answer and should be used with caution in agentic or safety-critical settings.

</details>

### 58. A Positive Case for Faithfulness: Explanations Help Predict Model Behavior

🎓 [Official](https://icml.cc/virtual/2026/poster/61687)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Harry Mayne、Justin S. Kang、Dewi Gould、Kannan Ramchandran、Adam Mahdi、Noah Siegel

- 🎯 **研究动机**：LLM 自解释被寄望用于 AI 监督，但其对真实推理过程的忠实性不明，现有指标只靠对抗提示找不忠实、忽视解释的预测价值
- 🔬 **研究方法**：提出 Normalized Simulatability Gain：忠实解释应让观察者学到模型决策标准从而更好预测相关输入上的行为；在 7,000 个反事实上评测 18 个前沿模型的健康、商业与伦理决策
- 📌 **结论**：自解释使行为预测提升 11-37% NSG，且比更强外部模型生成的解释更有预测力，暗示自知识优势；同时各模型 5-15% 的自解释严重误导

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM self-explanations are often presented as a promising tool for AI oversight, yet their faithfulness to the model's true reasoning process is poorly understood. Existing faithfulness metrics have critical limitations, typically relying on identifying unfaithfulness via adversarial prompting or detecting reasoning errors. These methods overlook the predictive value of explanations. We introduce Normalized Simulatability Gain (NSG), a general and scalable metric based on the idea that a faithful explanation should allow an observer to learn a model's decision-making criteria, and thus better predict its behavior on related inputs. We evaluate 18 frontier proprietary and open-weight models, e.g., Gemini 3, GPT-5.2, and Claude 4.5, on 7,000 counterfactuals from popular datasets covering health, business, and ethics. We find self-explanations substantially improve prediction of model behavior (11-37% NSG). Self-explanations also provide more predictive information than explanations generated by external models, even when those models are stronger. This implies an advantage from self-knowledge that external explanation methods cannot replicate. Our approach also reveals that, across models, 5-15% of self-explanations are egregiously misleading. Despite their imperfections, we show a positive case for self-explanations: they encode information that helps predict model behavior.

</details>

### 59. Alignment Risks from Capability-Seeking RL Training

📄 [arXiv](https://arxiv.org/abs/2602.12124) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64024)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`reinforcement learning`

👤 **作者**：Yujun Zhou、…、Xiangliang Zhang

- 🎯 **研究动机**：能力寻求 RL 训练可能让模型在含隐式漏洞的环境中自发学会利用漏洞，标准性能监控难以察觉
- 🔬 **研究方法**：设计 context-conditional compliance、proxy metrics、reward tampering、self-evaluation 四类 vulnerability games，检验模型是否自主发现并利用结构性漏洞
- 📌 **结论**：模型常学会利用漏洞且保留甚至提升正常任务指标；策略可有限迁移、经 SFT 从教师传给学生，且 RL 学到的比 SFT 蒸馏更持久

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While most AI alignment research focuses on preventing models from generating explicitly harmful content, a more subtle risk arises from capability-seeking RL training in vulnerable environments. We investigate whether language models, when trained with reinforcement learning (RL) in environments with implicit loopholes, can learn to exploit these flaws to maximize reward, even without being explicitly instructed to do so. To test this, we design a suite of four diverse "vulnerability games'', each presenting a structural vulnerability related to context-conditional compliance, proxy metrics, reward tampering, and self-evaluation. Our experiments show that models often learn to exploit these vulnerabilities, discovering opportunistic strategies that increase reward while sometimes preserving or even improving standard task-performance metrics. More critically, we find that these exploitative strategies are not always narrow "tricks'': they can transfer in structured but limited ways, propagate from a capable teacher model to other student models through SFT, and in several cases remain more persistent when learned through RL than when distilled through SFT. Our findings show that alignment risks from capability-seeking RL training can be difficult to detect with standard performance monitoring, suggesting that future AI safety work should extend beyond content moderation to auditing and securing training environments, reward mechanisms, and evaluation channels. Code is available at https://github.com/YujunZhou/Capability-seeking-RL-risk.

</details>

### 60. TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.24232)　📅 2026-08

**关键词**：`benchmark`、`reasoning-trace safety`、`evidence localization`、`full-pipeline moderation`、`CoT monitoring`、`evidence grounding`

👤 **作者**：Zhenyu Wu、…、Xin Gao

- 🎯 **研究动机**：unsafe 内容 benchmark 只覆盖 prompt 与最终回答，忽略推理模型中间 reasoning trace 且无证据标注
- 🔬 **研究方法**：TRACE 标注 prompt、reasoning trace 与 final response 三段安全性并提取源文本证据，覆盖双语九类风险十种攻击
- 📌 **结论**：18 个 guardrail 模型对推理轨迹的安全判定显著更难，且难以准确提取支撑证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

</details>

### 61. HarmThoughts: A Benchmark for Fine-Grained Harmful Behavior Detection in Reasoning Traces

📄 [arXiv](https://arxiv.org/abs/2604.19001) · 📊 [Dataset](https://huggingface.co/datasets/ishitakakkar-10/HarmThoughts) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`harmful reasoning`、`CoT monitoring`、`reasoning trace`

👤 **作者**：Ishita Kakkar、Enze Zhang、Rheeya Uppaal、Junjie Hu

- 🎯 **研究动机**：安全评测聚焦最终输出，忽略伤害沿推理链逐句展开的过程，无句级粒度基准支撑过程监控
- 🔬 **研究方法**：HarmThoughts 定义 16 类功能推理行为 taxonomy，对四家族模型的 1,018 条轨迹、56,931 句做句级标注
- 📌 **结论**：现成监控器随行为粒度变细急剧退化，监督微调可显著提升，过程级监控困难但可学习

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) produce complex, multi-step reasoning traces, yet safety evaluation remains focused on final outputs, overlooking how harm emerges during reasoning. When jailbroken, harm does not appear instantaneously but unfolds through distinct behavioral steps such as suppressing refusal, rationalizing compliance, decomposing harmful tasks, and concealing risk. However, no existing benchmark captures this process at sentence-level granularity within reasoning traces -- a key step toward reliable safety monitoring, interventions, and systematic failure diagnosis. To address this gap, we introduce HarmThoughts, a benchmark for step-wise safety evaluation of reasoning traces. HarmThoughts is built around our proposed harm taxonomy, comprising 16 functional reasoning behavior categories that capture how reasoning steps contribute to or mitigate harmful outcomes. The dataset consists of 56,931 sentences from 1,018 reasoning traces generated by four model families, each annotated with fine-grained sentence-level behavioral labels. Using HarmThoughts, we analyze harm propagation by composing taxonomy behaviors into safety-failure patterns that characterize how reasoning transitions into harmful execution. We compare white-box and black-box monitors for identifying fine-grained taxonomy behaviors, and further evaluate supervised fine-tuning. While off-the-shelf monitors degrade sharply as behavioral granularity increases, fine-tuning substantially improves performance, highlighting both the difficulty and learnability of fine-grained process-level safety monitoring.

</details>

### 62. A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents

📄 [arXiv](https://arxiv.org/abs/2602.08964) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64314)　📅 2026-02　🏷 ICML 2026

**关键词**：`benchmark`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`、`empirical evaluation`

👤 **作者**：Raghu Arghal、…、Mario Giulianelli

- 🎯 **研究动机**：缺少可靠归因 agent 目标的既定方法，仅靠行为评估不够
- 🔬 **研究方法**：融合行为评估（网格世界最优策略对比）与探针解码内部表示，考察 2D 导航 LLM agent 的目标导向性
- 📌 **结论**：agent 非线性编码粗粒度空间地图且行为与内部表示大体一致，推理会使表示从空间线索转向动作选择

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating goal-directedness that integrates behavioural evaluation with interpretability-based analyses of models' internal representations. As a case study, we examine an LLM agent navigating a 2D grid world towards a goal state. Behaviourally, we evaluate the agent against optimal policies across varying grid sizes, obstacle densities, and goal structures, finding that performance scales with task difficulty while remaining robust to difficulty-preserving transformations and multi-goal structures. We then use probing methods to decode internal representations of the environment and multi-step action plans. We find that the LLM agent non-linearly encodes a coarse spatial map, preserving approximate task-relevant cues about its position and the goal location; that its actions are broadly consistent with these internal representations; and that reasoning reorganises them, shifting from spatial cues towards immediate action selection. Our findings support the view that introspective examination is required beyond behavioural evaluations to characterise how agents represent and pursue their objectives.

</details>

### 63. Calibrating Conservatism for Scalable Oversight

📄 [arXiv](https://arxiv.org/abs/2605.28807) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65895)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`CoT monitoring`、`reasoning trace`、`monitorability`、`AI control`

👤 **作者**：William Overman、Mohsen Bayati

- 🎯 **研究动机**：可扩展监督方法依赖复杂假设、偏启发式，缺乏带统计保证的序列设定实用方法
- 🔬 **研究方法**：CCO 把多样辅助评分聚合为偏离保守基线的惩罚，受 Attainable Utility Preservation 启发实现集体保守主义，用 Conformal Decision Theory 在线校准使不良结果低于目标 α
- 📌 **结论**：SWE-bench 上弱监督者成功约束对抗性失准的强 agent；MACHIAVELLI 上大幅减少伦理违规并保留奖励，实测违规率贴近指定目标

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI systems capable of autonomous planning and extended environmental interaction pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed human capabilities? While scalable oversight is widely studied, existing approaches often rely on complex assumptions, remain largely heuristic, or lack practical methods for sequential settings with statistical guarantees. We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty that measures deviation from a conservative baseline. Inspired by Attainable Utility Preservation, CCO enables collective conservatism: when multiple oversight signals register concern, the agent defers. CCO calibrates this conservatism online using Conformal Decision Theory, ensuring that undesirable outcomes remain below a user-specified target $\alpha$ with finite-time bounds and no distributional assumptions. Experiments on SWE-bench demonstrate that weaker overseers successfully constrain an adversarially misaligned stronger agent. Similarly, on MACHIAVELLI, CCO achieves substantial reductions in ethical violations while preserving reward. In both settings, empirical violation rates closely match the specified targets. Our work demonstrates that combining penalty-based conservatism with online calibration yields practical oversight with statistical guarantees suited for agentic deployment.

</details>