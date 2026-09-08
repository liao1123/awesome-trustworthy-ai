# Agent Guardrail 与 Policy Compliance

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究部署在 Agent 外部或 trajectory 中的独立安全控制层。判断对象从单轮 prompt/response 扩展到 observation、plan、tool call、state transition、workflow 与完整 trajectory，重点处理 prompt injection、危险动作、敏感信息泄露、组织 policy 违规、动作前介入，以及 guardrail 自身的资源消耗和规避风险。

## 研究脉络

- **Action-local 审核：** 早期方案在工具调用前后判断单个 action 是否有害，但难以识别遗漏确认、顺序错误等跨步骤程序违规。
- **Trajectory-level guard：** Pre-Exec Bench、AgentDoG 和 PolicyGuardBench 将计划前缀或完整轨迹作为判断对象，使 guard 能在动作执行前检测、分类和解释风险。
- **专门攻击面：** WebAgentGuard 把网页 prompt injection detection 与执行 Agent 解耦，NSFA taxonomy 进一步覆盖数据泄露、恶意代码、tool misuse 与 resource exhaustion。
- **Policy workflow：** Policy internalization 降低长规则文档的上下文开销；跨步骤 workflow guard 的主条目见 [Policy-Adaptive Guardrail](../guardrails/policy-adaptive-guardrails.md)。
- **Guardrail 自身安全：** reasoning 和 schema-following 也会成为资源放大面；针对 guardrail 的可用性攻击主条目见 [Agent 与多 Agent DoS](../dos/agent-system-dos.md)。

## Workflow、Action 与 Prompt Injection 防护

### 1. Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents

📄 [arXiv](https://arxiv.org/abs/2609.03438)　📅 2026-09

**关键词**：`defense`、`multimodal action guard`、`conflict detection`、`safe abstention`、`GUI agent`、`conflict-aware termination`

👤 **作者**：Zhaoyuan Huang、…、Zhuosheng Zhang

- 🎯 **研究动机**：真实用户会发出不可行的错误指令，而 GUI Agent 在指令内部或指令-界面证据冲突时仍盲目执行，呈现 execution-biased overcompliance
- 🔬 **研究方法**：构建覆盖指令内部与指令-GUI 上下文冲突的 CONFLICTGUI 基准，并提出推理时框架 CONFLICTGUARD：行动前可行性验证协议加条件动作调制，把过度顺从的执行导向终止行为
- 📌 **结论**：五个常用 Agent 上平均冲突任务成功率显著提升且正常 GUI 任务性能保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent's feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent's competence to identify inappropriate execution scenarios and refrain from unnecessary actions.

</details>

### 2. KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents

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

### 3. PACE: Towards Surfacing Hidden Conflicts in User Requests

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

### 4. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

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

### 5. ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection

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

### 6. PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents

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

### 7. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

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

### 8. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

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

### 9. The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions

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

### 10. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

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

### 11. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

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

### 12. When Context Gets Root: Privilege Escalation in LLM Harnesses

📄 [arXiv](https://arxiv.org/abs/2608.27299)　📅 2026-08

**关键词**：`attack`、`coding-agent harness`、`instruction privilege escalation`、`permission bypass`、`permission-review bypass`、`provenance laundering`

👤 **作者**：Xingbang He、…、Bing Mao

- 🎯 **研究动机**：instruction hierarchy 是模型侧防御，但 Agent harness 组装每次调用上下文时会把低权限内容提升到更高指令层级并获得模型侧特权
- 🔬 **研究方法**：定义 instruction privilege escalation 攻击，利用多 Agent 机制在六种 coding-agent harness 上实现覆盖保密性、完整性、可用性与 RCE 的 13 个攻击目标
- 📌 **结论**：无限制执行时六种 harness 全部达成 13 个目标，提供自动权限审查的三种 harness 也全部达成，持久目标与定时任务下同样复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an agent to elevate low-level malicious content to a higher instruction level. The elevated content then causes the agent to execute instructions it would not follow at their original level. We evaluate this threat by using multi-agent mechanisms to achieve 13 attack objectives across six coding-agent harnesses. These objectives span confidentiality, integrity, availability, and remote code execution. With unrestricted action execution, the attacks achieve all 13 objectives on all six harnesses. Under automatic permission review, the attacks achieve all 13 objectives on all three harnesses that provide this mode. We further reproduce the vulnerability using harness-provided persistent goals and scheduled tasks. These results demonstrate the generality of instruction privilege escalation.

</details>

### 13. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

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

### 14. Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety

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

### 15. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.25817)　📅 2026-08

**关键词**：`defense`、`coding agent`、`prompt-space policy`、`malware prevention`、`system-prompt safeguard`、`persistent policy`

👤 **作者**：Xiaodong Wu、…、Jianbing Ni

- 🎯 **研究动机**：coding Agent 以开发者权限执行命令，weight 级对齐对 API 部署方不可用，输入过滤与执行监控又需辅助组件
- 🔬 **研究方法**：SkillShield 离线从已知攻击合成 security skill 注入 system prompt 并在整个工具循环生效，考察三种固定预算配置
- 📌 **结论**：RedCode 上 all-classes skill 把恶意软件生成严重度从 3.37 降至 0.58，执行 ASR 43.6% 媲美 Llama Guard 3 且无需 8B 分类器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A coding agent edits files and executes shell commands with its developer's privileges, allowing malicious requests to translate directly into harmful actions or functional malware. Existing defenses have complementary limitations: weight-level alignment is unavailable to API-only deployers, whereas input filters and execution-boundary monitors require auxiliary classification or checking components along the agent's trajectory. We therefore introduce SkillShield, a system-prompt defense that synthesizes security skills offline from known attacks or recorded agent failures. These skills are injected into the system prompt at session start and remain active throughout the tool-use loop. Unlike a reference monitor, they protect the system by defining the security policies the model should follow during execution. Due to the limited system-prompt space, we examine three fixed-budget provisioning scopes: all-classes, with one skill covering all threat classes, per-bundle, with one skill targeting a related subset, and per-class, with one skill dedicated to a single known class and used as the upper-bound reference. None requires runtime request classification or routing. Across six large language models on RedCode, the default all-classes skill reduces malware-generation severity from 3.37 to 0.58 and achieves a 43.6% execution attack success rate, comparable to Llama Guard 3's 42.7% without its separate 8B classifier. The per-bundle and class-fixed per-class settings further reduce this rate to 36.2% and 14.5%, respectively. Under two non-adaptive jailbreak families, SkillShield continues to outperform all baselines on malware generation. Across 731 benign task descriptions, SkillShield yields a mean safety-refusal rate of 0.14%. These results demonstrate the potential of prompt-space security skills to prevent harmful actions and malware generation for LLM coding agents.

</details>

### 16. Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation

📄 [arXiv](https://arxiv.org/abs/2608.23224)　📅 2026-08

**关键词**：`defense`、`analysis`、`prompt authority`、`candidate-admission split`、`task signature`、`prompt-form collapse`

👤 **作者**：Zhiruo Zhou、…、Xiaojun Zhu

- 🎯 **研究动机**：检索增强冻结 VLA 时检索文本一进入执行的 prompt 即成为控制干预：匹配审计显示直接附加文本使成功率从 92.47% 跌至 3.00%，揭示 prompt-form collapse——指令形式改变本身即可主导执行
- 🔬 **研究方法**：TOWN-VLA prompt-authority 接口把候选生成与更改策略输入的权限分离，固定兼容规则仅授权规范紧凑指令，否则精确恢复原 Base prompt
- 📌 **结论**：900 条审计路由全部遵守契约（525 条哈希级恢复 Base、375 条授权 prompt 保持任务签名）；LIBERO-Plus 4×7 评估成功率 69.5%→73.1%，实机 PiPER 臂 52.7%→78.7%（p=3.16e-6）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval can efficiently and effectively augment a frozen vision--language--action (VLA) policy without retraining, yet retrieved text becomes a control intervention once it enters the executed prompt. In a matched audit, raw appended text reduces mean success from 92.47\% to 3.00\%, while meaningful and length-matched meaningless appends both fail on all 500 states. This result identifies \emph{prompt-form collapse}: changing the instruction form, rather than adding useful semantics, can dominate execution. We introduce TOWN-VLA (Think Only When Needed), a prompt-authority interface that separates candidate generation from permission to alter the policy input. A fixed compatibility rule authorizes a canonical compact instruction; otherwise, the interface restores the original Base prompt exactly. Across 900 audited routes, every route follows this contract: 525 routes recover Base with matching hashes, and all 375 authorized prompts preserve the task signature. On a matched $4\times7$ LIBERO-Plus evaluation with 10{,}030 episodes per method, success rises from 69.5\% to 73.1\% ($+362$ episodes; 95\% CI 1.89--5.45 points), improving on six perturbation axes and all four suites. On a physical PiPER arm with a frozen \pizerofive{} checkpoint, success rises from 52.7\% to 78.7\% over 150 trials per method ($p=3.16\times10^{-6}$). Prompt authority is enforceable for a frozen controller; oracle-free admission calibration is the next deployment target.

</details>

### 17. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

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

### 18. StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing

📄 [arXiv](https://arxiv.org/abs/2608.24777)　📅 2026-08

**关键词**：`defense`、`pre-execution guard`、`step-level tool action`、`safety-utility balance`、`step-level guard model`、`Balance-GRPO`

👤 **作者**：Zhijie Zheng、…、Dongrui Liu

- 🎯 **研究动机**：现有 guardrail 多在轨迹完成后评估，step 级工具动作的执行前监控不足
- 🔬 **研究方法**：StepGuard 执行前检查工具动作；StepGen 生成同上下文异动作的安全/不安全样本，Balance-GRPO 动态平衡两类防御
- 📌 **结论**：AgentDojo 与 AgentDyn 上平均 ASR 相对降 77.3%，utility 仅降 2.8 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate completed trajectories, leaving pre-execution monitoring of step-level actions underexplored. We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed. To train StepGuard, we introduce StepGen, an automatic data engine that generates safe and unsafe trajectories with the same context but different actions at the risky step. To further reduce over-defense and under-defense, we propose Balance-GRPO, which dynamically balances learning between safe and unsafe actions based on their observed accuracy. Experiments show that StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. When used to guard agents on AgentDojo and AgentDyn, StepGuard reduces mean attack success rate by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 percentage points.

</details>

### 19. What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions

📄 [arXiv](https://arxiv.org/abs/2608.24022)　📅 2026-08

**关键词**：`detection`、`behavior-guiding instruction`、`attention localization`、`authority adjudication`

👤 **作者**：Yichao Gao、…、Zhiqiang Wang

- 🎯 **研究动机**：静态输入输出过滤无法捕捉推理时才被解析为行为引导指令的外部内容
- 🔬 **研究方法**：Attnlocate 聚合多层多头 attention 构建 token 级特征，以一维 U-Net 定位 behavior-guiding span，再按来源方权限裁决调用
- 📌 **结论**：五个 LLM 家族十个 Agent 配置上平均 IoU 0.743、AUROC 0.956，覆盖间接 prompt injection 与 tool poisoning

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during model reasoning. We propose Attnlocate, a runtime framework for fine-grained localization of context spans that genuinely influence tool-calling decisions, i.e., behavior-guiding instructions. Attnlocate casts this localization problem as an object detection task, aiming to detect the distinctive activation traces induced by behavior-guiding instructions within the attention matrix. Specifically, we design a multi-head, multi-layer attention aggregation scheme to construct a token-level feature space tailored for object detection. Then, a 1-D U-Net equipped with an anchor-free detection head is deployed to detect these spans. Finally, based on the authority of the provider from which the detected behavior-guiding spans originate, Attnlocate dynamically adjudicates malicious invocation attempts. We evaluate Attnlocate across ten agent configurations from five LLM families, covering scenarios involving indirect prompt injection and tool poisoning. Attnlocate achieves a mean IoU of 0.743, an average AUROC of 0.956, and a 0.934 true-positive rate at 0.067 false-positive rate. It also transfers effectively across unseen models and supports authority policy adaptation without retraining.

</details>

### 20. Policy-Guided RAG: A Governance Framework for Controlled Information Use in Large Language Models

🌐 [Project](https://doi.org/10.1145/3805712.3808490)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`defense`、`RAG governance`、`policy enforcement`、`auditable generation`、`framework`

- 🎯 **研究动机**：LLM对检索信息的使用缺策略级治理，生成过程难审计
- 🔬 **研究方法**：提出Policy-Guided RAG治理框架，按策略控制检索信息使用并支持可审计生成
- 📌 **结论**：实现受控、可审计的LLM信息消费

### 21. Safeguarding LLM Agents from Misalignment through Provenance Analysis

📄 [arXiv](https://arxiv.org/abs/2607.01236) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/239/Safeguarding-LLM-Agents-from-Misalignment-through-Provenance-Analysis)　📅 2026-07　🏷 ASE 2026

**关键词**：`defense`、`action provenance`、`misalignment detection`、`pre-execution guard`

👤 **作者**：Yining She、Yiliang Liang、Eunsuk Kang

- 🎯 **研究动机**：现有运行时护栏用 LLM-as-judge，缺乏系统化对齐推理框架，判断不一致难审计
- 🔬 **研究方法**：提出 ProvenanceGuard：把失准检测形式化为拟议工具调用是否被上下文中可追溯证据支持，多阶段管线在执行前分析三类失准并只放行对齐动作
- 📌 **结论**：AgentSafetyBench 与 WorkBench、11 个 backbone 上失准轨迹错误率从 44.3% 降至 2.1%（另一基准 32.4%→18.7%），对成功轨迹干预从 31.2% 降至 13.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM agents gain increasing access to powerful tools, ensuring that their actions align with the user's intent becomes critical. When an agent's proposed action deviates from that intent---a phenomenon called misalignment---it may cause harm that is difficult to undo. Existing runtime guardrails rely on an LLM-as-a-judge paradigm that lacks a systematic framework for reasoning about alignment, often producing inconsistent or difficult-to-audit judgments. Motivated by provenance analysis, we propose a conceptual framework that formalizes misalignment detection as determining whether a proposed tool call is supported by traceable evidence in the agent's context. Based on this framework, we build ProvenanceGuard, a multi-stage pipeline that analyzes the agent's action for three types of misalignment before its execution and only allows aligned actions. We evaluated ProvenanceGuard on AgentSafetyBench and WorkBench, across 11 backbone LLMs. Compared to the LLM-as-a-judge baseline, ProvenanceGuard reduces error rate on misaligned traces from 44.3% to 2.1% on Agent-SafetyBench and from 32.4% to 18.7% on WorkBench, while reducing interventions on task-successful traces from 31.2% to 13.0% and introducing no statistically significant increase in unnecessary interventions on aligned traces. These results demonstrate that structured, provenance-based reasoning provides an effective and practical foundation for safeguarding LLM agents from misalignment.

</details>

### 22. SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification

📄 [arXiv](https://arxiv.org/abs/2607.13081)　📅 2026-07

**关键词**：`defense`、`operational threat`、`dual-mode guard`、`extensible taxonomy`

👤 **作者**：SingGuard Team

- 🎯 **研究动机**：agentic AI 面临提示注入、敏感信息抽取、恶意代码请求与资源耗尽等运营威胁，需要可扩展护栏
- 🔬 **研究方法**：提出 NSFA 风险分类法（185 个变体、CIA 三元组层级、交叉验证 OWASP 指南），构建 133 语言 93K+ 自建样本与 3,435 跨源样本基准；双模态检测：SFT 生成式推理离线审计+冻结骨干判别头实现约 50ms 实时检测
- 📌 **结论**：0.8B-9B 四个模型在自建基准 F1 均 >=94%，超最强竞品 6-12 个绝对点；9B 跨源评估 F1 91.29%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce the NSFA taxonomy, which organizes 185 risk variants into a CIA-triad-grounded hierarchy and is cross-validated against three well-established OWASP guidelines. Based on this taxonomy, we construct a benchmark suite spanning 133 languages, comprising over 93K purpose-built samples targeting both user queries and agent responses, along with 3,435 cross-source samples adapted from five public agent-security datasets. To detect these operational threats in practice, we develop a dual-mode approach combining SFT-based generative reasoning for interpretable offline auditing with discriminative classification heads on the frozen backbone, enabling real-time detection at approximately 50,ms. We release four models with 0.8B, 2B, 4B, and 9B parameters, all achieving $\geq$94% F1 on purpose-built benchmarks and surpassing the strongest competing guardrails by 6 to 12 absolute points. On cross-source evaluation, the 9B model attains 91.29% F1 with a more balanced precision--recall trade-off. Moreover, ablation experiments show that classification heads can equip a guardrail with risk detection capabilities beyond its original scope and achieve state-of-the-art performance. These results demonstrate the extensibility of the approach and its generality as a plug-in enhancement.

</details>

### 23. WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents

📄 [arXiv](https://arxiv.org/abs/2604.12284)　📅 2026-04

**关键词**：`detection`、`web prompt injection`、`parallel guard agent`、`multimodal webpage`

👤 **作者**：Yulin Chen、…、Bryan Hooi

- 🎯 **研究动机**：Web agent 易受 HTML 或截图中嵌入的 prompt 注入攻击，system prompt 防御与直接微调效果有限
- 🔬 **研究方法**：让专用 guard agent 与执行 agent 并行以解耦检测；以 GPT-5 构造 164 主题、230 种视觉风格的多模态数据，经推理密集 SFT 加 RL 训练 WebAgentGuard
- 📌 **结论**：多基准上一致超过强基线，保持 agent 效用且不增加额外延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web agents powered by vision-language models (VLMs) enable autonomous interaction with web environments by perceiving and acting on both visual and textual webpage content to accomplish user-specified tasks. However, they are highly vulnerable to prompt injection attacks, where adversarial instructions embedded in HTML or rendered screenshots can manipulate agent behavior and lead to harmful outcomes such as information leakage. Existing defenses, including system prompt defenses and direct fine-tuning of agents, have shown limited effectiveness. To address this issue, we propose a defense framework in which a web agent operates in parallel with a dedicated guard agent, decoupling prompt injection detection from the agent's own reasoning. Building on this framework, we introduce WebAgentGuard, a reasoning-driven, multimodal guard model for prompt injection detection. We construct a synthetic multimodal dataset using GPT-5 spanning 164 topics and 230 visual and UI design styles, and train the model via reasoning-intensive supervised fine-tuning followed by reinforcement learning. Experiments across multiple benchmarks show that WebAgentGuard consistently outperforms strong baselines while preserving agent utility, without introducing additional latency.

</details>

### 24. RefineAct: Automatic Runtime Verification of LLM Agent Actions

🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/79/RefineAct-Automatic-Runtime-Verification-of-LLM-Agent-Actions)　📅 2026　🏷 ASE 2026

**关键词**：`defense`、`runtime verification`、`tool action`、`policy compliance`

- 🎯 **研究动机**：LLM agent的tool action缺自动运行时验证
- 🔬 **研究方法**：RefineAct按策略自动验证并修正agent动作
- 📌 **结论**：拦截违规动作并提升policy合规

### 25. Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`role-playing Agent`、`persona-aware guard`、`retrieved safety rule`、`jailbreak`、`self-evolution`

- 🎯 **研究动机**：角色扮演 agent 越忠于人设越易被越狱，训练时方案维护成本高、损害角色内行为且对闭源模型不可行
- 🔬 **研究方法**：提出免训练双循环对抗自进化：攻击循环合成渐进更强的越狱提示，防御循环把失败蒸馏为全局安全规则、角色约束与安全角色示例的层级知识库供推理时检索组合
- 📌 **结论**：多个专有 LLM 上角色保真与抗越狱均超过强基线，并对未见角色与攻击提示鲁棒泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based role-playing has rapidly improved in fidelity, yet stronger adherence to persona constraints commonly increases vulnerability to jailbreak attacks, especially for risky or negative personas. Most prior work mitigates this issue with trainingtime solutions (e.g., data curation or alignmentoriented regularization). However, these approaches are costly to maintain as personas and attack strategies evolve, can degrade in-character behavior, and are typically infeasible for frontier closed-weight LLMs. We propose a training-free Dual-Cycle Adversarial Self-Evolution framework with two coupled cycles. A Persona-Targeted Attacker Cycle synthesizes progressively stronger jailbreak prompts, while a Role-Playing Defender Cycle distills observed failures into a hierarchical knowledge base of (i) global safety rules, (ii) persona-grounded constraints, and (iii) safe in-character exemplars. At inference time, the Defender retrieves and composes structured knowledge from this hierarchy to guide generation, producing responses that remain faithful to the target persona while satisfying safety constraints. Extensive experiments across multiple proprietary LLMs show consistent gains over strong baselines on both role fidelity and jailbreak resistance, and robust generalization to unseen personas and attack prompts.

</details>

### 26. Analyzing and Internalizing Complex Policy Documents for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2510.11588) · 🎓 [Official](https://aclanthology.org/2026.acl-long.767/)　📅 2025-10　🏷 ACL 2026

**关键词**：`defense`、`policy internalization`、`CAP-CPT`、`workflow complexity`

👤 **作者**：Jiateng Liu、…、Heng Ji

- 🎯 **研究动机**：Agent 每轮携带庞大策略文档开销高，纯 SFT 内化又随策略复杂度增加急剧退化
- 🔬 **研究方法**：提出四级可控复杂度基准生成器 CC-Gen，并设计 CAP-CPT：把策略解析为事实、行为、条件类别并隔离复杂条件，指导数据合成后以自回归预训练内化策略
- 📌 **结论**：CAP-CPT 全面超越 SFT 基线，在 Qwen-3-32B 上最高提升 41% 与 22%，prompt 长度减少 97.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM)-based agentic systems rely on in-context policy documents encoding diverse business rules. As requirements grow, these documents expand rapidly, causing high computational overhead. This motivates developing internalization methods that embed policy documents into model priors while preserving performance. Prior prompt compression work targets generic prompts, but agentic policy documents span multiple complexity levels and require deeper reasoning, making internalization harder. We introduce CC-Gen, an agentic benchmark generator with Controllable Complexity across four levels, enabling systematic evaluation of agents' ability to handle complexity and offering a unified framework for assessing policy internalization. Our analysis shows that complex policy specifications governing workflows pose major reasoning challenges. Supporting internalization with gold user agent interaction trajectories containing chain-of-thought (CoT) annotations via supervised fine-tuning (SFT) is data-intensive and degrades sharply as policy complexity increases. To mitigate data and reasoning burdens, we propose Category-Aware Policy Continued Pretraining (CAP-CPT). Our automated pipeline parses policy documents to extract key specifications, grouping them into factual, behavioral, and conditional categories, and isolating complex conditions that drive workflow complexity. This guides targeted data synthesis and enables agents to internalize policy information through an autoregressive pretraining loss. Experiments show CAP-CPT improves SFT baselines in all settings, with up to 41% and 22% gains on Qwen-3-32B, achieving 97.3% prompt length reduction on CC-Gen and further enhancing tau-Bench with minimal SFT data.

</details>

### 27. Building a Foundational Guardrail for General Agentic Systems via Synthetic Data

📄 [arXiv](https://arxiv.org/abs/2510.09781) · 📝 [OpenReview](https://openreview.net/forum?id=M47SWYubR5) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009978)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`pre-execution guard`、`synthetic trajectory`、`cross-planner transfer`

👤 **作者**：Yue Huang、…、Xiangliang Zhang

- 🎯 **研究动机**：现有 guardrail 多在执行后干预，风险一旦落地难以挽回，且存在数据、模型与评测三重缺口
- 🔬 **研究方法**：用 AuraGen 合成注入分级标签风险的轨迹语料，训练带跨 planner adapter 的基础 guardrail Safiron，并发布 Pre-Exec Bench 评测检测、分类、解释与跨 planner 泛化
- 📌 **结论**：Safiron 在 Pre-Exec Bench 上持续超越强基线，为执行前安全干预提供实用模板

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While LLM agents can plan multi-step tasks, intervening at the planning stage-before any action is executed-is often the safest way to prevent harm, since certain risks can lead to severe consequences once carried out. However, existing guardrails mostly operate post-execution, which is difficult to scale and leaves little room for controllable supervision at the plan level. To address this challenge, we highlight three critical gaps in current research: data gap, model gap, and evaluation gap. To close the data gap, we introduce AuraGen, a controllable engine that (i) synthesizes benign trajectories, (ii) injects category-labeled risks with calibrated difficulty, and (iii) filters outputs via an automated reward model, producing large and reliable corpora for pre-execution safety. To close the guardian model gap, we propose a foundational guardrail Safiron, combining a cross-planner adapter with a compact guardian model. The adapter unifies different input formats, while Safiron flags risky cases, assigns risk types, and generates rationales; trained in two stages with a broadly explored data recipe, Safiron achieves robust transfer across settings. To close the evaluation gap, we release Pre-Exec Bench, a realistic benchmark covering diverse tools and branching trajectories, which measures detection, fine-grained categorization, explanation, and cross-planner generalization in human-verified scenarios. Extensive experiments demonstrate consistent gains of the proposed guardrail over strong baselines on Pre-Exec Bench, and ablations further distill actionable practices, providing a practical template for safer agentic systems.

</details>

### 28. CompAgent: An Agentic Framework for Visual Compliance Verification

📄 [arXiv](https://arxiv.org/abs/2511.00171)　📅 2025-10　🏷 CVPR 2026

**关键词**：`defense`、`visual compliance`、`tool routing`、`agentic verification`

👤 **作者**：Rahul Ghosh、…、Chun-Hao Liu

- 🎯 **研究动机**：视觉合规验证缺乏通用方法，MLLM 又难以独自处理细粒度视觉细节并执行结构化规则
- 🔬 **研究方法**：CompAgent 给 MLLM 配备物体检测、人脸分析、NSFW 检测与描述等工具，由规划 agent 按合规策略动态选工具，再由验证 agent 融合图像、工具输出与策略推理
- 📌 **结论**：超越专用分类器与直接 MLLM 提示，UnsafeBench 上 F1 最高 76%、较 SOTA 提升 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual compliance verification is a critical yet underexplored problem in computer vision, especially in domains such as media, entertainment, and advertising where content must adhere to complex and evolving policy rules. Existing methods often rely on task-specific deep learning models trained on manually labeled datasets, which are costly to build and limited in generalizability. While recent Multimodal Large Language Models (MLLMs) offer broad real-world knowledge and policy understanding, they struggle to reason over fine-grained visual details and apply structured compliance rules effectively on their own. In this paper, we propose CompAgent, the first agentic framework for visual compliance verification. CompAgent augments MLLMs with a suite of visual tools-such as object detectors, face analyzers, NSFW detectors, and captioning models-and introduces a planning agent that dynamically selects appropriate tools based on the compliance policy. A compliance verification agent then integrates image, tool outputs, and policy context to perform multimodal reasoning. Experiments on public benchmarks show that CompAgent outperforms specialized classifiers, direct MLLM prompting, and curated routing baselines, achieving up to 76% F1 score and a 10% improvement over the state-of-the-art on the UnsafeBench dataset. Our results demonstrate the effectiveness of agentic planning and robust tool-augmented reasoning for scalable, accurate, and adaptable visual compliance verification.

</details>

### 29. Defeating Prompt Injections by Design

📄 [arXiv](https://arxiv.org/abs/2503.18813) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-03　🏷 SaTML 2026

**关键词**：`defense`、`policy enforcement`、`capability guard`、`non-interference`、`LLM agent`、`prompt injection`

👤 **作者**：Edoardo Debenedetti、…、Florian Tramèr

- 🎯 **研究动机**：LLM agent 处理不可信数据时易受 prompt injection，仅靠模型自身对齐无法根治
- 🔬 **研究方法**：提出 CaMeL 防御层，从可信查询显式提取控制流与数据流使不可信数据无法影响程序流，并以 capability 与策略约束工具调用
- 📌 **结论**：在 AgentDojo 上以可证明安全解决 77% 任务（无防御系统为 84%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in agentic systems that interact with an untrusted environment. However, LLM agents are vulnerable to prompt injection attacks when handling untrusted data. In this paper we propose CaMeL, a robust defense that creates a protective system layer around the LLM, securing it even when underlying models are susceptible to attacks. To operate, CaMeL explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow. To further improve security, CaMeL uses a notion of a capability to prevent the exfiltration of private data over unauthorized data flows by enforcing security policies when tools are called. We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. We release CaMeL at https://github.com/google-research/camel-prompt-injection.

</details>

### 30. AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection

🎓 [Official](https://aclanthology.org/2025.acl-long.399/)　📅 2025-02　🏷 ACL 2025

**关键词**：`defense`、`lifelong guardrail`、`adaptive safety check`、`tool compatibility`

👤 **作者**：Weidi Luo、…、Chaowei Xiao

- 🎯 **研究动机**：LLM agent 面临管理员定义的任务特定风险与源自设计漏洞的系统性风险，现有防御无法自适应且有效地缓解
- 🔬 **研究方法**：AGrail 终身 guardrail，具备自适应安全检查生成、安全检查优化与工具兼容性三要素
- 📌 **结论**：对任务特定与系统风险均取得强防御效果，并可跨不同 LLM agent 任务迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancements in Large Language Models (LLMs) have enabled their deployment as autonomous agents for handling complex tasks in dynamic environments. These LLMs demonstrate strong problem-solving capabilities and adaptability to multifaceted scenarios. However, their use as agents also introduces significant risks, including task-specific risks, which are identified by the agent administrator based on the specific task requirements and constraints, and systemic risks, which stem from vulnerabilities in their design or interactions, potentially compromising confidentiality, integrity, or availability (CIA) of information and triggering security risks. Existing defense agencies fail to adaptively and effectively mitigate these risks. In this paper, we propose AGrail, a lifelong agent guardrail to enhance LLM agent safety, which features adaptive safety check generation, effective safety check optimization, and tool compatibility & flexibility. Extensive experiments demonstrate that AGrail not only achieves strong performance against task-specific and system risks but also exhibits transferability across different LLM agents’ tasks.

</details>

### 31. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

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

### 32. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

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

### 33. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

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

### 34. RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards

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

### 35. AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security

📄 [arXiv](https://arxiv.org/abs/2605.29801)　📅 2026-05

**关键词**：`defense`、`trajectory guard`、`alignment diagnosis`、`scalable deployment`

👤 **作者**：Dongrui Liu、…、Xia Hu

- 🎯 **研究动机**：OpenClaw 类开放世界 agent 执行力强且攻击门槛降低，现有对齐框架难以支撑实际部署
- 🔬 **研究方法**：更新 agent 安全 taxonomy 覆盖 Codex 与 OpenClaw 场景；影响函数净化的数据引擎仅用约 1k 样本训练 0.8B-8B 的 AgentDoG 1.5，并构建高效 SFT/RL 环境与免训练在线护栏
- 📌 **结论**：小模型性能比肩 GPT-5.4 等闭源模型，Docker 级部署开销降低两个数量级，多交互场景达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern open-world agents such as OpenClaw exhibit powerful cross-environment execution capabilities yet introduce broad new safety risk sources. Meanwhile, advanced frontier AI models drastically lower attack barriers, rendering current agent alignment frameworks inadequate for real-world deployment. To tackle these emerging threats, we propose a lightweight and scalable agent safety alignment framework. Specifically, we update the agent safety taxonomy to accommodate emergent risks from Codex and OpenClaw execution scenarios. We further build a taxonomy-guided data engine with influence-function purification to train lightweight AgentDoG 1.5 variants (0.8B, 2B, 4B, and 8B parameters) using only around 1k samples, achieving comparable performance with leading closed-source models (e.g., GPT-5.4). Based on AgentDoG 1.5, we construct a highly efficient agentic safety SFT and RL training environment, which reduces deployment overhead in Docker-level environments by two orders of magnitude. Finally, we deploy AgentDoG 1.5 as a training-free online guardrail for real-time safety moderation. Extensive experimental results indicate that AgentDoG 1.5 achieves state-of-the-art performance in diverse and complex interactive agentic scenarios. All models and datasets are openly released.

</details>

### 36. AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security

📄 [arXiv](https://arxiv.org/abs/2601.18491)　📅 2026-01

**关键词**：`detection`、`diagnostic guardrail`、`trajectory assessment`、`agent safety`

👤 **作者**：Dongrui Liu、…、Xia Hu

- 🎯 **研究动机**：现有 guardrail 缺乏 agentic 风险感知与风险诊断的透明度
- 🔬 **研究方法**：提出按来源（where）、失败模式（how）、后果（what）正交分类的三维 taxonomy，配套 ATBench 与可诊断不安全动作根因的 AgentDoG 框架（Qwen/Llama 三尺寸 4B/7B/8B）
- 📌 **结论**：在多样复杂交互场景的 agent 安全审核上达 SOTA，提供超越二值标签的溯源诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of AI agents introduces complex safety and security challenges arising from autonomous tool use and environmental interactions. Current guardrail models lack agentic risk awareness and transparency in risk diagnosis. To introduce an agentic guardrail that covers complex and numerous risky behaviors, we first propose a unified three-dimensional taxonomy that orthogonally categorizes agentic risks by their source (where), failure mode (how), and consequence (what). Guided by this structured and hierarchical taxonomy, we introduce a new fine-grained agentic safety benchmark (ATBench) and a Diagnostic Guardrail framework for agent safety and security (AgentDoG). AgentDoG provides fine-grained and contextual monitoring across agent trajectories. More Crucially, AgentDoG can diagnose the root causes of unsafe actions and seemingly safe but unreasonable actions, offering provenance and transparency beyond binary labels to facilitate effective agent alignment. AgentDoG variants are available in three sizes (4B, 7B, and 8B parameters) across Qwen and Llama model families. Extensive experimental results demonstrate that AgentDoG achieves state-of-the-art performance in agentic safety moderation in diverse and complex interactive scenarios. All models and datasets are openly released.

</details>

### 37. DualMirage: Hunting Stealthy Multimodal LLM Agents via CAPTCHAs with Contour and Adversarial Illusions

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DualMirage_Hunting_Stealthy_Multimodal_LLM_Agents_via_CAPTCHAs_with_Contour_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`multimodal agent`、`CAPTCHA probe`、`adversarial illusion`

👤 **作者**：Bei Chen、Gaolei Li、Jun Wu、Jianhua Li

- 🎯 **研究动机**：隐蔽 MLLM agent 通过模仿人类行为逃避常规检测，构成 web 安全风险
- 🔬 **研究方法**：DualMirage 双管齐下 CAPTCHA：轮廓错觉（人类轻易感知、MLLM 难解释）加对抗错觉（人不可察觉扰动误导目标 MLLM 视觉编码器诱发可识别响应）
- 📌 **结论**：人类平均成功率 95.8%、阻断 MLLM agent 最高 100%，诱导模型主动暴露身份（白盒 58.8%、黑盒 21.9% 成功率）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Multimodal Large Language Models (MLLMs) has given rise to sophisticated autonomous agents capable of performing complex, human-like tasks across the web. However, this also introduces significant security risks, particularly from stealthy MLLM agents that can evade conventional detection mechanisms by mimicking human behavior. In this paper, we propose DualMirage, a novel CAPTCHA framework that proactively counters and identifies stealthy agents by exploiting fundamental disparities between human and machine perception. DualMirage employs a dual-pronged strategy: (1) Contour Illusions, which utilize cognitive principles to generate illusory contours that humans perceive effortlessly yet pose interpretation challenges for MLLMs; and (2) Adversarial Illusions, which embed human-imperceptible perturbations optimized to mislead the visual encoders of target MLLMs and thereby elicit characteristic, identifiable model responses. Evaluations on five state-of-the-art MLLMs demonstrate that DualMirage achieves an average 95.8% human success rate while blocking MLLM agents (up to 100% agent blocking rate), outperforming existing CAPTCHAs. Furthermore, DualMirage induces models to expose identities actively, achieving 58.8% white-box and 21.9% black-box attack success rates, proving effective against stealthy multimodal agents.

</details>

### 38. Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

📄 [arXiv](https://arxiv.org/abs/2608.22248)　📅 2026-08

**关键词**：`defense`、`analysis`、`Code Agent`、`indirect prompt injection`、`instruction-data separation`、`agent safeguard`

👤 **作者**：Jiahao Chen、…、Shouling Ji

- 🎯 **研究动机**：LLM 难以区分指令与数据导致间接 prompt injection，现有 guardrail 又陷入高延迟或严重过度拒答的安全—效用权衡
- 🔬 **研究方法**：以理论与实证说明 LLM 内在可分离 instruction 与 data；AEGIS 提取 instruction-sensitive projector 识别恶意指令，并以 Unified Multi-Layer Consensus 聚合网络深度上拓扑不同的信号
- 📌 **结论**：对启发式与优化式 IPI 攻击均显著优于基线，缓解高延迟与过度拒答的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between "instructions" and "data" to manipulate LLMs via maliciously injected instructions. Existing defenses, however, face an intractable safety-utility trade-off: most guardrails either incur high latency or suffer from severe over-refusal. In this paper, we first demonstrate that LLMs can separate instruction from data intrinsically with both theoretical and empirical evidence. Inspired by this insight, we propose AEGIS (Adaptive Ensemble Guard for Injection Shielding). AEGIS extracts instruction-sensitive projectors to identify malicious instructions and leverages a Unified Multi-Layer Consensus mechanism that aggregates topologically distinct signals across the network depth. Empirical evaluations show that AEGIS achieves remarkable detection performance against both heuristic and optimization-based attacks compared to baselines, highlighting its potential to mitigate IPI. Code is available at https://github.com/xaddwell/AEGIS

</details>

### 39. SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation

📄 [arXiv](https://arxiv.org/abs/2608.21500)　📅 2026-08

**关键词**：`defense`、`agent prompt injection`、`token-level alignment`、`adaptive robustness`、`indirect prompt injection`、`tool-call security`

👤 **作者**：Yibo Peng、Long Lian、David Wagner、Sizhe Chen

- 🎯 **研究动机**：防御性微调的 LLM 面对自适应 prompt injection 仍近 100% ASR，原因是 DPO/GRPO 等只给序列级反馈，模型无法学到具体哪些输出 token 不安全
- 🔬 **研究方法**：SecOPD 提供 token 级反馈的 on-policy 蒸馏：初始化模型在对应干净输入下为注入样本 rollout 的逐 token 打分，指导防御微调
- 📌 **结论**：防御后的 Qwen3.6-27B 对 SoTA 自适应攻击 PISmith 的 ASR 为 9.0%（先前 SoTA Meta-SecAlign 为 94.0%），且泛化到未见域的 agentic tool calling（ASR 4.7%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection is listed as the \#1 threat to AI agents. When an agent accesses external data from websites, files, or emails, an attacker may inject a prompt into the data, saying, "Ignore all prior instructions and perform <an attacker's task>." To prevent arbitrary manipulation of agents, defenders try to train secure LLMs, which, however, still suffer from near 100% attack success rates (ASRs) against adaptive prompt injections. We note that this is because existing defensive finetuning recipes rely on sequence-level feedback signals (in DPO or GRPO). Treating an entire output equally prevents the model from learning precisely which output tokens are insecure. In this paper, we propose Secure On-Policy Distillation (SecOPD) that provides token-level feedback to guide defensive fine-tuning. The LLM receives an injected sample and produces a rollout, whose tokens are scored by the initialization model given the corresponding clean input. With more fine-grained training signals, our defended Qwen3.6-27B achieves a 9.0% ASR against the SoTA PISmith adaptive prompt injections, compared to 94.0% for the prior SoTA, Meta-SecAlign. The obtained security generalizes to domains completely unseen in training: in agentic tool calling, SecOPD achieves a 4.7% ASR compared to 5.5% for Meta-SecAlign. Code and the model are available at https://github.com/pppyb/SecOPD and https://huggingface.co/pybbb/Qwen3.6-27B-SecOPD.

</details>

### 40. Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents

📄 [arXiv](https://arxiv.org/abs/2608.17153)　📅 2026-08

**关键词**：`defense`、`analysis`、`evidence-access control`、`System 2 gating`、`RAG Agent`、`System 2 reasoning`

👤 **作者**：Mehrdad Ghassabi

- 🎯 **研究动机**：LLM 可能正确检测文档含错误信息却仍受其影响；Cordon Principle 严格隔离又带来大量计算开销
- 🔬 **研究方法**：提出精化原则——只有具备 System 2 深思推理能力的 agent 才可访问不可信文档；构建量化误信息检测与下游影响之差的指标并对比推理与标准模型
- 📌 **结论**：推理能力模型对损坏证据鲁棒得多，无需 Cordon 式严格隔离，为安全 RAG 设计提供更实用基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

</details>

### 41. Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production

📄 [arXiv](https://arxiv.org/abs/2608.08471)　📅 2026-08

**关键词**：`defense`、`jailbreak`、`multi-agent system`、`agent guardrail`、`production guardrail`、`failure-driven training`

👤 **作者**：Cong Ming、…、Yingfei Xiang

- 🎯 **研究动机**：部署的 guardrail 一经训练即冻结，而新越狱手法与有害类别数天内出现，静态防御持续落后
- 🔬 **研究方法**：SESG 多 agent 系统监控线上流量，确认失败后由生成 agent 合成配对训练数据、验证 agent 纠偏、路由 agent 匹配训练动作并回传新版本
- 📌 **结论**：六轮线上演化中 1.7B guardrail 以 16-24 小时、约 2 小时人力适应新威胁（手工需 40-90 小时）；两个月自主关闭 14/15 个新威胁场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deployed LLM safety guardrails are predominantly static: trained once and frozen at release, while new jailbreak techniques and previously un-addressed harmful categories emerge within days, leaving the defense perpetually a step behind. We present SESG (Self-Evolving Safety Guardrails), a multi-agent system running in production. SESG monitors the live traffic behind a deployed guardrail and surfaces two classes of failure: jailbreaks novel in form and harmful categories novel in content. Once a failure is confirmed, a generation agent synthesizes paired training data targeted at it; a validation agent rebalances the batch toward the direction in which the deployed model errs, so that the model's own mistakes steer its training set; and a routing agent matches the training action to the diagnosed gap and returns the next version to production. Over six rounds of live evolution (V0 to V6), a 1.7B guardrail adapts to a new threat in 16-24 hours, with about 2 hours of human effort, versus the 40-90 hours of the manual process it replaces. On six emerging threats, it outperforms static guardrails from 0.6B to 9B and an adaptive baseline while preserving its general screening competence. Since April 2026, SESG has been the primary update pipeline of Sangfor's guardrail, autonomously closing 14 of 15 new threat scenarios in two months. We release 9 test sets for the 6 new threats at https://github.com/Trams1017/SESG. Warning: This paper contains examples that may be harmful or offensive.

</details>

### 42. Steering Instruction Hierarchies at Inference Time

📄 [arXiv](https://arxiv.org/abs/2607.26228) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`defense`、`prompt injection`、`agent guardrail`、`action policy`、`instruction hierarchy`、`value-vector editing`

👤 **作者**：Siqi Zeng、Sewoong Lee、Han Zhao、Julia Hockenmaier

- 🎯 **研究动机**：指令层级是部署的核心安全假设（系统提示应覆盖用户/工具输入），但前沿 LLM 常违反
- 🔬 **研究方法**：提出 V-Steer 免训练推理时方法：用 direct logit attribution 定位低优先级 span 压制特权 span 的注意力头，对缓存 V 张量做乘性编辑放大特权、抑制冲突低优先级，兼容融合注意力后端
- 📌 **结论**：7B-70B 模型上把角色冲突基准的主约束准确率从 18% 以下提升到 92%，在四个规模中三个匹配或超越 SOTA 训练方法且解码速度开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools. Yet frontier LLMs often violate this hierarchy. We introduce V-Steer, a training-free inference time method that restores privileged influence by editing cached value vectors at prompt positions. Using direct logit attribution on the first next token prediction, V-Steer identifies heads where lower priority spans dominate privileged ones, then boosts privileged spans and suppresses conflicting lower priority spans through in-place multiplicative edits to cached V tensors. Since the method acts only on cached values, it remains compatible with fused attention backends and adds only a one time prefill overhead. Across models from 7B to 70B, this attribution guided intervention raises primary constraint accuracy from under 18% up to 92% on controlled role conflict benchmarks, and on broader instruction hierarchy evaluations substantially outperforms prompt only baselines while matching or exceeding SoTA training based methods on 3 of 4 scales of LLMs, with negligible decoding-speed overhead. The code is available at https://github.com/cindy2000sh/v-steer.

</details>

### 43. From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.05805)　📅 2026-06

**关键词**：`defense`、`agent guardrail`、`action policy`、`workflow compliance`

👤 **作者**：Yuhao Sun、Jiacheng Zhang、Shaanan Cohney、Zhexin Zhang、Feng Liu、Xingliang Yuan

- 🎯 **研究动机**：现有护栏把被污染任务整体判为不安全直接阻断，牺牲良性部分，且缺少护栏干预对下游行为影响的评估
- 🔬 **研究方法**：提出 TRIAD：微调模型输出 proceed/refuse/update 三分决策加结构化自然语言反馈，update 引导 agent 修订计划规避有害成分并保留良性任务，形成护栏-规划闭环
- 📌 **结论**：ASB 与 AgentHarm 上平均 ASR 降至 10.42%，在护栏集成基线中取得最佳安全-效用权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based guardrails typically safeguard agents by evaluating proposed actions or inputs before execution, producing safety signals such as binary allow/deny decisions, risk categories, and/or explanatory rationales about potential policy violations. However, agent risks often arise when otherwise benign tasks are contaminated by untrusted external content, unsafe instructions, or risky tool use. Existing guardrails often flag the entire task uniformly as unsafe, thereby blocking the threat but sacrificing the benign part. Moreover, existing work largely evaluates guardrails in isolation, leaving unclear whether their interventions lead to safer downstream agent behavior. To address this, we introduce TRIAD (Tripartite Response for Iterative Agent Guardrailing), a guardrail-integrated agent framework that leverages guardrail-generated verbal feedback as a guiding signal to keep the agent aligned with benign objectives at each planning step. We finetune a language model on a self-curated training dataset to output one of three decisions: proceed, refuse, or update, together with structured natural-language feedback. Rather than merely allowing or blocking execution, update guides the agent to revise its plan, avoid harmful components, and preserve the benign task where possible. TRIAD injects this feedback into the agent's context, enabling subsequent plan revision and forming a closed loop between guardrail feedback and agent planning. Extensive experiments on ASB and AgentHarm show that TRIAD reduces the average attack success rate to 10.42%, while achieving the best safety-utility trade-off among guardrail-integrated baselines. Our code is available at: https://github.com/YUHAOSUNABC/TRIAD.

</details>

### 44. SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety

📄 [arXiv](https://arxiv.org/abs/2605.05704) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64556)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`agent safety`、`over-refusal`、`adversarial robustness`、`empirical evaluation`、`failure recovery`

👤 **作者**：Zhe Liu、…、Hao Peng

- 🎯 **研究动机**：现有 agent 防御难以平衡安全与效用，常对良性请求过度拒答
- 🔬 **研究方法**：SafeHarbor 经增强对抗生成提取上下文感知防御规则，用本地层级记忆动态注入并辅以信息熵驱动的节点分裂合并自演化，免训练即插即用
- 📌 **结论**：在歧义良性任务与显式恶意攻击上均达 SOTA，GPT-4o 上良性效用峰值 63.6% 且有害请求拒答率保持 93% 以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in foundation models have transformed LLMs from passive conversational systems into autonomous agents capable of reasoning and tool execution. While these capabilities unlock substantial practical value, they also introduce new security risks, as adversaries can manipulate agents into performing harmful actions in real-world environments. Existing defense strategies mitigate such threats but frequently struggle to balance safety and utility, resulting in over-refusal of benign user requests. To mitigate this trade-off, we propose SafeHarbor, a novel framework designed to establish precise decision boundaries for LLM agents. Unlike static guidelines, SafeHarbor extracts context-aware defense rules through enhanced adversarial generation. We design a local hierarchical memory system for dynamic rule injection, offering a training-free, efficient, and plug-and-play solution. Furthermore, we introduce an information entropy-based self-evolution mechanism that continuously optimizes the memory structure through dynamic node splitting and merging. Extensive experiments demonstrate that SafeHarbor achieves state-of-the-art performance on both ambiguous benign tasks and explicit malicious attacks, notably attaining a peak benign utility of 63.6\% on GPT-4o while maintaining a robust refusal rate exceeding 93\% against harmful requests. The source code is publicly available at https://github.com/ljj-cyber/SafeHarbor.

</details>

### 45. Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense

📄 [arXiv](https://arxiv.org/abs/2602.09012) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60816)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`agent safety`、`agent guardrail`、`action policy`、`empirical evaluation`、`failure recovery`

👤 **作者**：Jiacheng Liu、Yaxin Luo、Jiacheng Cui、Xinyi Shang、Xiaohan Zhao、Zhiqiang Shen

- 🎯 **研究动机**：Gemini3-Pro-High、GPT-5.2-Xhigh 等推理模型在 OpenCaptchaWorld 通过率达 90%，传统验证码对 GUI agent 失效
- 🔬 **研究方法**：构建后端支持、可近乎无限生成的动态 CAPTCHA 框架，利用交互感知、记忆、决策与动作上的人机认知差设计任务
- 📌 **结论**：重建生物用户与 agent 的可靠区分，为 agentic 时代提供可扩展、多样的防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of GUI-enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, recent advancements in reasoning-heavy models, such as Gemini3-Pro-High and GPT-5.2-Xhigh have effectively collapsed this security barrier, achieving pass rates as high as 90% on complex logic puzzles like "Bingo". In response, we introduce Next-Gen CAPTCHAs, a scalable defense framework designed to secure the next-generation web against the advanced agents. Unlike static datasets, our benchmark is built upon a robust data generation pipeline, allowing for large-scale and easily scalable evaluations, notably, for backend-supported types, our system is capable of generating effectively unbounded CAPTCHA instances. We exploit the persistent human-agent "Cognitive Gap" in interactive perception, memory, decision-making, and action. By engineering dynamic tasks that require adaptive intuition rather than granular planning, we re-establish a robust distinction between biological users and artificial agents, offering a scalable and diverse defense mechanism for the agentic era.

</details>

### 46. VIGIL: Defending LLM Agents Against Tool-Stream Injection via Verify-Before-Commit

🎓 [Official](https://aclanthology.org/2026.acl-long.443/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`agent safety`、`LLM agent`、`agent guardrail`、`runtime guardrail`

👤 **作者**：Junda Lin、…、Enhong Chen

- 🎯 **研究动机**：工具流中被操纵的元数据与运行时反馈可劫持智能体执行，静态防护又会切断自适应推理所需的反馈回路
- 🔬 **研究方法**：提出 VIGIL：从限制性隔离转向 verify-before-commit 协议，推测性假设生成加意图锚定验证；并构建含 959 个工具流注入案例的 SIREN 基准
- 📌 **结论**：较 SOTA 动态防御降低攻击成功率超 22%，攻击下效用较静态基线翻倍以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents operating in open environments face escalating risks from indirect prompt injection, particularly within the tool stream where manipulated metadata and runtime feedback hijack execution flow. Existing defenses encounter a critical dilemma as advanced models prioritize injected rules due to strict alignment while static protection mechanisms sever the feedback loop required for adaptive reasoning. To reconcile this conflict, we propose VIGIL, a framework that shifts the paradigm from restrictive isolation to a verify-before-commit protocol. By facilitating speculative hypothesis generation and enforcing safety through intent-grounded verification, VIGIL preserves reasoning flexibility while ensuring robust control. We further introduce SIREN, a benchmark comprising 959 tool stream injection cases designed to simulate pervasive threats characterized by dynamic dependencies. Extensive experiments demonstrate that VIGIL outperforms state-of-the-art dynamic defenses by reducing the attack success rate by over 22% while more than doubling the utility under attack compared to static baselines, thereby achieving an optimal balance between security and utility. Our code is available at: https://github.com/Touring-686/vigil.

</details>

### 47. SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning

🎓 [Official](https://aclanthology.org/2026.acl-long.522/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`reasoning safety`、`agent safety`、`LLM agent`

👤 **作者**：Lichao Wang、…、Juntao Dai

- 🎯 **研究动机**：MCP 扩大了 agent 动作空间并带来 power-seeking 风险，微小错误或幻觉会被放大为灾难性失败
- 🔬 **研究方法**：提出服务端防御插件 SafeMCP：用内部世界模型做前瞻推理，主动过滤高危工具扩张并即时干预兜底，经环境动态接地、安全策略初始化与双可验证奖励 RL 三阶段训练
- 📌 **结论**：在 PowerSeeking Bench、ToolEmu 与 AgentHarm 上达到安全均衡，在保持效用的同时有效缓释风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Model (LLM) agents increasingly leverage the Model Context Protocol (MCP) to operate in complex environments, the expansion of their action spaces offers agents unsafe capabilities and underscores the risk of power-seeking. While broad action space and greater environment influence are essential for task fulfillment, they creates a fragile risk surface where minor errors or hallucinations are magnified into catastrophic failures. In response, we propose SafeMCP, a server-side defense plugin that constrains tool acquisition via predictive reasoning regarding future safety risks. SafeMCP utilizes an internal world model for look-ahead reasoning to implement a two-tier defense: proactive tool filtering to constrain hazardous power expansion and immediate intervention as a fail-safe. To train SafeMCP, we introduce a three-stage pipeline comprising environmental dynamic grounding, safe policy initialization, and reinforcement learning (RL) with dual verifiable rewards. Experiments on PowerSeeking Bench, ToolEmu, and AgentHarm show that SafeMCP achieves a safe equilibrium, effectively mitigating risks while preserving agent utility.

</details>

### 48. SafeAgent: Safeguarding LLM Agents via an Automated Risk Simulator

🎓 [Official](https://aclanthology.org/2026.acl-long.1501/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`agent safety`、`LLM agent`、`agent guardrail`、`runtime guardrail`

👤 **作者**：Xueyang Zhou、…、Lichao Sun

- 🎯 **研究动机**：多轮工具增强 agent 中动态交互、外部工具与意外有害行为使安全保障困难
- 🔬 **研究方法**：提出 SafeAgent：开放威胁模型 OTS 把风险分解为指令、上下文与动作诱发三类，自动化合成压力测试场景与自反思安全响应，无需危险真实数据
- 📌 **结论**：在 4 个开源模型上安全表现平均提升 45%，真实终端任务提升 28.91%，超过 SOTA 闭源模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents are rapidly being deployed in real-world applications (e.g., digital assistants and customer service), making safety a critical concern. However, in multi-turn, tool-augmented settings, dynamic user interactions, external tool use, and unintended harmful behaviors make robust safety assurance challenging. To address these challenges, we propose SafeAgent, a framework that improves agent safety through fully automated synthetic data generation. SafeAgent introduces (1) an open and extensible threat model OTS that decomposes agent risk into instruction-, context-, and action-induced sources to ground safety analysis and alignment; and (2) an automated pipeline that instantiates OTS to surface scenario-specific failure modes, stress-test agents, and generate self-reflective safe responses—without hazardous real-world data collection. We evaluate SafeAgent on two safety benchmarks and one real-world terminal task. Across four widely used open-source models, SafeAgent improves safety performance by 45% on average and delivers a 28.91% gain on the real-world task, outperforming state-of-the-art closed-source models. These results highlight the practical advancement and scalability of SafeAgent in building safer LLM agents for real-world deployment.

</details>

### 49. When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

📄 [arXiv](https://arxiv.org/abs/2608.23550)　📅 2026-08

**关键词**：`analysis`、`CLAUDE.md`、`soft security rule`、`hard permission control`、`policy enforcement gap`、`natural-language rule`

👤 **作者**：Ting Yan

- 🎯 **研究动机**：CLAUDE.md 中"do not"是模型解释的自然语言指令，Claude Code 的 deny 是行动前阻断的内置控制，两者表达同一安全目标却控制方式不同，差距未被测量
- 🔬 **研究方法**：从 481 个公开 CLAUDE.md 抽取安全规则，由 LLM 匹配 Claude Code 文档化控制，两名安全从业者独立盲审抽样
- 📌 **结论**：严格标准下仅 4.4%（95% CI 2.6–6.7%）的安全规则有匹配内置控制（宽松标准 4–16%）——CLAUDE.md 是只写通道，prompt 禁令不能证明 policy 已被强制执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In CLAUDE.md, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public CLAUDE.md files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers or each other's labels. Depending on how closely a control had to match the written rule, only about 4-16% of the retrieved security rules had a matching built-in control. Under the strictest standard the estimate was 4.4% (95% CI: 2.6-6.7%), and the two annotators agreed closely on which rules had a match. A manual review of complete files found that our extraction method captured 66.3% of eligible security rules; the reported rates therefore apply to the rules it captured. This is a usable security problem: CLAUDE.md is a write-only channel. A developer writes a security rule but gets no feedback on whether a control will enforce it. The same plain-text form hides two kinds of rule: those a permission rule, mode, or sandbox can enforce, and those left to the model to interpret.

</details>

### 50. One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI

📄 [arXiv](https://arxiv.org/abs/2608.18360)　📅 2026-08

**关键词**：`analysis`、`agent guardrail`、`action policy`、`workflow compliance`

👤 **作者**：Gaston Besanson

- 🎯 **研究动机**：agent 同时受权威、资源、证据多个前动作控制，一个控制的补救会改变另一控制评估的动作、证据或上下文，使其先前判断失效
- 🔬 **研究方法**：形式化补救诱导控制耦合并给出 remediate-and-regate 协议恢复每动作可靠性；有限模型检查器证明两个补救算子不交换；30 个预注册种子上实证
- 📌 **结论**：补救顺序是控制面语义而非实现细节；组合不制造新检测覆盖——须诚实报告；证据缓冲的当前可纳性也不代表未来引用可信

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI systems take consequential actions governed by more than one pre-action control at once: authority, resource, and evidence gates that can admit, degrade, or remediate an action before it executes. This paper's central object is remediation-induced control coupling: a remediation applied by one control can change the action, evidence, or context another control evaluates, invalidating that control's earlier judgment. We formalize this coupling and give a remediate-and-regate protocol that restores per-action soundness in the current bounded, idempotent setting under its stated assumptions. We further show that the two implemented remediation operators (evidence substitution and resource-budget downroute) do not commute -- a finite-model checker finds concrete counterexample instances -- making remediation order part of the control-plane semantics rather than an implementation detail. A governed evidence buffer that trusts its own most recent admitted write is a further instance of the same problem at the level of state -- current admissibility does not imply future reference trustworthiness -- and is vulnerable to poisoning from declared-uncovered defect classes; two mitigations reduce, not eliminate, that exposure. Supporting results establish the exact condition under which positive-weight linear aggregation of gate outcomes can compensate a member veto, a unified cross-control Evidence Set, and that composition manufactures no new detection coverage, reported honestly. Empirically, on a deterministic open-data artifact composing three published engines unmodified, CH1-CH5 meet their registered decision rules across all 30 pre-registered seeds; CH6 does so under W1 but not under the smaller W2 workflow, reported as such. This is a mechanism demonstration on open payload data with a synthetic metadata layer, not a claim about production prevalence.

</details>

### 51. A Policy Algebra for Trust-Preserving Agentic AI Execution

📄 [arXiv](https://arxiv.org/abs/2608.16402)　📅 2026-08

**关键词**：`analysis`、`agent guardrail`、`action policy`、`workflow compliance`

👤 **作者**：Bhaskar Tripathi、Anurag Kumar、Ramendra Kumar、Bhavesh Gadhe

- 🎯 **研究动机**：企业执行要求可靠能力——经未授权数据访问、扩大授权或预算耗尽产出的成功不可靠，现有框架只优化能力
- 🔬 **研究方法**：把可靠能力定义为路径性质并提出策略代数：安全画像与运行时义务经 join、交、预算收窄、审批继承与证据积累组合成信任保持的最少限制状态，限制跨多 agent 调用传播并引入成本感知工件物化
- 📌 **结论**：干预 94.8% 策略违规事件同时保留 86.9% 任务完成率，消除画像单调性与工件耗尽违规，审计完整性升至 98.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-based agentic frameworks primarily optimize capability: whether an agent can reason, retrieve information, call tools, delegate work, and complete a goal. Enterprise execution requires a stronger property. A successful result is not reliable if it was produced through unauthorized data access, widened delegated authority, unapproved side effects, unrecoverable budget consumption, or incomplete evidence. This paper defines reliable capability as a path property: an agent is reliably capable only when it completes a task through action events that remain admissible under identity, profile, tool, data, memory, budget, artifact, approval, and audit constraints. We propose a policy algebra that defines the reliability envelope within which agent capability may be exercised. Security profiles and runtime obligations compose through joins, intersections, budget narrowing, approval inheritance, and evidence accumulation; the resulting composition is both trust-preserving and the least restrictive state satisfying all governing inputs. The algebra also propagates restrictions across multi-agent calls and introduces cost-aware artifact materialization, which redirects open-ended execution toward a recoverable outcome as budget exposure grows. The evaluation is interpreted as a reliability-capability trade-off rather than a capability benchmark: the policy-algebra runtime intervenes on 94.8% of policy-violating events while retaining an 86.9% task-completion rate, eliminates the observed profile-monotonicity and zero-artifact-exhaustion violations, and increases audit completeness to 98.6%. The method provides researchers and practitioners with formal correctness conditions, executable decision semantics, and trace evidence for building agents that are not only capable, but reliably capable.

</details>

### 52. Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance

📄 [arXiv](https://arxiv.org/abs/2608.16055)　📅 2026-08

**关键词**：`analysis`、`agent guardrail`、`action policy`、`workflow compliance`

👤 **作者**：Bowen Li、Guojun Wang

- 🎯 **研究动机**：现有基准只问任务是否完成，不问是否在政策内完成；把 agent 分解为组件是否损害治理未知
- 🔬 **研究方法**：Fiducia-bench 评测金融 agent 可治理性（应报即报、应弃即弃、留审计痕迹）；626 个 episode 跨 100 个 KYC/AML 任务变体、2 个模型、3 种架构
- 📌 **结论**：32B 模型在约束距离 2 下事实衰减从单环 0% 升至固定管线 56%、orchestrator-subagent 85%；同一机制依被丢事实是风险信号还是免责信号分别造成漏报与过报

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing agent benchmarks ask whether the agent finished the task. We ask whether it finished it within policy. We introduce Fiducia-bench, a benchmark for the governability of financial agents---whether they escalate when obligated, abstain when required, and leave an auditable trail---and use it to study a question no prior benchmark addresses: does decomposing an agent into components degrade its governance? It does, and the mechanism is specific. Policy-relevant facts discovered by one component are attenuated at the handoff boundary before reaching the component that must act on them. In a 626-episode experiment across 100 KYC/AML task variants, two models, and three architectures, a 32B open-weights model attenuated 0% of discovered facts under a single-loop baseline, 56% under a fixed pipeline, and 85% under an orchestrator-subagent architecture (all at constraint distance 2). A stronger model (gpt-4.1-mini) attenuated 3-6% under the same conditions, suggesting the governance cost of decomposition is partly a function of model capability. Critically, the same mechanism produces both under-escalation and over-escalation, depending on whether the dropped fact was a risk signal or an exculpating one. The benchmark, all tasks, and the verification harness are open-source

</details>

### 53. TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions

📄 [arXiv](https://arxiv.org/abs/2608.15391)　📅 2026-08

**关键词**：`analysis`、`agent guardrail`、`action policy`、`workflow compliance`

👤 **作者**：Md Fazley Rafy

- 🎯 **研究动机**：LLM 电网助手生成的命令语法有效不等于物理可容许，缺模型无关的运行时授权
- 🔬 **研究方法**：TwinGridShield 在确定性网络孪生中评估连通性、支路潮流、发电机与切负荷不变式再放行，决策记入哈希链日志；IEEE 14 节点受控研究含模型失配评估
- 📌 **结论**：500 次受攻试验零不安全放行；但 ±20% 负荷测量误差下不安全接受达 5.63%、真实支路额定低 20% 时达 30.09%——验证的是对编码授权谓词的符合而非模型误差下的安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-assisted energy-management tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime authorization layer that evaluates each proposed action in a deterministic network twin before release. The prototype checks connectivity, branch-flow, generator, and load-shedding invariants and records each decision in a hash-chained log. A controlled IEEE 14-bus study evaluates single-step switching, redispatch, and load-shedding actions using DC power flow and experimentally assigned branch ratings. In the matched-model experiment, a stochastic proposal source configured to select an unsafe action with probability p=0.84 produced 421 unsafe proposals in 500 attacked-condition trials, a realized rate of 84.2%. This value characterizes the configured surrogate and is not an empirical measurement of LLM prompt-injection susceptibility. TwinGridShield produced 0 unsafe releases in those 500 trials. Because action labeling and authorization used the same DC model, system state, branch ratings, and encoded constraints, this result verifies conformance of the implementation to its encoded authorization predicate rather than safety under model error. The principal robustness evaluation therefore introduces model mismatch. Unsafe acceptance reached 5.63% under bounded +20% and -20% per-bus load-measurement error and 30.09% when actual branch ratings were 20% below modeled ratings.

</details>

### 54. Agentic Oversight via Dialectic Reasoning

🎓 [Official](https://aclanthology.org/2026.acl-long.1143/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`reasoning safety`、`agent guardrail`、`action policy`、`agent safety`、`LLM agent`

👤 **作者**：Leonardo Ranaldi、Federico Ranaldi

- 🎯 **研究动机**：Debate 作为 LLM 监督机制缺乏可验证证据且可扩展性未被探索
- 🔬 **研究方法**：提出 Agentic Oversight：两个专家模型经辩证论证各自为信念一致的答案辩护，第三个盲裁判用 Dialectic Argumentation 裁定胜者，扩展至多语言与多模态
- 📌 **结论**：六个任务上辩证论证持续优于单专家基线；弱模型的辩证判断经微调可给专家模型注入无监督推理信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Debate has emerged as a promising oversight mechanism for Large Language Models (LLMs) amid rising systemic complexity, particularly where models outperform human evaluators. Yet, Debate provides little verifiable evidence for its final judgments, and its scalability remains largely unexplored. To make oversight grounded and scale as capabilities extend, we introduce an Agentic Oversight framework. By using Dialectic Argumentation as a reasoning function, we extend this paradigm to multilingual and multimodal spaces. We employ a weak-to-strong oversight approach based on two expert models that evaluate and defend contesting answers, while a third blind judge determines the winner using Dialectic Argumentation. Experts argue only for belief-consistent answers, founding the Debate on disagreements. We experimented with six tasks on our framework in both multilingual and multimodal scenarios, and dialectic argumentation consistently outperforms single-expert baselines. Moreover, we show that dialectic judgements from a weaker model deliver argument-mediated supervision that, via fine-tuning, instils unsupervised reasoning signals in expert models.

</details>