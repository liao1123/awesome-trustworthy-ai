# 提示注入

## 研究方向

提示注入研究攻击者如何把恶意指令或对抗性证据嵌入网页、邮件、文档、工具输出或持久化 Agent 状态，从而劫持模型后续行为；重点包括跨会话攻击、文档解析差异、自动化红队、工具调用归因、实际应用风险与运行时防御。

## 研究脉络

- **攻击起点：** Prompt injection 最初通过单轮指令冲突覆盖系统或开发者意图。
- **攻击面扩展：** 攻击随后发展到 indirect、multimodal 和 cross-session stored injection。
- **防御与评测：** 防御由持续对抗训练扩展到 tool-call causal attribution 与可证明信息隔离，公开竞赛和自动 red-teaming 用于检验 adaptive attack。

## 攻击与真实系统风险

### 1. Will the User Ever Know? Covert Indirect Prompt Injection on Tool-Using LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.30362)　📅 2026-09

**关键词**：`attack`、`covert indirect prompt injection`、`CSR/OSR`、`ReAct trajectory`

👤 **作者**：Yunseok Lee、Yunji Kim、Woojin Lee

- 🎯 **研究动机**：标准 ASR 只统计注入是否成功，忽略用户能否从 Agent 最终回复察觉攻击
- 🔬 **研究方法**：把成功拆为 covert（无痕迹）与 overt（可察觉）两类并提出 CSR／OSR 指标；ICoA 攻击在执行注入后把 Agent 引导回原用户任务以掩盖痕迹
- 📌 **结论**：ReAct 格式下最终回复只摘要最近动作，covert 轨迹因此先交还控制权；ICoA 在 AgentDojo 四个模型上 CSR 比最强基线高 3.79-12.01 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final response. Looking at successful injection traces, we find two distinct outcomes: the agent executes the injection while returning an otherwise normal response, or reports the injected action in its final response, giving the user a chance to notice. We call these covert and overt successes. From the user's perspective, we decompose ASR into the Covert Success Rate (CSR), counting successes leaving no trace in the final response, and the Overt Success Rate (OSR), counting successes the user can detect. To understand what drives the gap, we analyze successful trajectories and find that the agent's behavior after the injection separates covert from overt: covert traces hand control back to the user task before ending, while overt traces end at the attack itself. This split follows from the ReAct format, where the final response summarizes the most recent action. Building on this observation, we propose ICoA (Induced Covert Attack), an IPI attack designed to induce covert outcomes by steering the agent back to the user task after executing the injection. Across four target models on AgentDojo, ICoA achieves the highest CSR, with gains of 3.79-12.01 percentage points over the strongest baseline.

</details>

### 2. When Context Gets Root: Privilege Escalation in LLM Harnesses

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

### 3. Beyond the Editing Canvas: Evidence Divergence in OOXML-to-LLM Ingestion

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

### 4. InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

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

### 5. MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds

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

### 6. HijackKV: New Threat in Position-Independent KV Cache Reuse

📄 [arXiv](https://arxiv.org/abs/2607.19957) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi)　📅 2026-07　🏷 USENIX Security 2026

**关键词**：`attack`、`KV cache reuse`、`prompt injection`、`instruction hierarchy`、`context contamination`、`behavior hijacking`

👤 **作者**：Yichi Zhang、Zhiqi Wang、Huan Zhang、Yuchen Yang

- 🎯 **研究动机**：位置无关 KV 复用按文本块匹配而不论位置，KV 编码了原始上下文， benign 文本块的缓存可能携带攻击者前缀
- 🔬 **研究方法**：提出 HijackKV：优化攻击者前缀使后续常见良性文本块的 KV 编码攻击目标，文本本身不变以保证未来缓存命中
- 📌 **结论**：单次尝试平均成功率 94%，在低命中率（10%）与频繁重算（50%）下仍有效，跨轮持续、黑盒跨模型迁移，并给出安全 KV 复用系统设计建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Key-Value (KV) cache reduces inference latency in large language models (LLMs). Traditional prefix-based reuse has low cache hit rates across inference requests because it requires exact token and position matches. To improve efficiency, recent system optimizations introduce position-independent KV reuse, allowing KV cache to be reused whenever identical text chunks appear, regardless of their position in the sequence. We show this design introduces a new threat, KV Cache Hijacking. Since KV caches are retrieved by token match but encode the context in which they were originally computed, the KV tied to a benign-looking token chunk may encode an attacker-controlled prefix. When later reused in a victim query, this contaminated KV silently hijacks the model's behavior, even if no attacker-controlled text appears in the input. We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality. HIJACKKV optimizes an attacker-controlled prefix, so that the KV computed for a subsequent common benign text encodes the attacker's goal, while the text remains unchanged for future cache hits. HIJACKKV achieves an average 94% success rate in a single attempt, remains effective under realistic constraints including low hit rates (10%) and frequent recomputation (50%), persists over multi-turn interactions, and transfers across models in black-box settings. We further provide design insights for building secure KV reuse systems.

</details>

### 7. CPInj: Uncovering Prompt Injection Risks in Textual Collabo- rative Prompt Optimization

📄 [arXiv](https://arxiv.org/abs/2607.18622) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`attack`、`collaborative prompt optimization`、`prompt injection`、`instruction hierarchy`、`persistent contamination`

👤 **作者**：Xinting Liao、…、Xiaoxiao Li

- 🎯 **研究动机**：TCPO 多客户端自由文本聚合优化引入未探索攻击面：本地提示中的恶意指令可经服务器聚合传播
- 🔬 **研究方法**：提出 CPInj 攻击：污染聚合全局提示、降低下游任务性能、抵抗良性客户端提示净化并绕过服务器检测；并提出锚定净化聚合 APAgg 缓解
- 📌 **结论**：现有防御对 CPInj 无效；三个 LLM 家族、五个推理任务上攻击高度有效，APAgg 首步缓解后威胁仍远未解决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Textual Collaborative Prompt Optimization (TCPO) extends TextGrad (Yuksekgonul et al., 2025) to a decentralized setting by allowing multiple clients to jointly improve prompts for large language models (LLMs) while keeping their data locally. Its reliance on free-form textual updating and aggregation introduces a new and largely unexplored attack surface, i.e., malicious instructions can be injected into local prompts and propagated through server-side prompt aggregation. Unlike conventional prompt injection attacks, attacking TCPO targets the collaborative optimization loop in TCPO. This setting is more challenging because malicious instructions must survive aggregation, persist through subsequent benign prompt optimization, and evade server-side defenses. To expose this risk, we propose Collaborative Prompt Injection (CPInj) attack that contaminates the aggregated global prompt with malicious instructions, degrades downstream task performance, resists purification by prompt optimization on benign clients, and evades advanced detection-based defenses on the server. We find that current defense methods are ineffective against CPInj. We further propose Anchored Purification Aggregation (APAgg), a defense-oriented aggregation that purifies malicious instructions without severely degrading TCPO utility. We conduct extensive experiments across three LLM families and five reasoning tasks in math, logic, and medicine, and demonstrate that our proposed attack reveals a critical vulnerability in TCPO. Although we take a first step toward mitigation, the attack remains highly effective and far from fully resolved, calling for more robust defense for TCPO.

</details>

### 8. Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings

📄 [arXiv](https://arxiv.org/abs/2606.27287) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.142/)　📅 2026-06　🏷 ACL 2026

**关键词**：`attack`、`hiring-system injection`、`résumé injection`、`multi-injection`

👤 **作者**：Preet Baxi、Jiannan Xu、Jane Yi Jiang、Stefanus Jasin

- 🎯 **研究动机**：LLM 简历筛选中候选人注入自荐文本（不新增资质但影响评估）的操纵效应与公平风险未知
- 🔬 **研究方法**：受控实验研究单注入与多注入设定下提示注入对排名的影响，操纵简历质量同质性与注入比例
- 📌 **结论**：注入在质量同质且少数人注入时可靠提升排名，注入普及后效应崩塌；异质质量下低质候选人偶尔反超高质，引发公平担忧

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-promotional text that introduces no new qualifications but is designed to influence LLM evaluations. Using controlled experiments, we show that prompt injection reliably improves applicant rankings when résumé quality is homogeneous and few candidates inject. However, its effectiveness rapidly diminishes as more candidates inject, collapsing when manipulation becomes widespread. When candidate quality is heterogeneous, prompt injection is less effective on average, but can occasionally allow lower-quality candidates to outrank higher-quality ones, raising fairness concerns. Overall, LLM-based screening is most vulnerable when manipulation is rare and candidate quality differences are small. Code and resources are publicly available at: https://github.com/preetb1199/Prompt_Injection_ACL26

</details>

### 9. What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2606.04425)　📅 2026-06

**关键词**：`attack`、`agent prompt injection`、`stored injection`、`cross-session persistence`

👤 **作者**：Yuanbo Xie、…、Tingwen Liu

- 🎯 **研究动机**：agent 持久化状态（记忆、文件系统、工具）重塑安全边界，恶意指令可跨会话潜伏，传统单次交互视角失效
- 🔬 **研究方法**：提出 Cross-Session Stored Prompt Injection 威胁向量（类比存储型 XSS），形式化其生命周期，建立持久化通道与吸收机制分类法并构建沙箱工具包评估
- 📌 **结论**：agent 安全的核心挑战不是过滤不可信输入，而是治理外部信息穿越持久边界时如何获得权威，需从交互中心转向状态中心安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern agentic systems fundamentally reshape the security boundary of LLMs by introducing persistent system state including memories, filesystems, tools, and other long-lived contextual artifacts that survives across sessions. As external information crosses this boundary and becomes part of persistent agent state, malicious instructions are no longer confined to a single interaction, but can silently persist and influence future executions long after the original attacker interaction has ended. We introduce Cross-Session Stored Prompt Injection, a new threat vector inspired by stored cross-site scripting that redefines prompt injection for agentic systems by extending its threat model across both time, where attacks persist and activate across sessions, and space, where adversarial instructions propagate beyond the immediate prompt into persistent system state. To systematically characterize this emerging threat, we formalize the lifecycle of cross-session stored prompt injection, develop a taxonomy of persistence channels and incorporation mechanisms, and build a sandbox toolkit for evaluation. Our findings suggest that the fundamental challenge of agent security is not merely filtering untrusted inputs, but governing how external information acquires authority as it crosses persistent system boundaries. We hope this work motivates a broader shift from interaction-centric security toward state-centric security, making the secure management of persistent agent state a first-class security principle for the agentic era.

</details>

### 10. Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening

📄 [arXiv](https://arxiv.org/abs/2605.28999) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-mohan)　📅 2026-05　🏷 USENIX Security 2026

**关键词**：`attack`、`analysis`、`prompt injection`、`resume screening`、`instruction hierarchy`、`real-world measurement`

👤 **作者**：Mohan Zhang、…、Dawn Song

- 🎯 **研究动机**：prompt injection 漏洞多停留在概念演示，其在真实 LLM 应用中的流行度与影响未测
- 🔬 **研究方法**：基于 hireEZ 多年积累的约 20 万份真实简历，设计定制注入检测器（小规模人工验证高精度）并做大规模测量研究
- 📌 **结论**：约 1% 简历含隐藏注入，近一两年明显增多，超 90% 注入不使用显式指令——首次大规模实证真实 LLM 应用中的 prompt injection

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely unexplored. In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening. Our analysis is based on approximately 200K real-world resumes collected over multiple years by hireEZ. We first design tailored methods to detect prompt injection in resumes. Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors. We then apply our detector to the full resume dataset and conduct a comprehensive measurement study of real-world prompt injection attacks. Our analysis reveals several intriguing findings: approximately 1% of resumes contain hidden prompt injections; the prevalence of such injected resumes has increased noticeably over the past one to two years; and more than 90% of injected prompts do not use explicit instructions. These results provide the first evidence of large-scale prompt injection in real-world LLM-based applications and lay the groundwork for future studies to understand and mitigate such attacks.

</details>

### 11. The Vulnerability of LLM Rankers to Prompt Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2602.16752) · 🌐 [Project](https://doi.org/10.1145/3805712.3808553)　📅 2026-02　🏷 SIGIR 2026

**关键词**：`attack`、`ranker prompt injection`、`objective hijack`、`criteria hijack`、`LLM ranker`

👤 **作者**：Yu Yin、Shuai Wang、Bevan Koopman、Guido Zuccon

- 🎯 **研究动机**：候选文档内 prompt 注入可操纵 LLM 排序，但该脆弱性跨模型家族与设定的边界未探明
- 🔬 **研究方法**：在 pairwise/listwise/setwise 三种排序范式下系统评估目标劫持与准则劫持两种注入，度量 ASR 与 nDCG@10 影响
- 📌 **结论**：刻画了脆弱性边界条件，发现 encoder-decoder 架构对越狱注入具有固有强韧性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have emerged as powerful re-rankers. Recent research has however showed that simple prompt injections embedded within a candidate document (i.e., jailbreak prompt attacks) can significantly alter an LLM's ranking decisions. While this poses serious security risks to LLM-based ranking pipelines, the extent to which this vulnerability persists across diverse LLM families, architectures, and settings remains largely under-explored. In this paper, we present a comprehensive empirical study of jailbreak prompt attacks against LLM rankers. We focus our evaluation on two complementary tasks: (1) Preference Vulnerability Assessment, measuring intrinsic susceptibility via attack success rate (ASR); and (2) Ranking Vulnerability Assessment, quantifying the operational impact on the ranking's quality (nDCG@10). We systematically examine three prevalent ranking paradigms (pairwise, listwise, setwise) under two injection variants: decision objective hijacking and decision criteria hijacking. Beyond reproducing prior findings, we expand the analysis to cover vulnerability scaling across model families, position sensitivity, backbone architectures, and cross-domain robustness. Our results characterize the boundary conditions of these vulnerabilities, revealing critical insights such as that encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks. We publicly release our code and additional experimental results at https://github.com/ielab/LLM-Ranker-Attack.

</details>

### 12. Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems

📄 [arXiv](https://arxiv.org/abs/2601.07072) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`attack`、`indirect prompt injection`、`prompt injection`、`instruction hierarchy`、`retrieval optimization`、`data exfiltration`

👤 **作者**：Hongyan Chang、Ergute Bao、Xinjian Luo、Ting Yu

- 🎯 **研究动机**：既往间接 prompt injection 研究回避最难点——保证恶意内容被自然查询实际检索，真实影响不明
- 🔬 **研究方法**：把恶意内容分解为保证检索的触发片段与承载任意攻击目标的攻击片段，仅需嵌入模型 API 访问即可黑盒构造紧凑触发片段
- 📌 **结论**：11 个基准 8 个嵌入模型上检索率近 100%，单查询成本低至 0.21 美元；单封毒邮件即可让 GPT-4o 在多 agent 工作流中以超 80% 成功率外传 SSH 密钥，现有防御无法阻止恶意文本被检索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly rely on retrieving information from external corpora. This creates a new attack surface: indirect prompt injection (IPI), where hidden instructions are planted in the corpora and hijack model behavior once retrieved. Previous studies have highlighted this risk but often avoid the hardest step: ensuring that malicious content is actually retrieved. In practice, unoptimized IPI is rarely retrieved under natural queries, which leaves its real-world impact unclear. We address this challenge by decomposing the malicious content into a trigger fragment that guarantees retrieval and an attack fragment that encodes arbitrary attack objectives. Based on this idea, we design an efficient and effective black-box attack algorithm that constructs a compact trigger fragment to guarantee retrieval for any attack fragment. Our attack requires only API access to embedding models, is cost-efficient (as little as $0.21 per target user query on OpenAI's embedding models), and achieves near-100% retrieval across 11 benchmarks and 8 embedding models (including both open-source models and proprietary services). Based on this attack, we present the first end-to-end IPI exploits under natural queries and realistic external corpora, spanning both RAG and agentic systems with diverse attack objectives. These results establish IPI as a practical and severe threat: when a user issued a natural query to summarize emails on frequently asked topics, a single poisoned email was sufficient to coerce GPT-4o into exfiltrating SSH keys with over 80% success in a multi-agent workflow. We further evaluate several defenses and find that they are insufficient to prevent the retrieval of malicious text, highlighting retrieval as a critical open vulnerability.

</details>

### 13. Prompt Injection as Role Confusion

📄 [arXiv](https://arxiv.org/abs/2603.12277) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64605)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Charles Ye、Jasmine Cui、Dylan Hadfield-Menell

- 🎯 **研究动机**：提示注入机制不明：模型从文本听起来像谁而非标签角色判断来源
- 🔬 **研究方法**：设计角色探针测模型内部对说话者的感知；CoT Forgery 零样本攻击把伪造推理注入用户提示与工具输出
- 📌 **结论**：注入文本占据其模仿的信任角色的表示空间；前沿模型上 ASR 达 60%（基线近零）；角色混淆程度可在生成前预测攻击成败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs see the world as a single stream of text, partitioned into roles like <user> or <tool>. We trace prompt injection to role confusion: models perceive the source of text from how it sounds, not its labeled role. A command hidden in a webpage hijacks an agent simply because it sounds like <user> text, despite its <tool> label. We design role probes to measure how LLMs internally perceive "who is speaking", and find that injected text occupies the same representational space as the trusted role it imitates. We demonstrate this with CoT Forgery, a zero-shot attack that injects fabricated reasoning into user prompts and tool outputs. Models mistake the forgery for their own thoughts, yielding 60% attack success against frontier models with near-zero baselines. Strikingly, the degree of role confusion predicts attack success before a single token is generated. This mechanism generalizes beyond CoT Forgery to standard agent prompt injections, revealing prompt injection as a measurable consequence of role perception. To the model, sounding like a role is indistinguishable from being one.

</details>

### 14. CHAI: Command Hijacking against Embodied AI

📄 [arXiv](https://arxiv.org/abs/2510.00181) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-10　🏷 SaTML 2026

**关键词**：`attack`、`visual text perturbation`、`embodied LVLM`、`command hijacking`、`environmental prompt injection`、`visual command`

👤 **作者**：Luis Burbano、…、Alvaro A Cardenas

- 🎯 **研究动机**：具身 AI 的多模态语言理解能力带来物理环境间接 prompt 注入新风险
- 🔬 **研究方法**：提出 CHAI：在视觉输入中嵌入误导标志等自然语言指令，系统搜索 token 空间构建 prompt 字典并引导攻击模型生成 Visual Attack Prompts
- 📌 **结论**：在无人机紧急降落、自动驾驶、空中目标跟踪与真实机器人车场景均超 SoTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a physical environment indirect prompt injection attack that exploits the multimodal language interpretation abilities of AI models. CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents: drone emergency landing, autonomous driving, aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

</details>

### 15. Mind the Web: The Security of Web Use Agents

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

### 16. Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection

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

### 17. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

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

### 18. ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection

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

### 19. The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection

📄 [arXiv](https://arxiv.org/abs/2608.26423)　📅 2026-08

**关键词**：`analysis`、`detection`、`safeguard classifier`、`decision trust`、`heuristic shortcut`、`prompt-injection classifier`

👤 **作者**：Jaturong Kongmanee、Smile Thanapattheerakul

- 🎯 **研究动机**：safeguard classifier 的高置信判定可能依赖脆弱 shortcut，部署者不知哪些可信
- 🔬 **研究方法**：以维度优化分类器与 latent support vector 定位改变预测的 token，按单 token 攻击幅度构建诊断 taxonomy 分流输入
- 📌 **结论**：prompt injection 数据上约 77% 高置信判定不抗移除单个 token，分为校准失败与真实可利用 shortcut 两类

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy, consists of (i) constructing a dimensionality-optimized classifier, in which the embedding dimensionality is empirically selected via cross-validated performance rather than fixed a priori, (ii) locating a relatively small set of latent support vectors (~ 29% of total training examples) representing influential prompts for identifying tokens that alter the classifier's predicted labels, and (iii) utilizing such tokens and their associated attack magnitudes for constructing a diagnostic taxonomy. This diagnostic taxonomy provides an end-to-end guideline for flagging prompts that require different treatments: rely Safely on the classifier's decision; flag Heuristic Bias and Heuristic Override cases; route Insufficient Context cases for further human/safety review. Applying the framework to a classifier trained on a public prompt injection dataset, we find that a substantial fraction of its confident decisions (~ 77%) are not robust to removing a single token, and that this brittleness separates into two distinct failure patterns: a confidence calibration failure and a genuinely exploitable shortcut. For each zone of the taxonomy, we also recommend strategies for remediating diagnosed prompts. We illustrate the framework as a series of steps, demonstrating how each step operates.

</details>

### 20. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

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

### 21. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control

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

### 22. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

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

### 23. Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

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

### 24. Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution

📄 [arXiv](https://arxiv.org/abs/2608.21656)　📅 2026-08

**关键词**：`defense`、`RAG prompt injection`、`context sanitization`、`database leakage`、`retrieved-context injection`、`keyword-grounded facts`

👤 **作者**：Ziliang Zhang、…、Sheng Zhong

- 🎯 **研究动机**：prompt injection 可误导 RAG 的检索器或生成器，暴露敏感数据库内容
- 🔬 **研究方法**：KFS-RAG 用 attention rollout 加因果扰动定位检索上下文中的关键影响词，引导辅助 LLM 生成 keyword-grounded facts 替换原始上下文，使生成器只基于净化证据工作
- 📌 **结论**：注入攻击下显著降低数据库泄漏风险，同时保持回答准确性与相关性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for combining large language models (LLMs) with external knowledge sources. However, RAG systems remain vulnerable to prompt injection attacks, which may mislead the retriever or generator to expose sensitive database contents. To address this issue, we propose KFS-RAG, a defense that mitigates information leakage by reformulating the retrieved context. Specifically, our method first identifies a small set of influential keywords from the retrieved context via an attention rollout plus a causal perturbation mechanism. These keywords are then used to guide an auxiliary LLM to generate a compact set of keyword-grounded facts from the retrieved passages. Finally, the original context is substituted with these curated facts, ensuring that the generator operates on sanitized evidence rather than the raw retrieved text. Experimental evaluations demonstrate that KFS-RAG significantly reduces the risk of database leakage under injection attacks while maintaining response accuracy and relevance. This work highlights a practical pathway toward building secure and trustworthy RAG systems.

</details>

### 25. SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation

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

### 26. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

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

### 27. COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense

📄 [arXiv](https://arxiv.org/abs/2608.19982)　📅 2026-08

**关键词**：`defense`、`prompt injection`、`continual-learning defense`、`adaptive prompt injection`、`continual GRPO`、`margin-weighted replay`

👤 **作者**：Roshan Sood、Onat Gungor、Tajana Rosing

- 🎯 **研究动机**：提示注入防御以静态为主，需随新攻击策略重设计；终身对齐方法不应对持续演化的自适应对手
- 🔬 **研究方法**：COPA 把提示注入防御当终身学习：经 GRPO 增量纳入新观察攻击反馈，margin 加权经验回放保留对既有攻击类的防御
- 📌 **结论**：终身提示注入攻击流上 ASR 最高降 6.3 倍、平均 4.4 倍，优于 SOTA 防御并保留通用模型能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to exploit weaknesses in previously learned defenses. This limitation is particularly important in real-world deployments, where evolving attack distributions necessitate continual adaptation without sacrificing robustness to previously encountered threats. We present COPA, a continual preference optimization framework that treats prompt-injection defense as a lifelong learning problem. Instead of one-time alignment, COPA incrementally incorporates feedback from newly observed attacks via GRPO-based optimization and uses margin-weighted experience replay to retain defenses against prior attack classes. This enables continuous adaptation to emerging threats while mitigating catastrophic forgetting and preserving general-purpose model capabilities. Across lifelong prompt injection attack streams, COPA reduces attack success rate by up to 6.3x and 4.4x on average compared to state-of-the-art defenses. These results highlight continual preference optimization as an effective paradigm for defending LLMs against adaptive adversaries.

</details>

### 28. AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations

📄 [arXiv](https://arxiv.org/abs/2603.10749) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/he-yu)　📅 2026-03　🏷 USENIX Security 2026

**关键词**：`defense`、`agent prompt injection`、`indirect injection`、`causal attribution`、`indirect prompt injection`、`tool invocation`

👤 **作者**：Yu He、…、Zhan Qin

- 🎯 **研究动机**：把间接注入当输入级语义判别问题的防御难以泛化到未见 payload
- 🔬 **研究方法**：动作级因果归因：AttriGuard 对每个工具调用做并行反事实测试，结合 teacher-forced 影子重放防归因混淆、层级控制衰减与模糊生存准则抗 LLM 随机性
- 📌 **结论**：4 个 LLM、2 个基准上静态攻击 ASR 为 0%、效用损失可忽略，在自适应优化攻击下依然稳健而领先防御显著退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are highly vulnerable to Indirect Prompt Injection (IPI), where adversaries embed malicious directives in untrusted tool outputs to hijack execution. Most existing defenses treat IPI as an input-level semantic discrimination problem, which often fails to generalize to unseen payloads. We propose a new paradigm, action-level causal attribution, which secures agents by asking why a particular tool call is produced. The central goal is to distinguish tool calls supported by the user's intent from those causally driven by untrusted observations. We instantiate this paradigm with AttriGuard, a runtime defense based on parallel counterfactual tests. For each proposed tool call, AttriGuard verifies its necessity by re-executing the agent under a control-attenuated view of external observations. Technically, AttriGuard combines teacher-forced shadow replay to prevent attribution confounding, hierarchical control attenuation to suppress diverse control channels while preserving task-relevant information, and a fuzzy survival criterion that is robust to LLM stochasticity. Across four LLMs and two agent benchmarks, AttriGuard achieves 0% ASR under static attacks with negligible utility loss and moderate overhead. Importantly, it remains resilient under adaptive optimization-based attacks in settings where leading defenses degrade significantly.

</details>

### 29. BERM: Low-Overhead Prompt-Injection Detection via In-Situ Benign Representation Modeling

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/8133.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`analysis`、`lightweight guard model`、`in-situ representation`、`deployment latency`、`prompt injection`

- 🎯 **研究动机**：现有提示注入防御依赖脆弱启发式或调用昂贵辅助模型，无法兼顾鲁棒与低延迟
- 🔬 **研究方法**：BERM 对 host LLM prefill 阶段提取的内部表征原位建模：联合对比学习良性表征紧致流形以最大化与恶意表征分离，轻量分类器推理时原位检测
- 📌 **结论**：F1 比最佳先前工作高 5.2 个百分点，同时快 12 倍以上，增量推理开销近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world deployment of large language models (LLMs) necessitates a robust and low-latency approach to detect prompt injections; existing lowoverhead methods fail to simultaneously boost robustness and reduce latency. Current defenses for prompt injection either rely on brittle heuristics or invoke costly auxiliary models, imposing a significant runtime burden. We introduce BERM, a lightweight framework that performs in-situ detection by modeling a host LLM’s internal representations extracted during prefill, adding negligible overhead. Our approach trains a lightweight classifier atop the LLM by learning a compact manifold of benign representations via joint contrastive learning to maximize the separation from malicious representations. At inference, this pre-trained classifier enables in-situ detection without invoking auxiliary guard models. On a diverse landscape of prompt injection attacks, our framework establishes a new state-of-the-art, achieving an F1-score 5.2 percentage points (pp) higher than the best prior work. Critically, BERM achieves this while being over 12x faster, reducing incremental inference overhead to near-zero.

</details>

### 30. ARGUS: Defending Against Multimodal Indirect Prompt Injection via Steering Instruction-Following Behavior

📄 [arXiv](https://arxiv.org/abs/2512.05745) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_ARGUS_Defending_Against_Multimodal_Indirect_Prompt_Injection_via_Steering_Instruction-Following_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`defense`、`indirect prompt injection`、`multimodal model`、`activation steering`

👤 **作者**：Weikai Lu、…、Hao Peng

- 🎯 **研究动机**：针对 MLLM 的多模态间接 prompt injection，现有 text-only 防御易被绕过、依赖模态且泛化差
- 🔬 **研究方法**：发现指令遵循行为编码于表示空间某子空间，ARGUS 在其中搜索与效用退化方向解耦的最优防御方向并做自适应强度 steering，辅以轻量注入检测按需激活与后过滤验证
- 📌 **结论**：对多模态 IPI 实现鲁棒防御，同时最大限度保留 MLLM 效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly vulnerable to multimodal Indirect Prompt Injection (IPI) attacks, which embed malicious instructions in images, videos, or audio to hijack model behavior. Existing defenses, designed primarily for text-only LLMs, are unsuitable for countering these multimodal threats, as they are easily bypassed, modality-dependent, or generalize poorly. Inspired by activation steering researches, we hypothesize that a robust, general defense independent of modality can be achieved by steering the model's behavior in the representation space. Through extensive experiments, we discover that the instruction-following behavior of MLLMs is encoded in a subspace. Steering along directions within this subspace can enforce adherence to user instructions, forming the basis of a defense. However, we also found that a naive defense direction could be coupled with a utility-degrading direction, and excessive intervention strength harms model performance. To address this, we propose ARGUS, which searches for an optimal defense direction within the safety subspace that decouples from the utility degradation direction, further combining adaptive strength steering to achieve a better safety-utility trade-off. ARGUS also introduces lightweight injection detection stage to activate the defense on-demand, and a post-filtering stage to verify defense success. Experimental results show that ARGUS can achieve robust defense against multimodal IPI while maximally preserving the MLLM's utility.

</details>

### 31. Defending Against Prompt Injection with DataFilter

📄 [arXiv](https://arxiv.org/abs/2510.19207) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-10　🏷 SaTML 2026

**关键词**：`defense`、`prompt injection`、`test-time sanitization`、`black-box LLM`

👤 **作者**：Yizhu Wang、Sizhe Chen、Raghad Alkhudair、Basel Alomair、David Wagner

- 🎯 **研究动机**：现有 prompt injection 防御要么需要模型权重（微调），要么损失效用（检测），要么要求系统重构
- 🔬 **研究方法**：DataFilter 是测试时模型无关防御，经模拟注入 SFT 训练，依据用户指令与数据内容选择性剥离对抗指令同时保留良性信息
- 📌 **结论**：多基准上把注入 ASR 降至近零并保持效用，可即插即用地保护黑盒商业 LLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When large language model (LLM) agents are increasingly deployed to automate tasks and interact with untrusted external data, prompt injection emerges as a significant security threat. By injecting malicious instructions into the data that LLMs access, an attacker can arbitrarily override the original user task and redirect the agent toward unintended, potentially harmful actions. Existing defenses either require access to model weights (fine-tuning), incur substantial utility loss (detection-based), or demand non-trivial system redesign (system-level). Motivated by this, we propose DataFilter, a test-time model-agnostic defense that removes malicious instructions from the data before it reaches the backend LLM. DataFilter is trained with supervised fine-tuning on simulated injections and leverages both the user's instruction and the data to selectively strip adversarial content while preserving benign information. Across multiple benchmarks, DataFilter consistently reduces the prompt injection attack success rates to near zero while maintaining the LLMs' utility. DataFilter delivers strong security, high utility, and plug-and-play deployment, making it a strong practical defense to secure black-box commercial LLMs against prompt injection. Our DataFilter model is released at https://huggingface.co/JoyYizhu/DataFilter for immediate use, with the code to reproduce our results at https://github.com/yizhu-joy/DataFilter.

</details>

### 32. Defeating Prompt Injections by Design

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

### 33. MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents

📄 [arXiv](https://arxiv.org/abs/2502.05174) · 🌐 [Project](https://proceedings.mlr.press/v267/zhu25z.html)　📅 2025-02　🏷 ICML 2025

**关键词**：`defense`、`agent prompt injection`、`indirect injection`、`provable defense`

👤 **作者**：Kaijie Zhu、Xianjun Yang、Jindong Wang、Wenbo Guo、William Yang Wang

- 🎯 **研究动机**：间接 prompt 注入防御或需大量训练资源、或防御不足、或损害效用
- 🔬 **研究方法**：MELON 以掩蔽用户 prompt 重执行轨迹：被攻击时动作更依赖恶意任务，两次执行动作相似即判为攻击
- 📌 **结论**：AgentDojo 上攻击阻断与效用保持均超 SOTA 防御，与 prompt 增强防御组合更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research has explored that LLM agents are vulnerable to indirect prompt injection (IPI) attacks, where malicious tasks embedded in tool-retrieved information can redirect the agent to take unauthorized actions. Existing defenses against IPI have significant limitations: either require essential model training resources, lack effectiveness against sophisticated attacks, or harm the normal utilities. We present MELON (Masked re-Execution and TooL comparisON), a novel IPI defense. Our approach builds on the observation that under a successful attack, the agent's next action becomes less dependent on user tasks and more on malicious tasks. Following this, we design MELON to detect attacks by re-executing the agent's trajectory with a masked user prompt modified through a masking function. We identify an attack if the actions generated in the original and masked executions are similar. We also include three key designs to reduce the potential false positives and false negatives. Extensive evaluation on the IPI benchmark AgentDojo demonstrates that MELON outperforms SOTA defenses in both attack prevention and utility preservation. Moreover, we show that combining MELON with a SOTA prompt augmentation defense (denoted as MELON-Aug) further improves its performance. We also conduct a detailed ablation study to validate our key designs. Code is available at https://github.com/kaijiezhu11/MELON.

</details>

### 34. LongPIBench: A Long-Context Benchmark for Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.28411)　📅 2026-08

**关键词**：`benchmark`、`long-context guardrail`、`prompt injection`、`real-world evaluation`、`long-context injection`、`real-world documents`

👤 **作者**：Yupei Liu、Yuqi Jia、Neil Zhenqiang Gong、Jinyuan Jia

- 🎯 **研究动机**：现有提示注入 benchmark 集中于短上下文输入，长上下文中的注入攻防几乎未被探索，导致对防御有效性的高估
- 🔬 **研究方法**：构建 LongPIBench，覆盖论文评审、简历筛选、代码审查、邮件摘要四类真实场景，每场景含合成与真实数据集，上下文长度从数千到数万 token
- 📌 **结论**：评测显示长上下文设定下即使简单启发式注入也取得高成功率，并频繁绕过 SOTA 提示注入防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely unexplored. This gap leads to a substantial overestimation of the effectiveness of current defenses. In this paper, we bridge the gap by introducing LongPIBench, a long-context benchmark for prompt injection covering 4 realistic application scenarios: paper peer review, resume screening, code review, and email summary. For each scenario, we construct a synthetic dataset and a real-world dataset, with context lengths ranging from thousands to tens of thousands of tokens. The evaluation results on LongPIBench reveal significant vulnerabilities of prompt injection defenses under long-context settings: even simple heuristic prompt injection attacks achieve high success rates and frequently bypass state-of-the-art defenses. We hope LongPIBench can serve as a practical benchmark for systematically evaluating prompt injection defenses in realistic long-context scenarios.

</details>

### 35. How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition

📄 [arXiv](https://arxiv.org/abs/2603.15714) · 📊 [Dataset](https://huggingface.co/datasets/sureheremarv/ipi_arena_attacks)　📅 2026-03

**关键词**：`benchmark`、`agent prompt injection`、`indirect injection`

👤 **作者**：Mateusz Dziemian、…、Zico Kolter

- 🎯 **研究动机**：间接注入可在最终回复不露痕迹的情况下执行有害动作，用户无从察觉，真实规模证据缺乏
- 🔬 **研究方法**：分析公开红队竞赛：464 名参与者对 13 个前沿模型提交 272,000 次攻击尝试，得 8,648 次成功攻击、41 个场景
- 📌 **结论**：所有模型皆可被攻破，ASR 从 0.5%（Claude Opus 4.5）到 8.5%（Gemini 2.5 Pro）；存在跨 21/41 行为迁移的通用攻击策略，能力与鲁棒性仅弱相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM based agents are increasingly deployed in high stakes settings where they process external data sources such as emails, documents, and code repositories. This creates exposure to indirect prompt injection attacks, where adversarial instructions embedded in external content manipulate agent behavior without user awareness. A critical but underexplored dimension of this threat is concealment: since users tend to observe only an agent's final response, an attack can conceal its existence by presenting no clue of compromise in the final user facing response while successfully executing harmful actions. This leaves users unaware of the manipulation and likely to accept harmful outcomes as legitimate. We present findings from a large scale public red teaming competition evaluating this dual objective across three agent settings: tool calling, coding, and computer use. The competition attracted 464 participants who submitted 272000 attack attempts against 13 frontier models, yielding 8648 successful attacks across 41 scenarios. All models proved vulnerable, with attack success rates ranging from 0.5% (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro). We identify universal attack strategies that transfer across 21 of 41 behaviors and multiple model families, suggesting fundamental weaknesses in instruction following architectures. Capability and robustness showed weak correlation, with Gemini 2.5 Pro exhibiting both high capability and high vulnerability. To address benchmark saturation and obsoleteness, we will endeavor to deliver quarterly updates through continued red teaming competitions. We open source the competition environment for use in evaluations, along with 95 successful attacks against Qwen that did not transfer to any closed source model. We share model-specific attack data with respective frontier labs and the full dataset with the UK AISI and US CAISI to support robustness research.

</details>

### 36. PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses

📄 [arXiv](https://arxiv.org/abs/2603.13026) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`tool`、`attack`、`agent prompt injection`、`adversarial evaluation`、`prompt-injection defense`、`adaptive red teaming`

👤 **作者**：Chenlong Yin、Runpeng Geng、Yanting Wang、Jinyuan Jia

- 🎯 **研究动机**：prompt injection 防御对自适应攻击的鲁棒性评估不足，制造虚假安全感
- 🔬 **研究方法**：PISmith 在黑盒设定用 RL 训练攻击 LLM 优化注入提示，针对奖励极度稀疏导致的熵塌缩引入自适应熵正则与动态优势加权
- 📌 **结论**：13 个基准上 SOTA 防御均可被自适应攻击突破，ASR 持续居首，并在 InjecAgent 与 AgentDojo 的 agent 场景对开源闭源 LLM 有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection poses serious security risks to real-world LLM applications, particularly autonomous agents. Although many defenses have been proposed, their robustness against adaptive attacks remains insufficiently evaluated, potentially creating a false sense of security. In this work, we propose PISmith, a reinforcement learning (RL)-based red-teaming framework that systematically assesses existing prompt-injection defenses by training an attack LLM to optimize injected prompts in a practical black-box setting, where the attacker can only query the defended LLM and observe its outputs. We find that directly applying standard GRPO to attack strong defenses leads to sub-optimal performance due to extreme reward sparsity -- most generated injected prompts are blocked by the defense, causing the policy's entropy to collapse before discovering effective attack strategies, while the rare successes cannot be learned effectively. In response, we introduce adaptive entropy regularization and dynamic advantage weighting to sustain exploration and amplify learning from scarce successes. Extensive evaluation on 13 benchmarks demonstrates that state-of-the-art prompt injection defenses remain vulnerable to adaptive attacks. We also compare PISmith with 7 baselines across static, search-based, and RL-based attack categories, showing that PISmith consistently achieves the highest attack success rates. Furthermore, PISmith achieves strong performance in agentic settings on InjecAgent and AgentDojo against both open-source and closed-source LLMs (e.g., GPT-4o-mini and GPT-5-nano). Our code is available at https://github.com/albert-y1n/PISmith.

</details>

### 37. Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States

📄 [arXiv](https://arxiv.org/abs/2608.02657)　📅 2026-08

**关键词**：`analysis`、`prompt injection`、`adversarial robustness`、`instruction hierarchy`

👤 **作者**：Jianshuo Dong、…、Han Qiu

- 🎯 **研究动机**：agent LLM 遭间接提示注入（IPI）时的内部表征机制不明，缺乏基于内部的防御
- 🔬 **研究方法**：在含 753B GLM-5.2、2.8T Kimi-K3 的八模型上训练线性探针预测 IPI 暴露，并提出探针门控的推理防御与解释分析框架
- 📌 **结论**：探针在未见攻击、指令与任务上 AUROC 0.90+；诊断出知识-行动差距后，探针门控防御把 AgentDojo 困难设定 ASR 从 34.6% 降到 0%（Qwen3.5-27B）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic LLMs are vulnerable to indirect prompt injection (IPI) attacks, e.g., malicious side-tasks hidden in external tool results. While many efforts have sought to address this threat, little is known about the internals of agentic LLMs when they are exposed to IPI attacks. For simplicity, we refer to this condition as IPI exposure. In this paper, we study IPI exposure from three perspectives. (1) Probing: Across eight models, including the 753B-parameter GLM-5.2 and the 2.8T-parameter Kimi-K3, simple linear probes trained on pre-generation hidden states can predict LLMs' IPI exposure. These probes achieve 0.90+ AUROC on unseen attacks, agent instructions, and task suites; they remain robustly predictive under adaptive attacks and in cross-lingual settings. (2) Defense: We reveal and diagnose a knowledge-action gap: post-trained LLMs encode signals predictive of IPI exposure, yet do not reliably bind these signals to safe agentic actions. We therefore introduce a probe-gated reasoning-based defense to bridge this gap at test time. On difficult AgentDojo settings, it substantially reduces attack success rate, e.g., from 34.6% to 0% on Qwen3.5-27B, and better preserves clean-task utility than the baselines. (3) Explanation: We introduce an analysis framework that identifies natural-language explanations strongly correlated with probe-captured signals. The resulting profiles differ across models: latent signals can align with either direct IPI-exposure sensing or indirect operational cues. Code is available at https://github.com/jianshuod/IPI-exposure-signal.

</details>

### 38. CachePrune: Teaching LLMs What Not to Follow via KV-Cache Editing

🎓 [Official](https://aclanthology.org/2026.acl-long.70/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`jailbreak defense`、`utility preservation`

👤 **作者**：Rui Wang、…、Julian McAuley

- 🎯 **研究动机**：间接提示注入源于 LLM 无法区分提示中的数据与指令
- 🔬 **研究方法**：CachePrune 在上下文 KV cache 编码阶段识别并剪除指令遵循相关神经元，引导 LLM 把上下文纯当数据；用偏好归因损失引导神经归因（理论上联系 DPO 目标上界）
- 📌 **结论**：显著降低 ASR 并保留用户指令遵循能力，不改提示格式且无测试时开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are susceptible to indirect prompt injection attack, where the model inadvertently responds to instructions injected into the prompt context. This vulnerability stems from LLMs’ inability to distinguish between data and instructions within a prompt. We propose CachePrune that defends against this attack by identifying and pruning neurons associated with instruction-following, during KV cache encoding of the prompt context. The pruning steers the LLM toward interpreting the context purely as data rather than as instructions to follow. To identify these neurons, we introduce a neural attribution mechanism guided by a preferential attribution loss, and theoretically connect this loss to an upper bound of the Direct Preference Optimization (DPO) objective. Further, we improve on the fidelity of neural attribution by leveraging an observed triggering effect in instruction-following. Our approach does not interfere with prompt formatting or incur test-time overhead in response generation. Experiments show that CachePrune significantly reduces the attack success rate while preserving the LLM’s ability to follow user instructions.

</details>

### 39. PIArena: A Platform for Prompt Injection Evaluation

🎓 [Official](https://aclanthology.org/2026.acl-long.1533/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`jailbreak defense`、`utility preservation`

👤 **作者**：Runpeng Geng、Chenlong Yin、Yanting Wang、Ying Chen、Jinyuan Jia

- 🎯 **研究动机**：提示注入评测缺统一平台，防御难可靠比较，许多报告有效的防御后来被证实在多样攻击下鲁棒性有限
- 🔬 **研究方法**：PIArena 统一可扩展平台集成 SOTA 攻击与防御跨基准评测，并设计按防御反馈自适应优化注入提示的动态策略攻击
- 📌 **结论**：揭示 SOTA 防御的局限：跨任务泛化有限、易受自适应攻击、注入任务与目标任务对齐时基本失防

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks pose serious security risks across a wide range of real-world applications. While receiving increasing attention, the community faces a critical gap: the lack of a unified platform for prompt injection evaluation. This makes it challenging to reliably compare defenses, understand their true robustness under diverse attacks, or assess how well they generalize across tasks and benchmarks. For instance, many defenses initially reported as effective were later found to exhibit limited robustness on diverse datasets and attacks. To bridge this gap, we introduce PIArena, a unified and extensible platform for prompt injection evaluation that enables users to easily integrate state-of-the-art attacks and defenses and evaluate them across a variety of existing and new benchmarks. We also design a dynamic strategy-based attack that adaptively optimizes injected prompts based on defense feedback. Through comprehensive evaluation using PIArena, we uncover critical limitations of state-of-the-art defenses: limited generalizability across tasks, vulnerability to adaptive attacks, and fundamental challenges when an injected task aligns with the target task. The code and datasets are available at https://github.com/sleeepeer/PIArena.

</details>

### 40. Security–Fidelity Tradeoffs: No Universal Defense Against Prompt Injection

🎓 [Official](https://icml.cc/virtual/2026/poster/60901)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`empirical evaluation`

👤 **作者**：Mitchell Hermon、Rahul Gupta、Weitong Ruan、Ekraam Sabir、Haohan Wang

- 🎯 **研究动机**：间接提示注入的防御越强越会损害模型忠实处理良性类指令文本的能力，现有评测把效用与保真混为一谈而掩盖这一代价
- 🔬 **研究方法**：提出 SecFid 基准，用行为可分离探针区分抵御、沦陷与忠实处理三种状态，并在决策论框架下证明良性输入与对抗输入重叠时不存在通用防御
- 📌 **结论**：最强防御靠激进压制有效内容换取安全，翻译任务保真失败率高达 50%；最优鲁棒性严格取决于任务对两类错误的容忍度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We identify a fundamental tension in securing LLMs: the \textbf{security--fidelity tradeoff}. While defenses against indirect prompt injection are becoming more robust, we show that they inevitably impair the model's ability to process benign, instruction-like text. Current evaluations miss this cost because they conflate utility with fidelity. We address this gap with \textsc{SecFid}, a benchmark that uses behaviorally separable probes to unambiguously distinguish between resisting an attack, succumbing to it, and faithfully processing it as data. Our evaluation reveals this tradeoff across a diverse set of models and highlights how the strongest defenses achieve security often by aggressively suppressing valid content, causing fidelity failure rates up to 50\% on translation. We ground these results in a decision-theoretic framework, proving that when benign and adversarial inputs overlap, no universal defense exists. Therefore, optimal robustness is strictly task-dependent, determined by an application’s tolerance for fidelity errors versus security failures.

</details>

### 41. RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse

📄 [arXiv](https://arxiv.org/abs/2602.01795) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62356)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`empirical evaluation`、`runtime defense`

👤 **作者**：Mingrui Liu、Sixiao Zhang、Cheng Long、Kwok-Yan Lam

- 🎯 **研究动机**：提示注入防御面临两难：微调式预防带来对齐税损害效用，检测式过滤延迟与内存开销过高
- 🔬 **研究方法**：提出 RedVisor：冻结骨干上可插拔轻量 adapter 生成定位注入并说明威胁的解释性分析，据此条件化模型拒绝恶意指令，响应阶段静默 adapter 并零拷贝复用 KV Cache，集成进 vLLM
- 📌 **结论**：检测准确率与吞吐量超过 SOTA 防御，良性输入上数学保持骨干原始效用，损失可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly vulnerable to Prompt Injection (PI) attacks, where adversarial instructions hidden within retrieved contexts hijack the model's execution flow. Current defenses typically face a critical trade-off: prevention-based fine-tuning often degrades general utility via the "alignment tax", while detection-based filtering incurs prohibitive latency and memory costs. To bridge this gap, we propose RedVisor, a unified framework that synthesizes the explainability of detection systems with the seamless integration of prevention strategies. To the best of our knowledge, RedVisor is the first approach to leverage fine-grained reasoning paths to simultaneously detect attacks and guide the model's safe response. We implement this via a lightweight, removable adapter positioned atop the frozen backbone. This adapter serves a dual function: it first generates an explainable analysis that precisely localizes the injection and articulates the threat, which then explicitly conditions the model to reject the malicious command. Uniquely, the adapter is active only during this reasoning phase and is effectively muted during the subsequent response generation. This architecture yields two distinct advantages: (1) it mathematically preserves the backbone's original utility on benign inputs; and (2) it enables a novel KV Cache Reuse strategy, eliminating the redundant prefill computation inherent to decoupled pipelines. We further pioneer the integration of this defense into the vLLM serving engine with custom kernels. Experiments demonstrate that RedVisor outperforms state-of-the-art defenses in detection accuracy and throughput while incurring negligible utility loss.

</details>

### 42. DRIP: Defending Prompt Injection via Token-wise Representation Editing and Residual Instruction Fusion

📄 [arXiv](https://arxiv.org/abs/2511.00447) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-11　🏷 ACM CCS 2026

**关键词**：`defense`、`prompt injection`、`representation editing`、`residual fusion`

👤 **作者**：Ruofan Liu、Yun Lin、Zhiyong Huang、Jin Song Dong

- 🎯 **研究动机**：现有防御难以兼顾效用与安全，且数据段中类指令语义仍可能覆盖原指令
- 🔬 **研究方法**：DRIP 用轻量表示编辑模块剥离数据段 token 的指令语义并保留数据语义，再加最小残差模块削弱对抗数据覆写原指令的能力
- 📌 **结论**：在 LLaMA 8B 与 Mistral 7B 上角色分离分数较 StruQ、SecAlign 等提升 12-49%，自适应攻击下 ASR 降超 66% 且效用与无防御模型相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly integrated into IT infrastructures, where they process user data according to predefined instructions. However, conventional LLMs remain vulnerable to prompt injection, where malicious users inject directive tokens into the data to subvert model behavior. Existing defenses train LLMs to semantically separate data and instruction tokens, but still struggle to (1) balance utility and security and (2) prevent instruction-like semantics in the data from overriding the intended instructions. We propose DRIP, which (1) precisely removes instruction semantics from tokens in the data section while preserving their data semantics, and (2) robustly preserves the effect of the intended instruction even under strong adversarial content. To "de-instructionalize" data tokens, DRIP introduces a data curation and training paradigm with a lightweight representation-editing module that edits embeddings of instruction-like tokens in the data section, enhancing security without harming utility. To ensure non-overwritability of instructions, DRIP adds a minimal residual module that reduces the ability of adversarial data to overwrite the original instruction. We evaluate DRIP on LLaMA 8B and Mistral 7B against StruQ, SecAlign, ISE, and PFT on three prompt-injection benchmarks (SEP, AlpacaFarm, and InjecAgent). DRIP improves role-separation score by 12-49\%, reduces attack success rate by over 66\% under adaptive attacks, and matches the utility of the undefended model, establishing a new state of the art for prompt-injection robustness.

</details>

### 43. The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections

📄 [arXiv](https://arxiv.org/abs/2510.09023) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nasr)　📅 2025-10　🏷 USENIX Security 2026

**关键词**：`defense`、`attack`、`adaptive attack`、`jailbreak defense`、`prompt injection defense`

👤 **作者**：Milad Nasr、…、Florian Tramèr

- 🎯 **研究动机**：越狱与 prompt injection 防御大多只对静态攻击集或弱优化方法评测，无法反映自适应攻击者的真实威胁
- 🔬 **研究方法**：系统调优并扩展梯度下降、强化学习、随机搜索与人工引导探索等通用优化技术，对 12 个近期防御发起自适应攻击
- 📌 **结论**：多数防御被以 90% 以上 ASR 绕过，而其原报告多为近零攻击成功率，现有鲁棒性声明不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How should we evaluate the robustness of language model defenses? Current defenses against jailbreaks and prompt injections (which aim to prevent an attacker from eliciting harmful knowledge or remotely triggering malicious actions, respectively) are typically evaluated either against a static set of harmful attack strings, or against computationally weak optimization methods that were not designed with the defense in mind. We argue that this evaluation process is flawed. Instead, we should evaluate defenses against adaptive attackers who explicitly modify their attack strategy to counter a defense's design while spending considerable resources to optimize their objective. By systematically tuning and scaling general optimization techniques-gradient descent, reinforcement learning, random search, and human-guided exploration-we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near-zero attack success rates. We believe that future defense work must consider stronger attacks, such as the ones we describe, in order to make reliable and convincing claims of robustness.

</details>

### 44. CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution

📄 [arXiv](https://arxiv.org/abs/2602.07918) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62590)　📅 2026-02　🏷 ICML 2026

**关键词**：`detection`、`defense`、`prompt injection`、`causal analysis`、`instruction hierarchy`、`runtime defense`

👤 **作者**：Minbeom Kim、…、Tomas Pfister

- 🎯 **研究动机**：IPI 防御常驻消毒造成过防御困境，良性场景也承担效用与延迟损失
- 🔬 **研究方法**：CausalArmor 在特权决策点做留一消融归因，仅当不可信片段主导用户意图时触发定向消毒，并回溯掩码被污染的 CoT
- 📌 **结论**：在 AgentDojo 与 DoomArena 上匹配激进防御的安全性，同时保留 agent 效用、延迟与可解释性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents equipped with tool-calling capabilities are susceptible to Indirect Prompt Injection (IPI) attacks. In this attack scenario, malicious commands hidden within untrusted content trick the agent into performing unauthorized actions. Existing defenses can reduce attack success but often suffer from the over-defense dilemma: they deploy expensive, always-on sanitization regardless of actual threat, thereby degrading utility and latency even in benign scenarios. We revisit IPI through a causal ablation perspective: a successful injection manifests as a dominance shift where the user request no longer provides decisive support for the agent's privileged action, while a particular untrusted segment, such as a retrieved document or tool output, provides disproportionate attributable influence. Based on this signature, we propose CausalArmor, a selective defense framework that (i) computes lightweight, leave-one-out ablation-based attributions at privileged decision points, and (ii) triggers targeted sanitization only when an untrusted segment dominates the user intent. Additionally, CausalArmor employs retroactive Chain-of-Thought masking to prevent the agent from acting on ``poisoned'' reasoning traces. We present a theoretical analysis showing that sanitization based on attribution margins conditionally yields an exponentially small upper bound on the probability of selecting malicious actions. Experiments on AgentDojo and DoomArena demonstrate that CausalArmor matches the security of aggressive defenses while improving explainability and preserving utility and latency of AI agents.

</details>

### 45. Localize and Neutralize: Gradient-Guided Token Suppression Against Visual Prompt Injection Attack

📄 [arXiv](https://arxiv.org/abs/2605.25194) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63777)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`prompt injection`、`instruction hierarchy`、`task hijacking`、`mechanistic analysis`

👤 **作者**：Dongpeng Zhang、…、Qingming Huang

- 🎯 **研究动机**：视觉提示注入防御缺机制理解，难平衡效率与保真
- 🔬 **研究方法**：发现攻击只依赖少量关键图像 token：GTM 用 Hidden-State Gradient Norm 定位（排序与完整对抗损失梯度一致）后置零中和，单次前向-反向即可
- 📌 **结论**：提示注入与多模态越狱攻击 ASR 降至近零，保留模型效用且计算开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial images pose a severe security threat to multimodal large language models through prompt injection. Existing defenses largely lack a principled understanding of the underlying mechanisms and struggle to balance efficiency and fidelity. In this work, we show that successful adversarial attacks do not rely on the entire image uniformly but instead depend on a small subset of critical image tokens. Based on this insight, we propose a defense that first localizes these critical tokens via gradient analysis and then neutralizes them through masking. We show that attribution based on output probabilities fails when adversarial attacks preserve the predicted token. To overcome this limitation, we introduce the Hidden-State Gradient Norm score for adversarial behavior attribution and prove that its ranking is consistent with that of the full adversarial loss gradient, providing a theoretical guarantee for accurate localization. GTM requires only a single forward–backward pass to identify and zero out a small number of high-scoring tokens, effectively disrupting the adversarial attack path. Extensive experiments on prompt injection and multimodal jailbreak attacks demonstrate that our approach reduces attack success rates (ASR) to near zero while preserving model utility with negligible computational overhead. The code is available at: https://github.com/fish883/GTM-Defense.

</details>

### 46. Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.14493) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai)　📅 2026-07　🏷 USENIX Security 2026

**关键词**：`benchmark`、`attack`、`passive prompt injection`、`security log`、`prompt injection`、`defense-in-depth`

👤 **作者**：Rabimba Karanjai、Yang Lu、Hemanth Hegadehalli Madhavarao、Lei Xu、Weidong Shi

- 🎯 **研究动机**：SOC 用 LLM 分析外部日志，日志生成字段中的注入载荷可持久存储并在分析师查询时执行（passive prompt injection）
- 🔬 **研究方法**：提出 LogInject 框架与 12,847 条日志（2,569 对抗样本）基准，评估三个生产 LLM 在活动隐匿、误报生成、信息外泄与输出劫持四目标下的表现，并提出跨条目分片的 Context Stitching；测试输入过滤+提示加固+输出验证的分层缓解
- 📌 **结论**：基线 ASR 最高 88.2%（平均 83.4%），Context Stitching 达 76.4%；分层防御降低 90.4% 攻击但残留 8.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural language contexts to generate security insights. We demonstrate that this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term passive prompt injection. We present LogInject, a systematic framework for evaluating these threats. Using LogInject-1.0, a benchmark of 12,847 log entries including 2,569 adversarial samples, we evaluate three production LLMs across four attack objectives: activity concealment, false positive generation, information exfiltration, and output hijacking. Our findings reveal an up to 88.2% attack success rate (83.4% average across models) under the baseline conditions. We introduce Context Stitching, a novel technique that fragments payloads across multiple log entries to evade stateless filters while exploiting LLM long-context reasoning, achieving a 76.4% success rate. As mitigation, we evaluate layered defenses by combining input filtering, prompt hardening, and output validation, demonstrating a 90.4% attack reduction, although 8.4% residual vulnerability persists. Our results establish that LLM-based log analysis creates an inherent confused deputy vulnerability where untrusted data and trusted instructions compete indistinguishably for model attention, requiring defense in-depth architectures and continued human oversight for security-critical decisions.

</details>

### 47. Stop Fixating on Prompts: Reasoning Hijacking and Constraint Tightening for Red-Teaming LLM Agents

🎓 [Official](https://aclanthology.org/2026.acl-long.1197/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`reasoning safety`、`agent safety`、`tool-use agent`、`automated red teaming`

👤 **作者**：Yanxu Mao、Peipei Liu、Tiehan Cui、Congying Liu、Mingzhe Xing、Datao You

- 🎯 **研究动机**：现有 LLM agent 红队方法多靠修改用户提示，对新数据适应性差且可能损害 agent 性能
- 🔬 **研究方法**：提出 JailAgent：完全不修改用户提示，经触发提取、推理劫持与约束收紧三阶段隐式操纵 agent 的推理轨迹与记忆检索
- 📌 **结论**：凭借触发识别、实时自适应机制与优化目标函数，在跨模型与跨场景环境中持续有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread application of LLM-based agents across various domains, their complexity has introduced new security threats. Existing red-team methods mostly rely on modifying user prompts, which lack adaptability to new data and may impact the agent’s performance. To address the challenge, this paper proposes the JailAgent framework, which completely avoids modifying the user prompt. Specifically, it implicitly manipulates the agent’s reasoning trajectory and memory retrieval with three key stages: Trigger Extraction, Reasoning Hijacking, and Constraint Tightening. Through precise trigger identification, real-time adaptive mechanisms, and an optimized objective function, JailAgent demonstrates outstanding performance in cross-model and cross-scenario environments.

</details>

### 48. Rethinking Indirect Prompt Injection as a Test-Time Search Problem

📄 [arXiv](https://arxiv.org/abs/2609.04495)　📅 2026-09

**关键词**：`attack`、`indirect prompt injection`、`test-time search`、`adaptive attacker`

👤 **作者**：Duong M. Nguyen、Joon Sik Kim、Blazej Manczak、Vaikkunth Mugunthan

- 🎯 **研究动机**：固定注入样本的评测把攻击成功率当作受害者的预算无关属性，低估了自适应搜索攻击者的能力
- 🔬 **研究方法**：把间接提示注入形式化为环境、用户任务与注入任务共同诱发的任务依赖攻击面上的 test-time search；实现带环境侦察、策略结构化推理与受害者反馈自适应评估的 agentic 攻击 harness
- 📌 **结论**：增加攻击者测试时算力持续提升漏洞发现与利用，显式策略管理对避免冗余搜索、维持大预算增益重要——agentic 安全评测应同时刻画攻击者的搜索过程与算力预算

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We formulate indirect prompt injection as a test-time search over a task-dependent attack surface induced by the environment, user task, and injection task. To operationalize this formulation, we introduce an agentic attacker with a dedicated search harness that performs environment reconnaissance, structured reasoning over attack strategies, and adaptive evaluation using victim-agent feedback. Across heterogeneous tasks, we find that increasing attacker test-time compute improves vulnerability discovery and exploitation, while ablations show that explicit strategy management is important for avoiding redundant search and sustaining gains at larger budgets. These results suggest that agentic security evaluations should characterize both the attacker's search procedure and compute budget, rather than treating attack success as a budget-independent property of the victim. More broadly, our findings identify the attacker's adaptive search over the system attack surfaces as an important and underexplored security risk for tool-using agents.

</details>
