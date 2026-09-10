# Memory 与 Self-Evolving Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 Agent 的 memory、model、tool、workflow 与 architecture 会随交互持续更新时产生的安全和隐私问题。与普通 RAG 不同，self-evolving Agent 可以把 observation、reasoning、成功轨迹或生成代码 commit 为未来默认行为，使短暂错误转化为 semantic drift、misevolution、跨 session 泄漏或 lineage-persistent compromise。核心控制点是 propose、evaluate、commit、serve 之间的 provenance、隔离、验证、回滚和遗忘。

## 研究脉络

- **Memory 作为示例库：** 早期攻击从 query-only interaction 写入恶意 demonstration 或抽取历史私密记录，建立 read/write trust boundary。
- **动态巩固与反馈环：** 被污染输出会再次保存为经验，形成 self-reinforcing error；防御开始使用 consensus、dual memory、decay 和 write-time validation。
- **Misevolution：** 风险从 memory 扩展到 model、tool 和 workflow，自主改进可能降低 alignment、引入新漏洞或放大错误策略。
- **生命周期与 lineage：** 新框架按 module 与 bootstrap/propose/evaluate/commit/serve 交叉分析，强调攻击在多代演化中永久编码和传播。
- **当前边界：** 需要能验证 update utility 与 safety、保留 provenance、支持 selective rollback/forgetting 的演化治理，而不能让同一个 Agent 同时提出、评估和批准自身更新。

## Self-Evolution 风险与系统分析

### 1. Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops

📄 [arXiv](https://arxiv.org/abs/2609.00077)　📅 2026-09

**关键词**：`analysis`、`autonomous research loop`、`mode collapse`、`evaluator gaming`

👤 **作者**：Bowei He、Weixu Zhang、Yili Jin、Xue Liu

- 🎯 **研究动机**：代码级 autonomous research loop 依赖可执行 in-loop metric 保留编辑，但是否带来泛化的真实改进不清楚
- 🔬 **研究方法**：识别 algorithmic mode collapse（表面编辑多样性稳定而语义与机制多样性塌缩），提出三层指标协议与 DAPS（类别覆盖重加权、持久编辑记忆、验证门）
- 📌 **结论**：DAPS 把编辑语义簇衰减降低 69.1%，blind／audited relative faithfulness 分别提升 83.7%／81.6%，同时保持 in-loop 优化速度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code-level autonomous research loops (ARLs) have recently emerged as a concrete object of study in automated machine learning research. In such loops, an LLM agent proposes modifications to an experimental training pipeline, executes the modified pipeline, and retains edits that improve a verifiable in-loop metric. Although executable metrics may appear to provide a reliable signal of progress, it remains unclear whether repeated metric-driven code editing leads to genuine improvements that generalize beyond the loop. We provide a systematic diagnosis of this question. Across various experiment settings, we identify a robust failure mode that we call \textbf{algorithmic mode collapse}. In this regime, surface-level edit diversity remains stable, but semantic and mechanism-level diversity collapse: the agent continues to edit different lines of code while repeatedly proposing the same kinds of algorithmic changes. This collapse is accompanied by a widening gap between in-loop metric gains and gains measured on independent held-out evaluations. We then propose Diversity-Aware Proposal Sampling (\textsc{DAPS}), a lightweight mitigation that combines category-coverage reweighting, persistent edit memory, and a validation gate. Under a three-tier protocol separating the in-loop metric, the audit metric read by the gate, and a blind metric no loop component ever accesses, \textsc{DAPS} reduces semantic-cluster decay of edits by $69.1\%$ and improves relative faithfulness by $83.7\%$ blind and $81.6\%$ audited, while preserving in-loop optimization speed. We provide the code in Github \href{https://github.com/BokwaiHo/arl-mode-collapse}{repository}.

</details>

### 2. Safin-1: Safety from Within through Memory-Native State Evolution

📄 [arXiv](https://arxiv.org/abs/2609.00092)　📅 2026-09

**关键词**：`architecture`、`memory-native safety`、`state evolution`、`test-time adaptation`

👤 **作者**：Ming Zhang、…、Chaochao Lu

- 🎯 **研究动机**：长程任务中安全过度依赖外部 safeguard 与事后对齐，难以作为模型内生属性保持
- 🔬 **研究方法**：提出基于 MARCH 记忆锚定路由与状态演化的 Safin-1 模型族，经 Safety State 接口在测试时适配持久能力状态而无需改动 backbone
- 📌 **结论**：Safety State 带来显著安全提升，routed-state 接口统一上下文记忆与持久能力适应；作者明确这只是 Safety from Within 的初步架构探索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning. This motivates Safety from Within, where safety-relevant capabilities are represented and invoked through the model's native computation. We present Safin-1, a family of foundation models realizing this principle through memory routing and state evolution. Safin-1 is built on Memory-Anchor Routing across Context History (MARCH), a network architecture that maintains structured memory states and selectively retrieves relevant historical information through content-conditioned routing. It supports test-time adaptation of persistent capability states without repeatedly modifying the backbone, enabling controlled specialization over a shared foundation. We investigate this interface on downstream safety tasks through a Safety State, demonstrating effective state-based adaptation with substantial safety improvements. More broadly, the routed-state interface unifies contextual memory and persistent capability adaptation within the model's native computation, reframing memory from a passive record of prior context into an active substrate for maintaining and evolving model behavior. Evaluations across general capabilities, long-context understanding, retrieval, and efficiency further validate Safin-1. These findings provide a path toward safety as a state-native and adaptively maintainable capability. This work is only an initial architectural exploration of Safety from Within, and substantial further work is needed to realize this broader vision.

</details>

### 3. EVOMAL: Self-Poisoning in Self-Evolving Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.25776)　📅 2026-08

**关键词**：`attack`、`coding agent`、`self-authored tool`、`skill worm`、`self-evolving agent`、`skill imitation`

👤 **作者**：Xiaodong Wu、…、Jianbing Ni

- 🎯 **研究动机**：自演化 coding Agent 模仿共享库编写工具时，检索到的恶意 skill 会成为保留 payload 的新模板（self-poisoning）
- 🔬 **研究方法**：EvoMal 用良性外观 banner 包裹可替换 payload 诱导模仿复制，作者化的恶意 skill 回流入库形成自我传播蠕虫，以 ASPR 度量
- 📌 **结论**：六模型 153 个 SWE-bench 任务上 ASPR 达 20.3%-41.8%，库中恶意 skill 为植入的 4.9-9.0 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving LLM coding agents write their own tools by imitating retrieved skills from shared skill libraries. We identify a vulnerability in this loop: during authoring, a retrieved malicious skill can become the template for a new skill that preserves the payload. We call this self-poisoning: the agent authors, stores, and runs the resulting malicious skill. We exploit it through EvoMal, an attack that amplifies self-poisoning by wrapping an interchangeable payload in a banner, a set of benign-looking structural elements that induces an imitating agent to reproduce the enclosed code. The attacker plants malicious skills in the library without invoking them. The agent then authors and executes new skills carrying the harmful code. Each authored copy can re-enter the library and be imitated again, forming a self-propagating worm that persists after the planted skills are removed. We define the agent self-poisoning rate (ASPR) as the fraction of tasks that add a newly authored malicious skill to the library. Across six models on 153 tool-relevant SWE-bench Verified tasks, ASPR ranges from 20.3% to 41.8%, and the poisoned libraries hold 4.9 to 9.0 times as many malicious skills as were planted. The vulnerability also appears without a banner: DeepSeek-V4-Pro reaches 11.1% ASPR with the payload alone. Tailoring the planted skill descriptions to one task family raises ASPR to 86.7%. After the planted skills are removed, Qwen3 retains a round-5 ASPR of 68% because agent-authored copies remain. These copies evade existing defenses, which focus on attacker-submitted names, code, and signatures. We propose counter-prompt, a defense that discourages banner-style copying and reduces EvoMal's ASPR to at most 6.7% with no significant task-completion loss.

</details>

### 4. Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.12851)　📅 2026-08

**关键词**：`analysis`、`agent memory`、`self-evolution`、`cross-session risk`、`skill misevolution`、`malicious exposure`

👤 **作者**：Xutao Mao、Liangjie Zhao、Xiang Zheng、Cong Wang

- 🎯 **研究动机**：自改进 agent 会把不安全成功蒸馏为持久跨任务策略，风险跨越创作、检索与后续执行的生命周期无法归因
- 🔬 **研究方法**：SkillMisevo-Gym 版本化技能状态，SkillMisevo-Bench 从恶意暴露到迁移任务含九项生命周期指标；SafeEvolve 包装器修复不安全内容并治理复用
- 📌 **结论**：21 个演化配置全部产出不安全工件但仅 15 个致新会话伤害；三个恶意任务把迁移 ASR 从 16.0% 抬至 35.3%，SafeEvolve 降不安全检索与新鲜会话伤害 26.7/17.3 个百分点而良性效用仅变 0.4

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or static artifacts but cannot attribute risk across authoring, retrieval, and later execution. To expose this lifecycle, we introduce SkillMisevo-Gym, a lifecycle-aware harness that versions skill state across agent frameworks, and SkillMisevo-Bench, a frozen design from malicious exposure to carryover tasks, with concept-aligned benign tasks and nine lifecycle metrics. We also introduce SafeEvolve, a wrapper that repairs unsafe content and governs subsequent reuse. Across 25 agent-method configurations, each covering 525 tasks in 25 episodes, all 21 evolved configurations author unsafe artifacts, while only fifteen lead to fresh-session harm. In the exposure sweep, three malicious tasks raise carryover ASR from 16.0% to 35.3%. Across representative skill evolution methods, SafeEvolve reduces unsafe retrieval and fresh-session harm by 26.7 and 17.3 percentage points, respectively, while mean benign utility changes by only 0.4 points. Together, persistent-adaptation safety must govern what updates write and what future executors reuse. Code is available at https://github.com/henrymao2004/misevolve.

</details>

### 5. Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies

📄 [arXiv](https://arxiv.org/abs/2606.23075)　📅 2026-06

**关键词**：`analysis`、`self-evolving agent`、`MLAS matrix`、`lineage persistence`

👤 **作者**：Ruixiao Lin、…、Shouling Ji

- 🎯 **研究动机**：自进化 agent 自主更新参数、记忆、工具与架构，使对抗影响永久编码、跨代自放大并在群体传播，威胁图谱未被系统化
- 🔬 **研究方法**：提出 Module-Lifecycle Attack Surface（MLAS）矩阵：5 功能模块 x 5 生命周期阶段共 25 格分析，识别七类跨切放大效应并对两个开源框架做案例研究
- 📌 **结论**：17 格面临无有效缓解的关键威胁；进化原生设计激活 3.5 倍攻击面、攻击持久率 100%（40/40），共存安全扫描器仅拦截 2.5%，静态防御结构性不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). Analysis of the resulting 25 cells reveals that 17 face critical threats for which no effective partial mitigation. We identify seven cross-cutting amplification effects that interact synergistically and cannot be addressed by securing individual modules in isolation. Comparative case studies of two open-source frameworks demonstrate that evolution-native design activates $3.5\times$ more attack surface cells and achieves a 100% attack persistence rate (40/40 payloads across all CIA+Privacy categories), while co-located security scanners block only 2.5% of attacks. Our findings establish that self-evolution converts every known attack category from session-bounded to lineage-persistent, gives rise to entirely new attack classes, and renders static defenses structurally inadequate, motivating evolution-aware security frameworks and formal verification for self-modifying systems.

</details>

### 6. Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents

📄 [arXiv](https://arxiv.org/abs/2509.26354) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010580)　📅 2025-09　🏷 ICLR 2026

**关键词**：`analysis`、`misevolution`、`memory accumulation`、`tool creation`

👤 **作者**：Shuai Shao、…、Jing Shao

- 🎯 **研究动机**：自进化 agent 的演化偏离预期导致有害结果的风险被现有安全研究忽视
- 🔬 **研究方法**：沿模型、记忆、工具、工作流四条演化路径系统评估 misevolution 现象
- 📌 **结论**：风险普遍存在，连 Gemini-2.5-Pro 驱动的 agent 也不例外：记忆累积后安全对齐退化，工具创建与复用引入漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in Large Language Models (LLMs) have enabled a new class of self-evolving agents that autonomously improve through interaction with the environment, demonstrating strong capabilities. However, self-evolution also introduces novel risks overlooked by current safety research. In this work, we study the case where an agent's self-evolution deviates in unintended ways, leading to undesirable or even harmful outcomes. We refer to this as Misevolution. To provide a systematic investigation, we evaluate misevolution along four key evolutionary pathways: model, memory, tool, and workflow. Our empirical findings reveal that misevolution is a widespread risk, affecting agents built even on top-tier LLMs (e.g., Gemini-2.5-Pro). Different emergent risks are observed in the self-evolutionary process, such as the degradation of safety alignment after memory accumulation, or the unintended introduction of vulnerabilities in tool creation and reuse. To our knowledge, this is the first study to systematically conceptualize misevolution and provide empirical evidence of its occurrence, highlighting an urgent need for new safety paradigms for self-evolving agents. Finally, we discuss potential mitigation strategies to inspire further research on building safer and more trustworthy self-evolving agents. Our code and data are available at https://github.com/ShaoShuai0605/Misevolution . Warning: this paper includes examples that may be offensive or harmful in nature.

</details>

### 7. Inferring Hidden User Models from the Behavior of Personalized LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.03815)　📅 2026-09

**关键词**：`attack`、`personalized memory`、`user-model inference`、`behavioral side channel`、`personalized agent`、`user-model extraction`

👤 **作者**：Haoyang Li、Yaxin Xiao、Qingqing Ye、Huadi Zheng、Haibo Hu

- 🎯 **研究动机**：个性化 Agent 把记忆压缩为 user model 后，直接记忆提取攻击失效被当作更隐私，但被塑造的可见选择仍泄露私有信息
- 🔬 **研究方法**：提出黑盒攻击 UMPeek：从请求留下的开放选择形成假设、在普通后续任务间切换、只保留被可见行为支持且未被反驳的断言
- 📌 **结论**：在 benchmark 与真实系统上均超过现有攻击，response 级防御下仍能恢复用户信息——记录与后端不可访问不保证语义隐私

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent personalized LLM agents increasingly transform information retained in memory into compressed or structured representations, which we call user models, to guide later decisions. When source wording is removed from the state reachable through the ordinary interface, these models are commonly treated as more privacy-preserving because direct memory-extraction attacks lose the text they target. Yet we argue that user models expose a new attack surface because an attacker can still recover the private information from the personalized choices they shape, even when source records and backend state remain inaccessible. We therefore introduce UMPeek, a black-box attack based on hypothesis-guided adaptive probing to infer such hidden user model. It forms hypotheses from choices left open by a request, switches among ordinary follow-up tasks, and retains only claims supported and not contradicted by visible behavior. We conduct an extensive benchmark evaluation across diverse personalization tasks and user-model backends against existing attacks. We further validate UMPeek in real-world systems using information confirmed to be retained, and we evaluate defenses against its adaptive probing. Overall, UMPeek outperforms existing attacks in both benchmark and real-world comparisons and continues to recover user information under response-level defenses, showing that keeping records and backend state inaccessible does not guarantee semantic privacy when retained information shapes visible behavior.

</details>

### 8. Inadvertent Context Leakage in Language Models

📄 [arXiv](https://arxiv.org/abs/2608.19857)　📅 2026-08

**关键词**：`attack`、`analysis`、`private agent context`、`memory predicate inference`、`adaptive extraction`、`linguistic steganography`

👤 **作者**：Jaiden Fairoze、Neal Mangaokar、Kamalika Chaudhuri、Sanjam Garg、Saeed Mahloujifar

- 🎯 **研究动机**：agent 上下文中的敏感秘密（日历、凭据、健康、金融）是否在良性输出中留下可重建的隐藏相关性未知
- 🔬 **研究方法**：研究被动泄漏与主动放大两种情形，用黑盒自适应攻击（含语义谓词分类器与 RL 训练对手）利用该有限泄漏
- 📌 **结论**：八个专有模型上 2 位上下文秘密近完美重建、4 位达 82% 精确匹配（全部来自普通非对抗请求）；更强模型泄漏更多——RL 对手可从生产式 agent 提取完整社会安全号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>

### 9. InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

📄 [arXiv](https://arxiv.org/abs/2608.23471) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers) · 📝 [OpenReview](https://openreview.net/forum?id=QVX6hcJ2um)　📅 2026-08

**关键词**：`attack`、`agent memory`、`memory injection`、`persistent tool hijacking`、`persistent memory`、`single-interaction injection`

👤 **作者**：Hanling Tian、…、Xiaolin Huang

- 🎯 **研究动机**：记忆正成为部署 LLM agent 的默认子系统，无需读写 memory store 的单次交互能否留下持久漏洞未知
- 🔬 **研究方法**：InjecMEM 记忆注入：按检索-生成机制构造检索器无关 anchor（高召回主题线索保证命中目标主题）加对抗命令（梯度坐标搜索优化，在融合上下文、变位置与长 prompt 下保持有效并跨骨干迁移）
- 📌 **结论**：多个记忆系统与骨干模型上实现可靠主题条件检索与定向生成，记忆漂移下仍有效且不影响非目标查询——记忆子系统亟需加固

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a retriever-agnostic anchor and an adversarial command. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

</details>

### 10. MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds

📄 [arXiv](https://arxiv.org/abs/2608.22061)　📅 2026-08

**关键词**：`attack`、`persistent memory`、`external-content ingestion`、`behavior steering`、`indirect prompt injection`、`external feed`

👤 **作者**：Minjae Seo、…、Myoungsung You

- 🎯 **研究动机**：personal agent 常规摄取网页、邮件与 SNS feed 并将选中内容写入持久记忆，这条普通摄取路径可在不接触 agent、记忆或未来查询时间接操纵后续行为
- 🔬 **研究方法**：IBIA 间接偏见注入组合 comment cloaking（伪装成语境一致的评论）、comment watermarking（策展时轻量识别）与 category anchoring（让立场后续显著）；构建 BiasBench（6,000 条对抗评论+120 封邮件）
- 📌 **结论**：水印策展识别 95.9% 注入评论；OpenClaw 下四个下游任务平均对手立场响应率 91.2%（GPT-5.5 上 86.6%），memory boundary 防御仅将其降至 80.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic into a victim agent's memory through external content, without direct access to the agent, its memory, or future user queries. For this, IBIA combines three mechanisms: comment cloaking, which keeps the crafted content consistent with the surrounding discussion, comment watermarking, which enables lightweight identification during curation, and category anchoring, which makes the retained stance salient under later related requests. We evaluate IBIA on BiasBench, a benchmark of 6,000 adversary-crafted social comments and 120 email instances. The watermark-based curation identifies 95.9% of the injected comments. Under the OpenClaw setting, IBIA achieves adversary-aligned response rates (AARs) of 91.2% on average across four downstream tasks, including 86.6% on the frontier GPT-5.5. We further propose a memory boundary defense that detects the injected bias and reduces AARs to 80.6%.

</details>

### 11. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

📄 [arXiv](https://arxiv.org/abs/2607.05029)　📅 2026-07

**关键词**：`attack`、`reasoning memory`、`self-reinforcement`、`forgery detection`、`FARMA`、`forged rationale`

👤 **作者**：Neeraj Karamchandani、Piyush Nagasubramaniam、Sencun Zhu、Dinghao Wu

- 🎯 **研究动机**：agent 的推理历史本身是新攻击面：毒化被记忆的推理而非事实知识此前未被研究
- 🔬 **研究方法**：提出 FARMA：插入用规避性语言绕过关键词防御的伪造推理轨迹，再经自引用强化击败基于共识的防御；配套 SENTINEL 分层防御用五个加权信号做结构化伪造分析
- 📌 **结论**：FARMA 基线条件下 ASR 最高 100%，击败关键词过滤与 A-MemGuard；SENTINEL 把 ASR 降到最低 0% 且 326 条良性轨迹零误报

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

</details>

### 12. Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution

📄 [arXiv](https://arxiv.org/abs/2603.23064)　📅 2026-03

**关键词**：`attack`、`background execution`、`memory pollution`、`cross-session influence`

👤 **作者**：Yechao Zhang、…、Tianwei Zhang

- 🎯 **研究动机**：Claw 心跳后台执行与前台对话共享 session，外部内容可无声进入同一记忆上下文且用户无感
- 🔬 **研究方法**：形式化 Exposure-Memory-Behavior 路径，在 Moltbook 复刻的 MissClaw 社交环境中测试普通误导内容，无需任何 prompt injection
- 📌 **结论**：社交共识线索误导率最高 61%；常规记忆保存使 91% 的短期污染固化为长期记忆，跨 session 行为影响达 76%，内容稀释下仍能跨会话

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We identify a critical security vulnerability in mainstream Claw personal AI agents: untrusted content encountered during heartbeat-driven background execution can silently pollute agent memory and subsequently influence user-facing behavior without the user's awareness. This vulnerability arises from an architectural design shared across the Claw ecosystem: heartbeat background execution runs in the same session as user-facing conversation, so content ingested from any external source monitored in the background (including email, message channels, news feeds, code repositories, and social platforms) can enter the same memory context used for foreground interaction, often with limited user visibility and without clear source provenance. We formalize this process as an Exposure (E) $\rightarrow$ Memory (M) $\rightarrow$ Behavior (B) pathway: misinformation encountered during heartbeat execution enters the agent's short-term session context, potentially gets written into long-term memory, and later shapes downstream user-facing behavior. We instantiate this pathway in an agent-native social setting using MissClaw, a controlled research replica of Moltbook. We find that (1) social credibility cues, especially perceived consensus, are the dominant driver of short-term behavioral influence, with misleading rates up to 61%; (2) routine memory-saving behavior can promote short-term pollution into durable long-term memory at rates up to 91%, with cross-session behavioral influence reaching 76%; (3) under naturalistic browsing with content dilution and context pruning, pollution still crosses session boundaries. Overall, prompt injection is not required: ordinary social misinformation is sufficient to silently shape agent memory and behavior under heartbeat-driven background execution.

</details>

### 13. Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

📄 [arXiv](https://arxiv.org/abs/2602.15654)　📅 2026-02　🏷 ICLR 2026 Workshop

**关键词**：`attack`、`self-evolving memory`、`indirect exposure`、`cross-session persistence`、`persistent control`

👤 **作者**：Xianglin Yang、Yufei He、Shuo Ji、Bryan Hooi、Jin Song Dong

- 🎯 **研究动机**：自进化 agent 会把良性 session 中观察的不可信内容写入长期记忆并被当作指令，跨 session 持久风险未被研究
- 🔬 **研究方法**：形式化 Zombie Agent 攻击：感染阶段经正常记忆更新写入 payload，触发阶段诱导未授权工具行为，并为滑窗与检索式记忆设计抗截断、抗过滤的持久化策略
- 📌 **结论**：一次间接注入可转化为跨 session 持久控制，仅做单 session 提示过滤的防御不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker. We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

</details>

### 14. Memory Injection Attacks on LLM Agents via Query-Only Interaction

📄 [arXiv](https://arxiv.org/abs/2503.03704) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42a97bbd9844d2bf68596730af80bcdf-Abstract-Conference.html)　📅 2025-03　🏷 NeurIPS 2025

**关键词**：`attack`、`query-only injection`、`bridging step`、`memory bank`、`MINJA`、`bridging steps`

👤 **作者**：Shen Dong、…、Zhen Xiang

- 🎯 **研究动机**：已有攻击假设可直接修改 Agent memory bank，纯查询交互注入未被研究
- 🔬 **研究方法**：MINJA 仅凭查询与输出观察注入恶意记录：bridging steps 把受害 query 连到恶意推理，指示 prompt 引导 Agent 自生成桥接步并渐进缩短
- 📌 **结论**：多类 Agent 上未来受害 query 会召回并执行恶意推理，任意用户即可影响 Agent 记忆

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agents powered by large language models (LLMs) have demonstrated strong capabilities in a wide range of complex, real-world applications. However, LLM agents with a compromised memory bank may easily produce harmful outputs when the past records retrieved for demonstration are malicious. In this paper, we propose a novel Memory INJection Attack, MINJA, without assuming that the attacker can directly modify the memory bank of the agent. The attacker injects malicious records into the memory bank by only interacting with the agent via queries and output observations. These malicious records are designed to elicit a sequence of malicious reasoning steps corresponding to a different target query during the agent's execution of the victim user's query. Specifically, we introduce a sequence of bridging steps to link victim queries to the malicious reasoning steps. During the memory injection, we propose an indication prompt that guides the agent to autonomously generate similar bridging steps, with a progressive shortening strategy that gradually removes the indication prompt, such that the malicious record will be easily retrieved when processing later victim queries. Our extensive experiments across diverse agents demonstrate the effectiveness of MINJA in compromising agent memory. With minimal requirements for execution, MINJA enables any user to influence agent memory, highlighting the risk.

</details>

### 15. Unveiling Privacy Risks in LLM Agent Memory

📄 [arXiv](https://arxiv.org/abs/2502.13172) · 🎓 [Official](https://aclanthology.org/2025.acl-long.1227/)　📅 2025-02　🏷 ACL 2025

**关键词**：`attack`、`memory extraction`、`black-box prompt`、`private interaction`

👤 **作者**：Bo Wang、…、Pengfei He

- 🎯 **研究动机**：LLM Agent 的 memory 存私密 user-agent 交互作示范，隐私风险未系统研究
- 🔬 **研究方法**：MEXTRA 黑盒提取：按攻击者知识水平设计提取 prompt 并自动生成
- 📌 **结论**：两个代表性 Agent 上有效抽取记忆隐私，并识别 memory 设计与攻击者知识对泄漏的影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents have become increasingly prevalent across various real-world applications. They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work, we systematically investigate the vulnerability of LLM agents to our proposed Memory EXTRaction Attack (MEXTRA) under a black-box setting. To extract private information from memory, we propose an effective attacking prompt design and an automated prompt generation method based on different levels of knowledge about the LLM agent. Experiments on two representative agents demonstrate the effectiveness of MEXTRA. Moreover, we explore key factors influencing memory leakage from both the agent designer's and the attacker's perspectives. Our findings highlight the urgent need for effective memory safeguards in LLM agent design and deployment.

</details>

### 16. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

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

### 17. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

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

### 18. Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework

📄 [arXiv](https://arxiv.org/abs/2603.11768)　📅 2026-03

**关键词**：`defense`、`memory governance`、`semantic drift`、`dynamic access control`

👤 **作者**：Chingkwun Lam、Jiaxin Li、Lingfei Zhang、Kuo Zhao

- 🎯 **研究动机**：记忆系统从静态检索库转向动态 agent 机制，语义漂移与记忆腐败风险被既有综述忽视
- 🔬 **研究方法**：SSGM 框架把记忆演化与执行解耦，在任何巩固前强制一致性验证、时间衰减建模与动态访问控制
- 📌 **结论**：形式化缓解敏感上下文固化导致的拓扑性知识泄露与迭代摘要导致的知识退化，建立记忆腐败风险分类法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory has emerged as a foundational component of autonomous Large Language Model (LLM) agents, enabling continuous adaptation, lifelong multimodal learning, and sophisticated reasoning. However, as memory systems transition from static retrieval databases to dynamic, agentic mechanisms, critical concerns regarding memory governance, semantic drift, and privacy vulnerabilities have surfaced. While recent surveys have focused extensively on memory retrieval efficiency, they largely overlook the emergent risks of memory corruption in highly dynamic environments. To address these emerging challenges, we propose the Stability and Safety-Governed Memory (SSGM) framework, a conceptual governance architecture. SSGM decouples memory evolution from execution by enforcing consistency verification, temporal decay modeling, and dynamic access control prior to any memory consolidation. Through formal analysis and architectural decomposition, we show how SSGM can mitigate topology-induced knowledge leakage where sensitive contexts are solidified into long-term storage, and help prevent semantic drift where knowledge degrades through iterative summarization. Ultimately, this work provides a comprehensive taxonomy of memory corruption risks and establishes a robust governance paradigm for deploying safe, persistent, and reliable agentic memory systems.

</details>

### 19. A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory

📄 [arXiv](https://arxiv.org/abs/2510.02373) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61006)　📅 2025-09　🏷 ICML 2026

**关键词**：`defense`、`memory validation`、`dual memory`、`error-cycle breaking`、`agent safety`、`empirical evaluation`

👤 **作者**：Qianshan Wei、…、XiaoFeng Wang

- 🎯 **研究动机**：agent 记忆注入的恶意效果仅在特定上下文激活，且一旦触发即形成自我强化的错误循环
- 🔬 **研究方法**：提出 A-MemGuard：多记忆推理路径的共识验证检测异常，双记忆结构把失败蒸馏为经验教训供未来行动前查询，不改 agent 架构
- 📌 **结论**：多基准上攻击成功率削减超 95% 且效用代价极小，把记忆安全从静态过滤转向经验驱动防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents use memory to learn from past interactions, enabling autonomous planning and decision-making in complex environments. However, this reliance on memory introduces a critical security risk: an adversary can inject seemingly harmless records into an agent's memory to manipulate its future behavior. This vulnerability is characterized by two core aspects: First, the malicious effect of injected records is only activated within a specific context, making them hard to detect when individual memory entries are audited in isolation. Second, once triggered, the manipulation can initiate a self-reinforcing error cycle: the corrupted outcome is stored as precedent, which not only amplifies the initial error but also progressively lowers the threshold for similar attacks in the future. To address these challenges, we introduce A-MemGuard (Agent-Memory Guard), the first proactive defense framework for LLM agent memory. The core idea of our work is the insight that memory itself must become both self-checking and self-correcting. Without modifying the agent's core architecture, A-MemGuard combines two mechanisms: (1) consensus-based validation, which detects anomalies by comparing reasoning paths derived from multiple related memories and (2) a dual-memory structure, where detected failures are distilled into ``lessons'' stored separately and consulted before future actions, breaking error cycles and enabling adaptation. Comprehensive evaluations on multiple benchmarks show that A-MemGuard effectively cuts attack success rates by over 95% while incurring a minimal utility cost. This work shifts LLM memory security from static filtering to a proactive, experience-driven model where defenses strengthen over time. Our code is available in https://github.com/TangciuYueng/AMemGuard

</details>

### 20. SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2609.02786)　📅 2026-09

**关键词**：`defense`、`self-evolving agent`、`harness-policy co-evolution`、`on-policy safety experience`

👤 **作者**：Qinghua Mao、…、Dongrui Liu

- 🎯 **研究动机**：Agent 安全同时由 base model 与运行 harness 决定，单独外部 harness 更新或策略优化都无法闭合运行时控制与内在安全
- 🔬 **研究方法**：提出 SafeEvolve：用完成的 on-policy 轨迹安全经验驱动 harness-policy 共演化循环——harness 侧转化为有界、可审计、可回滚的组件级更新，policy 侧经 harness-use SFT 引导与 harness 增强的分解奖励 RL
- 📌 **结论**：在 agentic 安全基准上取得更优安全-效用权衡：Qwen3.5-4B 上 AgentDojo ASR 降低 3 倍，benign utility 从 59.79% 升至 61.86%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving framework for agent safety alignment. SafeEvolve leverages safety experience from completed on-policy trajectories to drive a continual loop of harness-policy co-evolution. On the harness side, SafeEvolve converts trajectory-level safety evidence into bounded, component-level updates across safety prompt and hierarchical skills, yielding auditable and reversible harness artifacts. On the policy side, SafeEvolve follows a two-stage SFT-RL paradigm, where harness-use SFT bootstraps the policy to actively leverage evolved harness artifacts, and harness-augmented RL further shapes autonomous safety behaviors during multi-step exploration via verifier-decomposed rewards. Through harness-policy co-evolution, SafeEvolve converts safety experience into an evolved runtime harness and improved policy behavior. Experiments on agentic safety benchmarks show that SafeEvolve achieves a stronger safety-utility tradeoff than existing baselines. For Qwen3.5-4B, SafeEvolve achieves a $3\times$ ASR reduction on AgentDojo while improving benign utility from 59.79% to 61.86%.

</details>

### 21. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

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

### 22. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

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

### 23. Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.12977)　📅 2026-08

**关键词**：`defense`、`agent memory`、`self-evolution`、`cross-session risk`

👤 **作者**：Jiajun Ruan、Peiyang Li、Yukun Chen、Fengting Li、Chao Feng

- 🎯 **研究动机**：现有运行时防御依赖人工设计干预，缺乏原则化的构建与维护框架
- 🔬 **研究方法**：先给出 harness 级运行时防御形式化统一刻画现有干预；HARD 据失败轨迹自动识别干预策略并迭代改进防御工件
- 📌 **结论**：安全性超过现有人工防御且保持良性任务效用，把防御开发从人工工程转为自主演化过程

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The expanding operational capabilities of large language model (LLM) agents introduce sophisticated security threats. Runtime defenses have emerged as an effective approach to mitigating these risks by integrating security mechanisms into the agent execution loop. However, existing runtime defenses rely heavily on manually designed interventions and lack a principled framework for their construction and maintenance. In this work, we first develop a harness-level formulation of runtime defense that systematically characterizes how harness mechanisms enable defense construction and provides a unified view of existing runtime defense interventions from a harness perspective. Building on this formulation, we propose HARD (Harness-based Autonomous Runtime Defense Evolution), a self-evolving runtime defense framework that automatically identifies appropriate intervention strategies and iteratively improves defense artifacts based on observed failure traces. HARD transforms runtime defense development from manual engineering into an autonomous evolution process, and extensive experiments demonstrate that it improves security performance over existing handcrafted defenses while preserving benign task utility. Our findings highlight autonomous defense evolution as a promising new paradigm for securing deployed LLM agents, enabling agents to identify defense weaknesses and continuously improve their protection mechanisms.

</details>

### 24. Self-Evolving Just-In-Time Memory for Proactive Embodied Safety

📄 [arXiv](https://arxiv.org/abs/2607.16247) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5121)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`embodied safety`、`agent memory`、`self-evolution`、`active mitigation`、`test-time learning`

👤 **作者**：Bingrui Sima、Lizhong Wang、Xiaoya Lu、Kun He、Xiao Yang

- 🎯 **研究动机**：具身 agent 难以主动化解闭环交互中动态出现的危险，运行时护栏阻断或过度谨慎只会拖停任务
- 🔬 **研究方法**：提出 Self-Evolving Just-In-Time Memory：风险充分拓扑信念图持久追踪安全状态、事实记忆精确预判危险、经验记忆注入可执行的 Meta-Skill，并以 Test-Verify-Write 循环在测试时持续精化
- 📌 **结论**：IS-Bench 上跨多个 VLM 骨干大幅提升 Safe-Success（Qwen3-VL-8B +30.3%），实现不拖停任务的主动危险化解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Vision-Language Models (VLMs) have empowered embodied agents to execute complex household tasks, they struggle to proactively handle dynamically emerging hazards during closed-loop interactions. Existing safety approaches often rely on runtime guardrails to block unsafe actions or induce excessive caution, which severely stalls task progress instead of actively resolving the underlying risks. To break this safety-progress trade-off, we introduce the Self-Evolving Just-In-Time Memory framework, which reframes embodied safety from progress-stalling guardrails to proactive hazard mitigation. The framework consists of a Risk-Sufficient Topological Belief Graph (RSG) for persistent safety-relevant state tracking under partial observability, an Agency-Grounded Factual Memory for precise hazard anticipation, and an Experience Memory that injects procedural Meta-Skills to guide executable, progress-preserving mitigation. Furthermore, we propose an automated Test-Verify-Write loop, allowing agents to continually refine their mitigation Meta-Skills from execution traces at test time. Experiments on IS-Bench demonstrate that our framework substantially boosts the Safe-Success rate across multiple VLM backbones (e.g., +30.3% on Qwen3-VL-8B), enabling agents to proactively mitigate hazards without stalling task progress. Code is available at https://github.com/DyMessi/JIT-Memory.

</details>

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

### 26. RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution

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

### 27. Phantom Gains: Auditing Self-Improvement Against a Measured Null

📄 [arXiv](https://arxiv.org/abs/2608.20290)　📅 2026-08

**关键词**：`benchmark`、`agent memory`、`self-evolution`、`cross-session risk`

👤 **作者**：Cheng Xu、Nan Yan、Liming Chen、M-Tahar Kechadi

- 🎯 **研究动机**：以逐题增益/损失判断自我提升易受测量伪影影响：对两个噪声估计做差分本身脆弱
- 🔬 **研究方法**：对 Qwen3-8B 三轮 LoRA 自训练以冻结核对组过同一管线审计，识别七个在缺控制时反转结论的测量失败
- 📌 **结论**：单次贪心解码的账本能在未训练模型上制造能力变化、扩面统计赋其 0.280 获取率；换成 FDR 控制的逐题精确检验后任何保留重复上都检不出；外部蒸馏有效而三种自训练无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Several are standard practice. A ledger built on a single greedy decode manufactures capability changes on an untrained model, largely an artifact of inference batching; the expansion statistic separating acquisition from sharpening assigns that same model a rate of $0.280$. The natural threshold repair does not survive replication: estimated across the frozen comparisons such a design already contains, its null stays non-zero. We replace it with a per-problem exact test against a pooled baseline under false-discovery-rate control, which detects nothing on any held-out replicate and is unchanged under the multiple-testing rule, error rate and pool size. Applied to a ladder of arms matched in stream, volume and evaluation, the audit finds that external distillation improves problems the base model rarely reaches while three forms of self-training do not; a regression rejects this asymmetry as a by-product of distillation's larger overall gain ($p < 10^{-8}$). On the far smaller set of problems the base model never reaches, the evidence is inconclusive, while self-training corrupts problems solved at baseline at rates well above the measured floor. Transition-level auditing therefore requires a separately measured null for every statistic it reports: nulls that cost no new experiments, built from baseline replicates a multi-arm study already owns, though not from as few as most possess.

</details>

### 28. Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2608.17148)　📅 2026-08

**关键词**：`attack`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`

👤 **作者**：Sibo Liu

- 🎯 **研究动机**：个人 agent 从一个受众学到的事实可能被组装进另一受众的 prompt——记忆到上下文这一步是攻击面
- 🔬 **研究方法**：在记忆到上下文转换处施加反单调受众成员规则：条目携带记录时受众，当前 viewers 从信道元数据读取、歧义回退公共，仅当每个 viewer 已属其受众才准入，并证明投毒记忆不能扩大自身受众
- 📌 **结论**：合成语境完整性套件中被禁事实零进入边界组装的上下文，且所有读路径经审计 fail-closed

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A personal language agent learns a fact from one audience and may later place it in the prompt it assembles for another. This memory-to-context step is an attack surface: ambiguous or inconsistent channels, cross-audience prying, and poisoned memory can each cause the system to assemble context containing a fact relevant to the query yet unauthorized for the current viewers. We introduce authorization before context: a single, anti-monotone audience-membership rule applied at the memory-to-context transition. Each item carries the audience present when it was recorded; the current viewer set is read from channel metadata and falls back to public when ambiguous; and the item is admitted only when every current viewer already belonged to its audience. We prove that this rule gives every participant cross-channel recall while ensuring, by exclusion rather than by model behavior, that nothing recorded for a narrower audience reaches a broader one and that poisoned memory cannot widen its own audience. The boundary is a model-neutral invariant on the exact assembled context: a forbidden fact must be absent before the model is called. On a synthetic Contextual-Integrity suite, no forbidden fact entered the context our boundary assembled, whereas unscoped baselines included such facts by construction; we further audit that every read path fails closed. The evidence is preliminary and synthetic.

</details>
