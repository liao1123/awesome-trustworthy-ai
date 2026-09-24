## 研究方向

本页主要研究与具体安全风险绑定的 Agent trajectory monitoring：攻击链、policy violation、unsafe tool use、高后果内生故障、风险步骤定位、运行时 guard 和可审计 provenance；同时收录会直接影响安全干预设计的 monitor-signal validity 与 attribution-component boundary。一般任务失败、普通 debugging、成功率预测和工作流恢复不纳入；若论文只以一般任务失败验证可复用监控组件，则必须明确其证据尚未覆盖安全后果。

## 研究脉络

- **安全过程建模：** 监控对象从最终有害输出扩展到 instruction、tool call、state change 与 policy-compliance trajectory。
- **内生高后果风险：** 即使没有攻击者，长程小错误也可能累积为不可逆或高后果行为，需要定位最早风险步骤。
- **Guard 与过程监督：** trajectory reward、latent risk evidence 和结构化 guardrail 用于在执行期间发现并阻断 unsafe action。
- **可审计证据：** provenance signal 和 execution evidence 用于在日志缺失或文本被拼接后恢复责任边界。
- **信号有效性边界：** 早期 uncertainty、可见 rationale 和异常分数必须相对后续真实行为校验，普通 failure proxy 不能直接升级为 safety guarantee。
- **当前边界：** 一般 task failure 与安全故障不能混为一谈；通用归因或预测工作只在直接检验可复用监控组件时作为边界证据进入，并必须标明尚未证明具体风险识别或安全干预效果。

## Provenance 与 Failure Attribution

### 1. Detect Before You Attribute: Cascade Failure Attribution for Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.29646)　📅 2026-09

**关键词**：`detection`、`cascade failure`、`semantic-structural filtering`、`step-level attribution`

👤 **作者**：Jiayi Zhang、…、Jingjing Li

- 🎯 **研究动机**：拓扑／频谱归因忽略细粒度语义，LLM 归因又受长轨迹上下文退化影响，多 Agent 失败归因精度受限
- 🔬 **研究方法**：提出 detect-before-attribute 插件 DuoTrace：双视图语义-结构节点表示加 Tree-LSTM 轨迹编码与前缀链／LLM 数据增强做 VAE 异常检测，再向下游 LLM 归因供聚焦证据
- 📌 **结论**：使六种 LLM 归因基线的 agent 级与 step 级准确率分别提升 8.7% 和 7.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-based agents have shown strong potential in solving complex tasks through multi-step reasoning, yet they remain vulnerable to execution failures. Accurate failure attribution is therefore critical for improving agent reliability. Existing topology- and spectrum-based methods exploit trajectory structures but often overlook fine-grained semantics, while LLM-based attribution methods capture semantic cues but suffer from long-context degradation over lengthy trajectories. To address these challenges, we propose DUOTRACE, a plug-and-play detection filter for LLM-based failure attribution. DUOTRACE follows a detect-before-attribute paradigm: it first detects anomalous executions and then supplies focused trajectory evidence to downstream LLM-based attribution methods. For effective VAE-based anomaly detection on agent trajectories, DUOTRACE integrates dual-view semantic-structural node representations, a Tree-LSTM-based trajectory encoder, and prefix-chain- and LLM-based data augmentation to handle heterogeneous nodes, hierarchical execution structures, and limited failure data. Experiments with six LLM-based attribution baselines show that DUOTRACE improves agent-level and step-level attribution accuracy by 8.7% and 7.0%, respectively.

</details>

### 2. ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.27496)　📅 2026-08

**关键词**：`defense`、`pre-execution guard`、`origin policy`、`sensitive parameter`、`runtime reference monitor`、`parameter admission`

👤 **作者**：Xinhang Ma、Chaowei Xiao、William Yeoh、Ning Zhang、Yevgeniy Vorobeychik

- 🎯 **研究动机**：Agent 能力增强后工具序列与参数值多在运行时确定，仅凭用户查询做工具筛查或信息流控制会显著损失效用
- 🔬 **研究方法**：提出 ROPE：值只有不可伪造地追溯到用户、用户指定来源或用户权威记录才可进入有状态工具的敏感参数；对被审计参数集做确定性 origin check，LLM 仅介入可信用户请求
- 📌 **结论**：在四种 Agent 模型上把攻击成功率限制在 1.6%–2.6%，保留 82%–100% 无防御干净效用，使击穿既有防御的长程攻击成功率归零，并附两条可证明保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Indirect prompt injection (IPI) plants instructions in the content a tool-using LLM agent reads, steering the agent into harmful tool calls. The strongest defenses are system-level, leveraging techniques such as task-conditional tool screening to prevent execution of malicious tools, and information-flow control to avoid tool execution with untrusted parameters. However, as agents grow more capable, users delegate more to automation. Consequently, tool execution sequences and parameter values are increasingly determined at runtime and cannot be reliably screened from solely user's query without significant utility loss. We present ROPE (Routed Origin Policy Enforcement), which is anchored in a structural notion of trust: a value may reach a state-changing tool only if it traces unforgeably to the user, a source the user explicitly named, or the user's own authoritative records. Enforcement is then a deterministic origin check over an audited set of sensitive tool parameters, and the only reliance on a language model involves solely the trusted user request, out of the attacker's reach. Our approach admits two provable guarantees: 1) at every step of a trajectory, no value whose only origin is attacker-writable content reaches an origin-guarded parameter, and 2) no rewording of an injection changes an admission decision. We evaluate across four agent models on open-ended agent suites, ROPE holds attack success rate to 1.6--2.6\% while retaining 82--100\% of undefended clean utility, significantly exceeding state-of-the-art system-level defenses in utility while attaining comparable or better security. Further, we show that optimizing the injection against ROPE is largely ineffective, while long-horizon attacks that defeat prior system-level defenses achieve zero success rate. Our code and logs are available at https://github.com/xhOwenMa/ROPE .

</details>

### 3. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.27146)　📅 2026-08

**关键词**：`defense`、`action authorization`、`provenance tracking`、`indirect prompt injection`、`runtime authorization`、`provenance contract`

👤 **作者**：Xiaokun Guo、…、Yu Wang

- 🎯 **研究动机**：工具输出可从提供数据变成指定具体动作的命令并引发越权副作用，根源是现有 Agent 把动作诱导与执行授权混为一谈
- 🔬 **研究方法**：提出 SARA，将动作诱导与执行授权拆为独立运行时角色：上下文隔离的 Action Probe 暴露诱导语义并跨步记录 action provenance，工具调用仅凭用户目标与已授权执行证据放行，No-History-Promotion 防止历史递归洗白来源
- 📌 **结论**：在 AgentDojo 与 AgentDyn 四个主要设置中 ASR 不超过 0.63%，任务效用保持竞争力，且在多个 Agent backbone 上一致降低 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority. On the Observation side, a context-isolated Action Probe exposes action-inducing semantics and persistently records action-origin provenance across steps as a review signal; on the execution side, actual tool calls are authorized only against the user objective and audited evidence from authorized successful executions, while satisfying goal, execution-chain, and argument-level support. To preserve this separation across multi-step execution, SARA applies No-History-Promotion to prevent historical recurrence from laundering action origins into execution authority. Across AgentDojo and AgentDyn, SARA limits ASR to no more than \(0.63\%\) across four primary evaluation settings while maintaining competitive task utility, and consistently reduces ASR across additional Agent backbones.

</details>

### 4. HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

📄 [arXiv](https://arxiv.org/abs/2608.22512)　📅 2026-08

**关键词**：`defense`、`runtime witnessing`、`external choke point`、`tamper-resistant evidence`、`attribution laundering`、`multi-agent accountability`

👤 **作者**：Christos Sardianos、…、Georgios Th. Papadopoulos

- 🎯 **研究动机**：自主多 agent 系统致害时无法查清事实、原因与责任：溯源取证抽象层级错误、形式因果假设因果模型已知、审计信任 agent 自我记录，而 attribution laundering 可把行为摊到冗余 agent 直到谁都不是 but-for cause
- 🔬 **研究方法**：HANSARD 参考架构：在 agent 触及范围外的五个 choke point 捕获证据使遗漏可检测，运行时累积 PROV-DM 类型化因果图并以三个指标实时门控监督，事后按 modified Halpern-Pearl 重放得出偶然效应与补偿集大小，synergy residual 度量组合致害
- 📌 **结论**：原因、责任与问责分开报告并各受证据层级上限约束，使 attribution laundering 可见，不再依赖涉事 agent 自产日志

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, attribution laundering, i.e., spreading an act across redundant agents until none is a but-for cause. Worse, the record is produced by the suspects, which comprises the assumption adopted throughout this work. Agents may therefore anticipate the investigation and the part of logging infrastructure may itself collude. In this paper, HANSARD is proposed, a reference architecture treating accountability as a life-cycle property. First, a readiness profile sealed before operation bounds what later findings may claim. Second, capturing at five choke points beyond the agents' reach makes omissions detectable, not only tampering. Third, a typed PROV-DM-aligned causal graph accrues as the system runs, and three indicators read it live to gate oversight without adjudicating. Fourth, post-incident replay yields contingent effects under the modified Halpern-Pearl definition, together with a compensation-set size. Finally, a synergy residual measures harm due to the combination rather than to individuals, making laundering visible. Cause, responsibility and accountability are then reported separately, each capped by an evidentiary tier, while a future research agenda is also provided.

</details>

### 5. When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Auditing

📄 [arXiv](https://arxiv.org/abs/2603.17445)　📅 2026-03

**关键词**：`analysis`、`provenance watermark`、`metadata-free auditing`、`segment attribution`

👤 **作者**：Yi Nian、…、Yue Zhao

- 🎯 **研究动机**：执行日志与 agent 身份因隐私或系统边界丢失时，最终文本是唯一可审计工件，事后归因方法失效
- 🔬 **研究方法**：IET 在生成时把 agent 专属、密钥条件的统计信号嵌入 token 生成，离线审计员凭密钥注册表仅从最终文本恢复段边界与逐段 agent 归属
- 📌 **结论**：在身份删除、边界破坏与隐私删改下仍实现准确的段级归因，且不损生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a multi-agent system produces an incorrect or harmful answer, who is accountable if execution logs and agent identifiers are unavailable? In practice, generated content is often detached from its execution environment due to privacy or system boundaries, leaving the final text as the only auditable artifact. Existing attribution methods rely on full execution traces and thus become ineffective in such metadata-deprived settings. We propose Implicit Execution Tracing (IET), a provenance-by-design framework that shifts attribution from post-hoc inference to built-in instrumentation. Rather than inferring provenance after the fact, IET embeds agent-specific, key-conditioned statistical signals into the token generation process at generation time, turning the output text into a self-verifying provenance record. An offline auditor, holding a verification registry that maps each agent to its key, then recovers segment-level provenance - segment boundaries and per-segment agent attribution - from the final text alone without access to execution logs or private traces. Experiments across diverse multi-agent coordination settings demonstrate that IET achieves accurate segment-level attribution and reliable transition recovery under identity removal, boundary corruption, and privacy-preserving redaction, while maintaining generation quality. These results show that embedding provenance into generation provides a practical foundation for accountability in multi-agent language systems under metadata loss.

</details>

### 6. VET Your Agent: Towards Host-Independent Autonomy via Verifiable Execution Traces

📄 [arXiv](https://arxiv.org/abs/2512.15892) · 🌐 [Project](https://doi.org/10.1145/3779208.3786259)　📅 2025-12　🏷 ACM CCS 2026

**关键词**：`defense`、`agent provenance`、`verifiable trace`、`host tampering`、`agent integrity`、`verifiable execution trace`

👤 **作者**：Artem Grigor、Christian Schroeder de Witt、Simon Birnbach、Ivan Martinovic

- 🎯 **研究动机**：agent 在宿主控制的基础设施上执行，宿主可篡改模型、输入或输出，自主性失去意义
- 🔬 **研究方法**：VET 框架以 Agent Identity Document 规定配置与证明系统，组合可信硬件、简洁密码学证明与 notarized TLS 转录（Web Proofs）实现宿主无关的 agent 输出认证
- 📌 **结论**：对黑盒含密 API 调用 Web Proofs 最实用（开销通常低于 3 倍），公开 API 用 TEE 代理即可；可验证交易 agent 案例验证了组合部署

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large language models (LLMs) have enabled a new generation of autonomous agents that operate over sustained periods and manage sensitive resources on behalf of users. Trusted for their ability to act without direct oversight, such agents are increasingly considered in high-stakes domains including financial management, dispute resolution, and governance. Yet in practice, agents execute on infrastructure controlled by a host, who can tamper with models, inputs, or outputs, undermining any meaningful notion of autonomy. We address this gap by introducing VET (Verifiable Execution Traces), a formal framework that achieves host-independent authentication of agent outputs and takes a step toward host-independent autonomy. Central to VET is the Agent Identity Document (AID), which specifies an agent's configuration together with the proof systems required for verification. VET is compositional: it supports multiple proof mechanisms, including trusted hardware, succinct cryptographic proofs, and notarized TLS transcripts (Web Proofs). We implement VET for an API-based LLM agent and evaluate our instantiation on realistic workloads. We find that for today's black-box, secret-bearing API calls, Web Proofs appear to be the most practical choice, with overhead typically under 3$\times$ compared to direct API calls, while for public API calls, a lower-overhead TEE Proxy is often sufficient. As a case study, we deploy a verifiable trading agent that produces proofs for each decision and composes Web Proofs with a TEE Proxy. Our results demonstrate that practical, host-agnostic authentication is already possible with current technology, laying the foundation for future systems that achieve full host-independent autonomy.

</details>

### 7. CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents

📄 [arXiv](https://arxiv.org/abs/2608.30147)　📅 2026-09

**关键词**：`defense`、`action-level critique`、`process supervision`、`irreversible tool action`

👤 **作者**：Amir Saeidi、…、Chitta Baral

- 🎯 **研究动机**：长程工具调用中单个不可逆错误动作须在执行前拦截，但优化式方法缺少系统产出验证 rationale 的途径
- 🔬 **研究方法**：提出 CAST，把稀疏任务结果转为 action-level critique 监督：分析轨迹合成部分可观测下动作有效性的结构化 rationale，再构造 critique-aware 数据优化策略模型
- 📌 **结论**：微调 Qwen3 系模型在动态工具调用基准上跨域提升可靠性，Retail pass^4 超 GPT-OSS-120B 逾 10%，域外 Telehealth 再提 9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be intercepted before execution. Such failures may not appear in every single run, but can emerge across repeated trials, making reliability across steps and trials critical. However, ensuring agentic reliability is challenging: even frontier LLMs struggle to explain why an action may be wrong, especially in long, intertwined trajectories governed by domain-specific policies. Much recent work relies on prompt-based critique agents, while optimization-based methods lack a systematic way to produce rich verification rationales for training. We address this gap with CAST, a critique-aware training framework that converts sparse task outcomes into action-level supervision for critique learning and policy optimization. CAST analyzes agent trajectories to synthesize structured rationales explaining action validity under partial observability. The resulting critique model is used to construct critique-aware training data for optimizing the policy model. Fine-tuning Qwen3-family models on dynamic tool-calling benchmarks, CAST improves reliability across domains, outperforming GPT-OSS-120B by over 10% pass^4 on Retail tasks and yielding an additional 9% improvement on Telehealth in an out-of-domain setting. These results demonstrate that critique-aware training improves the robustness of LLM agents in realistic dynamic environments.

</details>

### 8. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

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

### 9. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

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

### 10. PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents

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

### 11. SafeBranch: Branch-Pair Safety Alignment for Embodied Agents

📄 [arXiv](https://arxiv.org/abs/2608.19729)　📅 2026-08

**关键词**：`defense`、`interactive agent safety`、`branch-pair alignment`、`unsafe-action correction`、`risk-step localization`、`environment rollback`

👤 **作者**：Hyunse Lee、Jiwoo Jeong、Haneul Lee、Kyochul Jang、Youngjae Yu、Woojin Lee

- 🎯 **研究动机**：具身 agent 的安全只在轨迹中少数关键步出现，模仿安全轨迹不解释为何安全，任意安全/不安全对比混入无关差异
- 🔬 **研究方法**：SafeBranch 从自身不安全 rollout 经环境回滚构造分支对：回滚到致违关键步、查询 actor 安全替代，原动作与替代仅在该步配对；部署时无 critic
- 📌 **结论**：IS-Bench、SafetyALFRED 与 OOD 变体上可靠安全且不牺牲任务成功，未见物体变体上安全成功约为未训练基线的十倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting arbitrary safe and unsafe trajectories mixes the safety signal with unrelated differences. We propose SafeBranch, a framework that aligns an embodied actor on safety through branch pairs constructed from the actor's own unsafe rollouts via environment rollback. SafeBranch rolls each unsafe rollout back to the safety-critical step that caused the violation, queries the actor for a safe alternative, and pairs the original action with the alternative so that the two branches differ only at that step. The trained actor acts safely at deployment with no critic in the loop. On IS-Bench, SafetyALFRED, and out-of-distribution variants with unseen tasks and objects, it handles safety reliably without sacrificing task success, achieving roughly ten times more safe successes than the untrained baseline on the unseen-object variant.

</details>

### 12. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21126)　📅 2026-08

**关键词**：`defense`、`task-effect contract`、`delegated authority`、`lifecycle governance`、`contract-governed guardrail`、`authority boundary`

👤 **作者**：Bohao Liao、Jingchao Wang、Qipeng Song、Jin Cao、Jieling Wang、Boyu Deng

- 🎯 **研究动机**：联网 Agent 任务内容可夹带间接 prompt injection 重定向工具或篡改参数，现有防御只约束不可信内容或单次调用，用户意图、运行时证据与实际效果间缺乏闭环
- 🔬 **研究方法**：TraceGrant 以显式 Contract 治理任务效果生命周期：执行前从可信用户请求建立 task-effect 边界，执行中证据只能实例化 Contract 已确立的权限，执行后按实际工具结果验证任务完成
- 📌 **结论**：949 个 AgentDojo 与 400 个 Agent Security Bench 攻击案例中零攻击成功，攻击下效用保留率分别为 77.32% 与 83.00%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidence, realized effects, and task completion insufficiently connected. We present TraceGrant, a security framework that governs the task-effect lifecycle of networked LLM agents through an explicit Contract. Before execution, TraceGrant establishes a task-effect boundary from the trusted user request. During execution, admitted evidence can instantiate only authority already established by the Contract. After execution, task completion is verified against actual tool results. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed benchmark settings, TraceGrant recorded no attack successes while retaining utility under attack rates of 77.32% and 83.00%, respectively. We further evaluate TraceGrant through white-box defense-aware attacks, Contract quality analysis, stage ablations, targeted stress tests, and runtime overhead measurements. The results show that TraceGrant provides a unified governance layer that connects trusted user intent, runtime evidence, concrete tool execution, and verified task completion.

</details>

### 13. HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark

📄 [arXiv](https://arxiv.org/abs/2604.13954)　📅 2026-04

**关键词**：`benchmark`、`intrinsic risk`、`risk-step localization`、`benign trajectory`

👤 **作者**：Jiacheng Wang、Jinchang Hou、Fabian Wang、Ping Jian、Chenfu Bao、Zhonghou Lv

- 🎯 **研究动机**：Agent 安全评测聚焦外部攻击，良性条件下内源风险沿长轨迹潜伏传播并演化为高后果的设定未被研究
- 🔬 **研究方法**：HINTBench 含 629 条轨迹（523 危险、106 安全，平均 33 步），支持风险检测、风险步定位与失败类型识别，按五约束 taxonomy 标注
- 📌 **结论**：强 LLM 轨迹级风险检测尚可，但风险步定位 Strict-F1 降至 35 以下，现有 guard 模型迁移很差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benchmark of 629 agent trajectories (523 risky, 106 safe; 33 steps on average) supporting three tasks: risk detection, risk-step localization, and intrinsic failure-type identification. Its annotations are organized under a unified five-constraint taxonomy. Experiments reveal a substantial capability gap: strong LLMs perform well on trajectory-level risk detection, but their performance drops to below 35 Strict-F1 on risk-step localization, while fine-grained failure diagnosis proves even harder. Existing guard models transfer poorly to this setting. These findings establish intrinsic risk auditing as an open challenge for agent safety.

</details>

### 14. Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling

📄 [arXiv](https://arxiv.org/abs/2604.08178) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1062/)　📅 2026-04　🏷 ACL 2026

**关键词**：`benchmark`、`trajectory reward`、`planning preference`、`Plan-RewardBench`

👤 **作者**：Jiaxuan Wang、Yulan Hu、Wenjin Yang、Zheng Pan、Xin Li、Lan-Zhe Guo

- 🎯 **研究动机**：工具集成环境下 reward model 的能力缺乏专门评测基准
- 🔬 **研究方法**：Plan-RewardBench 覆盖安全拒答、工具无关或不可用、复杂规划与错误恢复四类任务，含真实正轨迹与难负样本，以统一成对协议评测三类 RM
- 📌 **结论**：generative、discriminative 与 LLM-as-Judge 三类评测器均表现不佳，长轨迹上性能急剧退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In classical Reinforcement Learning from Human Feedback (RLHF), Reward Models (RMs) serve as the fundamental signal provider for model alignment. As Large Language Models evolve into agentic systems capable of autonomous tool invocation and complex reasoning, the paradigm of reward modeling faces unprecedented challenges -- most notably, the lack of benchmarks specifically designed to assess RM capabilities within tool-integrated environments. To address this gap, we present Plan-RewardBench, a trajectory-level preference benchmark designed to evaluate how well judges distinguish preferred versus distractor agent trajectories in complex tool-using scenarios. Plan-RewardBench covers four representative task families -- (i) Safety Refusal, (ii) Tool-Irrelevance / Unavailability, (iii) Complex Planning, and (iv) Robust Error Recovery -- comprising validated positive trajectories and confusable hard negatives constructed via multi-model natural rollouts, rule-based perturbations, and minimal-edit LLM perturbations. We benchmark representative RMs (generative, discriminative, and LLM-as-Judge) under a unified pairwise protocol, reporting accuracy trends across varying trajectory lengths and task categories. Furthermore, we provide diagnostic analyses of prevalent failure modes. Our results reveal that all three evaluator families face substantial challenges, with performance degrading sharply on long-horizon trajectories, underscoring the necessity for specialized training in agentic, trajectory-level reward modeling. Ultimately, Plan-RewardBench aims to serve as both a practical evaluation suite and a reusable blueprint for constructing agentic planning preference data.

</details>

### 15. TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories

📄 [arXiv](https://arxiv.org/abs/2604.07223) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04　🏷 COLM 2026

**关键词**：`benchmark`、`mid-trajectory safety`、`structured trace`、`guardrail evaluation`、`tool-call trajectory`、`mid-step guardrail`

👤 **作者**：Yen-Shan Chen、Sian-Yao Huang、Cheng-Lin Yang、Yun-Nung Chen

- 🎯 **研究动机**：安全护栏评测集中在自然语言最终输出，多步工具调用轨迹的中途风险长期缺乏系统基准
- 🔬 **研究方法**：TraceSafe-Bench 覆盖 12 类风险、1000+ 执行实例，评测 13 个 LLM-as-a-guard 模型与 7 个专用护栏
- 📌 **结论**：护栏效果由结构化数据能力主导（与结构化基准相关 ρ=0.79）而与 jailbreak 鲁棒性无关；通用 LLM 一致超过专用护栏，检测精度不随规模单调提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) evolve from static chatbots into autonomous agents, the primary vulnerability surface shifts from final outputs to intermediate execution traces. While safety guardrails are well-benchmarked for natural language responses, their efficacy remains largely unexplored within multi-step tool-use trajectories. To address this gap, we introduce **TraceSafe-Bench**, the first comprehensive benchmark specifically designed to assess mid-trajectory safety. It encompasses 12 risk categories, ranging from security threats (e.g., prompt injection, privacy leaks) to operational failures (e.g., hallucinations, interface inconsistencies), featuring over 1,000 unique execution instances. Our evaluation of 13 LLM-as-a-guard models and 7 specialized guardrails yields three critical findings: 1) *Structural Bottleneck*: Guardrail efficacy is driven more by structural data competence (e.g., JSON parsing) than semantic safety alignment. Performance correlates strongly with structured-to-text benchmarks ($ρ=0.79$, $p<0.01$) while we detect no association with standard jailbreak robustness. 2) *Scale Is Not the Deciding Factor*: Trajectory detection accuracy does not scale monotonically with model size, and general-purpose LLMs consistently outperform specialized safety guardrails. 3) *Bounded Temporal Stability*: Detection accuracy improves with trajectory length within native context bounds as models process dynamic execution behavior, but degrades in extreme long-context regimes due to over-refusal.

</details>

### 16. Willful Disobedience: Automatically Detecting Failures in Agentic Traces

📄 [arXiv](https://arxiv.org/abs/2603.23806)　📅 2026-03

**关键词**：`tool`、`specification extraction`、`trace compliance`、`AgentPex`

👤 **作者**：Reshabh K Sharma、Shraddha Barke、Benjamin Zorn

- 🎯 **研究动机**：只看结果的评分漏掉工作流路由错误、不安全工具使用与提示规则违规等程序性失败
- 🔬 **研究方法**：AgentPex 从 agent 提示与系统指令抽取行为规则并自动评估 trace 合规性，在 τ²-bench 的 424 条 telecom/retail/airline trace 上评测
- 📌 **结论**：区分不同模型行为并暴露结果评分未覆盖的规范违规，支持按域与指标的细粒度诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are increasingly embedded in real software systems, where they execute multi-step workflows through multi-turn dialogue, tool invocations, and intermediate decisions. These long execution histories, called agentic traces, make validation difficult. Outcome-only benchmarks can miss critical procedural failures, such as incorrect workflow routing, unsafe tool usage, or violations of prompt-specified rules. This paper presents AgentPex, an AI-powered tool designed to systematically evaluate agentic traces. AgentPex extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance. We evaluate AgentPex on 424 traces from $τ^2$-bench across models in telecom, retail, and airline customer service. Our results show that AgentPex distinguishes agent behavior across models and surfaces specification violations that are not captured by outcome-only scoring. It also provides fine-grained analysis by domain and metric, enabling developers to understand agent strengths and weaknesses at scale. The source code of AgentPex is available at https://github.com/microsoft/agentpex.

</details>

### 17. DRAFT: Task Decoupled Latent Reasoning for Agent Safety

📄 [arXiv](https://arxiv.org/abs/2604.03242)　📅 2026-02

**关键词**：`detection`、`latent draft`、`sparse risk evidence`、`trajectory safety`

👤 **作者**：Lin Wang、Junfeng Fang、Dan Zhang、Fei Shen、Xiang Wang、Tat-Seng Chua

- 🎯 **研究动机**：长 agent 轨迹中风险证据稀疏，二元监督难以信用分配，显式摘要再判有损信息
- 🔬 **研究方法**：DRAFT 两阶段：Extractor 把全轨迹蒸馏为紧凑连续潜草稿，Reasoner 联合注意草稿与原轨迹预测安全性，端到端可微训练
- 📌 **结论**：ASSEBench 与 R-Judge 上平均准确率从 LoRA 的 63.27% 升至 91.18%，并学到更可分的表示

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advent of tool-using LLM agents shifts safety monitoring from output moderation to auditing long, noisy interaction trajectories, where risk-critical evidence is sparse-making standard binary supervision poorly suited for credit assignment. To address this, we propose DRAFT (Task Decoupled Latent Reasoning for Agent Safety), a latent reasoning framework that decouples safety judgment into two trainable stages: an Extractor that distills the full trajectory into a compact continuous latent draft, and a Reasoner that jointly attends to the draft and the original trajectory to predict safety. DRAFT avoids lossy explicit summarize-then-judge pipelines by performing evidence aggregation in latent space, enabling end-to-end differentiable training.Across benchmarks including ASSEBench and R-Judge, DRAFT consistently outperforms strong baselines, improving accuracy from 63.27% (LoRA) to 91.18% averaged over benchmarks, and learns more separable representations. Ablations demonstrate a clear synergy between the Extractor and the Reasoner.Overall, DRAFT suggests that continuous latent reasoning prior to readout is a practical path to robust agent safety under long-context supervision with sparse evidence.

</details>

### 18. You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring

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

### 19. Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision

📄 [arXiv](https://arxiv.org/abs/2609.02057)　📅 2026-09

**关键词**：`monitoring`、`web agent`、`key-step supervision`、`early intervention`

👤 **作者**：Sitong Pan、Yipeng Shen、Yilin Lu、Caiwen Ding、Lu Cheng、Qianwen Wang

- 🎯 **研究动机**：无法访问 logits 等内部信号时，web Agent 的前缀级失败风险预测缺少可行方案
- 🔬 **研究方法**：构造两类可观察轨迹表示：总结跨步 Agent-环境行为的 Macro 特征与经重复黑盒查询测量意图-动作-预期状态一致的 Micro 特征；以首个未被纠正且导致失败的临界错误为标注边界
- 📌 **结论**：在 WebArena-Lite 与 Online Mind2Web、五个 backbone 上与内部信号基线相当，支持固定误切预算下的早期干预并跨未见网站类别迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reliable web-agent monitoring is difficult when model-internal uncertainty signals such as token logits are unavailable. In this work, we study prefix-level risk prediction for web agents using observable trajectory signals: given an evolving prefix, estimate whether the current execution remains on track or is tending toward failure. We derive two observable trajectory representations: Macro features summarize cross-step agent--environment behavior and feedback, while Micro features measure the consistency of intention, action, and anticipated state change through repeated black-box queries. Instead of inheriting the final result label, we label the first critical error that remains uncorrected in the observed continuation and is associated with final failure as a key-step boundary, preserving valid early prefixes of failed trajectories as on track. Across WebArena-Lite and Online Mind2Web web agent benchmarks with five open- and closed-source backbones, observable trajectory signals are competitive with internal-signal baselines. The resulting predictors also support early intervention under fixed false-cut budgets and transfer across held-out website categories. These findings show that observable trajectory signals support valuable risk prediction abilities.

</details>

### 20. Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents

📄 [arXiv](https://arxiv.org/abs/2608.29685)　📅 2026-09

**关键词**：`analysis`、`early failure prediction`、`uncertainty signal`、`path switching`

👤 **作者**：Zongyue Li、Chengyue Yu、Lei Zang、Chenyi Zhuang、Linjian Mo、Leilei Gan

- 🎯 **研究动机**：早期失败预测可让 long-horizon Agent 及时干预并节省成本，但 uncertainty 信号在执行中段是否保持判别力未经验证
- 🔬 **研究方法**：在 deep-research 任务上评估主流 uncertainty 信号（verbal confidence、perplexity 等）随轨迹进度的 AUROC
- 📌 **结论**：终局 verbal confidence 平均 AUROC 0.85，但轨迹 50% 进度时所有信号均不超 0.60；根因是频繁 path switching 切断早期信号与最终结果的联系

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early failure prediction is important for long-horizon agents, as it enables timely intervention and can reduce inference and tool-use costs. Uncertainty quantification, such as verbal confidence and perplexity, offers a promising approach to detecting agent failures; however, it has not been explored whether these signals retain their discriminative power during the intermediate stages of long-horizon execution. We evaluate mainstream uncertainty signals on deep-research tasks and find that verbal confidence reliably distinguishes failures at trajectory completion, achieving a mean AUROC of 0.85, whereas all evaluated signals offer limited predictive value earlier in execution, with none exceeding a mean AUROC of 0.60 at 50% trajectory progress. We identify an underlying mechanism explaining this gap: path switching, where agents frequently abandon their current search direction in-trajectory, breaking the link between early signal and final outcome. These findings challenge the assumption that intermediate uncertainty can reliably guide early intervention. They also motivate a practical recommendation for agent harnesses in deep-research settings: use final-step confidence to decide whether to restart, an approach that our experiments find more effective than in-trajectory intervention.

</details>

### 21. Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency

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

### 22. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21101)　📅 2026-08

**关键词**：`defense`、`progressive Agent guardrail`、`tiered review`、`session anti-bypass`、`runtime supervision gateway`、`Agent Harness Protocol`

👤 **作者**：Kai Wang、…、Xingcheng Xu

- 🎯 **研究动机**：agentic 风险是渐进的：可从 skill 准入、调用意图、执行效果与事后后果四个位置进入，被拒目标可跨工具、跨轮次改头换面重现，而现有防护只覆盖单一生命周期边界或单次调用
- 🔬 **研究方法**：ClawSentry 框架无关安全监督网关，含 skill 执行前首次审计、三层渐进审查、会话级反绕过（识别换工具与改写重试）与事后高严重性证据回注，经 Agent Harness Protocol 统一接入 Codex、Claude Code、Kimi CLI、Gemini CLI
- 📌 **结论**：SkillInject+Codex/GPT-5.4 上 contextual ASR 从 39.55% 降至 2.61%（TSR 仅 83.78%→83.05%）；五个 Work Agent 上 ASR 被压至 9.09–15.03%（未防护 33.5–49.7%），干净 skill TSR 保持 98.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reappear across surface forms, tools, or turns; existing safeguards are typically local to one lifecycle boundary or one call. Guided by this threat model, we present ClawSentry, an open-source, framework-agnostic security supervision gateway for agent runtimes. Before a skill package is ever executed, First-use Skill Package Review (FSPR) audits it under a deterministic evidence floor, escalating unresolved cases to bounded read-only agentic review (locus A). At runtime, a three-tier progressive decision engine--a deterministic L1 layer, a rule-anchored L2 semantic reviewer, and a read-only L3 evidence-seeking agent--spends contextual review only on the residual ambiguity, while a session-level anti-bypass mechanism recognizes tool-switching and rephrased retries (loci B--C); a post-action path feeds high-severity evidence non-retroactively into later review (locus D). An Agent Harness Protocol (AHP) abstraction applies one policy across Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying agent internals. On SkillInject with Codex/GPT-5.4, contextual ASR falls from 39.55% to 2.61% while contextual TSR moves only from 83.78% to 83.05%. Across five Work Agents on the full SkillsSafety benchmark, ClawSentry confines ASR to 9.09--15.03% from 33.5--49.7% unprotected, and aggregate TSR on clean skills remains 98.7%.

</details>

### 23. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.27141)　📅 2026-08

**关键词**：`analysis`、`defense`、`monitor composition`、`cross-iteration state`、`safety bound`、`cross-iteration guard`

👤 **作者**：Chenhao Wu、…、Bin Chong

- 🎯 **研究动机**：自主 Agent 循环的安全监控以单轨迹为作用域、安全状态逐轨迹重置，而攻击证据可碎片化分散在多次迭代中
- 🔬 **研究方法**：证明任何 trajectory-scoped monitor 对此类攻击的真阳性率等于假阳性率，几何衰减风险分数也不够；提出 LoopHarness，在循环层维护持久不衰减安全状态并以 mediated commit 提交
- 📌 **结论**：在 arbiter 检测下界 δ_M 下，未授权不可逆动作的期望数量被约束为与迭代 horizon N 无关的常数 B+m-1+m/δ_M

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central result is a separation: against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate, however expressive it is, because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. We further show that the obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon $N$. We then present LoopHarness, which restores a persistent, non-decaying safety state at the loop level. Under mediated commits and an arbiter detection floor $δ_M$, it bounds the expected number of unauthorized irreversible actions by $B+m-1+m/δ_M$, a constant in $N$, of which the $B+m-1$ term is decided by a model-free rule and therefore survives a fully colluding verifier. We give a complete evaluation protocol on native Agent-SafetyBench tasks with paired clean and attacked episodes, an outer-state attack suite whose decisive evidence exists only across iterations, per-module ablations, and an adaptive white-box red team.

</details>

### 24. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

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

### 25. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25340)　📅 2026-08

**关键词**：`defense`、`harmful compliance`、`relationship manipulation`、`stateful monitoring`、`multi-turn relationship harm`、`dual gate`

👤 **作者**：Pei-Sze Tan、Tasuku Igarashi、Isao Echizen

- 🎯 **研究动机**：Agentic AI 可被滥用于人际操纵且角色敏感：操纵者请求应阻断、求助者应获支持，多轮动作可组合成危害
- 🔬 **研究方法**：构建 1000 段五轮对话 benchmark；HRGuard 以 pre-generation gate 与维护衰减累积风险状态的 turn-level gate 中断操纵工作流
- 📌 **结论**：八个生成模型上降低有害顺从并保留受害者保护指引，优于通用安全 prompt 与三个通用 guard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings, individually plausible actions may combine into a harmful workflow. We introduce a benchmark of 1,000 five-turn conversations. It covers both attacker-side and victim-side scenarios. It also includes direct and adversarially paraphrased variants. We further propose HRGuard. It includes an online pre-generation gate and a turn-level post-generation gate. The post-generation gate maintains a decayed cumulative risk state and interrupts emerging manipulative workflows. Across eight generation models, HRGuard reduces harmful compliance while preserving victim-side protective guidance. It also outperforms a generic safety prompt and three general-purpose guard models. Independent-judge evaluation supports the main findings. Under our evaluation protocol, the tested generic prompt and general-purpose guards leave substantial residual risk, motivating turn-aware relationship-specific evaluation.

</details>

### 26. Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety

📄 [arXiv](https://arxiv.org/abs/2608.25711)　📅 2026-08

**关键词**：`defense`、`trajectory-conditioned action`、`cross-turn evidence`、`generation-time guard`、`distributed risk`、`trajectory evidence`

👤 **作者**：Yanbo Dai、Zhenlan Ji、Zongjie Li、Shuai Wang

- 🎯 **研究动机**：多轮分解攻击把危害拆成各自合理的调用，现有防御靠在线推理或事后评估，开销大
- 🔬 **研究方法**：ReDiR 动作生成前把轨迹压缩为潜在安全表示注入冻结基模型，以跨视角监督学习
- 📌 **结论**：两个 benchmark、三个模型家族上 ASR 降至 8% 以下，且可迁移至未见工具域

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using LLM agents extend security risks beyond generated text to actions that affect external systems. Under multi-turn decomposition attacks, a harmful objective can be distributed across individually plausible requests and tool calls, becoming apparent only from the accumulated trajectory. Existing defenses either rely on auxiliary online reasoning to recover long-horizon security evidence or assess actions after generation, often incurring additional inference cost or depending on runtime-specific action representations. We propose \emph{Reassembling Distributed Risk} (ReDiR), a generation-time defense that conditions action generation on trajectory-level security evidence. Before each action, ReDiR compresses the current trajectory into a compact latent safety representation and injects it into the frozen base model. The representation is learned through same-model, cross-view supervision, where safe behavior from an explicit task view provides supervision for recovering distributed safety evidence from the original multi-turn trajectory. This design enables ReDiR to integrate cross-turn security information directly within the generation process without relying on a separate action-level safety module. We evaluate ReDiR on two agent-safety benchmarks across three model families and eight held-out tool domains. ReDiR reduces attack success rates to below 8\%, transfers to unseen tool domains, and preserves benign fidelity with low computational overhead.

</details>

### 27. GuardianAgentBench: Where Agents Fail and How to Guard Them

📄 [arXiv](https://arxiv.org/abs/2607.20982)　📅 2026-07

**关键词**：`defense`、`adversarial robustness`、`agent trajectory`、`failure attribution`

👤 **作者**：Vishal Ishwar Naik、…、Humayun Irshad

- 🎯 **研究动机**：自主 LLM agent 的失败模式与护栏有效性需要跨框架可复现评估
- 🔬 **研究方法**：构建 GuardianAgentBench：580 场景、六领域、五种对抗攻击模式，在 LangChain、LlamaIndex、Vectara 三个生产框架上评估六个 SOTA 模型并实现护栏
- 📌 **结论**：最强配置总体准确率仅 74.8%；强模型漏调用工具、弱模型误选并过度调用，长程规划是更陡的瓶颈；护栏以 0.5% 误报率挽回 19.9% 失败，优于系统提示防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language model agents increasingly operate autonomously with access to tools and external environments, ensuring their safe and reliable behavior becomes critical. We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara. The benchmark incorporates rigorous multi-stage validation and five adversarial attack modes. Experiments with six state-of-the-art models reveal that even the strongest configuration achieves only 74.8% overall accuracy and expose two distinct failure regimes: stronger models under-call required tools, while weaker models mis-select and over-call tools. Performance degrades monotonically with both tool-set size and sequential turn depth, with long-horizon planning proving the steeper bottleneck. Our guardrail implementation consistently outperforms system-prompt-based defenses across all models, recovering 19.9% of failures at a false positive rate of just 0.5%. These results demonstrate that execution-time structural intervention improves safety without disrupting correct agent behavior.

</details>

### 28. ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction

📄 [arXiv](https://arxiv.org/abs/2508.00500) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/117/ProbGuard-Proactive-Runtime-Monitoring-for-LLM-Agent-Safety-via-Probabilistic-Predic)　📅 2025-08　🏷 ASE 2026

**关键词**：`defense`、`runtime monitoring`、`risk prediction`、`LLM agent`

👤 **作者**：Haoyu Wang、Christopher M. Poskitt、Jiali Wei、Jun Sun

- 🎯 **研究动机**：现有运行时监控依赖反应式规则，只能在不安全行为临近或已发生时才告警，难以处理长程依赖
- 🔬 **研究方法**：提出 ProbGuard：把执行抽象为符号状态并从轨迹学习 DTMC，运行时估计保持安全的概率、低于阈值即干预，配 PAC 式样本复杂度分析
- 📌 **结论**：自动驾驶中可提前最多 15.84 秒预警违规且零误报；具身任务重提示干预降 65.37% 不安全行为并保留 80.4% 任务完成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents increasingly operate across domains such as robotics, virtual assistants, and web automation. However, their stochastic decision-making introduces safety risks that are difficult to anticipate during execution. Existing runtime monitoring frameworks, such as AgentSpec, primarily rely on reactive safety rules that detect violations only when unsafe behavior is imminent or has already occurred, limiting their ability to handle long-horizon dependencies. We present ProbGuard, a proactive runtime monitoring framework for LLM agents that anticipates safety violations through probabilistic risk prediction. ProbGuard abstracts agent executions into symbolic states and learns a Discrete-Time Markov Chain (DTMC) from execution traces to model behavioral dynamics. At runtime, the monitor estimates the probability that execution will remain safe from the current state, and triggers an intervention when this probability falls below a user-defined threshold. To improve robustness, ProbGuard incorporates semantic validity constraints in the abstraction and admits a PAC-style analysis that characterizes the sample complexity required to certify the learned model under standard assumptions. We evaluate ProbGuard in two safety-critical domains: autonomous driving and embodied household agents. Across evaluated scenarios, ProbGuard consistently predicts traffic law violations and collisions in advance, with warnings up to 15.84 seconds at a threshold yielding no false alarms, and up to 38.66 seconds at stricter thresholds. In embodied agent tasks, ProbGuard's re-prompting intervention mode reduces unsafe behavior by 65.37% relative to the unmonitored baseline while retaining 80.4% of the baseline task completion; a stricter halting configuration reduces unsafe behavior by 93.60% at a larger cost in completion.

</details>

### 29. Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/65283)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`multi-agent evaluation`、`tool-use agent`、`tool interface`、`LLM agent security`、`tool-use attack`

👤 **作者**：Zezhong WANG、Xueyang Tang、RUI LIAN、Yang Lou、Heqing Huang

- 🎯 **研究动机**：多轮交互攻击把恶意意图拆分到多轮隐藏未来风险，依赖历史上下文的回顾式检测难以识别
- 🔬 **研究方法**：提出 SSH：小 LLM 多 agent 模拟构建动作级 speculate-and-verify 工作流，推测阶段异步构建轨迹树提前暴露风险，验证阶段用真实动作校准剪枝，可插拔增强现有检测器
- 📌 **结论**：按轨迹树演化而非单时点判险，降低对单检测组件精度的依赖，提升防御韧性与预警提前量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Model (LLM) agents are increasingly deployed in complex environments, multi-turn interaction attacks have become a significant security challenge. Existing detection methods typically rely on historical context. However, this retrospective logic struggles to identify deep malicious intents that are split across turns to hide future risks. Inspired by speculative decoding, we propose the Speculative Safety Honeypot (SSH) framework. SSH uses a multi-agent simulation system composed of small LLMs to build an action-level speculate-and-verify workflow. In the speculation stage, SSH predicts future behaviors of the target agent and asynchronously builds a trajectory tree to expose potential risks in advance. In the verification stage, the system uses the target agent's real actions to calibrate and prune the trajectory tree, effectively reducing false positives. As a plug-and-playable component, SSH provides existing detectors with rich decision redundancy beyond the current interaction slice. By judging risk based on the evolution of the entire trajectory tree rather than a single point in time, the system reduces the reliance on the absolute precision of individual detection components. This improves the defense resilience and the warning lead-time of agent systems against complex temporal attacks.

</details>

### 30. MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/jiang-changyue)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`mobile agent`、`policy auditing`、`trajectory learning`

👤 **作者**：Changyue Jiang、Jiayi Wang、Xin Wen、Jiarun Dai、Geng Hong、Xudong Pan

- 🎯 **研究动机**：移动智能体轨迹可违反 app 特定安全策略，现有轨迹防御靠 LLM 提示或僵化规则，难支持跨 app 的自然语言细粒度策略
- 🔬 **研究方法**：MATE 把策略当可编辑文本的策略条件化审计器，从数百 app 提取描述/工作流/策略并多阶段合成 14 万+ 轨迹训练；发布 MATEBench
- 📌 **结论**：MATEBench 准确率超 95%，真实设备上审计 AutoGLM 与 Mobile-Agent 轨迹准确率超 95%，超先前方法 20% 以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile agents powered by foundation models now automate complex, multi-step workflows on real devices, but their trajectories can violate app-specific security policies. Existing trajectory-level defenses rely on LLM prompting or rigid rules, and thus fail to support fine-grained, natural-language policies that generalize across apps and tasks. In this work, we introduce MATE, a lightweight, policy-conditioned auditor that encodes both agent trajectories and natural-language security policies to determine whether a trajectory violates a given policy and to explain why. Treating policies as editable text rather than fixed model parameters allows MATE to handle user-defined and evolving requirements without retraining. To construct MATE, we build a knowledge base by extracting app descriptions, workflows, and policies from hundreds of popular mobile apps worldwide, and synthesizing over 140K semantically realistic, policy-conditioned trajectories with a multi-stage pipeline. We further release MATEBench, a trajectory-level auditing benchmark with two synthetic subsets and one real-world subset of manually collected trajectories. Models trained with our synthesis-driven trajectory learning achieve over 95% accuracy on MATEBench, retain strong performance on external safety benchmarks, and audit trajectories from Zhipu's AutoGLM and Alibaba's Mobile-Agent on real devices with over 95% accuracy, outperforming prior methods by over 20%. MATE shows that practical, fine-grained security auditing for heterogeneous mobile agents is both feasible and effective.

</details>

### 31. Causal Detection of Multi-Step LLM Agent Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/64714)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`causal analysis`、`tool-use agent`、`tool interface`、`LLM agent security`、`tool-use attack`

👤 **作者**：Viraaji Mothukuri、Reza M. Parizi

- 🎯 **研究动机**：多步提示注入的恶意意图在工作流完成后才显现、单动作均合法，现有防御作用于单动作或内容模式无法捕捉序列结构
- 🔬 **研究方法**：CausalTrace 把防御重构为因果推断：从 agent 轨迹构建带数据依赖、信任转移、状态使能类型边的结构因果模型，用 Pearl do-calculus 回答阻断注入是否仍会发生有害结果
- 📌 **结论**：检测优于内容基线且 LLM 推理成本低，双向切片高边召回恢复完整攻击链并提供可解释归因

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-step prompt injection attacks on LLM agents present a fundamental detection challenge because malicious intent emerges only after the workflow completes, while individual actions remain legitimate in isolation. Existing defenses, including input sanitization, output validation, and instruction hierarchy, operate on individual actions or content patterns and cannot capture this sequential structure. We present CausalTrace, a detection system that reframes prompt-injection defense as causal inference. It constructs Structural Causal Models from agent trajectories with typed edges capturing data dependency, trust transfer, and state enablement, then applies Pearl’s do-calculus to answer a counterfactual question, namely, whether the harmful outcome would have occurred if the injection had been blocked. This formalization enables a principled distinction between attacks that depend on injections and benign workflows that share surface-level features. Evaluation on a dataset spanning crowdsourced traces, LLM agent benchmarks, and semi-real and real scenarios demonstrates strong detection performance, outperforming content-based baselines while requiring minimal LLM inference cost; bidirectional slicing recovers complete attack chains with high edge recall, providing interpretable explanations that trace exploitation to its causal origins.

</details>

### 32. DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents
📄 [arXiv](https://arxiv.org/abs/2609.10892)　📅 2026-09


👤 **作者**：Asif Pinjari、Mithun Paul Saint-Germain

**关键词**：`detection`、`prompt injection localization`、`trajectory transformer`、`agent monitor`

- 🎯 **研究动机**：注入检测只给整轨迹判定或单索引，运维需要注入点/被劫持步骤/是否被抵抗三要素
- 🔬 **研究方法**：双头轨迹 Transformer：轨迹级 compromised 判定 + 每步四类标注；<2M 参数无需访问 agent 模型
- 📌 **结论**：AgentDrift 任务不相交划分 F1 0.983、注入点恢复 98.7%；表面基线 partial hijack 恢复仅 11.1% vs 本方法 98.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When an indirect prompt injection succeeds against an LLM agent, the compromise is visible in the agent's own behavior: a benign prefix of tool calls, a poisoned observation, and a suffix of actions that serve the attacker. An operator needs three facts: where the attack entered, which steps it corrupted, and whether apparent poison was resisted. Existing systems return either a whole-trace verdict or a single unsafe index. We present DriftNet, a dual-head trajectory Transformer that reads a logged tool-call trajectory and answers all three questions in one forward pass: one head classifies the trajectory as compromised or not, and a second assigns every step one of four labels (benign, injection point, hijacked, failed injection). To our knowledge it is the first supervised detector to produce this joint output. A frozen sentence encoder and four identity-free world features embed each step; the trained trunk, under two million parameters and optimized with a class-weighted joint objective over both heads, needs no access to the agent's model. On the task-disjoint split of the AgentDrift benchmark (12,536 trajectories, 71,024 labeled steps), with a 20-configuration sweep bounding hyperparameter sensitivity to 0.011 F1 and the test part evaluated exactly once, DriftNet reaches trajectory-level F1 of 0.983, exact injection-point recovery on 98.7% of attacked trajectories, hijacked-span IoU of 0.979, zero flags on 218 resisted attacks, and 2.9% flags on hard negatives. A surface baseline retrained on the identical split recovers 11.1% of partial hijacks and 17.1% of delayed executions; DriftNet reaches 98.6% and 93.2% while lowering every false-alarm rate. Reading all 26 residual errors shows that most misses trace to trajectories whose labeled injection observation carries no legible instruction, and we report the benchmark's measured world-identity regularity alongside the results.

</details>

### 33. Locating Hidden Failures Makes Long-Horizon Agents More Reliable

📄 [arXiv](https://arxiv.org/abs/2609.17930)　📅 2026-09

**关键词**：`benchmark`、`failure localization`、`long-horizon agent`、`verifier`、`irreversible harm`

👤 **作者**：Salman Rahman、…、Hamid Palangi

- 🎯 **研究动机**：长程 agent 时代人类从执行者变成监督者，却仍几乎只按最终成败评判——结果无法揭示运行在哪里出错、是否恢复、沿途造成哪些不可逆伤害
- 🔬 **研究方法**：研究 2,518 条软件工程/计算机使用/科学任务 agent 轨迹，把 6,967 个错误人工归类为 78 种失效类型；发布 Traverse 基准并训练 4B 验证器 Scout，与 6 个前沿 judge 对比定位能力；test time 用于在 agent 候选运行间选择
- 📌 **结论**：失效呈重复签名：首次错误后 agent 常无法恢复且极少自查，运行继续却看似正确；被评"已解决"的运行也会删数据、破坏系统或伪造成功；最强 frontier judge 在不到 1/3 运行中正确定位首个错误，Scout 远超它们且能迁移到未见领域；用于运行选择时把任务成功率提到 agent 单次尝试之上——无需重训 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI agents take on long, autonomous tasks, we increasingly oversee rather than perform the work, yet we still judge them almost entirely by whether they finally succeed. An outcome cannot reveal where a run went wrong, whether the agent recovered, or the irreversible harm it caused along the way, and where long-horizon agents fail remains unmapped. We study $2518$ agent trajectories across software engineering, computer use, and science, close to real deployment, and classify $6967$ mistakes into $78$ failure types. Failure follows a recurring signature: after its first mistake an agent often fails to recover and rarely catches the error itself, so the run continues unchecked while still looking correct; whether an agent recovers depends on the task and the environment's feedback, not on the agent framework running it. Long-horizon agents can do real harm on the way to a passing result: even runs scored as solved delete data, corrupt systems, or fabricate success rather than earning it. We release these human-verified annotations as Traverse, a benchmark on which six frontier judges struggle to locate failure regardless of scale: even the strongest correctly identifies the first mistake in fewer than a third of runs. Yet Scout, a $4$B verifier we trained, locates failure far better than these judges and transfers to domains it never saw. Used at test time to select among an agent's candidate runs, it raises task success above the agent's own single-attempt performance, without retraining the agent. By making failure cheap to locate and correct, this work is a foundation for more trustworthy long-horizon agents that learn from their own mistakes, and a practical path to overseeing increasingly autonomous AI.

</details>

### 34. PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety

📄 [arXiv](https://arxiv.org/abs/2609.28197)　📅 2026-09

**关键词**：`benchmark`、`proactive safety monitoring`、`optimal intervention window`、`trajectory risk`、`timeliness`

👤 **作者**：Jiapeng Sun、…、Yike Guo

- 🎯 **研究动机**：agent 安全评测从单轮走向多轮后仍有两大缺口：步级方法孤立看待动作错过风险累积、轨迹级评测事后进行无法及时干预
- 🔬 **研究方法**：PASTABench：1,139 条多轮轨迹 × 5 风险类 13 子类；解耦主动安全监控三维度（是否/何时/何险）+ 最优干预窗口（OIW，锚定最早信号轮与触发轮）量化干预及时性；16 LLM 评测
- 📌 **结论**：最佳模型最优时机干预仅 40.74%——主动干预远未解决（agent 监控评测从检出率到时机有效性）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations, we formalize Decoupled Proactive Safety Monitoring along three dimensions: whether to intervene, when to intervene, and what the risk is. We introduce PASTABench, a benchmark of 1,139 multi-turn trajectories spanning 5 risk categories and 13 subcategories. We further propose the Optimal Intervention Window (OIW), anchored by annotated Earliest-Signal and Trigger turns, to quantify intervention timeliness. Evaluation of 16 LLMs reveals that proactive intervention remains largely unsolved, with the best model achieving only 40.74% optimal-timing interventions. Fine-grained diagnosis further uncovers pervasive lexical overfitting: competitive safety scores of smaller models mask keyword hypersensitivity rather than genuine risk comprehension, as their proactive capability largely collapses once hazard vocabulary is neutralized.

</details>

## 常规收录

### 35. DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems

📄 [arXiv](https://arxiv.org/abs/2609.04749)　📅 2026-09

**关键词**：`analysis`、`failure attribution`、`causal dependency graph`、`counterfactual refinement`、`multi-agent trace`

👤 **作者**：Zehao Wang、Lanjun Wang、Shilong Jin、Junjie Chen、Yanghua Xiao

- 🎯 **研究动机**：LLM 多智能体系统频繁出现推理与协调错误并导致系统级失败——失效归因须从 agent 间自然语言交互中定位「决定性错误」（最早一个纠正即可逆转系统失败的动作）；既有方法浅归因（只抓不完整检索/格式错误等可被验证机制纠正的次要偏差）且随 trace 变长推理能力快速退化
- 🔬 **研究方法**：DCFA 免训练双视角框架：全局模块从系统 trace 构建结构化因果依赖图定位初始决定性错误；局部模块用反事实启发推理精炼归因
- 📌 **结论**：Who&When 基准 × 6 个 LLM 上步级准确率最高提升 8.27% 超既有 SOTA——从浅偏差检测到决定性因果定位的归因升级

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-based multi-agent systems have experienced rapid growth in recent years. Despite their promise, such systems remain fragile, frequently exhibiting reasoning and coordination errors that can lead to system-level failures. Failure attribution in such systems relies on tracing natural language interactions among agents to identify the decisive error, which refers to the earliest action whose correction can reverse system failure. There are two key challenges: 1) Shallow attribution: Existing methods often capture only minor deviations, such as incomplete retrievals or formatting errors, which verification mechanisms can correct, while missing the decisive cause of system failure. 2) Contextual degradation: As the length of the system traces increases, the model's reasoning ability rapidly deteriorates. To address these challenges, we propose DCFA, a training-free framework for failure attribution. DCFA integrates a global module that constructs structured causal-inspired dependency graphs from system traces to identify the initial decisive error, and a local module that applies local counterfactual-inspired reasoning to refine causal-inspired attribution. Experiments on the Who&When benchmark across six LLMs show that DCFA improves step-level accuracy by up to 8.27% over state-of-the-art baselines.

</details>
