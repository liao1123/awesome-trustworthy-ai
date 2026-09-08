# Agent Skill 投毒与后门

[返回投毒与后门目录](README.md)

## 研究方向

这一方向研究攻击者如何污染第三方或 Agent 自生成的 skill，使恶意 instruction、代码、依赖、资源或条件规则被持久保存，并在 discovery、retrieval、planning、composition 或 execution 阶段触发。与 Agent memory 投毒不同，skill 是可复用、可分发且常带执行权限的制品；其安全边界同时涉及 prompt injection、软件供应链、权限继承和 self-evolution lineage。

> **收录口径（截至 2026-09-02）：** 收录直接研究 poisoned/malicious skill、skill-file prompt injection、skill backdoor、trajectory-to-skill contamination，以及专门面向这些威胁的 benchmark、scanner 和 runtime defense；一般 plugin/MCP 风险、skill 能力评测与纯生态统计见文末交叉索引。

## 研究脉络

- **第三方 skill 投毒：** 攻击者在共享库或 marketplace 植入带恶意 instruction、代码、模型、资源或依赖的制品。
- **选择与策略层操纵：** 攻击者还可以只改写 skill metadata、策略性示例或自然语言规则，利用语义匹配和隐式偏好改变 skill admission、候选选择或 Agent policy，而不需要显式注入命令。
- **条件与组合后门：** 单个 skill 可等待语义 trigger，多项 scanner-passing skill 也可通过 artifact flow、trust transfer 或 execution handoff 组合成有害链。
- **Trajectory-to-skill 投毒：** 不可信交互或经验被晋升为高信任 skill，使一次输入获得跨任务持久性。
- **自复制与 lineage 传播：** Agent 模仿已污染 skill 生成新制品，即使删除原始植入项，后门仍可沿衍生谱系保留。
- **检测与修复：** 防御需联合审计文本、代码、图像、依赖与实际运行效果，并在 admission、invocation、execution 和 post-action 阶段持续约束权限。

## 第三方 Skill 投毒、注入与后门

### 1. A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors

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

### 2. Implicit Manipulation for Skill Selection in LLM Agents with Semantic Matching

📄 [arXiv](https://arxiv.org/abs/2609.02035)　📅 2026-09

**关键词**：`attack`、`skill selection`、`semantic matching`、`implicit manipulation`

👤 **作者**：Qikai Wang、Yongzhao Zhang、Zhiwei Chen、Yimiao Sun、Jiguo Yu、Xiaosong Zhang

- 🎯 **研究动机**：显式 prompt injection 或指令级 steering 会留下可识别的操纵信号，而 skill 选择阶段的语义匹配面未被攻击
- 🔬 **研究方法**：提出 ISM：联合塑造目标 skill 元数据与可复用 prompt，在不出现显式选择指令的情况下操纵语义匹配；三阶段策略扩展语义覆盖、强化目标独特性并保持措辞自然
- 📌 **结论**：四个领域八个 selector 上目标选中率从 15.2% 升至 63.5%；人工审查仅拦 2.9%（Explicit Steering 为 91.4%），五个 LLM inspector 平均放行 82.9%，并可绕过 PPL-W、Llama Prompt Guard 2 与 PIGuard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skill selection is a key stage in LLM-agent workflows, determining which installed skill should handle a user request. Existing attacks on this stage primarily rely on explicit prompt injection or instruction-level steering, which can expose recognizable manipulation signals. In this work, we identify a new implicit attack surface for skill selection: even when the user prompt and skill description appear benign in isolation, their semantic relationship can still be strategically shaped to favor an attacker-chosen skill. Based on this observation, we present Implicit Skill-Selection Manipulation via Semantic Matching (ISM), which jointly shapes target-skill metadata and reusable prompts to manipulate skill selection without explicit selection instructions. Specifically, we develop a three-stage strategy to broaden semantic coverage, strengthen target distinctiveness, and preserve natural prompt wording. Across four task domains and eight selector models, ISM increases the average target-selection rate (TSR) from 15.2% to 63.5%. In a matched comparison, ISM achieves a 73.5% TSR, only 9.8 percentage points below Explicit Steering. Human reviewers block ISM in only 2.9% of judgments, versus 91.4% for Explicit Steering, while five LLM-based inspectors pass ISM at an average rate of 82.9%, versus 37.4% for Explicit Steering. Moreover, ISM remains effective against PPL-W, Llama Prompt Guard 2, and PIGuard.

</details>

### 3. A Finger on the Scale: Covert Policy Steering through Agentic Skills

📄 [arXiv](https://arxiv.org/abs/2609.02564)　📅 2026-09

**关键词**：`attack`、`skill policy integrity`、`black-box optimization`、`policy steering`

👤 **作者**：Jiarui Li、…、Shouling Ji

- 🎯 **研究动机**：第三方 skill 作为外置行为策略构成供应链风险：可保持声明任务与合法输出接口不变，暗中把 Agent 决策引向未披露目标
- 🔬 **研究方法**：形式化 Skill Policy Integrity，提出受约束黑盒框架 SkillShift：语义合理的策略编辑加分层验证、失败引导优化与策略压缩，不注入显式目标指令也不劫持任务
- 📌 **结论**：在 agentic commerce 与软件依赖场景达到 81.33%／63.33% 的攻击者偏好选择率、100% 效用保持，冻结策略可零优化跨异构 LLM 与环境迁移，且受测扫描器全部漏检

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functionality and the user-authorized objective. We further present SkillShift, a constrained black-box framework for covert policy steering without explicit target command injection or task hijacking. It combines semantically plausible policy edits with hierarchical validation, failure-guided optimization, and strategy compression to preserve effectiveness, output validity, transferability, and inconspicuousness. We instantiate this threat in agentic commerce and software dependency use, with SkillShift achieving attacker-favored selection rates of 81.33% and 63.33% while maintaining a 100% utility-preserving rate. The frozen policies also transfer without further optimization across heterogeneous LLM backends and agent environments. Moreover, the evaluated scanners fail to detect the constructed skills, motivating behavioral auditing of reusable skills as agent policy artifacts.

</details>

### 4. SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

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

### 5. CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

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

### 6. Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.12273)　📅 2026-08

**关键词**：`attack`、`tool-using agent DoS`、`third-party skill`、`path hijacking`、`description steering`、`planning detour`

👤 **作者**：Junliang Liu、…、Laizhong Cui

- 🎯 **研究动机**：第三方技能的描述与指令体是两个顺序控制点，选段操纵与工具链资源放大被割裂研究，端到端组合 unclear
- 🔬 **研究方法**：Convergent Detour Hijacking 纯文本攻击：描述建立相关性、指令体复用该理由伪造依赖，吸引攻击者协调者并招募良性技能走有界弯路后回到原路线保任务完成
- 📌 **结论**：DeepSeek-V4-Pro 上协调者被 80.02% 任务选中；被命中的完成任务运行 token 消耗增 66.91%、执行时间增 92.45%，而任务完成率相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly rely on third-party skills, using natural-language descriptions for selection and instruction bodies for planning. This progressive-disclosure design exposes two sequential control points to untrusted publishers: a static skill may steer an otherwise correct task onto an unnecessarily costly trajectory. Prior work studies selection manipulation, malicious skill instructions, and tool-chain resource amplification largely separately, leaving their end-to-end composition unclear. We introduce Convergent Detour Hijacking (CDH), a text-only, runtime-independent attack that couples these stages. Under shared semantic cover, a description establishes relevance during selection, while an aligned body reuses that rationale to fabricate plausible dependencies during planning. CDH attracts an attacker-controlled coordinator alongside legitimate skills, recruits unnecessary benign skills into a bounded detour, and then re-enters the original route to preserve task completion. We evaluate it across multiple LLM backends and 491 held-out tasks under single-task and multi-turn conditions. On DeepSeek-V4-Pro, the matched coordinator is selected in 80.02% of tasks; among coordinator-hit runs that complete tasks, token consumption and end-to-end execution time increase by 66.91% and 92.45%, respectively, while aggregate task completion remains comparable. Thus, correct outcomes do not guarantee trajectory integrity or cost safety.

</details>

### 7. ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners

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

### 8. ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization

📄 [arXiv](https://arxiv.org/abs/2608.09577)　📅 2026-08

**关键词**：`attack`、`conditional backdoor`、`semantic trigger`、`weight-free attack`

👤 **作者**：Hao Sui、Simeng Qin、Jie Liao、Xiaojun Jia、Bing Chen、Yang Liu

- 🎯 **研究动机**：现有技能攻击要么每次请求都触发、要么依赖微调权重或多个技能，条件化、低成本的单技能后门缺失
- 🔬 **研究方法**：ElasticBack 在技能文档植入规则 R、用户查询植入良性触发 T，仅两者同时出现才触发；用语义锚定规则注入生成 R，冻结 R 后以隐蔽约束遗传搜索进化 T
- 📌 **结论**：三种目标行为（各 50 技能）、四个 agent LLM 上高 ASR、近零误报且干净精度保持，跨模型迁移并绕过部署时防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills, bundles of instructions and resources that an LLM agent loads on demand, form an emerging supply chain where a single poisoned skill can persistently compromise every agent that installs it. However, existing skill attacks either fire on every request or rely on fine-tuned weights or multiple skills, leaving a conditional and low-cost backdoor unexplored. In this work, we present ElasticBack, an effective conditional single-skill backdoor that plants a rule R in the skill document and a benign-looking trigger T in the user query, so the malicious payload fires only when both co-occur. ElasticBack binds the two sides through a trigger-as-switch construction, generating R via semantic-anchored rule injection. It then freezes R and evolves T against it with a stealth-constrained genetic search, so that effectiveness and stealth are optimized, keeping the backdoor weight-free and dormant on benign inputs. Extensive experiments across three target behaviors (50 skills each) and four agent LLMs show that ElasticBack attains a high attack success rate at a near-zero false-positive rate with preserved clean accuracy, transfers across models, and evades deployment-time defenses. These results motivate stronger defenses for the skill supply chain.

</details>

### 9. PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2606.19191)　📅 2026-06

**关键词**：`attack`、`auxiliary resource`、`VulMask`、`triggered code`

👤 **作者**：Yu-Ting Lin、Chia-Mu Yu

- 🎯 **研究动机**：skill 生态的恶意行为可藏于辅助资源而非文本描述，显式恶意脚本易被检测
- 🔬 **研究方法**：提出 PhantomSkill 与 VulMask：把显式恶意脚本改写为漏洞形态实现，仅在攻击者控制的触发条件下激活恶意行为，使可见信号从恶意意图变为普通不安全代码
- 📌 **结论**：跨多宿主 skill、攻击目标与 coding agent，VulMask 保持良性效用的同时显著降低警告与恶意软件级检测，要求对 skill 做资源级审查

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills allow LLM-based coding agents to acquire domain-specific capabilities from third-party packages, but they also introduce a new supply-chain attack surface. We present PhantomSkill, an attack framework that hides malicious behavior in a skill's auxiliary resources rather than in its textual description. Its core technique, VulMask, rewrites overt malicious scripts into vulnerability-shaped implementations whose malicious behavior is activated only under attacker-controlled trigger conditions. This design shifts the visible signal from explicit malicious intent to ordinary-looking insecure code. Across representative host skills, attack goals, coding agents, generation models, and automated reviewers, VulMask preserves benign utility while reducing warning and malware-level detection compared with overt malicious scripts. Our results show that skill ecosystems require resource-level vetting, execution-time containment, and security policies that treat exploitable vulnerabilities in agent skills as potential malicious payloads.

</details>

### 10. Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners

📄 [arXiv](https://arxiv.org/abs/2606.18198)　📅 2026-06

**关键词**：`attack`、`SkillCamo`、`image-hidden instruction`、`multimodal scanner`

👤 **作者**：Xiaojun Jia、…、Yang Liu

- 🎯 **研究动机**：现有 skill 扫描器主要分析文本描述、manifest 与源码，图像中传递的恶意意图缺乏检查，多模态 agent 部署时仍可恢复
- 🔬 **研究方法**：提出 SkillCamo：把恶意指令藏于 skill 附带图像并改写文档使其自然引用该图像；配套 ExecScan 执行接地多模态扫描，做意图提取、行为重构、滥用评估与推演式执行模拟
- 📌 **结论**：图像隐藏指令挑战现有扫描器，ExecScan 显著提升 skill 扫描性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills are emerging as an important attack surface in LLM-based systems. Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave visually conveyed malicious intent insufficiently examined. This creates a practical blind spot: harmful operational instructions hidden in images may bypass scanning while still being recoverable by multimodal agents during deployment. To systematically investigate this threat, we propose SkillCamo, a document-mediated multimodal instruction attack that conceals malicious instructions within images bundled with a skill while rewriting the surrounding documentation to naturally reference those images as part of the normal workflow. Thus, the attack does not rely on the image alone, but on the joint interpretation of textual guidance and visual payload at execution time. To defend against such attacks, we further propose ExecScan, an execution-grounded multimodal scanning module that performs intent extraction, behavior reconstruction, abuse assessment, and deliberative execution simulation over skill artifacts. ExecScan jointly analyzes documentation, code, referenced resources, and visual content to recover hidden instructions, reconstruct executable behavior chains, and identify downstream risks such as exfiltration, destruction, persistence, deception, and privilege escalation. Extensive experiments show that image-hidden malicious instructions challenge existing skill scanners, while ExecScan can improve the skill scanning performance.

</details>

### 11. Dynamic Malicious Skills in Agentic AI

📄 [arXiv](https://arxiv.org/abs/2606.16287)　📅 2026-06

**关键词**：`attack`、`runtime mutation`、`SKILL.md injection`、`read-only mount`

👤 **作者**：Tianhao Chen、Zhengyuan Jiang、Yuepeng Hu、Yebei Gou、Neil Zhenqiang Gong

- 🎯 **研究动机**：skill 的自然语言文档（SKILL.md）可诱导 agent 在执行时动态注入恶意逻辑，绕过静态审查
- 🔬 **研究方法**：演示动态恶意 skill：在 SKILL.md 嵌入指令使 agent 运行时向良性 skill 注入恶意行为，跨 OpenHands 与 Claude Code 框架评估；并提出内核强制只读挂载的系统级防御
- 📌 **结论**：动态恶意 skill 以可观成功率在运行时注入多种恶意行为；只读挂载有效阻断该攻击且不影响良性 skill 功能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skills are a key enabling component of agentic AI. While they enhance agents' capabilities, they also introduce new attack surfaces. In this work, we investigate one such attack surface by demonstrating dynamic malicious skills. By embedding malicious instructions in natural-language documentation (e.g., SKILL.md), an attacker can induce an agent to dynamically inject malicious logic into an otherwise benign skill during execution. We evaluate this attack across agentic frameworks such as OpenHands and Claude Code, showing that dynamic malicious skills can successfully introduce a range of malicious behaviors at runtime with non-trivial success rates. To mitigate this vulnerability, we propose a system-level defense that prevents dynamic modification of skills using operating system kernel-enforced read-only mounts. Our evaluation demonstrates that this defense effectively blocks dynamic malicious skills while preserving the functionality of benign skills.

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

### 13. Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills

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

### 14. Exploiting LLM Agent Supply Chains via Payload-less Skills

📄 [arXiv](https://arxiv.org/abs/2605.14460)　📅 2026-05

**关键词**：`attack`、`semantic compliance hijacking`、`payload-less skill`、`RCE`

👤 **作者**：Xinyu Liu、Yukai Zhao、Xing Hu、Xin Xia

- 🎯 **研究动机**：现有审计擅长识别显式代码 payload 与预定义威胁内容，但运行时由 agent 生成能力动态合成的恶意行为可绕过检测
- 🔬 **研究方法**：Semantic Compliance Hijacking（SCH）把恶意目标写成自然语言合规规则的 payload-less skill，诱导 agent 自行生成并执行未授权代码；Multi-Skill 自动优化进一步增强
- 📌 **结论**：最脆弱配置下机密性违规最高 77.67%、远程代码执行 67.33%；因无 AST 签名与显式恶意意图，对现有扫描工具检出率为 0.00%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces. Adopting these integrations broadens the potential attack surface, prompting a need for systematic security evaluation. Current auditing mechanisms are effective at identifying explicit code payloads and predefined threat contents through security scanning. These detection mechanisms are bypassed if malicious behaviors lack direct injection and are instead synthesized dynamically at runtime through the agent's inherent generative capabilities. Exploring this blind spot, we introduce Semantic Compliance Hijacking (SCH), a payload-less supply chain attack targeting autonomous coding environments. The SCH approach translates malicious goals into unstructured natural language instructions formatted as necessary compliance rules, leading the agent to generate and execute unauthorized code. To assess the real-world viability of this attack, we developed an automated pipeline to evaluate its effectiveness across a test matrix comprising three mainstream agent frameworks and three distinct foundation models using contextualized scenarios. The findings demonstrate the pervasive nature of this threat, with SCH achieving peak success rates of up to 77.67% for confidentiality breaches and 67.33% for Remote Code Execution (RCE) under the most vulnerable configurations. Furthermore, the introduction of Multi-Skill Automated Optimization (MS-AO) further boosted attack efficacy. By omitting recognizable Abstract Syntax Tree (AST) signatures and explicit harmful intents, the manipulated skill files maintained a 0.00% detection rate, evading current scanning tools. This research highlights an underexplored attack surface within agent supply chains, pointing to a necessary transition from signature-based detection models toward semantic intent validation.

</details>

### 15. Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry

📄 [arXiv](https://arxiv.org/abs/2605.11418)　📅 2026-05

**关键词**：`attack`、`registry manipulation`、`discovery poisoning`、`governance evasion`

👤 **作者**：Shoumik Saha、Kazem Faghih、Soheil Feizi

- 🎯 **研究动机**：SKILL.md 的自然语言元数据影响 skill 被接纳、呈现、选择与加载，构成语义供应链风险
- 🔬 **研究方法**：仅修改 SKILL.md，在 Discovery、Selection、Governance 三个 registry 阶段用真实 ClawHub skill 与真实机制评测
- 📌 **结论**：Discovery 最高 86% 成对胜率与 80% Top-10 占位；对抗变体在 Selection 中平均 77.6% 被选；Governance 阶段恶意 skill 有 36.5%-100% 逃避封禁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous AI agents increasingly extend their capabilities through Agent Skills: modular filesystem packages whose SKILL.md files describe when and how agents should use them. While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded. We study SKILL.md - only attacks across three registry-facing stages of the Agent Skill lifecycle, using real ClawHub skills and realistic registry mechanisms. In Discovery, short textual triggers can manipulate embedding-based retrieval and improve adversarial skill visibility, achieving up to 86% pairwise win rate and 80% Top-10 placement. In Selection, description-only framing biases agents toward functionally equivalent adversarial variants, which are selected in 77.6% of paired trials on average. In Governance, semantic evasion strategies cause malicious skills to avoid a blocking verdict in 36.5%-100% of cases. Overall, our results show that SKILL.md is not passive documentation but operational text that shapes which third-party capabilities agents find, trust, and use.

</details>

### 16. Skill Description Deception Attack against Task Routing in Internet of Agents

📄 [arXiv](https://arxiv.org/abs/2605.09889)　📅 2026-05

**关键词**：`attack`、`skill description`、`semantic routing`、`malicious agent`

👤 **作者**：Jiayi He、Xiaofeng Luo、Jiawen Kang、Ruichen Zhang、Jianhang Tang、Dong In Kim

- 🎯 **研究动机**：IoA 依赖 agent 自声明 skill description 做语义路由，该元数据可被恶意操纵却未被研究
- 🔬 **研究方法**：形式化 Skill Description Deception（SDD）攻击，用 LLM 自动生成欺骗性 skill description 偏置路由决策
- 📌 **结论**：九个代表领域最高 ASR 达 98%，威胁具普遍性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A new paradigm, Internet of Agents (IoA), is transforming networked systems into LLM-driven service networks, where heterogeneous agents collaborate through task routing based on their self-declared skill descriptions. Although this promising paradigm enables agentic, distributed, and advanced intelligence, it also exposes a new and overlooked attack surface. In particular, malicious agents can strategically manipulate their skill descriptions to bias routing decisions and increase their probability of being selected for task execution, thereby disrupting user tasks and degrading system reliability. To characterize this threat, we propose and formalize a new attack model, termed \emph{Skill Description Deception} (SDD) attack. We further design an LLM-enabled SDD attack framework that automatically generates deceptive skill descriptions, enabling systematic vulnerability assessment of IoA systems. Experimental results on nine representative domains show that the proposed attack can achieve up to 98\% attack success rate, demonstrating the severity and generality of the attack. Our paper reveals a new security vulnerability in IoA and calls for secure and trustworthy semantic routing mechanisms for future IoA systems.

</details>

### 17. Trust Me, Import This: Dependency Steering Attacks via Malicious Agent Skills

📄 [arXiv](https://arxiv.org/abs/2605.09594)　📅 2026-05

**关键词**：`attack`、`dependency steering`、`package hallucination`、`persistent instruction`

👤 **作者**：Yiyong Liu、Chia-Yi Hsu、Chun-Ying Huang、Michael Backes、Rui Wen、Chia-Mu Yu

- 🎯 **研究动机**：包幻觉风险被视为被动模型失败，持久 Skill 工件能否主动诱导未被研究
- 🔬 **研究方法**：Dependency Steering 对良性 Skill 搜索保持表面用途的局部语义编辑，使编码 agent 在良性任务中倾向攻击者控制的包
- 📌 **结论**：多个编码 LLM 与基准上定向幻觉率高，跨模型与任务域迁移，且 Skill scanner 与 LLM 审计均难检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-powered coding agents increasingly make software supply chain decisions. They generate imports, recommend packages, and write installation commands. Prior work showed that these systems can hallucinate non-existent package names, which attackers may register as malicious packages. In this paper, we show that this risk is not only a passive model failure. It can be actively induced through the persistent Skill artifact. We introduce Dependency Steering, an attack paradigm in which a malicious Skill biases a coding agent toward an attacker-controlled package during benign coding tasks. The attack does not require modifying model weights, training data, or user prompts. To construct realistic attacks, we design a Skill-level optimization method that searches for localized semantic edits that preserve the apparent purpose of the original Skill while increasing targeted package generation. Across multiple coding-oriented LLMs and programming benchmarks, Dependency Steering achieves high targeted hallucination rates, transfers across models and task domains, and remains difficult for evaluated Skill scanners and LLM-based auditors to detect. Our results show that persistent agent instructions form an underexplored software supply chain attack surface.

</details>

### 18. BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning

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

### 19. SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

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

### 20. Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems

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

### 25. EVOMAL: Self-Poisoning in Self-Evolving Coding Agents

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

### 26. Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents

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

### 27. Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning

📄 [arXiv](https://arxiv.org/abs/2608.08303)　📅 2026-08

**关键词**：`attack`、`query-only attack`、`trajectory poisoning`、`condition-action rule`

👤 **作者**：Yuyang Luo、Haoran Wang、Kai Shu

- 🎯 **研究动机**：自进化技能系统把技能获取从外部市场移入可信内部管线，但该管线引入可被诱导轨迹操纵的新攻击面
- 🔬 **研究方法**：Trajectory Backdoor Attack 仅通过查询诱导受损轨迹：让 agent 执行目标动作并在轨迹中显式写明触发条件，跨任务重复条件-动作模式促使演化器固化为技能
- 📌 **结论**：三基准、两技能演化系统、四骨干模型上可靠植入条件后门且保持干净效用，媲美甚至超越直接技能注入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic skills improve large language model (LLM) agents by encoding reusable procedures for complex tasks. However, manually authored skills often adapt poorly to long-horizon tasks and changing environments. To address the limitation, self-evolving skill systems have been developed to automatically construct and update skills from execution trajectories, shifting skill acquisition from external marketplaces to a trusted evolution pipeline. By replacing external skill acquisition with trusted internal construction, self-evolving skill systems reduce exposure to skill injection attacks that rely on direct skill manipulation. However, this skill evolution pipeline may introduce a new attack surface in which an attacker can indirectly steer skill evolution by inducing compromised trajectories through agent interactions. To demonstrate the threat, we propose Trajectory Backdoor Attack (TBA), a query-only attack that steers a trusted skill-evolution pipeline toward producing a backdoored skill. Specifically, we craft attacker-submitted queries to lead the agent to perform the target action and explicitly state the corresponding activation condition in the trajectory. We repeat the same condition-action pattern across diverse triggered tasks, while leaving clean queries unchanged, encouraging the evolver to consolidate the pattern as a reusable trigger-dependent rule into the evolved skill. Experiments on three benchmarks across two skill-evolution systems using four open- and closed-source backbone models demonstrate that TBA reliably implants conditional backdoors while preserving clean-task utility, matching or even surpassing direct skill injection. The results reveal a critical vulnerability in trajectory-driven skill evolution.

</details>

### 28. When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.05810)　📅 2026-08

**关键词**：`defense`、`contamination chain`、`pre-commit gate`、`VaG`

👤 **作者**：Linfang Shang、…、Ning Zheng

- 🎯 **研究动机**：自进化技能池超过临界规模后新技能反而降低性能，缺陷技能的污染链在结构上不可逆、事后回滚收效甚微
- 🔬 **研究方法**：Verifier-as-Gatekeeper 用结构有效性、行为无害、语义一致三个异构评审逐技能过滤，再加边际增益子集选择在顶层消除组合污染
- 📌 **结论**：Terminal-Bench 2 上 VaG 每轮提升至 72% pass@1、技能池约小 5 倍；冻结技能池无需再演化即可正迁移到四个骨干与第二基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We further show the contamination is structurally irreversible: removing a source skill after the fact cannot erase the flawed reasoning its descendants have already inherited, so post-hoc rollback recovers only a small fraction of the lost performance. This makes skill admission a pre-commit necessity rather than a post-hoc fix, and motivates Verifier-as-Gatekeeper (VaG): a progressive trust hierarchy whose three heterogeneous critics - structural validity, behavioral harmlessness, and semantic consistency - filter each skill individually, coupled with a marginal-gain subset selection that removes combinatorial contamination at the top tier before skills reach the runtime context. On Terminal-Bench 2, unconditional accumulation rises to a peak and then degrades, giving back most of its gains as the pool keeps growing, and post-hoc removal of the culprit skills recovers only a small part of the drop - the empirical signature of irreversibility. In contrast, VaG improves every round, reaching 72% pass@1 with a pool roughly 5x smaller, and its frozen skill pool transfers positively to four other backbones and a second benchmark without re-evolution. Ablations confirm the three critics are complementary and mutually non-substitutable, each intercepting a largely disjoint class of harmful skills.

</details>

### 29. When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems

📄 [arXiv](https://arxiv.org/abs/2608.05563)　📅 2026-08

**关键词**：`attack`、`experience promotion`、`trajectory poisoning`、`persistent instruction`

👤 **作者**：Jialuo Chen、…、Jingyi Wang

- 🎯 **研究动机**：自进化技能系统把不可信轨迹蒸馏为可信技能，证据晋升过程构成未被检验的安全边界
- 🔬 **研究方法**：PoisonedEvolution 中黑盒攻击者仅贡献有限证据，使目标行为显得因果有用、可复现且可泛化而被晋升为技能；用惰性金丝雀规格评测四类安全效果
- 📌 **结论**：10% 攻击支持率下 SkillClaw 六个 LLM 演化器中 546/600 试验（91.0% SER）植入目标行为，Trace2Skill 上 61.5% SER，跨演化架构迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving skill (SES) systems distill agent trajectories into persistent skills, allowing untrusted experience to become trusted instruction. We introduce PoisonedEvolution, a trajectory-poisoning attack on this promotion process. Our skill-visible black-box attacker can inspect a target skill and contribute bounded evidence, but cannot observe private pools or evolution logic or edit the skill bank. Artifact poisoning requires Inclusion, Evolution Attribution, and Realization. Attribution is the distinctive bottleneck: the target behavior must appear causally useful, recurrent, and generalizable before promotion. We evaluate four representative security-effect families using inert canary specifications. At 10% attacker support, across six mainstream LLM evolvers in SkillClaw, PoisonedEvolution embeds target behaviors in 546/600 trials (91.0% SER). On the structurally different Trace2Skill pipeline at the same ratio, it embeds target behaviors in 369/600 trials (61.5% SER), demonstrating transfer across evolution architectures. In a representative controlled study, three consistent attacker records suffice in a 30-record batch, whereas a single record is much weaker. Ablations identify recurring support, causal framing, and domain-aligned encoding as the main determinants of success. These findings expose evidence promotion as a security boundary for self-evolving agents.

</details>

### 30. SkillJack: Persistent Skill Backdoors in Self-Evolving Agents

📄 [arXiv](https://arxiv.org/abs/2608.03509)　📅 2026-08

**关键词**：`attack`、`experience-to-skill extraction`、`persistent backdoor`、`artifact deletion`

👤 **作者**：Zonghao Ying、…、Jing Guo

- 🎯 **研究动机**：记忆投毒仅在记录被检索时生效，被投毒经验被 agent 自身转化为持久技能的风险更根本且未被研究
- 🔬 **研究方法**：SkillJack 劫持经验到技能的提取流水线，利用清洗洗白、跨层晋升与持久隔离三特性把恶意行为植入可复用技能库，在 SkillX 与 Anything2Skill 上评测
- 📌 **结论**：SkillX 上安全检测率从投毒轨迹的 98.5% 降至提取技能的 11.4%；植入技能 ASR 达 56.2%/89.2%，删除源记录后 80.0% 攻击仍存活

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present \textbf{SkillJack}, the first attack that exploits the experience-to-skill pipeline of self-evolving agents. Instead of directly manipulating runtime context, SkillJack hijacks the agent's own learning process to implant malicious behaviors into its reusable skill repertoire. We identify three key properties of this transformation: \emph{sanitization whitewashing}, where malicious intent is obscured during skill extraction; \emph{cross-layer promotion}, where transient experiences become persistent capabilities; and \emph{persistence isolation}, where the attack survives removal of its original source records. We evaluate SkillJack on two representative systems, SkillX and Anything2Skill, using a shared dataset of 150 trajectories across four policy-risk categories. Results show that skill extraction substantially reduces attack detectability: in SkillX, safety detection drops from 98.5\% for poisoned trajectories to 11.4\% for extracted skills, while Anything2Skill shows a similar effect. Meanwhile, the implanted skills remain effective, achieving attack success rates of 56.2\% and 89.2\% on the two systems, respectively. Furthermore, 80.0\% of skill-mediated attacks persist after deleting the original poisoned records, and some skills unintentionally activate on benign queries. Our findings reveal skill evolution as a new attack surface and motivate provenance-aware skill lifecycle protection. Our code is available at https://github.com/Tencent/AI-Infra-Guard/research/skilljack.

</details>

### 31. MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection

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

### 32. Towards a Risk Assessment of Malicious Skill Files in Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.05223)　📅 2026-08

**关键词**：`benchmark`、`malicious shell command`、`MITRE ATT&CK`、`coding agent`

👤 **作者**：Rui Yang、Michael Fu、Kla Tantithamthavorn、Chetan Arora、Joey Chua

- 🎯 **研究动机**：自主编码 agent 的技能接口让恶意 shell 命令可藏于自然语言技能文件，企业风险未量化
- 🔬 **研究方法**：六个 LLM 把 471 条真实 shell 命令转化为 2826 个良性外观技能（映射 11 种 MITRE ATT&CK 战术），三法官 LLM 评审（与人类盲评 kappa=0.85）评测 5629 次运行
- 📌 **结论**：Gemini CLI 95.5-96.1% 运行被利用、Qwen Code 71.6-74.0%，仅 1.99% 运行出现显式安全识别，企业须先评估技能接口风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous coding agents are increasingly embedded in enterprise software workflows with delegated authority over connected systems. Central to this architecture is the agent skills interface: folders of instructions and scripts that agents load dynamically to specialize their behavior. This interface also widens the attack surface, letting malicious shell commands hide within natural-language skill files. We make three contributions. First, an adversarial skill-synthesis method using six LLMs across four families to transform 471 real-world shell commands into benign-appearing skills, released as a benchmark of 2,826 skills mapped to 11 MITRE ATT&CK tactics. Second, a reproducible evaluation pipeline coupling run stratification, evidence anchoring, a refusal veto, and a deterministic declared-intent override with a three-judge LLM-as-a-judge panel, validated against a blind human gold standard (Cohen's kappa = 0.85). Third, a large-scale characterization of two enterprise-grade agents across 5,629 completed runs. Gemini CLI is exploited in 95.5-96.1% of runs and Qwen Code in 71.6-74.0% (raw majority vote to declared-intent-corrected estimate, both within the human gold standard), nearly invariant to the generating model. Explicit safety recognition occurs in only 1.99% of runs. Enterprises must assess and mitigate skill-interface risk before adopting coding agents. Our code and dataset are available at https://github.com/awsm-research/AgentJailbreak

</details>

### 33. OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills

📄 [arXiv](https://arxiv.org/abs/2607.20121)　📅 2026-07

**关键词**：`benchmark`、`real-world skill`、`sandbox`、`behavioral diagnosis`

👤 **作者**：Qiyuan Liu、Tingfeng Hui、Kun Zhan、Kaike Zhang、Ning Miao

- 🎯 **研究动机**：看似无害的第三方 skill 的潜在风险只在实际执行时显现，当前 agent 系统识别与规避能力未知
- 🔬 **研究方法**：构建 OpenSkillRisk：从公开市场收集 263 个风险 skill，按七类威胁分类并配标准用户任务与沙箱，覆盖三个 CLI agent 框架与十三个 SOTA LLM，做行为模式细粒度诊断
- 📌 **结论**：无系统可靠处理风险 skill：最安全配置仍约 17% 执行不安全动作；识别失败、识别而不干预、超出用户意图执行三种失败模式反复出现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios. However, third-party skills can introduce extra security vulnerabilities, as seemingly harmless skills can contain latent safety risks that only emerge during actual execution. In this work, we conduct a systematic investigation into how well current agent systems recognize and avoid such risks. To support quantitative and qualitative evaluation, we construct OpenSkillRisk, a dedicated safety benchmark containing 263 risky skills collected from public skill marketplaces. We classify these skills into seven categories based on their threat types and pair each skill with a standardized user task and a corresponding sandbox for controlled evaluation. Distinct from prior benchmarks, OpenSkillRisk not only covers more realistic and diverse unsafe scenarios, but also provides a fine-grained analysis to diagnose the behavioral patterns of agents in such scenarios. We conduct comprehensive experiments covering three mainstream CLI agent frameworks and thirteen state-of-the-art LLMs. Experimental results show that no tested system handles risky skills reliably: even the safest configurations still execute unsafe actions in about 17% of cases. Context-dependent and system-level risks are especially difficult for current agent systems to avoid. Our behavioral analysis reveals three recurring failure patterns: agents may fail to recognize the risk, recognize it but fail to intervene before acting, or follow skill instructions beyond the user's intended scope. These findings highlight the need to improve both risk reasoning in LLMs and execution control in agent frameworks.

</details>

### 34. Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation

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

### 35. SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills

📄 [arXiv](https://arxiv.org/abs/2606.15899)　📅 2026-06

**关键词**：`benchmark`、`semantic vetting`、`SARS`、`memory-poisoning skill`

👤 **作者**：Ismail Hossain、Sai Puppala、Md Jahangir Alam、Tanzim Ahad、Sajedul Talukder

- 🎯 **研究动机**：开源 skill 生态缺乏安全审查，现有扫描器工作在代码层，对指令层与多 agent 风险结构性失明
- 🔬 **研究方法**：提出 SKILLVETBENCH（HuggingFace 实时榜单）用 LLM-as-Judge 审核 skill，定义 SARS 五维 agentic 风险评分并整合 CVSS v4.0 与 ClawHub 双视图
- 📌 **结论**：78 个确认恶意 skill 零漏报、22 个良性对照零误报（最佳静态基线 SKILLSIEVE 仍漏 15%）；prompt injection 与 memory poisoning 等指令层威胁传统工具漏检 89-100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source LLM agent ecosystems are growing rapidly, yet the security of community-contributed skills - modular tool definitions that extend agent capabilities - remains largely unvetted. The gap we fill: existing scanners operate at the code layer and are structurally blind to instruction-layer and multi-agent risk - natural-language directives that hijack an agent, exfiltrate data through encoded side channels, or chain harm across pipelines - so what is needed is a semantic, multi-dimensional vetting system rather than another signature matcher. We present SKILLVETBENCH, a live public leaderboard on Hugging Face that uses an LLM-as-Judge to vet agent skills. What is new: SARS (Skill Agentic Risk Score), a five-dimensional agentic-risk metric with a principled weighted formula for instruction-following systems. What is integrated: full CVSS v4.0 vector decomposition and a ClawHub dual-view that places our LLM-generated review beside the official marketplace verdict. What is demonstrated: drawing on our companion benchmark paper [ 1], the LLM-as-Judge stage achieves zero false negatives across 78 confirmed-malicious skills and zero false positives across 22 benign controls, while the best static baseline (SKILLSIEVE) still misses 15%; for instruction-layer categories such as Prompt Injection and Memory Poisoning, conventional tools miss between 89% and 100% of threats (e.g., CODEBERT detects none of nine memory-poisoning skills). Detection rates vary from 35% to 95% across four LLM evaluators, motivating ensemble scoring in production deployments.

</details>

### 36. Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2606.15242)　📅 2026-06

**关键词**：`benchmark`、`SCR-Bench`、`capability flow`、`authorization confusion`

👤 **作者**：Yi Xie、Jiawei Du、Yu Cheng、Jiuan Zhou、Zhaoxia Yin

- 🎯 **研究动机**：skill 审查通常孤立评估单个 skill，而真实任务在共享执行上下文中调用多个 skill，单独无害的组合可能有害（Skill Composition Risk）
- 🔬 **研究方法**：构建 SCR-Bench（沙箱化三个子基准：CapFlow 能力流、TrustLift 信任转移、AuthBlur 授权混淆），记录组合执行的状态变化与路径级结果
- 📌 **结论**：组合路径暴露孤立评估几乎不存在的风险：CapFlow 组合 ASR 达 33.6%（孤立近零），TrustLift 五个后端中四个超 96.5%，AuthBlur 风险批准率较孤立基线增 71.8%；应按激活路径而非孤立工件评估 skill 安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skills are becoming the capability layer through which LLM agents turn plans into actions, but their use introduces security risks such as data leakage, unauthorized operations, and tool misuse. Existing vetting usually evaluates each skill in isolation, while real agent tasks often invoke multiple skills in a shared execution context. This creates Skill Composition Risk (SCR): a skill that appears benign alone can become harmful when its outputs, trust signals, authorization cues, or side effects influence later invocations along an activated path. We introduce SCR-Bench to evaluate this risk in controlled, sandboxed skill environments. Rather than relying only on textual intent or surface behavior, SCR-Bench records downstream state changes and path-level outcomes across composed skill executions. It contains three sub-benchmarks: SCR-CapFlow for capability-flow composition, SCR-TrustLift for trust-transfer composition, and SCR-AuthBlur for authorization-confusion composition. Across SCR-Bench, composed paths expose risks that are largely absent under isolated evaluation. In SCR-CapFlow, attack success rate reaches 33.6 percent under composition, compared with near-zero isolated baselines. In SCR-TrustLift, attack success rate exceeds 96.5 percent on four of five backends. In SCR-AuthBlur, the risky-approval rate increases by 71.8 percent relative to the L0 isolated baseline under the L1 context setting. These results show that agent skill security should be assessed at the level of activated paths rather than isolated artifacts. SCR and SCR-Bench provide a foundation for path-aware risk evaluation and defense in LLM agent skill ecosystems. Benchmark: https://github.com/saint-viperx/SCR_Bench.

</details>

### 37. MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills

📄 [arXiv](https://arxiv.org/abs/2606.07131)　📅 2026-06

**关键词**：`benchmark`、`runtime verification`、`hybrid artifact`、`108-cell taxonomy`

👤 **作者**：Wenbo Guo、…、Yang Liu

- 🎯 **研究动机**：检测工具从未在覆盖代码+指令混合空间的经核验真值上测量，恶意 skill 检测有效性未知且 wild-only 评估有偏
- 🔬 **研究方法**：构建 MalSkillBench：3,944 个恶意 skill、三维 108 格分类，其中 3,214 个经 Generate-Verify-Feedback 闭环 Docker 沙箱+系统调用监控+LLM judge 运行时验证，另含 703 wild 与 4,000 匹配良性样本
- 📌 **结论**：最强检测器在代码注入上 98.4% recall 却在 prompt injection 与 agent 控制面攻击上崩溃；wild-only 评分可使排名摆动最多 66 个 recall 点，需联合推理意图、代码与指令

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding agents such as Claude Code and Gemini CLI increasingly extend themselves with third-party skills: markdown packages bundling natural-language instructions, executable scripts, and tool permissions. Because a skill is at once code and agent-facing instruction, it introduces a supply chain dependency whose risk is neither pure code nor pure prompt. Detection tools have never been measured against verified ground truth spanning this hybrid space, leaving their effectiveness unknown and wild-only evaluations biased. We present MalSkillBench, the first runtime-verified benchmark of malicious agent skills: 3,944 malicious skills labeled along a three-dimensional taxonomy of 108 cells. Of these, 3,214 come from a closed-loop Generate-Verify-Feedback pipeline admitting only samples whose malicious behavior fires inside a Docker sandbox under system-call monitoring and an LLM judge; we add 703 in-the-wild and 4,000 matched benign skills. Our measurements are consistent: code injection reaches 94.5% verification yield but prompt injection only 75.8%, the same fragility that later makes it hard to detect; the wild sample is narrow, dominated by one cryptocurrency-theft campaign (86.6% one behavior, 81% from two accounts) with a small but architecturally new tail attacking the agent control plane; the strongest skill-specific detector reaches 98.4% recall on code injection yet collapses on prompt-injection and agent-control attacks, and wild-only scoring swings the ranking by up to 66 recall points; supply-chain scanners and prompt-injection defenses each see only half of a skill, and no combination recovers the code-instruction relationship. Detecting malicious skills therefore requires reasoning jointly over task intent, code, and instructions. We release the dataset, pipeline, baselines, and results.

</details>

### 38. SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction

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

### 39. Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2606.00925)　📅 2026-05

**关键词**：`benchmark`、`semantic vetting`、`sandbox verification`、`ClawHavoc`

👤 **作者**：Ismail Hossain、Sai Puppala、Zhuoran Lu、Sajedul Talukder、Nan Jiang

- 🎯 **研究动机**：开放 skill 生态缺同时评测恶意 skill 检测与运行时验证的基准
- 🔬 **研究方法**：SkillVetBench 两阶段：对自然语言 spec 做语义审查检隐藏恶意意图，再把可疑 skill 放入插桩沙箱执行收集可审计证据；样本取自 OpenClaw 真实生态含 ClawHavoc 供应链事件
- 📌 **结论**：仅语义与签名基线漏掉高达 89% 恶意 skill；运行时攻击集中于 exec、write_file、install_skill、spawn 等少量高权限原语

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open agent platforms allow community contributors to publish reusable skills that agents can invoke at runtime. This extensibility also creates a supply-chain risk: malicious contributors can hide harmful behavior inside skills that appear benign under superficial inspection. However, existing defenses are hard to evaluate because there is no benchmark that measures both malicious-skill detection and runtime verification. We present SkillVetBench, a two-stage security vetting benchmark for open agentic skill ecosystems. The first stage performs semantic vetting over each skill's natural-language specification to detect hidden malicious intent. The second stage executes flagged skills in an instrumented sandbox to observe runtime behavior and collect auditable evidence. We build a benchmark from confirmed malicious skills in the live OpenClaw ecosystem, including samples from the recent ClawHavoc supplychain campaign. Unlike static-only methods, SkillVetBench verifies detected threats with execution traces. Our experiments show that: (1) semantic-only and signature-based baselines are insufficient, missing up to 89\% of malicious skills whose threats arise from natural-language instructions, multicomponent logic, or cross-component interactions; (2) runtime attacks are concentrated in a small set of high-permission primitives, especially exec, write\_file, install\_skill, and spawn; and (3) SkillVetBench provides case studies in which sandbox execution directly supports malicious verdicts with concrete runtime evidence.

</details>

### 40. AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills

📄 [arXiv](https://arxiv.org/abs/2605.13940)　📅 2026-05

**关键词**：`benchmark`、`runtime trust`、`sandbox`、`side-effect verification`

👤 **作者**：Haomin Zhuang、…、Xiangliang Zhang

- 🎯 **研究动机**：恶意 skill 无需请求明显有害动作，可把危害伪装成常规工作流的一部分，现有评测难以捕捉
- 🔬 **研究方法**：AgentTrap 含 91 个恶意与 50 个良性任务、16 个安全影响维度，沙箱中执行完整轨迹并判定攻击成功、拒绝、未触发等结果
- 📌 **结论**：最有信息量的失败不是简单越狱——模型常完成可见用户任务，同时把 skill 引入的不安全副作用当作正常流程执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Third-party skills are becoming the package ecosystem for LLM agents. They package natural-language instructions, helper scripts, templates, documents, and service configuration into reusable workflows. This makes skills useful, but it also introduces a new security problem: a malicious skill does not need to ask the model to perform an obviously harmful action. Instead, it can disguise the harmful behavior as part of a routine workflow, relying on the agent to execute that workflow with high-value permissions and limited human supervision. We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior. AgentTrap contains 141 tasks: 91 malicious tasks and 50 benign utility tasks, covering 16 security-impact dimensions grounded in agent-skill supply-chain threats. In each task, the agent receives an ordinary user request, runs with installed skills that may contain malicious workflow elements, and is executed in a sandboxed environment. AgentTrap then judges complete trajectories for attack success, blocked or refused behavior, attack-not-triggered cases, and no-attack-evidence outcomes. Our central finding is that the most informative failures are not simple jailbreaks. Models often complete the visible user task while treating unsafe side effects introduced by the skill as part of the normal workflow. This motivates runtime evaluation of the concrete model--framework--workspace environment in which users actually delegate work. Code and data are available at https://github.com/zhmzm/AgentTrap and https://huggingface.co/datasets/zhmzm/AgentTrap.

</details>

### 41. SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces

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

### 42. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks

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

### 43. “Do Not Mention This to the User”: Detecting and Understanding Malicious Agent Skills in the Wild

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

### 44. Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

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

### 45. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

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

### 46. SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills

📄 [arXiv](https://arxiv.org/abs/2608.03485)　📅 2026-08

**关键词**：`detection`、`honey world`、`dynamic testing`、`trace attribution`

👤 **作者**：Nizhang Li、…、Xiangzheng Zhang

- 🎯 **研究动机**：静态分析与一次性语义判断难以暴露技能在特定环境状态或交互历史下才显现的恶意行为
- 🔬 **研究方法**：SkillSentry 推断技能能力边界，构建含受控诱饵资源的 LLM 模拟环境自适应生成任务，对比有/无技能的轨迹并把可疑行为溯源到源代码与执行迹
- 📌 **结论**：标准基准上 Recall 99.50%、平均 F1 96.26%；语义保持规避下 F1 达 92.95%，最强基线仅 80.07%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

External skills extend the capabilities of large language model agents, but also introduce an execution-time attack surface: a skill that appears benign under inspection may reveal harmful behavior only after particular environmental states, resources, or interaction histories are encountered. Existing scanners primarily rely on static analysis, predefined rules, or one-shot semantic judgments, making such conditional behavior difficult to elicit and attribute. We present SkillSentry, a dynamic safety-testing framework based on adaptive honey worlds. SkillSentry infers the intended capability boundary of a skill, constructs an LLM-simulated environment with controlled decoy resources, and adaptively generates tasks to explore its behavioral states. It then compares skill-enabled trajectories with matched no-skill executions, grounding suspicious behaviors in source code and verified execution traces before making a final decision. We evaluate SkillSentry against seven scanner configurations. SkillSentry achieves 99.50% Recall and 96.26% average F1 on standard benchmarks. Under semantics-preserving evasion, it reaches 92.95% average F1, compared with 80.07% for the strongest baselines. Our code is available at https://github.com/nizhangli062-jpg/SkillSentry-Adaptive-Honey-Worlds-for-Dynamic-Safety-Testing-of-Agent-Skills.

</details>

### 47. SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills

📄 [arXiv](https://arxiv.org/abs/2608.08468)　📅 2026-08

**关键词**：`detection`、`static analysis`、`dataflow taint`、`capability mismatch`

👤 **作者**：Xinze Chen、Chi Zhang、Ping Ji、Yimin Liu

- 🎯 **研究动机**：Agent Skills 快速扩散但安全性质欠研究，静态分析的检测能力边界未被度量
- 🔬 **研究方法**：SkillsMetric 五阶段静态分析（模式密度、统计异常、数据流污点、导入异常、能力失配）打分；构建 2266 个技能、16 类攻击的对抗评测集
- 📌 **结论**：AUC 0.93、数据渗出与隐写载荷检出 93%；但常规 shell 的主机破坏攻击 0% 检出、自然语言提示注入仅 42%，静态分析单独不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores skill packages along pattern density, statistical anomaly, dataflow taint, import anomaly, and capability mismatch dimensions. We construct an adversarial evaluation dataset of 2{,}266 skills spanning 16~attack types across code-level, system-level, and semantic-level threats, and evaluate on the full SkillMD-138K corpus. Our framework achieves an AUC of 0.93 and 5-fold cross-validated F1 of 73.4\%$\pm$0.5\%, with strong detection of data exfiltration (93\%) and steganographic payloads (93\%). Crucially, we identify fundamental blind spots: \emph{host destruction} attacks using common shell commands evade all five stages (0\% detection), and \emph{prompt injection} via natural-language manipulation achieves only 42\% detection. These findings establish that static analysis alone is insufficient for skill security, motivating defense-in-depth architectures that combine fast static pre-screening with semantic review.

</details>

### 48. SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents

📄 [arXiv](https://arxiv.org/abs/2607.25619)　📅 2026-07

**关键词**：`detection`、`hybrid gateway`、`snippet review`、`cost efficiency`

👤 **作者**：Rui Yang、Michael Fu、Kla Tantithamthavorn、Chetan Arora、Joey Chua

- 🎯 **研究动机**：coding agent 的 skill 文件可经 npx 一键安装且无安全筛查，恶意 skill 可静默重编程 agent、窃取凭证，注册表已现数百恶意包，缺乏系统工具链防御
- 🔬 **研究方法**：提出 SkillGate 安全网关：regex 预过滤+LLM-judge 混合管线，安全信号文件完全跳过 judge，被标记文件只把匹配片段窗口送审，在 SkillsBench（n=1,650、9.1% 恶意）上评估
- 📌 **结论**：F1=0.817、FPR=1.13%，LLM 输入 token 比全文筛查省 77%，AUPRC 0.830 超现有工具（0.144/0.162）5-6 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Software engineering teams now deploy AI coding agents (Cursor, Claude Code, GitHub Copilot) as first-class productivity tools, installing domain-specific skill files to tailor agent behavior to project APIs, framework conventions, and organizational workflows. These complex Markdown files are easily downloaded from public registries with a single npx skills add command and no real security screening, representing a novel supply-chain attack surface: a malicious skill file can silently reprogram agent behavior, exfiltrating credentials, injecting backdoors into generated code, or redirecting agent actions to attacker-controlled endpoints. The threat is not hypothetical: recent reports document hundreds of malicious skill packages in public registries, including organized campaigns that distributed credential-stealing infostealers via fake productivity skills. No systematic toolchain defense exists for this attack surface. We present SkillGate, a deployable security gateway that screens AI skill packages before coding agent installation. SkillGate uses a hybrid regex-prefilter + LLM-judge pipeline: safe-signal files bypass the LLM entirely (skip savings); flagged files have only their matched snippet windows sent to the judge, not the full content (snippet savings). We answer four research questions covering detection effectiveness, screening cost, runtime overhead, and false positive behavior on the SkillsBench benchmark against two existing tools. On SkillsBench (n=1,650, 9.1% malicious), SkillGate achieves F1=0.817, FPR=1.13% while reducing LLM input tokens by 77% vs. full-file screening, and outperforming existing tools by 5-6x on threshold-independent AUPRC (0.830 vs. 0.144/0.162).

</details>

### 49. Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware

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

### 50. Cross-Layer Misalignment Detection in Agent Skills: A Progressive Loading-Aware Contrastive Learning Approach

📄 [arXiv](https://arxiv.org/abs/2607.10534)　📅 2026-07

**关键词**：`detection`、`metadata mismatch`、`progressive loading`、`contrastive learning`

👤 **作者**：Chengjun Zhang、Yang Gao、Jianna Hur、Jingjing Zhang、Sagar Samtani

- 🎯 **研究动机**：skill 元数据与其真实行为的不一致（跨层失准）随市场扩张而难以发现
- 🔬 **研究方法**：提出 PL-HCL：建模 Agent Skill 的分层结构并学习跨层一致性，用超 26.4 万个开源 skill 归一化语料与人工核验挑战集训练
- 📌 **结论**：Macro-F1 从未适配基线的约 0.45 提升到 0.87-0.89，为用户与运营方提供有效筛查工具

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents are increasingly extended through Agent Skills, reusable artifacts that package natural-language metadata, procedural instructions, and execution-time resources for runtime use. As open-source skill marketplaces expand, users and agents increasingly rely on brief metadata to select third-party skills, making it difficult to detect inconsistencies between a skill's description and its true behavior, a problem we call cross-layer misalignment. To address this issue, we propose Progressive Loading-Aware Hierarchical Contrastive Learning (PL-HCL), an LLM-based framework that detects misalignment by modeling the layered structure of Agent Skills and learning cross-layer consistency. Using a normalized corpus of over 264,000 open-source skills and a human-verified challenge set, PL-HCL improves Macro-F1 from approximately 0.45 for unadapted baselines to 0.87-0.89 across evaluated LLM backbones. This approach offers an effective screening tool for users and operators, as well as design principles for detecting inconsistencies in layered digital artifacts.

</details>

### 51. VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills

📄 [arXiv](https://arxiv.org/abs/2606.26524)　📅 2026-06

**关键词**：`defense`、`runtime enforcement`、`temporal policy`、`SMT`

👤 **作者**：Ying Li、…、Yuan Tian

- 🎯 **研究动机**：skill 的自然语言规范描述了行为边界但不提供可执行运行时强制，固定事件模型的监控粒度不当会误拦或漏检跨动作违规
- 🔬 **研究方法**：提出 VIGIL：策略语言刻画上下文相关的时序依赖、参数约束与值流条件，符号求值规则把策略转为有限迹上的 SMT 约束，对 agent 执行轨迹做运行时检查
- 📌 **结论**：真实 LLM agent 运行（办公、运维、工程任务）上违规召回超 95%、误报低于 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic systems increasingly act through third-party skills, allowing model-generated decisions to affect files, communication channels, and cyber-physical devices. These skills often include natural-language specifications that define access permissions, disclosure limits, execution privileges, and required preconditions. Although such specifications describe the intended boundaries of skill behavior, they do not by themselves provide executable runtime enforcement. Enforcing them raises a contextual granularity challenge: even when a policy is written for a particular task context, a monitor must still decide which events to observe, what state to retain, how far across the execution to reason, and where to intervene. Choosing the wrong granularity can either block benign executions or miss violations that emerge only across multiple actions. Most existing enforcement mechanisms, however, assume a fixed event model or enforcement point. In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. VIGIL checks an agent's actual execution trace against behavioral policies from skill specifications, operator-defined constraints, and global rules spanning multiple skills. To make such policies executable, VIGIL introduces a policy language that captures context-specific enforcement requirements over agent-tool events, including temporal dependencies, argument constraints, and value-flow conditions. The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. On real LLM-agent runs spanning office-document, operational, and engineering tasks, VIGIL detects policy violations with over 95% recall and a false-positive rate below 10%.

</details>

### 52. Detecting Malicious Agent Skills in the Wild using Attention

📄 [arXiv](https://arxiv.org/abs/2606.23416)　📅 2026-06

**关键词**：`detection`、`attention locator`、`marketplace scan`、`cost reduction`

👤 **作者**：Bacem Etteib、Daniele Lunghi、Tégawendé F. Bissyandé

- 🎯 **研究动机**：skill 本身就是指令集合，prompt injection 防御赖以成立的可信指令-不可信数据边界失效，恶意 skill 检测缺乏可扩展方案
- 🔬 **研究方法**：提出 Locate-and-Judge 两段检测：轻量定位器按各结构片段获得的指令跟随注意力打分保留 top-K，judge 只详查高注意力片段
- 📌 **结论**：比直接 LLM 扫描降一个数量级成本即可审计整个市场，高精度标记出数十个在用恶意 skill，其中多个伪装成良性功能且被 SkillSpector 与 Cisco 扫描器漏检

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly load skills, file-based packages of natural-language instructions written by third parties and distributed through marketplaces, that execute with the user's privileges. A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. Prompt-injection defenses do not carry over to this setting. They rely on a boundary between trusted instructions and untrusted data, whereas a skill is itself a body of instructions, so an injected command sits among many legitimate ones and inherits their authority. We present Locate-and-Judge, a two-stage detector designed for this regime. A lightweight locator scores the structural spans of a skill by the instruction-following attention each span draws and retains only the top-K. A judge then examines the retained spans in detail. Concentrating the costly judgment on a few high-attention spans lets the detector audit an entire marketplace instead of a sample. Compared to direct LLM-based scanning, this approach offers an order-of-magnitude cost reduction, dramatically increasing its scalability at a small cost to recall, and it dominates keyword and regex baselines at comparable expense. Deployed at marketplace scale and at negligible cost, Locate-and-Judge flags skills with high precision, the majority of which we manually confirmed as malicious, surfacing dozens of live malicious skills, including several disguised as benign functionality and many that SkillSpector and Cisco Skill Scanner fail to detect. We release the resulting labeled dataset.

</details>

### 53. SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills

📄 [arXiv](https://arxiv.org/abs/2606.14154)　📅 2026-06

**关键词**：`detection`、`language-code attack`、`adversarial mutation`、`local scanner`

👤 **作者**：Youngduk Kim、Minkyoo Song、Seungwon Shin

- 🎯 **研究动机**：skill 安全依赖自然语言说明与可执行代码的跨模态推理，SKILL.md 良性而指令隐性引导 exfiltration 的跨模态攻击未被测量
- 🔬 **研究方法**：提出 SkillMutator 基准：模拟 13 类攻击下的对抗变异过程迭代逼近检测器，并提出四阶段推理轨迹蒸馏把前沿教师 trace 蒸馏进小型开源模型做本地扫描器
- 📌 **结论**：开源与商业扫描器仅检出 2%-17% 此类攻击；蒸馏的 Qwen2.5-Coder-7B 在最难子集把检出率从 17.1% 提到 88.2%，超过 GPT-5.4-mini（79.0%）、接近 GPT-5.4（86.8%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly extend their capabilities at runtime by loading Agent Skills, which pair natural-language specifications (SKILL.md) with executable scripts and resources. Because a skill's behavior relies on both natural-language instructions and executable code, assessing its safety requires cross-modal reasoning, creating a new language-and-code attack surface. Attackers can present a benign workflow in SKILL.md while embedding implicit directives that steer the agent to exfiltrate sensitive files, even if the scripts appear harmless. This attack surface remains understudied; prior work treats skills merely as prompt-injection vectors or static code artifacts, leaving attacks emerging from cross-modal interactions largely unmeasured. In our evaluation, open-source and commercial skill scanners detect only 2%-8% and 9%-17% of such attacks, respectively. To address this gap, we introduce SkillMutator, the first benchmark for install-time detection of language-and-code cross-modal attacks on Agent Skills. It emulates an adversarial mutation process across 13 attack categories, iteratively refining malicious skills using scanner feedback to make injected behaviors indistinguishable from legitimate workflows. We further propose a four-phase reasoning-trajectory distillation framework to distill frontier-teacher traces into smaller open-weight models. This produces a locally deployable scanner avoiding third-party data exposure and excessive API costs. On the strongest SkillMutator subset (n=76), our distilled model (Qwen2.5-Coder-7B-Instruct) improves detection from 17.1% to 88.2%, surpassing GPT-4o-mini (23.7%) and GPT-5.4-mini (79.0%), and reaching frontier-level GPT-5.4 (86.8%). These results show practical defense against cross-modal attacks is feasible without relying on costly frontier models.

</details>

### 54. Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

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

### 55. SkillGuard: A Permission-Centric Framework for Agent Skill Security

📄 [arXiv](https://arxiv.org/abs/2606.03024)　📅 2026-06

**关键词**：`defense`、`permission model`、`context influence`、`runtime side effect`

👤 **作者**：Shidong Pan、Xiaoyu Sun、Tianyi Zhang、Dianshu Liao、Kaiwen Yang、Zhenchang Xing

- 🎯 **研究动机**：Agent skill 既能在工具调用前改变推理又能导向带副作用的行为，现有生态缺少覆盖这种双重角色的权限模型
- 🔬 **研究方法**：提出 SkillGuard，把 skill 视为携带权限的可执行工件，通过 skill manifest、运行时权限控制、用户交互与策略执行构成双平面治理，同时约束上下文影响与动作副作用
- 📌 **结论**：1,260 个真实 skill 上权限分类覆盖 99.93% 受保护对象；SkillInject 数据集上上下文注入 ASR 从 35.3% 降至 20.7%，明显注入从 36.7% 降至 18.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Skills extend LLM agents with reusable instructions, scripts, data, and tool bindings. This shift makes skills a new security principal in agent systems: a skill can alter the agent's reasoning before any tool is called, and it can also steer the agent toward actions with concrete side effects. However, current skill ecosystems lack a permission model that captures this dual role. Existing defenses either inspect skill files before use or constrain individual tool calls during execution, leaving the connection between skill-level intent, contextual influence, and runtime behavior weakly governed. In this paper, we present SkillGuard, a skill-centric permission framework that treats skills as permission-bearing executable artifacts. SkillGuard introduces a dual-plane governance model that jointly regulates context influence and action side effects through skill manifests, runtime permission control, user interaction, and policy enforcement. We evaluate the permission taxonomy expressiveness on 1,260 real-world skills, and 99.93% of observed protected objects are covered. In adversarial evaluations on SkillInject dataset, SkillGuard reduces attack success rate from 35.3% to 20.7% for contextual injections and from 36.7% to 18.0% for obvious injections, while decently maintaining benign task completion. These results suggest that SkillGuard, as a skill-centric permission framework, can provide a practical foundation for improving the security of agent skill ecosystems.

</details>

### 56. Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents

📄 [arXiv](https://arxiv.org/abs/2606.01567)　📅 2026-06

**关键词**：`defense`、`guardian agent`、`static rewrite`、`attack reframing`

👤 **作者**：Yoshinari Fujinuma、…、Anand Kannappan

- 🎯 **研究动机**：skill 文档成为 agent 新攻击面，guardian 式防御及其对自适应攻击的抵抗力未被研究
- 🔬 **研究方法**：评测两类 guardian：动态 guardian 中介 skill 文件访问、静态 guardian 构建时预改写；以四种保留恶意指令只改措辞的 attack reframing 做压力测试
- 📌 **结论**：三个 LLM agent 家族上 guardian 削减 ASR 过半且保任务效用；reframing 把无防护 ASR 推至 81.4% 时动态 guardian 仍压到 18.6%，实时中介更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on reusable skills i.e. documents describing task-specific procedures. However, this introduces a new attack surface for agents to manage. We study two complementary directions for this threat. First, we evaluate guardian-based defenses: an intermediary LLM agent that acts as a mediator for skill file access (dynamic guardian) or pre-rewrites these files at build time (static guardian). Across three LLM agent families, our guardians cut attack success rate (ASR) by well over half while preserving task utility. Second, we stress test them through attack reframing using four attacks that preserve the malicious instruction but change the phrasing. For non-guardian setup, the reframing pushes the ASR up to 81.4\%, but the dynamic guardian brings it down to 18.6\%, showing that real-time mediation is a robust defense.

</details>

### 57. Behavioral Integrity Verification for AI Agent Skills

📄 [arXiv](https://arxiv.org/abs/2605.11770)　📅 2026-05

**关键词**：`detection`、`declared-vs-actual capability`、`hybrid analysis`、`registry audit`

👤 **作者**：Yuhao Wu、Tung-Ling Li、Hongliang Liu

- 🎯 **研究动机**：现有安全工作抓恶意 prompt 与危险运行时动作，但 skill 工件声明与实际能力是否一致无人验证
- 🔬 **研究方法**：BIV 形式化为共享 taxonomy 上的声明-实际能力类型集合比较，确定性代码分析配 LLM 辅助能力抽取，支持偏差分类、根因归因与恶意检测
- 📌 **结论**：OpenClaw 49,943 个 skill 中 80.0% 偏离声明行为（81.1% 源于疏忽、18.9% 恶意，5.0% 带多阶段攻击链）；906-skill 恶意检测 F1 达 0.946

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend LLM agents with privileged third-party capabilities such as filesystem access, credentials, network calls, and shell execution. Existing safety work catches malicious prompts and risky runtime actions, but the skill artifact itself goes unverified. We formalize this as the behavioral integrity verification (BIV) problem: a typed set comparison between declared and actual capabilities over a shared taxonomy that bridges code, instructions, and metadata. The BIV framework instantiates this comparison by pairing deterministic code analysis with LLM-assisted capability extraction. The resulting structured evidence supports three downstream analyses: deviation taxonomy, root-cause classification, and malicious-skill detection. On 49,943 skills from the OpenClaw registry, the deviation taxonomy reveals a pervasive description-implementation gap: 80.0% of skills deviate from declared behavior, with four novel compound-threat categories surfaced. Root-cause classification finds that deviations are mostly oversight, not malice: 81.1% trace to developer oversight and 18.9% to adversarial intent, with 5.0% of skills carrying predicted multi-stage attack chains. On a 906-skill malicious-skill detection benchmark, BIV reaches an F1 of 0.946, outperforming state-of-the-art rule-based and single-pass LLM baselines. These results demonstrate behavioral integrity auditing for agent skills at scale.

</details>

### 58. SkillScope: Toward Fine-Grained Least-Privilege Enforcement for Agent Skills

📄 [arXiv](https://arxiv.org/abs/2605.05868)　📅 2026-05

**关键词**：`defense`、`least privilege`、`task-conditioned analysis`、`control-flow constraint`

👤 **作者**：Jiangrong Wu、…、Zibin Zheng

- 🎯 **研究动机**：Skill 越权本质是任务条件化的——同一动作在一个 prompt 下必要、在另一个下越权，现有检测不适用
- 🔬 **研究方法**：SkillScope 以图把指令级流程与代码级操作建模为细粒度动作节点，在图实例化用户任务上做 replay 验证越权候选，再经控制流约束限权
- 📌 **结论**：越权检测 F1 达 94.53%，实测 7,039 个真实 Skill 存在越权行为；约束后任务内越权动作实例减少 88.56% 且保留合法完成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills have become a practical way to extend LLM agents by packaging metadata, natural-language instructions, and executable resources into reusable capability bundles. However, this growing Skill ecosystem introduces a new compliance risk: a Skill may perform high-impact actions that exceed the minimum necessary scope of the user's current task, thereby violating least-privilege. Existing skill detection approaches are insufficient for this problem because it is inherently task-conditioned: the same action may be necessary under one user prompt but over-privileged under another. In this paper, we present SkillScope, a framework for fine-grained least-privilege enforcement in Agent Skills. SkillScope adopts a graph-based analysis approach that models instruction-level procedures and code-level operations as fine-grained action nodes. It extracts potential over-privilege candidates, validates them under graph-instantiated user tasks through replay-based analysis, and constrains validated over-privileged actions via control-flow privilege constraining. We evaluate SkillScope through effectiveness experiments and large-scale real-world measurement. SkillScope achieves 94.53% F1 for skill over-privilege detection. In the wild, SkillScope validates 7,039 Skills with over-privileged behaviors, showing that least-privilege violations are prevalent in current Skill ecosystems. In the privilege-constraining evaluation, SkillScope reduces triggered over-privileged action-in-task instances by 88.56% while preserving legitimate task completion.

</details>

### 59. Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis

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

### 60. RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents

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

### 61. MalSkills: Detecting Malicious Skills in the Agentic Supply Chain via Neuro-symbolic Reasoning

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

### 62. SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration

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