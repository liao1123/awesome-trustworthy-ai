# Policy-Adaptive Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究把自然语言 policy、用户规则、平台规范或法规作为 guardrail 的显式输入，使审核标准可以在推理时变化，而不必为每套 taxonomy 重新训练模型。核心问题包括未见规则的组合泛化、复杂 policy 的逐条执行、reasoning 与最终 label 的一致性、低延迟部署，以及从合成数据、用户反馈和历史事件中持续更新规则。

## 研究脉络

- **固定 taxonomy 到可变 policy：** 研究从预定义 harm category 的二分类器转向把 policy 本身作为条件，要求同一内容在不同规则和严格度下得到不同判断。
- **Policy reasoning：** GSPR、DynaGuard 等工作用 reasoning trace、SFT 或 RL 学习逐条执行未见规则，PL-Guard 则把 neural grounding 与 ProbLog policy inference 分离，使规则依据和 safety-helpfulness trade-off 可审计。
- **效率与一致性：** LPG、ConsisGuard 和 FlexGuard 分别探索 latent reasoning、deliberation-enforcement 对齐和连续风险分数，降低动态规则带来的延迟与决策不稳定。
- **持续适应、个性化与工作流：** LiSA 将事故反馈归纳为可更新 memory，个性化审核把 policy boundary 下沉到用户 sensitivity profile，PolicyGuide 则把判断对象从单次 action 扩展到完整 Agent workflow。
- **评测边界：** SafePyramid、GMP 与 PluRule 开始覆盖层级规则、组合违规、社区差异、多轮上下文和 policy conflict；policy invariance 研究进一步要求 judge 区分真正的规范变化与语义等价改写。

## 动态 Policy 执行与适应

### 1. Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers

📄 [arXiv](https://arxiv.org/abs/2608.14089)　📅 2026-08

**关键词**：`detection`、`defense`、`safety-classifier adaptation`、`policy mismatch`、`drift monitoring`、`classifier adaptation`

👤 **作者**：Thiago Sandoval、Ufuk Topcu

- 🎯 **研究动机**：安全分类器决策反映训练学到的策略而非部署者策略，且随部署流量演化而退化
- 🔬 **研究方法**：RCV 轻量包装器从分类器内部表征估计每个预测与部署者策略不一致的概率并选择性纠正；同一估计提供无标签分布漂移检测
- 📌 **结论**：三个现成分类器×两基准全部改善策略遵循，不改分类器补上至多 0.81 此前漏检的不安全内容；十次保留攻击战役全部检出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees with the deployer's policy, and selectively corrects predictions likely to be wrong. The same correctness estimates also provide a label-free signal for detecting distribution shift, enabling a maintenance loop that updates the correctness estimation layer and resorts to classifier fine-tuning only when necessary. Across three off-the-shelf safety classifiers and two benchmark datasets, RCV improves adherence to the deployer's policy in every classifier-dataset combination, catching up to 0.81 of previously missed unsafe content without modifying the underlying classifier. In a deployment study with ten attack campaigns, each a harm category held out of RCV's training, RCV detects every campaign in a dedicated injection panel; in the maintenance census most drift episodes are repaired without updating the classifier, and the fine-tune is reserved for the residual episodes that repair does not restore.

</details>

### 2. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

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

### 3. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

📄 [arXiv](https://arxiv.org/abs/2608.27548) · 🤗 [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · 📊 [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset)　📅 2026-08

**关键词**：`tool`、`compact guard model`、`prompt-response moderation`、`production deployment`、`multimodal moderator`、`image-conditioned safety`

👤 **作者**：Varun Singh、Anuj Doshi、Makesh Narsimhan Sreedhar、Shaona Ghosh、Katherine Luna

- 🎯 **研究动机**：部署场景的安全审核需覆盖图像、文档、生成回答与各域自定义策略，现有 guardrail 通常只覆盖部分设置，难以兼顾广覆盖、自定义策略与低算力
- 🔬 **研究方法**：发布 4B 视觉语言安全 moderator Nemotron 3.5 CS 及多模态多语言安全数据集，联合分类 12 种语言的 prompt、图像与回答；低延迟路径仅输出标签，按需生成应用自定义策略并指认违规类别的推理轨迹
- 📌 **结论**：在多模态安全、文本审核、跨语言鲁棒性、自定义策略遵循、良性误报与延迟评测中取得实用的覆盖—成本权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

</details>

### 4. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

📄 [arXiv](https://arxiv.org/abs/2608.27234)　📅 2026-08

**关键词**：`defense`、`plan-first guardrail`、`information-flow control`、`persistent agent`、`plan-first runtime`、`information-flow contract`

👤 **作者**：Dylan Girrens、Guangjing Wang

- 🎯 **研究动机**：持久 LLM Agent 面临攻击者数据经持久状态污染控制流与后续查询的威胁，现有防御只保护规划或单次工具交互
- 🔬 **研究方法**：提出 plan-first 架构 SPA：每查询一次生成 DSL 完整计划，对显式数据流与控制依赖施加 dual-lattice 信息流控制，执行结果存为带标签 artifact，后续规划只暴露语义元数据
- 📌 **结论**：在 AgentDojo 上将 tool_knowledge 攻击成功率降至 0，在自建多查询扩展 AgentDojo-MQ 上降至 0.2%，同时揭示严格完整性约束的安全—效用权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly operate over untrusted webpages, documents, tools, and persistent states while exercising authority over security-sensitive resources. Existing defenses typically protect either planning or individual tool interactions, but persistent agents face a broader threat: attacker-controlled data can alter control flow, enter security-sensitive tool arguments, or compromise later queries. We present SPA, a plan-first architecture that secures planning, execution, and cross-query state reuse. SPA invokes the planner once per query to generate a complete executable plan in a declarative domain-specific language, then applies dual-lattice information-flow control to track confidentiality and integrity across explicit data flows and control dependencies. To support persistence without re-exposing untrusted payloads to the planner, SPA stores execution results as labeled artifacts and reveals only semantic metadata during later planning. We evaluate SPA on AgentDojo and AgentDojo-MQ, which is our multi-query extension for measuring secure state reuse and delayed attacks. Under the 'tool_knowledge' attack, SPA with information-flow control reduces attack success to zero on AgentDojo and 0.2% on AgentDojo-MQ. Our results show that plan-first execution combined with label-preserving persistence can substantially strengthen persistent LLM agents, while revealing an important security-utility tradeoff introduced by strict integrity enforcement.

</details>

### 5. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2608.26008)　📅 2026-08

**关键词**：`defense`、`cross-interaction memory`、`failure abstraction`、`self-evolving safeguard`、`adaptive jailbreak guard`、`persistent rule memory`

👤 **作者**：Tongyan Hu、Bryan Hooi

- 🎯 **研究动机**：静态 jailbreak 防御无法积累经验或适应新出现的攻击 wrapper
- 🔬 **研究方法**：把成功攻击抽象为 method-level rule 写入持久跨交互记忆，测试时复用与扩展，无参数更新
- 📌 **结论**：四个黑盒攻击家族上 ASR 显著下降，自适应组合 wrapper 下稳健且不增加过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have proliferated in an ongoing cat-and-mouse game, yet most remain static: their safety behavior is fixed at deployment, so they cannot accumulate defensive experience or adapt to unseen strategies. We propose a self-evolving test-time defense built around a persistent, cross-interaction rule memory: when an attack succeeds, the framework abstracts that failure into a method-level rule capturing the structural attack wrapper rather than the harmful topic, and reuses it against future inputs. Because rules are method-level, one induced rule generalizes across an entire attack family, and the label space expands as novel wrappers appear. The mechanism operates entirely through external memory and prompting, with no parameter updates, and applies to both open-weight and black-box API models. We realize it as four cooperating modules, but the contribution is the memory-based adaptation mechanism, not the module decomposition. Across four black-box jailbreak families and multiple models, our method substantially reduces attack success rates while preserving benign utility, remains robust under an adaptive composite-wrapper attack, and does not increase over-refusal as the memory grows.

</details>

### 6. LMSM: LLM Security Framework Inspired by Linux Security Modules

📄 [arXiv](https://arxiv.org/abs/2608.25697)　📅 2026-08

**关键词**：`defense`、`tool`、`security backend`、`runtime enforcement`、`production guard architecture`、`versioned policy`

👤 **作者**：XiuYu Zhang、Bonan Ruan、Junfeng Fang、An Zhang、Tat-Seng Chua、Zhenkai Liang

- 🎯 **研究动机**：模型内部安全信号各自绑定校准、策略与干预代码，无法汇成统一运行时防御
- 🔬 **研究方法**：LMSM 借鉴 Linux Security Modules：分离校准证据 backend、版本化 policy 与输出授权 gate，适配 Transformers 与 vLLM
- 📌 **结论**：Qwen3-4B 上 HarmBench ASR 从 39.20% 降至 3.32%（误拒仅增 2 个点），32 活跃序列下保留 98.14% 吞吐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a shared defense. We present Language Model Security Modules (LMSM), a security framework that adapts the separation behind Linux Security Modules (LSM) to LLM serving. In LMSM, a selected security backend exposes calibrated evidence, a versioned policy evaluates active rules over trusted per-request context, and a separate gate authorizes buffered output release. This design separates mediation correctness from policy effectiveness, and it allows backend, rule, or schedule changes without rebuilding request handling or enforcement. Our prototype shows the separation working in practice: with Hugging Face Transformers and continuously batched vLLM, the same substrate hosts artifact-backed sparse autoencoder (SAE) and transcoder deployments and task-fitted dense probes, preserves request-specific decisions under scheduler churn, and selectively enforces and composes multiple rules per request. On Qwen3-4B, LMSM-Checkpoint reduces HarmBench attack success rate from 39.20% to 3.32%, with XSTest false refusals rising from 2.40% to 4.40%, while retaining 98.14% of the throughput of a matched serving path that performs no monitoring work at 32 active sequences. LMSM gives advances in interpretability and model-internal analysis a common path to runtime enforcement.

</details>

### 7. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.22868)　📅 2026-08

**关键词**：`defense`、`flow-centric policy`、`runtime enforcement`、`prompt injection`、`runtime reference monitor`、`stateful taint`

👤 **作者**：Basavesh Ammanaghatta Shivakumar、Swarn Priya、Peng Gao

- 🎯 **研究动机**：LLM agent 的伤害常来自敏感数据跨多个看似合理步骤的流动而非单个不安全动作，现有防御只约束单次调用
- 🔬 **研究方法**：AgentFlow 流中心策略语言与运行时执行模型：策略定义在带标签的运行时边上，约束哪些工具可收敏感字段、哪些 sink 可接收释放数据、何种权限可跨委托边界，支持 flow/path 规则、task-scoped capability 与有状态 taint 语义，由 reference monitor 仲裁并经有界 SMT 验证
- 📌 **结论**：949 个 AgentDojo 注入案例确认攻陷从 33.0% 降至 0.0% 且效用从 46.7% 升至 63.3%；AgentDyn 上 73.5%→0.0%，ASB 直接注入 harness 攻击成功 0/1200

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive fields, which sinks may receive released data, and what authority may cross delegation boundaries. The language supports flow and path rules, task-scoped capabilities, controlled release, and stateful taint semantics. A runtime reference monitor mediates agent actions, and a bounded SMT-based verifier checks safety properties for a structured policy fragment. We evaluate AgentFlow on multiple agent benchmarks. In our prototype, seven safety properties verify in under 0.5 seconds each, and the verifier catches all seeded unsafe policy variants in our study. On 949 AgentDojo injected cases across four suites, AgentFlow reduces confirmed compromise from 33.0\% to 0.0\% while improving aggregate utility from 46.7\% to 63.3\%. On a 200-case AgentDyn Dailylife benchmark, it reduces confirmed compromise from 73.5\% to 0.0\% while preserving near-baseline utility (44.5\% to 43.5\%). Breadth checks across ASB, InjecAgent, BIPIA, AgentHarm, and MCPTox replays suggest that the configured policies block the benchmark-specified policy-visible attacker flows; in ASB's direct-prompt-injection harness, attack success is 0/1{,}200. These results are preliminary and scoped to the modeled policy-visible agent behaviors and evaluated benchmarks.

</details>

### 8. RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards

📄 [arXiv](https://arxiv.org/abs/2608.24275)　📅 2026-08

**关键词**：`defense`、`trajectory safeguard`、`policy-grounded rationale`、`policy invocation`、`dynamic policy invocation`、`verifiable reward`

👤 **作者**：Houcheng Jiang、Boxuan Zhang、Qiyong Zhong、Junfeng Fang、Xiang Wang、Xiangnan He

- 🎯 **研究动机**：policy-aware safeguard 依赖 prompting 或 SFT，难以适应未见轨迹与动态 policy context
- 🔬 **研究方法**：RePolicy 以 RL 学习调用动态策略库并生成 policy-grounded 判定，用 PolicyTraj-20K 初始化加可验证奖励 GRPO 训练
- 📌 **结论**：六个 Agent 安全 benchmark 上安全检测表现强，policy context 变化下策略调用保持稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safeguarding language model agents requires assessing complete execution trajectories under context-dependent safety policies. Existing policy-aware safeguards mainly rely on prompting or supervised fine-tuning, limiting their ability to adapt to unseen trajectories and changing policy contexts. We propose RePolicy, an agent safeguard that learns safety-policy invocation through reinforcement learning. Given an agent trajectory and a dynamic policy library, RePolicy invokes the applicable policy and uses its content to produce a policy-grounded rationale and safety judgment. We construct PolicyTraj-20K to support supervised initialization, followed by GRPO with verifiable rewards and policy-context perturbation. Experiments across six agent safety benchmarks show that RePolicy achieves strong overall safety-detection performance and robust policy invocation under varying policy contexts.

</details>

### 9. PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.19861)　📅 2026-08

**关键词**：`defense`、`workflow guardrail`、`persistent policy state`、`missing-step remediation`、`workflow monitoring`、`persistent state graph`

👤 **作者**：Seongjae Kang、Taehyung Yu、Sung Ju Hwang

- 🎯 **研究动机**：运行时防护只拦危险动作、不引导多步流程；工作流跟随系统以流程完成为目标而非守护 agent 行为
- 🔬 **研究方法**：PolicyGuide 把域政策编译为工作流图并在用户轮边界调用主动验证器，从持久图状态对账未决请求并返回政策合规路径上的逐步补救
- 📌 **结论**：τ²-bench 航空/零售/电信域 GPT-5.4 agent 上平均 Pass^4 从 0.42 升至 0.62（电信 0.19 至 0.61）；工作流迁移到 Claude 与 Gemini agent，对抗用户下 ASR 最低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion rather than safeguarding agent behavior. PolicyGuide instead compiles each domain policy into a workflow graph and invokes a proactive verifier at user-turn boundaries. From persisted graph state, the verifier reconciles open requests and returns step-specific remediation along a policy-compliant path. Across the $τ^2$-bench airline, retail, and telecom domains with a GPT-5.4 agent and verifier, PolicyGuide raises mean $\mathrm{Pass}^4$ from $0.42$ to $0.62$, with the largest gain on telecom ($0.19$ to $0.61$), the most workflow-structured domain. The same workflows transfer to Claude Sonnet 4.6 and Gemini 2.5 Pro agents. Complementary evaluations find the lowest observed attack-success rate under adversarial users and the strongest procedural compliance in an author-designed workflow-level validation.

</details>

### 10. PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.15673)　📅 2026-08

**关键词**：`defense`、`neurosymbolic guardrail`、`ProbLog`、`policy consistency`

👤 **作者**：Satchit Chatterji、Shihan Wang、Giovanni Sileno、Erman Acar

- 🎯 **研究动机**：现有 guardrail 把语义接地与策略推理混在同一模型，导致有害合规或良性误拒
- 🔬 **研究方法**：PL-Guard 神经符号架构：本地 LLM 以重归一化 True/False token 分数把 prompt-回应接地为谓词概率，ProbLog 对符号策略做显式概率规则推理
- 📌 **结论**：XSTest 上手工策略把不安全合规从基座 22.0% 降至 0.5%（低于 LLM-judge 基线 6.0%），代价是过拒 14.4% 对 5.2%，但中间推理显式可审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with harmful prompts, or refusals to assist benign ones. To separate grounding and reasoning roles, we propose PL-Guard, a neurosymbolic guardrail architecture. Using a symbolic policy interface consisting of predicates and ProbLog rules, a local LLM grounds prompt-response pairs into predicate probabilities using renormalized True/False token scores, while ProbLog performs explicit probabilistic rule inference over the symbolic policy. On the XSTest benchmark, an offline Qwen-based evaluator finds that PL-Guard with a hand-curated policy reduces unsafe compliance from 22.0% for the base model to 0.5%, and below the 6.0% rate of an LLM-as-a-judge baseline. This comes at the cost of higher over-refusal than the LLM-as-a-judge baseline, 14.4% versus 5.2%. These results suggest that separating neural grounding from probabilistic symbolic reasoning can expose the safety-helpfulness tradeoff while making the guardrail's intermediate reasoning steps explicit and auditable.

</details>

### 11. SCOPE: Streaming Covariance-Orthogonal Post-Hoc Editing for Continual LLM Safety Governance

🌐 [Project](https://doi.org/10.1145/3770855.3817993)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`continual safety editing`、`post-hoc governance`、`capability retention`

- 🎯 **研究动机**：持续叠加安全编辑会侵蚀模型既有能力
- 🔬 **研究方法**：SCOPE以流式协方差正交化的post-hoc编辑，使更新与能力方向正交
- 📌 **结论**：实现连续安全治理且能力保留

### 12. SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning

📄 [arXiv](https://arxiv.org/abs/2606.22873)　📅 2026-06

**关键词**：`defense`、`policy-adaptive guard`、`multimodal moderation`、`dynamic reasoning`

👤 **作者**：SingGuard Team

- 🎯 **研究动机**：多数护栏依赖固定分类法或窄交互设定，策略随产品、地区与阶段变化时适应性不足
- 🔬 **研究方法**：提出 SingGuard：把活跃策略作为运行时输入逐条规则检查并输出触犯规则，支持快/混合/慢推理档与快慢解耦 RL；配套 SingGuard-Bench（56,340 例、80+ 细粒度风险、含跨模态联合风险）
- 📌 **结论**：六族基准（35 数据集）全部 SOTA 平均 F1；动态规则评估中策略跟随准确率从 0.6465 升至 0.7415

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are increasingly deployed in consumer, medical, financial, and enterprise applications. This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. Most existing guardrails either rely on fixed taxonomies or target only a narrow set of interaction settings, which limits their adaptability when safety rules change at deployment time. We present \textbf{SingGuard}, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. SingGuard treats the active policy as a runtime input: given natural-language rules, it checks the target content against the active policy rule by rule and predicts both the safety label and the triggered rule. To balance efficiency and interpretability, SingGuard supports fast, hybrid, and slow inference regimes along a fast-to-slow reasoning spectrum, ranging from direct safety judgments to policy-grounded deliberation. We further optimize this behavior with fast--slow decoupled reinforcement learning. We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. Across six benchmark families (35 datasets), SingGuard achieves state-of-the-art average F1 in every family. Dynamic-rule evaluation further shows improved policy-following accuracy from 0.6465 to 0.7415 under runtime policy shifts. Our code is available at https://github.com/inclusionAI/Sing-Guard.

</details>

### 13. ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2605.31073)　📅 2026-05

**关键词**：`defense`、`policy enforcement`、`trajectory distillation`、`functional coupling`

👤 **作者**：Yan Wang、…、Hui Xue

- 🎯 **研究动机**：推理式护栏存在 deliberation-to-enforcement gap：推理中识别有害却判安全，或无政策依据即下不安全决定
- 🔬 **研究方法**：ConsisGuard 做 Policy-to-Decision 轨迹蒸馏与功能耦合对齐，使推理 grounded 于安全政策且最终决策被该推理蕴含
- 📌 **结论**：在 prompt 与 response 危害检测基准上提升检测性能并减少政策执行失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning-based LLM guardrails improve safety moderation by generating explicit rationales before issuing final decisions. However, their rationales do not always lead to faithful enforcement: a model may recognize a harmful intent in its reasoning but still predict a safe label, or issue an unsafe decision without policy-grounded justification. We identify this safety-critical failure mode as the deliberation-to-enforcement gap. Unlike general chain-of-thought faithfulness, guardrail reliability requires policy execution consistency: the generated reasoning should be grounded in the safety policy, and the final decision should be entailed by that reasoning. We propose ConsisGuard, a consistency-aware framework for reasoning-based LLM guardrails. ConsisGuard performs Policy-to-Decision Trajectory Distillation and Functional Coupling Alignment, aligning the internal coupling between safety deliberation and decision enforcement. Experiments on prompt and response harmfulness detection benchmarks show that ConsisGuard improves detection performance while reducing policy execution failures. These results suggest that reliable reasoning-based guardrails require accurate faithful execution of safety policies.

</details>

### 14. LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails

📄 [arXiv](https://arxiv.org/abs/2605.17329)　📅 2026-05

**关键词**：`defense`、`latent policy reasoning`、`fixed-budget inference`、`latency`

👤 **作者**：Nanxi Li、Zhengyue Zhao、Chaowei Xiao

- 🎯 **研究动机**：推理时定制安全政策要求护栏动态适配而不重训，但忠实政策判断需推理能力、部署要求低延迟，存在根本张力
- 🔬 **研究方法**：LPG 把意图解释与政策落地的内部审议压缩为决策语义监督的连续潜状态，推理时只生成锚定被违反政策条款的紧凑结论
- 📌 **结论**：LPG-4B 以 10 个 latent token 达 84.5% 平均安全准确率与 77.9% F1，超过最强动态基线且比 Qwen3-4B-Thinking 快约 11 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrails are a critical safety layer for modern AI systems, but their operating regime is changing. As LLMs are deployed as customized assistants, safety policies are increasingly specified at inference time by users, organizations, or regulatory contexts. This makes safety enforcement fundamentally dynamic: the guardrail should adapt to changing safety policies without retraining. Yet this requirement creates a fundamental tension: faithfully judging complex policy contexts demands reasoning capability, while practical deployment requires low-latency responses. We introduce Latent Policy Guardrail (LPG), a guardrail framework that learnssemantic latent deliberation over dynamic policies. LPG compresses the internal deliberation needed for intent interpretation and policy grounding into continuous states supervised by decision-relevant semantics. At inference time, it generates only a compact verdict anchored to the violated policy clauses, preserving auditability while avoiding the latency of explicit reasoning. Across policy guardrail benchmarks, LPG-4B reaches 84.5% average safety accuracy and 77.9% F1 by compressing deliberation into just 10 latent tokens, outperforming the strongest dynamic baseline while running roughly 11 times faster than Qwen3-4B-Thinking under the single-sample evaluation setup. Code and data are available at https://github.com/SaFo-Lab/Latent_Policy_Guard.

</details>

### 15. LiSA: Lifelong Safety Adaptation via Conservative Policy Induction

📄 [arXiv](https://arxiv.org/abs/2605.14454)　📅 2026-05

**关键词**：`defense`、`lifelong adaptation`、`policy induction`、`structured memory`

👤 **作者**：Minbeom Kim、…、Long T. Le

- 🎯 **研究动机**：guardrail 失败可泄密或授权危险动作，最难的是上下文性失败，而部署反馈只有稀疏噪声的用户上报且反复微调不现实
- 🔬 **研究方法**：LiSA 保守策略归纳：把偶发失败转为可复用策略抽象、冲突感知局部规则防过度泛化、基于后验下界的证据感知置信门控
- 📌 **结论**：PrivacyLens+、ConFaide+ 与 AgentHarm 上稀疏反馈下持续超过记忆基线，20% 标签翻转噪声下仍鲁棒，延迟-性能前沿超越骨干模型扩容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI agents move from chat interfaces to systems that read private data, call tools, and execute multi-step workflows, guardrails become a last line of defense against concrete deployment harms. In these settings, guardrail failures are no longer merely answer-quality errors: they can leak secrets, authorize unsafe actions, or block legitimate work. The hardest failures are often contextual: whether an action is acceptable depends on local privacy norms, organizational policies, and user expectations that resist pre-deployment specification. This creates a practical gap: guardrails must adapt to their own operating environments, yet deployment feedback is typically limited to sparse, noisy user-reported failures, and repeated fine-tuning is often impractical. To address this gap, we propose LiSA (Lifelong Safety Adaptation), a conservative policy induction framework that improves a fixed base guardrail through structured memory. LiSA converts occasional failures into reusable policy abstractions so that sparse reports can generalize beyond individual cases, adds conflict-aware local rules to prevent overgeneralization in mixed-label contexts, and applies evidence-aware confidence gating via a posterior lower bound, so that memory reuse scales with accumulated evidence rather than empirical accuracy alone. Across PrivacyLens+, ConFaide+, and AgentHarm, LiSA consistently outperforms strong memory-based baselines under sparse feedback, remains robust under noisy user feedback even at 20% label-flip rates, and pushes the latency--performance frontier beyond backbone model scaling. Ultimately, LiSA offers a practical path to secure AI agents against the unpredictable long tail of real-world edge risks.

</details>

### 16. Who Decides What Is Harmful? Content Moderation Policy Through A Multi-Agent Personalised Inference Framework

📄 [arXiv](https://arxiv.org/abs/2605.01416) · 🌐 [Project](https://aisel.aisnet.org/ecis2026/is_policy/is_policy/2/)　📅 2026-05

**关键词**：`defense`、`personalized moderation`、`user sensitivity profile`、`multi-agent inference`

👤 **作者**：Ewelina Gajewska、Michal Wawer、Katarzyna Budzynska、Jaroslaw A. Chudziak

- 🎯 **研究动机**：集中式自上而下的内容审核规则无法适应伤害感知的主观性与个体差异
- 🔬 **研究方法**：LLM 多智能体个性化推理框架：领域 Expert Agents、Manager Agent 编排内容分析、Ghost Profile Agent 模拟用户敏感度画像
- 📌 **结论**：较非个性化基线准确率最高提升 32%，更贴合个体用户的敏感度边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing scale and complexity of online platforms raises critical policy questions around harmful content, digital well-being, and user autonomy. Traditional content moderation systems rely on centralised, top-down rules, often failing to accommodate the subjective nature of harm perception. This paper proposes an LLM-based multi-agent personalised inference framework that filters content based on unique sensitivity profiles of individual users. Our architecture combines domain-specific Expert Agents, a Manager Agent for orchestrating content analysis and agent selection, and a Ghost Profile Agent for simulating user perspectives, to inform moderation decisions. Evaluated against a range of non-personalised baselines, the system demonstrates up to a 32% improvement in accuracy, showing increased alignment with individual user sensitivities. Beyond technical performance, our framework provides policy-relevant insights for platform governance, providing a scalable way to reconcile moderation policies with societal and individual digital rights

</details>

### 17. BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

📄 [arXiv](https://arxiv.org/abs/2604.25203) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64273)　📅 2026-04　🏷 ICML 2026

**关键词**：`defense`、`custom policy guard`、`asymmetric debate`、`synthetic training`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Arnon Mazza、Elad Levi

- 🎯 **研究动机**：通用安全模型不懂定制政策，prompt 方式边界不一致且推理成本高，训练分类器又需昂贵标注
- 🔬 **研究方法**：BARRED 仅凭任务描述与少量无标注样本合成训练数据：维度分解保证域覆盖，多智能体验证标签正确性，再微调小语言模型
- 📌 **结论**：微调后的小语言模型在多种定制政策上持续超过 SOTA 专有 LLM 与专用护栏模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying guardrails for custom policies remains challenging, as generic safety models fail to capture task-specific requirements, while prompting LLMs suffers from inconsistent boundary-case performance and high inference costs. Training custom classifiers achieves both accuracy and efficiency, yet demands substantial labeled data that is costly to obtain. We present BARRED (Boundary Alignment Refinement through REflection and Debate), a framework for generating faithful and diverse synthetic training data using only a task description and a small set of unlabeled examples. Our approach decomposes the domain space into dimensions to ensure comprehensive coverage, and employs multi-agent debate to verify label correctness, yielding a high-fidelity training corpus. Experiments across diverse custom policies demonstrate that small language models finetuned on our synthetic data consistently outperform state-of-the-art proprietary LLMs (including reasoning models) and dedicated guardrail models. Ablation studies confirm that both dimension decomposition and debate-based verification are critical for ensuring the diversity and label fidelity required for effective fine-tuning. The BARRED framework eliminates the reliance on extensive human annotation, offering a scalable solution for accurate custom guardrails.

</details>

### 18. FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation

📄 [arXiv](https://arxiv.org/abs/2602.23636) · 🎓 [Official](https://aclanthology.org/2026.acl-long.263/)　📅 2026-02　🏷 ACL 2026

**关键词**：`defense`、`continuous risk score`、`strictness adaptation`、`risk calibration`、`content moderation`、`harmful content`

👤 **作者**：Zhihao Ding、Jinming Li、Ze Lu、Jieming Shi

- 🎯 **研究动机**：二值审核器隐含固定有害定义，在平台执行严格度各异且随时间演化时表现脆弱
- 🔬 **研究方法**：提出严格度自适应基准 FlexBench；FlexGuard 经 risk-alignment 优化输出校准的连续风险分，部署时按阈值适配目标严格度
- 📌 **结论**：在 FlexBench 与公开基准上取得更高审核精度和跨严格度的显著鲁棒性提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of LLM-generated content is essential for real-world deployment. Most existing guardrail models formulate moderation as a fixed binary classification task, implicitly assuming a fixed definition of harmfulness. In practice, enforcement strictness - how conservatively harmfulness is defined and enforced - varies across platforms and evolves over time, making binary moderators brittle under shifting requirements. We first introduce FlexBench, a strictness-adaptive LLM moderation benchmark that enables controlled evaluation under multiple strictness regimes. Experiments on FlexBench reveal substantial cross-strictness inconsistency in existing moderators: models that perform well under one regime can degrade substantially under others, limiting their practical usability. To address this, we propose FlexGuard, an LLM-based moderator that outputs a calibrated continuous risk score reflecting risk severity and supports strictness-specific decisions via thresholding. We train FlexGuard via risk-alignment optimization to improve score-severity consistency and provide practical threshold selection strategies to adapt to target strictness at deployment. Experiments on FlexBench and public benchmarks demonstrate that FlexGuard achieves higher moderation accuracy and substantially improved robustness under varying strictness. We release the source code and data to support reproducibility.

</details>

### 19. CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety

📄 [arXiv](https://arxiv.org/abs/2602.22557)　📅 2026-02

**关键词**：`defense`、`zero-shot policy adaptation`、`policy retrieval`、`multi-agent debate`

👤 **作者**：Umid Suleymanov、…、Murat Kantarcioglu

- 🎯 **研究动机**：静态微调安全分类器存在适应刚性，无法在不重训下执行新治理规则
- 🔬 **研究方法**：CourtGuard 检索增强多 agent 框架把安全评测重构为基于外部政策文档的证据辩论（Evidentiary Debate）
- 📌 **结论**：7 个安全基准 SOTA；仅换政策文件即零样本泛化到 Wikipedia 破坏检测（90% 准确率），并自动构建九个对抗数据集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current safety mechanisms for Large Language Models (LLMs) rely heavily on static, fine-tuned classifiers that suffer from adaptation rigidity, the inability to enforce new governance rules without expensive retraining. To address this, we introduce CourtGuard, a retrieval-augmented multi-agent framework that reimagines safety evaluation as Evidentiary Debate. By orchestrating an adversarial debate grounded in external policy documents, CourtGuard achieves state-of-the-art performance across 7 safety benchmarks, outperforming dedicated policy-following baselines without fine-tuning. Beyond standard metrics, we highlight two critical capabilities: (1) Zero-Shot Adaptability, where our framework successfully generalized to an out-of-domain Wikipedia Vandalism task (achieving 90\% accuracy) by swapping the reference policy; and (2) Automated Data Curation and Auditing, where we leveraged CourtGuard to curate and audit nine novel datasets of sophisticated adversarial attacks. Our results demonstrate that decoupling safety logic from model weights offers a robust, interpretable, and adaptable path for meeting current and future regulatory requirements in AI governance.

</details>

### 20. Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`role-playing Agent`、`persona-aware guard`、`retrieved safety rule`、`jailbreak`、`self-evolution`

- 🎯 **研究动机**：角色扮演 agent 越忠于人设越易被越狱，训练时方案维护成本高、损害角色内行为且对闭源模型不可行
- 🔬 **研究方法**：提出免训练双循环对抗自进化：攻击循环合成渐进更强的越狱提示，防御循环把失败蒸馏为全局安全规则、角色约束与安全角色示例的层级知识库供推理时检索组合
- 📌 **结论**：多个专有 LLM 上角色保真与抗越狱均超过强基线，并对未见角色与攻击提示鲁棒泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based role-playing has rapidly improved in fidelity, yet stronger adherence to persona constraints commonly increases vulnerability to jailbreak attacks, especially for risky or negative personas. Most prior work mitigates this issue with trainingtime solutions (e.g., data curation or alignmentoriented regularization). However, these approaches are costly to maintain as personas and attack strategies evolve, can degrade in-character behavior, and are typically infeasible for frontier closed-weight LLMs. We propose a training-free Dual-Cycle Adversarial Self-Evolution framework with two coupled cycles. A Persona-Targeted Attacker Cycle synthesizes progressively stronger jailbreak prompts, while a Role-Playing Defender Cycle distills observed failures into a hierarchical knowledge base of (i) global safety rules, (ii) persona-grounded constraints, and (iii) safe in-character exemplars. At inference time, the Defender retrieves and composes structured knowledge from this hierarchy to guide generation, producing responses that remain faithful to the target persona while satisfying safety constraints. Extensive experiments across multiple proprietary LLMs show consistent gains over strong baselines on both role fidelity and jailbreak resistance, and robust generalization to unseen personas and attack prompts.

</details>

### 21. Taxonomy-Adaptive Moderation Model with Robust Guardrails for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2512.05339)　📅 2025-12

**关键词**：`defense`、`taxonomy adaptation`、`input-output moderation`、`instruction tuning`

👤 **作者**：Mahesh Kumar Nandwana、Youngwan Lim、Joseph Liu、Alex Yang、Varun Notibala、Nishchaie Khanna

- 🎯 **研究动机**：LLM 后训练对齐后仍可能产生不当输出，需要覆盖输入与输出的稳健防护
- 🔬 **研究方法**：Roblox Guard 1.0 基于 Llama-3.1-8B-Instruct，用合成与开源安全数据、CoT rationale 与 input inversion 做指令微调以泛化到未见安全分类法，并发布 RobloxGuard-Eval 基准
- 📌 **结论**：在域外安全基准上表现强劲，能泛化适配未见过的安全 taxonomy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are typically aligned for safety during the post-training phase; however, they may still generate inappropriate outputs that could potentially pose risks to users. This challenge underscores the need for robust safeguards that operate across both model inputs and outputs. In this work, we introduce Roblox Guard 1.0, a state-of-the-art instruction fine-tuned LLM designed to enhance the safety of LLM systems through comprehensive input-output moderation, using a pipeline of LLMs to enhance moderation capability. Built on the Llama-3.1-8B-Instruct backbone, our model is instruction fine-tuned to generalize across previously unseen safety taxonomies and demonstrates strong performance on out-of-domain safety benchmarks. The instruction fine-tuning process uses a mix of synthetic and open-source safety datasets, augmented with chain-of-thought (CoT) rationales and input inversion to enhance contextual understanding and decision making. To support systematic evaluation, we also release RobloxGuard-Eval, a new benchmark featuring an extensible safety taxonomy to assess the effectiveness of LLM guardrails and moderation frameworks.

</details>

### 22. Beyond One-Size-Fits-All: Personalized Harmful Content Detection with In-Context Learning

📄 [arXiv](https://arxiv.org/abs/2511.05532) · 📊 [Dataset](https://huggingface.co/datasets/ChaseLabs/Harmful-Texts-On-Mastodon)　📅 2025-10

**关键词**：`defense`、`personalized moderation`、`in-context learning`、`user-defined category`

👤 **作者**：Rufan Zhang、Lin Zhang、Xianghang Mi

- 🎯 **研究动机**：集中式任务专用审核缺乏透明度且忽视用户偏好，不适合隐私敏感与去中心化环境
- 🔬 **研究方法**：用基础模型 in-context learning 统一毒性、垃圾与负面情绪检测，支持用户以 prompt 增删类别或扩展语义变体而无需重训
- 📌 **结论**：跨任务泛化常媲美微调模型，单个用户示例即可实现个性化，标签定义与理由补充显著增强噪声鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of harmful online content--e.g., toxicity, spam, and negative sentiment--demands robust and adaptable moderation systems. However, prevailing moderation systems are centralized and task-specific, offering limited transparency and neglecting diverse user preferences--an approach ill-suited for privacy-sensitive or decentralized environments. We propose a novel framework that leverages in-context learning (ICL) with foundation models to unify the detection of toxicity, spam, and negative sentiment across binary, multi-class, and multi-label settings. Crucially, our approach enables lightweight personalization, allowing users to easily block new categories, unblock existing ones, or extend detection to semantic variations through simple prompt-based interventions--all without model retraining. Extensive experiments on public benchmarks (TextDetox, UCI SMS, SST2) and a new, annotated Mastodon dataset reveal that: (i) foundation models achieve strong cross-task generalization, often matching or surpassing task-specific fine-tuned models; (ii) effective personalization is achievable with as few as one user-provided example or definition; and (iii) augmenting prompts with label definitions or rationales significantly enhances robustness to noisy, real-world data. Our work demonstrates a definitive shift beyond one-size-fits-all moderation, establishing ICL as a practical, privacy-preserving, and highly adaptable pathway for the next generation of user-centric content safety systems. To foster reproducibility and facilitate future research, we publicly release our code on GitHub and the annotated Mastodon dataset on Hugging Face.

</details>

### 23. Learning Efficient Guardrails for Compliance

📄 [arXiv](https://arxiv.org/abs/2510.03485) · 🌐 [Project](https://rakanwen.github.io/policyguard-page/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60652)　📅 2025-10　🏷 ICML 2026

**关键词**：`defense`、`policy trajectory`、`prefix violation`、`efficient compliance`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Xiaofei Wen、Wenjie Jacky Mo、Yanan Xie、Peng Qi、Muhao Chen

- 🎯 **研究动机**：长程 web agent 对真实政策的遵循能力相比标准安全目标被严重低估
- 🔬 **研究方法**：构建 60K 政策-轨迹对的 PolicyGuardBench（含全轨迹与新型前缀违规检测任务），训练轻量护栏 PolicyGuard
- 📌 **结论**：检测精度强、推理高效，对未见领域泛化稳健，证明小规模合规护栏可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous web agents are increasingly deployed for long-horizon tasks, yet their ability to adhere to real-world policies remains critically underexplored compared to standard safety objectives. To address this gap, we introduce PolicyGuardBench, a benchmark of 60k policy-trajectory pairs designed to evaluate compliance through both full-trajectory and novel prefix-based violation detection tasks. Using this dataset, we train PolicyGuard, a lightweight guardrail model that achieves strong detection accuracy while maintaining high inference efficiency. Notably, our model demonstrates robust generalization capabilities, preserving high performance even on unseen domains. These contributions establish a comprehensive framework for studying policy compliance, showing that accurate and generalizable guardrails are feasible at small scales.

</details>

### 24. GSPR: Aligning LLM Safeguards as Generalizable Safety Policy Reasoners

📄 [arXiv](https://arxiv.org/abs/2509.24418) · 📝 [OpenReview](https://openreview.net/forum?id=H2e5TerulJ)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`policy reasoning`、`GRPO`、`unseen taxonomy`

👤 **作者**：Haoran Li、…、Yangqiu Song

- 🎯 **研究动机**：各安全基准分类学各异，现有护栏要么粗粒度二分要么被窄分类学束缚
- 🔬 **研究方法**：提出 GSPR 通用安全政策推理器：经 RL 激励跨多种安全分类学的推理能力，识别违规输入输出并给出类别与简洁解释
- 📌 **结论**：显著提升护栏的安全与类别预测推理能力，且推理 token 成本最低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are integrated into numerous applications, LLMs' safety becomes critical for both application developers and intended users. Currently, great efforts have been made to develop safety benchmarks with fine-grained taxonomies. However, these benchmarks' taxonomies are disparate with different safety policies. Thus, existing safeguards trained on these benchmarks are either coarse-grained to only distinguish between "safe'' and "unsafe,'' or constrained by the specified narrow risk taxonomies. To leverage these fine-grained safety policies across multiple safety taxonomies, we propose GSPR, a Generalizable Safety Policy Reasoner to identify unsafe inputs and outputs with violated safety taxonomies and concise explanations. Unlike prior safeguards which only cover a fixed set of risk factors, GSPR incentivizes its reasoning capability with varied safety taxonomies through reinforcement learning. Our GSPR can be trained across multiple safety benchmarks with distinct taxonomies and naturally exhibits powerful generalization ability. We conduct extensive experiments to show that GSPR significantly improves existing safety guardrails' reasoning capabilities for both safety and category prediction tasks. Moreover, GSPR also achieves the least inference token costs with explanations.

</details>

### 25. Scaling Policy Compliance Assessment in Language Models with Policy Reasoning Traces

📄 [arXiv](https://arxiv.org/abs/2509.23291) · 📝 [OpenReview](https://openreview.net/forum?id=QgEDWbZQ6V)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`policy reasoning traces`、`compliance assessment`、`trace supervision`

👤 **作者**：Joseph Marvin Imperial、Harish Tayyar Madabushi

- 🎯 **研究动机**：政策合规评估缺乏专家级逐步推理的文档，人工获取成本高
- 🔬 **研究方法**：提出 Policy Reasoning Traces 作为推理桥梁，应用于推理时与训练时两种场景
- 📌 **结论**：显著提升开源与商用模型合规评估性能，HIPAA 与 GDPR 上创新 SoTA，并改善政策条款引用准确性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Policy compliance assessment is a fundamental task of evaluating whether an input case strictly complies with a set of human-defined rules, more generally known as policies. In practice, human experts follow a systematic, step-by-step process to identify violations with respect to specific stipulations outlined in the policy. However, such documentation of gold-standard, expert-level reasoning processes is costly to acquire. In this paper, we introduce Policy Reasoning Traces (PRT), a form of specialized generated reasoning chains that serve as a reasoning bridge to improve an LLM's policy compliance assessment capabilities. Our empirical evaluations demonstrate that the use of PRTs for both inference-time and training-time scenarios significantly enhances the performance of open-weight and commercial models, setting a new state-of-the-art for HIPAA and GDPR policies. Beyond accuracy gains, we also highlight how PRTs can improve an LLM's ability to accurately cite policy clauses, as well as influence compliance decisions through their high utilization from the raw chains of thought.

</details>

### 26. DynaGuard: A Dynamic Guardian Model With User-Defined Policies

📄 [arXiv](https://arxiv.org/abs/2509.02563) · 📝 [OpenReview](https://openreview.net/forum?id=gc8Ylt0lbm) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008138)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`user-defined policy`、`fast-slow inference`、`dynamic taxonomy`

👤 **作者**：Monte Hoover、…、Tom Goldstein

- 🎯 **研究动机**：标准护栏模型局限于预定义静态危害类别，无法适配用户政策
- 🔬 **研究方法**：提出 DynaGuard 动态护栏套件按用户自定义策略评估文本，配 DynaBench 数据集，提供快检测与 CoT 推理两种模式
- 📌 **结论**：传统安全类别检测精度超静态模型，自由格式政策违规上可比前沿推理模型且耗时仅其零头

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardian models play a crucial role in ensuring the safety and ethical behavior of user-facing AI applications by enforcing guardrails and detecting harmful content. While standard guardian models are limited to predefined, static harm categories, we introduce DynaGuard, a suite of dynamic guardian models offering novel flexibility by evaluating text based on user-defined policies, and DynaBench, a dataset for training and evaluating dynamic guardian models. Our models provide both rapid detection of policy violations and a chain-of-thought reasoning option that articulate and justify model outputs. Critically, DynaGuard not only surpasses static models in detection accuracy on traditional safety categories, but is competitive with frontier reasoning models on free-form policy violations, all in a fraction of the time. This makes DynaGuard an critical tool for language model guardrails.

</details>

### 27. Towards Trustworthy Multimodal Moderation via Policy-Aligned Reasoning and Hierarchical Labeling

📄 [arXiv](https://arxiv.org/abs/2508.03296) · 🌐 [Project](https://doi.org/10.1145/3770854.3783934)　📅 2025-08　🏷 KDD 2026

**关键词**：`defense`、`analysis`、`multimodal moderation`、`policy-grounded reasoning`、`hierarchical taxonomy`、`policy alignment`

👤 **作者**：Anqi Li、Wenwei Jin、Jintao Tong、Pengda Qin、Weijia Li、Guo Lu

- 🎯 **研究动机**：现有内容审核依赖噪声标签学习，与审核规则脱节且决策不透明、妨碍人工复核
- 🔬 **研究方法**：提出 Hi-Guard 层级审核：轻量二分类过滤后由强模型在层级分类法上做路径式细粒度分类，规则入 prompt，GRPO 加多级软边距奖励优化
- 📌 **结论**：分类精度、泛化与可解释性均更优，并已在真实场景部署

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Social platforms have revolutionized information sharing, but also accelerated the dissemination of harmful and policy-violating content. To ensure safety and compliance at scale, moderation systems must go beyond efficiency and offer accuracy and interpretability. However, current approaches largely rely on noisy, label-driven learning, lacking alignment with moderation rules and producing opaque decisions that hinder human review. Therefore, we propose Hierarchical Guard (Hi-Guard), a multimodal moderation framework that introduces a new policy-aligned decision paradigm. The term "Hierarchical" reflects two key aspects of our system design: (1) a hierarchical moderation pipeline, where a lightweight binary model first filters safe content and a stronger model handles fine-grained risk classification; and (2) a hierarchical taxonomy in the second stage, where the model performs path-based classification over a hierarchical taxonomy ranging from coarse to fine-grained levels. To ensure alignment with evolving moderation policies, Hi-Guard directly incorporates rule definitions into the model prompt. To further enhance structured prediction and reasoning, we introduce a multi-level soft-margin reward and optimize with Group Relative Policy Optimization (GRPO), penalizing semantically adjacent misclassifications and improving explanation quality. Extensive experiments and real-world deployment demonstrate that Hi-Guard achieves superior classification accuracy, generalization, and interpretability, paving the way toward scalable, transparent, and trustworthy content safety systems. Code is available at: https://github.com/lianqi1008/Hi-Guard.

</details>

### 28. PAM: Training Policy-Aligned Moderation Filters at Scale

📄 [arXiv](https://arxiv.org/abs/2505.19766) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-05

**关键词**：`defense`、`policy-aligned moderation`、`synthetic data`、`filter distillation`

👤 **作者**：Masoomali Fatehkia、Enes Altinisik、Mohamed Osman、Husrev Taha Sencar

- 🎯 **研究动机**：现有审核 filter 局限安全范畴，难以满足真实部署中的定制策略对齐需求
- 🔬 **研究方法**：提出 PAM，从用户自定义策略自动生成合成监督训练审核过滤器，无需人工标注，并发布 PAMbench 四个基准
- 📌 **结论**：匹配 SoTA 安全过滤器与策略推理模型并在 PAMbench 上更优，推理快 5 至 100 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) remain vulnerable to misalignment and jailbreaks, making external safeguards like moderation filters essential, yet existing filters often focus narrowly on safety, falling short of the broader alignment needs seen in real-world deployments. We introduce Policy Aligned Moderation (PAM), a flexible framework for training custom moderation filters grounded in user-defined policies that extend beyond conventional safety objectives. PAM automates training data generation without relying on human-written examples, enabling scalable support for diverse, application-specific alignment goals and generation policies. PAM-trained filters match the performance of state-of-the-art safety moderation filters and policy reasoning models, and outperform them on PAMbench, four newly introduced user-annotated policy enforcement benchmarks that target age restrictions, dietary accommodations, cultural alignment, and limitations in medical guidance. These performance gains are achieved while the PAM filter runs 5-100x faster at inference than policy-conditioned reasoning models.

</details>

### 29. Granite.Trust Policy Tools: Shareable, Actionable Policies for Generative AI Applications

📄 [arXiv](https://arxiv.org/abs/2608.23870)　📅 2026-08

**关键词**：`tool`、`actionable policy`、`content constraint`、`runtime monitoring`

👤 **作者**：Nathalie Baracaldo、Nicolas Mello、Kush R. Varshney、Heiko Ludwig、Kate Soule、David Cox

- 🎯 **研究动机**：GenAI 安全策略因组织、监管环境与用户画像而异，但现有策略规范面向传统访问控制，无法表达基于内容的响应约束
- 🔬 **研究方法**：提出 YAML 格式 Actionable Policy schema（规定模型响应能/不能包含什么并支持例外追踪治理）、生成 policy-aligned 训练数据的合成数据管线及策略定义与执行工具，全部开源
- 📌 **结论**：组织可一次定义策略并贯穿 GenAI 应用全生命周期——从模型对齐、测试到运行时监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When it comes to safety policies for generative AI, one size does not fit all. Each organization and use case needs to mitigate different risks depending on the application context, regulatory environment, organizational values, and user personas. Yet, existing policy specification approaches are designed for traditional access control and fail to capture the nuances of GenAI application: the enforcement of content-based constraints. We present two contributions to address this gap: (1) the Actionable Policy schema, a YAML-based format for specifying what model responses can and cannot contain. The schema enables exception-based policy governance, proposing exceptions to track policy violations; (2) synthetic data generation pipeline that produces policy-aligned training data for model alignment and testing, and a set of tools to help define the schema and enforce policy. Together, these enable organizations to specify policies once and enforce them throughout the GenAI application lifecycle: from model alignment to runtime monitoring. The Actionable Policy schema, example policies, and tools are available as open source: https://github.com/ibm-granite/granite.trust.policy-tools We welcome new ideas, contributions and feedback.

</details>

### 30. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

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

### 31. It is not enough to give your moderation rules to ChatGPT: Policy-as-Prompt Moderation and Its Potential Impacts on Community Governance

📄 [arXiv](https://arxiv.org/abs/2607.12149)　📅 2026-07

**关键词**：`analysis`、`policy-as-prompt`、`community moderation`、`governance impact`

👤 **作者**：Anna Neumann、Jasmin Wyss、Ivy Turk、Rebekah Overdorf

- 🎯 **研究动机**：policy-as-prompt（把社区规则写成提示交给 LLM 审核）被当作去中心化审核的可行方案，其技术与治理局限未被系统分析
- 🔬 **研究方法**：剖析 policy-as-prompt 的技术属性（可复现性、一致性问题）与治理属性，推导其对社区自治的风险并提出改进考量
- 📌 **结论**：仅靠写提示不足以支撑有意义的社区治理，需针对可问责性与程序正当性补充机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content moderation practices and governance paradigms are changing rapidly, as fewer human moderators are deployed as `experts' by social media companies in a centralized manner. Instead, the companies are focusing more on community approaches, relying on volunteers to provide accurate information and make correct decisions. In decentralized moderation, communities have always relied on volunteers, updated community guidelines, and internal discussions thereof. For both content moderation paradigms, Artificial Intelligence (AI) seems like it could help ease moderation burdens of time, mental health, and accuracy. One possible way to operationalize AI in content moderation is a `policy-as-prompt'' approach, where the policy is formulated as a natural-language prompt and then passed to a large language model (LLM). This model then aids in moderation tasks. In this paper, we briefly lay out the technical and governance properties of this approach, and argue that its limitations lead to specific risks and harms that have to be addressed. Towards alleviating them, we lay out multiple considerations towards more effective prompt governance, but ultimately find that writing prompts alone is not appropriate for ensuring meaningful community governance.

</details>

### 32. SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing

📄 [arXiv](https://arxiv.org/abs/2606.29887)　📅 2026-06

**关键词**：`benchmark`、`in-context policy guard`、`hierarchical rules`、`multi-turn dialogue`

👤 **作者**：Jiacheng Zhang、…、Feng Liu

- 🎯 **研究动机**：真实应用要求护栏按上下文给定的应用策略判定违规，in-context 策略护栏能力缺乏系统基准
- 🔬 **研究方法**：构建 SafePyramid：10 域 1,000 段多轮对话+3,000 条应用策略共 61,699 条自然语言规则，按 L0 单规则理解、L1 规则依赖推理、L2 新策略框架适应三级评估 10 个 LLM 与 5 个可配置护栏
- 📌 **结论**：最佳模型 GPT-5.5 在 L0/L1/L2 上完整识别全部违规规则的比例分别仅 54.0%、35.3%、12.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In real-world applications, guardrails are often expected to identify unsafe user-model interactions according to application-specific safety policies, rather than relying on predefined risk taxonomies. In this work, we study this setting under the paradigm of in-context policy guardrailing, where guardrails predict safety violations based on policy specifications provided in context. To systematically evaluate this capability, we introduce SafePyramid, a safety benchmark comprising 1,000 multi-turn conversations across 10 domains and 3,000 corresponding application-specific policies, which together contain 61,699 distinct natural-language rules. SafePyramid organizes the evaluation into three difficulty levels: L0 evaluates individual-rule understanding, L1 evaluates reasoning over rule dependencies, and L2 evaluates adaptation of full novel policy frameworks defined in context. To ensure benchmark quality, we employ a rigorous multi-stage pipeline to construct and validate the benchmark. Using SafePyramid, we evaluate 10 frontier LLMs and 5 policy-configurable guardrails and find that in-context policy guardrailing remains highly challenging: even the best-performing model, GPT-5.5, exactly identifies the full set of violated rules in only 54.0%, 35.3%, and 12.9% cases on L0, L1, and L2, respectively. These results highlight the limitations of current guardrails and call for stronger in-context policy guardrails that can reliably execute policies, resolve rule dependencies, and adapt to novel policy frameworks.

</details>

### 33. PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media

📄 [arXiv](https://arxiv.org/abs/2605.17187) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1590/)　📅 2026-05　🏷 ACL 2026

**关键词**：`benchmark`、`community-specific rule`、`multilingual moderation`、`multimodal context`

👤 **作者**：Zoher Kachwala、Bao Tran Truong、Rasika Muralidharan、Haewoon Kwak、Jisun An、Filippo Menczer

- 🎯 **研究动机**：社交媒体转向社区自治的多元主义，一个社区的违规在另一个可能完全可接受，AI 能否执行社区规范未知
- 🔬 **研究方法**：PluRule 多模态多语言基准：给定评论与上下文，从 1,989 个 Reddit 社区的 2,885 条规则中选出违反项，含 13,371 个违规、9 种语言
- 📌 **结论**：SOTA VLM 表现挣扎——GPT-5.2 高推理仅略优于平凡基线，更大模型与更多上下文收益边际

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Social media are shifting towards pluralism -- community-governed platforms where groups define their own norms. What violates rules in one community may be perfectly acceptable in another. Can AI models help moderate such pluralistic communities? We formalize the task as a multiple-choice problem, mirroring how human moderators operate in the real world: given a comment and its surrounding context, identify which specific rule, if any, is violated. We introduce PluRule, a multimodal, multilingual benchmark for detecting 13,371 rule violations across 1,989 Reddit communities spanning 2,885 rules in 9 languages. Using this benchmark, we show that state-of-the-art vision-language models struggle significantly: even GPT-5.2 with high reasoning performs only slightly better than a trivial baseline. We also find that bigger models and increased context provide marginal gains, and universal rules like civility and self-promotion are easier to detect. Our results show that moderation of pluralistic communities on social media is a fundamental challenge for language models. Our code and benchmark are publicly available.

</details>

### 34. Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges

📄 [arXiv](https://arxiv.org/abs/2605.06161)　📅 2026-05

**关键词**：`analysis`、`policy invariance`、`safety judge`、`rubric robustness`

👤 **作者**：Shihao Weng、Yang Feng、Xiaofei Xie

- 🎯 **研究动机**：LLM-as-Judge 的判决被当作真值代理，却无人检验其取决于 agent 行为还是评估政策的措辞
- 🔬 **研究方法**：提出政策不变性三原则（语义等价改写不变、严格度变化应响应、歧义感知校准），对四个 agent 类 judge 做压力测试
- 📌 **结论**：保内容政策改写可翻转高达 9.1% 判决，18-43% 翻转发生在无歧义案例；Policy Invariance Score 与 Judge Card 暴露纯准确率榜单看不见的数量级可靠性差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-as-a-Judge pipelines have become the de facto evaluator for agent safety, yet existing benchmarks treat their verdicts as ground-truth proxies without checking whether the verdicts depend on the agent's behavior or merely on how the evaluation policy happens to be worded. We argue that any trustworthy safety judge must satisfy a basic property we call policy invariance, and we operationalize it as three testable principles: rubric-semantics invariance under certified-equivalent rewrites, rubric-threshold invariance under intentional strict-to-lenient shifts, and ambiguity-aware calibration so that verdict instability concentrates on genuinely ambiguous cases. Instantiating these principles as a stress-test protocol with four agent-class judges on trajectories drawn from ASSEBench and R-Judge, we surface a previously unmeasured failure mode: today's judges respond to meaningful normative shifts and to meaningless structural rewrites with comparable strength, and cannot tell the two apart. Content-preserving policy rewrites flip up to 9.1% of verdicts above baseline jitter, and 18-43% of all observed flips occur on unambiguous cases under such rewrites, so existing safety scores conflate what the agent did with how the evaluator was prompted. Beyond the diagnosis, we contribute the Policy Invariance Score and the Judge Card reporting protocol, which expose an order-of-magnitude spread in judge reliability that is invisible to accuracy-only leaderboards. We release the protocol and code so that future agent-safety benchmarks can audit their own evaluators rather than trust them by default.

</details>

### 35. Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation

📄 [arXiv](https://arxiv.org/abs/2605.24247)　📅 2026-05

**关键词**：`analysis`、`constitutional definition`、`label consistency`、`AI evaluation`

👤 **作者**：Konstantin Berlin、Adam Swanda

- 🎯 **研究动机**：简单类别定义不足以产出一致 gold 标签，而详细到能定分界的定义又超出人类标注者工作记忆
- 🔬 **研究方法**：AI 辅助撰写逐类 constitution 定义，由前沿 LLM 据此逐条判读产出 gold 标签，人只负责类别含义的高层决策
- 📌 **结论**：三个内容审核类别上跨模型不一致最多降 57 倍；安全评估引入意图与内容双轴独立打分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many automated labeling pipelines classify inputs into categories defined by a written specification, content moderation being a prominent use case. Simple category definitions are not detailed enough for labelers to produce the accurate, consistent golden labels these pipelines require. One solution is to write a prescriptive definition that settles enough real boundary cases that labelers cannot disagree with the written interpretation. In practice, definitions at that level of detail exceed what a human annotator can hold in working memory, so annotators fall back on intuition and the labels drift from the written rules, regressing on accuracy and consistency. We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document. We evaluate on three content moderation categories (harassment, hate speech, non-violent crime) and show that the approach reduces cross-model inconsistency by up to 57x compared to paragraph definitions, with cross-model disagreement diagnosing specification gaps and the human responsible for high-level decisions about what each category should mean rather than individual labeling calls. For the safety evaluation, we introduce a dual-axis formulation scoring intent and content independently over the full conversation, so downstream consumers can act on either axis or both.

</details>

### 36. GMP: A Benchmark for Content Moderation under Co-occurring Violations and Dynamic Rules

📄 [arXiv](https://arxiv.org/abs/2603.01724)　📅 2026-03

**关键词**：`benchmark`、`dynamic moderation rule`、`co-occurring violation`、`policy generalization`

👤 **作者**：Houde Dong、Yifei She、Kai Ye、Liangcai Su、Chenxiong Qian、Jie Hao

- 🎯 **研究动机**：静态基准高分并不保证 LLM 能应对单帖多重违规与平台规则动态变化的真实审核
- 🔬 **研究方法**：提出 GMP 基准，把共现违规（如偏见加人身攻击）与动态审核规则纳入同一评测，检验策略泛化
- 📌 **结论**：在固定准则下表现好的模型面对组合违规与规则漂移时判别力退化，导致误删或漏放

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online content moderation is essential for maintaining a healthy digital environment, and reliance on AI for this task continues to grow. Consider a user comment using national stereotypes to insult a politician. This example illustrates two critical challenges in real-world scenarios: (1) Co-occurring Violations, where a single post violates multiple policies (e.g., prejudice and personal attacks); (2) Dynamic rules of moderation, where determination of a violation depends on platform-specific guidelines that evolve across contexts . The intersection of co-occurring harms and dynamically changing rules highlights a core limitation of current AI systems: although large language models (LLMs) are adept at following fixed guidelines, their judgment capabilities degrade when policies are unstable or context-dependent . In practice, such shortcomings lead to inconsistent moderation: either erroneously restricting legitimate expression or allowing harmful content to remain online . This raises a critical question for evaluation: Does high performance on existing static benchmarks truly guarantee robust generalization of AI judgment to real-world scenarios involving co-occurring violations and dynamically changing rules?

</details>

### 37. Poly-Guard: Massive Multi-Domain Safety Policy-Grounded Guardrail Dataset

📄 [arXiv](https://arxiv.org/abs/2506.19054) · 📊 [Dataset](https://huggingface.co/datasets/Virtue-AI-HUB/PolyGuard)　📅 2025-06　🏷 NeurIPS 2025

**关键词**：`benchmark`、`multi-domain policy`、`adversarial instance`、`over-refusal`

👤 **作者**：Mintong Kang、…、Bo Li

- 🎯 **研究动机**：现有护栏基准的风险分类学临时拼凑、缺政策依据，且忽视同一风险在不同领域的差异
- 🔬 **研究方法**：构建首个多领域政策锚定护栏数据集 Poly-Guard：八大安全攸关领域、真实政策构建风险、多种交互格式、解毒提示与攻击增强样本
- 📌 **结论**：19 个护栏模型评测显示跨风险类别 F1 方差大、常见类别性能可能随版本下降，且全部可被优化对抗攻击攻破

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs become widespread across diverse applications, concerns about the security and safety of LLM interactions have intensified. Numerous guardrail models and benchmarks have been developed to ensure LLM content safety. However, existing guardrail benchmarks are often built upon ad hoc risk taxonomies that lack a principled grounding in standardized safety policies, limiting their alignment with real-world operational requirements. Moreover, they tend to overlook domain-specific risks, while the same risk category can carry different implications across different domains. To bridge these gaps, we introduce Poly-Guard, the first massive multi-domain safety policy-grounded guardrail dataset. Poly-Guard offers: (1) broad domain coverage across eight safety-critical domains, such as finance, law, and codeGen; (2) policy-grounded risk construction based on authentic, domain-specific safety guidelines; (3) diverse interaction formats, encompassing declarative statements, questions, instructions, and multi-turn conversations; (4) advanced benign data curation via detoxification prompting to challenge over-refusal behaviors; and (5) \textbf{attack-enhanced instances} that simulate adversarial inputs designed to bypass guardrails. Based on Poly-Guard, we benchmark 19 advanced guardrail models and uncover a series of findings, such as: (1) All models achieve varied F1 scores, with many demonstrating high variance across risk categories, highlighting their limited domain coverage and insufficient handling of domain-specific safety concerns; (2) As models evolve, their coverage of safety risks broadens, but performance on common risk categories may decrease; (3) All models remain vulnerable to optimized adversarial attacks. We believe that \dataset and the unique insights derived from our evaluations will advance the development of policy-aligned and resilient guardrail systems.

</details>

### 38. The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions

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

### 39. COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.2139/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`safety alignment`、`policy-aware guardrail`、`runtime policy`、`fine-tuning robustness`、`safety–utility trade-off`

👤 **作者**：Dasol Choi、…、Minsuk Kahng

- 🎯 **研究动机**：现有安全评测只关注普适危害，组织特定的允许与禁止清单政策合规缺乏评估框架
- 🔬 **研究方法**：COMPASS 在八个行业场景生成并验证 5920 条查询，测常规合规与经边缘案例设计的对抗鲁棒性，评估七个 SOTA 模型
- 📌 **结论**：根本不对称：合法请求处理准确率超 95%，但对对抗性禁止清单违规仅拒绝 13 至 40%，当前 LLM 不具备政策关键部署所需鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models are deployed in high-stakes enterprise applications, from healthcare to finance, ensuring adherence to organization-specific policies has become essential. Yet existing safety evaluations focus exclusively on universal harms. We present COMPASS (Company/Organization Policy Alignment Assessment), the first systematic framework for evaluating whether LLMs comply with organizational allowlist and denylist policies. We apply COMPASS to eight diverse industry scenarios, generating and validating 5,920 queries that test both routine compliance and adversarial robustness through strategically designed edge cases. Evaluating seven state-of-the-art models, we uncover a fundamental asymmetry: models reliably handle legitimate requests (>95% accuracy) but catastrophically fail at enforcing prohibitions, refusing only 13–40% of adversarial denylist violations. These results demonstrate that current LLMs lack the robustness required for policy-critical deployments, establishing COMPASS as an essential evaluation framework for organizational AI safety.

</details>

### 40. DUET: Dual-Teacher On-Policy Distillation via Same-Weight Disagreement for Prohibition Compliance

📄 [arXiv](https://arxiv.org/abs/2608.14644)　📅 2026-08

**关键词**：`analysis`、`policy-aware guardrail`、`runtime policy`、`policy compliance`

👤 **作者**：Zihan Li、Feifei Li、Wenhui Que

- 🎯 **研究动机**：运行时注入的禁令随请求与租户变化，SFT 把违规信号藏进合规标签、DPO 序列级偏好错配 token 局部违规
- 🔬 **研究方法**：DUET 双教师同权重在线策略蒸馏：见禁令与不见禁令两教师的逐 token 分歧隔离禁令因果效应，驱动信号清洗与偏好导向学习
- 📌 **结论**：1.5B-8B Qwen 上达成 72.3-85.2% 违禁合规同时保留 88-93% 正常效用，大幅超过教师模型与蒸馏基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant. Conventional post-training is structurally ill-suited: SFT hides the violation signal in compliant labels, and DPO's sequence-level preferences mismatch token-localized violations. We propose DUET, a token-selective on-policy distillation method for prohibition compliance. DUET pairs a teacher that sees the prohibition (positive) with an identical-weight teacher that does not (negative). Because the two teachers differ only in prohibition visibility, their per-token disagreement isolates the prohibition's causal effect--yielding a clean supervision signal uncontaminated by model capacity or mismatch. This disagreement drives two complementary mechanisms: signal cleaning, which discards agreement tokens as redundant or prefix-corrupted, and preference-directed learning, which pushes the student away from the negative teacher and toward the positive one at token granularity, embedding DPO-style optimization directly into OPD without offline preference data. We construct an industrial Prohibition-Compliance benchmark spanning five task families covering explicit-refusal, paraphrase robustness, and over-refusal. Across 1.5B-8B Qwen variants, DUET achieves 72.3-85.2% violation compliance while preserving 88-93% normal utility, dramatically outperforming teacher model and other distillation baselines. External evaluation on SysBench confirms improved safety alignment with minimal degradation on GSM8K and MATH-500.

</details>