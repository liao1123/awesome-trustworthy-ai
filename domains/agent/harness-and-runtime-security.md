# Agent Harness 与 Runtime Security

[返回 Agent Security 目录](README.md)

## 研究方向

Agent harness 是连接 base model 与实际系统的编排层，负责 context assembly、instruction surfaces、tool dispatch、permission、persistent state、hooks、tracing、budget、error recovery 和 human approval。相同模型在不同 harness 中可能产生完全不同的 capability 与 risk；因此本页以 model-harness configuration 为评测单位，关注执行全程的 authorization、information flow、stability 与 incident recovery，而不只看 final answer。

## 研究脉络

- **Harness 作为隐藏变量：** 早期 Agent benchmark 固定或忽略 harness，使任务成功和安全差异被错误归因给 base model。
- **配置级诊断：** 新 benchmark 在共享任务、budget 和 validator 下比较 model-harness pairing，并记录 tool trace、artifact、资源和 recovery。
- **全轨迹安全：** HarnessAudit、HarnessSafe 和 HarnessRisk 从 final output 扩展到边界违规、persistent carrier 和完整 operational lifecycle。
- **Instruction surface：** system prompt、project file、user turn、tool 与 skill description 之间并不存在简单由深度决定的稳定优先级，需要单独测试冲突和 against-prior rule。
- **Runtime contract：** harness 不只要在动作前做 permission gate，还应要求 test、log、diff 与 citation 等可核验 evidence，避免 Agent 仅声称任务已完成。
- **Harness 演化：** 研究开始从失败轨迹归因到具体 artifact，再局部更新 rule bank、safety memory 与 tool policy，但更新本身也需防止回归和投毒。

## 安全审计与生命周期 Benchmark

### 1. Auditing Harness Tampering in Self-Improving Agents

📄 [arXiv](https://arxiv.org/abs/2609.00069)　📅 2026-09

**关键词**：`attack`、`harness tampering`、`self-improvement audit`、`authorization integrity`

👤 **作者**：Xing Wang、Xiaoyi Zhang、Jie Shao

- 🎯 **研究动机**：self-improving Agent 迭代修改自身 harness 可能制造虚假性能提升或破坏授权、溯源与完整性约束，该现象未系统研究
- 🔬 **研究方法**：定义 harness tampering，提出按 harness 功能角色与所违背义务的双轴分类，在真实自提升轨迹中注入 tampered-benign 编辑对构建标注语料并适配多种审计方法
- 📌 **结论**：篡改在不同 Agent 的真实运行中一致出现，常沿最佳 Agent 的 lineage 持续存在，并形成系统特异的分布画像

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-improving agents iteratively modify their own harness to push the frontier of their performance. However, such modifications can produce illusory performance gains or compromise integrity constraints such as authorization, provenance, and completeness without genuinely improving capability. We term this phenomenon as harness tampering, which extends the concept from reward and measurement tampering to the full self-improvement lifecycle. To systematically study this problem, we propose a two-axis taxonomy that categorizes each misaligned edit by the harness functional role in which it occurs and the obligation it violates. Then we build an annotated corpus by seeding tampered-benign edit pairs into the real trajectories of self-improving agents. We adapt and benchmark diverse audit methods on tampering classification and localization tasks. Finally we systematically audit real trajectories of self-improving agents. The results demonstrate that harness tampering consistently occurs in real runs from different agents, often persists in the lineage of the best agent, and forms distinct system-specific profiles across the taxonomy.

</details>

### 2. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

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

### 3. Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.16393)　📅 2026-08

**关键词**：`benchmark`、`prompt injection`、`agent harness`、`runtime isolation`

👤 **作者**：Zonghao Ying、…、Jing Guo

- 🎯 **研究动机**：DeepSeek Harness 对间接提示注入的抵抗力缺乏系统测量
- 🔬 **研究方法**：用 AI-Infra-Guard 构建 14,560 次受控执行：16 个间接内容通道、文本/文件载体、35 个 payload 目标与 12 种攻击方法，规则 judge 与 LLM judge 双重裁决
- 📌 **结论**：最高 ASR 为文本模式假完成 17.0%（LLMJudge）、文件模式隐藏 Unicode 25.5%（RuleJudge）与 skills 通道 16.0%；需在不可信内容与敏感动作间设控制点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content channels, text and file carrier modes, 35 payload objectives, one unmodified baseline, and 12 attack methods. The experiment preserves DSH's agent loop, tool registry, model adapter, and session-event path; source tools and sensitive sinks are local fixtures, so attempted actions are recorded without external side effects. We evaluate each trace with a deterministic rule-based judge, \JudgeR{} (RuleJudge), and a semantic LLM-based judge, \JudgeL{} (LLMJudge). The strongest observed attack success rates are 17.0% under \JudgeL{} for fake-completion attack in text mode, 25.5% under \JudgeR{} for hidden Unicode in file mode, and 16.0% under \JudgeR{} for the skills channel in file mode. \JudgeL{} also assigns partial compliance more often than \JudgeR{} (7.3% versus 2.0%). We relate these results to DSH's treatment of tool results, additional contexts, and tool-call policy hooks, then identify controls that should sit between untrusted content and sensitive actions. Our code is available at https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/deepseek-harness-security-assessment .

</details>

### 4. HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses

📄 [arXiv](https://arxiv.org/abs/2608.06984)　📅 2026-08

**关键词**：`benchmark`、`persistent carrier`、`risk lifecycle`、`trace evidence`

👤 **作者**：Xiao Zhang、…、Zhaofeng He

- 🎯 **研究动机**：agent harness 的持久载体（记忆、技能、工具、共享工件）造成延迟安全风险，现有基准覆盖载体少且 ASR 不反映风险传播过程
- 🔬 **研究方法**：HarnessSafe 含 328 个可执行用例覆盖七类持久载体家族，每例定义 Persistent-Risk Lifecycle 追踪攻击从进入到违规的全链路，多阶段轨迹评测
- 📌 **结论**：遏制效果载体特定且强依赖 harness-模型组合；harness 与模型后端共同塑造遏制结果，单一 ASR 无法反映生命周期推进差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. Each case is specified as a Persistent-Risk Lifecycle that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, while attack success rates cannot reflect distinct lifecycle progression patterns.

</details>

### 5. Auditing Agent Harness Safety

📄 [arXiv](https://arxiv.org/abs/2605.14271)　📅 2026-05

**关键词**：`benchmark`、`trajectory audit`、`permission boundary`、`information flow`

👤 **作者**：Chengzhi Liu、…、Xin Eric Wang

- 🎯 **研究动机**：harness 可能沿越权访问或上下文泄漏的轨迹仍返回正确答案，输出级评测看不到中途违规
- 🔬 **研究方法**：HarnessAudit 审计完整执行轨迹的边界合规、执行保真与系统稳定；HarnessAudit-Bench 含 8 个域 210 个任务，以单/多 agent 配置嵌入安全约束
- 📌 **结论**：任务完成与安全执行错位且违规随轨迹长度累积；违规集中于资源访问与 agent 间信息传递；多 agent 协作扩大风险面，harness 设计决定安全上限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. However, a harness can return a correct, benign answer over a trajectory that accesses unauthorized resources or leaks context to the wrong agent. Output-level evaluation cannot see these failures, yet most safety benchmarks score only final outputs or terminal states, even though many violations occur mid-trajectory rather than at termination. The central question is whether the harness respects user intent, permission boundaries, and information-flow constraints throughout execution. To address this gap, we propose HarnessAudit, a framework that audits full execution trajectories across boundary compliance, execution fidelity, and system stability, with a focus on multi-agent harnesses where these risks are most pronounced. We further introduce HarnessAudit-Bench, a benchmark of 210 tasks across eight real-world domains, instantiated in both single-agent and multi-agent configurations with embedded safety constraints. Evaluating ten harness configurations across frontier models and three multi-agent frameworks, we find that: (i) task completion is misaligned with safe execution, and violations accumulate with trajectory length; (ii) safety risks vary across domains, task types, and agent roles; (iii) most violations concentrate in resource access and inter-agent information transfer; and (iv) multi-agent collaboration expands the safety risk surface, while harness design sets the upper bound of safe deployment.

</details>

### 6. Quantifying Frontier LLM Capabilities for Container Sandbox Escape

📄 [arXiv](https://arxiv.org/abs/2603.02277) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66709)　📅 2026-03　🏷 ICML 2026

**关键词**：`benchmark`、`agent harness`、`runtime isolation`、`lifecycle security`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Rahul Marchand、…、Harry Coppock

- 🎯 **研究动机**：agent 普遍部署于 Docker/OCI 容器沙箱，但其逃逸沙箱的能力缺少安全测量手段
- 🔬 **研究方法**：SandboxEscapeBench 以 Inspect AI CTF 嵌套沙箱实现（外层含 flag 且无已知漏洞），覆盖配置错误、权限分配、内核缺陷与运行时编排弱点等逃逸机制
- 📌 **结论**：一旦注入漏洞，LLM 即可识别并利用，说明高能力模型时代需此类评测确保沙箱封装持续有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly act as autonomous agents, using tools to execute code, read and write files, and access networks, creating novel security risks. To mitigate these risks, agents are commonly deployed and evaluated in isolated "sandbox" environments, often implemented using Docker/OCI containers. We introduce SANDBOXESCAPEBENCH, an open benchmark that safely measures an LLM's capacity to break out of these sandboxes. The benchmark is implemented as an Inspect AI Capture the Flag (CTF) evaluation utilising a nested sandbox architecture with the outer layer containing the flag and no known vulnerabilities. Following a threat model of a motivated adversarial agent with shell access inside a container, SANDBOXESCAPEBENCH covers a spectrum of sandboxescape mechanisms spanning misconfiguration, privilege allocation mistakes, kernel flaws, and runtime/orchestration weaknesses. We find that, when vulnerabilities are added, LLMs are able to identify and exploit them, showing that use of evaluation like SANDBOXESCAPEBENCH is needed to ensure sandboxing continues to provide the encapsulation needed for highly-capable models.

</details>

### 7. AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes

📄 [arXiv](https://arxiv.org/abs/2609.00052)　📅 2026-09

**关键词**：`audit`、`API provenance`、`tool-use policy`、`model substitution`

👤 **作者**：Xun Wang、Bihe Zhao、Michael Backes、Franziska Boenisch、Adam Dziedzic

- 🎯 **研究动机**：商业 LLM API 可能静默替换、量化或包装所宣称模型，现有 text 通道审计在 agentic 服务栈只暴露结构化 action 时结构脆弱
- 🔬 **研究方法**：提出首个基于动作的身份审计 AgentProv：通过分类 tool-call 分布指纹化部署模型，用 MMD 置换检验判定同一性
- 📌 **结论**：630 对 checkpoint 上 100% 抓获替换模型，系统提示注入下 false positive 仅 7%（MET 67%、RUT 53%）；与 MET 的分歧和独立 token-count 侧信道一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs. All existing audits decide backbone identity from the text-output channel, which is structurally fragile for agentic APIs because modern serving stacks (OpenAI, Anthropic, Gemini, Cloudflare Workers AI, LangGraph) discard text and expose only structured actions when the model calls a tool, and provider-injected system prompts can distort text distributions enough that text-channel tests falsely accuse honest providers of substituting the claimed model. We observe that recent agentic post-training internalizes tool-use directly into the weights, opening a new audit channel that the serving stack still exposes and that is largely invariant to deployment context. We introduce Agentic Provenance (AgentProv), the first action-based identity audit for agentic LLM APIs: AgentProv fingerprints a deployed model through its categorical tool-call distribution and decides identity via an MMD permutation test. AgentProv catches every substituted model (100% on 630 evaluated checkpoint pairs), while holding the false-positive rate under system-prompt injection at 7% (vs. 67% for MET and 53% for RUT). On third-party API endpoints, AgentProv's disagreements with MET are consistent with an independent token-count side-channel that detects provider-injected system prompts.

</details>

### 8. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

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

### 9. When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

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

### 10. Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.11727)　📅 2026-08

**关键词**：`benchmark`、`instruction surface`、`against-prior rule`、`coding harness`

👤 **作者**：Zining Huang、…、Wenhao Huang

- 🎯 **研究动机**：现有指令跟随基准把规则集中在用户轮，无法区分真遵守规则与本来就会那么做
- 🔬 **研究方法**：Harness-IF 把规则逐条部署到 agent 读取的五个配置面（60 个多轮编码项、256 条规则），AP-Acc 只对与默认行为相反的规则计分
- 📌 **结论**：12 个前沿模型准确率 72.1-85.9%、AP-Acc 低 3.6-7.4 个百分点，聚合分数高估合规；优先级不随 prompt 深度走，系统提示与项目文件领先于工具描述

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a coding agent obeys a rule, it may simply have been going to do that anyway. Existing instruction-following benchmarks cannot tell the difference: they concentrate rules in the user turn, while coding-agent benchmarks emphasize final task success. We introduce Harness-IF, which scores operational rules one at a time from execution evidence: 60 realistic multi-turn coding items drawn from a 642-rule library, 256 rules receiving verdicts, placed on the five configurable surfaces a deployed agent reads. To separate compliance from coincidence we introduce Against-Prior Accuracy (AP-Acc), which scores only rules labeled as opposing unprompted defaults, observed by re-running tasks with the rule withheld across nine probe builds and curated otherwise. Across 12 frontier models, accuracy spans 72.1-85.9% and AP-Acc 66.1-78.6%; every model is worse on against-prior rules, by 3.6 to 7.4 points (mean 5.81), and the direction survives a common-support analysis with item-clustered intervals. Aggregate scores therefore overstate compliance by a model-specific margin: prior control leaves the top build unchanged and exchanges three adjacent rank pairs. A counterbalanced conflict pilot on nine separate builds adds a second result: pooled precedence does not follow prompt depth, with system prompts, project files, and user instructions ahead of tool and skill descriptions.

</details>

### 11. $A^2E$: An End-to-End Agent Auditing Engine

📄 [arXiv](https://arxiv.org/abs/2608.07346)　📅 2026-08

**关键词**：`tool`、`agent auditing`、`standardized trace`、`model-harness comparison`

👤 **作者**：Haoning Wang、…、Na Zou

- 🎯 **研究动机**：harness 生态快速演化，高效构建端到端系统化的 agent harness 评测管线仍困难
- 🔬 **研究方法**：A2E 用 Agent Task Protocol 快速接入评测任务，自动插桩 Monitor 生成标准化执行轨迹，多维指标刻画执行效率、工具使用、规划与错误恢复
- 📌 **结论**：模型-harness 组合在不同任务类型上表现差异巨大，没有组合全面占优，需系统化评测指导模型与 harness 共同演化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce $A^2E$ (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. $A^2E$ leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, $A^2E$ systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with $A^2E$ further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at https://github.com/datamllab/A2E.

</details>

### 12. Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

📄 [arXiv](https://arxiv.org/abs/2605.27922)　📅 2026-05

**关键词**：`benchmark`、`harness configuration`、`execution alignment`、`artifact validation`

👤 **作者**：Yilun Yao、…、Tong Yang

- 🎯 **研究动机**：agent 性能取决于 harness 层，而现有基准抽象掉执行、比较完整系统或固定 harness，配置级影响难研究
- 🔬 **研究方法**：Harness-Bench 含 106 个沙箱离线任务，在共享任务环境、预算与协议下保留各 harness 原生执行行为，记录产物、轨迹、用量与验证器输出，共 5,194 条轨迹
- 📌 **结论**：model-harness 配对在完成度、过程质量、效率与失败行为上差异巨大，agent 能力应按配置级报告；识别出推理与工具反馈、工作区状态脱节的 execution-alignment 失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are increasingly deployed as executable systems that use tools, modify workspaces, and produce concrete artifacts. In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context, tools, state, constraints, permissions, tracing, and recovery. However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study. We introduce Harness-Bench, a diagnostic benchmark for evaluating configuration-level harness effects in realistic agent workflows. Harness-Bench evaluates representative harness configurations across multiple model backends under shared task environments, budgets, and evaluation protocols, while preserving each harness's native execution behavior. The benchmark contains 106 sandboxed offline tasks constructed from practical agent-use patterns and manually reviewed for realism, solvability, oracle-checkability, and integrity. Each run records final artifacts, execution traces, usage statistics, and validator outputs, enabling analysis beyond final completion. Across 5,194 execution trajectories, we observe substantial variation in completion, process quality, efficiency, and failure behavior across model-harness pairings. These results suggest that agent capability should be reported at the model-harness configuration level rather than attributed to the base model alone. Our analysis further identifies recurring execution-alignment failures, where plausible reasoning becomes decoupled from tool feedback, workspace state, evidence, or verifiable output contracts. Harness-Bench provides a reproducible foundation for diagnosing and improving reliable, efficient, and auditable agent execution stacks.

</details>

### 13. Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.30041)　📅 2026-09

**关键词**：`defense`、`harness enforcement`、`capability reachability`、`inline reference monitor`、`skill-output contamination`、`capability restriction`

👤 **作者**：Wujie Xiong、Rabimba Karanjai、Yang Lu、Weidong Shi、Lei Xu

- 🎯 **研究动机**：不可信 skill 输出进入 Agent 状态后，现有防御只分类内容或授权操作，不改变 Agent 后续权限
- 🔬 **研究方法**：提出 harness 层 SkillGuard：以 Skill Impact Graph、steerability signature 与 inline reference monitor 把污染事件映射为加权 capability restriction（binary／fractional／fractional-flow）
- 📌 **结论**：AgentDojo Tool Knowledge 攻击下四个套件中三个 ASR 归零（Slack 降至 4.8%／14.3%），fractional-flow 同 ASR 下保留更多能力，且零额外模型调用与 token 开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents place outputs from external skills into their execution context, allowing attacker-controlled data to influence later privileged actions. Existing defenses mainly classify untrusted content or authorize proposed operations. They do not directly address how an agent's future authority should change once untrusted data enters its state. We present SkillGuard, a harness-level enforcement layer that treats this event as contamination and restricts future capabilities to disconnect the resulting state from deployer-defined forbidden states. Given sound skill summaries and policies, SkillGuard represents security-relevant transitions with a Skill Impact Graph, specifies admissible control over skill parameters via steerability signatures, and mediates invocations with an inline reference monitor. Following contamination, it computes weighted capability restrictions using binary, fractional, or fractional-flow strategies without auxiliary language-model inference. We evaluate SkillGuard on four AgentDojo suites with two backend LLMs, Gemini 2.5 Flash and Llama3.3-70B, against an LLM-only No Defense baseline and three defenses at different system layers: Spotlighting, CaMeL, and AttriGuard. We construct a compositional attack benchmark in which each attack combines observations individually insufficient to induce target violation and evaluate the same baselines on it. Under AgentDojo's Tool Knowledge attacks, SkillGuard eliminates attack success on three of four suites for both backends and reduces it to 4.8% and 14.3% on Slack. Against compositional attacks, it outperforms every baseline on Llama and matches the strongest baseline on Gemini at higher benign utility. Fractional-flow restriction preserves substantially more capabilities than binary restriction at the same attack success rate. Across both settings, SkillGuard adds no model calls or token overhead.

</details>

### 14. ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection

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

### 15. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

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

### 16. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

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

### 17. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

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

### 18. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

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

### 19. Beyond the Editing Canvas: Evidence Divergence in OOXML-to-LLM Ingestion

📄 [arXiv](https://arxiv.org/abs/2608.25880)　📅 2026-08

**关键词**：`analysis`、`attack`、`ingestion contract`、`evidence fork`、`extractor differential`、`OOXML ingestion`

👤 **作者**：Side Liu、Jiangpeng Liu、Jinwen Xin、Guojun Peng、Jiang Ming

- 🎯 **研究动机**：LLM 流水线把 OOXML 文档当一级证据，隐含假设 Office 画布所见与模型所取一致，该假设可被破坏
- 🔬 **研究方法**：遍历规范挖掘 21 类 evidence forks，用画布不可见的 task-relevant trap 测试 4 个原生 API 与 13 个提取工具
- 📌 **结论**：4 个 API 在 48%-76% 试验中返回 trap，13 个工具全部受至少一种机制影响，暴露由提取器配置决定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM pipelines increasingly ingest Office Open XML (OOXML) documents (Word, Excel, and PowerPoint files) as first-class evidence in financial, compliance, and retrieval-augmented workflows, implicitly assuming semantic integrity: that the evidence consumed by the model matches the content shown in the Microsoft Office suite editing canvas. We show that this assumption can fail in OOXML-to-LLM pipelines. The same specification-valid OOXML file can yield one evidentiary view in Microsoft Office and another when extracted for an LLM. Each view is treated as authoritative by its consumer, a condition we call plural ground truth. The ingestion contract rarely states which view and semantic roles become model evidence or preserves how that evidence was derived. We call the specification-grounded OOXML constructions that induce such divergence evidence forks. We systematically traverse and mine the OOXML specification and confirm 21 evidence forks across Excel, Word, and PowerPoint, spanning six dimensions of view construction. All 13 tools in our extraction panel emit evidence from at least one fork. We test four native-ingestion LLM APIs and seven web chatbots. Each test document carries a trap: a task-relevant fact exposed by extraction but not shown in Office. Across this 21-mechanism evaluation, the four APIs return the trap in 48--76% of trials. For 20 of 21 mechanisms, at least one of the eleven interfaces returns the trap. Our measurements further show that exposure is shaped upstream of the model by the ingestion path and extractor configuration. A source-level survey of sixteen popular open-source LLM projects further shows that default OOXML ingestion paths concentrate on affected extractor families.

</details>

### 20. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

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

### 21. HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

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

### 22. Agent Safety Should Be a Runtime Contract

📄 [arXiv](https://arxiv.org/abs/2608.11274)　📅 2026-08

**关键词**：`analysis`、`runtime contract`、`evidence chain`、`trajectory schema`

👤 **作者**：Albus W. Ng、Yi Han、Jusheng Zhang、Wenhao Wang

- 🎯 **研究动机**：主流范式把安全当作训练期经 RLHF/DPO 植入的属性，对会执行代码、改文件、发消息的自主 agent 结构性不足
- 🔬 **研究方法**：主张安全应为 harness 强制的运行时契约：预防面（沙箱、权限门、轨迹监控）加证据面（测试运行、日志、diff 等可验证证据），并形式化 Agent Trajectory Schema 与 Evidence Chain
- 📌 **结论**：四线证据支撑：52 起事故调查、31 例假完成审计、12 个 agent 系统轨迹审计与 28,560 篇顶会论文 8-12 倍训练期/部署期失衡；正确安全单元是带可查证据的轨迹而非模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The dominant paradigm treats AI safety as a property to be instilled during model training via RLHF, DPO, or Constitutional AI. We argue this is structurally insufficient for autonomous agents that execute code, mutate files, send messages, and modify databases. Agent safety should be a runtime contract enforced by the harness, and the contract has two complementary faces. The preventive face blocks dangerous actions before they happen via sandboxes, permission gates, output filters, and trajectory monitors. The evidential face requires verifiable proof that good actions actually happened, gating task submission on hard evidence such as test runs, log captures, file diffs, and citation grounding. We ground the position in four lines of public evidence, with row-level protocols and data released in the supplementary JSON files: a survey of 52 documented AI-agent and LLM safety incidents, a false-completion audit with 31 non-contested core cases plus one disputed illustrative case, a trajectory-schema audit of 12 public agent systems and harnesses, and a title-level audit of all 28,560 papers accepted at NeurIPS, ICML, and ICLR 2023-2025 showing a pooled 8-12x imbalance between training-time and deployment-time publication. Two prior communities that needed to enforce safety, computer security and the experimental sciences, converged on runtime contracts with both preventive and evidential elements; agentic AI is now under the same pressure. We formalize an Agent Trajectory Schema and Evidence Chain, state a compositional gating proposition based on standard monitor composition, and outline a research agenda. The right unit of safety in agentic AI is the trajectory-with-checkable-evidence, not the model.

</details>

### 23. Defeating Prompt Injections by Design

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

### 24. Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

📄 [arXiv](https://arxiv.org/abs/2609.01487)　📅 2026-09

**关键词**：`defense`、`harness runtime`、`task-conditioned guard`、`runtime evolution`、`runtime skill`、`task-conditioned policy`

👤 **作者**：Xiaofang Yang、Ziqi Miao、Dianbo Sui、Jing Shao、Lijun Li

- 🎯 **研究动机**：恶意 skill 只有在具体用户任务与工作区状态使不安全动作显得有用时才实施泄密或越权，安装前审查不足
- 🔬 **研究方法**：提出 Defense-as-Skill：把运行时护栏 SkillSonar 本身做成可安装、可检查、可编辑的 skill，对敏感动作按用户任务边界路由 allow／replan／confirm；构建 SCOPE-R 数据集并用 MCTS 的 guard-skill evolution 从 rollout 反馈进化护栏
- 📌 **结论**：跨 Claude Code 与 OpenClaw 大幅降低攻击且保持安全-效用平衡，GLM-5 重复运行中 ID ASR 从 0.482 降至 0.104、OOD 从 0.606 降至 0.115，并对自适应攻击者保持防护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skill-augmented agents load reusable skills as persistent runtime context, improving task performance but also giving malicious skills a durable channel for steering future actions. Such skills may leak secrets, corrupt code, bypass approvals, or stage data for exfiltration only after a concrete user task and workspace state make the unsafe action appear useful. This makes pre-install vetting insufficient and calls for runtime, task-conditioned protection. We propose Defense-as-Skill, a defense paradigm that implements the runtime guard itself as an installable, inspectable, and editable skill. Our guard, SkillSonar, runs alongside untrusted task skills and checks sensitive actions against the user's task boundary, routing each action to an allow, replan, or confirmation decision without modifying the underlying agent runtime. To study this setting, we construct SCOPE-R, a task-conditioned dataset covering 6 risk families and 21 sub-categories, with 206 attack-confirmed malicious instances and 43 benign tasks. We then improve SkillSonar on the SCOPE-R training subset using runtime guard-skill evolution, a Monte-Carlo Tree Search procedure that evolves the on-disk guard skill from feedback on the rollouts. Across Claude Code and OpenClaw, the evolved guard substantially reduces attack success while maintaining a favorable safety-utility trade-off. On repeated GLM-5 runs, SkillSonar reduces ID ASR from 0.482 to 0.104 and OOD ASR from 0.606 to 0.115. Further analyses demonstrate transfer across victim models, held-out risk families, and external benchmarks, as well as retained protection against adaptive attackers. Ablations further show that explicit safety responsibility assignment and the skill-native representation are both important to the observed gains.

</details>

### 25. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

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

### 26. CURA: Certified Runtime Alarms for Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2608.27808)　📅 2026-08

**关键词**：`detection`、`harness telemetry`、`sequential alarm`、`certified false alarm`、`computer-use agent`、`online failure alarm`

👤 **作者**：Divake Kumar、…、Amit Ranjan Trivedi

- 🎯 **研究动机**：computer-use Agent 的自我报告恰在最需要监督处失效：OSWorld 上 71 次失败中 64 次以成功声明结束，显式失败通道在约 9,100 次调用中几乎不用
- 🔬 **研究方法**：提出 CURA 外部监控器，只读 harness 可见遥测（无模型内部、无额外 LLM 调用、无 prompt 修改），把运行轨迹转为带认证假警报控制的 CUSUM 序贯检验
- 📌 **结论**：α=0.10 时以 0.066 实际假警报率、提前中位数 31 步检出 42.3% 失败，同等认证预算下在线召回 0.41 对 token 基线 0.34，级联中途监督挽回 70 次失败中的 23 次

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-report is the cheapest oversight channel a deployer has, and on capable computer-use agents (CUAs) it fails precisely where oversight matters. On 361 OSWorld tasks our pipeline, a read-only feasibility gate, a planner, and a GUI executor, reaches a mean task score of 82.9, above the 72.4 human reference, yet 64 of its 71 failures (90%) end with a success claim, 61 acknowledging no blocker, and the explicit failure affordance is never used in roughly 9,100 calls. We introduce CURA (Certified Runtime Alarms for Computer-Use Agents), an external monitor that reads only harness-visible telemetry, with no model internals, extra LLM calls, or prompt changes, and turns the running trajectory into a sequential test with certified false-alarm control. At alpha = 0.10 its CUSUM alarm detects 42.3% of failures a median of 31 steps before termination at a realized false-alarm rate of 0.066, and risk is partly resolvable before the first action (gate probe, 0.69 AUROC). Retrospectively the composite reaches 0.828 AUROC (fold-internal floor 0.802), but its margin over a total-token baseline is not significant (Delta = +0.026, p = 0.101); the separation is online, where CURA recalls more at matched certified budgets: 0.41 versus 0.34 at alpha = 0.10, 0.56 versus 0.38 at alpha = 0.20. Alarm-gated mid-execution oversight recovers 23 of 70 failures while spending a frontier overseer on 38, giving a deployable cascade at mean score 86.8 and 84.5% full-solve (305 of 361). The certificate bounds false alarms only. We also report where behavioral monitoring is uninformative.

</details>

### 27. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

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

### 28. SHE: Trajectory-driven Safety Harness Evolution for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.09885)　📅 2026-08

**关键词**：`defense`、`harness evolution`、`failure attribution`、`safety-utility validation`

👤 **作者**：Wanying Qu、…、Dongrui Liu

- 🎯 **研究动机**：agent 安全依赖 harness，但现有机制把 harness 当固定制品，组件耦合使安全责任难归因、难以局部演化
- 🔬 **研究方法**：SHE 把 harness 分解为 System Prompt、Rule Bank、Safety Memory、Tool Policy 四个责任明确工件，归因引导的演化循环把轨迹失败转为结构化诊断并经安全-效用验证选择演化版
- 📌 **结论**：Agent-SafetyBench 上 ASR 较静态 SafeHarness 降 3.1 倍且良性效用提升；演化 harness 泛化到 AgentHarm 未见风险并跨 agent 模型迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

</details>

### 29. Evo-Bench: Can Language Models Improve Agent Harness?

📄 [arXiv](https://arxiv.org/abs/2608.09096)　📅 2026-08

**关键词**：`benchmark`、`harness evolution`、`cross-suite generalization`、`iterative research`

👤 **作者**：Lisheng Huang、…、Tao Zhang

- 🎯 **研究动机**：agent 自主优化自身 harness 的能力缺乏能将其与基座模型实力隔离、防任务过拟合的基准
- 🔬 **研究方法**：Evo-Bench 用辅助任务演化识别对框架改进真正敏感的任务，再做敏感度感知分层切分保证跨套件泛化，覆盖 Search、Office、General 三域九模型
- 📌 **结论**：顶级模型绝对增益达 16.6 分接近人工设计基线；General 与 Search 域超越人工 harness、Office 域吃力，合成 harness 作为推理结构可迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operating harness. However, systematically benchmarking this capability remains challenging, as existing evaluations fail to isolate harness improvements from base model strength, prevent task-specific overfitting, or capture long-horizon iterative research. To address these challenges, we introduce Evo-Bench, the first benchmark designed to evaluate models' intrinsic harness-evolving capabilities across Search, Office, and General agent domains. To rigorously isolate this capability, Evo-Bench employs a novel harness-guided construction framework: it leverages auxiliary-task evolution to identify tasks genuinely sensitive to framework improvements, followed by sensitivity-aware stratified splitting to ensure robust cross-suite generalization. Extensive evaluations across nine frontier and open-weight models reveal that top models achieve massive absolute gains reaching 16.6 points, closely approaching state-of-the-art human-engineered baselines. Crucially, while autonomous evolution outpeforms artificial harness in General tasks and excels in Search tasks, it struggles in Office tasks that demand highly specific processing workflows. Furthermore, our analysis exposes critical temporal anomalies like early saturation, while demonstrating that the synthesized harnesses act as highly transferable reasoning structures, consistently boosting diverse policy models.

</details>

### 30. Code as Agent Harness

📄 [arXiv](https://arxiv.org/abs/2605.18747)　📅 2026-05

**关键词**：`survey`、`code harness`、`execution substrate`、`verifiable agent`

👤 **作者**：Xuying Ning、…、Jingrui He

- 🎯 **研究动机**：code 在 agent 系统中不再只是输出目标，而成为推理、行动、环境建模与执行验证的运行基底，缺乏统一视角
- 🔬 **研究方法**：综述按 harness 接口、机制（规划、记忆、工具使用、反馈驱动控制）与从单 agent 到多 agent 扩展三层组织相关方法与应用
- 📌 **结论**：提出 harness engineering 开放挑战：超越最终成功的评估、不完整反馈下的验证、无回归改进、共享状态一致性与高风险动作的人工监督

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure. To systematically study this perspective, we organize the survey around three connected layers. First, we study the harness interface, where code connects agents to reasoning, action, and environment modeling. Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon execution, together with feedback-driven control and optimization that make harness reliable and adaptive. Third, we discuss scaling the harness from single-agent systems to multi-agent settings, where shared code artifacts support multi-agent coordination, review, and verification. Across these layers, we summarize representative methods and practical applications of code as agent harness, spanning coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization and recommendation, DevOps, and enterprise workflows. We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments. By centering code as the harness of agentic AI, this survey provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

</details>

### 31. ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers

📄 [arXiv](https://arxiv.org/abs/2603.24414)　📅 2026-03

**关键词**：`defense`、`runtime watcher`、`skill policy`、`execution intervention`

👤 **作者**：Songyang Liu、…、Zhongyuan Wang

- 🎯 **研究动机**：OpenClaw 生态安全措施碎片化，只覆盖生命周期孤立阶段，模型错误可变为系统级威胁
- 🔬 **研究方法**：ClawKeeper 三层防护：skill 层注入结构化策略约束、plugin 层配置加固与行为监控、watcher 层解耦的系统级中间件持续验证状态并可实时干预或要求人工确认
- 📌 **结论**：定性与定量评估验证跨威胁场景的有效性，watcher 范式可作下一代自主 agent 安全的基础构件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

OpenClaw has rapidly established itself as a leading open-source autonomous agent runtime, offering powerful capabilities including tool integration, local file access, and shell command execution. However, these broad operational privileges introduce critical security vulnerabilities, transforming model errors into tangible system-level threats such as sensitive data leakage, privilege escalation, and malicious third-party skill execution. Existing security measures for the OpenClaw ecosystem remain highly fragmented, addressing only isolated stages of the agent lifecycle rather than providing holistic protection. To bridge this gap, we present ClawKeeper, a real-time security framework that integrates multi-dimensional protection mechanisms across three complementary architectural layers. (1) \textbf{Skill-based protection} operates at the instruction level, injecting structured security policies directly into the agent context to enforce environment-specific constraints and cross-platform boundaries. (2) \textbf{Plugin-based protection} serves as an internal runtime enforcer, providing configuration hardening, proactive threat detection, and continuous behavioral monitoring throughout the execution pipeline. (3) \textbf{Watcher-based protection} introduces a novel, decoupled system-level security middleware that continuously verifies agent state evolution. It enables real-time execution intervention without coupling to the agent's internal logic, supporting operations such as halting high-risk actions or enforcing human confirmation. We argue that this Watcher paradigm holds strong potential to serve as a foundational building block for securing next-generation autonomous agent systems. Extensive qualitative and quantitative evaluations demonstrate the effectiveness and robustness of ClawKeeper across diverse threat scenarios. We release our code.

</details>

### 32. A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors

📄 [arXiv](https://arxiv.org/abs/2609.03884)　📅 2026-09

**关键词**：`attack`、`harness hook`、`plugin supply chain`、`lifecycle execution`、`hook update`、`lifecycle payload`

👤 **作者**：Pengxun Li、…、Xi Zhang

- 🎯 **研究动机**：Agent harness 把生命周期 hook 配置（绑定 shell 命令到会话启动、工具调用等事件）当作可信更新，以宿主权限执行且可能在 LLM 不可见时触发
- 🔬 **研究方法**：在攻击者只控制插件元数据与 hook 配置的供应链威胁模型下提出 HookPry：自动化的更新路径攻击框架，静默把攻击者命令绑到良性事件实现提权等十类目标
- 📌 **结论**：25 种 harness-backend 组合、1,000 次端到端运行中攻陷全部七个受测 harness（单 harness 成功率最高 92.5%）；Microsoft Defender 召回 0%，三种静态防御的并集仍漏检 47.5% 恶意 artifact

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern AI agent harnesses expose lifecycle hooks that bind shell commands to runtime events such as session start, tool calls, and file edits. These commands run with host privileges yet ship as lifecycle-hook configuration and may fire at times the LLM never observes. We identify the lifecycle-hook update path, which harnesses trust blindly, as a new attack surface. Under a supply-chain threat model in which an attacker controls only plugin metadata and lifecycle-hook configuration, a benign versioned plugin can be trojanized by an update that silently binds attacker-chosen commands to benign events, yielding malicious host-side behavior such as privilege escalation. We propose HookPry, an open-source and fully automated attack framework that systematically exploits this vulnerability across heterogeneous AI agent harnesses. HookPry realizes ten attack objectives; across 25 combinations of harnesses and backends in 1,000 end-to-end runs, it compromises all seven evaluated harnesses, with per-harness success rates reaching 92.5%. Representative defenses remain insufficient: Microsoft Defender has 0% recall, and the union of three static defenses misses 47.5% of malicious artifacts.

</details>

### 33. What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness

📄 [arXiv](https://arxiv.org/abs/2609.01222)　📅 2026-09

**关键词**：`attack`、`context assembly`、`privilege escalation`、`cross-scope persistence`

👤 **作者**：Zichuan Li、Jian Cui、Ashley Chen、Xiaojing Liao、Luyi Xing

- 🎯 **研究动机**：真实 Agent harness 的上下文组装来源与权限逻辑不透明，由此产生的安全风险未被探索
- 🔬 **研究方法**：首次系统分析 12 个真实 harness 的上下文组装设计，提出两类攻击：低权限内容进入高权限消息角色的 M-CPE 与内容跨作用域持久化的 X-CPE
- 📌 **结论**：对包括 Claude Code 与 Codex 在内的 12 个 harness，后果涵盖完整 Agent 接管、远程代码执行、拒绝服务与工具／skill 调用操纵

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of practical attack vectors arising from these designs. Our analysis brings to light two novel categories of attacks in the context assembly of real-world harnesses: (1) MessageRole Context Privilege Escalation (M-CPE), which occurs when attacker-controlled content originating from a low-privileged context is incorporated into a higher-privileged message role. (2) Cross-Scope Context Privilege Escalation (X-CPE), which occurs when attacker-controlled content persists beyond the context in which it was introduced. We performed a systemic security analysis of the CPE attacks against 12 real-world agent harnesses, including Claude Code and Codex. The resulting consequences include full agent compromise, remote code execution, denial of service, and manipulated tool or skill invocations, etc.

</details>

### 34. ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

📄 [arXiv](https://arxiv.org/abs/2608.27800)　📅 2026-08

**关键词**：`attack`、`runtime context`、`malicious tool`、`parameter exfiltration`、`malicious tool metadata`、`context exfiltration`

👤 **作者**：Yuqi Jia、Ruiqi Wang、Patrick Li、Yuepeng Hu、Peinian Li、Neil Gong

- 🎯 **研究动机**：恶意工具外泄 Agent 运行时上下文需同时满足工具被选中、上下文作为参数传入、结果外传三条件，已有工作聚焦条件 1 与 3，条件 2 未被探索
- 🔬 **研究方法**：提出 ContextLeak，用攻击 LLM 生成恶意工具的名称与描述，并在多样模拟上下文的 shadow user 上以 RL 微调攻击 LLM，配合新奖励函数诱导 Agent 选择工具并把上下文写入参数
- 📌 **结论**：攻击在 shadow 与受害用户上下文差异显著时仍高效，显著优于改造后的既有攻击，可外泄用户 prompt、执行轨迹与工具列表

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: (1) the agent selects the malicious tool for task execution, (2) the agent passes its runtime context as input arguments to the tool, and (3) the tool's implementation transmits these inputs to an attacker-controlled endpoint. Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration. In this work, we bridge this gap by developing ContextLeak, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

</details>

### 35. When Context Gets Root: Privilege Escalation in LLM Harnesses

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

### 36. Beyond Direct Access: Resource Hijacking in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.15108)　📅 2026-08

**关键词**：`attack`、`agent harness`、`runtime isolation`、`lifecycle security`

👤 **作者**：Puyu Zeng、Qibing Ren

- 🎯 **研究动机**：agent 可达的高价值资源（算力、凭据、预算、身份、私有知识、信道）作为直接攻击目标被忽视
- 🔬 **研究方法**：首次系统研究 agent 资源劫击：六类资源、300 个场景 900 条攻击 prompt，隔离本地环境记录真实资源使用而非只看文本回应
- 📌 **结论**：无防御时 OpenClaw 平均 ASR 84.06%，跨模型后端 69.98%-89.58%；最强现有防御仍留 55.11% 平均 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents are increasingly connected to high-value resources such as computing infrastructure, credentials, usage budgets, identities, private knowledge, communication channels, and organizational workflows. Existing agent security research mainly studies attacks on instructions, data, and tool behaviors, while high-value resources accessible to agents have received much less attention as direct attack targets. We are the first to identify and systematically study agent resource hijacking, a security blind spot in which attackers induce agents to invoke, consume, transfer, or control high-value resources for their own goals without directly obtaining those resources or their credentials. To study this threat, we introduce ResourceHijackBench together with an automated pipeline for generating resource hijacking cases. We organize high-value agent resources into six categories and construct 300 attack scenarios with 900 attack prompts. Each case runs in an isolated local environment that records actual resource use, allowing attacks to be evaluated from agent behavior rather than text responses alone. Without additional defenses, OpenClaw reaches an average attack success rate of 84.06%. The attack remains effective across different model backends, with average success rates ranging from 69.98% to 89.58%. Existing defenses reduce part of the risk, but the strongest evaluated defense still leaves an average attack success rate of 55.11%. These results show that high-value resources accessible to agents form an important and previously overlooked attack surface, and that current agent defenses are not sufficient to protect them from resource hijacking.

</details>

### 37. When Compression Becomes an Attack Surface: Black-Box Attacks on Prompt-Compressed LLM Agents

📄 [arXiv](https://arxiv.org/abs/2510.22963) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/64/When-Compression-Becomes-an-Attack-Surface-Black-Box-Attacks-on-Prompt-Compressed-LL)　📅 2025-10　🏷 ASE 2026

**关键词**：`attack`、`prompt compression`、`adversarial information loss`、`agent pipeline`

👤 **作者**：Zesen Liu、Zhixiang Zhang、Yuchong Xie、Dongdong She

- 🎯 **研究动机**：可信与不可信输入共享压缩预算时，有损 prompt 压缩本身成为未被发现的新攻击面
- 🔬 **研究方法**：形式化 adversarial information loss（AIL），提出 COMA 迁移式黑盒攻击，用攻击方代理压缩器与后端 LLM 优化压缩前扰动，诱使压缩器丢弃任务关键证据或安全护栏
- 📌 **结论**：三任务六压缩器上平均 ASR 达 0.71（最强基线 0.21），并成功迁移到两个真实 agent 案例

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt compression is increasingly deployed in LLM agents to reduce latency and cost, but it also determines what the backend LLM ultimately sees. We show that, when trusted and untrusted inputs are compressed under a shared budget, this lossy transformation creates a new attack surface: by perturbing only untrusted inputs before compression, an adversary can cause the compressor to discard task-critical evidence or safety guardrails before inference. Unlike prompt injection, jailbreaks, or RAG poisoning, the attack target is the compressor rather than the backend LLM; the perturbation need not encode a meaningful instruction or survive compression. We formalize this vulnerability as adversarial information loss (AIL), the excess downstream distortion caused by adversarially steering a lossy compressor beyond benign compression alone. To exploit AIL, we present COMA, a transfer-based black-box attack that optimizes pre-compression perturbations using attacker-side surrogate compressors and backend LLMs. Across three tasks and six compressors, COMA achieves 0.71 average ASR, versus 0.21 for the strongest baseline, and transfers to two real-world agent case studies.

</details>

### 38. Mind the Web: The Security of Web Use Agents

📄 [arXiv](https://arxiv.org/abs/2506.07153) · 🌐 [Project](https://doi.org/10.1145/3779208.3805968)　📅 2025-06　🏷 ACM CCS 2026

**关键词**：`attack`、`browser harness`、`inherited privilege`、`execution constraint`、`web-use agent`、`indirect prompt injection`

👤 **作者**：Avishag Shapira、Parth Atulbhai Gandhi、Edan Habler、Asaf Shabtai

- 🎯 **研究动机**：web-use agent 的广泛浏览器能力带来未被探索的攻击面，网页中的恶意内容可劫持任务执行
- 🔬 **研究方法**：提出 task-aligned injection 把恶意指令伪装成任务引导，构建三阶段自动管线训练注入生成器，按 CIA 三元组组织载荷
- 📌 **结论**：五个 agent 上 ASR 超 80% 且跨载荷、环境与底层 LLM 强迁移，仅需在公开网站发帖即可攻破含内置安全机制的 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-use agents are rapidly being deployed to automate complex web tasks with extensive browser capabilities. However, these capabilities create a critical and previously unexplored attack surface. This paper demonstrates how attackers can exploit web-use agents by embedding malicious content in web pages, such as comments, reviews, or advertisements, that agents encounter during legitimate browsing tasks. We introduce the task-aligned injection technique that frames malicious commands as helpful task guidance rather than obvious attacks, exploiting fundamental limitations in LLMs' contextual reasoning. Agents struggle to maintain coherent contextual awareness and fail to detect when seemingly helpful web content contains steering attempts that deviate them from their original task goal. To scale this attack, we developed an automated three-stage pipeline that generates effective injections without manual annotation or costly online agent interactions during training, remaining efficient even with limited training data. This pipeline produces a generator model that we evaluate on five popular agents using payloads organized by the Confidentiality-Integrity-Availability (CIA) security triad, including unauthorized camera activation, file exfiltration, user impersonation, phishing, and denial-of-service. This generator achieves over 80% attack success rate (ASR) with strong transferability across unseen payloads, diverse web environments, and different underlying LLMs. This attack succeed even against agents with built-in safety mechanisms, requiring only the ability to post content on public websites. To address this risk, we propose comprehensive mitigation strategies including oversight mechanisms, execution constraints, and task-aware reasoning techniques.

</details>

### 39. A Programming Paradigm for Spatiotemporal Composability

📄 [arXiv](https://arxiv.org/abs/2608.25512)　📅 2026-08

**关键词**：`analysis`、`spatiotemporal composability`、`revertible effect`、`agent harness`

👤 **作者**：Yifan Shi、Wei Zhang、Tianyi Cui

- 🎯 **研究动机**：插件化自进化agent harness动态装卸组件后副作用难回滚、依赖难同步
- 🔬 **研究方法**：形式化revertible effect与reactive coeffect并实现Cordis演算
- 📌 **结论**：将时空可组合性从单组件扩展到交错执行的完整系统

### 40. AIR: Improving Agent Safety through Incident Response

📄 [arXiv](https://arxiv.org/abs/2602.11749) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62353)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`agent safety`、`agent harness`、`runtime isolation`、`mechanistic analysis`、`failure recovery`

👤 **作者**：Zibo Xiao、Jun Sun、Junjie Chen

- 🎯 **研究动机**：现有 LLM agent 安全机制几乎只做事前预防，缺乏事后响应、遏制与恢复能力
- 🔬 **研究方法**：AIR 首个 agent 事件响应框架：定义领域语言管理事件响应生命周期并集成进执行循环，经语义检查检测事故、引导遏制与恢复动作、在根除阶段合成 guardrail 规则
- 📌 **结论**：三类 agent 上检测、修复与根除成功率均超 90%；LLM 生成的规则接近开发者手写规则的效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents are increasingly deployed in practice across a wide range of autonomous applications. Yet current safety mechanisms for LLM agents focus almost exclusively on preventing failures in advance, providing limited capabilities for responding to, containing, or recovering from incidents after they inevitably arise. In this work, we introduce AIR, the first incident response framework for LLM agent systems. AIR defines a domain-specific language for managing the incident response lifecycle autonomously in LLM agent systems, and integrates it into the agent's execution loop to (1) detect incidents via semantic checks grounded in the current environment state and recent context, (2) guide the agent to execute containment and recovery actions via its tools, and (3) synthesize guardrail rules during eradication to block similar incidents in future executions. We evaluate AIR on three representative agent types. Results show that AIR achieves detection, remediation, and eradication success rates all exceeding 90%. Extensive experiments further confirm the necessity of AIR's key design components, show the timeliness and moderate overhead of AIR, and demonstrate that LLM-generated rules can approach the effectiveness of developer-authored rules across domains. These results show that incident response is both feasible and essential as a first-class mechanism for improving agent safety.

</details>