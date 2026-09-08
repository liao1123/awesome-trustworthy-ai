# Agent Skill、Plugin 与供应链安全

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究以自然语言说明、脚本、依赖、模型或其他资源封装的 Agent skill/plugin。skill 通常经历 discovery、activation、execution、update 与 reuse，并以 Agent 或用户权限运行；威胁包括恶意 marketplace package、描述诱导、credential theft、代码执行、延迟 payload、self-mutation、skill composition 和 scanner evasion。页面重点是第三方生态与供应链；由 memory 或 trajectory 演化出的持久后门主记录在投毒目录。

## 研究脉络

- **新型 instruction supply chain：** skill 将 prompt、code 和依赖同时变成可安装能力，传统 package scanner 看不见自然语言指令，LLM judge 又可能看不见动态代码行为。
- **攻击生命周期：** 研究从单次恶意执行扩展到 discovery/activation 操纵、延迟复用、self-mutating content 和多个良性 skill 组合后的 emergent harm。
- **真实生态测量：** 大规模 registry crawl 发现 credential theft、RCE、隐藏能力和品牌仿冒已经出现在真实 skill 市场。
- **检测演进：** 防御由 pattern matching 与 LLM review 发展到 sandbox detonation、OS-boundary evidence、taint tracking 和 runtime audit。
- **当前边界：** scanner 对语义等价变形、下载后 payload、环境依赖行为和 signed-but-compromised update 仍缺少稳健保证。

## Survey 与 Threat Model

### 1. Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.13987)　📅 2026-07

**关键词**：`benchmark`、`skill lifecycle`、`SkillSec-Eval`、`repository admission`

👤 **作者**：Sanket Badhe、Priyanka Tiwari

- 🎯 **研究动机**：可复用 skill 的安全研究集中于 prompt injection 与运行时执行，覆盖完整 skill 生命周期（仓库准入、语义检索、规划选择、执行、演化）的评估缺失
- 🔬 **研究方法**：构建 SkillSec-Eval 生命周期感知评估框架：先刻画生命周期并建立威胁分类法，再在 327 个真实 skill 仓库上实证评估
- 📌 **结论**：漏洞在执行之外的多个生命周期阶段出现，需要生命周期感知的安全分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and runtime execution, leaving security risks throughout the broader skill lifecycle largely unexplored. In this paper, we present SkillSec-Eval, a lifecycle-aware framework for systematically evaluating the security of reusable agent skills. We first characterize the skill lifecycle and develop a threat taxonomy spanning repository admission, semantic retrieval, planner selection, execution, and skill evolution. We then instantiate this taxonomy in SkillSec-Eval and conduct a comprehensive empirical evaluation using a repository of 327 real-world skills. Our study demonstrates that vulnerabilities arise at multiple lifecycle stages beyond execution, highlighting the need for lifecycle-aware security analysis of reusable agent skills.

</details>

### 2. Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis

📄 [arXiv](https://arxiv.org/abs/2604.02837)　📅 2026-04

**关键词**：`survey`、`skill lifecycle`、`threat taxonomy`、`structural risk`

👤 **作者**：Zhiyuan Li、Jingzheng Wu、Xiang Ling、Xing Cui、Tianyue Luo

- 🎯 **研究动机**：Agent Skills 标准被多平台广泛采用但安全属性未被系统研究
- 🔬 **研究方法**：定义 Creation、Distribution、Deployment、Execution 四阶段生命周期，构建三层七类十七场景威胁分类法，并以五个已确认安全事件验证
- 📌 **结论**：最严重威胁源于框架结构性缺陷：缺数据-指令边界、单次批准的持久信任与无强制市场审核，增量缓解无法解决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills is an emerging open standard that defines a modular, filesystem-based packaging format enabling LLM-based agents to acquire domain-specific expertise on demand. Despite rapid adoption across multiple agentic platforms and the emergence of large community marketplaces, the security properties of Agent Skills have not been systematically studied. This paper presents the first comprehensive security analysis of the Agent Skills framework. We define the full lifecycle of an Agent Skill across four phases -- Creation, Distribution, Deployment, and Execution -- and identify the structural attack surface each phase introduces. Building on this lifecycle analysis, we construct a threat taxonomy comprising seven categories and seventeen scenarios organized across three attack layers, grounded in both architectural analysis and real-world evidence. We validate the taxonomy through analysis of five confirmed security incidents in the Agent Skills ecosystem. Based on these findings, we discuss defense directions for each threat category, identify open research challenges, and provide actionable recommendations for stakeholders. Our analysis reveals that the most severe threats arise from structural properties of the framework itself, including the absence of a data-instruction boundary, a single-approval persistent trust model, and the lack of mandatory marketplace security review, and cannot be addressed through incremental mitigations alone.

</details>

### 3. SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2602.20867)　📅 2026-02

**关键词**：`survey`、`skill lifecycle`、`design pattern`、`governance`

👤 **作者**：Yanna Jiang、…、Guangsheng Yu

- 🎯 **研究动机**：agentic skill 作为可复用过程能力常被等同于一次性工具调用，缺少覆盖全生命周期的系统梳理
- 🔬 **研究方法**：沿发现、练习、蒸馏、存储、组合、评估、更新七阶段提出七类设计模式与表示×范围双分类法，并以 ClawHavoc 事件做安全案例分析
- 📌 **结论**：ClawHavoc 近 1,200 个恶意 skill 大规模窃取 API key、钱包与浏览器凭据；精选 skill 大幅提升 agent 成功率而自生成 skill 可能降低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability conditions, execution policies, termination criteria, and reusable interfaces. Unlike one-off plans or atomic tool calls, skills operate (and often do well) across tasks. This paper maps the skill layer across the full lifecycle (discovery, practice, distillation, storage, composition, evaluation, and update) and introduces two complementary taxonomies. The first is a system-level set of \textbf{seven design patterns} capturing how skills are packaged and executed in practice, from metadata-driven progressive disclosure and executable code skills to self-evolving libraries and marketplace distribution. The second is an orthogonal \textbf{representation $\times$ scope} taxonomy describing what skills \emph{are} (natural language, code, policy, hybrid) and what environments they operate over (web, OS, software engineering, robotics). We analyze the security and governance implications of skill-based agents, covering supply-chain risks, prompt injection via skill payloads, and trust-tiered execution, grounded by a case study of the ClawHavoc campaign in which nearly 1{,}200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale. We further survey deterministic evaluation approaches, anchored by recent benchmark evidence that curated skills can substantially improve agent success rates while self-generated skills may degrade them. We conclude with open challenges toward robust, verifiable, and certifiable skills for real-world autonomous agents.

</details>

### 4. Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward

📄 [arXiv](https://arxiv.org/abs/2602.12430) · 🌐 [Project](https://www.agentskills-workshop.org/)　📅 2026-02

**关键词**：`survey`、`progressive disclosure`、`skill acquisition`、`trust tier`

👤 **作者**：Renjun Xu、Yang Yan

- 🎯 **研究动机**：agent skill 抽象层快速演进，缺少聚焦其架构、获取、部署与安全的系统综述
- 🔬 **研究方法**：沿架构基础（SKILL.md、progressive disclosure、MCP）、skill 获取、规模化部署与安全四轴梳理该领域
- 📌 **结论**：引用实证：26.1% 社区 skill 含漏洞；提出按 provenance 分级授权的四层 Skill Trust and Lifecycle Governance 框架与七项开放挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL$.$md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries, autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for the next generation of agentic systems. Project repo: https://github.com/scienceaix/agentskills

</details>

### 5. Formal Analysis and Supply Chain Security for Agentic AI Skills

📄 [arXiv](https://arxiv.org/abs/2603.00195)　📅 2026-02

**关键词**：`analysis`、`formal model`、`supply chain`、`SkillFortify`

👤 **作者**：Varun Pratap Bhardwaj

- 🎯 **研究动机**：混合自然语言、脚本与依赖的 agent skill 缺少统一可检查的形式模型
- 🔬 **研究方法**：形式化 permission、information flow 与供应链验证并实现 SkillFortify 工具，含 5 个定理完整证明
- 📌 **结论**：修订实验显示 pattern matching 已覆盖该语料检出项（F1 96.15%），information flow 分析无额外检出，明确了形式化保证的适用边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

32 pages, 5 theorems with full proofs, 68 references, open-source tool: https://github.com/qualixar/skillfortify. v2: corrects the bibliography (22 entries had author lists that did not match the papers at the cited arXiv identifiers; all verified against the arXiv API and corrected, and affected authors notified) and three external claims against primary sources: MalTool reports 1,300 standalone and 5,727 embedded malicious tools, not 6,487; CVE-2026-25253 is authentication-token exfiltration via an unvalidated gatewayUrl, credited to depthfirst and fixed in 2026.1.29, not remote code execution through a crafted skill package; ClawHavoc counts are 341, later 824, and 1,184 by source and date, not "over 1,200". All experiments re-measured against the released v0.6.0 implementation using harnesses now committed to the repository. E1/E2 unchanged (F1 96.15%). E3 reverses to a negative result: information flow analysis adds no detections over pattern matching on this corpus. The soundness theorem's scope is stated explicitly and no longer conflated with the zero false-positive rate.

</details>

### 6. A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors

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

### 7. Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction

📄 [arXiv](https://arxiv.org/abs/2608.26733)　📅 2026-08

**关键词**：`attack`、`skill extraction`、`black-box task interaction`、`functional reconstruction`、`agent-skill extraction`、`output-only access`

👤 **作者**：Yu-Lin Tsai、Yu-An Lu、Ci-Yang Tsai、Muxi Lyu、Raluca Ada Popa、Chia-Mu Yu

- 🎯 **研究动机**：泄露防御能拦截索要 skill 的请求，却拦不住服务本就要完成的普通任务，隐藏 skill 可被从结果逆向
- 🔬 **研究方法**：Daydreaming 自适应构造能区分隐藏行为的任务，用 shadow Agent 与本地执行检查重建多文件 skill，仅凭输出访问运作
- 📌 **结论**：7 个 skill、4 个受害模型上恢复原 skill 86.8% 的能力（约 SigLeak 四倍），每个 skill 中位数仅 32 次调用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that steals a multi-file skill through black-box task interactions. The victim is never asked to reveal the skill or grade a reconstruction. Instead, Daydreaming adaptively creates crafted tasks whose results distinguish possible hidden behaviors. It tests individual behaviors, uses attacker-controlled shadow agents to choose a design, and completes each file using stored victim results and local execution checks. We formalize three nested threat levels of access as Differential, Trace, and Output, and focus on Output, where the attacker sees only the final response and returned files. Across 7 skills and 4 victim models, Daydreaming recovers 86.8% of the original skill's capability at Output, outperforming SigLeak by almost 4x. It produces installable skills using a median of 32 victim calls per skill even with disclosure defenses enabled. These results show that hiding skill files and filtering direct disclosure do not, by themselves, prevent functional reconstruction through normal use.

</details>

### 8. EVOMAL: Self-Poisoning in Self-Evolving Coding Agents

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

### 9. SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.21929)　📅 2026-08

**关键词**：`attack`、`coding agent`、`skill injection`、`resource amplification`、`token amplification`、`resource abuse`

👤 **作者**：Yuanjin Zheng、Jingbang Chen

- 🎯 **研究动机**：coding agent 把已安装 skill 当可信指令通道，可被滥用于安全攻击之外的经济性资源滥用：诱导 agent 消耗远超任务所需的 token
- 🔬 **研究方法**：SkillBloat 两阶段攻击：先跨多种放大机制筛选攻击类型条件，再用 LLM 引导的全文 skill 重写精炼最强候选，在真实 skill benchmark 与多种 coding-agent 配置上评估
- 📌 **结论**：平均最佳 token 放大达 5.4184–10.1455 倍，二阶段精炼稳定优于一阶段；该 token amplification 攻击面与既有 skill poisoning 正交

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of diverse attack-type conditions across multiple amplification mechanisms and then refines the strongest candidate through LLM-guided full-document skill rewriting. Evaluated on a real-world skill benchmark, SkillBloat achieves 5.4184x-10.1455x average best amplification across multiple coding-agent target configurations. An ablation shows that the second-stage refinement loop consistently improves average best amplification over Phase 1 attack-type screening alone, demonstrating that iterative optimization provides additional benefit beyond initial attack-type selection. These results show that skill ecosystems expose a practical resource-amplification attack surface that is orthogonal to existing security-oriented skill poisoning.

</details>

### 10. CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

📄 [arXiv](https://arxiv.org/abs/2608.16246)　📅 2026-08

**关键词**：`attack`、`Agent Skill`、`plugin supply chain`、`persistent compromise`、`skill composition`、`scanner bypass`

👤 **作者**：Mingxiao Liu、…、Zhen Wang

- 🎯 **研究动机**：技能市场逐个认证技能，单技能通过扫描器不代表组合安全——组合风险是路径性质而非节点性质
- 🔬 **研究方法**：CompoSkill 双攻击者：白盒注入显式 skill-id 序列，黑盒按角色画像下载热门技能构建 Skill Composition Graph 搜高风险链；CompoSkill-Bench 含 1140 条记录
- 📌 **结论**：风险链形成率白盒最高 83.3%、黑盒 80.6%，现有扫描器拦截有限；桥接技能提升攻击但链长超三跳后 ASR 衰减

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill composition risk a path level property rather than a node level property, explaining why existing skill scanners that inspect individual packages achieve limited interception. To study this threat, we present CompoSkill, a framework that constructs skill composition attacks through a dual attacker system. The white-box attacker knows the victim's installed skill pool and directly injects explicit skill-id sequences; the black-box attacker knows only a role profile, downloads the top marketplace skills for that scenario, builds a Skill Composition Graph, and searches for high risk chains whose implicit lures never name skill identifiers. We further construct CompoSkill-Bench, a benchmark of 1,140 records built from long-horizon professional workflows across five threats and six scenarios on OpenClaw and Nanobot. CompoSkill achieves risk Chain Formation Rates (CFR) up to 83.3% in the white box setting and 80.6% in the black box setting, while existing skill scanners block only a limited fraction of the risky compositions. Finally, we observe a bridge-bonus-then-hop-decay pattern: a bridge skill can increase attack success, but Attack Success Rate (ASR) decreases once additional hops make the risk chain longer than three skills. These results expose a systematic gap in single skill certification for autonomous AI agents.

</details>

### 11. ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners

📄 [arXiv](https://arxiv.org/abs/2608.09732)　📅 2026-08

**关键词**：`attack`、`Agent Skill`、`adversarial robustness`、`plugin supply chain`、`cross-skill collusion`、`artifact flow`

👤 **作者**：Puyu Zeng、Simeng Qin、Jingzhi Li、Ju Jia、Zheli Liu、Xiaojun Jia

- 🎯 **研究动机**：现有技能扫描器只检查单个技能，多个局部合理技能组合成有害工作流的跨技能风险是盲区
- 🔬 **研究方法**：ColluSkill 把恶意意图分解为独立打包技能中的相互依赖子载荷，靠上下文依赖、工件传递与执行交接涌现恶意；ChainGuard 联合分析候选技能与已装技能重建跨技能依赖与工作流行为
- 📌 **结论**：六个技能扫描器上 ColluSkill 平均 ASR 96.0%；ChainGuard 把 ASR 降至 22.5% 同时放行 99.5% 良性工作流

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills are emerging as an important attack surface in LLM-based agent systems. Through an empirical study of existing skill scanners, we find that current defenses mainly inspect individual skills, leaving risks from cross-skill composition insufficiently examined. This creates a practical blind spot: multiple locally plausible skills may pass security checks while collectively forming a harmful workflow during agent execution. To investigate this threat, we propose ColluSkill, a collusive multi-skill-chain attack framework that decomposes a complete malicious intent into interdependent sub-payloads embedded in independently packaged skills. The attack does not rely on any single malicious skill, but emerges from the ordered composition of locally plausible behaviors through contextual dependencies, artifact passing, and execution handoffs. ColluSkill further employs LLM-based chain planning and scanner-feedback refinement to preserve chain-level attack semantics while reducing suspicious signals in individual sub-skills. To defend against such attacks, we propose ChainGuard, a context-aware skill-chain scanner that jointly analyzes a candidate skill and the skills already installed in the agent environment. ChainGuard reconstructs cross-skill dependencies, artifact flows, capability compositions, and downstream behaviors to identify risks that emerge only at the workflow level. Experiments on six representative skill scanners show that ColluSkill achieves an average attack success rate of 96.0% and consistently outperforms the evaluated single-skill and multi-skill attack baselines. Meanwhile, ChainGuard reduces the attack success rate to 22.5% while allowing 99.5% of benign workflows to pass, highlighting the importance of chain-level security analysis for agent skill ecosystems.

</details>

### 12. Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.07943)　📅 2026-06

**关键词**：`attack`、`skill injection`、`position-aware blending`、`stealth`、`position-aware injection`、`task preservation`

👤 **作者**：Haochang Hao、…、Lu Cheng

- 🎯 **研究动机**：skill 投毒需攻击动作完成同时用户任务通过验证器，而 skill 文件存在可靠性-可见性权衡（YAML 前置块显眼、正文可被跳过）
- 🔬 **研究方法**：提出 Poise：用上下文感知生成在结构可行的正文位置放置恰好一条看似良性、含命令的指令；ASR 定义要求后条件校验的沙箱动作与任务验证器同时通过
- 📌 **结论**：Skill-Inject 上（codex+gpt-5.2）ASR 89.3%，比随机放置高 28 个点、接近 YAML 基线的 86.7%；SkillTester 审计中 LLM judge 平均误报 74.6% 干净 skill，Poise 仅 5.6% 新增高危告警

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend general-purpose agents, but their open format enables skill poisoning: a tampered skill can make an agent run an attacker's command while completing the user's legitimate task. Invocation alone is insufficient; the attack-specific action must complete while that task still passes its verifier. We therefore define Attack Success Rate (ASR) to require a postcondition-validated sandbox action and a passing task verifier in the same trial. Skill files expose a reliability-visibility trade-off between a preloaded but conspicuous YAML frontmatter block and a longer body, where arbitrary placement may be skipped or locally incongruent. We introduce Poise, a position-aware attack that uses context-aware generation to place exactly one benign-looking, command-bearing instruction at a structurally feasible body position. On the eligible Skill-Inject pool with codex+gpt-5.2, Poise achieves 89.3\% ASR, 28.0 points above a context-free random-placement body baseline and comparable to the 86.7\% ASR of a high-exposure YAML-only baseline. Under the SkillTester audit, four LLM judges falsely flag 74.6\% of clean skills on average across both benchmarks, while only 5.6\% of Poise variants gain a new high-risk alert over their clean counterparts. One locally plausible, command-bearing body instruction therefore matches YAML-level reliability, while the resulting poisoned skill seldom adds a new high-risk finding over its clean counterpart.

</details>

### 13. SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction

📄 [arXiv](https://arxiv.org/abs/2606.02540)　📅 2026-06

**关键词**：`attack`、`benchmark`、`skill lifecycle`、`self-mutating poisoning`、`automated construction`、`fixed-payload poisoning`

👤 **作者**：Yuting Ning、…、Huan Sun

- 🎯 **研究动机**：已有 skill 攻击只评单次任务执行且风险清单零散，忽略跨复用的生命周期风险
- 🔬 **研究方法**：SkillHarm 覆盖 skill 使用生命周期：Fixed-Payload Poisoning 直接危害调用会话、Self-Mutating Poisoning 首次良性执行后静默改写持久 skill 内容延迟到复用时发作；12 类风险按数据管线、系统环境与 agent 自治划分；AutoSkillHarm 自动构建 879 个攻击样本
- 📌 **结论**：当前 agent 在 FPP 与 SMP 下 ASR 最高分别达 86.3% 与 69.3%；许多表面失败实为 agent 未读到毒文件而非真正抵抗，现有防御仍不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills occupy a privileged position in the agent workflow, as agents are expected to implicitly follow and execute them, rendering third-party skills a vulnerable attack surface. Existing studies have revealed unsafe agent behaviors induced by skill-based attacks, but they primarily evaluate poisoned skills within a single task execution and enumerate harms through ad-hoc risk lists. To bridge these gaps, we introduce SkillHarm, a benchmark of skill-based attacks across the skill-use lifecycle, paired with a systematic taxonomy of skill-relevant risks. SkillHarm evaluates two attack scenarios: Fixed-Payload Poisoning (FPP), where a fixed poisoned skill package directly compromises any task session that invokes it, and Self-Mutating Poisoning (SMP), where an initially benign execution silently mutates persistent skill content, deferring harm until a subsequent reuse. It further defines 12 risk types based on the agent workflow component targeted by the harm: data pipelines, system environments, and agent autonomy. To instantiate these attacks at scale, we build AutoSkillHarm, an automated construction pipeline with coding agents driven by natural-language harnesses. The resulting benchmark contains 879 attack samples across 71 skills. Experiments show that current agents remain vulnerable with attack success rates up to 86.3% in FPP and 69.3% in SMP. Our analysis further reveals a latent risk: many apparent attack failures stem from the agent failing to engage with the poisoned file rather than genuine resistance, and current defenses still fail to reliably mitigate the threat.

</details>

### 14. Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills

📄 [arXiv](https://arxiv.org/abs/2605.29354)　📅 2026-05

**关键词**：`attack`、`neutral prompting`、`package hallucination`、`supply chain`、`scanner evasion`

👤 **作者**：Chia-Yi Hsu、Chia-Mu Yu、Chun-Ying Huang、Jun Sakuma

- 🎯 **研究动机**：包幻觉攻击与防御聚焦自然幻觉或定向 steering，语义良性指令的隐蔽操纵未探索
- 🔬 **研究方法**：Neutral Prompting Attack（NPA）：鼓励想象与穷举等良性指令提高包幻觉倾向，不指定攻击者选择的包，使依赖生成转向投机性包名
- 📌 **结论**：同时提高 Hallucination ASR 与 Pip Install ASR 并改变幻觉包名分布，可绕过静态分析、LLM 与 agent 式 skill 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-powered coding agents increasingly participate in software development workflows by generating code, selecting dependencies, and producing package installation commands. This creates a new software supply chain risk: when an agent hallucinates a non-existent package, an attacker may register the hallucinated name and later compromise users who install it. Existing package hallucination attacks and defenses primarily focus on naturally occurring hallucinations, targeted dependency steering, or post-hoc package validation. In this paper, we introduce \emph{Neutral Prompting Attack} (NPA), a highly stealthy attack paradigm in which semantically benign instructions, such as encouraging imagination and exhaustiveness, increase package hallucination propensity without containing explicit malicious intent. Unlike targeted dependency steering, NPA does not specify an attacker-chosen package. Instead, it shifts the model's dependency generation behavior toward more speculative package names. We evaluate NPA across multiple coding-oriented LLMs and package hallucination benchmarks. Our results show that NPA increases both \emph{Hallucination ASR} and \emph{Pip Install ASR}, changes the distribution of hallucinated package names, and evades existing static-analysis, LLM-based, and agent-based Skill defenses. These findings reveal that harmless-looking prompts can covertly manipulate hallucination behavior and create downstream software supply chain risks.

</details>

### 15. When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2606.00448)　📅 2026-05

**关键词**：`analysis`、`skill composition`、`emergent risk`、`cross-skill interaction`

👤 **作者**：Su Wang、…、Jingzhou Xu

- 🎯 **研究动机**：单个安全的 skill 组合安装后可能形成不安全能力集，逐 skill 扫描按构造漏检
- 🔬 **研究方法**：SkillReact 三件套：确定性静态组合基准、双人 LLM 辅助人工裁决管线、基于动作的可利用性 harness；1,520 个 ClawHub skill 中 651 个过审组成 211,575 对
- 📌 **结论**：22.25% 对被标为结构候选，经人工校准约五分之一属真实组合风险（有效率 18.2%），单一 registry 隐含约 1.4 万条逐 skill 扫描必漏的风险；实际触发由宿主模型决定——Haiku-4-5 在 39 次直接 prompt 试验全部发出 dropper 工具调用，Sonnet-4-6 直接拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly rely on community-contributed skills that expand an agent's operational capability set. We study a core safety problem in agentic AI systems: whether individually safe skills can compose into unsafe installed skill sets. We present SkillReact, a compositional security measurement framework with three components: a deterministic static-composition benchmark, a two-rater LLM-assisted human-adjudication pipeline, and an action-based exploitability harness. On 1,520 ClawHub skills, 651 pass individual inspection and form 211,575 pairs; the benchmark flags 22.25% of these as structural candidates. We treat this raw rate as a recall-oriented scanner ceiling and calibrate it against human judgment: in a pattern-stratified audit, roughly one in five flagged pair-pattern hits survives as a real compositional risk (population-weighted validity 18.2%, our headline result), implying about 14K genuine risk memberships in a single registry that per-skill scanning misses by construction, since every pair is individually safe. An action-based harness then probes when these candidates become model-issued tool calls, and finds realization gated by host-model disposition: on an anchor-conditioned dropper subset, Haiku-4-5 issues the dropper-stage tool call on all 39 direct-prompt trials (36 of them the full download-then-execute chain, 3 download-only), Opus-4-7 stops at the download, and Sonnet-4-6 refuses outright. A control that holds the request fixed and varies only the installed skills finds compliance highest with no skills installed: a composition fixes which capabilities are reachable, while the host model decides whether to use them. Together these motivate install-time compositional checks and capability isolation as complements to per-skill scanning.

</details>

### 16. BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning

📄 [arXiv](https://arxiv.org/abs/2604.09378)　📅 2026-04

**关键词**：`attack`、`model-in-skill`、`semantic trigger`、`backdoor`、`model supply chain`

👤 **作者**：Guiyao Tie、Jiawen Shi、Pan Zhou、Lichao Sun

- 🎯 **研究动机**：Agent skill 可捆绑模型工件，prompt 注入与普通插件滥用分析均覆盖不了这种模型供应链威胁
- 🔬 **研究方法**：BadSkill 发布内嵌后门微调模型的看似良性 skill，常规参数的语义触发组合才激活隐藏 payload，以复合目标函数训练内嵌分类器
- 📌 **结论**：8 种架构上最高 99.5% ASR，3% 投毒率即达 91.7%，负类查询的良性准确率基本无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent ecosystems increasingly rely on installable skills to extend functionality, and some skills bundle learned model artifacts as part of their execution logic. This creates a supply-chain risk that is not captured by prompt injection or ordinary plugin misuse: a third-party skill may appear benign while concealing malicious behavior inside its bundled model. We present BadSkill, a backdoor attack formulation that targets this model-in-skill threat surface. In BadSkill, an adversary publishes a seemingly benign skill whose embedded model is backdoor-fine-tuned to activate a hidden payload only when routine skill parameters satisfy attacker-chosen semantic trigger combinations. To realize this attack, we train the embedded classifier with a composite objective that combines classification loss, margin-based separation, and poison-focused optimization, and evaluate it in an OpenClaw-inspired simulation environment that preserves third-party skill installation and execution while enabling controlled multi-model study. Our benchmark spans 13 skills, including 8 triggered tasks and 5 non-trigger control skills, with a combined main evaluation set of 571 negative-class queries and 396 trigger-aligned queries. Across eight architectures (494M--7.1B parameters) from five model families, BadSkill achieves up to 99.5\% average attack success rate (ASR) across the eight triggered skills while maintaining strong benign-side accuracy on negative-class queries. In poison-rate sweeps on the standard test split, a 3\% poison rate already yields 91.7\% ASR. The attack remains effective across the evaluated model scales and under five text perturbation types. These findings identify model-bearing skills as a distinct model supply-chain risk in agent ecosystems and motivate stronger provenance verification and behavioral vetting for third-party skill artifacts.

</details>

### 17. SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

📄 [arXiv](https://arxiv.org/abs/2604.06811) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65209)　📅 2026-04　🏷 ICML 2026

**关键词**：`attack`、`skill implementation`、`payload fragmentation`、`trigger`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Yunhao Feng、…、Wenke Huang

- 🎯 **研究动机**：基于组合 skill 的 agent 系统的安全攻击面未被检验
- 🔬 **研究方法**：SkillTrojan 攻击 skill 实现而非模型参数：把加密 payload 分片藏于多个看似良性的 skill 调用，经标准组合在预定义触发下重组执行；支持从任意模板自动合成并发布 3,000+ 后门 skill 数据集
- 📌 **结论**：EHR SQL 上对 GPT-5.2 达 97.2% ASR 同时保持 89.3% 干净准确率，暴露 skill 组合执行的安全盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skill-based agent systems tackle complex tasks by composing reusable skills, improving modularity and scalability while introducing a largely unexamined security attack surface. We propose SkillTrojan, a backdoor attack that targets skill implementations rather than model parameters or training data. SkillTrojan embeds malicious logic inside otherwise plausible skills and leverages standard skill composition to reconstruct and execute an attacker-specified payload. The attack partitions an encrypted payload across multiple benign-looking skill invocations and activates only under a predefined trigger. SkillTrojan also supports automated synthesis of backdoored skills from arbitrary skill templates, enabling scalable propagation across skill-based agent ecosystems. To enable systematic evaluation, we release a dataset of 3,000+ curated backdoored skills spanning diverse skill patterns and trigger-payload configurations. We instantiate SkillTrojan in a representative code-based agent setting and evaluate both clean-task utility and attack success rate. Our results show that skill-level backdoors can be highly effective with minimal degradation of benign behavior, exposing a critical blind spot in current skill-based agent architectures and motivating defenses that explicitly reason about skill composition and execution. Concretely, on EHR SQL, SkillTrojan attains up to 97.2% ASR while maintaining 89.3% clean ACC on GPT-5.2-1211-Global.

</details>

### 18. SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement

📄 [arXiv](https://arxiv.org/abs/2604.04989)　📅 2026-04

**关键词**：`attack`、`adversarial prompt`、`attack path`、`latent vulnerability`

👤 **作者**：Zenghao Duan、…、Xueqi Cheng

- 🎯 **研究动机**：良性 skill 也可能潜伏可被对抗提示利用的高权限漏洞，无需修改 skill 本身
- 🔬 **研究方法**：SkillAttack 闭环红队：漏洞分析、并行攻击面生成与反馈驱动利用精化，逐步收敛到成功利用
- 📌 **结论**：10 个 LLM、71 个对抗与 100 个真实 skill 上 ASR 达 0.73-0.93（对抗）/最高 0.26（真实），善意 skill 也构成现实安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agent systems increasingly rely on agent skills sourced from open registries to extend their capabilities, yet the openness of such ecosystems makes skills difficult to thoroughly vet. Existing attacks rely on injecting malicious instructions into skills, making them easily detectable by static auditing. However, non-malicious skills may also harbor latent vulnerabilities that an attacker can exploit solely through adversarial prompting, without modifying the skill itself. We introduce SkillAttack, a red-teaming framework that dynamically verifies skill vulnerability exploitability through adversarial prompting. SkillAttack combines vulnerability analysis, surface-parallel attack generation, and feedback-driven exploit refinement into a closed-loop search that progressively converges toward successful exploitation. Experiments across 10 LLMs on 71 adversarial and 100 real-world skills show that SkillAttack outperforms all baselines by a wide margin (ASR 0.73--0.93 on adversarial skills, up to 0.26 on real-world skills), revealing that even well-intended skills pose serious security risks under realistic agent interactions.

</details>

### 19. Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2604.03081)　📅 2026-04

**关键词**：`attack`、`document-driven payload`、`coding skill`、`MITRE ATT&CK`、`DDIPE`、`documentation payload`

👤 **作者**：Yubin Qu、…、Lei Ma

- 🎯 **研究动机**：显式恶意指令会被强对齐拒绝，供应链攻击能否直接劫持 agent 动作空间未知
- 🔬 **研究方法**：DDIPE 把恶意逻辑藏入 skill 文档的代码示例与配置模板，agent 正常任务复用示例时即无提示执行 payload
- 📌 **结论**：1,070 个对抗 skill、15 类 MITRE ATT&CK 下，四框架五模型绕过率 11.6%-33.5%（显式指令攻击为 0%），2.5% 同时逃过静态检测与对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based coding agents extend their capabilities via third-party agent skills distributed through open marketplaces without mandatory security review. Unlike traditional packages, these skills are executed as operational directives with system-level privileges, so a single malicious skill can compromise the host. Prior work has not examined whether supply-chain attacks can directly hijack an agent's action space, such as file writes, shell commands, and network requests, despite existing safeguards. We introduce Document-Driven Implicit Payload Execution (DDIPE), which embeds malicious logic in code examples and configuration templates within skill documentation. Because agents reuse these examples during normal tasks, the payload executes without explicit prompts. Using an LLM-driven pipeline, we generate 1,070 adversarial skills from 81 seeds across 15 MITRE ATTACK categories. Across four frameworks and five models, DDIPE achieves 11.6% to 33.5% bypass rates, while explicit instruction attacks achieve 0% under strong defenses. Static analysis detects most cases, but 2.5% evade both detection and alignment. Responsible disclosure led to four confirmed vulnerabilities and two fixes.

</details>

### 20. How Your Credentials Are Leaked by LLM Agent Skills: An Empirical Study

📄 [arXiv](https://arxiv.org/abs/2604.03070) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/43/How-Your-Credentials-Are-Leaked-by-LLM-Agent-Skills-An-Empirical-Study)　📅 2026-04　🏷 ASE 2026

**关键词**：`analysis`、`credential leakage`、`cross-modal audit`、`skill marketplace`、`agent skill`

👤 **作者**：Zhihao Chen、…、Zhiqiang Li

- 🎯 **研究动机**：skill 在特权执行环境中常规处理敏感凭据，其泄露方式未被大规模实证
- 🔬 **研究方法**：从 SkillsMP 分层抽样 17,022 个 skill，结合静态秘密提取（regex 与 AST）、mock 凭据沙箱动态测试与意图-行为交叉分析
- 📌 **结论**：520 个 skill 含 1,708 个问题、10 类泄露模式；73.5% 源于调试日志（stdout 进入 LLM 上下文），89.6% 凭据立即可利用，fork 分发使上游修复失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents increasingly rely on third-party skills that operate within privileged execution environments and routinely handle sensitive credentials, yet how these credentials are leaked remains largely unexplored. To fill this gap, we present the first large-scale empirical study on credential leakage in agent skills. From 170,226 artifacts on SkillsMP, the largest open-source skill marketplace, we sampled 17,022 skills via stratified random sampling and analyzed each through static secret extraction (regex and AST parsing), dynamic sandbox testing with mock credentials, and cross-referencing developer intent against runtime behavior. Our analysis identifies 520 affected skills containing 1,708 security issues, and yields a taxonomy of 10 leakage patterns. Three findings stand out. First, 76.3% of cases require jointly analyzing natural-language descriptions and programming logic, showing that credential exposure in skills is fundamentally cross-modal. Second, debug logging accounts for 73.5% of vulnerabilities because agent frameworks feed stdout into the LLM context window, turning routine debugging into a credential exposure vector. Third, 89.6% of leaked credentials are immediately exploitable -- 92.5% during routine execution without elevated privileges -- and the fork-based distribution model defeats remediation, as secrets removed from 107 upstream repositories persist across 50+ independent forks. Following responsible disclosure, all malicious skills have been removed and 91.6% of hardcoded cases remediated. We release our dataset, taxonomy, and detection pipeline to support future agent security research.

</details>

### 21. Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance

📄 [arXiv](https://arxiv.org/abs/2603.19974)　📅 2026-03

**关键词**：`attack`、`guidance injection`、`bootstrap file`、`OpenClaw`

👤 **作者**：Fazhong Liu、…、Haojin Zhu

- 🎯 **研究动机**：OpenClaw 生命周期钩子允许第三方在初始化时注入行为指导，这一未探索的攻击面可操纵推理上下文
- 🔬 **研究方法**：guidance injection 把有害动作包装成日常最佳实践写入 bootstrap 指导文件；构建 26 个恶意 skill、13 类攻击与 ORE-Bench 工作区基准
- 📌 **结论**：6 个 LLM 后端、52 个自然提示下 ASR 达 16.0%-64.2%，多数恶意动作无需用户确认自动执行，94% 逃过静态与 LLM 扫描器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous coding agents are increasingly integrated into software development workflows, offering capabilities that extend beyond code suggestion to active system interaction and environment management. OpenClaw, a representative platform in this emerging paradigm, introduces an extensible skill ecosystem that allows third-party developers to inject behavioral guidance through lifecycle hooks during agent initialization. While this design enhances automation and customization, it also opens a novel and unexplored attack surface. In this paper, we identify and systematically characterize guidance injection, a stealthy attack vector that embeds adversarial operational narratives into bootstrap guidance files. Unlike traditional prompt injection, which relies on explicit malicious instructions, guidance injection manipulates the agent's reasoning context by framing harmful actions as routine best practices. These narratives are automatically incorporated into the agent's interpretive framework and influence future task execution without raising suspicion.We construct 26 malicious skills spanning 13 attack categories including credential exfiltration, workspace destruction, privilege escalation, and persistent backdoor installation. We evaluate them using ORE-Bench, a realistic developer workspace benchmark we developed. Across 52 natural user prompts and six state-of-the-art LLM backends, our attacks achieve success rates from 16.0% to 64.2%, with the majority of malicious actions executed autonomously without user confirmation. Furthermore, 94% of our malicious skills evade detection by existing static and LLM-based scanners. Our findings reveal fundamental tensions in the design of autonomous agent ecosystems and underscore the urgent need for defenses based on capability isolation, runtime policy enforcement, and transparent guidance provenance.

</details>

### 22. SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents

📄 [arXiv](https://arxiv.org/abs/2602.14211)　📅 2026-02

**关键词**：`attack`、`coding skill`、`closed-loop refinement`、`payload hiding`、`automated poisoning`、`helper script`

👤 **作者**：Xiaojun Jia、…、Philip Torr

- 🎯 **研究动机**：手工 skill 投毒的显式恶意指令易被拒绝或忽略，脆弱且难以自动化适配任务
- 🔬 **研究方法**：SkillJect 把 payload 藏于辅助 helper 脚本，重写 SKILL.md 将其包装为强制前置步骤，并用攻击-受害-评估多 agent 闭环按执行反馈迭代改写
- 📌 **结论**：跨 skill 平台、后端 LLM 与攻击类别均大幅超越直接注入与手工攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend LLM agents with task-specific instructions, executable scripts, and auxiliary resources, improving reusability but creating a new supply-chain attack surface. A malicious or compromised skill can be repeatedly loaded as trusted guidance and steer downstream tool use. Existing skill-based prompt-injection attacks are often manual and brittle, because explicit malicious instructions are rejected or ignored when they are not aligned with the original workflow. We propose SkillJect, the first automated framework for generating poisoned skills against skill-enabled agent systems. SkillJect uses two coordinated channels. In the artifact channel, it hides the payload inside an auxiliary helper script. In the instruction channel, it rewrites SKILL.md with a front-loaded inducement strategy, placing injected content at the beginning and framing the helper script as a mandatory prerequisite or initialization step. The rewritten instruction explicitly references the helper-script path and provides an executable example command, making the helper appear to be a legitimate setup step before normal skill operations. SkillJect further adopts a closed-loop multi-agent process to improve attack effectiveness. An Attack Agent generates poisoned skills, a Victim Agent executes downstream tasks with the poisoned skill, and an Evaluate Agent inspects execution traces to determine whether the hidden payload was executed. The Attack Agent then uses this feedback to diagnose failure causes and rewrite SKILL.md, while keeping the payload fixed. Experiments across skill-enabled platforms, backend LLMs, and attack categories show that SkillJect substantially outperforms naive direct injection and prior manual skill-injection attacks, highlighting poisoned skills as a persistent threat in reusable skill ecosystems.

</details>

### 23. When Skills Lie: Hidden-Comment Injection in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2602.10498)　📅 2026-02

**关键词**：`attack`、`hidden comment`、`human-model visibility`、`tool intent`、`human-model visibility gap`

👤 **作者**：Qianli Wang、Boyang Ma、Minghui Xu、Yue Zhang

- 🎯 **研究动机**：Markdown skill 渲染为 HTML 后注释块对人工审核不可见，原文却仍原样进入模型，存在隐藏注入风险
- 🔬 **研究方法**：在合法 skill 末尾附加含恶意指令的隐藏注释，测试 DeepSeek-V3.2 与 GLM-4.5-Air 是否受影响
- 📌 **结论**：可诱导输出敏感工具意图；将 skill 视为不可信并禁止敏感操作的防御提示可阻断攻击并暴露可疑指令

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents often rely on Skills to describe available tools and recommended procedures. We study a hidden-comment prompt injection risk in this documentation layer: when a Markdown Skill is rendered to HTML, HTML comment blocks can become invisible to human reviewers, yet the raw text may still be supplied verbatim to the model. In experiments, we find that DeepSeek-V3.2 and GLM-4.5-Air can be influenced by malicious instructions embedded in a hidden comment appended to an otherwise legitimate Skill, yielding outputs that contain sensitive tool intentions. A short defensive system prompt that treats Skills as untrusted and forbids sensitive actions prevents these malicious tool calls and instead surfaces the suspicious hidden instructions.

</details>

### 24. Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections

📄 [arXiv](https://arxiv.org/abs/2510.26328)　📅 2025-10

**关键词**：`attack`、`agent skill`、`prompt injection`、`approval reuse`、`skill file`

👤 **作者**：David Schmotz、Sahar Abdelnabi、Maksym Andriushchenko

- 🎯 **研究动机**：Agent Skills 以 markdown 文件为 agent 注入知识并被 coding agent 信任，其安全性未经检验
- 🔬 **研究方法**：演示在长 Skill 文件与引用脚本中隐藏恶意指令外传内部文件与密码，并利用任务级“不再询问”审批泛化到密切相关但有害的操作
- 📌 **结论**：前沿 LLM 在现实场景中仍会被极其简单的 prompt injection 绕过系统级防护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Enabling continual learning in LLMs remains a key unresolved research challenge. In a recent announcement, a frontier LLM company made a step towards this by introducing Agent Skills, a framework that equips agents with new knowledge based on instructions stored in simple markdown files. Although Agent Skills can be a very useful tool, we show that they are fundamentally insecure, since they enable trivially simple prompt injections. We demonstrate how to hide malicious instructions in long Agent Skill files and referenced scripts to exfiltrate sensitive data, such as internal files or passwords. Importantly, we show how to bypass system-level guardrails of a popular coding agent: a benign, task-specific approval with the "Don't ask again" option can carry over to closely related but harmful actions. Overall, we conclude that despite ongoing research efforts and scaling model capabilities, frontier LLMs remain vulnerable to very simple prompt injections in realistic scenarios. Our code is available at https://github.com/aisa-group/promptinject-agent-skills.

</details>

### 25. Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

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

### 26. Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection

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

### 28. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

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

### 29. Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware

📄 [arXiv](https://arxiv.org/abs/2607.02357)　📅 2026-07

**关键词**：`detection`、`scanner evasion`、`sandbox detonation`、`taint tracking`

👤 **作者**：Zimo Ji、…、Shing-Chi Cheung

- 🎯 **研究动机**：静态 skill 扫描器基于外观模式或 LLM-as-judge，能否抵御保持语义只变外观的自适应逃逸未知
- 🔬 **研究方法**：先以 SkillCloak（结构混淆+自解压打包）对八个扫描器与 1,613 个在野恶意 skill 做规避研究；再提出 SkillDetonate 沙箱执行式审计：按需闭包提升+marker 污点追踪 OS 边界信息流
- 📌 **结论**：SFS 打包对每个扫描器逃逸率超 90%、结构混淆超 80%（混合扫描器达 96%）；SkillDetonate 以 2% 误报检出 97% 攻击、在野样本保持 87% 检出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance. This paper first presents an adversarial study of existing skill scanners through SkillCloak, a payload-preserving evasion framework that keeps the attack semantics intact while transforming their visible form. SkillCloak uses two complementary strategies: Structural Obfuscation, which rewrites visible payload indicators into semantically equivalent forms, and Self-Extracting Skill (SFS) Packing, which hides malicious components from the install-time view and restores them during agent execution. Across eight scanners and 1,613 in-the-wild malicious skills, SFS Packing bypasses every scanner at over 90%, while Structural Obfuscation bypasses over 80% on most static scanners and reaches 96% on a hybrid scanner, showing that appearance-based auditing is insufficient. Motivated by this finding, we propose SkillDetonate, a behavior-centric runtime auditor that executes skills in a sandbox and detects malicious effects through OS-boundary information-flow evidence rather than install-time appearance. SkillDetonate combines on-demand closure lift, which observes instructions materialized during execution, with marker-based taint analysis, which tracks sensitive-data flows across the agent context, files, processes, and network operations. The results show that SkillDetonate detects 97% of attacks at a 2% false-positive rate and sustains 87% detection on real-world malicious skills.

</details>

### 30. Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

📄 [arXiv](https://arxiv.org/abs/2606.11671)　📅 2026-06

**关键词**：`detection`、`runtime audit`、`targeted probing`、`trace evidence`、`self-evolving attack`

👤 **作者**：Tu Lan、Chaowei Xiao

- 🎯 **研究动机**：skill 可能在文档与代码层面无害，仅在特定用户请求、本地资产或工具交互下变恶意，纯静态审查脆弱
- 🔬 **研究方法**：提出 Runtime Skill Audit（RSA）：画像风险相关接口、构造执行上下文、依据 trace 证据赋予安全标签，在 OpenClaw 上对 100 个 skill 评估
- 📌 **结论**：准确率 90.0%（TPR 88.0%、FPR 8.0%），比最佳静态基线高 13 个点；自进化攻击下静态检测一两轮即崩溃而 RSA 持续检出 19-20/20

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills let LLM agents reuse instructions, resources, tools, and workflows, but they also create a new place for malicious behavior to hide. A skill may look benign in its documentation or code while becoming harmful only when it is invoked with particular user requests, local assets, persistent state, or multi-step tool interactions. This makes purely static vetting brittle. We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions. Instead of testing every skill with the same generic tasks, RSA profiles risk-relevant interfaces, prepares the execution context needed to exercise them, and assigns security labels from the resulting trace evidence. We instantiate RSA on OpenClaw and evaluate it on 100 skills against representative static baselines. RSA achieves 90.0\% accuracy with an 88.0\% true positive rate and an 8.0\% false positive rate, improving accuracy by 13.0 percentage points over the best static baseline. Under self-evolving attacks, static detectors collapse after one or two rounds, while RSA continues to detect 19--20 out of 20 malicious skills across rounds.

</details>

### 31. Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis

📄 [arXiv](https://arxiv.org/abs/2605.00314)　📅 2026-05

**关键词**：`detection`、`static audit`、`Datalog reachability`、`hybrid artifact`、`SDL`

👤 **作者**：Hongbo Wen、…、Yu Feng

- 🎯 **研究动机**：静态分析器只解析 skill 的结构化半边，LLM 工具读散文却无法可复现地证明污点输入到达高危 sink
- 🔬 **研究方法**：Semia 把 skill 提升为 SDL Datalog 事实库（含 LLM 触发动作、散文条件、人审检查点），CGRS propose-verify-evaluate 循环合成事实库，安全属性归约为可达性查询
- 📌 **结论**：13,728 个真实 skill 全部可审计且超半数含关键语义风险；541 个专家标注样本上 recall 97.7%、F1 90.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An agent skill is a configuration package that equips an LLM-driven agent with a concrete capability, such as reading email, executing shell commands, or signing blockchain transactions. Each skill is a hybrid artifact-a structured half declares executable interfaces, while a prose half dictates when and how those interfaces fire-and the prose is reinterpreted probabilistically on every invocation. Conventional static analyzers parse the structured half but ignore the prose; LLM-based tools read the prose but cannot reproducibly prove that a tainted input reaches a high-impact sink. We present Semia, a static auditor for agent skills. Semia lifts each skill into the Skill Description Language (SDL), a Datalog fact base that captures LLM-triggered actions, prose-defined conditions, and human-in-the-loop checkpoints. Synthesizing a fact base that is both structurally sound and semantically faithful to the original prose is the central challenge; we address it with Constraint-Guided Representation Synthesis (CGRS), a propose-verify-evaluate loop that refines LLM candidates until convergence. Security properties (e.g., indirect injection, secret leakage, confused deputies, unguarded sinks, etc.) over an agent skill can then be reduced to Datalog reachability queries. We evaluate Semia on 13,728 real-world skills from public marketplaces. Semia renders all of them auditable and finds that more than half carry at least one critical semantic risk. On a stratified sample of 541 expert-labeled skills, Semia achieves 97.7% recall and an F1 of 90.6%, substantially outperforming signature-based scanners and LLM baselines.

</details>

### 32. RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2604.22888)　📅 2026-04

**关键词**：`detection`、`attention hijacking`、`hidden state`、`pre-execution`

👤 **作者**：Wenjie Xiao、Xuehai Tang、Biyu Zhou、Songlin Hu、Jizhong Han

- 🎯 **研究动机**：恶意指令可藏于密集合法 skill 中，比传统间接注入更隐蔽，纯文本过滤不足且缺 pre-execution 检测
- 🔬 **研究方法**：发现 skill 中毒引发 attention hijacking——响应期注意力从受信上下文转向恶意 span；RouteGuard 冻结骨干，以可靠性门控晚期融合响应条件注意力与隐状态对齐
- 📌 **结论**：Skill-Inject 切片 F1 达 0.8834，找回 90.51% 被词法筛查漏掉的 description 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills introduce a new and more severe form of indirect injection for LLM agents: unlike traditional indirect prompt injection, attackers can hide malicious instructions inside a dense, action-oriented skill that already functions as a legitimate instruction source. We study pre-execution skill-poison detection and show that successful skill poisoning induces a structured internal effect, attention hijacking, in which response-time attention shifts from trusted context to malicious skill spans and drives harmful behavior. Motivated by this mechanism, we propose RouteGuard, a frozen-backbone detector that combines response-conditioned attention and hidden-state alignment through reliability-gated late fusion. Across both real and synthetic open-source skill benchmarks, RouteGuard is consistently the strongest or most robust detector; on the critical Skill-Inject channel slice, it reaches 0.8834 F1 and recovers 90.51% of description attacks missed by lexical screening, showing that defending against skill poisoning requires internal-signal detection rather than text-only filtering

</details>

### 33. Latent Reuse in Agent Skills: Multi-modal Clone Detection at Ecosystem Scale

📄 [arXiv](https://arxiv.org/abs/2603.22447) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/172/Latent-Reuse-in-Agent-Skills-Multi-modal-Clone-Detection-at-Ecosystem-Scale)　📅 2026-03　🏷 ASE 2026

**关键词**：`analysis`、`skill provenance`、`clone detection`、`supply-chain tracing`

👤 **作者**：Jiaying Zhu、Lyuye Zhang、Wenbo Guo、Yang Liu

- 🎯 **研究动机**：公开仓库超 200 万 skill，复制、改名与改编形成的复用链无人追踪，单通道克隆检测器易漏
- 🔬 **研究方法**：SkillReuse 融合全局词法匹配与 YAML、文本、代码各通道表示，经逻辑回归输出克隆分数与类型标签，配 300 对标注基准
- 📌 **结论**：F1 达 0.939；137,470 个 skill 中发现 106 万克隆对（涉及 66.8%），95.3% 跨作者；938 个安全 skill 追踪出 16,587 条单 skill 扫描必漏的克隆链

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An agent skill is a reusable package for extending an LLM agent, typically a SKILL.md file that combines YAML metadata, natural-language instructions, and executable code. Public repositories now host over two million skills, yet existing tools analyze each artifact in isolation, and registries do not track reuse created through copying, renaming, or adaptation. Detecting these links is difficult because reuse may appear in one channel while the others change; conventional single-channel clone detectors can therefore miss such adaptations. We present SkillReuse, a multi-modal clone detector that combines global lexical matching with channel-specific representations for YAML, prose, and code, then uses logistic regression to produce clone scores and interpretable clone-type labels. We also introduce SkillReuse-Bench, an annotated benchmark of 300 skill pairs spanning exact copies, renamed copies, adaptations, and semantic equivalents. On SkillReuse-Bench, SkillReuse reaches an F1 of 0.939 with 0.952 precision, improving over TF-IDF and delivering 4.2x higher recall on Type-4 semantic clones than MinHash. Applied to all 137,470 skills that pass the content filter, SkillReuse identifies 1.06 million clone pairs involving 66.8% of the analyzed skills; 95.3% of these pairs cross author boundaries. Among skills in the analyzed name-based clone families, 67% are superseded by a higher-quality variant. Tracing 938 security-relevant skills through the clone graph surfaces 16,587 clone links spanning 6,376 related skills that per-skill scanners alone would miss.

</details>

### 34. MalSkills: Detecting Malicious Skills in the Agentic Supply Chain via Neuro-symbolic Reasoning

📄 [arXiv](https://arxiv.org/abs/2603.27204) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/45/MalSkills-Detecting-Malicious-Skills-in-the-Agentic-Supply-Chain-via-Neuro-symbolic-)　📅 2026-03　🏷 ASE 2026

**关键词**：`detection`、`malicious skill`、`neuro-symbolic reasoning`、`agent supply chain`、`dependency graph`、`marketplace audit`

👤 **作者**：Shenao Wang、Junjie He、Yanjie Zhao、Yayi Wang、Kan Yu、Haoyu Wang

- 🎯 **研究动机**：恶意 skill 证据分散在异构工件且需情境推理，静态、LLM 与动态方法各自只覆盖局部
- 🔬 **研究方法**：MalSkills 以符号解析加 LLM 语义分析提取安全敏感操作，构建 skill 依赖图后做神经符号推理推断恶意模式与可疑工作流
- 📌 **结论**：200 个真实 skill 上 F1 达 93%（超基线 5-87 个百分点）；扫描 7 个注册库 150,108 个 skill 标记 620 个，人工确认 400 个恶意

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skills are increasingly used to extend LLM agents by packaging prompts, code, and configurations into reusable modules. As public registries and marketplaces expand, they form an emerging agentic supply chain, but also introduce a new attack surface for malicious skills. Detecting malicious skills is challenging because relevant evidence is often distributed across heterogeneous artifacts and must be reasoned in context. Existing static, LLM-based, and dynamic approaches each capture only part of this problem, making them insufficient for robust real-world detection. In this paper, we present MalSkills, a neuro-symbolic framework for malicious skills detection. MalSkills first extracts security-sensitive operations from heterogeneous artifacts through a combination of symbolic parsing and LLM-assisted semantic analysis. It then constructs the skill dependency graph that links artifacts, operations, operands, and value flows across the skill. On top of this graph, MalSkills performs neuro-symbolic reasoning to infer malicious patterns or previously unseen suspicious workflows. We evaluate MalSkills on a benchmark of 200 real-world skills against 5 state-of-the-art baselines. MalSkills achieves 93% F1, outperforming the baselines by 5--87 percentage points. We further apply MalSkills to analyze 150,108 skills collected from 7 public registries, flagging 620 potentially malicious skills. Through manual review, we confirm that 400 of them are indeed malicious, all of which were responsibly reported and are currently awaiting confirmation from the platforms and maintainers. These results demonstrate the practical potential of MalSkills in securing the agentic supply chain.

</details>

### 35. SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration

📄 [arXiv](https://arxiv.org/abs/2603.21019) · 🌐 [Project](https://skillhub.holosai.io/)　📅 2026-03

**关键词**：`detection`、`marketplace audit`、`semantic-behavior alignment`、`composition`、`admission filter`、`semantic alignment`

👤 **作者**：Zihan Guo、Zhiyu Chen、Xiaohang Nie、Jianghao Lin、Yuanjian Zhou、Weinan Zhang

- 🎯 **研究动机**：skill 市场面临语义-行为不一致与组合风险：单独良性的 skill 协同调用可诱发恶意行为
- 🔬 **研究方法**：SkillProbe 以 Skills-for-Skills 范式把审计流程封装为标准 skill 模块，串联准入过滤、语义-行为对齐检测与组合风险模拟
- 📌 **结论**：ClawHub 2,500 个真实 skill 上发现流行度-安全悖论：90% 以上高热度 skill 未通过严格审计，高风险 skill 在风险维度形成单一巨连通分量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid evolution of Large Language Model (LLM) agent ecosystems, centralized skill marketplaces have emerged as pivotal infrastructure for augmenting agent capabilities. However, these marketplaces face unprecedented security challenges, primarily stemming from semantic-behavioral inconsistency and inter-skill combinatorial risks, where individually benign skills induce malicious behaviors during collaborative invocation. To address these vulnerabilities, we propose SkillProbe, a multi-stage security auditing framework driven by multi-agent collaboration. SkillProbe introduces a "Skills-for-Skills" design paradigm, encapsulating auditing processes into standardized skill modules to drive specialized agents through a rigorous pipeline, including admission filtering, semantic-behavioral alignment detection, and combinatorial risk simulation. We conducted a large-scale evaluation using 8 mainstream LLM series across 2,500 real-world skills from ClawHub. Our results reveal a striking popularity-security paradox, where download volume is not a reliable proxy for security quality, as over 90% of high-popularity skills failed to pass rigorous auditing. Crucially, we discovered that high-risk skills form a single giant connected component within the risk-link dimension, demonstrating that cascaded risks are systemic rather than isolated occurrences. We hope that SkillProbe will inspire researchers to provide a scalable governance infrastructure for constructing a trustworthy Agentic Web. SkillProbe is accessible for public experience at skillhub.holosai.io.

</details>

### 36. SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces

📄 [arXiv](https://arxiv.org/abs/2605.12015) · 🌐 [Project](https://jinchang1223.github.io/skill-safety-bench-website/)　📅 2026-05

**关键词**：`benchmark`、`skill-mediated risk`、`CLI agent`、`rule-based verifier`

👤 **作者**：Chang Jin、…、Xingcheng Xu

- 🎯 **研究动机**：现有安全评测漏掉 skill 接口攻击面——用户请求良性时，不安全影响可藏于 skill 指导、本地工件或环境文件
- 🔬 **研究方法**：SkillSafetyBench 含 47 个任务、155 个对抗案例、6 个风险域、30 个安全类别，每例配规则式验证器并在沙箱中评完整轨迹
- 📌 **结论**：非用户侧攻击可持续诱发不安全行为，失败模式随风险域、攻击方法与 scaffold-model 配对显著变化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reusable skills are becoming a common interface for extending large language model agents, packaging procedural guidance with access to files, tools, memory, and execution environments. However, this modularity introduces attack surfaces that are largely missed by existing safety evaluations: even when the user request is benign, unsafe influence may reside in skill guidance, local artifacts, or execution-environment files that steer the agent toward unsafe actions. We present SkillSafetyBench, a runnable benchmark for evaluating such skill-facing safety failures. SkillSafetyBench includes 155 adversarial cases across 47 tasks, 6 risk domains, and 30 safety categories, each evaluated with a case-specific rule-based verifier. Experiments with multiple CLI agents and model backends show that non-user attacks can consistently induce unsafe behavior, with distinct failure patterns across domains, attack methods, and scaffold-model pairings. Our findings suggest that agent safety depends not only on model-level alignment, but also on how agents interpret skills, trust workflow context, and act through executable environments. The complete benchmark is available at https://github.com/AI45Lab/skill-safety-bench.

</details>

### 37. HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?

📄 [arXiv](https://arxiv.org/abs/2604.15415)　📅 2026-04

**关键词**：`benchmark`、`harmful skill`、`ecosystem measurement`、`implicit intent`

👤 **作者**：Yukun Jiang、Yage Zhang、Michael Backes、Xinyue Shen、Yang Zhang

- 🎯 **研究动机**：skill 生态安全研究聚焦 skill 内部漏洞如 prompt 注入，忽视可被直接滥用于网络攻击、诈骗的有害 skill
- 🔬 **研究方法**：测量两大 registry 共 98,440 个 skill，按有害 taxonomy 做 LLM 评分；构建 200 个有害 skill、20 类、四种条件的 HarmfulSkillBench 评 6 个 LLM
- 📌 **结论**：4.93% 的 skill 有害（ClawHub 达 8.84%）；预装 skill 使平均 harm score 从 0.27 升至 0.47，意图隐式时达 0.76

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have evolved into autonomous agents that rely on open skill ecosystems (e.g., ClawHub and Skills.Rest), hosting numerous publicly reusable skills. Existing security research on these ecosystems mainly focuses on vulnerabilities within skills, such as prompt injection. However, there is a critical gap regarding skills that may be misused for harmful actions (e.g., cyber attacks, fraud and scams, privacy violations, and sexual content generation), namely harmful skills. In this paper, we present the first large-scale measurement study of harmful skills in agent ecosystems, covering 98,440 skills across two major registries. Using an LLM-driven scoring system grounded in our harmful skill taxonomy, we find that 4.93% of skills (4,858) are harmful, with ClawHub exhibiting an 8.84% harmful rate compared to 3.49% on Skills.Rest. We then construct HarmfulSkillBench, the first benchmark for evaluating agent safety against harmful skills in realistic agent contexts, comprising 200 harmful skills across 20 categories and four evaluation conditions. By evaluating six LLMs on HarmfulSkillBench, we find that presenting a harmful task through a pre-installed skill substantially lowers refusal rates across all models, with the average harm score rising from 0.27 without the skill to 0.47 with it, and further to 0.76 when the harmful intent is implicit rather than stated as an explicit user request. We responsibly disclose our findings to the affected registries and release our benchmark to support future research (see https://github.com/TrustAIRLab/HarmfulSkillBench).

</details>

### 38. SkillTester: Benchmarking Utility and Security of Agent Skills

📄 [arXiv](https://arxiv.org/abs/2603.28815)　📅 2026-03

**关键词**：`benchmark`、`paired execution`、`security probe`、`quality assurance`

👤 **作者**：Leye Wang、Zixing Wang、Anjie Xu

- 🎯 **研究动机**：skill 评估或只看任务成功或只查恶意模式，缺乏统一质量保障
- 🔬 **研究方法**：SkillTester 以成对基线/带 skill 执行加独立安全探针套件，把原始执行工件归一化为效用分、安全分与三级安全状态标签
- 📌 **结论**：提供可复用的 agent skill 比较式 QA harness，公共服务已上线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This technical report presents SkillTester, a tool for evaluating the utility and security of agent skills. Its evaluation framework combines paired baseline and with-skill execution conditions with a separate security probe suite. Grounded in a comparative utility principle and a user-facing simplicity principle, the framework normalizes raw execution artifacts into a utility score, a security score, and a three-level security status label. More broadly, it can be understood as a comparative quality-assurance harness for agent skills in an agent-first world. The public service is deployed at https://skilltester.ai, and the broader project is maintained at https://github.com/skilltester-ai/skilltester.

</details>

### 39. Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem

📄 [arXiv](https://arxiv.org/abs/2603.16572) · 🌐 [Project](https://www.agentskills-workshop.org/)　📅 2026-03

**关键词**：`analysis`、`repository context`、`false positive`、`abandoned repository`

👤 **作者**：Florian Holzbauer、David Schmidt、Gabriel Gegenhuber、Sebastian Schrittwieser、Johanna Ullrich

- 🎯 **研究动机**：自动扫描器孤立评估 skill，把高达 46.8% 判为恶意，误报问题突出
- 🔬 **研究方法**：收集三大分发平台与 GitHub 的 238,180 个 skill，检验被标记 skill 是否与其所在 GitHub 项目上下文一致
- 📌 **结论**：仓库感知分析后仅 0.52% 仍属可疑；同时发现废弃仓库 skill 被接管等此前未记录的真实攻击向量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend local AI agents, such as Claude Code and OpenClaw, with additional functionality. Their growing popularity has led to dedicated marketplaces resembling mobile app stores, as well as automated scanners that assess whether skills are benign or malicious. However, scanner reports from individual marketplaces classify up to 46.8% of skills as malicious, raising concerns about false positives. We present the largest empirical security analysis of the AI agent skill ecosystem to date. We collect 238,180 unique skills from three major distribution platforms and GitHub, and analyze their contents, behavior, and repository context. Unlike existing scanner-based assessments, which evaluate skills largely in isolation, our repository-aware analysis checks whether a flagged skill is consistent with its surrounding GitHub project. This context substantially reduces the number of suspicious skills: only 0.52% remain suspicious after repository-aware analysis. Our results show that existing scanners can substantially overestimate maliciousness when repository context is ignored. At the same time, we identify previously undocumented real-world attack vectors, including the hijacking of skills hosted in abandoned GitHub repositories. Overall, our findings provide a more robust view of the agent-skill ecosystem's current risk surface and highlight the need for context-aware security evaluation.

</details>

### 40. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks

📄 [arXiv](https://arxiv.org/abs/2602.20156) · 🌐 [Project](https://www.skill-inject.com/)　📅 2026-02

**关键词**：`benchmark`、`skill file`、`contextual injection`、`authorization`

👤 **作者**：David Schmotz、Luca Beurer-Kellner、Sahar Abdelnabi、Maksym Andriushchenko

- 🎯 **研究动机**：skill 文件把第三方代码、知识与指令引入 agent 供应链，构成新的注入面但缺少标准评测
- 🔬 **研究方法**：SkillInject 含 202 个注入-任务对，从显式恶意到隐藏于合法指令的上下文依赖攻击，联合度量有害指令规避与合法指令服从
- 📌 **结论**：前沿模型 ASR 最高 80%，可执行数据外泄、破坏与勒索行为；模型 scaling 与简单输入过滤均无法解决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are evolving rapidly, powered by code execution, tools, and the recently introduced agent skills feature. Skills allow users to extend LLM applications with specialized third-party code, knowledge, and instructions. Although this can extend agent capabilities to new domains, it creates an increasingly complex agent supply chain, offering new surfaces for prompt injection attacks. We identify skill-based prompt injection as a significant threat and introduce SkillInject, a benchmark evaluating the susceptibility of widely-used LLM agents to injections through skill files. SkillInject contains 202 injection-task pairs with attacks ranging from obviously malicious injections to subtle, context-dependent attacks hidden in otherwise legitimate instructions. We evaluate frontier LLMs on SkillInject, measuring both security in terms of harmful instruction avoidance and utility in terms of legitimate instruction compliance. Our results show that today's agents are highly vulnerable with up to 80% attack success rate with frontier models, often executing extremely harmful instructions including data exfiltration, destructive action, and ransomware-like behavior. They furthermore suggest that this problem will not be solved through model scaling or simple input filtering, but that robust agent security will require context-aware authorization frameworks. Our benchmark is available at https://www.skill-inject.com/.

</details>

### 41. Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality

📄 [arXiv](https://arxiv.org/abs/2602.08004)　📅 2026-02

**关键词**：`analysis`、`ecosystem measurement`、`skill taxonomy`、`unsafe capability`

👤 **作者**：George Ling、Shanshan Zhong、Richard Huang

- 🎯 **研究动机**：agent skill 市场快速扩张，其类型分布、采用模式与风险缺乏定量证据
- 🔬 **研究方法**：对某大型市场 40,285 个公开 skill 做数据驱动分析，考察内容分布、供需关系与长度预算
- 📌 **结论**：内容高度集中于软件工程且意图级冗余严重，供需失衡明显，存在可执行系统级动作的非平凡安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend large language model (LLM) agents with reusable, program-like modules that define triggering conditions, procedural logic, and tool interactions. As these skills proliferate in public marketplaces, it is unclear what types are available, how users adopt them, and what risks they pose. To answer these questions, we conduct a large-scale, data-driven analysis of 40,285 publicly listed skills from a major marketplace. Our results show that skill publication tends to occur in short bursts that track shifts in community attention. We also find that skill content is highly concentrated in software engineering workflows, while information retrieval and content creation account for a substantial share of adoption. Beyond content trends, we uncover a pronounced supply-demand imbalance across categories, and we show that most skills remain within typical prompt budgets despite a heavy-tailed length distribution. Finally, we observe strong ecosystem homogeneity, with widespread intent-level redundancy, and we identify non-trivial safety risks, including skills that enable state-changing or system-level actions. Overall, our findings provide a quantitative snapshot of agent skills as an emerging infrastructure layer for agents and inform future work on skill reuse, standardization, and safety-aware design.

</details>

### 42. "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild

📄 [arXiv](https://arxiv.org/abs/2602.06547) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`analysis`、`skill marketplace`、`malware measurement`、`credential theft`、`agent skill`、`supply chain`

👤 **作者**：Yi Liu、…、Leo Yu Zhang

- 🎯 **研究动机**：agent skill 注册表快速膨胀，但因缺少标注威胁数据其安全影响未被研究
- 🔬 **研究方法**：对两大注册表的 98,380 个 skill 结合静态模式匹配与动态行为验证做系统安全分析
- 📌 **结论**：确认 157 个恶意 skill、632 个漏洞、13 类攻击技术，单个平均含 4.03 个漏洞；超半数来自单一威胁行为者，上报后 100% 被下架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based coding agents increasingly rely on third-party extensions called skills, which bundle natural language instructions and helper scripts that execute with full user privileges. Community registries have emerged to distribute these skills, but the security implications remain unstudied due to the absence of labeled threat data. This paper presents a systematic security analysis of 98,380 skills collected from two major registries. Through a combination of static pattern matching and dynamic behavioral verification, we identify 157 skills exhibiting confirmed malicious behavior, encompassing 632 distinct vulnerabilities across 13 attack techniques. Our analysis reveals that these threats are deliberate rather than accidental: each malicious skill contains an average of 4.03 vulnerabilities spanning multiple attack phases. We identify two dominant attack strategies with statistically significant negative correlation -- credential theft via remote code execution, and agent manipulation through adversarial instructions embedded in documentation. Over half of all confirmed cases originate from a single threat actor employing templated brand impersonation at scale. We further observe that attack sophistication correlates with concealment investment, with advanced skills universally employing undocumented capabilities while also exploiting platform-native trust mechanisms. Following responsible disclosure, registry maintainers removed all 157 (100%) of the reported skills. Our dataset and detection pipeline are publicly available to facilitate future research on securing LLM agent ecosystems.

</details>

### 43. Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale

📄 [arXiv](https://arxiv.org/abs/2601.10338)　📅 2026-01

**关键词**：`analysis`、`SkillScan`、`vulnerability taxonomy`、`marketplace measurement`

👤 **作者**：Yi Liu、…、Leo Zhang

- 🎯 **研究动机**：agent skill 以隐式信任执行且几乎无安全审查，其生态攻击面从未被量化
- 🔬 **研究方法**：从两大市场收集 42447 个 skill，用静态分析加 LLM 语义分类的多阶段框架 SkillScan 系统分析 31132 个
- 📌 **结论**：26.1% skill 含至少一个漏洞，横跨 prompt injection、数据外泄、提权与供应链四类 14 种模式；捆绑脚本的 skill 漏洞率高 2.12 倍，5.2% 呈高严重度恶意特征

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of AI agent frameworks has introduced agent skills, modular packages containing instructions and executable code that dynamically extend agent capabilities. While this architecture enables powerful customization, skills execute with implicit trust and minimal vetting, creating a significant yet uncharacterized attack surface. We conduct the first large-scale empirical security analysis of this emerging ecosystem, collecting 42,447 skills from two major marketplaces and systematically analyzing 31,132 using SkillScan, a multi-stage detection framework integrating static analysis with LLM-based semantic classification. Our findings reveal pervasive security risks: 26.1% of skills contain at least one vulnerability, spanning 14 distinct patterns across four categories: prompt injection, data exfiltration, privilege escalation, and supply chain risks. Data exfiltration (13.3%) and privilege escalation (11.8%) are most prevalent, while 5.2% of skills exhibit high-severity patterns strongly suggesting malicious intent. We find that skills bundling executable scripts are 2.12x more likely to contain vulnerabilities than instruction-only skills (OR=2.12, p<0.001). Our contributions include: (1) a grounded vulnerability taxonomy derived from 8,126 vulnerable skills, (2) a validated detection methodology achieving 86.7% precision and 82.5% recall, and (3) an open dataset and detection toolkit to support future research. These results demonstrate an urgent need for capability-based permission systems and mandatory security vetting before this attack vector is further exploited.

</details>

### 44. TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation

📄 [arXiv](https://arxiv.org/abs/2608.17588)　📅 2026-08

**关键词**：`analysis`、`Agent Skill`、`cyber misuse`、`plugin supply chain`

👤 **作者**：Zhibo Zhang、Zhen Ouyang、Ling Shi、Kailong Wang

- 🎯 **研究动机**：自动生成 Agent Skill 时仅看产物或最终任务结果无法确定 agent 会执行哪些动作、产生哪些副作用
- 🔬 **研究方法**：TRUSS 证据引导框架：静态门按九项安全属性检查产物，通过者在可控执行环境由影子 agent 加载、代理工具把动作暴露给策略执行并记录溯源轨迹，失败回链指导迭代精炼
- 📌 **结论**：SkillInject 上漏洞检测 100% 精确率与召回；修复把 ASR 从 38.71% 降至 19.35%（GPT 5.5）且零攻击回归；任务有效性从 17.11% 升至 52.94%、安全率 50.80% 升至 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills package reusable natural language procedures with executable resources, enabling software agents to acquire task specific capabilities without model adaptation. Automatically generating such Skills can improve task performance, yet evaluating a candidate solely from its artifact or final task outcome leaves unresolved which actions the equipped agent will perform and which side effects those actions will produce. We present TRUSS, an evidence guided framework for generating functionally effective and safety reliable Agent Skills. TRUSS first inspects functional claims against source and domain evidence while evaluating the complete artifact under nine predefined safety properties. Candidates admitted by this static gate are loaded by a shadow agent inside a Controllable Execution Environment, where brokered tools expose requested actions to policy enforcement and record their results as provenance preserving execution traces. Functional failures and property violations are linked back to the responsible Skill content and used to guide iterative refinement. We evaluate TRUSS on 168 SkillInject artifacts, 155 SkillSafetyBench cases, and all 187 tasks in SkillGenBench. TRUSS achieves 100.00\% precision and recall in vulnerability detection. Repair reduces attack success from 38.71\% to 19.35\% with GPT 5.5 and from 46.45\% to 29.68\% with GPT 5.4, with zero attack regression. For Skill generation, TRUSS raises task effectiveness from 17.11\% without Skills to 52.94\%, while increasing the benchmark Security rate from 50.80\% to 100.00\%. These results show that execution evidence can expose behavioral failures missed by artifact inspection and can guide Skill generation toward jointly verified functional and safety outcomes.

</details>

### 45. Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.11888)　📅 2026-08

**关键词**：`analysis`、`Agent Skill`、`plugin supply chain`、`persistent compromise`

👤 **作者**：Gen Dong、Yanjie Gao、Liqun Li、Tianyin Xu、Yu Hua、Fan Yang

- 🎯 **研究动机**：agent 技能的效果研究结论不一，技能诱发的任务失败与成本回归未被归因到具体技能
- 🔬 **研究方法**：差分分析框架对比有技能与无技能/语义匹配技能的运行，在 SkillsBench 与 SWE-Skills-Bench 归因出 307 例技能诱发失败；SkillTriage 做分类学归因
- 📌 **结论**：功能失败多源于看似相关的技能导致错误实现或遗漏要素；效率回归不能仅由 prompt 长度解释，过度验证与重型实现流水线分别贡献 67 与 30 例

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and cost regressions to specific loaded skills. We introduce a differential analysis framework that attributes a failure or regression to a skill by comparing a target skill-guided run against a no-skill or semantically matched skill reference run that solves the same task, or solves it more cheaply. We instantiate this framework on SkillsBench and SWE-Skills-Bench, yielding 307 skill-induced failures, including 125 functional failures and 182 efficiency regressions. We also build SkillTriage, a taxonomy-guided attribution tool that normalizes paired cases, extracts differential evidence, and produces triage reports. Our major findings include: (1) Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task-required implementation elements. (2) Skill-induced efficiency regressions are not explained by prompt length alone. (3) The largest sources within Excessive Procedure are excessive verification and heavy implementation pipelines, contributing 67 and 30 cases, respectively. This shows that skills often turn validation checklists and construction recipes into mandatory work. Based on our findings, we propose research topics and tooling improvements for safer and more cost-aware skill reuse.

</details>

### 46. MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection

📄 [arXiv](https://arxiv.org/abs/2608.19901)　📅 2026-08

**关键词**：`benchmark`、`malicious skill detection`、`source-disjoint evaluation`、`benign false positive`、`structural family`、`benign FPR`

👤 **作者**：Yue Wang、…、Leo Zhang

- 🎯 **研究动机**：现有恶意 Agent Skill 数据集在来源、格式、证据体制与良性覆盖上割裂，重复与结构关联内容阻碍聚合评测
- 🔬 **研究方法**：MaliciousSkillBench 整合 13 个公开源，8414 条原始恶意记录归一为 7539 唯一身份、4588 个结构家族；主基准 9740 个 Skill（7505 恶意+2235 良性），评三个学习型检测器与三个现成扫描器
- 📌 **结论**：学习检测器随机 Macro-F1 0.882-0.932 但源不相交评测仅 0.653-0.665；最强 TF-IDF SVM 在保留源上良性误报率 62.4%——可靠检测须联合测攻击检出与良性过标

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious Agent Skill detection. We consolidate 13 public sources, 11 of which contribute Core malicious artifacts, and reduce 8,414 raw malicious records to 7,539 normalized-unique identities in 4,588 operational structural families. After conservative cross-label conflict exclusion, the primary benchmark contains 9,740 Skills: 7,505 malicious and 2,235 benign. To characterize its coverage, we harmonize 11 attack categories for 4,983 malicious identities with supported source-native mappings and find substantial differences in threat composition across sources. We then evaluate three learned text detectors and three off-the-shelf Skill scanners. Learned detectors achieve 0.882-0.932 Random Macro-F1 but only 0.653-0.665 under Source-Disjoint evaluation; the strongest word TF-IDF SVM scores 0.932/0.916/0.665 on Random/structural-disjoint/Source-Disjoint while retaining 95.6% malicious recall but producing 62.4% benign FPR on held-out sources. Off-the-shelf scanners occupy different but also unsatisfactory operating regimes, reducing false positives only at the cost of sharply lower malicious recall. Together, these results show that reliable malicious-Skill detection requires both broader cross-source benchmark coverage and evaluation that jointly measures attack detection and benign over-flagging.

</details>