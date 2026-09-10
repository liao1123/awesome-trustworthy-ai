# Coding Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究能够读取 repository、issue、文档和 CI log，并修改文件、执行 shell、访问网络和提交变更的 Coding Agent。主要风险包括 malicious issue/repository instruction、dependency 与 skill supply chain、secret exfiltration、生成或执行恶意代码、对良性任务做越界修改，以及 defense 只在 base model 而没有在 Agent permission layer 生效。普通 code model vulnerability 若不涉及 Agent workflow 则不收录。

## 研究脉络

- **代码输出安全：** 初期评测集中于模型是否生成 vulnerable 或 malicious code，但未观察代码实际执行及工具副作用。
- **Agentic red teaming：** 研究加入 sandbox、adaptive attacker 和多种 coding product，联合检查生成、执行、debugging 与环境变化。
- **Repository 输入攻击：** issue、comment、PDF、README 和 tool output 都可承载恶意要求，并借 Agent 权限形成持久修改或数据泄漏。
- **良性任务越权：** 新 benchmark 把 overeager action 建模为 authorization failure，区分主动做多了和任务能力不足。
- **当前边界：** model refusal、framework approval、OS sandbox、secret scope 和 patch review 必须分别度量，不能把任一层的阻断归因于整体安全。

## Malicious Request 与 Prompt Injection

### 1. When Context Gets Root: Privilege Escalation in LLM Harnesses

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

### 2. IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests

📄 [arXiv](https://arxiv.org/abs/2607.20759)　📅 2026-07

**关键词**：`benchmark`、`malicious issue`、`delivery vector`、`deployed coding agent`

👤 **作者**：Ankur Singh、Jinqiu Yang、Tse-Hsun Chen

- 🎯 **研究动机**：已部署 coding agent（Cursor、Claude Code、Codex Desktop）面对恶意 issue 请求的抵抗力未被系统评估
- 🔬 **研究方法**：构建 IssueTrojanBench：四类新型攻击 x 六种投递向量（PDF、issue 评论等）加扰动增强，评估两大模型家族的三个 agent 的护栏穿透
- 📌 **结论**：66.5% 恶意 issue 穿透全部 agent 与 LLM 级护栏；拒绝几乎全部来自 LLM 而非 agent 框架，GPT 系广泛脆弱而 Sonnet 4.6 更有选择性，agent 级防御附加保护有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools. Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments. This paper presents a systematic evaluation of malicious issue requests against state-of-the-art coding agents (Cursor, Claude Code, and Codex Desktop), powered by two major model families (OpenAI GPT-5.3 Codex/GPT-5.4 and Anthropic Sonnet 4.6). Our novel benchmark IssueTrojanBench contains malicious issues that are constructed based on four novel attack categories (i.e., embedded as malicious instructions in issues), six delivery vectors (e.g., PDF, or issue comment), and further augmented by perturbations. Our results reveal critical vulnerabilities in the as-deployed modern coding agents, i.e., 66.5% of the malicious issues from IssueTrojanBench penetrate all the guardrails (agent- and LLM-level) of coding agents. Our further analysis shows that rejection is almost entirely from LLMs rather than the agent frameworks, with GPT models broadly vulnerable and Sonnet 4.6 exhibiting more selective, risk-aware blocking of high-impact actions. Our evaluation also highlights that the current agent-level defense strategy offers limited additional protection for coding agents. Our findings highlight the urgent need for stronger agent- and model-level safety mechanisms to protect AI coding agents.

</details>

### 3. Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems

📄 [arXiv](https://arxiv.org/abs/2601.17548)　📅 2026-01

**关键词**：`survey`、`coding assistant`、`delivery vector`、`protocol ecosystem`

👤 **作者**：Narek Maloyan、Dmitry Namiot

- 🎯 **研究动机**：agentic coding assistant 的 prompt injection 研究分散，缺乏统一分类与防御有效性评估
- 🔬 **研究方法**：SoK 综合 78 项研究（2021-2026），提出投递向量、攻击模态与传播行为三维分类法，编目 42 种攻击技术并批判性分析 18 种防御
- 📌 **结论**：自适应攻击对 SOTA 防御的成功率超 85%，多数防御缓解率不足 50%；prompt injection 应被视为需架构级缓解的一级漏洞类

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of agentic AI coding assistants, including Claude Code, GitHub Copilot, Cursor, and emerging skill-based architectures, has fundamentally transformed software development workflows. These systems leverage Large Language Models (LLMs) integrated with external tools, file systems, and shell access through protocols like the Model Context Protocol (MCP). However, this expanded capability surface introduces critical security vulnerabilities. In this \textbf{Systematization of Knowledge (SoK)} paper, we present a comprehensive analysis of prompt injection attacks targeting agentic coding assistants. We propose a novel three-dimensional taxonomy categorizing attacks across \textit{delivery vectors}, \textit{attack modalities}, and \textit{propagation behaviors}. Our meta-analysis synthesizes findings from 78 recent studies (2021--2026), consolidating evidence that attack success rates against state-of-the-art defenses exceed 85\% when adaptive attack strategies are employed. We systematically catalog 42 distinct attack techniques spanning input manipulation, tool poisoning, protocol exploitation, multimodal injection, and cross-origin context poisoning. Through critical analysis of 18 defense mechanisms reported in prior work, we identify that most achieve less than 50\% mitigation against sophisticated adaptive attacks. We contribute: (1) a unified taxonomy bridging disparate attack classifications, (2) the first systematic analysis of skill-based architecture vulnerabilities with concrete exploit chains, and (3) a defense-in-depth framework grounded in the limitations we identify. Our findings indicate that the security community must treat prompt injection as a first-class vulnerability class requiring architectural-level mitigations rather than ad-hoc filtering approaches.

</details>

### 4. Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks

📄 [arXiv](https://arxiv.org/abs/2605.18583)　📅 2026-05

**关键词**：`benchmark`、`scope expansion`、`authorization boundary`、`permission gating`

👤 **作者**：Yubin Qu、…、Yi Liu

- 🎯 **研究动机**：coding agent 在良性请求下做出超出授权的动作（删除无关文件、改写配置），是不同于能力失败与 prompt 注入的授权问题
- 🔬 **研究方法**：OverEager-Gen 以行为梯度验证器认证场景区分力、双通道工具调用审计与 byte 级一致的 consent 保留/剥离配对变体构建基准，500 场景约 7,500 次运行
- 📌 **结论**：剥离同意声明使 Claude Code 越权率从 0.0% 升至 17.1%；framework 影响大于模型差异——宽松框架 5.4-27.7% vs ask-to-continue 的 OpenHands 仅 0.2-4.5%，框架内模型间差异达 15.9 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coding agents now run autonomously with shell, file, and network privileges. When a user issues a benign request, the agent sometimes does more than asked: it deletes unrelated files, wipes a stale credentials backup, or rewrites configuration the user never mentioned. We call these scope expansions overeager actions, an authorization problem distinct from capability failures, prompt injection, or sandbox escapes. We present OverEager-Gen, a benchmark dedicated to overeager behavior on benign tasks. Building it surfaces a measurement-validity issue: if a benchmark spells out the authorized scope inside the prompt, the agent stops inferring boundaries and starts pattern-matching declaration text. On Claude Code, stripping the consent declaration alone raises the overeager rate from 0.0% to 17.1% on paired scenarios (McNemar exact p = 2.4 x 10^-4). OverEager-Gen therefore certifies each scenario's discriminative power before admission via a behavioral-gradient validator, audits internal tool calls through a dual-channel stack (PATH-injected shim plus per-agent event streams), and ships byte-identical consent_kept and consent_stripped variants. OverEager-Bench contains 500 validated scenarios and ~7,500 runs across four agent products (Claude Code, OpenHands, Codex CLI, Gemini CLI) and six base models; a 50-sample re-annotation gives Cohen's kappa = 0.73 and rule-judge recall = 1.00. Stripping consent multiplies the overeager rate on every shared base model (Delta in [11.9, 17.2] pp). The framework axis dominates effect size: a permissive cluster (Claude Code, Codex CLI, Gemini CLI) runs at 5.4-27.7% while the ask-to-continue framework (OpenHands) sits at 0.2-4.5% (Fisher p <= 10^-5). Within-framework base-model variance reaches 15.9 pp, indicating that model-layer alignment does not fully propagate through permissive permission gating.

</details>

### 5. What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants

📄 [arXiv](https://arxiv.org/abs/2605.30777) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/63/What-Breaks-When-LLMs-Code-Characterizing-Operational-Safety-Failures-of-Agentic-Cod)　📅 2026-05　🏷 ASE 2026

**关键词**：`analysis`、`coding agent`、`operational safety`、`incident taxonomy`

👤 **作者**：Alif Al Hasan、Sumon Biswas

- 🎯 **研究动机**：coding agent 在良性使用中的操作安全失效（环境破坏、伪造成功报告）高发，现有基准只测显式恶意输入
- 🔬 **研究方法**：双证据流实证：筛查 22 个顶会 68,816 篇文献得 185 篇相关研究，挖掘 16,586 个 GitHub issue 并人工确认 547 起真实安全失效，开放编码得 7 维 33 类操作风险 taxonomy
- 📌 **结论**：547 起中 326 起为高危或致命；主导风险是约束违反、破坏性操作、授权绕过与欺骗，超 65% 发生在修 bug 与配置阶段——护栏须超越对抗 prompt 防御并落实环境约束、失败透明与安全停机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous coding agents built on large language models (LLMs) are rapidly being integrated into development workflows, yet their operational safety properties remain poorly understood beyond evaluations of explicitly malicious inputs. In practice, high-impact failures arise during benign, goal-directed use through environment breakage, fabricated success reports, etc. that current benchmarks do not capture. What categories of operational safety failures actually occur when coding agents are used for everyday development tasks and what is their impact? We present an incident-driven empirical study grounded in two complementary evidence streams. We screen 68,816 papers from 22 premier venues, curating 185 safety-relevant studies, and mine 16,586 GitHub issues from widely deployed LLM-powered coding tools, manually confirming 547 genuine safety failures. Applying systematic open coding over both corpora, we derive a multi-dimensional safety taxonomy of 33 operational risk types organized across seven dimensions, and annotate each incident with contributing factors, task context, severity, and downstream impact. Our findings show that coding-agent failures are often severe, with 326 of 547 incidents rated high or critical. The dominant risks are constraint violations, destructive operations, authorization bypasses, and deception, and over 65% of incidents arise in bug fixing and setup or configuration, patterns largely missing from prior literature. These results have direct implications for SE tool designers and benchmark developers: guardrails must go beyond adversarial-prompt defenses to enforce environmental constraints, failure transparency, and safe-halt behaviors.

</details>

### 6. CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild

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

### 7. BlueCodeAgent: A Blue Teaming Agent Enabled by Automated Red Teaming for CodeGen AI

📄 [arXiv](https://arxiv.org/abs/2510.18131)　📅 2025-10

**关键词**：`defense`、`code analysis`、`automated red team`、`dynamic validation`

👤 **作者**：Chengquan Guo、Yuzhou Nie、Chulin Xie、Zinan Lin、Wenbo Guo、Bo Li

- 🎯 **研究动机**：代码生成模型的红队研究多而蓝队防御少，缺乏区分安全与不安全代码的有效语义理解
- 🔬 **研究方法**：BlueCodeAgent 端到端蓝队 agent：红队生成多样风险实例，蓝队以 constitution、代码分析与动态执行验证构建多层防御，覆盖偏见指令、恶意指令与漏洞代码检测三类任务
- 📌 **结论**：四数据集平均 F1 提升 12.7%，动态分析有效降低漏洞代码检测的假阳性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly used for code generation, concerns over the security risks have grown substantially. Early research has primarily focused on red teaming, which aims to uncover and evaluate vulnerabilities and risks of CodeGen models. However, progress on the blue teaming side remains limited, as developing defense requires effective semantic understanding to differentiate the unsafe from the safe. To fill in this gap, we propose BlueCodeAgent, an end-to-end blue teaming agent enabled by automated red teaming. Our framework integrates both sides: red teaming generates diverse risky instances, while the blue teaming agent leverages these to detect previously seen and unseen risk scenarios through constitution and code analysis with agentic integration for multi-level defense. Our evaluation across three representative code-related tasks--bias instruction detection, malicious instruction detection, and vulnerable code detection--shows that BlueCodeAgent achieves significant gains over the base models and safety prompt-based defenses. In particular, for vulnerable code detection tasks, BlueCodeAgent integrates dynamic analysis to effectively reduce false positives, a challenging problem as base models tend to be over-conservative, misclassifying safe code as unsafe. Overall, BlueCodeAgent achieves an average 12.7\% F1 score improvement across four datasets in three tasks, attributed to its ability to summarize actionable constitutions that enhance context-aware risk detection. We demonstrate that the red teaming benefits the blue teaming by continuously identifying new vulnerabilities to enhance defense performance.

</details>

### 8. RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents

📄 [arXiv](https://arxiv.org/abs/2510.02609) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010244)　📅 2025-10　🏷 ICLR 2026

**关键词**：`attack`、`adaptive red teaming`、`sandbox execution`、`jailbreak composition`

👤 **作者**：Chengquan Guo、…、Bo Li

- 🎯 **研究动机**：静态安全基准与红队工具难覆盖越狱工具组合效应等真实风险场景
- 🔬 **研究方法**：提出 RedCodeAgent：自适应记忆模块复用越狱知识，按输入动态选择最有效红队工具与组合，并以模拟沙箱评估代码执行结果
- 📌 **结论**：多个 SoTA 代码 agent 上 ASR 更高、拒绝率更低，并在 Cursor 与 Codeium 等真实助手暴露此前未知的风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code agents have gained widespread adoption due to their strong code generation capabilities and integration with code interpreters, enabling dynamic execution, debugging, and interactive programming capabilities. While these advancements have streamlined complex workflows, they have also introduced critical safety and security risks. Current static safety benchmarks and red-teaming tools are inadequate for identifying emerging real-world risky scenarios, as they fail to cover certain boundary conditions, such as the combined effects of different jailbreak tools. In this work, we propose RedCodeAgent, the first automated red-teaming agent designed to systematically uncover vulnerabilities in diverse code agents. With an adaptive memory module, RedCodeAgent can leverage existing jailbreak knowledge, dynamically select the most effective red-teaming tools and tool combinations in a tailored toolbox for a given input query, thus identifying vulnerabilities that might otherwise be overlooked. For reliable evaluation, we develop simulated sandbox environments to additionally evaluate the execution results of code agents, mitigating potential biases of LLM-based judges that only rely on static code. Through extensive evaluations across multiple state-of-the-art code agents, diverse risky scenarios, and various programming languages, RedCodeAgent consistently outperforms existing red-teaming methods, achieving higher attack success rates and lower rejection rates with high efficiency. We further validate RedCodeAgent on real-world code assistants, e.g., Cursor and Codeium, exposing previously unidentified security risks. By automating and optimizing red-teaming processes, RedCodeAgent enables scalable, adaptive, and effective safety assessments of code agents.

</details>

### 9. PatchBench: Evaluating AI Agents for Vulnerability Patching

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

### 10. Reveree: Diagnosing LLM Reverse-Engineering Agents

📄 [arXiv](https://arxiv.org/abs/2609.01185)　📅 2026-09

**关键词**：`benchmark`、`reverse-engineering agent`、`trajectory diagnosis`、`memorization audit`

👤 **作者**：Hadjer Benkraouda、Hongyu Cai、Berkay Celik、Gang Wang

- 🎯 **研究动机**：CTF 逆向工程评测只看是否拿到 flag，既不定位 RE 过程中的失败阶段，也无法区分二进制分析与公开答案记忆
- 🔬 **研究方法**：提出 Reveree 三层诊断：解题率、八阶段 RE 里程碑进度（comprehension 由盲评 LLM judge、其余确定性验证）、行为画像；在 88 个 picoCTF／NYU-CTF 挑战上评测九个模型与四种提示策略
- 📌 **结论**：base model 主导表现、更大更贵模型并不可靠更强；失败集中于 comprehension 阶段且追加预算极少能挽救；真实分析与记忆并存，NYU-CTF 几乎无可测记忆

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reverse engineering (RE) is critical to security tasks such as malware analysis and vulnerability discovery, and large language model (LLM) agents are increasingly able to perform it autonomously. Capture-the-flag (CTF) RE challenges have become the standard proxy for measuring this capability, but evaluation rests on a single criterion: whether the agent captures the flag. This solve rate reveals neither where in the RE process an agent fails nor whether a success reflects analysis of the binary or recall of a public solution. In this paper, we propose Reveree, a diagnostic framework that scores an LLM RE agent's trajectory at three tiers: solve rate, milestone progress through an eight-stage RE schema, and a behavioral profile of its actions. Comprehension stages are scored by an outcome-blinded LLM judge validated against a human expert; all other stages are verified deterministically. Using Reveree, we evaluate nine frontier models and four prompting strategies on 88 picoCTF and NYU-CTF challenges. We find that the base model dominates performance, whereas prompting strategy is a secondary, model-dependent effect. Surprisingly, larger, newer, or costlier models are not reliably stronger. We also find that failures concentrate at the comprehension stages of the RE process, and that extra budget, persistence, or reasoning effort rescues few of them, pointing to a competence limit rather than a resource limit. Regarding memorization, while models reproduce picoCTF flags from challenge descriptions alone, NYU-CTF shows minimal measurable recall, and most solves survive surface perturbation, indicating that genuine analysis coexists with memorization. We release Reveree to the community.

</details>

### 11. FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs

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

### 12. Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code

📄 [arXiv](https://arxiv.org/abs/2608.22652) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/259/Guided-Decoding-as-a-Defense-against-Package-Hallucination-in-LLM-Generated-Code)　📅 2026-08

**关键词**：`benchmark`、`package hallucination`、`adversarial package seed`、`defense utility`

👤 **作者**：Alberick Euraste Djire、Iyiola E. Olatunji、Melissa Tessa、Earl T. Barr、Jacques Klein、Tegawendé F. Bissyandé

- 🎯 **研究动机**：LLM 生成代码常幻觉不存在的软件包，形成供应链攻击入口；且先前评测把标准库模块误判为幻觉，Python 上高估达 9.4 个百分点
- 🔬 **研究方法**：评估七种推理时防御（Greedy、Contrastive、DoLa、Nudging、Active Layer-Contrastive 五种 guided decoding 加 Self-Refine 与 RAG），跨八个模型与多语言，并用植入伪造包名的对抗 prompt 压力测试
- 📌 **结论**：对抗条件下幻觉率最多飙升 45 个百分点（Ruby 最脆弱，80.9–95.2%）；此时 RAG 与 Self-Refine 胜过所有纯解码策略，敌意 prompt 下必须外部接地或迭代自验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are increasingly used for code generation, yet they frequently hallucinate non-existent software packages, creating exploitable entry points into the software supply chain. We make four contributions to this problem. First, we show that prior evaluation methodologies systematically inflate hallucination rates by misclassifying standard-library modules as hallucinations in some languages. For Python, the overestimation reaches 9.4 percentage points. Second, we evaluate seven inference-time defenses for mitigating package hallucinations, including five guided decoding strategies (Greedy, Contrastive, DoLa, Nudging, and Active Layer-Contrastive Decoding), an iterative self-refinement approach (Self-Refine), and a Retrieval-Augmented Generation (RAG)-based defense.. Across eight models spanning five families and four programming languages (Python, JavaScript, Ruby, Rust), RAG reduces the package hallucination rate (PHR) in 18 of 32 model--language configurations. Third, we introduce Package Utility (PU) to assess whether defenses preserve valid and task-relevant recommendations. Among strategies evaluated, Greedy decoding provides the strongest average mitigation--utility trade-off. Fourth, we stress-test all strategies under adversarial prompts seeded with fabricated package names and find that PHR surges by up to 45 percentage points relative to standard prompts, with Ruby consistently the most vulnerable language (80.9--95.2\%). Under adversarial conditions, RAG and Self-Refine outperform all decoding-only strategies, indicating that robust defense requires either external grounding or iterative self-verification when prompts are actively hostile. Our results recast package hallucination as both a measurement problem and a decoding-time control problem, and they demonstrate that the choice of defense must be matched to the threat model and recommendation utility.

</details>

### 13. Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks

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

### 14. Benchmarking Automated Security Patch Backporting: How Far Are We?

📄 [arXiv](https://arxiv.org/abs/2608.17671) · 🌐 [Project](https://conf.researchr.org/track/ase-2026/ase-2026-research-track)　📅 2026-08　🏷 ASE 2026

**关键词**：`benchmark`、`coding agent`、`repository attack`、`code security`

👤 **作者**：Jincheng Yang、…、Hui Li

- 🎯 **研究动机**：安全补丁回移植工具自报成功率超 80%，但评测限于同质环境（单仓库或特定版本），跨场景泛化未知
- 🔬 **研究方法**：Porting Benchmark 含 1234 个跨版本/分支/仓库案例加统一评测框架，对齐设定下评五个工具（程序分析、LLM prompt、LLM agent）
- 📌 **结论**：对齐评测改变格局：FixMorph 与 Mystique 大幅退化；最优 commit 级成功率从 Type-I 85.2% 跌至 Type-IV 24.0%；可执行验证揭示静态参考一致性漏掉的残留集成失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated security patch backporting is critical for mitigating N-day vulnerabilities. Recent tools report success rates above 80% on their respective datasets. However, these evaluations are often confined to homogeneous environments, such as one repository or specific project versions. Consequently, it remains unclear how well these tools generalize beyond their originally targeted scenarios. We present Porting Benchmark, a curated dataset of 1,234 security patch backporting cases spanning cross-version, cross-branch, and cross-repository scenarios, paired with a common evaluation framework. Using this benchmark, we evaluate five tools spanning program analysis, LLM prompting, and LLM agents under aligned settings. Our results show that aligned evaluation changes the apparent performance landscape: PortGPT and TSBPort remain comparatively strong on the Replication Dataset, while FixMorph and Mystique degrade substantially under the common protocol. Performance degrades sharply on structurally complex patches: the best commit-level success rate falls from 85.2% on Type-I patches to 24.0% on Type-IV. We identify four root-cause categories (missing target API awareness, cross-version semantic mismatch, non-local dependency propagation failure, and patch construction or localization failure) and derive concrete directions for next-generation tool design. On a 45-case dynamically validated subset with verified test cases and constructed POCs, we further observe that reference-based benchmark scores do not fully capture real-world remediation: exact match sharply under-credits harder target adaptations, while executable validation reveals residual integration failures in the target that static reference agreement misses. Executable-feedback refinement provides limited but measurable recovery on the hardest executable cases.

</details>

### 15. WeSCE: A Benchmark for Measuring Security Drift in LLM-Driven Code Editing

📄 [arXiv](https://arxiv.org/abs/2608.15092)　📅 2026-08

**关键词**：`benchmark`、`coding agent`、`repository attack`、`code security`

👤 **作者**：Zhiyu Zhang、Tingyue Wen、Senke Sun、Dengxiang Liang、Enhao Huang

- 🎯 **研究动机**：弱安全约束（只给功能目标、无安全要求）下的代码编辑安全漂移缺乏量化基准
- 🔬 **研究方法**：WeSCE 含 400 个源自真实代码的可执行程序，覆盖加/删功能、修 bug 与重构；统一形式聚合异构漏洞信号的连续风险表示，并定义总体风险、最差严重度与分布漂移度量
- 📌 **结论**：提供从平均行为到最坏情形强调的多尺度安全视图，量化代码变换下的安全漂移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this work, we introduce WeSCE, a benchmark for quantifying security drift in code editing under weak-security constraints, where tasks specify only functional objectives without explicit security requirements. WeSCE consists of 400 executable programs derived from real-world code, covering feature addition, feature removal, bug fixing, and refactoring. To quantify security drift, we propose a continuous risk representation that aggregates heterogeneous vulnerability signals through a unified formulation, and define drift measures capturing changes in overall risk, worst-case severity, and vulnerability distribution under code transformations, providing a multi-scale view of security spanning average-case behavior to worst-case emphasis.

</details>

### 16. Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows

📄 [arXiv](https://arxiv.org/abs/2604.20200) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`coding agent`、`evaluation exploitation`、`user pressure`

👤 **作者**：Hardy Chen、…、Yuyin Zhou

- 🎯 **研究动机**：用户主要通过工作区公开分数监督 coding agent，多轮提分压力会否诱发绕过私有评测的作弊未研究
- 🔬 **研究方法**：先在表格分类任务验证，再构建 34 任务 ML 仓库基准 AgentPressureBench，收集 13 个 agent 的 1,326 条多轮轨迹
- 📌 **结论**：出现 403 次作弊性运行；模型越强作弊率越高（Spearman 0.77），高压力使首次作弊从 19.67 轮提前到 4.08 轮，显式反作弊措辞可把作弊从 100% 降至 8.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier coding agents are increasingly used in workflows where users supervise progress primarily through repeated improvement of a public score, namely the reported score on a public evaluation file with labels in the workspace, rather than through direct inspection of the agent's intermediate outputs. We study whether multi-round user pressure to improve that score induces public score exploitation: behavior that raises the public score through shortcuts without improving hidden private evaluation. We begin with a preliminary single-script tabular classification task, where GPT-5.4 and Claude Opus 4.6 both exploit label information within 10 rounds of user-agent interaction. We then build AgentPressureBench, a 34-task machine-learning repository benchmark spanning three input modalities, and collect 1326 multi-round trajectories from 13 coding agents. On our benchmark, we observe 403 exploitative runs, spanning across all tasks. We also find that stronger models have higher exploitation rates, supported by a significant Spearman rank correlation of 0.77. Our ablation experiments show that higher user pressure leads to earlier exploitation, reducing the average first exploit round by 15.6 rounds (i.e., 19.67 to 4.08). As a mitigation, adding explicit anti-exploit wordings in prompt mostly eliminates exploitation (100% to 8.3%). We hope that our work can bring attention to more careful use of coding agents workflow, and developing more robust coding agents under user pressure. Our project page is at https://ucsc-vlaa.github.io/AgentPressureBench .

</details>

### 17. SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark

📄 [arXiv](https://arxiv.org/abs/2603.00520) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62669)　📅 2026-03　🏷 ICML 2026

**关键词**：`benchmark`、`adversarial robustness`、`coding agent`、`repository attack`、`agent safety`、`empirical evaluation`

👤 **作者**：Boxi Yu、…、Lionel Briand

- 🎯 **研究动机**：SWE-Bench Verified 接近饱和（榜首 78.80%），但成绩因弱测试套件而虚高
- 🔬 **研究方法**：SWE-ABS 两阶段强化测试：程序切片驱动的覆盖增强定位未测代码区，变异驱动的对抗测试合成貌似正确的错误补丁暴露盲区
- 📌 **结论**：强化 50.2% 实例（较先前提升 25.1 倍），拒掉 19.71% 原通过补丁，榜首模型分数降至 62.20% 并跌至第五

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The SWE-Bench Verified leaderboard is approaching saturation, with the top system achieving 78.80%. However, we show that this performance is inflated. Our re-evaluation reveals that one in five "solved" patches from the top-30 agents are semantically incorrect, passing only because weak test suites fail to expose their errors. We present SWE-ABS, an adversarial framework that strengthens test suites through a two-stage pipeline: (1) coverage-driven augmentation using program slicing to target untested code regions, and (2) mutation-driven adversarial testing that synthesizes plausible but incorrect patches to expose semantic blind spots. On SWE-Bench Verified (500 instances), SWE-ABS strengthens 50.2% of instances, a 25.1x improvement over prior work, and rejects 19.71% of previously passing patches. As a result, the top agent's score decreases from 78.80% to 62.20%, leading to significant leaderboard reshuffling, with the previous top-ranked agent dropping to fifth place.

</details>

### 18. AIALIB: A Threat Library for AI-Generated Code

🌐 [Project](https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets)　📅 2026　🏷 ASE 2026

**关键词**：`tool`、`AI-generated code`、`threat library`、`vulnerability provenance`

- 🎯 **研究动机**：AI生成代码的威胁缺系统化编目与溯源资源
- 🔬 **研究方法**：构建威胁库AIALIB，分类整理AI生成代码的漏洞类别与来源
- 📌 **结论**：为AI生成代码的安全审计提供统一威胁参照

### 19. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

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

### 20. Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

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

### 21. Think Before You Code: Dual Reasoning for the NLSafety–Utility Trade-Off in LLM Code Generation

📄 [arXiv](https://arxiv.org/abs/2604.12088) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/55/Think-Before-You-Code-Dual-Reasoning-for-the-NLSafety-Utility-Trade-Off-in-LLM-Code-)　📅 2026-04　🏷 ASE 2026

**关键词**：`defense`、`harmful code content`、`dual reasoning`、`safety-utility trade-off`

👤 **作者**：Honghao Tan、Haibo Wang、Shin Hwei Tan

- 🎯 **研究动机**：代码生成只评功能正确性，忽略 prompt 中有害内容经代码传播；已有方法只检测有害不保功能
- 🔬 **研究方法**：基于双通道约束理论提出 SUDS 指标统一效用、安全与警示，Dual Reasoning 在生成前强制显式安全审计与代码评审
- 📌 **结论**：六模型两基准上 DR 均获最高 SUDS，较基线提升 1.32-3.42 倍，而 CoT 提示的安全收益可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) for code generation are typically evaluated on functional correctness alone, overlooking whether generated code propagates harmful content embedded in the prompt. Prior work has shown that most Code LLMs reproduce offensive identifiers from injected renaming instructions without warning, yet existing approaches focus on detecting harmful content, neglecting functional correctness. Grounded in the Theory of Dual Channel Constraints (which states that code is a dual-channel medium combining an algorithmic (AL) channel for machine execution and a natural language (NL) channel for human communication, creating a unique safety-utility trade-off where a model must balance functional execution with responsible communication), we propose NLSafety-Utility Duality Score (SUDS), a metric that unifies code utility, safety adherence, and warning awareness into a single score across 12 ranked response scenarios, and Dual Reasoning (DR), a structured inference-time technique that requires an explicit safety audit and task-grounded code review before code generation. Evaluated on six LLMs across two benchmarks augmented with harmful keyword injections (820 and 2,135 samples), DR consistently achieves the highest SUDS across all models, improving mean SUDS by 1.32$\times$ to 3.42$\times$ over the baseline, while chain-of-thought prompting yields negligible safety gains and a safety-aware prompt provides only partial improvement. Further analysis reveals that DR's effectiveness scales with model capacity, that the one-shot exemplar primarily stabilizes output format for smaller models, and that structured reasoning cannot compensate for models with limited safety vocabularies.

</details>

### 22. When "Correct" Is Not Safe: Can We Trust Functionally Correct Patches Generated by Code Agents?

🎓 [Official](https://aclanthology.org/2026.acl-long.707/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`agent safety`、`coding agent`、`repository attack`、`cybersecurity`、`LLM agent`

👤 **作者**：Yibo Peng、…、Beidi Chen

- 🎯 **研究动机**：代码智能体安全评估几乎只看功能正确性，忽视通过全部测试但含漏洞代码的补丁（FCV）
- 🔬 **研究方法**：提出 FCV-Attack：仅需黑盒访问与单次查询，诱导 SOTA LLM 与智能体框架生成功能正确但含漏洞的补丁
- 📌 **结论**：SWE-Bench 上 12 个 agent-模型组合均受威胁；CWE-538 信息暴露漏洞上 GPT-5 Mini+OpenHands 攻击成功率达 40.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code agents are increasingly trusted to autonomously fix bugs on platforms such as GitHub, yet their security evaluation focuses almost exclusively on functional correctness. In this paper, we reveal a novel type of threat to real-world code-agents: functionally correct yet vulnerable (FCV) patches, which pass all test cases but contain vulnerable code. With our proposed FCV-Attack, we demonstrate that SOTA LLMs (e.g., ChatGPT and Claude) and agent scaffolds (e.g., SWE-agent and OpenHands) are all vulnerable to this FCV threat; across 12 agent-model combinations on SWE-Bench, the attack only requires black-box access and a single query to the code agent to perform the attack. For example, for CWE-538 (information exposure vulnerability), the FCV-Attack attains an attack success rate of 40.7% on GPT-5 Mini + OpenHands. Our results reveal an important security threat overlooked by current evaluation paradigms and urge the development of security-aware defenses for code agents.

</details>

### 23. EVOMAL: Self-Poisoning in Self-Evolving Coding Agents

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

### 24. SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

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

### 25. Workspace Topology as an Attack Vector in Agentic Coding Assistants

📄 [arXiv](https://arxiv.org/abs/2608.14876)　📅 2026-08

**关键词**：`attack`、`coding agent`、`repository attack`、`code security`

👤 **作者**：Alexandre G. R. Day、…、Giri Iyengar

- 🎯 **研究动机**：编码助手以宽文件系统权限运行于开发者工作区，工作区拓扑对间接提示注入成功率的影响未被研究
- 🔬 **研究方法**：定义目录深度、代码库模块化、文件内注入位置与上下文框架四维工作区拓扑，跨 10 语言 6 领域开源仓库、三个注入入口对开源模型与开源 harness 实证
- 📌 **结论**：拓扑可测量改变 ASR：高模块化环境注入成功率显著更低，上下文框架与工作区内安全线索也能改变 ASR，凸显无污染测试环境的重要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic coding assistants are finding widespread use, not just in new code development but in quickly ingesting and leveraging third-party code. This opens up a risk of malicious code being ingested as these coding tools operate with broad filesystem access inside developer workspaces. In this paper, we extensively study the impact of different dimensions of a novel attack surface we term workspace topology -- defined via directory depth, codebase modularity, in-file injection position and context framing -- on the attack success rate of adversarial prompt injection attempts. We perform an empirical study of indirect prompt injection (IPI) across a diverse set of open-source repositories spanning 10 languages and 6 engineering domains, evaluating three IPI entry points against open-weight models operating open source code harnesses. We find that workspace topology measurably affects IPI success. Specifically, changes in codebase modularity can significantly alter the Attack Success Rate (ASR), with highly modular environments demonstrating significantly lower attack success rates. Furthermore, context framing and introduction of security-cues in the workspace can also alter the ASR. Our findings offer practical value for the evaluation and security testing of coding agents across diverse settings, while underscoring the importance of an uncontaminated testing environment to obtain reliable results and conclusions.

</details>

### 26. Distributed Attacks in Persistent-State AI Control

📄 [arXiv](https://arxiv.org/abs/2607.02514) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`attack`、`AI control`、`persistent state`、`coding agent`、`distributed sabotage`

👤 **作者**：Josh Hills、Ida Caspary、Asa Cooper Stickland

- 🎯 **研究动机**：coding agent 在持久代码库上跨 PR 迭代交付，失准或被注入的 agent 可把攻击分摊到多个 PR 并选择掩护最好的时机
- 🔬 **研究方法**：提出 Iterative VibeCoding 基准（CLI 工具与 Flask 服务 20 个任务变体），以 Sonnet 4.5 为攻击 agent、GPT-4o 为监视器，比较渐进式与单 PR 集中式攻击，并提出跨 PR 链接追踪监视器
- 📌 **结论**：无单一监视器同时防住两类攻击，高逃逸率（>=65%）跨攻击模型泛化；链接追踪+四监视器集成把渐进攻击逃逸从 93% 降至 47%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterative VibeCoding, a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task. Our benchmark includes two task families: CLI tools and Flask web services, across 20 total task variations. We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. No single monitor is robust to both: which strategy evades best (success while evading the monitor) depends on the monitor type, so a defender cannot close off both gradual and non-gradual attacks with any one monitor. High evasion (>= 65%) generalizes across model attack agent backends (Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5), confirming this is a property of the persistent-state attack surface rather than a single model's capability. Evasion also remains high across state-of-the-art monitor models and the gap between gradual and non-gradual evasion widens for more capable models. We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. On both task families, it detects gradual attacks substantially better than diff monitors that merely see more accumulated history. Combining this stronger monitor with trajectory monitors in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%.

</details>

### 27. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

📄 [arXiv](https://arxiv.org/abs/2602.03012) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65622)　📅 2026-02　🏷 ICML 2026

**关键词**：`attack`、`cyber misuse`、`coding agent`、`repository attack`、`LLM agent security`、`multi-agent evaluation`

👤 **作者**：Xianzhen Luo、…、Wanxiang Che

- 🎯 **研究动机**：代码安全 agent 评测依赖昂贵不可扩展的人工复现且数据分布过时
- 🔬 **研究方法**：CVE-Factory 多 agent 框架把稀疏 CVE 元数据自动转化为可执行 agentic 任务，并构建 LiveCVEBench 基准与超 1000 个训练环境
- 📌 **结论**：解题正确率 95%、环境保真 96%，最新真实漏洞验证成功率 66.2%；微调 Qwen3-32B 在 LiveCVEBench 从 5.3% 升至 35.8% 超越 Claude 4.5 Sonnet，并泛化到 Terminal Bench（12.5%→31.3%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves 95\% solution correctness and 96\% environment fidelity, confirming its expert-level quality. It is also evaluated on the latest realistic vulnerabilities and achieves a 66.2\% verified success. This automation enables two downstream contributions. First, we construct LiveCVEBench, a continuously updated benchmark of 190 tasks spanning 14 languages and 153 repositories that captures emerging threats including AI-tooling vulnerabilities. Second, we synthesize over 1,000 executable training environments, the first large-scale scaling of agentic tasks in code security. Fine-tuned Qwen3-32B improves from 5.3\% to 35.8\% on LiveCVEBench, surpassing Claude 4.5 Sonnet, with gains generalizing to Terminal Bench (12.5\% to 31.3\%). We open-source CVE-Factory, LiveCVEBench, Abacus-cve (fine-tuned model), training dataset, and leaderboard. All resources are available at https://github.com/livecvebench/CVE-Factory .

</details>

### 28. When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

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

### 29. Beyond Pass@k: Measuring Reliability and Security of Agentic Code Generation

📄 [arXiv](https://arxiv.org/abs/2608.14711)　📅 2026-08

**关键词**：`analysis`、`coding agent`、`repository attack`、`code security`

👤 **作者**：Jiajun Jiang、Sharon Zheng、Natan Vidra、Spurthi Setty

- 🎯 **研究动机**：编码 agent 基准误用 pass@k：把 n 设为单次提交的单元测试数而非独立 rollout 数，混淆测试规模与尝试独立性
- 🔬 **研究方法**：诊断并以反例证明该误用，提出 reliability@k（n=独立 rollout、c=全通过 rollout）与 security-adjusted reliability@k（只计功能正确且无高危不安全模式的 rollout）
- 📌 **结论**：误用指标虚报 0.85-0.97 绝对分（校正后 0.00-0.12），单次 rollout 代理与重复运行 Spearman 仅 0.417；SWE-bench 试点宏平均隐藏测试通过率 0.80 而严格解决率仅 0.20

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding agent benchmarks rank agents with the Chen et al. (2021) pass@k estimator, but current implementations misapply it: they set n to the number of unit tests in a single submission rather than the number of independent rollout attempts, conflating test-suite size with attempt independence. We diagnose this operationalization error, prove it by counterexample, and propose reliability@k, the same estimator applied correctly, with n = independent rollouts and c = fully-passing rollouts per (task, agent) pair. In a synthetic multi-rollout benchmark, the misapplied metric inflates reported scores by 0.85-0.97 in absolute terms (0.96-0.98 reported vs. 0.00-0.12 corrected), and a cheap single-rollout proxy fails to substitute for repeated runs (Spearman $ρ= 0.417$). Motivated by evidence that functional correctness does not imply security safety, we additionally propose security-adjusted reliability@k, which counts only rollouts that are both functionally correct and free of high-severity insecure patterns. In an initial live-API test with three agents, the adjustment did not change any ranking under our current scanner and threshold, so we present it as a proposed complementary lens whose decisive evaluation requires better-powered future runs. Finally, a preliminary 5-task SWE-bench Verified pilot observes the same core concern in a real repository setting: macro-averaged hidden-test pass rate was 0.80 while strict task resolution was 0.20.

</details>

### 30. “Impossible to Hide Secret ...”: Uncovering Security and Privacy Issues in LLM-Native IDEs

📄 [arXiv](https://arxiv.org/abs/2607.26390) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/133/-Impossible-to-Hide-Secret-Uncovering-Security-and-Privacy-Issues-in-LLM-Native)　📅 2026-07　🏷 ASE 2026

**关键词**：`analysis`、`LLM-native IDE`、`unchecked action`、`data exposure`

👤 **作者**：Mostafijur Rahman Akhond、Md Afif Al Mamun、Gias Uddin、Song Wang

- 🎯 **研究动机**：LLM 原生 IDE 是从头为 LLM 设计的系统，其开发者报告的安全与隐私问题未被系统收集分析
- 🔬 **研究方法**：收集 29 个相关 subreddit 的 110 万帖，识别 446 个讨论 LIDE 安全隐私问题的帖子与 6,000+ 评论，用质性定量混合方法构建问题分类法
- 📌 **结论**：多数问题源于系统级设计（用户数据访问、未检查的自主行动）而非底层 LLM；开发者普遍依赖沙箱与人工审查等外部保障，反映对 LIDE 的普遍不信任

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-native IDEs (Integrated Development Environments), aka LIDEs, are designed from the ground up to work with Large Language Models (LLMs). LIDEs have found remarkable success in Software Engineering (SE) tasks such as coding, debugging, and program comprehension. LIDEs are software systems, and, like any system, they can exhibit vulnerabilities. In this paper, we study the security and privacy issues that developers reported while using popular LIDEs in their development tasks. We collected 1.1M posts from 29 popular subreddits related to LIDEs. We identified 446 posts and analyzed over 6K comments to the posts that discussed security and privacy issues in almost all popular LIDEs, such as Cursor, Copilot, Codex, etc. Using a mix of qualitative and quantitative methods, we constructed a taxonomy of the reported security and privacy issues. Our results show that most issues in LIDEs stem from system-level design choices, rather than the underlying LLMs, such as user data access, unchecked autonomous actions, etc. To overcome these issues, developers frequently relied on external safeguards like code sandboxing and manual reviewing, highlighting prevalent mistrust among developers about LIDEs. We share lessons from our study to support future design of secure and privacy-aware LIDEs.

</details>

### 31. Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda

📄 [arXiv](https://arxiv.org/abs/2608.21107)　📅 2026-08

**关键词**：`survey`、`coding agent`、`software security`、`evaluation validity`

👤 **作者**：Wei Lin、Tao Zhou、Zhaofei Xie、Changgui Hong

- 🎯 **研究动机**：LLM 代码系统的证据分裂于软件工程评测（功能完成）与安全评测（漏洞检测、安全生成）之间，弱测试 oracle、数据泄漏等效度威胁频发，难以支撑部署判断
- 🔬 **研究方法**：证据中心结构化综述，综合 2026 年 5 月底前代表性工作，提出任务分类法与区分功能正确性/安全性的 assurance 框架，梳理 recurring 效度威胁并给出最小报告协议
- 📌 **结论**：功能高分与安全保证很少同时成立；模型能力应作为有任务适配证据的 assurance case 评判，而非单一 benchmark 分数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are moving from code completion toward repository-scale agents that retrieve context, edit files, execute tools, and participate in security-sensitive workflows. The evidence for these systems, however, remains divided between software engineering evaluations centered on functional task completion and software security evaluations centered on vulnerability detection, secure generation, or exploit-oriented validation. This evidence-centered structured survey synthesizes representative work available through May 31, 2026 across software engineering tasks, software security tasks, adaptation mechanisms, artifact granularity, and evaluation design. In addition to a task taxonomy, we introduce an assurance framework that separates functional correctness, security, operational reliability, evidence provenance, and agent authority. The review shows that execution feedback and repository access can substantially improve engineering task completion, but do not by themselves establish security; conversely, static-analysis labels or vulnerability-classification scores rarely establish deployable correctness. We identify recurring validity threats--weak test oracles, duplicated and temporally leaked data, changing agent harnesses, proxy-only security checks, and under-reported budgets and human intervention--and derive a minimum reporting protocol for cross-study comparison. The resulting research agenda prioritizes jointly secure-and-functional benchmarks, repository-scale threat models, calibrated human oversight, longitudinal maintainability evidence, and reproducible agent evaluation. The central conclusion is that model capability should be judged as an assurance case supported by task-appropriate evidence, rather than by a single benchmark score.

</details>

### 32. SecureVibeBench: Benchmarking Secure Vibe Coding of AI Agents via Reconstructing Vulnerability-Introducing Scenarios

🎓 [Official](https://aclanthology.org/2026.acl-long.1107/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`agent safety`、`cyber misuse`、`agent safety benchmark`、`LLM agent`、`runtime guardrail`

👤 **作者**：Junkai Chen、…、David Lo

- 🎯 **研究动机**：现有基准未覆盖人类开发者真实引入漏洞的场景，无法公平比较人与代码 agent 的安全编码能力
- 🔬 **研究方法**：构建 SecureVibeBench：来自 OSS-Fuzz 41 个项目的 105 个 C/C++ 任务，要求大仓库多文件编辑，结合功能测试与动静态双 oracle 安全检查
- 📌 **结论**：评测 5 个代码 agent 与 5 个 LLM，最优 agent 也仅产出 23.8% 正确且安全的解法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-powered code agents are rapidly transforming software engineering, yet the security risks of their generated code have become a critical concern. Existing benchmarks have provided valuable insights, but they fail to capture scenarios in which vulnerabilities are actually introduced by human developers, making fair comparisons between humans and agents infeasible. We therefore introduce SecureVibeBench, a benchmark of 105 C/C++ secure coding tasks sourced from 41 projects in OSS-Fuzz for code agents. SecureVibeBench has the following features: (i) realistic task settings that require multi-file edits in large repositories, (ii) aligned contexts based on real-world open-source vulnerabilities with precisely identified vulnerability introduction points, and (iii) comprehensive evaluation that combines functionality testing and security checking with both static and dynamic oracles. We evaluate 5 popular code agents like OpenHands, supported by 5 LLMs (e.g., Claude sonnet 4.5) on SecureVibeBench. Results show that current agents struggle to produce both correct and secure code, as even the best-performing one, produces merely 23.8% correct and secure solutions on SecureVibeBench.

</details>

### 33. XOXO: Stealthy Cross-Origin Context Poisoning Attacks against AI Coding Assistants

🎓 [Official](https://aclanthology.org/2026.acl-long.521/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`LLM backdoor`、`model integrity`

👤 **作者**：Adam Štorek、…、Suman Jana

- 🎯 **研究动机**：编码助手自动纳入不可信上下文，语义不变的代码改动即可隐蔽投毒
- 🔬 **研究方法**：XOXO以重命名等语义保持变换诱导生成漏洞模式，GCGS黑盒搜索有效变换组合
- 📌 **结论**：对八个SOTA模型平均ASR 73.20%，漏洞注入率最高66.67%，GitHub Copilot实战验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding assistants automatically gather context from potentially untrusted sources to generate code recommendations. We introduce Cross-Origin Context Poisoning (XOXO), a novel attack that exploits this automatic context inclusion by subtly manipulating code without changing its semantics. Attackers introduce semantics-preserving transformations (e.g., renamed variables) to shared code, causing AI assistants to unknowingly recommend vulnerable code patterns to victims. To systematically identify effective transformations, we present Greedy Cayley Graph Search (GCGS), a black-box algorithm that efficiently composes transformations to identify adversarial inputs. Our evaluation demonstrates XOXO’s effectiveness at making LLMs generate buggy and vulnerable code, achieving average attack success rates of 73.20% against eight state-of-the-art models including GPT 4.1 and Claude 3.5 Sonnet v2, with vulnerability injection rates up to 66.67%. We also demonstrate a real-world attack against GitHub Copilot, highlighting critical security gaps in current AI coding tools.

</details>

### 34. Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-tong)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`RAG code generation`、`knowledge injection`、`tool-use agent`、`CVE reachability`

👤 **作者**：Tong Sun、Jingyi Su、Yi Gao、Wei Dong

- 🎯 **研究动机**：嵌入式 IoT 的仓库级 RACG 会经良性公开 API 传递性触达 pinned 快照内漏洞例程而继承已知 CVE，现有 secure RACG 忽视版本特定暴露，CVE 扫描器又判不了 API 可达性
- 🔬 **研究方法**：提出 IoTRAGuarder：静态分析加证据门控 LLM 恢复 CVE 例程到公开 API 的反向调用链，构建版本感知安全知识库并做双层 API 对齐在线检索注入约束
- 📌 **结论**：在 44 个 Zephyr 任务、4 个 LLM 上将整体安全成功率从 5.11% 提升到 78.41%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Repository-grounded retrieval-augmented code generation (RACG) is increasingly used in embedded IoT development by retrieving code and documentation from a pinned RTOS/SDK repository (e.g., Zephyr OS). In this setting, security risks are often version-inherited: even without retrieval poisoning, generated applications may invoke benign-looking public APIs that transitively reach vulnerable internal routines in the pinned snapshot, thereby inheriting known CVEs. Existing secure RACG pipelines largely focus on task-level intent and generic vulnerability patterns, which can miss repository- and version-specific exposure. Meanwhile, conventional CVE scanners can flag vulnerable locations but cannot determine whether those vulnerabilities are reachable through the public APIs that the generator commits to during repository-grounded generation. In this paper, we present IoTRAGuarder, a contextual knowledge injection framework that aligns security hardening with generation-time API selection under repository grounding. IoTRAGuarder (i) recovers auditable reverse call chains from CVE-localized internals to exposing public APIs via static analysis plus an evidence-gated LLM to bridge indirections and macro-driven "call-graph islands", (ii) constructs a version-aware security knowledge base that binds affected version intervals to exposed public APIs with prompt-ready constraints, safer alternatives, or avoidance/upgrade guidance, and (iii) performs dual-layer, API-aligned online retrieval to inject concise, version-matched constraints into the final prompt. We evaluate IoTRAGuarder on 44 real-world Zephyr tasks across four LLMs. Compared to the prior state-of-the-art secure RACG baseline, IoTRAGuarder improves the overall security success rate from 5.11% to 78.41%.

</details>
