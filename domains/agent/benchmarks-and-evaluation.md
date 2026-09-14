# Agent Security 通用 Benchmark 与评测方法

[返回 Agent Security 目录](README.md)

## 研究方向

本页整理跨多个 Agent 攻击面和应用环境的通用安全 benchmark，以及对评测有效性的研究。关键维度包括 benign 与 adversarial utility、真实工具和权限、多轮自适应攻击、长程 delayed trigger、trajectory-level observation、风险 taxonomy、scorer validity 和 capability confounding；只针对 Web、MAS、skill 等单一系统的 benchmark 留在对应页面。

## 研究脉络

- **静态任务集：** 早期 benchmark 以固定 harmful task、prompt injection case 和工具环境比较拒绝、攻击成功率与任务完成率。
- **真实工具环境：** 评测逐渐从抽象 API 扩展到 browser、shell、filesystem、messaging 和多用户任务，使违规动作产生可观察后果。
- **长程与动态 adversary：** 新 benchmark 引入 memory、delayed trigger、多轮攻击者和 attacker adaptation，暴露单轮防御的失效。
- **指标有效性：** benchmark audit 开始检查 F1 baseline、model ranking、capability confounding 和跨任务 convergent validity，避免用单一分数代表“整体安全”。
- **当前边界：** benchmark 仍难同时覆盖真实凭据、长期部署、环境漂移和不可逆后果，且 LLM-as-judge 需要人工审计与可复现 scorer。

## 动态环境与自动 Red Team

### 1. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

📄 [arXiv](https://arxiv.org/abs/2608.27990)　📅 2026-08

**关键词**：`benchmark`、`defense`、`delivery-aware injection`、`emerging attack`、`adaptive defense evaluation`、`adaptive Agent guardrail`

👤 **作者**：Zi Liang、Xiaoyu Xu、Yanyun Wang、Minxin Du、Qingqing Ye、Haibo Hu

- 🎯 **研究动机**：现有提示注入防御只对已知攻击有效，Agent 环境中变体与新威胁不断涌现，且运行效率、上下文精度与适应性构成三难
- 🔬 **研究方法**：提出 Agent 无关防御中间件 CAITLYN：System I 用 Tier-0 规则脚本加 Tier-1 优化 LLM 推理的两级库即时防御；System II 持续监测异常信号并自动合成、验证新防御入库
- 📌 **结论**：在标准 benchmark 上以低于 LLM-as-a-judge 的 token 开销匹配 SOTA 检测性能，并在新建 delivery-aware 的 Emerging benchmark 三种 Agent 环境中显著降低新型注入攻击成功率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks on Large Language Model (LLM) agents seek to introduce malicious instructions or content into external text sources retrieved by agents, forcing the underlying LLMs to execute harmful actions outside their benign scope. While current defenses effectively counter known injection attacks, deploying them in LLM agent environments remains challenging due to attack variants and emerging threats. Moreover, existing solutions typically suffer from an inherent trilemma, i.e., a constant trade-off among runtime efficiency, contextual precision, and adaptability. To bridge this gap, we propose Continuous Agents for Injection Threats via Lifelong Yielding Nexus (CAITLYN), an agent-agnostic defense middleware. CAITLYN integrates two systems. System I focuses on immediate defense against existing attacks using a two-tiered library: Tier-0 for rule-based detection scripts and Tier-1 for optimized LLM-based accurate inference. System II, in contrast, is deployed to monitor potential abnormal signals and attempt to synthesize new defenses. On standard benchmarks, CAITLYN matches the detection performance of state-of-the-art defenses at lower token overhead than LLM-as-a-judge baselines. On Emerging, our new delivery-aware benchmark featuring novel injection techniques, static baselines and the standalone System I configuration remain vulnerable. In contrast, System II autonomously synthesizes verified defense capabilities, substantially lowering the attack success rate across three diverse agent environments.

</details>

### 2. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution

📄 [arXiv](https://arxiv.org/abs/2608.27439)　📅 2026-08

**关键词**：`attack`、`automated red team`、`attack-skill evolution`、`cross-harness transfer`、`self-evolving red team`、`attack skill`

👤 **作者**：Junjie Zhang、Hui Liu、Kecheng Chen、Xianbo Mo、Changsheng Chen、Haoliang Li

- 🎯 **研究动机**：自动红队多依赖固定攻击，agentic 攻击者的轨迹检索受检索偏差与工具贡献不清影响，全轨迹还增加上下文开销并降低可解释性
- 🔬 **研究方法**：提出 RedEvoAgent 黑盒红队 Agent，把跨案例攻击轨迹蒸馏为简洁可读的攻击 skill，经工具效果画像、Deciding-Tool Attribution 与只保留有效更新的 validation ratchet 驱动 skill 演化
- 📌 **结论**：在多 benchmark、目标模型与执行 harness 上超越固定与 agentic 基线，提升工具效率，并可零调整跨攻击者模型与目标 harness 迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit, and full trajectories add context overhead while reducing interpretability. We propose RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill. The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses.

</details>

### 3. ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.08531)　📅 2026-06

**关键词**：`benchmark`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`

👤 **作者**：Lu Jia、…、Yi Zeng

- 🎯 **研究动机**：现有 agent 安全评估依赖人工场景、静态提示或最终输出判断，难以覆盖任务执行中的多样风险
- 🔬 **研究方法**：提出 ForesightSafety-SAGE：基于五个风险维度自动生成 1,072 个可测场景，自动化流水线在两种权限上下文下评估 12 个 LLM agent
- 📌 **结论**：当前 agent 执行期行为风险依旧严峻，平均 ASR 47.1%、多模型超 70%，凸显可执行过程级评估的必要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access external environments, and execute tasks. As their capabilities and autonomy expand, the safety risks they face also become more diverse. Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. We introduce ForesightSafety-SAGE, a fully automated scenario generation and safety evaluation framework for LLM agents. Based on five risk dimensions,we instantiae abstract and diverse safety risks in real-world task execution into 1,072 measurable evaluation scenarios. Using the automated evaluation pipeline, 12 LLM agents are evaluated under two authority contexts. The results show that current agents still face substantial behavioral safety risks during task execution, with an average ASR of 47.1% and several models exceeding 70%. These findings demonstrate the importance of executable, process-level evaluation for understanding and improving LLM agent safety.

</details>

### 4. DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents

📄 [arXiv](https://arxiv.org/abs/2605.04808)　📅 2026-05

**关键词**：`tool`、`automated red team`、`interactive environment`、`verifiable judge`

👤 **作者**：Zhaorun Chen、…、Bo Li

- 🎯 **研究动机**：Agent 安全评测缺乏真实、可控、可复现的大规模风险评估环境
- 🔬 **研究方法**：DTap 覆盖 14 个领域、50+ 个模拟环境（复刻 Google Workspace、PayPal、Slack 等）；DTap-Red 自主探索 prompt、tool、skill、环境等注入向量并策展带可验证 judge 的 DTap-Bench
- 📌 **结论**：对多种骨干模型构建的主流 agent 的大规模评测揭示系统性漏洞模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are increasingly deployed across diverse domains to automate complex workflows through long-horizon and high-stakes action executions. Due to their high capability and flexibility, such agents raise significant security and safety concerns. A growing number of real-world incidents have shown that adversaries can easily manipulate agents into performing harmful actions, such as leaking API keys, deleting user data, or initiating unauthorized transactions. Evaluating agent security is inherently challenging, as agents operate in dynamic, untrusted environments involving external tools, heterogeneous data sources, and frequent user interactions. However, realistic, controllable, and reproducible environments for large-scale risk assessment remain largely underexplored. To address this gap, we introduce the DecodingTrust-Agent Platform (DTap), the first controllable and interactive red-teaming platform for AI agents, spanning 14 real-world domains and over 50 simulation environments that replicate widely used systems such as Google Workspace, Paypal, and Slack. To scale the risk assessment of agents in DTap, we further propose DTap-Red, the first autonomous red-teaming agent that systematically explores diverse injection vectors (e.g., prompt, tool, skill, environment, combinations) and autonomously discovers effective attack strategies tailored to varying malicious goals. Using DTap-Red, we curate DTap-Bench, a large-scale red-teaming dataset comprising high-quality instances across domains, each paired with a verifiable judge to automatically validate attack outcomes. Through DTap, we conduct large-scale evaluations of popular AI agents built on various backbone models, spanning security policies, risk categories, and attack strategies, revealing systematic vulnerability patterns and providing valuable insights for developing secure next-generation agents.

</details>

### 5. AgentDyn: Are Your Agent Security Defenses Deployable in Real-World Dynamic Environments?

📄 [arXiv](https://arxiv.org/abs/2602.03117)　📅 2026-02

**关键词**：`benchmark`、`dynamic environment`、`indirect prompt injection`、`over-defense`

👤 **作者**：Hao Li、Ruoyao Wen、Shanghao Shi、Ning Zhang、Yevgeniy Vorobeychik、Chaowei Xiao

- 🎯 **研究动机**：现有 agent 安全基准缺动态开放任务、缺有用第三方指令且用户任务过简，难以反映真实部署
- 🔬 **研究方法**：AgentDyn 手工构建 60 个开放任务与 560 个注入测试用例（Shopping、GitHub、Daily Life），要求动态规划并纳入有用的第三方指令
- 📌 **结论**：十个 SOTA 防御几乎全部要么安全性不足、要么严重过度防御，距真实世界部署尚远

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents that autonomously interact with external tools and environments have shown great promise across real-world applications. However, their reliance on external data exposes them to serious indirect prompt injection attacks, where malicious instructions embedded in third-party content hijack agent behaviors. To mitigate this threat, a growing number of defenses have been proposed and evaluated under existing agent security benchmarks. These benchmarks provide structured environments for comparing attacks and defenses, and have become a key driver for defense design and optimization. However, as agents move toward more complex and open-ended real-world deployments, there is a pressing need for benchmarks to become more adaptive and better reflect the dynamic environments faced by real-world agentic systems. In this work, we reveal three fundamental flaws in the current benchmarks and push the frontier along these dimensions: (i) lack of dynamic open-ended tasks, (ii) lack of helpful instructions, and (iii) simplistic user tasks. To bridge this gap, we introduce AgentDyn, a manually designed benchmark featuring 60 challenging open-ended tasks and 560 injection test cases across Shopping, GitHub, and Daily Life. Unlike prior static benchmarks, AgentDyn requires dynamic planning and incorporates helpful third-party instructions. Our evaluation of ten state-of-the-art defenses suggests that almost all existing defenses are either not secure enough or suffer from significant over-defense, revealing that existing defenses are still far from real-world deployment. Our benchmark is available at https://github.com/leolee99/AgentDyn.

</details>

### 6. Multimodal Safety Evaluation in Generative Agent Social Simulations

🎓 [Official](https://aclanthology.org/2026.acl-long.1915/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`multimodal safety`、`agent safety`、`VLM safety`、`LLM agent`

👤 **作者**：Alhim Adonai Vera Gonzalez、Carlos Hinojosa、Karen Sanchez、Haidar Bin Hamid、Donghoon Kim、Bernard Ghanem

- 🎯 **研究动机**：生成式智能体在多模态环境中跨模态的安全推理与信任能力未知
- 🔬 **研究方法**：可复现仿真框架评迭代规划修订的安全改进、跨社交语境的不安全活动检测与社会动态，发布 1,000 个多模态计划（逾 60 万仿真步）
- 📌 **结论**：智能体能发现直接多模态矛盾但难对齐局部修订与全局安全，纠正不安全计划成功率仅 55%；误导性视觉线索下 45% 不安全行为被接受，过度信任视觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Can generative agents be trusted in multimodal environments? Despite recent advances, agents remain limited in their ability to reason about safety, coherence, and trust across modalities. We introduce a reproducible simulation framework to evaluate generative agents in three aspects: (1) safety improvement over time via iterative plan revision in multimodal scenarios; (2) detection of unsafe activities across social contexts; and (3) social dynamics, measured through interaction and acceptance rates. These multimodal agents are evaluated using metrics that quantify plan revisions and unsafe-to-safe conversions. Experiments show that while agents detect direct multimodal contradictions, they often fail to align local revisions with global safety, achieving only a 55% success rate in correcting unsafe plans. We release a dataset of 1,000 multimodal plans, yielding more than 600,000 simulation steps. Notably, 45% of unsafe actions are accepted when paired with misleading visual cues, revealing a strong tendency to overtrust visual content. Code is available at https://github.com/AdonaiVera/X-CASE

</details>

### 7. Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

📄 [arXiv](https://arxiv.org/abs/2607.18063)　📅 2026-07

**关键词**：`benchmark`、`adaptive attacker`、`multi-turn attack`、`scenario sensitivity`

👤 **作者**：Devina Jain、David Hartmann、Chuan Li

- 🎯 **研究动机**：多数安全基准使用评估前收集的固定攻击池，自适应多轮攻击者对无记忆 LLM 防守方的威胁未被量化
- 🔬 **研究方法**：构建 21 场景基准：自主 LLM 攻击者观察历史响应跨轮调整，固定场景、攻击者、防守者与结构化评分做受控对比，并发布 945 份转录与攻击重放数据
- 📌 **结论**：仅评第一轮 ASR 为 0-1%，允许 15 轮自适应攻击后升至 5.4-14.0%；三攻击者池比最佳单个多发现 1.4-2.2 倍独特攻击，模型弱点呈场景特异性（排名不一致，Kendall W=0.19）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. Holding the 21 scenarios, attackers, defenders, and structured-output scoring fixed, restricting scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing 15 rounds of adaptive attack yields $5.4$-$14.0\%$. Pooling three frontier attacker LLMs uncovers $1.4$-$2.2\times$ as many unique successful attacks as the best single attacker, and the generated attacks have low cosine similarity ($0.02$-$0.14$) to attacks in existing benchmarks. Claude Opus 4.6 and GPT-5.4 are tied in aggregate ($5.4\%$ each; overlapping $95\%$ CIs), but their weaknesses differ sharply: on one scenario Opus reaches $60\%$ ASR ($95\%$ CI $36$--$80\%$) while GPT-5.4 and Gemini each stay at $7\%$ (CI $1$-$30\%$; the gap is preserved in a higher-$N$ replication). $13$ of $21$ scenarios distinguish at least one defender pair, yet rankings disagree across scenarios (Kendall's $W = 0.19$). We release the benchmark -- 21 evaluation scenarios, 10 public development scenarios, the orchestrator, baseline harnesses, and a multi-attacker CLI -- plus 945 transcripts from the 3$\times$3 frontier matrix, an attack-replay dataset, and 18{,}422 gpt-oss-20b battles from an open competition's final scoring rounds.

</details>

### 8. ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis

📄 [arXiv](https://arxiv.org/abs/2604.02022) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`long-horizon trajectory`、`delayed trigger`、`risk taxonomy`

👤 **作者**：Yu Li、…、Dongrui Liu

- 🎯 **研究动机**：轨迹级安全基准交互多样性不足、安全失效可观测性粗、长程真实性弱
- 🔬 **研究方法**：ATBench 按风险源、失效模式、现实危害三维组织，用异构工具池与长上下文延迟触发协议构建 1,000 条轨迹（平均 9.01 轮、2,084 个可用工具），经规则与 LLM 过滤加全程人工审计
- 📌 **结论**：对前沿 LLM、开源模型与专用护栏系统均具挑战性，支持分类分层分析与长程失效模式诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the safety of LLM-based agents is increasingly important because risks in realistic deployments often emerge over multi-step interactions rather than isolated prompts or final responses. Existing trajectory-level benchmarks remain limited by insufficient interaction diversity, coarse observability of safety failures, and weak long-horizon realism. We introduce ATBench, a trajectory-level benchmark for structured, diverse, and realistic evaluation of agent safety. ATBench organizes agentic risk along three dimensions: risk source, failure mode, and real-world harm. Based on this taxonomy, we construct trajectories with heterogeneous tool pools and a long-context delayed-trigger protocol that captures realistic risk emergence across multiple stages. The benchmark contains 1,000 trajectories (503 safe and 497 unsafe), averaging 9.01 turns and 3.95k tokens, with 1,954 invoked tools drawn from pools spanning 2,084 available tools. Data quality is supported by rule-based and LLM-based filtering plus full human audit. Experiments on frontier LLMs, open-source models, and specialized guard systems show that ATBench is challenging even for strong evaluators, while enabling taxonomy-stratified analysis, cross-benchmark comparison, and diagnosis of long-horizon failure patterns.

</details>

### 9. AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks

📄 [arXiv](https://arxiv.org/abs/2602.16901) · 🌐 [Project](https://tanqiujiang.github.io/AgentLAB_main) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65640)　📅 2026-02　🏷 ICML 2026

**关键词**：`benchmark`、`long-horizon attack`、`memory poisoning`、`objective drift`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Tanqiu Jiang、Yuhui Wang、Jiacheng Liang、Ting Wang

- 🎯 **研究动机**：长程攻击利用多轮用户-agent-环境交互实现单轮不可行的目标，缺少专用评测基准
- 🔬 **研究方法**：AgentLAB 覆盖 intent hijacking、tool chaining、task injection、objective drifting、memory poisoning 五类攻击，含 28 个环境与 644 个安全测试用例
- 📌 **结论**：代表性 LLM agent 对长程攻击高度易感，面向单轮交互设计的防御无法可靠缓解长程威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are increasingly deployed in long-horizon, complex environments to solve challenging problems, but this expansion exposes them to long-horizon attacks that exploit multi-turn user-agent-environment interactions to achieve objectives infeasible in single-turn settings. To measure agent vulnerabilities to such risks, we present AgentLAB, the first benchmark dedicated to evaluating LLM agent susceptibility to adaptive, long-horizon attacks. Currently, AgentLAB supports five novel attack types including intent hijacking, tool chaining, task injection, objective drifting, and memory poisoning, spanning 28 realistic agentic environments, and 644 security test cases. Leveraging AgentLAB, we evaluate representative LLM agents and find that they remain highly susceptible to long-horizon attacks; moreover, defenses designed for single-turn interactions fail to reliably mitigate long-horizon threats. We anticipate that AgentLAB will serve as a valuable benchmark for tracking progress on securing LLM agents in practical settings. The benchmark is publicly available at https://tanqiujiang.github.io/AgentLAB_main.

</details>

### 10. PACE: Towards Surfacing Hidden Conflicts in User Requests

📄 [arXiv](https://arxiv.org/abs/2609.03293)　📅 2026-09

**关键词**：`benchmark`、`personalized assistant`、`latent constraint`、`conflict evaluation`、`context conflict`、`evidence retrieval`

👤 **作者**：Yoojin Kim、Jihyoung Jang、Hyounghun Kim

- 🎯 **研究动机**：个性化助手只顾准确执行请求，忽视了结合用户情境识别隐含约束并做基于冲突的拒绝；现有冲突检测又依赖显式给定因素
- 🔬 **研究方法**：构建 PACE 数据集：把基于 persona 的用户请求与自我中心知识库事实配对，要求模型经隐式检索整合证据判断请求是否冲突；并提出 PaceMaker 多 Agent 框架（查询改写、多跳图遍历、冲突感知过滤）
- 📌 **结论**：隐式检索设定使现有模型难以定位用户特定事实，PaceMaker 在证据检索质量与冲突决策准确率上持续超过现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personalized assistants should not only comply with user requests but also assess whether those requests are appropriate given the user's current circumstances. However, prior work has primarily focused on accurately executing requests, overlooking the need for assistants to account for context and engage in conflict-based refusal. Furthermore, while existing work on conflict or safety detection relies on explicitly provided factors, real-world scenarios often involve implicit factors that must be retrieved from a knowledge base (KB). To this end, we introduce Personalized Assistants for Conflict Evaluation (PACE), a dataset for evaluating whether models can identify latent constraints, expressed as egocentric knowledge or events, that render seemingly reasonable user requests inappropriate. PACE pairs user requests grounded in well-defined personas with egocentric KB facts, requiring models to integrate contextual evidence to determine whether a request is conflicting. This implicit retrieval setting hinders the direct association between user requests and conflict-inducing knowledge, making it difficult for existing models to identify relevant user-specific facts. To address this challenge, we further propose PaceMaker, a multi-agent framework in which specialized agents coordinate across query reformulation, multi-hop graph traversal, and conflict-aware filtering to retrieve contextually decisive evidence. Experiments on PACE evaluate both evidence retrieval quality and conflict decision accuracy, showing that PaceMaker consistently outperforms existing approaches.

</details>

### 11. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

📄 [arXiv](https://arxiv.org/abs/2608.17597) · 🌐 [Project](https://baiyajing.github.io/harness-risk/)　📅 2026-08

**关键词**：`benchmark`、`operational lifecycle`、`model-harness pairing`、`attack persistence`、`harness lifecycle`、`configuration attack`

👤 **作者**：Yajing Bai、…、Tianlong Chen

- 🎯 **研究动机**：现有 agent 安全基准针对单一攻击机制或少量运营设定，难以比较不同 harness 职责下安全失效如何出现
- 🔬 **研究方法**：HarnessRisk 把 harness 安全组织为配置、能力扩展、运行、状态持久、动作控制与事故恢复六阶段，128 个沙箱用例以 Utility、ASR、Persistence、Detection 四指标评 14 种模型-harness 配置
- 📌 **结论**：攻击成功率 12.6%-80.9%；Harness Configuration 是三个 harness 共同最弱阶段；显式风险识别不保证安全行动——部分配置 90% 以上运行检出风险仍保高 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities. We present HarnessRisk, a lifecycle oriented benchmark that organizes agent harness safety into six operational phases including Harness Configuration, Capability Extension, Runtime Operation, State Persistence, Action Control, and Incident Recovery. HarnessRisk contains 128 sandboxed cases, each pairing a benign user objective with an adversarial instruction embedded in an untrusted workflow artifact. We evaluate each trajectory using Utility, Attack Success Rate, Persistence, and Detection. Across three harnesses, six language models, and 14 model and harness configurations, attack success ranges from 12.6% to 80.9%, while Utility remains between 75.0% and 97.6%. Harness Configuration is the most vulnerable phase across all three harnesses, showing that attacks can succeed by altering security sensitive parameters within otherwise authorized workflows. We also find that explicit risk recognition does not reliably lead to safe action, as some configurations detect risks in more than 90% of runs while retaining substantial attack success. These results highlight the need to evaluate agent safety across multiple harness responsibilities and at the level of the deployed model and harness configuration.

</details>

### 12. Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents

📄 [arXiv](https://arxiv.org/abs/2604.06132) · 🌐 [Project](https://claw-eval.github.io/)　📅 2026-04

**关键词**：`benchmark`、`trajectory evidence`、`safety robustness`、`autonomous agent`

👤 **作者**：Bowen Ye、…、Tong Yang

- 🎯 **研究动机**：agent 基准受轨迹不透明评分、安全鲁棒性评测不完整与模态覆盖窄的限制
- 🔬 **研究方法**：Claw-Eval 含 300 个人工验证任务，经执行轨迹、审计日志与环境快照三通道证据与 2,159 个 rubric 项评 Completion、Safety、Robustness，三次试验区分真实能力与运气
- 📌 **结论**：轨迹不透明评测漏掉 44% 安全违规与 13% 鲁棒性失败；能力不等于一致性（Pass^3 最多掉 24 个百分点），模型排名随任务组强烈变化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed as autonomous agents for multi-step workflows in real-world software environments. However, existing agent benchmarks are limited by trajectory-opaque grading, underspecified safety and robustness evaluation, and narrow coverage of modalities and interaction paradigms. We introduce Claw-Eval, an end-to-end evaluation suite addressing these gaps with 300 human-verified tasks spanning 9 categories across three groups: general service orchestration, multimodal perception and interaction, and multi-turn professional dialogue. To enable trajectory-aware grading, each run is recorded through three independent evidence channels: execution traces, audit logs, and environment snapshots, yielding 2,159 fine-grained rubric items. The scoring protocol evaluates Completion, Safety, and Robustness, with Average Score, Pass@k, and Pass^k across three trials to distinguish genuine capability from lucky outcomes. Experiments on 14 frontier models show that: (1) Trajectory-opaque evaluation is systematically unreliable, missing 44% of safety violations and 13% of robustness failures detected by our framework. (2) Capability does not imply consistency, with Pass@3 remaining stable under error injection while Pass^3 dropping by up to 24 percentage points. (3) Agent capability is strongly multi-dimensional, with model rankings varying across task groups and metrics, indicating that our heterogeneous evaluation coverage is essential. Claw-Eval highlights directions for developing agents that are not only capable but reliably deployable.

</details>

### 13. Benchmarking the Robustness of Agentic Systems to Adversarially-Induced Harms

📄 [arXiv](https://arxiv.org/abs/2508.16481) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-08

**关键词**：`benchmark`、`prompt injection`、`adversarial robustness`、`agent safety benchmark`

👤 **作者**：Jonathan Nöther、Adish Singla、Goran Radanovic

- 🎯 **研究动机**：agent 系统可能表现出的恶意行为谱系与鲁棒性缺乏系统刻画
- 🔬 **研究方法**：提出 agent 危害分类法与 BAD-ACTS 基准：五种应用环境实现、238 个高质量有害行为样本与 699 个对抗行为扩展集，测试对抗 agent 与 prompt 注入等攻击者
- 📌 **结论**：各模型攻击成功率介于 40%-90%；提出的零样本消息监控防御有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safe use of agentic systems requires a thorough understanding of the range of malicious behaviors these systems may exhibit. In this paper, we evaluate the robustness of LLM-based agentic systems against attacks that aim to elicit harmful actions from agents. To this end, we propose a novel taxonomy of harms for agentic systems and a novel benchmark, BAD-ACTS, for studying the security of agentic systems with respect to a wide range of harmful actions. BAD-ACTS consists of five implementations of agentic systems in distinct application environments, as well as a dataset of 238 high-quality examples of harmful actions and an extended dataset containing 699 additional adversarial actions. This enables a comprehensive study of the robustness of agentic systems across a wide range of categories of harmful behaviors, available tools, and inter-agent communication structures. Using this benchmark, we analyze the robustness of agentic systems under an array of attackers attempting to elicit malicious behaviors, including agents acting adversarially and prompt injections. We found that agents are often vulnerable, as indicated by success rates between 40% and 90% depending on the model. We additionally propose an effective defense based on zero-shot message monitoring. We believe that this benchmark provides a diverse testbed for the safety research of agentic systems. Code is available at https://github.com/JNoether/BAD-ACTS.

</details>

### 14. OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety

📄 [arXiv](https://arxiv.org/abs/2507.06134) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006628)　📅 2025-07　🏷 ICLR 2026

**关键词**：`benchmark`、`real tools`、`multi-user task`、`extensible framework`

👤 **作者**：Sanidhya Vijayvargiya、…、Maarten Sap

- 🎯 **研究动机**：既有 agent 安全基准依赖模拟环境、窄域任务或不真实的工具抽象
- 🔬 **研究方法**：构建 OpenAgentSafety：真实工具（浏览器、代码执行、文件系统、bash、消息平台）、8 类风险、350+ 多轮多用户任务，规则加 LLM-as-judge 判定
- 📌 **结论**：五个 LLM 在安全攸关任务中的不安全行为率从 51.2%（Claude-Sonnet-3.7）到 72.7%（o3-mini）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in AI agents capable of solving complex, everyday tasks, from scheduling to customer service, have enabled deployment in real-world settings, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to assess agent safety, most fall short by relying on simulated environments, narrow task domains, or unrealistic tool abstractions. We introduce OpenAgentSafety, a comprehensive and modular framework for evaluating agent behavior across eight critical risk categories. Unlike prior work, our framework evaluates agents that interact with real tools, including web browsers, code execution environments, file systems, bash shells, and messaging platforms; and supports over 350 multi-turn, multi-user tasks spanning both benign and adversarial user intents. OpenAgentSafety is designed for extensibility, allowing researchers to add tools, tasks, websites, and adversarial strategies with minimal effort. It combines rule-based analysis with LLM-as-judge assessments to detect both overt and subtle unsafe behaviors. Empirical analysis of five prominent LLMs in agentic scenarios reveals unsafe behavior in 51.2% of safety-vulnerable tasks with Claude-Sonnet-3.7, to 72.7% with o3-mini, highlighting critical safety vulnerabilities and the need for stronger safeguards before real-world deployment.

</details>

### 15. AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2506.00641) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3dc85735f6e2fcf093e67b134fa00d21-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`benchmark`、`automated auditing`、`security scenario`、`ASSEBench`

👤 **作者**：Hanjun Luo、…、Hanan Salam

- 🎯 **研究动机**：规则或 LLM 评测器会漏掉 agent 分步动作中的危险、细微含义与复合小问题
- 🔬 **研究方法**：提出 AgentAuditor：以结构化语义特征与推理轨迹构建经验记忆，多阶段上下文感知 RAG 引导评估；发布 2293 条、15 类风险的 ASSEBench
- 📌 **结论**：全面提升 LLM 评测器表现，在 agent 安全与安全评测上达成人类水平的 LLM-as-a-judge 新 SoTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents' step-by-step actions, overlook subtle meanings, fail to see how small issues compound, and get confused by unclear safety or security rules. To overcome this evaluation crisis, we introduce AgentAuditor, a universal, training-free, memory-augmented reasoning framework that empowers LLM evaluators to emulate human expert evaluators. AgentAuditor constructs an experiential memory by having an LLM adaptively extract structured semantic features (e.g., scenario, risk, behavior) and generate associated chain-of-thought reasoning traces for past interactions. A multi-stage, context-aware retrieval-augmented generation process then dynamically retrieves the most relevant reasoning experiences to guide the LLM evaluator's assessment of new cases. Moreover, we developed ASSEBench, the first benchmark designed to check how well LLM-based evaluators can spot both safety risks and security threats. ASSEBench comprises 2293 meticulously annotated interaction records, covering 15 risk types across 29 application scenarios. A key feature of ASSEBench is its nuanced approach to ambiguous risk situations, employing "Strict" and "Lenient" judgment standards. Experiments demonstrate that AgentAuditor not only consistently improves the evaluation performance of LLMs across all benchmarks but also sets a new state-of-the-art in LLM-as-a-judge for agent safety and security, achieving human-level accuracy. Our work is openly accessible at https://github.com/Astarojth/AgentAuditor.

</details>

### 16. Agent-SafetyBench: Evaluating the Safety of LLM Agents

📄 [arXiv](https://arxiv.org/abs/2412.14470) · 🌐 [Project](https://trustagenticai.github.io/AAAI2026/AAAI-Workshop/30.pdf)　📅 2024-12　🏷 AAAI 2026

**关键词**：`benchmark`、`unsafe action`、`tool-use safety`、`risk category`

👤 **作者**：Zhexin Zhang、…、Minlie Huang

- 🎯 **研究动机**：LLM Agent 缺乏综合安全评测基准
- 🔬 **研究方法**：Agent-SafetyBench 含 349 个交互环境与 2000 个测试用例，覆盖 8 类风险与 10 种失败模式，评测 16 个流行 Agent
- 📌 **结论**：无一 Agent 安全分超 60%；揭示鲁棒性缺失与风险意识缺失两大缺陷，仅靠防御 prompt 不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed as agents, their integration into interactive environments and tool use introduce new safety challenges beyond those associated with the models themselves. However, the absence of comprehensive benchmarks for evaluating agent safety presents a significant barrier to effective assessment and further improvement. In this paper, we introduce Agent-SafetyBench, a comprehensive benchmark designed to evaluate the safety of LLM agents. Agent-SafetyBench encompasses 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 common failure modes frequently encountered in unsafe interactions. Our evaluation of 16 popular LLM agents reveals a concerning result: none of the agents achieves a safety score above 60%. This highlights significant safety challenges in LLM agents and underscores the considerable need for improvement. Through failure mode and helpfulness analysis, we summarize two fundamental safety defects in current LLM agents: lack of robustness and lack of risk awareness. Furthermore, our findings suggest that reliance on defense prompts alone may be insufficient to address these safety issues, emphasizing the need for more advanced and robust strategies. To drive progress in this area, Agent-SafetyBench has been released at https://github.com/thu-coai/Agent-SafetyBench/ to facilitate further research in agent safety evaluation and improvement.

</details>

### 17. R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

🎓 [Official](https://aclanthology.org/2024.findings-emnlp.79/)　📅 2024-11　🏷 EMNLP 2024

**关键词**：`benchmark`、`risk awareness`、`interaction record`、`safety judge`

👤 **作者**：Tongxin Yuan、…、Gongshen Liu

- 🎯 **研究动机**：已有研究聚焦生成内容无害性，LLM 智能体在交互环境中的行为安全缺评测基准
- 🔬 **研究方法**：R-Judge 含 569 条多轮智能体交互记录，覆盖 5 类应用、27 个风险场景与 10 种风险类型，附安全标签与风险描述，评测 11 个 LLM 的风险判别力
- 📌 **结论**：最佳模型 GPT-4o 仅 74.42%，其余不显著超随机；安全判别微调显著提升而简单提示机制无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. Despite this, these LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLM-generated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments. We introduce R-Judge, a benchmark crafted to evaluate the proficiency of LLMs in judging and identifying safety risks given agent interaction records. R-Judge comprises 569 records of multi-turn agent interaction, encompassing 27 key risk scenarios among 5 application categories and 10 risk types. It is of high-quality curation with annotated safety labels and risk descriptions. Evaluation of 11 LLMs on R-Judge shows considerable room for enhancing the risk awareness of LLMs: The best-performing model, GPT-4o, achieves 74.42% while no other models significantly exceed the random. Moreover, we reveal that risk awareness in open agent scenarios is a multi-dimensional capability involving knowledge and reasoning, thus challenging for LLMs. With further experiments, we find that fine-tuning on safety judgment significantly improve model performance while straightforward prompting mechanisms fail. R-Judge is publicly available at Annoymous.

</details>

### 18. Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents

📄 [arXiv](https://arxiv.org/abs/2410.02644) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5750f91d8fb9d5c02bd8ad2c3b44456b-Abstract-Conference.html)　📅 2024-10　🏷 ICLR 2025

**关键词**：`benchmark`、`attack-defense matrix`、`tool agent`、`security formalization`

👤 **作者**：Hanrong Zhang、…、Yongfeng Zhang

- 🎯 **研究动机**：LLM Agent 攻防缺乏统一形式化与综合评测协议
- 🔬 **研究方法**：ASB 覆盖 10 场景、10 个 Agent、400 余工具、27 类攻防与 7 项指标；评测 prompt 注入、memory 投毒、新型 Plan-of-Thought 后门及 11 种防御
- 📌 **结论**：Agent 各阶段平均 ASR 最高 84.30%，现有防御效果有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although LLM-based agents, powered by Large Language Models (LLMs), can use external tools and memory mechanisms to solve complex real-world tasks, they may also introduce critical security vulnerabilities. However, the existing literature does not comprehensively evaluate attacks and defenses against LLM-based agents. To address this, we introduce Agent Security Bench (ASB), a comprehensive framework designed to formalize, benchmark, and evaluate the attacks and defenses of LLM-based agents, including 10 scenarios (e.g., e-commerce, autonomous driving, finance), 10 agents targeting the scenarios, over 400 tools, 27 different types of attack/defense methods, and 7 evaluation metrics. Based on ASB, we benchmark 10 prompt injection attacks, a memory poisoning attack, a novel Plan-of-Thought backdoor attack, 4 mixed attacks, and 11 corresponding defenses across 13 LLM backbones. Our benchmark results reveal critical vulnerabilities in different stages of agent operation, including system prompt, user prompt handling, tool usage, and memory retrieval, with the highest average attack success rate of 84.30\%, but limited effectiveness shown in current defenses, unveiling important works to be done in terms of agent security for the community. We also introduce a new metric to evaluate the agents' capability to balance utility and security. Our code can be found at https://github.com/agiresearch/ASB.

</details>

### 19. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2406.13352) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2024-06　🏷 NeurIPS 2024

**关键词**：`benchmark`、`prompt injection`、`dynamic environment`、`utility-security`

👤 **作者**：Edoardo Debenedetti、Jie Zhang、Mislav Balunović、Luca Beurer-Kellner、Marc Fischer、Florian Tramèr

- 🎯 **研究动机**：静态测试集无法衡量持续演化的 prompt injection 攻防与 Agent 任务效用
- 🔬 **研究方法**：AgentDojo 是可扩展动态环境：97 个现实任务、629 个安全测试用例与文献中多种攻防范式
- 📌 **结论**：SOTA LLM 在无攻击时也常失败，现有注入攻击只破坏部分安全属性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents aim to solve complex tasks by combining text-based reasoning with external tool calls. Unfortunately, AI agents are vulnerable to prompt injection attacks where data returned by external tools hijacks the agent to execute malicious tasks. To measure the adversarial robustness of AI agents, we introduce AgentDojo, an evaluation framework for agents that execute tools over untrusted data. To capture the evolving nature of attacks and defenses, AgentDojo is not a static test suite, but rather an extensible environment for designing and evaluating new agent tasks, defenses, and adaptive attacks. We populate the environment with 97 realistic tasks (e.g., managing an email client, navigating an e-banking website, or making travel bookings), 629 security test cases, and various attack and defense paradigms from the literature. We find that AgentDojo poses a challenge for both attacks and defenses: state-of-the-art LLMs fail at many tasks (even in the absence of attacks), and existing prompt injection attacks break some security properties but not all. We hope that AgentDojo can foster research on new design principles for AI agents that solve common tasks in a reliable and robust manner.. We release the code for AgentDojo at https://github.com/ethz-spylab/agentdojo.

</details>

### 20. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

📄 [arXiv](https://arxiv.org/abs/2403.02691) · 🎓 [Official](https://aclanthology.org/2024.findings-acl.624/)　📅 2024-03　🏷 ACL 2024

**关键词**：`benchmark`、`indirect prompt injection`、`tool-integrated agent`、`external content`

👤 **作者**：Qiusi Zhan、Zhixiang Liang、Zifan Ying、Daniel Kang

- 🎯 **研究动机**：工具集成 LLM Agent 面临间接 prompt 注入攻击，缺乏系统评测基准
- 🔬 **研究方法**：InjecAgent 含 1054 个测试用例、17 种用户工具与 62 种攻击者工具，攻击意图分直接伤害与隐私外泄两类
- 📌 **结论**：30 个 Agent 均脆弱，ReAct 版 GPT-4 被攻击成功 24%；攻击指令加 hacking prompt 后成功率近翻倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has embodied LLMs as agents, allowing them to access tools, perform actions, and interact with external content (e.g., emails or websites). However, external content introduces the risk of indirect prompt injection (IPI) attacks, where malicious instructions are embedded within the content processed by LLMs, aiming to manipulate these agents into executing detrimental actions against users. Given the potentially severe consequences of such attacks, establishing benchmarks to assess and mitigate these risks is imperative. In this work, we introduce InjecAgent, a benchmark designed to assess the vulnerability of tool-integrated LLM agents to IPI attacks. InjecAgent comprises 1,054 test cases covering 17 different user tools and 62 attacker tools. We categorize attack intentions into two primary types: direct harm to users and exfiltration of private data. We evaluate 30 different LLM agents and show that agents are vulnerable to IPI attacks, with ReAct-prompted GPT-4 vulnerable to attacks 24% of the time. Further investigation into an enhanced setting, where the attacker instructions are reinforced with a hacking prompt, shows additional increases in success rates, nearly doubling the attack success rate on the ReAct-prompted GPT-4. Our findings raise questions about the widespread deployment of LLM Agents. Our benchmark is available at https://github.com/uiuc-kang-lab/InjecAgent.

</details>

### 21. PatchBench: Evaluating AI Agents for Vulnerability Patching

📄 [arXiv](https://arxiv.org/abs/2609.04075)　📅 2026-09

**关键词**：`benchmark`、`evaluation validity`、`patch memorization`、`security correctness`、`vulnerability patching`、`semantic validation`

👤 **作者**：Chihao Shen、Jiacheng Li、Aastha Mahajan、Jeffery Siyuan Tian、Yonghwi Kwon、Yizheng Chen

- 🎯 **研究动机**：只用 PoC 不再崩溃验证补丁，会让记忆历史开发者补丁或仅压制崩溃的表面修补冒充安全修复
- 🔬 **研究方法**：提出 PatchBench：选取真值修复位于崩溃栈之外的漏洞，用漏洞移植与代码变异迁移到新仓库上下文，并新增兼顾安全与语义正确性的补丁验证方法
- 📌 **结论**：平均 25% 的 Agent 补丁与历史开发者补丁高度相似；对 11 个 SOTA Agent（含 AIxCC 前三），仅 PoC 验证平均把解题率夸大 1.83 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash. This leaves two key threats to validity: agents may reproduce memorized historical developer patches, or they may generate surface-level fixes that only suppress the reported crash. We study these concerns for C/C++ vulnerability patching. We introduce a patch similarity metric to detect memorized patches. On average, 25% of the agent patches exhibit substantial similarity to historical developer patches, indicating that patch memorization is a real threat to the validity of vulnerability patching evaluations. Meanwhile, agents also frequently exploit benchmark structures to pass patch validation by patching on the crash stack trace to suppress the crash, rather than localizing and fixing the root cause of the vulnerabilities. To handle these issues, we propose PatchBench, a new benchmark for evaluating AI agents on realistic vulnerability patching tasks. PatchBench selects vulnerabilities whose ground-truth fixes lie outside the crash stack and uses vulnerability transplant and code mutations to migrate historical vulnerabilities into new repository contexts, reducing the risks of surface-level fixes and patch memorization. We develop new patch validation methods that thoroughly evaluate both security and semantic correctness of agent patches. Across 11 state-of-the-art agents, including the top three AIxCC agents, the original PoC-only validation inflates the patching task solve rate of agents by 1.83$\times$ on average. Our results reveal key limitations of current patching agents and point to future research directions for more reliable vulnerability repair.

</details>

### 22. LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails

📄 [arXiv](https://arxiv.org/abs/2609.02246)　📅 2026-09

**关键词**：`analysis`、`LLM-as-a-judge`、`reward hacking`、`self-improving agent`

👤 **作者**：Vansh Wahi

- 🎯 **研究动机**：self-improving 管线中心是 LLM judge，而它未 earned oracle 地位——生产运行中评测信号被多种方式 gaming
- 🔬 **研究方法**：基于数月自主 prompt 优化生产运行归纳 11 类评测失败（judge 偏差、harness／指标故障、真值错误、reward hacking），提出 PROCTOR：judge 降为 advisor，由密封沙箱、能力分离角色、高于 Teacher 的验收检查、冻结 holdout 与作弊金丝雀五重确定性护栏门控每次变更
- 📌 **结论**：曾出现满分率 100% 掩盖 68% 真实能力、错误真值导致删除正确合规规则等案例；重写 judge rubric 会平台化，唯结构性约束可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is itself an LLM. That judge has the last word on whether the system is getting better, and our position is that it has not earned it. The judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override. We reached this position by building the alternative and running it. Over months of running autonomous prompt-optimization loops in production across contract analysis, compliance review, and code quality, we cataloged eleven ways the evaluation signal failed, in four classes: judge bias, harness and metric failures, ground-truth errors, and reward hacking. Agents achieved perfect scores by reading cached answer keys from their environment, a 100% pass rate concealing 68% true capability. A corrupted ground-truth label caused the optimizer to delete correct compliance rules to agree with it. A syntactically broken prompt was promoted as the winner because a silent parser fallback improved the metric. Attempts to fix the judge by rewriting its rubric plateaued; the only reliable gain came from a structural constraint on its output order. In response we describe PROCTOR, a Teacher-Student loop in which a stateful orchestrator holds all tool access, stateless subagents diagnose failures and draft mutations they cannot apply, and a Teacher grades those mutations under five deterministic guardrails: hermetic sandboxes, capability-disjoint roles, acceptance checks that outrank the Teacher, frozen holdouts, and canary cases engineered so that a perfect score is itself evidence of cheating. We report the failures this prevented, and, because the Teacher is itself an LLM judge, the failures it did not.

</details>

### 23. Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds

📄 [arXiv](https://arxiv.org/abs/2609.02302)　📅 2026-09

**关键词**：`analysis`、`evaluation awareness`、`deployment realism`、`alignment audit`

👤 **作者**：Axel Ahlqvist、…、John Hughes

- 🎯 **研究动机**：evaluation awareness 使有能力模型可分辨测试与部署，削弱模拟对齐评测的结论效力
- 🔬 **研究方法**：提出两项技术：critique refinement 用目标模型实例的反馈精修多个候选动作、选最像部署者继续评测；DISH 用部署级 SWE-Agent harness 包裹目标缩小编码场景的模拟-真实差距
- 📌 **结论**：两项技术可叠加、联合 realism 增益大于单独使用，且额外算力的效果好于单纯拉长审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback from an instance of the target model on how to make them more realistic, and continues the evaluation with the most deployment-like candidate. Our second technique, DISH (Deployment-Imitating SWE-Agent Harness), wraps the target in an agent harness, reducing the gap between simulated and real deployment environments in coding settings. We test the techniques on multiple target models and find that they compose: applying both yields larger realism gains than either alone. Our results show that automated approaches can improve the realism of alignment evaluations, and that these improvements use additional compute more effectively than making the audits longer.

</details>

### 24. EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models

📄 [arXiv](https://arxiv.org/abs/2609.01611) · 📊 [Dataset](https://huggingface.co/datasets/el7982/aware-bench)　📅 2026-09

**关键词**：`benchmark`、`evaluation awareness`、`safety-evaluation validity`、`model-behavior shift`

👤 **作者**：Xinning Li、Kemunto Ochwang'i、Aryasomayajula Ram Bharadwaj、Alexandra Souly、Robert Kirk

- 🎯 **研究动机**：模型能识别自己正被评测（evaluation awareness），若评测与部署行为不同将破坏安全评测效度
- 🔬 **研究方法**：构建开放 pipeline 与 benchmark EvalDetectBench：兼容任意 Inspect 评测，配备 frontier system-card 评测与多来源部署 transcript 套件，并用逐模型探针校准与分层生成器调和纠正两个系统性偏差
- 📌 **结论**：部署 transcript 生成模型身份解释 11.25% 测量方差并可能重排模型排名，在某模型上调优的探针在其他模型上接近随机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier large language models can often recognize when they are being evaluated, a capability known as evaluation awareness. If models behave differently in evaluations than in deployment, this undermines the validity of evaluation results, which are a crucial component of current AI safety frameworks. We introduce EvalDetectBench, an open pipeline and benchmark for measuring evaluation awareness that works with any Inspect-compatible evaluation, allowing practitioners to test against current and future benchmarks. EvalDetectBench ships with a newly curated transcript suite covering current frontier system-card evaluations and diverse deployment sources. The benchmark serves two purposes: measuring how reliably frontier LLMs recognize that they are being evaluated, and assessing how detectable individual benchmarks are as evaluations. We identify two methodological choices in the existing literature that introduce systematic bias: the identity of the model that generated the deployment transcripts accounts for 11.25% of measurement variance and can reorder model rankings; and elicitation prompts selected for high performance on one model can perform near chance on others. EvalDetectBench corrects for both via per-model probe calibration and a stratified generator-harmonisation procedure.

</details>

### 25. Training Alignment Auditors via Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2608.25460)　📅 2026-08

**关键词**：`detection`、`analysis`、`alignment auditor`、`hidden behavior`、`cross-scaffold generalization`、`automated alignment audit`

👤 **作者**：Paul Rosu、Rowan Wang

- 🎯 **研究动机**：自动 alignment auditor 难以连贯调查隐藏行为且审计真实性不足
- 🔬 **研究方法**：以 RL 训练 auditor：目标模型经 system prompt 植入隐藏行为，LLM judge 将策略调查与参考调查对比给奖励
- 📌 **结论**：pairwise 奖励比 pointwise 稳健、假阳性率低于 1%，调查能力可跨 scaffold 迁移至 AuditBench

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistically compares the policy's investigation to a reference investigation to determine the reward. With systematic ablations, we find that pairwise rewards yield more robust training compared to pointwise rewards, and that adding targets without planted behaviors helps maintain a low false positive rate. Training improves investigation quality against targets with planted behaviors, the rate of concerning behaviors surfaced in unmodified production models, and audit realism, while false-positive rates stay below 1%. Furthermore, auditing capabilities generalize across scaffolds: performance on AuditBench's adversarially fine-tuned targets substantially improves [Sheshadri et al., 2026].

</details>

### 26. No Task Fails Every Time: Why One-Shot Audits Are Structurally Blind to Agent Damage

📄 [arXiv](https://arxiv.org/abs/2608.15286)　📅 2026-08

**关键词**：`detection`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`

👤 **作者**：Shiven Khurdi

- 🎯 **研究动机**：一次性审计对 agent 伤害结构上盲：伤害具随机性且无任务每次都失败
- 🔬 **研究方法**：AgentRelBench 环境无关可靠性工具：从数据库状态 diff 计算真值严重度定价伤害、测量路径无 LLM；2128 次评测跨 9 个模型 6 家族含预注册保留集
- 📌 **结论**：42 个确认伤害事件中零“总是失败”单元，单次干净运行漏掉致伤害配对概率 0.80；最强模型唯一伤害任务以 p=0.16 发生、单次审计漏检 84%；转录与 judge 评分会把违规误标为安全拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce AgentRelBench, an environment-agnostic reliability instrument that computes ground-truth, severity-priced damage from database state diffs across repeated runs, with no LLM in the measurement path, demonstrated on EnterpriseOps-Gym. Across 2,128 evaluation runs spanning nine models in six families (four development, three pre-registered held-out, plus a frontier pass on two frontier-tier models that the pre-registration designates exploratory), we find: (1) damage on irreversible actions is universal across the families we measured and stochastic within them on pinned, single-provider stacks. (2) No task damaged on every run: zero always-fail cells across 42 confirmatory held-out damage events. A single clean run misses a damage-producing (model, task) pair 0.80 of the time on the development pool (13 pairs); the held-out pool is descriptively consistent (0.575 over 5 pairs, pair-weighted) but sits below our pre-registered power floor and is reported as underpowered, not as confirmation. (3) Damage-producing task count falls with model capability, from 7 of 20 tasks for an 8B model to 1 of 20 for the most capable; capability is confounded with family and training, so this is an observed gradient, not a causal claim. The residual damage does not change in character: in the exploratory frontier pass, the most capable model's one damaging task damages at $\hat{p} = 0.16$ per run, inside the same demonstrably-stochastic band, and a single audit misses it 84% of the time. (4) One model family committed the gated irreversible change while declaring it had refused: transcript- and judge-based grading scores those runs as safe refusals, only state diffs as damage. All confirmatory findings were pre-registered with per-claim demote criteria; one demoted our own initially favored finding, which we report.

</details>

### 27. REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.10669)　📅 2026-08

**关键词**：`benchmark`、`adversarial robustness`、`agent safety benchmark`、`trajectory evaluation`

👤 **作者**：Zixing Chen、…、Chi Zhang

- 🎯 **研究动机**：现有评测把 agent 安全压缩为单一 ASR，混淆暴露、执行、观测与裁决，可能把实际违规与证据可见性混为一谈
- 🔬 **研究方法**：REDAgentBench 从显式安全约束派生攻击、在隔离服务沙箱执行并以服务回执与终态验证危害，含 1661 例覆盖五个服务面
- 📌 **结论**：六模型三 harness 宏观 ASR 65.69%；近五分之一确认违规发生在 agent 已陈述相关约束之后（识别-执行差距）；免训练策略提醒使确认违规降 70+ 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents combine language-based reasoning with external tools to perform complex tasks. Adversarial inputs can exploit interactions between the agent and its environment, causing the agent to violate safety policies during execution. Yet existing evaluations often reduce agent safety to a single attack success rate (ASR), collapsing exposure, execution, observation, and adjudication and potentially conflating actual violations with evidence visibility. We introduce REDAgentBench, an executable framework for autonomous red-teaming and faithful measurement. It derives attacks from explicit safety constraints and associated agent-system vulnerabilities, runs them in isolated service sandboxes, and verifies harmful effects from service receipts and final-state changes. The benchmark contains 1,661 cases across five service surfaces. Across six models and three agent harnesses, macro-average ASR is 65.69%; reported ASR varies with harness and evidence view, while evaluation-context disclosure changes execution behavior. In a state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs after the agent states the relevant constraint or risk, revealing a Recognition--Execution Gap. Finally, a training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay. These findings show that executable evaluation can improve safety measurement and identify actionable intervention points.

</details>

### 28. Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks

📄 [arXiv](https://arxiv.org/abs/2607.28685)　📅 2026-07

**关键词**：`analysis`、`benchmark validity`、`capability confounding`、`metric audit`

👤 **作者**：Youting Wang、Xiao Han、Dingyan Shang、Yuan Tang、Bowen Liu

- 🎯 **研究动机**：各 agent 安全基准分数被互换引用为统一的安全性，其测量效度从未被验证
- 🔬 **研究方法**：统一协议下对 R-Judge、InjecAgent、AgentHarm、AgentDojo 四基准跑最多 22 个模型，以自测 MMLU/GPQA 作能力对照
- 📌 **结论**：R-Judge 上全正策略 F1=0.690 即超过半数模型；能力预测任务成功（ρ=+0.60）却与错位安全负相关（ρ=-0.44），安全声明须指明基准、指标与模型面板

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent-safety benchmarks measure different behaviors, and their scores get quoted interchangeably as an agent's safety. We treat four of them (R-Judge, InjecAgent, AgentHarm, AgentDojo) as measurements to be validated, running each under its official implementation and author-provided scorer on up to 22 models, with MMLU and GPQA measured by us under one protocol as a capability composite. The metric is the first problem. On any binary trace-judgment benchmark scored by $F_1$, an ``always positive'' policy attains $F_1 = 2π/(1+π)$; on R-Judge that is $0.690$, above five of the 21 models that actually discriminate. The three broad-coverage benchmarks then rank the same 18 models differently, and the trade-off behind that disagreement is a small-panel artifact: R-Judge specificity against AgentHarm safety correlates $-0.64$ at $n{=}7$ and $+0.02$ at $n{=}18$, and a quarter of random size-7 subsets reach $|ρ| \geq 0.5$ around that near-zero value. Held-out validity turns on which outcome you pick. Capability predicts task success ($ρ{=}{+}0.60$) but correlates negatively with misalignment safety ($ρ{=}{-}0.44$, $n{=}21$). On their paired $n{=}20$ panel, the corresponding contrast is $Δ{=}{-}1.00$ (95% CI $[-1.48, -0.49]$, $p<0.001$), and it survives leave-one-organization-out and organization-clustered bootstrap analyses. On an expanded 41-model panel, the misalignment correlation weakens to $-0.16$ (95% CI $[-0.54, +0.22]$) and jailbreak strengthens to $+0.34$, though neither change is significant. \mbox{AgentHarm} shows the strongest held-out association, $ρ{=}{+}0.72$ with three-template jailbreak safety after controlling capability. But both instruments score harmful compliance, so this is evidence of convergent validity rather than general safety. Naming the benchmark, metric, target behavior, and model panel is the minimum a safety claim needs.

</details>

### 29. BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks

📄 [arXiv](https://arxiv.org/abs/2604.24955)　📅 2026-04

**关键词**：`benchmark`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`

👤 **作者**：Xinming Tu、…、Sara Mostafavi

- 🎯 **研究动机**：复杂基准中许多 agent 失败实为基准自身失败（规范破损、隐式假设、僵化评估脚本），缺系统审计手段
- 🔬 **研究方法**：BenchGuard 以前沿 LLM 为审计员，通过结构化协议交叉核验基准工件，可引入 agent 解法或执行轨迹作诊断证据
- 📌 **结论**：在 ScienceAgentBench 发现 12 个作者确认问题（含致命不可解任务），BIXBench Verified-50 上匹配 83.3% 专家问题，50 个任务完整审计成本低于 15 美元

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As benchmarks grow in complexity, many apparent agent failures are not failures of the agent at all - they are failures of the benchmark itself: broken specifications, implicit assumptions, and rigid evaluation scripts that penalize valid alternative approaches. We propose employing frontier LLMs as systematic auditors of evaluation infrastructure, and realize this vision through BenchGuard, the first automated auditing framework for task-oriented, execution-based agent benchmarks. BenchGuard cross-verifies all benchmark artifacts via structured LLM protocols, optionally incorporating agent solutions or execution traces as additional diagnostic evidence. Deployed on two prominent scientific benchmarks, BenchGuard identified 12 author-confirmed issues in ScienceAgentBench - including fatal errors rendering tasks unsolvable - and exactly matched 83.3% of expert-identified issues on the BIXBench Verified-50 subset, catching defects that prior human review missed entirely. A full audit of 50 complex bioinformatics tasks costs under USD 15, making automated benchmark auditing a practical and valuable complement to human review. These findings point toward AI-assisted benchmark development, where frontier models serve not only as subjects of evaluation but as active participants in validating the evaluation infrastructure itself.

</details>

### 30. ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm

📄 [arXiv](https://arxiv.org/abs/2607.10455) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63234)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`benchmark`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`、`agent safety`

👤 **作者**：Kefan Song、Yanjun Qi

- 🎯 **研究动机**：自主 CLI agent 可在数小时会话中执行数百个动作，现有对齐审计未覆盖持续恶意用户场景
- 🔬 **研究方法**：ANCHOR 基于美国法院真实案件构建非法任务，用暗黑人格数据经监督与强化微调的 auditor agent 扮演持续恶意用户：分解任务、被拒后重构请求并跨轮适应策略
- 📌 **结论**：前沿 CLI agent 直接询问时常拒绝非法任务，但持续恶意交互下合规率达 100%，且常超出请求自主搭建大规模伤害基础设施（如金融欺诈与生物武器开发）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous CLI agents can now execute hundreds of actions across multi-hour sessions: writing code, executing shell commands, browsing the web, and managing cloud infrastructure, all with minimal human oversight. Does greater autonomy invite greater risk? We introduce ANCHOR, an automated auditing framework that stress-tests CLI agents on illegal tasks grounded in public US court cases. ANCHOR deploys an auditor agent fine-tuned on dark personality data using supervised and reinforcement fine tuning. This auditor roleplays persistent malicious users who decompose tasks, reframe requests upon refusal, and adapt strategies across multi-turn interactions. Evaluating frontier CLI agents, we find that while they often refuse illegal tasks when prompted directly, compliance reaches 100\% under persistent malicious interaction. When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development. These findings demonstrate that current alignment techniques are insufficient for autonomous agents and underscore the need for safety evaluations against persistent, adaptive malicious users.

</details>

### 31. KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.03588)　📅 2026-09

**关键词**：`benchmark`、`knowledge conflict`、`stateful tools`、`protected-data flow`、`conflict-aware action`、`stateful tool`

👤 **作者**：Yaxing Lyu、Shengjie Zhou、Binbin Toh、Pengyu Zhu、Lijun Li

- 🎯 **研究动机**：工具型 LLM Agent 须在行动前协调用户指令、参数知识与动态环境观察，该冲突协调能力缺少可控多轮测试
- 🔬 **研究方法**：构建 KC-Bench：238 个从千余候选人工筛出的任务，组合用户模拟器、有状态工具、确定性环境断言、开源评测器与人工轨迹核验，覆盖世界知识冲突、输入不一致与多源时序冲突
- 📌 **结论**：九个模型（含 DeepSeek-V4-Flash、GLM-5.2、MiniMax-M3）跨域差异大，无一能可靠处理事实纠正、身份一致性与时序冲突；漏检冲突会传播到工具调用与合成 protected-data flow

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs increasingly act through tools, they must reconcile user instructions, parametric knowledge, and dynamic environmental observations before taking actions. We introduce KC-Bench, a controlled multi-turn benchmark for measuring this capability across world-knowledge conflicts, input inconsistencies, and multi-source temporal conflicts. Its 238 tasks are manually screened from more than 1,000 generated candidates and combine a user simulator, stateful tools, deterministic environment assertions, an open-source natural-language evaluator, and human trajectory verification. Evaluation of nine models, including DeepSeek-V4-Flash, GLM-5.2, and MiniMax-M3, shows substantial cross-domain variation: no model handles factual correction, identity consistency checking, and temporal conflict resolution reliably across all settings. In the simulated environments, missed conflicts can propagate to tool calls or synthetic protected-data flows. KC-Bench isolates this model-level behavior rather than ranking complete agent frameworks, and provides a reproducible diagnostic for developing conflict-aware reasoning and execution safeguards.

</details>

### 32. Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling

📄 [arXiv](https://arxiv.org/abs/2609.00949)　📅 2026-09

**关键词**：`benchmark`、`tool-calling calibration`、`action-class diagnosis`、`multi-turn safety`

👤 **作者**：Kangjia Zhao、…、Jianwei Yin

- 🎯 **研究动机**：多轮工具调用的聚合精度掩盖了模型是选错动作类别还是执行工具失败
- 🔬 **研究方法**：提出四类动作空间（TOOL_CALL／ASK／REFUSE／CONFIRM）的诊断框架，用自暴露上界 Acc<=GAR 把失效拆为动作类错配（违反上界）与执行失败（上界余量大）
- 📌 **结论**：state grader 看不见的动作类错配是重要失效模式，会抬高重度工具训练家族的排名；上下文扰动对不同家族产生相反效果（+11.5 vs -21.0pp）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn tool calling is a core evaluation scenario for large language model (LLM) agents. On public tool-calling benchmarks, open-weight models now approach or even surpass closed-source frontier models in aggregate accuracy. However, this metric averages over many different multi-turn situations and obscures whether progress is balanced across them. We propose an action-class-oriented diagnostic framework that decomposes multi-turn failures into two orthogonal modes: action-class miscalibration and action-execution failure. The framework operates over a four-class action space (TOOL_CALL/ASK/REFUSE/CONFIRM) and introduces a self-revealing upper bound Acc <= GAR (Gold Action Recall); the two modes show up as bound violation (Acc > GAR, exposing state-grader masking of miscalibration) and large bound slack (GAR >> Acc, localizing execution failure within TOOL_CALL). We validate it on a panel of tool-calling models across multiple multi-turn benchmarks. Across our panel, the diagnostic reveals action-class miscalibration as a substantial failure mode the state grader cannot see. This gap inflates standing for heavily tool-trained families, which our diagnostic separates from families with context-appropriate action choice. Calibration is reshapable through context-only perturbations, but the reshape is heterogeneous: a single perturbation moves accuracy in opposite directions across families (up to +11.5 vs -21.0 pp on the same scenario), and its effect further depends on the perturbation mechanism. We argue that multi-turn tool-calling evaluations should supplement aggregate accuracy with action-class diagnostics that expose what the model actually does in each scenario.

</details>

### 33. The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions

📄 [arXiv](https://arxiv.org/abs/2608.27009)　📅 2026-08

**关键词**：`benchmark`、`over-safety validity`、`mechanical labeling`、`twin contrast`、`agent guardrail`、`over-refusal`

👤 **作者**：Yingjie Zhang、Yuanbo Xie、Kai Chen

- 🎯 **研究动机**：Agent guardrail 的 over-safety 难以评测：授权边界处动作彼此相似，安全标签取决于授权策略而非动作本身，真实数据难以收集与验证
- 🔬 **研究方法**：构建 Cautious Bench，将每个样本与显式授权策略共同设计，构建时门机制使标签成为策略的机械推论，含 756 个 benign/twin 对（三种对象名共 2268 对）与 40 个 Undecidable 对
- 📌 **结论**：实测五类设计的六个 guardrail 均现名称迷信效应：仅把对象名换成危险措辞就更频繁拒绝合法动作，说明其依赖表面名称而非授权上下文

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one that maps the decision boundary of an ideal guardrail. Harvesting such a benchmark from real data is impractical: boundary cases are hard to collect, their labels hard to verify. The gap is real, so we construct Cautious Bench, the first benchmark to make over-safety the construct for agent guardrails; it codesigns each sample and its label with a stated authorization policy. A build-time gate re-derives every example to certify it, so each label is a mechanical consequence of the policy rather than an annotator's per-sample verdict, a reference against which researchers can measure real guardrails. The benchmark renders 756 Decidable benign/twin pairs, each under three object-name types (2,268 measured pairs), and 40 Undecidable pairs reported separately. Measuring six guardrails from five designs, we find a name-superstition effect: each over-refuses an authorized action more often under a scary-looking object name than a benign one. Since only the object name varies in the aforementioned contrast experiments, the deviation is the name's doing: the guardrails read the surface label, not the authorization context.

</details>

### 34. Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks

📄 [arXiv](https://arxiv.org/abs/2608.22103) · 🌐 [Project](https://majoroth.github.io/hack-verifiable-environments/hvtb)　📅 2026-08

**关键词**：`benchmark`、`agent evaluation`、`verifiable scorer`、`unknown exploit`、`coding agent`、`reward hacking`

👤 **作者**：Amit Roth、Ivan Bercovich、Yonathan Efroni

- 🎯 **研究动机**：agent 的 reward hacking（满足任务检查却违背意图）日益重要，但检测依赖人工检查或不可靠的 LLM judge
- 🔬 **研究方法**：把 hack-verifiable environments 方法移植到 Terminal Bench 形成 HVTB：在真实终端与编码任务中嵌入可检测 hack 使作弊可自动可靠识别，并用含不同 hack 信息量的 prompt 测试缓解效果
- 📌 **结论**：可测量前沿模型的 reward hacking 率，并区分 prompting 防御只对已知策略有效还是能泛化到 unknown unknown exploit

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agents grow more capable and autonomous, their tendency to reward hack, satisfying a task's checks while violating its intent, becomes an increasingly important failure mode. Measuring reward hacking is itself challenging, as detection typically relies on human inspection or LLM judges, both of which can be unreliable. The hack-verifiable environments (HVE) methodology addresses this challenge by embedding detectable hacks into tasks, allowing reward hacks to be identified automatically and reliably. In this work, we adapt HVE to Terminal Bench, a leading benchmark of real-world terminal and coding tasks, and introduce Hack-Verifiable Terminal Bench (HVTB). Using HVTB, we measure reward-hacking rates across frontier models and study whether prompts with varying amounts of information on the hack can mitigate this behavior. This lets us test whether prompting can prevent not only known reward-hacking strategies, but also 'unknown unknown' exploits that the prompt does not anticipate. We release all environments and agent traces at https://majoroth.github.io/hack-verifiable-environments/hvtb

</details>

### 35. FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs

📄 [arXiv](https://arxiv.org/abs/2608.25158)　📅 2026-08

**关键词**：`benchmark`、`executable environment`、`sanitizer feedback`、`coverage-aware scoring`、`coding agent`、`open-ended fuzzing`

👤 **作者**：Ze Sheng、Aleksandar Kezic、Zhicheng Chen、Jeff Huang

- 🎯 **研究动机**：现有 bug 发现 benchmark 只认预定义目标漏洞，漏计模型发现的其他合法 crash
- 🔬 **研究方法**：FuzzingBrain-Bench 给模型开源项目与 sanitizer 插桩 harness，按不同 crash 签名数加权计分，含 43 个项目 77 道题
- 📌 **结论**：Claude Opus 4.8 最佳：77 题中 60 题触发 crash，得分 196/579

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the ability of large language models (LLMs) to discover software bugs is increasingly important. Existing benchmarks typically evaluate this capability by asking the model to generate a proof-of-concept input that triggers a predefined target vulnerability. However, this setup may overlook valid crashes discovered by the model when they do not match the predefined target. As a result, the evaluation may not reflect the model's real capability. We present FuzzingBrain-Bench, a benchmark for assessing AI models' ability to discover bugs in open-source software. Models are given an open-source project and a sanitizer-instrumented harness in a self-contained Docker image. Their goal is to generate inputs that trigger as many distinct crashes as possible through the harness. A model's performance on each challenge is scored based on the number of distinct crash signatures it produces, capped at a predefined maximum and weighted by a difficulty coefficient. FuzzingBrain-Bench V1 consists of 77 challenges drawn from 43 open-source projects, with 36 C, 32 C++, and 9 Java/JVM challenges. We evaluate Claude Haiku 4.5, Claude Sonnet 4.6, and Claude Opus 4.8 on the full benchmark. Claude Opus 4.8 performs best, triggering crashes in 60 of 77 challenges and achieving a score of 196 out of 579. None of the three models triggers a crash in 13 challenges. The FuzzingBrain-Bench corpus and harnesses are publicly available at https://github.com/fuzzingbrain/FuzzingBrain-Bench.

</details>

### 36. CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild

📄 [arXiv](https://arxiv.org/abs/2608.23181)　📅 2026-08

**关键词**：`tool`、`executable cyber instance`、`agentic trajectory`、`evidence-based validation`、`cyber agent`、`PoC generation`

👤 **作者**：Jian Yang、…、Weifeng Lv

- 🎯 **研究动机**：开源网络安全 LLM 训练缺乏可复现方案：前沿开源权重不提供训练方法，已有方案聚焦孤立任务、缺规模化 agentic 数据
- 🔬 **研究方法**：CyberFactory 统一框架连接数据构建、轨迹合成与模型训练，覆盖 PoC 生成、漏洞修补与 CyberQA；从真实 CVE 构造仓库级可执行任务，用可复用分析 skill 引导源码检查并按执行反馈迭代修订，训练出内化 skill 的 Aegis 模型
- 📌 **结论**：CyberGym 一小时预算下 Pass@1 达 52.4%，比 Qwen 3.5 基座高 22.8 分，超过同 scaffold 的通用 backbone

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts requires strong domain priors. In this work, we introduce \textbf{CyberFactory}, a unified open-source framework that connects data construction, trajectory synthesis, and model training across proof-of-concept (PoC) generation, vulnerability patching, and cybersecurity question answering (CyberQA). CyberFactory transforms public vulnerability artifacts, including CVEs from the wild, into executable and verifiable task instances. It further uses a reusable vulnerability-analysis skill to guide the teacher through source inspection, problem solving with domain prior, and evidence-based validation. The resulting supervision is agentic: the model interacts with tools and target environments and revises its solutions according to execution feedback. Using these trajectories, we train and release \modelname\footnote{\emph{Aegis} is, in Greek mythology, the protective shield of Zeus and Athena; the name reflects the model's defensive, security-oriented purpose.}, which internalizes the skill-guided procedure without requiring the skill at inference time. On CyberGym, \modelname reaches 52.4% Pass@1 under a one-hour budget, improving over its Qwen~3.5 base model by +22.8 points and outperforming the evaluated general-purpose backbones under the same scaffold.

</details>

### 37. Helpful to a Fault: Measuring Illicit Assistance in Multi-Turn, Multilingual LLM Agents

📄 [arXiv](https://arxiv.org/abs/2602.16346) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61155)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`tool-use agent`、`tool interface`、`action integrity`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Nivya Talokar、Ayush K Tarun、Murari Mandal、Maksym Andriushchenko、Antoine Bosselut

- 🎯 **研究动机**：现有智能体滥用基准只测单轮指令，未测多轮中智能体如何被逐步引导协助非法任务
- 🔬 **研究方法**：STING 以良性 persona 构造逐步非法计划并自适应追问，judge 智能体追踪阶段完成；把多轮红队建模为 time-to-first-jailbreak 随机变量并提出 Restricted Mean Jailbreak Discovery 指标
- 📌 **结论**：AgentHarm 场景非法任务完成率显著高于单轮与对话式多轮基线；六种非英语语言中攻击成功率并不随语言资源降低而上升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents execute real-world workflows via tools. These affordances enable ill-intended adversaries to also use these agents to carry out complex misuse scenarios. Existing agent-misuse benchmarks largely test single-prompt instructions, leaving a gap in measuring how agents end up helping with harmful or illegal tasks over multiple turns. We introduce STING ( Sequential Testing of Illicit N-step Goal execution ), an automated red-teaming framework that constructs a step-by-step illicit plan grounded in a benign persona and iteratively probes a target agent with adaptive follow-ups, using judge agents to track phase completion. We further introduce an analysis framework that models multi-turn red-teaming as a time-to-first-jailbreak random variable, enabling analysis tools like discovery curves, hazard-ratio attribution by attack language, and a new metric: Restricted Mean Jailbreak Discovery. Across AgentHarm scenarios, STING yields substantially higher illicit-task completion than single-turn prompting and chat-oriented multi-turn baselines adapted to tool-using agents. In multilingual evaluations across six non-English settings, we find that attack success and illicit-task completion do not consistently increase in lower-resource languages, diverging from common chatbot findings. Overall, STING provides a practical way to evaluate and stress-test agent misuse in realistic deployment settings, where interactions are inherently multi-turn and often multilingual. Our code is available at https://github.com/epfl-nlp/helpful-to-a-fault.

</details>

### 38. AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories

📄 [arXiv](https://arxiv.org/abs/2609.06972)　📅 2026-09

**关键词**：`benchmark`、`indirect prompt injection`、`trajectory labeling`、`agent guard`

👤 **作者**：Asif Pinjari、Mithun Paul Saint-Germain

- 🎯 **研究动机**：注入劫持检测缺逐步标注语料，整轨迹 guard 无法定位注入点与被劫持步骤
- 🔬 **研究方法**：AgentDrift：12,536 条合成工具调用轨迹、71,024 步四类标签（benign/注入点/被劫持/失败注入），含 hard negative 与正则语法约束
- 📌 **结论**：表面特征逻辑回归仅检出 55.4%（partial hijack 8.2%），近半攻击需行为序列建模；LLM judge 也被 hard negative 欺骗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents complete tasks by issuing sequences of tool calls, and every observation they read is a channel through which an indirect prompt injection can enter. A successful injection has a characteristic shape when the trajectory is read in order: a benign prefix gives way to actions that serve the attacker rather than the user. Existing benchmarks measure whether such attacks succeed against live agents, and existing guard models judge a trace as a whole; no public corpus labels, step by step, where an injection enters a trajectory and which steps it corrupts. We present AgentDrift, a benchmark of 12,536 synthetic tool-call trajectories over five agent domains in which every one of the 71,024 steps carries one of four labels: benign, injection point, hijacked, or failed injection. The corpus contains 4,000 benign, 5,536 attacked, 1,500 failed-attack, and 1,500 hard-negative trajectories; attacked trajectories follow three compliance patterns whose label strings obey a stated regular grammar. Failed attacks carry an injection the agent resisted, and hard negatives carry legitimate content that resembles an attack, so a detector must separate attempt from success and deviation from novelty. Trajectories were generated by a single open model under category-specific protocols, enforced by a closed-vocabulary structural validator, screened by an LLM judge, and audited by hand on 1,200 trajectories; we show that the LLM judge was itself fooled by the hard negatives. A surface-feature logistic regression recovers only 55.4% of attacks (F1 0.647), including only 8.2% of partial hijacks and 23.1% of delayed executions, so nearly half of the attacks require modeling the behavioral sequence. We measure template concentration, attack-goal-family collapse, and world-identity leakage in the generated data, and release the corpus with its documentation under CC BY 4.0.

</details>

### 39. An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks

📄 [arXiv](https://arxiv.org/abs/2609.09404)　📅 2026-09

**关键词**：`benchmark`、`multimodal prompt injection`、`agentic framework`、`attack propagation`、`audio channel`

👤 **作者**：Viet K. Nguyen、Mohammad I. Husain

- 🎯 **研究动机**：agent 读图给攻击者绕过用户向上下文注入指令的通道，缺可复现的多模态注入评测
- 🔬 **研究方法**：MMPIBench：6 种视觉载体（OCR/叠加/EXIF/二维码/假界面/混合）× 6 框架 × 5 模型共 720 次，追踪指令从感知到工具调用的传播并扩展音频通道
- 📌 **结论**：攻击完成约 1% 但尝试 12.8%，差距几乎全在规划步被拦截；音频通道到达处完成率 49%（单模型 75%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user. We present MMPIBench, a reproducible benchmark that measures what happens next. It delivers a fixed set of attacks through six visual carriers (OCR text, overlays, EXIF metadata, QR codes, fake interfaces, and hybrids) and records how far each injected instruction travels through the agent, from perception through planning to the tool call. Across 720 runs covering six frameworks, five foundation models, six carriers, and four attacker objectives, attacks complete in approximately 1% of runs but are attempted in 12.8%, and the gap is closed almost entirely at the planning step, where the model reads the injected instruction and declines to act on it. The model matters far more than the framework for whether an instruction is acted on. One model never attempts an attack and recognizes the injection in 59.7% of runs, while two others attempt in 23.6%. We then extend the benchmark to audio, the only other raw perceptual channel current frontier models accept. Only two of the five models ingest audio and only three of the six frameworks deliver it, but where the signal arrives the attack completes in 49% of cells, and in 75% for one model. Reporting completion alone therefore understates exposure, and perceptual channels beyond vision are narrower but much less defended.

</details>

### 40. Black-Box Red Teaming of Agentic AI: A Taxonomy-Driven Framework for Automated Risk Discovery

📄 [arXiv](https://arxiv.org/abs/2609.09647)　📅 2026-09

**关键词**：`benchmark`、`agent red teaming`、`black-box risk discovery`、`taxonomy`

👤 **作者**：Divyanshu Kumar、Nitin Aravind Birur、Tanay Baswa、Sahil Agarwal、Prashanth Harshangi

- 🎯 **研究动机**：单轮评测无法覆盖生产 agent 的多步漏洞，缺黑盒自动化风险发现框架
- 🔬 **研究方法**：七域风险 taxonomy + SAGE-RT 自动红队（每域 120 对抗场景）+ LLM judge 人审，评测 CrewAI/AutoGen × 4 基座
- 📌 **结论**：平均治理风险 56.25%、多智能体配置隐私风险 65%、行为漏洞达 85%，无需特权访问即可发现架构级漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic systems are rapidly moving to production, where they read untrusted inputs, call tools with real permissions, and act autonomously, expanding the security surface beyond chat-only models. Yet standard evaluations remain single-turn and fail to capture multi-step agent vulnerabilities. We present a systematic black-box framework for risk-aware agent evaluation requiring only basic system descriptions. Our approach introduces: (1) a seven-domain taxonomy mapping observable behaviors to risk categories, (2) fully automated SAGE-RT red teaming producing 120 adversarial scenarios per domain, and (3) human-validated evaluation using LLM judges. Empirical validation across two agent architectures (CrewAI and AutoGen) with four base models reveals alarming patterns: 56.25\% average governance risk, 65\% privacy risk in multi-agent configurations, and agent behavior vulnerabilities reaching 85\%. Our black-box approach effectively identifies critical architectural vulnerabilities without privileged access, providing a scalable path toward safer agent deployments.

</details>

### 41. LexAgentHallu: A Hierarchical Benchmark for Profiling Hallucinations in Legal Agents

📄 [arXiv](https://arxiv.org/abs/2609.09754)　📅 2026-09

**关键词**：`benchmark`、`agentic hallucination`、`legal agent`、`trajectory diagnosis`

👤 **作者**：Yujin Zhou、…、Sirui Han

- 🎯 **研究动机**：法律 agent 的工具调用与推理错误会级联成伪造判例，现有基准只有单轮结果级指标
- 🔬 **研究方法**：LexAgentHallu：专家四阶段管线构建 3,414 实例 × 17 法律类 × 6 任务，双层 7+27 幻觉 taxonomy 与轨迹定位指标，评测 18 个 agent
- 📌 **结论**：发现 Right-Answer-Wrong-Reason 效应；幻觉子类聚集成框架/任务/类别画像，结果级评测不可见

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models are increasingly deployed as tool-augmented legal agents, they introduce agentic hallucinations where tool-call and reasoning errors cascade into fabricated holdings and miscited authority. However, existing legal benchmarks evaluate only single-turn QA with outcome-level metrics, while agentic hallucination benchmarks lack legal-specific diagnostic capability. Neither answers to what extent and how a legal agent hallucinates along its trajectory. To address these limitations, we introduce LexAgentHallu, a legal agentic hallucination benchmark designed to evaluate to what extent and how legal agents fail along multi-step trajectories. Built through a four-stage expert-in-the-loop pipeline, LexAgentHallu contains 3414 instances across 17 legal categories and 6 task types. Each instance is annotated under a dual-layer hallucination taxonomy of 7 high-level categories and 27 fine-grained subclasses, covering both substantive errors and agent-procedural failures. We further design fine-grained metrics that quantify to what extent and localize how each failure occurs along an agent's execution path. Our evaluation across 18 proprietary and open-source agents uncovers a Right-Answer-Wrong-Reason effect and reveals that hallucination subclasses cluster rather than scatter, forming distinct agentic framework, legal task, and category profiles. These findings, invisible to outcome-level evaluation, validate the diagnostic power of LexAgentHallu for evaluating agentic hallucination in law.

</details>

### 42. DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows

📄 [arXiv](https://arxiv.org/abs/2608.26546)　📅 2026-08

**关键词**：`benchmark`、`real-session benchmark`、`production agent`、`environmental complexity`、`capability coordination`

👤 **作者**：Zechun Niu、…（生产 agent 平台团队）

- 🎯 **研究动机**：自主 agent 越来越多地承担真实多工具工作流，但现有 benchmark 按应用或能力分任务、在比实践更干净稳定的环境中评测，无法反映生产就绪度。
- 🔬 **研究方法**：DuMateBench 从大规模生产 agent 平台的匿名化脱敏用户会话重建任务：保留求解前交互历史、持久配置与工作区状态并经人工验证；200 个任务覆盖 8 场景、17 细粒度能力类，多数需多能力协调；在隔离 Docker 容器中注入 Insufficient/Unstable/Noisy 三种真实环境复杂性，用确定性+LLM-as-Judge 混合协议评分；5 个自主 agent 框架 × 4 个 SOTA LLM 实验。
- 📌 **结论**：真实条件下性能显著退化、能力协调缺口巨大——为 agent 生产部署就绪度提供更忠实的度量。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous agents are increasingly adopted to complete complex, multi-tool workflows in real-world settings. However, existing benchmarks typically separate tasks by application or capability and evaluate agents in environments that are cleaner and more stable than those encountered in practice. We introduce DuMateBench, a real-session benchmark reconstructed from anonymized and privacy-screened user sessions collected from a large-scale production agent platform. Each task preserves the relevant pre-solution interaction history, persistent configurations, and workspace state, and is then validated through human verification. The resulting benchmark comprises 200 tasks spanning 8 broad scenarios and 17 fine-grained capability categories, with most tasks requiring multiple capability coordination. We execute these tasks in isolated Docker containers injected with three forms of real-world environmental complexity: Insufficient, Unstable, and Noisy, and assess performance using a hybrid deterministic and LLM-as-Judge evaluation protocol. Experiments across five representative autonomous-agent frameworks paired with four state-of-the-art LLMs reveal substantial performance degradation under realistic conditions and large capability-coordination gaps, offering a more faithful measure of agent readiness for production deployment.

</details>
