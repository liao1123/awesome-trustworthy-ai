# Agent Memory 投毒

[返回投毒与后门目录](README.md)

## 研究方向

这一方向研究不可信输入如何被 Agent 的 long-term memory、经验库、图记忆或持久会话状态保存，并在未来任务中被检索、激活并转化为攻击者指定的行为。核心问题包括 memory write 与 retrieval 的信任边界、跨 session 持久性、来源与完整性标记、污染传播，以及从写入、触发、后果到 selective repair 的全生命周期评测。

> **收录口径（截至 2026-09-02）：** 收录直接研究 Agent memory poisoning、memory injection、persistent memory backdoor，以及专门针对这些攻击的 benchmark、检测、溯源和修复工作；普通 memory 能力、单纯隐私抽取和一般 RAG corpus poisoning 不在本页重复收录。

## 研究脉络

- **写入投毒：** 攻击者利用对话、邮件、网页、图像或 tool output 诱导 Agent 自行写入恶意记忆，而不必直接访问 memory store。
- **检索与延迟激活：** 毒记忆通过 semantic anchor、事实伪装、关系冲突或持久状态在未来任务中命中，把一次输入变成跨 session 攻击。
- **组合与传播：** 多条单看无害的 memory、consolidation 生成的派生记录或 shared memory promotion 可共同恢复恶意语义，并把污染传播给其他 Agent。
- **评测与修复：** 评测需要同时跟踪 persistence、retrieval、behavioral consequence、lineage 与 forgetting；防御则从内容过滤发展到 origin-bound authority、运行时 gating 和 selective rollback。

## 记忆投毒与跨 Session 攻击

### 1. Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.00523)　📅 2026-09

**关键词**：`attack`、`end-to-end optimization`、`write-retrieve-utilize`、`transferability`、`defense robustness`

👤 **作者**：Chuanchao Zang、…、Shanqing Guo

- 🎯 **研究动机**：间接记忆投毒需穿越写入-检索-利用多阶段管线，现有攻击孤立优化单阶段，上游转换会抹去为下游准备的改进
- 🔬 **研究方法**：提出 PipePoison 端到端优化：从本地 shadow 系统收集细粒度阶段反馈，用链式损失识别瓶颈阶段，用稳定性校准的阶段与配置权重提升迁移性
- 📌 **结论**：三个 Agent 框架、四种记忆机制上攻击利用率提升 19.1 个百分点；完全未见配置上仍超最强基线 16 个百分点，并在八种防御下有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory can turn untrusted external content into persistent influence over an LLM agent's future decisions, creating the threat of indirect memory poisoning. A successful attack must survive a multi-stage pipeline comprising memory writing, retrieval, and utilization. Existing attacks largely rely on intra-stage optimization, optimizing individual stages in isolation while overlooking inter-stage coupling. Specifically, these stages impose different requirements on the same poisoning content, and each stage operates on the transformed output of its predecessor. Consequently, optimizing one stage may undermine the effectiveness of other stages, while upstream transformations may erase improvements intended for downstream stages. Indirect memory poisoning should therefore be viewed as an end-to-end optimization problem. Based on this insight, we present \textsc{PipePoison}, which collects fine-grained stage feedback from local shadow systems, uses chain-structured losses to identify and optimize the stage bottlenecking end-to-end success, and applies stability-calibrated stage and configuration weights to improve transferability. Across three agent frameworks and four memory mechanisms, \textsc{PipePoison} improves attack utilization rate by 19.1 percentage points. Even on fully unseen victim configurations, it outperforms the strongest baseline by 16 percentage points and remains effective under eight representative defenses.

</details>

### 2. InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

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

### 3. MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds

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

### 4. MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.03844)　📅 2026-08

**关键词**：`attack`、`query-only injection`、`memory probing`、`audit evasion`

👤 **作者**：Jiaming Chen、Yisen Gao、Yanping Li、Zifan Liu、Yumeng Zhang、Jun Zhang

- 🎯 **研究动机**：现有 query-only 记忆攻击在大规模良性记忆池与主动输入审计两个现实设定下失效
- 🔬 **研究方法**：MAFIA 用记忆探测、预算分配与调度保证检索竞争力，并用紧凑事实外衣保持语义相似的同时绕过语义审计
- 📌 **结论**：ASR 最高达 90.7%，同时把审计检测率从峰值 83.3% 压至至多 7.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiveness and rigorous semantic checks. To overcome these limitations, we propose MAFIA, a query-only Memory Attack framework via probing and Factual Injection against Audit, tailored to this extended threat model. Specifically, MAFIA introduces: (1) a placement strategy that ensures retrieval-competitive injection via memory probing, budget allocation, and scheduling; and (2) a payload design that bypasses audits using compact factual cloaks, preserving malicious effects while maintaining high semantic similarity. Extensive evaluations reveal that MAFIA achieves up to a 90.7% attack success rate while suppressing audit detection from a peak of 83.3% to at most 7.4%, exposing critical vulnerabilities across agentic memory systems. Code will be made publicly available at https://github.com/JiamingChen1234/MAFIA.

</details>

### 5. Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw

📄 [arXiv](https://arxiv.org/abs/2608.01637)　📅 2026-08

**关键词**：`attack`、`collusive memory`、`benign-looking fragments`、`cross-session composition`

👤 **作者**：Zheng Lin、Yuzhe Huang、Zhenxing Niu、Xianmin Ye、Haichang Gao

- 🎯 **研究动机**：记忆投毒攻击依赖单条恶意记录，多条单独良性的记忆组合致害的组合威胁被忽视
- 🔬 **研究方法**：MemCollusion 用切香肠策略生成单独良性、集体有害的记忆片段；在复现 Moltbook 的跨会话环境 MoltLab 中对 OpenClaw 评测 48 个场景
- 📌 **结论**：最强记忆保存设定下 Memory Save Rate 81.3%、ASR 75.0%，在良性记忆稀释与记忆级防御下仍然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memory poisoning attacks. MemCollusion applies salami tactics---a strategy that slices an adversarial objective into small, individually innocuous pieces---to generate memory fragments that are individually benign looking but collectively harmful. It constructs memory coalitions using four design constraints, five theory-informed strategies, and a fine-tuned generator. To assess collusive memory poisoning in a realistic cross-session setting, we develop MoltLab, a controlled research reproduction of Moltbook, in which crafted platform content must first be observed and distilled into persistent memory before influencing the agent's behavior in a separate session. We evaluate MemCollusion on OpenClaw using two backbone models across 48 scenarios. Under the strongest memory-saving setting, MemCollusion achieves an average Memory Save Rate of 81.3% and an Attack Success Rate of 75.0%, and remains effective under both benign memory dilution and memory-level defenses.

</details>

### 6. Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents

📄 [arXiv](https://arxiv.org/abs/2607.15657)　📅 2026-07

**关键词**：`attack`、`multimodal memory`、`imperceptible perturbation`、`black-box attack`、`Lucid`、`long-term memory`

👤 **作者**：Halima Bouzidi、Mboutidem Ekemini Mkpong、Mohammad Abdullah Al Faruque

- 🎯 **研究动机**：多模态 agent 无条件信任视觉数据，图像即可成为严格图像边界威胁模型下的攻击载体
- 🔬 **研究方法**：提出 Lucid 黑盒对抗框架：仅对图像加不可感知扰动，实现上下文内记忆投毒（有历史文本强化时替换良性图）与上下文外记忆注入（无文本矫正时诱导生成）
- 📌 **结论**：跨五个黑盒记忆架构（图结构、LLM 摘要、商用系统）投毒 ASR 61.6%、注入 58.4%，暴露多模态记忆管线结构漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

</details>

### 7. When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents

📄 [arXiv](https://arxiv.org/abs/2607.06595)　📅 2026-07

**关键词**：`attack`、`GhostWriter`、`email injection`、`long-term memory`

👤 **作者**：George Torres、Sharad Shrestha、Satyajayant Misra

- 🎯 **研究动机**：融合对话与行动规划的 tool-using 个人 agent 处理敏感信息又接触不可信来源，记忆子系统缺乏安全治理
- 🔬 **研究方法**：提出 GhostWriter 两阶段攻击：注入（向 agent 发送隐藏攻击载荷）与激活（毒化记忆被检索）；并提出 AM-Sentry（记忆保存策略+记忆检索筛查）防御
- 📌 **结论**：对 SOTA agent 注入率约 98%、平均激活率约 60%；AM-Sentry 大幅降低成功率并保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.

</details>

### 8. When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents

📄 [arXiv](https://arxiv.org/abs/2607.05189)　📅 2026-07

**关键词**：`attack`、`stealth injection`、`personal agent`、`WhisperBench`

👤 **作者**：Yechao Zhang、…、Tianwei Zhang

- 🎯 **研究动机**：持久个人 agent 中不可信外部内容可被静默写入记忆并作为可信状态复用，单邮件隐蔽注入的威胁未被系统研究
- 🔬 **研究方法**：构建 WhisperBench（108 例、五类风险、事实与偏好投毒，基于真实 IMAP/SMTP 工作流）；提出 MemGhost 一次性载荷生成：环境代理模拟持久执行、目标代理把记忆采纳与对话隐蔽转为 rubric 奖励，SFT+RL 训练攻击策略
- 📌 **结论**：56 个留出测试上 OpenClaw+GPT-5.4 端到端成功率 87.5%、Claude Code SDK+Sonnet 4.6 达 71.4%，跨架构与记忆后端迁移并抗输入/模型/系统级防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write poisoned memory, stay hidden in the agent's response to the user, and affect future behavior. We introduce WhisperBench, a 108-case benchmark spanning five risk categories and both fact and preference poisoning. Built on a real IMAP/SMTP workflow and an authentic email agent skill, it enables full-cycle evaluation of stealth memory injection attacks. To enable this black-box attack under single-email delivery and without runtime feedback, we propose MemGhost, a one-shot payload generation framework. MemGhost uses an environment proxy to emulate persistent-agent execution and an objective proxy to convert memory adoption and conversational stealth into dense rubric-based rewards, then trains the attacker policy with supervised fine-tuning and reinforcement learning. Across 56 held-out test cases, MemGhost achieves 87.5% end-to-end success on OpenClaw with GPT-5.4 and 71.4% on Claude Code SDK with Sonnet 4.6. It also transfers across personal-agent architectures (NanoClaw and Hermes Agent) and memory backends (filesystem and vector-based Mem0), and remains effective against input-level, model-level, and system-level defenses. These results suggest that persistent memory can turn ordinary external processing into a practical pathway for long-term agent compromise.

</details>

### 9. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

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

### 10. FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion

📄 [arXiv](https://arxiv.org/abs/2606.15609) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/rao)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`attack`、`memory fragmentation`、`access control`、`tool-use agent`、`LLM agent`、`access-control bypass`

👤 **作者**：Zixin Rao、…、Zhen Xiang

- 🎯 **研究动机**：agent 访问控制只检查最终用户查询，长期记忆引入的时间信道使被禁内容可碎片化存入记忆再重组
- 🔬 **研究方法**：提出 FragFuse 三阶段：黑盒自适应查询+片段掩码识别会触发拒绝的片段、用标记载体查询注入记忆、后续攻击查询检索融合片段；并以代理优化自动生成攻击
- 📌 **结论**：四种 agent 设定、三种 SOTA 访问控制上平均绕过率 86.3%、端到端有害任务成功率 41.1%，任务退化仅 4.4%；prompt injection 与困惑度检测器均无法防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating requests and prevent misuse. We reveal a novel attack surface arising from agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing form, and later reconstructed through memory retrieval without appearing explicitly in the final user query. We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory. FragFuse operates in three stages: (1) identifying rejection-responsive fragments via black-box adaptive querying with fragment masking; (2) injecting these fragments into memory using marker carrier queries; and (3) retrieving and fusing the stored fragments through a follow-up attack query. Although FragFuse can be instantiated manually for individual agents, we further develop a surrogate-based optimization scheme that tunes fusion instructions and marker designs, enabling automated attack generation without violating the attacker's threat-model assumptions. We evaluate FragFuse across four representative agent settings and task domains, covering three state-of-the-art agent access-control mechanisms. FragFuse achieves an average bypass success rate of 86.3% and an average end-to-end harmful task success rate of 41.1% across all settings, with only 4.4% average task-success degradation compared with configurations without access control. We also show that alternative defenses, including state-of-the-art prompt-injection detectors and perplexity detectors, do not effectively address this attack.

</details>

### 11. MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents

📄 [arXiv](https://arxiv.org/abs/2606.10742)　📅 2026-06

**关键词**：`attack`、`multimodal memory`、`graph memory`、`triggered retrieval`、`web agent`、`persistent retrieval`

👤 **作者**：Yv Zhang、…、Yaowei Wang

- 🎯 **研究动机**：web agent 图结构外部记忆可被持久检索，恶意内容注入记忆后被反复召回影响行为，多模态记忆投毒被忽视
- 🔬 **研究方法**：提出 MemVenom 黑盒框架两阶段攻击：触发条件化检索保证恶意记忆高概率召回，检索后用对抗扰动+隐蔽 OCR 注入覆盖用户目标，无需改参数或重优化
- 📌 **结论**：多个 agent 框架与 VLM 上端到端攻击成功率高，GPT-5 系 web agent 上达 99.15%，且跨架构与规模迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

</details>

### 12. Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction

📄 [arXiv](https://arxiv.org/abs/2605.29960)　📅 2026-05

**关键词**：`attack`、`conversational injection`、`selective memory`、`semantic bridge`

👤 **作者**：Hongtao Wang、Se Yang、Yu Chen、Puzhuo Liu

- 🎯 **研究动机**：已有记忆投毒假设内容可直接写入记忆，忽略现代记忆管线的选择性抽取与改写阶段，现实设定下失效
- 🔬 **研究方法**：MemPoison 三组件：语义关系桥绑定触发与 payload 确保一起被抽取、实体伪装抗改写、联合嵌入优化使注入文本聚簇且与良性嵌入隔离
- 📌 **结论**：跨 agent 域与记忆机制最高 ASR 达 0.95；机制上利用嵌入各向异性并改变注意力模式，多种防御存在根本局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly leverage long term memory to support persistent and autonomous task execution. However, this capability also introduces a new attack surface: memory poisoning, where adversaries can inject malicious information to influence future behavior. Existing memory poisoning attacks often assume that injected content can be stored directly in memory, overlooking the selective extraction and rewriting stages in modern memory pipelines. This makes prior methods ineffective under realistic settings. In this paper, we propose MemPoison, a novel memory poisoning attack that bypasses selective memory mechanisms in LLM agents, where an attacker can inject triggerable backdoors into the agent's long-term memory through dialogue interactions, thereby misleading its subsequent responses. MemPoison introduces three key components: (i) a semantic relational bridge that binds the trigger and payload into a coherent statement to ensure they are extracted into memory together; (ii) entity masquerading that optimizes triggers to mimic named entities, resisting rewriting; and (iii) joint embedding optimization that shapes trigger-injected texts into a tight cluster in the embedding space while maintaining isolation from benign embeddings for stealth. Evaluations across different agent domains and memory mechanisms show MemPoison achieves attack success rates up to 0.95, outperforming existing baselines. Mechanistic analysis indicates that the attack exploits embedding-space anisotropy and shifts attention patterns, highlighting core vulnerabilities in selective memory systems. We evaluate multiple defense strategies and demonstrate their fundamental limitations in mitigating the attack.

</details>

### 13. MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.26154)　📅 2026-05

**关键词**：`attack`、`tool selection`、`fact disguise`、`policy steering`

👤 **作者**：Xuanye Zhang、…、Kwok-Yan Lam

- 🎯 **研究动机**：现有攻击操纵工具元数据，易被审计且随 agent 依赖记忆积累经验优化选择而失效
- 🔬 **研究方法**：MemMorph 毒化长期记忆：注入伪装成技术事实、事故报告与操作策略的少量记录，重塑 agent 上下文感知使其自主推断并选择攻击者偏好的工具
- 📌 **结论**：3 个基准、10 个骨干、3 种记忆实现下仅 3 条注入记录即达最高 85.9% ASR，超最强基线 25 个百分点，3 种代表性防御下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-driven agents are capable of selecting external tools to complete users' tasks. However, attackers could compromise such process, steering agents toward inappropriate/wrong tools and enabling malicious actions. Most existing attacks primarily manipulate the tool metadata, which is easily detectable by auditing and may lose effectiveness as modern agents increasingly adopt memory modules to refine tool selection policies through accumulated experience. This paper proposes MemMorph, the first attack that bias tool selection by poisoning the agent's long-term memory. Rather than explicitly dictating the tool invocation decision, MemMorph injects a small number of crafted records that are disguised as technical facts, incident reports, and operational policies. These poisoned records reshape the agent's contextual perception and decision-making process, leading it to autonomously infer and select the tool preferred by the attacker. Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. Our findings expose long-term memory as a critical and under-explored attack surface in tool-augmented agents, urging the development of memory-level integrity safeguards.

</details>

### 14. Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.15338)　📅 2026-05

**关键词**：`attack`、`sleeper memory`、`external context`、`delayed activation`

👤 **作者**：Sidharth Pulipaka、…、Mario Fritz

- 🎯 **研究动机**：持久记忆带来新风险——对抗内容可污染助手记住的用户信息并跨对话潜伏重现
- 🔬 **研究方法**：sleeper memory poisoning：操纵文档、网页或代码库等外部上下文使助手存储伪造用户记忆，评估写入、检索与后续操纵全链路
- 📌 **结论**：毒记忆写入率在 GPT-5.5 上达 99.8%、Kimi-K2.6 上 95%；成功检索后 60-89% 的评测产生攻击者指定的 agent 动作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity. This statefulness introduces a new security risk: adversarial content can corrupt what an assistant remembers and thereby influence future interactions. We propose and study sleeper memory poisoning, a delayed attack in which an adversary manipulates external context, such as a document, webpage, or repository, to cause the assistant to store a fabricated memory about the user. Unlike conventional prompt injection, the attack can remain dormant and re-emerge across multiple later conversations. We evaluate the full attack pipeline: whether poisoned memories are written, later retrieved, and ultimately used to steer the following conversations. Across stateful LLM assistants, poisoned memories were added up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6. Crucially, among successful retrievals, poisoned memories cause attacker-intended agentic actions in 60-89% of evaluations across models. These results show that persistent memory can act as a long-term attack surface across multiple future conversations.

</details>

### 15. ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts

📄 [arXiv](https://arxiv.org/abs/2605.09033)　📅 2026-05

**关键词**：`attack`、`graph memory`、`relation conflict`、`Mem0`

👤 **作者**：Yang Luo、…、Lingyun Peng

- 🎯 **研究动机**：已有 agent 记忆投毒针对扁平文本记录，在图记忆中恶意关系常无法被抽取、并入目标锚邻域或检索
- 🔬 **研究方法**：ShadowMerge 让毒关系与良性证据共享同一 query 激活锚与规范化关系通道但携带冲突值；AIR pipeline 把冲突转成可被图记忆正常处理的交互
- 📌 **结论**：Mem0 与三个公开数据集上平均 ASR 93.8%，较最佳基线高 50.3 个百分点，对无关良性任务影响可忽略；代表性输入侧防御不足以缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into graph memory so that it is later retrieved and influences agent behavior. Existing agent-memory poisoning attacks mainly target flat textual records and are ineffective in graph-based memory because malicious relations often fail to be extracted, merged into the target anchor neighborhood, or retrieved for the victim query. We present SHADOWMERGE, a poisoning attack against graph-based agent memory that exploits relation-channel conflicts. Its key insight is that a poisoned relation can share the same query-activated anchor and canonicalized relation channel as benign evidence while carrying a conflicting value. To realize this, we design AIR, a pipeline that converts the conflict into an ordinary interaction that can be extracted, merged, and retrieved by the graph-memory system. We evaluate SHADOWMERGE on Mem0 and three public real-world datasets: PubMedQA, WebShop, and ToolEmu. SHADOWMERGE achieves 93.8% average attack success rate, improving the best baseline by 50.3 absolute points, while having negligible impact on unrelated benign tasks. Mechanism studies show that SHADOWMERGE overcomes the three key limitations of existing agent-memory poisoning attacks, and defense analysis shows that representative input-side defenses are insufficient to mitigate it. We have responsibly disclosed our findings to affected graph-memory vendors and open sourced SHADOWMERGE.

</details>

### 16. Stateful Agent Backdoor

📄 [arXiv](https://arxiv.org/abs/2605.06158) · 🌐 [Project](https://anonymous.4open.science/r/stateful_agent_backdoor-E89F)　📅 2026-05

**关键词**：`attack`、`cross-session backdoor`、`persistent state`、`state machine`

👤 **作者**：Zhengchunmin Dai、Jiaxiong Tang、Liantao Wu、Peng Sun、Honglong Chen

- 🎯 **研究动机**：现有 LLM agent 后门是无状态的、限于单 session，跨 session 与权限隔离下的攻击未被探索
- 🔬 **研究方法**：把攻击建模为 Mealy 机，经持久组件维护状态，一次触发注入后跨 session 自主增量执行；分解框架支持逐转移独立构造数据
- 📌 **结论**：四个模型上主攻击 ASR 达 80%-95%，更换拓扑与持久组件的扩展变体同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing backdoor attacks on Large Language Model-based agents remain stateless, executing fixed behaviors confined to a single session. We propose a stateful agent backdoor that extends the attack lifecycle across multiple sessions under permission isolation. The attack maintains state through persistent components, enabling autonomous, incremental execution across sessions following a one-time trigger injection. Formally, we model the attack as a Mealy machine and derive a decomposition framework that enables independent per-transition data construction. We instantiate this framework with a primary attack and two extensibility variants. The primary instantiation achieves an attack success rate of 80\%--95\% across four models, with per-transition analysis demonstrating the effectiveness of the decomposition. Extensibility variants with alternative topologies and persistent components demonstrate consistent effectiveness. Code and data are available at https://anonymous.4open.science/r/stateful_agent_backdoor-E89F.

</details>

### 17. Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration

📄 [arXiv](https://arxiv.org/abs/2605.01970)　📅 2026-05

**关键词**：`attack`、`data exfiltration`、`dormant payload`、`tool output`

👤 **作者**：Debeshee Das、Julien Piet、Darya Kaviani、Luca Beurer-Kellner、Florian Tramèr、David Wagner

- 🎯 **研究动机**：agent 长期记忆构成新攻击面，已有记忆投毒威胁模型不现实且缺跨架构系统评估
- 🔬 **研究方法**：Trojan Hippo 经一次不可信 tool call（如 crafted 邮件）植入休眠 payload，仅在用户谈及财务、健康等敏感话题时激活并外传数据；配套 OpenEvolve 自适应红队基准与能力感知安全/效用分析
- 📌 **结论**：四种记忆后端上对 OpenAI 与 Google 前沿模型 ASR 达 85-100%，100 个良性 session 后仍可激活；四种防御可压至 0-5% 但效用代价差异大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory systems enable otherwise-stateless LLM agents to persist user information across sessions, but also introduce a new attack surface. We characterize the Trojan Hippo attack, a class of persistent memory attacks that operates in a more realistic threat model than prior memory poisoning work: the attacker plants a dormant payload into an agent's long-term memory via a single untrusted tool call (e.g., a crafted email), which activates only when the user later discusses sensitive topics such as finance, health, or identity, and exfiltrates high-value personal data to the attacker. While anecdotal demonstrations of such attacks have appeared against deployed systems, no prior work systematically evaluates them across heterogeneous memory architectures and defenses. We introduce a dynamic evaluation framework comprising two components: (1) an OpenEvolve-based adaptive red-teaming benchmark that stress-tests defenses and memory backends against continuously refined attacks, and (2) the first capability-aware security/utility analysis for persistent memory systems, enabling principled reasoning about defense deployment across different usage profiles. Instantiated on an email assistant across four memory backends (explicit tool memory, agentic memory, RAG, and sliding-window context), Trojan Hippo achieves up to 85-100% ASR against current frontier models from OpenAI and Google, with planted memories successfully activating even after 100 benign sessions. We evaluate four memory-system defenses inspired by basic security principles, finding they substantially reduce attack success rates (to as low as 0-5%), though at utility costs that vary widely with task requirements. Because of this substantial security-utility tradeoff, the effective real-world deployment of defenses remains an open challenge, which our evaluation framework is specifically designed to address.

</details>

### 18. Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning

📄 [arXiv](https://arxiv.org/abs/2604.16966) · 🎓 [Official](https://aclanthology.org/2026.acl-long.954/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`multimodal memory`、`recommender agent`、`visual trigger`、`multimodal safety`、`agent safety`

👤 **作者**：Jiachen Qian

- 🎯 **研究动机**：Agentic RecSys 依赖长期记忆 LTM，用户上传图像可成为记忆投毒入口
- 🔬 **研究方法**：Visual Inception 在用户图像注入触发器作为记忆中的沉睡者，规划时被检索即劫持推理链，无需 prompt 注入；配套双过程防御 CognitiveGuard（扩散净化加反事实验证）
- 📌 **结论**：攻击 GHR 约 85%，CognitiveGuard 降至约 10%，延迟按模式 1.5-6.5 秒且不降质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The evolution from static ranking models to Agentic Recommender Systems (Agentic RecSys) empowers AI agents to maintain long-term user profiles and autonomously plan service tasks. While this paradigm shift enhances personalization, it introduces a vulnerability: reliance on Long-term Memory (LTM). In this paper, we uncover a threat termed "Visual Inception." Unlike traditional adversarial attacks that seek immediate misclassification, Visual Inception injects triggers into user-uploaded images (e.g., lifestyle photos) that act as "sleeper agents" within the system's memory. When retrieved during future planning, these poisoned memories hijack the agent's reasoning chain, steering it toward adversary-defined goals (e.g., promoting high-margin products) without prompt injection. To mitigate this, we propose CognitiveGuard, a dual-process defense framework inspired by human cognition. It consists of a System 1 Perceptual Sanitizer (diffusion-based purification) to cleanse sensory inputs and a System 2 Reasoning Verifier (counterfactual consistency checks) to detect anomalies in memory-driven planning. Extensive experiments on a mock e-commerce agent environment demonstrate that Visual Inception achieves about 85% Goal-Hit Rate (GHR), while CognitiveGuard reduces this risk to around 10% with configurable latency trade-offs (about 1.5s in lite mode to about 6.5s for full sequential verification), without quality degradation under our setup.

</details>

### 19. Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents

📄 [arXiv](https://arxiv.org/abs/2604.02623) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`attack`、`web-agent memory`、`environment injection`、`cross-session compromise`、`web agent`、`memory poisoning`

👤 **作者**：Wei Zou、…、Jiarong Jiang

- 🎯 **研究动机**：现有记忆攻击假设可直接写记忆存储或跨用户共享，更现实的环境观察污染未被研究
- 🔬 **研究方法**：eTAMP 仅通过一次被污染的环境观察（如浏览被操纵商品页）毒化 agent 记忆，在未来不同网站的任务中激活，绕过权限防御
- 📌 **结论**：VisualWebArena 上 GPT-5-mini ASR 达 32.5%；环境受挫（点击丢失、乱码）使 ASR 最高放大 8 倍，能力更强的模型并不更安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions. While existing security research on memory assumes attackers can directly inject into memory storage or exploit shared memory across users, we present a more realistic threat model: contamination through environmental observation alone. We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access. A single contaminated observation (e.g., viewing a manipulated product page) silently poisons an agent's memory and activates during future tasks on different websites, bypassing permission-based defenses. Our experiments on (Visual)WebArena reveal two key findings. First, eTAMP achieves substantial attack success rates: up to 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B. Second, we discover Frustration Exploitation: agents under environmental stress become dramatically more susceptible, with ASR increasing up to 8 times when agents struggle with dropped clicks or garbled text. Notably, more capable models are not more secure. GPT-5.2 shows substantial vulnerability despite superior task performance. With the rise of AI browsers like OpenClaw, ChatGPT Atlas, and Perplexity Comet, our findings underscore the urgent need for defenses against environment-injected memory poisoning.

</details>

### 20. Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution

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

### 21. From Storage to Steering: Memory Control Flow Attacks on LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.15125)　📅 2026-03

**关键词**：`attack`、`MEMFLOW`、`tool control flow`、`persistent deviation`

👤 **作者**：Zhenlin Xu、Xiaogang Zhu、Yu Yao、Minhui Xue、Yiliao Song

- 🎯 **研究动机**：现有安全分析把 agent 工具控制流当作一次性会话，忽视记忆的持续支配影响
- 🔬 **研究方法**：定义 Memory Control Flow Attack 并设计 MEMFLOW 自动化评测框架，跨异构任务与长交互量化记忆对控制流的劫持
- 📌 **结论**：对 GPT-5 mini、Claude Sonnet 4.5、Gemini 2.5 Flash 在 LangChain/LlamaIndex 真实工具上，严格安全约束下超 90% 试验仍脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern agentic systems allow Large Language Model (LLM) agents to tackle complex tasks through extensive tool usage, forming structured control flows of tool selection and execution. Existing security analyses often treat these control flows as ephemeral, one-off sessions, overlooking the persistent influence of memory. This paper identifies a new threat from Memory Control Flow Attacks (MCFA) that memory can dominate the control flow, forcing unintended tool usage even against explicit user instructions and inducing persistent behavioral deviations across tasks. To understand the impact of this vulnerability, we further design MEMFLOW, an automated evaluation framework that systematically identifies and quantifies MCFA across heterogeneous tasks and long interaction horizons. To evaluate MEMFLOW, we attack state-of-the-art LLMs, including GPT-5 mini, Claude Sonnet 4.5 and Gemini 2.5 Flash on real-world tools from two major LLM agent development frameworks, LangChain and LlamaIndex. The results show that in general over 90% of trials are vulnerable to MCFA even under strict safety constraints, highlighting critical security risks that demand immediate attention.

</details>

### 22. Memory Poisoning Attacks on Retrieval-Augmented Large Language Model Agents via Deceptive Semantic Reasoning

🌐 [Project](https://doi.org/10.1016/j.engappai.2026.113968)　📅 2026-03

**关键词**：`attack`、`DSRM`、`historical-knowledge poisoning`、`tool steering`

- 🎯 **研究动机**：检索增强agent的历史知识可被投毒操纵决策
- 🔬 **研究方法**：DSRM以self-refine与CoT reasoning将恶意决策伪装成任务相关历史经验
- 📌 **结论**：攻击可跨模型与retriever泛化

### 23. Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

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

### 24. MemIncept: Steering LLM Agents via Cooperative Stealthy Memory Injections

🎓 [Official](https://icml.cc/virtual/2026/poster/66667)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`tool-use agent`、`tool interface`、`action integrity`、`LLM agent security`、`representation steering`

👤 **作者**：Nan Yan、Qian Lou、Jiarong Xing

- 🎯 **研究动机**：记忆注入攻击两难：有效注入显恶意易被检测，良性伪装注入则改变行为的效果差
- 🔬 **研究方法**：MemIncept 黑盒仅用良性查询生成协同查询集：前向保证集体导向目标结果，后向保证语义接近良性查询便于检索，双向进化 meet-in-the-middle
- 📌 **结论**：显著超单记录攻击，成功率接近显式攻击且难被自动过滤或人工审查标记

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory empowers LLM-based agents with adaptive reasoning but exposes a critical attack surface---adversaries can inject malicious records to bias agent behaviors. However, existing attacks face a dilemma: effective injections are often visibly malicious and easily detected, while stealthy, benign-looking injections are often less effective in altering agent behaviors. To address this, we propose MemIncept, a memory poisoning attack that can impact agents even in black-box settings using only benign-appearing queries. Unlike prior methods that inject isolated records, MemIncept generates a cooperative set of queries that work together to bias the agent. It achieves this via a bidirectional evolutionary strategy that optimizes the query set from two ends. A forward pass ensures the queries collectively lead the agent to the target outcome, while a backward pass ensures they are semantically close to victim (benign) queries for reliable retrieval. This ``meet-in-the-middle'' approach creates injected records that are both easy to retrieve and effective at steering behavior. Through extensive experiments across diverse agents, we show that MemIncept significantly outperforms single-record attacks, achieving high success rates comparable to explicit attacks while remaining difficult to flag under automated filters or human inspection.

</details>

### 25. MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval

📄 [arXiv](https://arxiv.org/abs/2512.16962)　📅 2025-12

**关键词**：`attack`、`experience retrieval`、`semantic imitation`、`procedure template`

👤 **作者**：Saksham Sahai Srivastava、Haoyu He

- 🎯 **研究动机**：agent 依赖长期记忆复用成功经验，其推理核心与自身过往之间的信任边界是未探索的攻击面
- 🔬 **研究方法**：MemoryGraft 间接注入：攻击者提供良性外观的 ingestion 级工件，诱导 agent 把恶意 procedure template 持久化进自身 RAG 记忆，利用语义模仿倾向在相似任务时采纳不安全模式
- 📌 **结论**：在 MetaGPT DataInterpreter 加 GPT-4o 上，少量毒记录即可占良性工作负载检索经验的大份额，造成跨 session 的持久行为漂移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents increasingly rely on long-term memory and Retrieval-Augmented Generation (RAG) to persist experiences and refine future performance. While this experience learning capability enhances agentic autonomy, it introduces a critical, unexplored attack surface, i.e., the trust boundary between an agent's reasoning core and its own past. In this paper, we introduce MemoryGraft. It is a novel indirect injection attack that compromises agent behavior not through immediate jailbreaks, but by implanting malicious successful experiences into the agent's long-term memory. Unlike traditional prompt injections that are transient, or standard RAG poisoning that targets factual knowledge, MemoryGraft exploits the agent's semantic imitation heuristic which is the tendency to replicate patterns from retrieved successful tasks. We demonstrate that an attacker who can supply benign ingestion-level artifacts that the agent reads during execution can induce it to construct a poisoned RAG store where a small set of malicious procedure templates is persisted alongside benign experiences. When the agent later encounters semantically similar tasks, union retrieval over lexical and embedding similarity reliably surfaces these grafted memories, and the agent adopts the embedded unsafe patterns, leading to persistent behavioral drift across sessions. We validate MemoryGraft on MetaGPT's DataInterpreter agent with GPT-4o and find that a small number of poisoned records can account for a large fraction of retrieved experiences on benign workloads, turning experience-based self-improvement into a vector for stealthy and durable compromise. To facilitate reproducibility and future research, our code and evaluation data are available at https://github.com/Jacobhhy/Agent-Memory-Poisoning.

</details>

### 26. Context Manipulation Attacks: Web Agents Are Susceptible to Corrupted Memory

📄 [arXiv](https://arxiv.org/abs/2506.17318) · 🎓 [Official](https://icml.cc/virtual/2025/49801)　📅 2025-06　🏷 ICML 2025

**关键词**：`attack`、`plan injection`、`context manipulation`、`web agent`

👤 **作者**：Atharv Singh Patlan、Ashwin Hebbar、Pramod Viswanath、Prateek Mittal

- 🎯 **研究动机**：web agent 的记忆多由客户端或第三方管理，成为易被污染的攻击面
- 🔬 **研究方法**：形式化 plan injection 上下文操纵攻击，污染 agent 内部任务表示，并以 context-chained injections 在用户目标与攻击目标间搭逻辑桥
- 📌 **结论**：对 Browser-use 与 Agent-E 的攻击成功率达可比 prompt 注入的 3 倍并绕过稳健防御，链式注入再使隐私外泄成功率升 17.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous web navigation agents, which translate natural language instructions into sequences of browser actions, are increasingly deployed for complex tasks across e-commerce, information retrieval, and content discovery. Due to the stateless nature of large language models (LLMs), these agents rely heavily on external memory systems to maintain context across interactions. Unlike centralized systems where context is securely stored server-side, agent memory is often managed client-side or by third-party applications, creating significant security vulnerabilities. This was recently exploited to attack production systems. We introduce and formalize "plan injection," a novel context manipulation attack that corrupts these agents' internal task representations by targeting this vulnerable context. Through systematic evaluation of two popular web agents, Browser-use and Agent-E, we show that plan injections bypass robust prompt injection defenses, achieving up to 3x higher attack success rates than comparable prompt-based attacks. Furthermore, "context-chained injections," which craft logical bridges between legitimate user goals and attacker objectives, lead to a 17.7% increase in success rate for privacy exfiltration tasks. Our findings highlight that secure memory handling must be a first-class concern in agentic systems.

</details>

### 27. Real AI Agents with Fake Memories: Fatal Context Manipulation Attacks on Web3 Agents

📄 [arXiv](https://arxiv.org/abs/2503.16248)　📅 2025-03

**关键词**：`attack`、`memory injection`、`Web3 agent`、`unauthorized transfer`

👤 **作者**：Atharv Singh Patlan、Peiyao Sheng、S. Ashwin Hebbar、Prateek Mittal、Pramod Viswanath

- 🎯 **研究动机**：Web3 agent 触碰金融协议与不可变合约，输入、记忆、外部数据等上下文表面无防护，prompt 注入之外还有更隐蔽持久的威胁
- 🔬 **研究方法**：提出 context manipulation 攻击向量（含 memory injection），基于 ElizaOS 构建 CrAIBench，覆盖 150+ 区块链任务与 500+ 攻击用例
- 📌 **结论**：memory injection 比 prompt 注入危害显著更大，可触发未授权转账；prompt 注入防御几乎无效，微调防御能明显降低 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents integrated with Web3 offer autonomy and openness but raise security concerns as they interact with financial protocols and immutable smart contracts. This paper investigates the vulnerabilities of AI agents within blockchain-based financial ecosystems when exposed to adversarial threats in real-world scenarios. We introduce the concept of context manipulation -- a comprehensive attack vector that exploits unprotected context surfaces, including input channels, memory modules, and external data feeds. It expands on traditional prompt injection and reveals a more stealthy and persistent threat: memory injection. Using ElizaOS, a representative decentralized AI agent framework for automated Web3 operations, we showcase that malicious injections into prompts or historical records can trigger unauthorized asset transfers and protocol violations which could be financially devastating in reality. To quantify these risks, we introduce CrAIBench, a Web3-focused benchmark covering 150+ realistic blockchain tasks. such as token transfers, trading, bridges, and cross-chain interactions, and 500+ attack test cases using context manipulation. Our evaluation results confirm that AI models are significantly more vulnerable to memory injection compared to prompt injection. Finally, we evaluate a comprehensive defense roadmap, finding that prompt-injection defenses and detectors only provide limited protection when stored context is corrupted, whereas fine-tuning-based defenses substantially reduce attack success rates while preserving performance on single-step tasks. These results underscore the urgent need for AI agents that are both secure and fiduciarily responsible in blockchain environments.

</details>

### 28. Memory Injection Attacks on LLM Agents via Query-Only Interaction

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

### 29. AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

📄 [arXiv](https://arxiv.org/abs/2407.12784) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html)　📅 2024-07　🏷 NeurIPS 2024

**关键词**：`attack`、`optimized trigger`、`memory bank`、`knowledge base`、`agentic RAG backdoor`、`action hijacking`

👤 **作者**：Zhaorun Chen、Zhen Xiang、Chaowei Xiao、Dawn Song、Bo Li

- 🎯 **研究动机**：LLM Agent 依赖未验证的 memory 或 RAG 知识库，其安全风险未明
- 🔬 **研究方法**：AgentPoison 以约束优化把触发样本映射到唯一嵌入区，含触发指令即高概率检索恶意示范；无需模型训练或微调
- 📌 **结论**：自动驾驶、QA、EHR 三类真实 Agent 平均 ASR 超 80%，投毒率低于 0.1%，良性性能损失小于 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents have demonstrated remarkable performance across various applications, primarily due to their advanced capabilities in reasoning, utilizing external knowledge and tools, calling APIs, and executing actions to interact with environments. Current agents typically utilize a memory module or a retrieval-augmented generation (RAG) mechanism, retrieving past knowledge and instances with similar embeddings from knowledge bases to inform task planning and execution. However, the reliance on unverified knowledge bases raises significant concerns about their safety and trustworthiness. To uncover such vulnerabilities, we propose a novel red teaming approach AgentPoison, the first backdoor attack targeting generic and RAG-based LLM agents by poisoning their long-term memory or RAG knowledge base. In particular, we form the trigger generation process as a constrained optimization to optimize backdoor triggers by mapping the triggered instances to a unique embedding space, so as to ensure that whenever a user instruction contains the optimized backdoor trigger, the malicious demonstrations are retrieved from the poisoned memory or knowledge base with high probability. In the meantime, benign instructions without the trigger will still maintain normal performance. Unlike conventional backdoor attacks, AgentPoison requires no additional model training or fine-tuning, and the optimized backdoor trigger exhibits superior transferability, in-context coherence, and stealthiness. Extensive experiments demonstrate AgentPoison's effectiveness in attacking three types of real-world LLM agents: RAG-based autonomous driving agent, knowledge-intensive QA agent, and healthcare EHRAgent. On each agent, AgentPoison achieves an average attack success rate higher than 80% with minimal impact on benign performance (less than 1%) with a poison rate less than 0.1%.

</details>

### 30. Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking

📄 [arXiv](https://arxiv.org/abs/2608.21230)　📅 2026-08

**关键词**：`analysis`、`false-memory poisoning`、`screening limit`、`provenance trade-off`

👤 **作者**：Arulnidhi Karunanidhi

- 🎯 **研究动机**：Agent 持久记忆使虚假信息经久生效——存入的虚假断言可被后续匹配会话检索，而仅凭文本内容能否区分真假断言存疑
- 🔬 **研究方法**：用无指令、无触发词优化的单轮朴素虚假断言投毒 LongMemEval，评估四阶段写入时筛查管线与 provenance 加权检索两类防御
- 📌 **结论**：仅投毒 1.2% 语料即使准确率从 0.850 跌至 0.300，筛查对 360 条毒记忆拒收 0 条；出厂来源权重与无防御无差异（p=0.80），够强的权重又把不可信合法证据压到准确率 0.0417——应改用检索期占用约束

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent memory makes false information durable: once a false statement is stored, it can be retrieved into future sessions that match it. We measure the cost of this failure mode using plainly worded false assertions generated in a single pass, with no instruction, trigger, or retriever optimization. Poisoning 1.2% of a LongMemEval corpus reduces accuracy from 0.850 to 0.300. A four-stage write-time screening pipeline that reaches 0.832 recall on indirect prompt injection while flagging 1.5% of trigger-word-laden benign text rejects 0 of 360 poisoned memories. We argue this exposes a boundary of content-only screening: distinguishing a false assertion from a true one generally requires external grounding beyond the text itself. We then evaluate provenance-weighted retrieval. The shipped weight is statistically indistinguishable from no defense (p=0.80), while a stronger weight recovers utility only by excluding untrusted content. In a mixed-provenance corpus where untrusted content is mostly benign, accuracy rises from 0.3167 to 0.7000; when the answer-bearing evidence itself arrives untrusted, evidence recall falls to zero and accuracy to 0.0417. Under the measured similarity regime, the additive provenance term has no usable setting: a weight strong enough to resist query-shaped poison is also strong enough to suppress legitimate untrusted evidence. We therefore argue for bounded occupancy constraints at retrieval rather than additive provenance penalties, and release the harnesses, corpora, and aggregate run reports.

</details>

### 31. MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

📄 [arXiv](https://arxiv.org/abs/2607.27080)　📅 2026-07

**关键词**：`benchmark`、`Write-Execute-Forget`、`lifecycle evaluation`、`selective repair`

👤 **作者**：Xuanze Chen、Xukang Xie、Wentao Fu、Jiajun Zhou、Shanqing Yu、Qi Xuan

- 🎯 **研究动机**：已有记忆安全基准少有追踪同一恶意语义从持久化、下游后果到选择性修复的全生命周期并跨记忆后端比较
- 🔬 **研究方法**：构建 MemSecBench：310 案例、48 个真实上下文，按 Write-Execute-Forget 协议在隔离运行时执行，24 配置矩阵（2 harness x 4 记忆后端 x 3 LLM）七检查点证据裁定
- 📌 **结论**：全部配置中恶意记忆 84.2% 持久化、完整 Write-Execute 链 50.3% 成功、选择性修复 56.1%；不同记忆栈端到端攻击成功率最大差 16.1 点、修复差 41.3 点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist. A malicious instruction crafted by an attacker may be stored in long-term memory, recalled much later, and quietly shape a real action. Recent benchmarks increasingly examine agent memory security, yet few trace the same malicious semantics across persistence, downstream consequences, and selective repair under diverse memory-backend comparisons. To address this gap, we introduce MemSecBench, a task-grounded benchmark for the lifecycle security of agent memory systems. It contains 310 cases drawn from 48 realistic contexts across code and science, daily life, and office work. Each case follows a controlled Write--Execute--Forget protocol in an isolated runtime under an exact agent configuration, defined by an agent harness, a memory backend, and an LLM backend. Evidence-based adjudication combines a deterministic write check, checkpoint-specific judge-model evaluations, and programmatic gates across seven lifecycle checkpoints. The experimental design spans a 24-configuration matrix of two agent harnesses, four memory backends, and three LLM backends. Across all 24 configurations, malicious memory persists in 84.2% of all cases, and the full Write--Execute chain succeeds in 50.3%. Among successfully poisoned cases, 59.6% complete the full Execute chain, while 56.1% achieve selective repair.Compared with matched Native configurations, the largest absolute differences are 16.1 percentage points for end-to-end attack success and 41.3 percentage points for selective repair. These descriptive contrasts indicate that the evaluated memory system stacks differ in lifecycle security, both in the propagation of malicious memory and in selective repair after successful memory poisoning.

</details>

### 32. BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents

📄 [arXiv](https://arxiv.org/abs/2601.04566) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.791/)　📅 2026-07　🏷 ACL 2026

**关键词**：`benchmark`、`stage-aware backdoor`、`memory stage`、`trigger propagation`、`attack framework`、`planning／memory／tool`

👤 **作者**：Yunhao Feng、…、Yu-Gang Jiang

- 🎯 **研究动机**：后门研究碎片化、孤立分析单个攻击向量，agent 工作流内跨阶段的触发交互与传播缺乏统一视角
- 🔬 **研究方法**：BackdoorAgent 把攻击面结构化为 planning、memory、tool-use 三个功能阶段并插桩 agent 执行，构建覆盖 Agent QA、Code、Web、Drive 四类应用的标准化基准
- 📌 **结论**：单阶段植入的触发器可跨多步持久传播：GPT 骨干上 planning 攻击持久率 43.58%、memory 77.97%、tool 阶段 60.28%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents execute tasks through multi-step workflows that combine planning, memory, and tool use. While this design enables autonomy, it also expands the attack surface for backdoor threats. Backdoor triggers injected into specific stages of an agent workflow can persist through multiple intermediate states and adversely influence downstream outputs. However, existing studies remain fragmented and typically analyze individual attack vectors in isolation, leaving the cross-stage interaction and propagation of backdoor triggers poorly understood from an agent-centric perspective. To fill this gap, we propose \textbf{BackdoorAgent}, a modular and stage-aware framework that provides a unified, agent-centric view of backdoor threats in LLM agents. BackdoorAgent structures the attack surface into three functional stages of agentic workflows, including \textbf{planning attacks}, \textbf{memory attacks}, and \textbf{tool-use attacks}, and instruments agent execution to enable systematic analysis of trigger activation and propagation across different stages. Building on this framework, we construct a standardized benchmark spanning four representative agent applications: \textbf{Agent QA}, \textbf{Agent Code}, \textbf{Agent Web}, and \textbf{Agent Drive}, covering both language-only and multimodal settings. Our empirical analysis shows that \textit{triggers implanted at a single stage can persist across multiple steps and propagate through intermediate states.} For instance, when using a GPT-based backbone, we observe trigger persistence in 43.58\% of planning attacks, 77.97\% of memory attacks, and 60.28\% of tool-stage attacks, highlighting the vulnerabilities of the agentic workflow itself to backdoor threats. To facilitate reproducibility and future research, our code and benchmark are publicly available at GitHub.

</details>

### 33. MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2607.14651)　📅 2026-07

**关键词**：`benchmark`、`compositional poisoning`、`dormant corruption`、`defense frontier`

👤 **作者**：Jifeng Gao、…、Sanglu Lu

- 🎯 **研究动机**：持久外部记忆可被注入并跨轮保留、之后扭曲下游行为，写时防御对组合式与休眠式投毒的盲区未知
- 🔬 **研究方法**：构建 MemPoison：1,227 个人工验证案例跨四类攻击、三种注入通道、三种记忆基底，评估十个模型家族；三级分类（L1 单记录直接、L2 多记录组合、L3 上下文触发休眠），并做机制影响分解
- 📌 **结论**：写时一致性检查显著压制 L1 却无法可靠压制 L2/L3；看似良性的记录可经联合检索组合或触发条件激活变害，需从静态过滤转向上下文敏感防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

</details>

### 34. Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2607.14611)　📅 2026-07

**关键词**：`benchmark`、`memory file`、`multi-session injection`、`coding agent`

👤 **作者**：Soham Gadgil、David Alexander、Sai Sunku、Franziska Roesner

- 🎯 **研究动机**：持久记忆文件使 prompt injection 可跨会话潜伏，其对 Anthropic Claude Code 与 OpenAI Codex 等真实系统的威胁未量化
- 🔬 **研究方法**：在沙箱合成工作区评估两个 agent 系统、四个模型（Claude Haiku 4.5、Opus 4.7、GPT-5.2、GPT-5.5），研究外部内容覆写记忆的难度与已植入载荷的持续攻击
- 📌 **结论**：让 agent 覆写自身记忆困难，但已植入记忆文件的载荷能成功攻击当前与未来会话；攻击成功率与载荷持久性随系统、模型、目标与多会话序列大幅变化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases. While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections in which malicious instructions can be embedded within persistent files and influence future behavior. In this work, we study prompt injection attacks in memory-based agentic systems using a sandboxed synthetic workspace. We evaluate two agentic systems, Anthropic Claude Code and OpenAI Codex, across four models: Claude Haiku 4.5, Claude Opus 4.7, GPT-5.2, and GPT-5.5. Our results show that although it is difficult to make an agent overwrite its own memory files using untrusted external content, payloads already planted in those files can successfully attack current and future sessions. Attack success and payload persistence vary substantially across systems, models, adversarial goals, and multi-session attack sequences. These findings show that persistent memory changes the threat model for prompt injection and motivate defenses that protect memory updates without removing useful agent adaptation.

</details>

### 35. Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts

📄 [arXiv](https://arxiv.org/abs/2606.29279)　📅 2026-06

**关键词**：`analysis`、`memory consolidation`、`confidence laundering`、`source redundancy`

👤 **作者**：Alex Kwon

- 🎯 **研究动机**：记忆巩固（mem0、LangMem 等）把对话改写为存储事实供后续信任使用，该改写会制造置信度且无需攻击者
- 🔬 **研究方法**：在构造的 agent 设定中量化记忆改写对请求授权的影响，隔离来源归因、措辞置信度与证据语域的作用，并测试常见修复
- 📌 **结论**：随口对冲性言论被存为带日期的确定断言并被执行；agent 响应的是措辞置信度而非来源，被动 unverified 标签被忽略而主动不信任指令会误伤正确记忆；保留原始措辞并增加冗余源才能恢复正确决策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents carry conclusions across steps and sessions in compressed memory, and memory products (e.g., mem0, LangMem) rewrite conversation into stored "facts" that later steps trust. We show this rewriting manufactures confidence: across our constructed agent settings, a casual, hedged remark becomes a confident, dated assertion the agent then obeys like a verified fact, granting every above-clearance request it faces. No attacker is needed: a role that was true once and never corrected is stored as a flat fact and acted on like a deliberate injection. We then isolate what the agent responds to. It is not the source: attributed, unattributed, and even forged "system of record" claims all grant alike. It is the confidence of the phrasing. A hedge is discounted, a flat assertion is obeyed, and this holds with no special keyword. Not all hedges are equal, though: the evidential register is the least-discounted, with "reportedly" obeyed like a flat assertion on most models. The obvious fixes fail. A passive "unverified" tag is ignored, and an active "do not trust this" instruction escalates even correct memory, so it is safe only by refusing to decide. The real fix lives in the store: keep the tentative phrasing rather than upgrade it. But that is hygiene, not a defense against an attacker who can simply write a confident lie. The deployable lesson is narrower and constructive: a single load-bearing memory is the hazard, and one redundant source restores correct decisions. We release the harness and demonstrations.

</details>

### 36. Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering

📄 [arXiv](https://arxiv.org/abs/2606.29030)　📅 2026-06

**关键词**：`analysis`、`memory manipulation`、`MCQ`、`controlled study`

👤 **作者**：Shahnewaz Karim Sakib、Anindya Bijoy Das

- 🎯 **研究动机**：agent 记忆中的信息可在当前查询干净时仍影响输出，记忆操纵对选择题问答的影响未经受控研究
- 🔬 **研究方法**：实现带外部记忆的 LLM agent，注入误导或损坏记忆，受控对比操纵前后的答案准确率、ASR 与被操纵选项选择率
- 📌 **结论**：即使简单的记忆操纵也显著改变最终答案，agent 在收到干净格式良好的问题时仍选择错误选项

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents extend conventional large language model (LLM) applications by integrating language understanding with task execution, external tool use, and memory mechanisms. While memory allows agents to retain prior interactions and provide more personalized and context-aware responses, it also introduces a new vulnerability: information stored in memory can influence future outputs even when the current query is clean. In this paper, we investigate memory manipulation in LLM-based agents for multiple-choice question answering. We first design and implement an LLM-based AI agent with an external memory component that stores and retrieves task-relevant information. We then introduce basic memory manipulation scenarios in which misleading or corrupted memories are inserted into the agent before it answers multiple-choice questions. Using a controlled experimental setup, we compare the agent's performance before and after memory manipulation and measure changes in answer accuracy, attack success rate, and selection of manipulated options. Our results show that even simple memory manipulations can noticeably affect the agent's final answers, causing it to select incorrect options despite receiving clean and well-formed questions.

</details>

### 37. From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.04329)　📅 2026-06

**关键词**：`analysis`、`MPBench`、`write channels`、`threat taxonomy`

👤 **作者**：Pritam Dash、Tongyu Ge、Aditi Jain、Tanmay Shah、Zhiwei Shang

- 🎯 **研究动机**：持久记忆使单次恶意写入可长期影响 agent 行为，但记忆投毒缺乏系统研究
- 🔬 **研究方法**：识别 4 条记忆写入通道与 9 个结构漏洞，构建 6 类攻击分类法，并设计 MPBench 基准评估记忆投毒
- 📌 **结论**：写读越激进的 agent 越易被利用，现有 prompt injection 防御无法覆盖记忆投毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance. However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior. We present a systematic study of memory poisoning in LLM-based agents. We identify four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture that make these channels exploitable. Based on these vulnerabilities, we develop a taxonomy of six classes of memory poisoning attacks. Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable. We also show that existing prompt injection defenses fail to cover memory poisoning attacks. Our findings provide a foundation for understanding and mitigating memory poisoning attacks against AI agents.

</details>

### 38. Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.17830)　📅 2026-05

**关键词**：`benchmark`、`temporal contamination`、`trigger-probe`、`longitudinal safety`

👤 **作者**：Ahmad Al-Tawaha、Shangding Gu、Peizhi Niu、Ruoxi Jia、Ming Jin

- 🎯 **研究动机**：记忆型 agent 安全评测只测单任务内安全性，忽略早期任务累积的记忆对后续无关任务的影响
- 🔬 **研究方法**：提出 temporal memory contamination 与 trigger-probe 协议：固定 probe 集对不同前缀长度的只读记忆快照评测，NullMemory 反事实基线隔离记忆诱发违规
- 📌 **结论**：记忆诱发违规率随暴露长度稳健上升且由累积内容而非顺序驱动；风险在生成前即可从检索状态高召回检出——记忆安全是需要时序评测的纵向属性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations of memory-equipped LLM agents typically measure within-task safety: whether an agent completes a single scenario safely, often under adversarial conditions such as prompt injection or memory poisoning. In deployment, however, a single agent serves many independent tasks over a long horizon, and memory accumulated during earlier tasks can affect behavior on later, unrelated ones. Studying this regime requires evaluation along the temporal dimension across tasks: not whether an agent is safe at any single memory state, but how its safety profile changes as memory accumulates across many independent interactions. We call this failure mode temporal memory contamination. To isolate memory exposure from stream non-stationarity, we introduce a trigger-probe protocol that evaluates a fixed probe set against read-only memory snapshots at varying prefix lengths, together with a NullMemory counterfactual baseline for identifying memory-induced violations. We apply this protocol across three deployment scenarios spanning records, memos, forms, and email correspondence and eight memory architectures, and additionally on Claw-like AI agents, such as OpenClaw, using the platform's native memory mechanism. Memory-enabled agents consistently exceed the NullMemory baseline, and memory-induced violation rates show a robust upward trend with exposure length on both agent classes. Order-randomization experiments indicate that the effect is driven primarily by accumulated content rather than encounter order. Finally, a structural consequence of the event decomposition is that memory-induced risk is detectable from retrieval state before generation, which we confirm with a high-recall diagnostic monitor. Our results argue for treating memory safety as a longitudinal property that requires temporal evaluation, not a single-state property that can be captured by a snapshot.

</details>

### 39. The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems

📄 [arXiv](https://arxiv.org/abs/2605.22842)　📅 2026-05

**关键词**：`analysis`、`trust laundering`、`causal attribution`、`shared memory`

👤 **作者**：Tanzim Ahad、Ismail Hossain、Md Jahangir Alam、Sai Puppala、Syed Bahauddin Alam、Sajedul Talukder

- 🎯 **研究动机**：记忆层攻击产生的行为与模型失效不可区分，防御者会错误归因于模型错位（Misattribution Gap）
- 🔬 **研究方法**：形式化 Semantic Norm Drift：策略格式文档经正常上传进入共享向量库，经 Trust Laundering Chain 丢失来源后以可信系统上下文重现；提出反事实组合测试与记忆持久信息流控制
- 📌 **结论**：64 起记录在案的事故中归因系统全怪模型，四个安全分类器在 510 个检查点零检出；CCT 以 87.5% 准确率、零误报定位因果入口，信息流控制阻断 97% 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent AI pipelines typically assume that agent misconduct originates from model misalignment. We identify a structural failure in this assumption, the \emph{Misattribution Gap}, where memory-layer attacks produce behaviors indistinguishable from model failure, causing defenders to apply the wrong remediation. We formalize \emph{Semantic Norm Drift} (SND) as a third path to agent misconduct, distinct from emergent misalignment and collusion. In SND, a policy-formatted document enters a shared vector store through normal uploads and later reappears as trusted system context after provenance is lost through a Trust Laundering Chain. Across 64 documented failures, attribution systems consistently blamed the model. Four safety classifiers, including one trained on memory poisoning, produced zero detections across 510 checkpoints. In 59 of 65 valid cases, agents explicitly cited the injected document as normative authority before complying. The attack requires no trigger, model access, or repeated interaction, achieves full effect within five sessions, and persists indefinitely. We introduce Counterfactual Composition Testing, which identifies the causal entry with 87.5% accuracy and zero false positives, while a forensics baseline fails across all 25 scenarios. We further prove the Retrieval-Coverage Dilemma, showing that stronger evasion inherently weakens the attack, limiting adaptive bypass strategies. Finally, we propose Memory-Persistent Information-Flow Control, which blocks 97% of attacks at the cross-session boundary where prior defenses fail. We release the SND Corpus, the first adversarial memory benchmark with temporal persistence and multi-agent composition across financial and Health Care domains.

</details>

### 40. No Attacker Needed: Unintentional Cross-User Contamination in Shared-State LLM Agents

📄 [arXiv](https://arxiv.org/abs/2604.01350)　📅 2026-04

**关键词**：`analysis`、`non-adversarial contamination`、`shared state`、`scope confusion`

👤 **作者**：Tiankai Yang、…、Yue Zhao

- 🎯 **研究动机**：共享状态 agent 中单用户局部有效的信息被无作用域复用会损害其他用户，该非对抗性污染未被研究
- 🔬 **研究方法**：形式化 unintentional cross-user contamination，提出三类污染分类法并在两种共享状态机制下做受控评测
- 📌 **结论**：仅良性交互即使原始共享状态产生 57-71% 污染率；写入时净化对对话态有效，但对可执行工件残留大量风险，表现为静默错误答案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents increasingly operate across repeated sessions, maintaining task states to ensure continuity. In many deployments, a single agent serves multiple users within a team or organization, reusing a shared knowledge layer across user identities. This shared persistence expands the failure surface: information that is locally valid for one user can silently degrade another user's outcome when the agent reapplies it without regard for scope. We refer to this failure mode as unintentional cross-user contamination (UCC). Unlike adversarial memory poisoning, UCC requires no attacker; it arises from benign interactions whose scope-bound artifacts persist and are later misapplied. We formalize UCC through a controlled evaluation protocol, introduce a taxonomy of three contamination types, and evaluate the problem in two shared-state mechanisms. Under raw shared state, benign interactions alone produce contamination rates of 57--71%. A write-time sanitization is effective when shared state is conversational, but leaves substantial residual risk when shared state includes executable artifacts, with contamination often manifesting as silent wrong answers. These results indicate that shared-state agents need artifact-level defenses beyond text-level sanitization to prevent silent cross-user failures.

</details>

### 41. Memory Poisoning Attack and Defense on Memory Based LLM-Agents

📄 [arXiv](https://arxiv.org/abs/2601.05504)　📅 2026-01

**关键词**：`analysis`、`MINJA robustness`、`EHR agent`、`trust-aware retrieval`

👤 **作者**：Balachandra Devarangadi Sunil、Isheeta Sinha、Piyush Maheshwari、Shantanu Todmal、Shreyan Mallik、Shuchi Mishra

- 🎯 **研究动机**：MINJA 等记忆投毒在理想条件下成功率极高，但真实部署下的攻击鲁棒性与有效防御缺乏研究
- 🔬 **研究方法**：在 MIMIC-III 临床数据的 EHR agent 中，从初始记忆状态、指示 prompt 数与检索参数三维度系统评测攻击，并提出复合信任评分的输入输出审核与带时间衰减、模式过滤的信任感知检索净化两类防御
- 📌 **结论**：真实预存的良性记忆会显著削弱攻击效果；有效净化需精细校准信任阈值，否则要么过度拒绝要么漏检微妙攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents equipped with persistent memory are vulnerable to memory poisoning attacks, where adversaries inject malicious instructions through query only interactions that corrupt the agents long term memory and influence future responses. Recent work demonstrated that the MINJA (Memory Injection Attack) achieves over 95 % injection success rate and 70 % attack success rate under idealized conditions. However, the robustness of these attacks in realistic deployments and effective defensive mechanisms remain understudied. This work addresses these gaps through systematic empirical evaluation of memory poisoning attacks and defenses in Electronic Health Record (EHR) agents. We investigate attack robustness by varying three critical dimensions: initial memory state, number of indication prompts, and retrieval parameters. Our experiments on GPT-4o-mini, Gemini-2.0-Flash and Llama-3.1-8B-Instruct models using MIMIC-III clinical data reveal that realistic conditions with pre-existing legitimate memories dramatically reduce attack effectiveness. We then propose and evaluate two novel defense mechanisms: (1) Input/Output Moderation using composite trust scoring across multiple orthogonal signals, and (2) Memory Sanitization with trust-aware retrieval employing temporal decay and pattern-based filtering. Our defense evaluation reveals that effective memory sanitization requires careful trust threshold calibration to prevent both overly conservative rejection (blocking all entries) and insufficient filtering (missing subtle attacks), establishing important baselines for future adaptive defense mechanisms. These findings provide crucial insights for securing memory-augmented LLM agents in production environments.

</details>

### 42. Proof-of-Execution Memory: Defending LLM Agents Against Forged-Reasoning Attacks by Verifying What Actually Happened

📄 [arXiv](https://arxiv.org/abs/2608.16032)　📅 2026-08

**关键词**：`defense`、`tamper-evident ledger`、`forged reasoning`、`action verification`

👤 **作者**：Md Habibur Rahman、Jaeho Kim

- 🎯 **研究动机**：FARMA 伪造推理记忆声称安全步骤已完成；SENTINEL 基于可疑措辞列表的防御可被改写绕过且差距比声称更糟
- 🔬 **研究方法**：先证明让 LLM 自动改写伪造即可首次尝试绕过 SENTINEL（保护归零，强模型上攻击 98-100%）；PoEM 不检查记忆，改用仅可信动作层可写的 HMAC 链式防篡改执行账本，账本确认真实执行才允许跳过
- 📌 **结论**：三模型三场景把 ASR 降至 0%、九格中八格零误报（其一 1.7%），而 SENTINEL 误拦 33-50% 合法操作；开销微秒级且可直接用于真实 LangChain agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are stateless and rely on external memory to carry context between steps. Because agents treat that memory as trustworthy, an adversary who can write to it can steer their behavior. The FARMA attack does this with no malicious command: it inserts fabricated entries into the agent's reasoning memory claiming a required safety step is already done, so the agent skips it. SENTINEL, the defense proposed with FARMA, scores entries against a fixed list of suspicious wordings; its authors note that an attacker who knows the list can reword the forgery and evade it, and leave this open. We show the gap is worse than stated. An automated attacker that simply asks a language model to reword the forgery evades SENTINEL on its first try, reducing its protection to zero on every model tested. We also find a capability paradox: the attack succeeds far more often on stronger models (98-100% on GPT-4o and GPT-4o-mini) than on Llama-3.1-8B (44%), because more capable agents follow reworded claims more faithfully, so the threat grows with capability. We propose Proof-of-Execution Memory (PoEM), which does not inspect memory at all. PoEM keeps a separate, tamper-evident, HMAC-chained ledger of the safety steps that actually executed, writable only by the trusted action layer, and allows a skip only if the ledger confirms real execution. An attacker can change what memory says but cannot forge a ledger entry for a step that never ran, so rewording no longer helps. Across three models and three scenarios, PoEM drives attack success to 0% while leaving legitimate operation intact (0% false positives in eight of nine cells, 1.7% in the ninth, within sampling noise), whereas SENTINEL wrongly blocks 33-50% of legitimate operations. PoEM also withstands attacks aimed at itself, adds microseconds of overhead, and works unchanged in a real LangChain agent. PoEM protects exactly the decisions it gates.

</details>

### 43. From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

📄 [arXiv](https://arxiv.org/abs/2608.10502)　📅 2026-08

**关键词**：`defense`、`dependency graph`、`selective rollback`、`state repair`

👤 **作者**：Caili Yu、…、Taotao Cai

- 🎯 **研究动机**：记忆 agent 出错后，删除源记忆留下已传播的声明与衍生记忆，全量重置则毁掉良性状态并重复计算
- 🔬 **研究方法**：形式化失败后记忆恢复问题；从运行时溯源构建类型化记忆-动作图，追踪下游依赖、保留有独立可信支持的候选、停用无支持状态并选择性重放受影响计算
- 📌 **结论**：150 例受控基准恢复率 85.3%（次优 77.3%），移除全部故障记忆且保留全部良性记忆；LongMemEval-V2 适配子集 68.0% 对比 54.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent memory writes. Existing defenses mainly detect or delete suspicious memories, or revise the current response. Deleting the source leaves already propagated claims, actions, and derived memories active, whereas resetting the store or replaying the full trace destroys benign state and repeats unnecessary computation. We therefore formulate \textbf{post-failure memory recovery: } \textit{given a failed execution and diagnosed faulty memories, recover both the answer and persistent state while retaining unaffected work.} Our \textbf{dependency-guided rollback repair} builds a typed memory-to-action graph from runtime provenance, traces explicit downstream dependencies, preserves candidates with independent trusted support, deactivates unsupported memory state, and selectively replays only answer-relevant affected computation. We evaluate this approach on a 150-case controlled benchmark spanning three tool-use domains and four memory failure types, and on a 50-case trajectory-derived stress test adapted from LongMemEval-V2. On the controlled benchmark, it achieves 85.3\% recovery versus 77.3\% for the best competing recovery method, removes all diagnosed faulty memories, preserves all benign memories, and requires only selective replay with modest LLM-call cost. On the adapted subset, it reaches 68.0\% recovery versus 54.0\% for the next best method, while also achieving the highest claim invalidation F1, 0.669 versus 0.603. Overall, the results do not imply uniformly better trace reconstruction, but show that dependency-guided rollback repair provides a strong recovery--cost trade-off while repairing faulty memory state and preserving benign memory.

</details>

### 44. MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory

📄 [arXiv](https://arxiv.org/abs/2608.02843)　📅 2026-08

**关键词**：`defense`、`authorized mutation`、`signed transition`、`tamper evidence`

👤 **作者**：Walid Saidi

- 🎯 **研究动机**：持久 agent 记忆的可变权重造成归因难题：审查者难以区分授权变更与数据库篡改
- 🔬 **研究方法**：MutMem 记录签名正负结果证据，每次权重变更提交为管家授权转换：绑定溯源节点、签名纪元、量化新旧权重与双 SHA-256 承诺，Ed25519 双端验证
- 📌 **结论**：LongMemEval 500 题答对 91.8%；N=100 PoisonedRAG 适配中投毒 0/100 进入 top-5、目标攻击成功率 1.02%；签名转换中位延迟 4.865ms

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized adaptation from database tampering. We present MutMem, an authorized-mutation protocol in HOM-AIMOS, a persistent agent-memory engine. MutMem retains memory content, records signed positive and negative outcome evidence without age-based expiry, and commits each nontrivial weight change as a housekeeper-authorized transition. Each transition binds a terminal provenance node, signer epoch, quantized old and new weights, a no-fork predecessor, and two domain-separated SHA-256 commitments. Ed25519 verification runs in both the database writer and a portable verifier. Content classified as poison-likely is retained with signed, revisable labels used by recall as trust evidence. We evaluate utility, mutation integrity, and poisoning adaptation. HOM-AIMOS answers 459/500 LongMemEval questions correctly under LLM judgment (91.8%). On LoCoMo, it obtains 74.12% judged accuracy and, under a separate upstream-compatible protocol, 58.20 token F1. A native suite passes all declared authorization, topology, tamper, signer-epoch, and post-mutation-recall cases; median signed-transition latency is 4.865 ms. In a declared N=100 PoisonedRAG adaptation, no injected poison appears in attacked top-5 disclosures (0/100; 95% Wilson upper bound 3.70%), while induced target-answer attack success among 98 clean-negative targets is 1/98 (1.02%). A preregistered four-arm ablation attributes the retrieval reduction to signed stored labels: the retriever selects poison for 94/100 targets when epistemic policy is bypassed and 0/100 when labels are restored. MutMem provides evidence of integrity, authorization, traceability, and historical continuity; it does not establish content truth.

</details>

### 45. MAPLE-Guard: Memory-Aware Link Enforcement Against Memory-Link Poisoning in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.00426)　📅 2026-08

**关键词**：`defense`、`shared memory`、`promotion gate`、`cross-agent propagation`

👤 **作者**：Wenjun Xiong、…、Muning Wen

- 🎯 **研究动机**：多智能体共享记忆可被一次投毒后持续检索、晋升并跨 agent 复用，现有防护只查 prompt、动作或通信边
- 🔬 **研究方法**：MAPLE-Guard 监控记忆生命周期，在写入、检索、晋升、跨 agent 复用四处设门，隔离风险记忆并阻断投毒进入共享记忆
- 📌 **结论**：LongMemEval 上 ASR 从 38.2% 降至 0.9%，AppWorld 上从 34.7% 降至 0.2%；MDSR 分别升至 74.3% 与 99.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems (MAS) increasingly rely on persistent private and shared memories for long-horizon coordination. This memory layer improves continuity, but it also gives attackers a durable channel: a poisoned memory can be written once, continuously retrieved in later tasks, promoted into shared memory, and reused by other agents. A single poisoned write can therefore steer many later decisions and contaminate agents that never saw the original attack, all while no malicious message crosses a visible communication edge at the moment of harm. Further, because existing safeguards mainly inspect prompts, actions, or communication edges, they can miss attacks whose content appears benign at write time but becomes harmful after retrieval. We introduce Memory-Aware Propagation and Link Enforcement Guard, MAPLE-Guard, a memory-link guard for memory-enabled MAS. MAPLE-Guard monitors the memory lifecycle and places gates at write, retrieval, promotion, and cross-agent reuse, so risky memories can be quarantined, unsafe retrievals filtered, and poisoned private memories blocked before they enter shared memory. In the main evaluation, MAPLE-Guard lowers attack success rate (ASR) from 38.2% to 0.9% on LongMemEval and from 34.7% to 0.2% on AppWorld; it also raises multi-agent defense success rate (MDSR) from 54.0% to 74.3% and from 42.5% to 99.8% on the same benchmarks. These results suggest that memory-aware link enforcement covers a gap left by prompt-level and topology-level defenses. Code is available at the link: https://github.com/xiong-wenjun/MAPLE-Guard.

</details>

### 46. Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory

📄 [arXiv](https://arxiv.org/abs/2607.29167)　📅 2026-07

**关键词**：`defense`、`provenance laundering`、`authority cap`、`tool gate`

👤 **作者**：Jinghan Xu、Yiyong Xiao、Wanru Shao、Hankai Liu、Xinjin Li

- 🎯 **研究动机**：LLM 记忆整合可把不可信外部观察重写为用户历史，抹除低信任来源，现有 prompt 过滤与工具防护不检查来源权限放大
- 🔬 **研究方法**：形式化记忆溯源洗钱问题，提出 PPMF 轻量中间件，保留平台维护的溯源并按动作风险与相关记忆权限匹配来授权工具调用
- 📌 **结论**：溯源缺失时 ASR 最高达 1.000；PPMF 门控下所有未授权高风险动作均被拦截，确认良性动作与低风险记忆使用不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authority. Existing prompt filters, content sanitizers, and tool guards do not enforce source-authority non-amplification after lossy memory consolidation. We formalize this boundary and instantiate it as Provenance-Preserving Memory Fire wall (PPMF), a lightweight memory middleware that preserves platform-maintained provenance and authorizes tool calls by matching action risk to the authority of action-relevant memories. In our schema-grounded evaluation with fixed risk policies, vulnerable consolidated memories reach up to 1.000 attack success rate(ASR); with intact platform-maintained provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the PPMF gate while confirmed benign actions and targeted low-risk memory use remain executable.

</details>

### 47. MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck

📄 [arXiv](https://arxiv.org/abs/2607.28103)　📅 2026-07

**关键词**：`detection`、`intent-behavior relation`、`information bottleneck`、`lightweight defense`

👤 **作者**：Dongyi Liu、Haixing He、Xiaobao Wu、Jia Li

- 🎯 **研究动机**：agent 可能检索到攻击者投毒的记忆而偏离用户意图，已有防御计算开销高或受多轮上下文信息冗余拖累
- 🔬 **研究方法**：提出 MIND：用意图感知信息瓶颈从初始意图与逐轮行为提取紧凑意图-行为表示，保留跨轮攻击相关信号并过滤任务无关重复信息，轻量检测器据此识别恶意记忆
- 📌 **结论**：ReAct-StrategyQA 上 ASR-r 与 ASR-a 平均分别降低 55.4% 与 55.3%，准确率与延迟和无防御 agent 相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Our preliminary analysis reveals that benign and poisoned trajectories exhibit distinguishable relationships between the initial user intent and subsequent behavior. Building on this observation, MIND employs an intent-aware Information Bottleneck(IB) to extract compact intent--behavior representations from the initial intent and turn-level behavior. The IB preserves intent-relevant cross-turn attack signals while filtering task-irrelevant and repetitive information, and a lightweight detector identifies malicious memories from the resulting representations. As such, MIND mitigates information redundancy in multi-turn contexts while avoiding the overhead of repeated LLM auditing. Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency. Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.

</details>

### 48. Forensic Trajectory Signatures for Agent Memory Poisoning Detection

📄 [arXiv](https://arxiv.org/abs/2606.30566)　📅 2026-06

**关键词**：`detection`、`trajectory signature`、`runtime triage`、`deployment boundary`

👤 **作者**：Jun Wen Leong

- 🎯 **研究动机**：LLM agent 记忆投毒的行为不变量与部署边界需要刻画
- 🔬 **研究方法**：发现成功攻击必须在 email_send_email 前调用 memory_recall_fact 的强制转移不变量，构建规则与 19 维轨迹特征随机森林检测器，并以预注册实验（N=4,360、13 模型）划定部署边界
- 📌 **结论**：随机森林 AUC 0.9904，跨 9 模型留出 6/9 达 1.000；但良性记忆接地的发送也产生同签名（条件 FPR 100%），仅可作攻击前置条件配合收件人元数据门控，前缀变体 AUC 0.934 可实时分流

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We discover a behavioral invariant in LLM agents under persistent memory poisoning and characterize its deployment boundary. In architectures where retrieval is routed through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition mechanistically forced by the attack's information-retrieval dependency. A simple rule exploiting this invariant achieves AUC = 0.9563; a Random Forest over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993]). The signature is overdetermined within the poisoned-but-defended evaluation set: removing all recall-related features leaves AUC unchanged. Cross-model hold-out on 9 models (7B-120B) confirms AUC = 1.000 on 6/9 splits, and the invariant transfers to frontier models (GPT-4.1, GPT-4o) without retraining. [v2] A preregistered follow-up (N=4,360, 13 models) reveals a critical deployment boundary: benign memory-grounded sends produce the same recall_before_send signature, yielding 100% false positives conditional on recall_before_send=1 (unconditional benign FPR: 24.7-52.6% depending on recall protocol). The signature is a valid attack precondition, not a maliciousness predicate; standalone blocking is not viable, but gating with recipient metadata restores separation. A prefix-only variant achieves AUC = 0.934, enabling real-time triage.

</details>

### 49. Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees

📄 [arXiv](https://arxiv.org/abs/2606.24322)　📅 2026-06

**关键词**：`defense`、`origin-bound authority`、`provenance laundering`、`TLA+`

👤 **作者**：Yedidel Louck

- 🎯 **研究动机**：基于内容或派生历史的记忆权限信号均可被漂洗：经 agent 自身摘要、可信工具回显与伪造佐证把不可信来源洗白
- 🔬 **研究方法**：形式化记忆写-取-行动管线的可塑性并机器检验证明分离定理（内容/血缘防御不健全、写时来源绑定必要且充分），实现 TMA-NM 非可塑性信息流控制
- 📌 **结论**：八个前沿模型上已有防御恰在理论预测处失效（漂洗 ASR 最高 68%），TMA-NM 在全部模型与通道上直接与漂洗攻击 ASR 均 0% 且合法效用完整

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly rely on persistent long-term memory, which creates a critical vulnerability that we study here: memory poisoning. An adversary can store untrusted content in one session that later steers a consequential action, such as a payment, a setting change, or data exfiltration, in a future session. Existing defenses base a memory item's authority to act on either its content (detection or trust-scoring) or its derivation history (lineage). We show that both signals are malleable. An attacker can launder an untrusted origin through three channels specific to LLM agents: the agent's own summarization, a trusted-tool echo, and manufactured corroboration. Each makes the content look benign and breaks or flips its derivation edge to ``trusted.'' We formalize malleability for the memory write-retrieve-act pipeline and prove a machine-checked separation theorem. No content- or lineage-based defense is sound under laundering (T1), write-time origin binding is necessary (T2), and non-malleable origin-bound authority with Sybil-resistant corroboration-gated elevation is sufficient (T3). Our construction, TMA-NM (Tamper-evident Memory Authority, Non-Malleable), instantiates non-malleable information-flow control (IFC) for LLM-agent memory. A cross-defense, cross-attack, and cross-model benchmark over eight frontier models shows that existing defenses fail exactly where the theory predicts (up to 68% laundering attack-success), while TMA-NM reaches 0% attack success on both direct and laundering attacks across all models and channels, at full legitimate utility. We release the benchmark, harness, and machine-checked TLA+ models to support reproducibility.

</details>

### 50. When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense

📄 [arXiv](https://arxiv.org/abs/2606.22030)　📅 2026-06

**关键词**：`defense`、`Bayesian memory`、`reliability update`、`provenance cap`

👤 **作者**：Pranav Singh

- 🎯 **研究动机**：belief 式记忆何时优于朴素记忆存疑，且内容派生的可靠性可被操纵
- 🔬 **研究方法**：构建 Nous：实体-属性对以分类概率分布表示，闭式贝叶斯更新+信息论惊喜驱动信念修正；引入可靠性条件化更新与来源封顶的投毒防御
- 📌 **结论**：现有会话记忆基准少有矛盾证据时贝叶斯更新几乎无增益；在矛盾/可信度差异场景显著胜出，来源封顶抗大量投毒；另发现 token-F1 与 LLM-judge 评分间 27.5 分差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate when belief-based memory actually improves large language model (LLM) agents. Our vehicle is Nous, a long-term memory architecture that represents each entity-attribute pair as a categorical probability distribution updated through closed-form Bayesian inference, with information-theoretic surprise driving belief revision and entropy-based forgetting. A controlled ablation on the LoCoMo benchmark shows that Bayesian belief updating alone provides little benefit over naive last-write-wins because existing conversational memory benchmarks rarely contain contradictory or differently reliable evidence. We then introduce reliability-conditioned updating, estimating per-observation reliability from epistemic language, and show on a controlled contradiction benchmark that belief updating substantially outperforms last-write-wins and raw-memory retrieval when observations differ in trustworthiness. Because content-derived reliability is itself vulnerable to manipulation, we further propose provenance-capped belief updating, where trust is bounded by source provenance rather than textual confidence. Under controlled memory-poisoning experiments, this approach resists volumetric poisoning attacks while revealing the utility costs and implementation requirements of provenance-aware memory. Finally, we quantify a 27.5-point discrepancy between strict token-F1 and LLM-as-judge evaluation on identical outputs, highlighting important reproducibility concerns for long-term memory benchmarks. Our results suggest that probabilistic belief-based memory is most beneficial in environments requiring reasoning over conflicting and differently trustworthy evidence, rather than conventional conversational recall alone.

</details>

### 51. SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

📄 [arXiv](https://arxiv.org/abs/2606.12703)　📅 2026-06

**关键词**：`defense`、`signed memory`、`smoothed retrieval`、`certified robustness`

👤 **作者**：Tarun Sharma

- 🎯 **研究动机**：持久记忆 agent 面临 Multi-Session Memory Poisoning（仅经正常渠道注入记忆即影响后续用户），已有防御（RobustRAG 等静态语料假设）无认证保证
- 🔬 **研究方法**：提出 SMSR：写入时 HMAC-SHA256 来源签名阻断未签名注入，查询时随机记忆消融+verdict 投票并给出超几何认证界，证明无来源签名的检索期过滤不可认证
- 📌 **结论**：15 个企业场景 3,150 次试验：组件一把未签名攻击 ASR 从 93-100% 降到 0%；端到端查询式攻击从 65.3% 降至 5.3%，干净效用保持 85-90%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions. This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights or code. We call this Multi-Session Memory Poisoning (MSMP) and show that no existing defence certifies against it; static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base, and heuristic filters are bypassed by fluent enterprise-style text. We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting. Component 1 adds HMAC-SHA256 provenance at write time, blocking unsigned injection. Component 2 applies randomised memory ablation with verdict-based majority voting at query time, bounding the influence of authenticated adversaries. We prove that no provenance-free retrieval-time filter can certify against adaptive injection, derive a hypergeometric certificate for Component 2, and formalise the Consistent Minority Effect, whereby a consistent adversarial answer wins string-based voting as a numerical minority while verdict-based voting removes it. Across 15 enterprise scenarios (3,150 repeated trials), Component 1 cuts attack success from 93-100% to 0% for all unsigned variants. For an authenticated adversary with a single injection, Component 2 holds success to 8.0% (95% CI [5.8, 10.9], n=450), below the certified worst case. In an end-to-end query-only attack where the agent itself writes the poison rather than it being pre-seeded, SMSR reduces success from 65.3% to 5.3% (n=150, non-overlapping CIs) on a live agent stack. Clean-query utility is 90% (Component 1) and 85% (combined).

</details>

### 52. MemLineage: Lineage-Guided Enforcement for LLM Agent Memory

📄 [arXiv](https://arxiv.org/abs/2605.14421)　📅 2026-05

**关键词**：`defense`、`cryptographic provenance`、`derivation DAG`、`sensitive-action gate`

👤 **作者**：Ciyan Ouyang、Rui Hou

- 🎯 **研究动机**：不可信内容可写入持久 agent 状态并在后续 session 作为指令重现，难题是如何在保留记忆召回的同时阻止其正当化敏感动作
- 🔬 **研究方法**：MemLineage 把它当监管链问题：RFC-6962 Merkle 日志加每主体 Ed25519 签名条目，加权派生 DAG 记录影响关系，敏感动作门拒绝以外源祖先为依据的调度
- 📌 **结论**：三种记忆投毒 workload 下唯一把三列 ASR 全部压到零的配置，每操作开销亚毫秒；AgentDojo 桥接下严格 ASR 同样降为零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. Recent and concurrent work shows that untrusted content can be written into persistent agent state and re-enter later sessions as an instruction; the remaining systems question is how to preserve useful memory recall while preventing such state from justifying sensitive actions. MemLineage treats this as a chain-of-custody problem rather than a filtering problem. It is a six-module design around an RFC-6962 Merkle log over per-principal Ed25519-signed entries: a weighted derivation DAG records which retrieved entries influenced each new memory, and a max-of-strong-edges propagation rule makes Untrusted-Path Persistence hold for any chain whose attribution edges remain above threshold. The sensitive-action gate then refuses dispatches whose active justification descends from an external ancestor, while still allowing benign recall. We evaluate three defense cells against three memory-poisoning workloads on a deterministic mechanism-isolation harness; MemLineage is the only configuration in that harness that drives all three columns to zero ASR, while sub-millisecond per-operation overhead keeps it well below the noise floor of any LLM call. A Codex-backed AgentDojo bridge further separates strong-model behavior from defense-layer behavior: under an intentionally vulnerable tool-output profile, no-defense and signature-only baselines fail on all six banking pairs, while all MemLineage rows reduce strict AgentDojo ASR to zero. The core deterministic artifacts are byte-equal CI-verified; hosted-model AgentDojo and live-model sweeps are recorded as auditable logs rather than byte-pinned artifacts.

</details>

### 53. MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

📄 [arXiv](https://arxiv.org/abs/2605.23723)　📅 2026-05

**关键词**：`defense`、`post-hoc audit`、`counterfactual influence`、`consistency graph`

👤 **作者**：Zhewen Tan、…、Lin Sun

- 🎯 **研究动机**：现有记忆防御只做在线干预，不回答有害行为已发生后哪些存储记忆是致因的事后审计问题
- 🔬 **研究方法**：MemAudit 结合反事实记忆影响分（对有害输出的因果贡献）与记忆一致性图（结构异常）定位毒记忆
- 📌 **结论**：对 MINJA 攻击，QA 与 reasoning 设置的 ASR 分别从 70% 和 83.3% 降至 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution. However, this memory mechanism also creates a practical security vulnerability: an adversarial user may inject malicious records into the agent's memory through ordinary interaction, and these records can later be retrieved to steer the agent's reasoning and actions. Existing defenses primarily focus on online intervention, such as prompt filtering or output blocking, but they do not address the post-hoc question of which stored memories are responsible after harmful behavior has already been observed. We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. The framework combines two complementary signals: (1) a counterfactual memory influence score that measures each memory's causal contribution to harmful outputs, and (2) a memory consistency graph that identifies structurally anomalous memories within the broader memory store. We evaluate MemAudit against MINJA, a query-only memory injection attack in which malicious records are generated and stored through normal agent interactions rather than direct memory-bank modification. Across both QA and reasoning-agent settings, MemAudit substantially reduces attack success rates under realistic post-hoc auditing scenarios. The results show that QA attack success is reduced from $70\%$ to $0\%$, while RAP attack success drops from $83.3\%$ to $0\%$.

</details>

### 54. MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents

📄 [arXiv](https://arxiv.org/abs/2605.03482)　📅 2026-05

**关键词**：`detection`、`semantic anomaly`、`certified radius`、`adaptive calibration`

👤 **作者**：Ishrith Gowda

- 🎯 **研究动机**：检索增强 agent 持久外部记忆的安全属性缺乏形式化刻画
- 🔬 **研究方法**：把记忆投毒形式化为 Stackelberg 博弈；MEMSAD 基于梯度耦合定理（连续扰动降低检测风险必然损害检索排名）做校准式异常检测，附认证检测半径与 minimax 最优性证明
- 📌 **结论**：修正评测协议后 ASR-R 从 0.25 升到 1.00；复合防御 TPR 1.00、FPR 0.00，但同义替换可完全绕过，暴露连续空间防御的边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent external memory enables LLM agents to maintain context across sessions, yet its security properties remain formally uncharacterized. We formalize memory poisoning attacks on retrieval-augmented agents as a Stackelberg game with a unified evaluation framework spanning three attack classes with escalating access assumptions. Correcting an evaluation protocol inconsistency in the triggered-query specification of Chen et al. (2024), we show faithful evaluation increases measured attack success by $4\times$ (ASR-R: $0.25 \to 1.00$). Our primary contribution is MEMSAD (Semantic Anomaly Detection), a calibration-based defense grounded in a gradient coupling theorem: under encoder regularity, the anomaly score gradient and the retrieval objective gradient are provably identical, so any continuous perturbation that reduces detection risk necessarily degrades retrieval rank. This coupling yields a certified detection radius guaranteeing correct classification regardless of adversary strategy. We prove minimax optimality via Le Cam's method, showing any threshold detector requires $Ω(1/ρ^2)$ calibration samples and MEMSAD achieves this up to $\log(1/δ)$ factors. We further derive online regret bounds for rolling calibration at rate $O(σ^{2/3}Δ^{1/3})$, and formally characterize a discrete synonym-invariance loophole that marks the boundary of what continuous-space defenses can guarantee. Experiments on a $3 \times 5$ attack-defense matrix with bootstrap confidence intervals, Bonferroni-corrected hypothesis tests, and Clopper-Pearson validation ($n=1{,}000$) confirm: composite defenses achieve TPR $= 1.00$, FPR $= 0.00$ across all attacks, while synonym substitution evades detection at $Δ$ ASR-R $\approx 0$, exposing a gap existing embedding-based defenses cannot close.

</details>

### 55. A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory

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
