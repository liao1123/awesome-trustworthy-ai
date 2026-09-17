# Cybersecurity 与 Dual-Use

[返回上级目录](README.md)

## 研究方向

研究 AI 在漏洞发现、利用、恶意代码、诈骗、攻防自动化与安全运营中的能力和风险，既覆盖 offensive uplift，也收录针对 AI 生成代码、Agent 行为或 AI 安全机制的可验证防御。只用普通 ML 提升传统安全分类精度、一般 SOC 效率、密码学能力、区块链任务和传统 phishing 工作不收录；若 phishing 只作为直接 AI 模型或 Agent 攻击机制的实验载体，则归入对应模型或 Agent 安全领域。

## 研究脉络

- **能力评测：** CTF、vulnerability、secure-code 和 autonomous exploitation benchmark 测量模型在真实网络任务中的有效能力。
- **进攻性滥用：** Scam、malware 与 automated exploitation 研究模型如何降低攻击成本；传统 phishing 生成、检测和用户易感性不在范围内。
- **防御自动化：** Secure generation、AI-generated-code detection、risk-bounded patching 和针对 AI 攻击面的防御形成可执行防线。
- **治理与边界：** Dual-use evaluation 需要区分 AI 造成的新攻击面、能力放大与仅把 AI 当作普通工具的传统安全工作。

## Scam 与 Technology-Facilitated Abuse

### 1. Breaking and Defending LLM-Powered Social Media Bot Detection Systems

📄 [arXiv](https://arxiv.org/abs/2608.15893) · 🌐 [Project](https://doi.org/10.53941/pc.2026.100010)　📅 2026-08

**关键词**：`detection`、`cyber misuse`、`offensive capability`、`dual-use risk`

👤 **作者**：Nof Orenstein、Yoni Birman

- 🎯 **研究动机**：LLM 驱动的社媒 bot 检测引入新攻击面，对抗方可直接瞄准其推理与生成机制
- 🔬 **研究方法**：提出两种系统性利用 LLM 分类器语义与语境弱点的对抗攻击，并设计 LSABRE 多 LLM 集成防御
- 📌 **结论**：攻击使检测准确率最多降 48%；LSABRE 在强自适应对抗下保持 86% 检测准确率，方法可推广至钓鱼检测、邮件分类等 LLM 安全系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of social media bots poses a persistent threat, enabling misinformation, opinion manipulation, and the erosion of trust in online platforms. To combat this, machine learning systems have been developed to detect and limit bot activity, but attackers continuously adapt through techniques such as adversarial learning and behavior imitation, fueling an ongoing arms race between bots and detection tools. Recent advances in large language models (LLMs) have significantly improved bot detection by enabling deeper semantic and contextual analysis of accounts and their content. However, this shift also introduces new attack surfaces, allowing adversaries to craft exploits that directly target the reasoning and generation mechanisms of LLM-based classifiers. Industry tools such as Anthropic's Claude Code Security similarly leverage LLMs for security-critical decisions, further motivating a careful study of their attack surfaces. In this work, we investigate both the offensive and defensive aspects of LLM-powered, threat-specific cybersecurity applications. While centered on the challenge of social media bot detection, our methodology and insights generalize to a broad class of LLM-powered cybersecurity systems, including phishing detection, email classification, and fraud analysis. We introduce two novel adversarial attack strategies that systematically exploit the semantic and contextual weaknesses of LLM-based classifiers, degrading their detection accuracy by up to 48%. To counter these threats, we propose a robust multi-LLM defense architecture designed to preserve detection reliability under adaptive adversarial conditions. Our solution, LSABRE (LLM-powered Social Adversarial Bot Recognition Ensemble), is a multi-LLM framework that substantially improves robustness across a range of attacks, maintaining 86% detection accuracy even under strong, adaptive adversarial pressure.

</details>

### 2. Assessing LLM Response Quality in the Context of Technology-Facilitated Abuse

📄 [arXiv](https://arxiv.org/abs/2602.17672) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/prakash)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`benchmark`、`technology-facilitated abuse`、`LLM response safety`、`cyber misuse`、`survivor support`

👤 **作者**：Vijay Prakash、Majed Almansoori、Donghan Hu、Rahul Chatterjee、Danny Yuxing Huang

- 🎯 **研究动机**：技术媒介虐待幸存者可能先咨询 LLM 聊天机器人，其回复质量缺乏专家与幸存者视角的评估
- 🔬 **研究方法**：专家主导人工评估两个通用与两个 IPV 领域模型对真实 TFA 问题的零样本单轮回复，并开展幸存者参与的用户研究
- 📌 **结论**：揭示当前 LLM 在 TFA 场景的能力与局限，并给出面向幸存者支持的具体改进建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Technology-facilitated abuse (TFA) is a pervasive form of intimate partner violence (IPV) that leverages digital tools to control, surveil, or harm survivors. While tech clinics are one of the reliable sources of support for TFA survivors, they face limitations due to staffing constraints and logistical barriers. As a result, many survivors turn to online resources for assistance. With the growing accessibility and popularity of large language models (LLMs), and increasing interest from IPV organizations, survivors may begin to consult LLM-based chatbots before seeking help from tech clinics. In this work, we present the first expert-led manual evaluation of four LLMs - two widely used general-purpose non-reasoning models and two domain-specific models designed for IPV contexts - focused on their effectiveness in responding to TFA-related questions. Using real-world questions collected from literature and online forums, we assess the quality of zero-shot single-turn LLM responses generated with a survivor safety-centered prompt on criteria tailored to the TFA domain. Additionally, we conducted a user study to evaluate the perceived actionability of these responses from the perspective of individuals who have experienced TFA. Our findings, grounded in both expert assessment and user feedback, provide insights into the current capabilities and limitations of LLMs in the TFA context and may inform the design, development, and fine-tuning of future models for this domain. We conclude with concrete recommendations to improve LLM performance for survivor support.

</details>

### 3. Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs

📄 [arXiv](https://arxiv.org/abs/2509.02372) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62158)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`benchmark`、`cyber misuse`、`offensive capability`、`dual-use risk`、`safety alignment`

👤 **作者**：Zhiyang Chen、Tara Saba、Xun Deng、Xujie Si、Fan Long

- 🎯 **研究动机**：网络级训练数据使诈骗内容被吸收进 LLM 权重并在推理时复现（已有开发者因 ChatGPT 生成含钓鱼 URL 的脚本损失 2,500 美元）
- 🔬 **研究方法**：提出 Scam2Prompt：爬取已知诈骗网站、推断功能意图并合成无害的开发者式编码提示，构建 1,377 条经人工验证为良性任务的 Innoc2Scam-bench
- 📌 **结论**：7 个 2025 年生产 LLM 的恶意代码生成率为 12.9%-47.3%，无一免疫；SOTA 护栏与 RAG agent 保护有限，亟需 URL 显式校验

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The insatiable demand for web-scale training data has exposed LLMs to a subtle but consequential threat: the absorption of malicious scam content into model weights and its subsequent reproduction during inference. In November 2024, this risk materialized when a developer reportedly lost 2,500 USD after ChatGPT generated an otherwise routine cryptocurrency trading script containing a live phishing URL. To systematically investigate this problem, we introduce Scam2Prompt, an automated auditing framework that crawls known scam websites, infers their functional intent, and synthesizes innocuous developer-style prompts — the kind of legitimate coding requests a programmer might naturally submit — to evaluate whether LLMs reproduce the underlying scam endpoints. Importantly, our approach requires neither jailbreaking nor adversarial prompting; all 1,377 prompts in our benchmark, Innoc2Scam-bench, which is automatically constructed by Scam2Prompt, were human-validated as benign coding tasks. Evaluation of seven production LLMs released in 2025 on Innoc2Scam-bench shows that the vulnerability proves both persistent and severe: malicious code generation rates range from 12.9% to 47.3% across the evaluated models, and no tested model proves immune. State-of-the-art guardrails and RAG-based agents offer only limited protection, underscoring an urgent need for explicit URL validation in LLM-assisted software development pipelines.

</details>

### 4. Love, Lies, and Language Models: Investigating AI's Role in Romance-Baiting Scams

📄 [arXiv](https://arxiv.org/abs/2512.16280) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gressel)　📅 2025-12　🏷 USENIX Security 2026

**关键词**：`analysis`、`romance-baiting`、`scam automation`、`dual-use risk`、`LLM misuse`、`safety filter`

👤 **作者**：Gilad Gressel、…、Yisroel Mirsky

- 🎯 **研究动机**：杀猪盘等 romance-baiting 诈骗本质是文本密集型，LLM 全自动化的现实风险与防御缺口不明
- 🔬 **研究方法**：访谈 145 名业内人员与 5 名受害者，开展 LLM 诈骗 agent 与人类操盘手的盲测长期对话研究，并评测商业安全过滤器
- 📌 **结论**：87% 诈骗劳动属可自动化的对话任务；LLM agent 赢得更高信任（p=0.007）、请求依从率 46%（人类 18%）；主流安全过滤器对 romance-baiting 对话检出率为 0.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Romance-baiting scams have become a major source of financial and emotional harm worldwide. These operations are run by organized crime syndicates that traffic thousands of people into forced labor, requiring them to build emotional intimacy with victims over weeks of text conversations before pressuring them into fraudulent cryptocurrency investments. Because the scams are inherently text-based, they raise urgent questions about the role of Large Language Models (LLMs) in both current and future automation. We investigate this intersection by interviewing 145 insiders and 5 scam victims, performing a blinded long-term conversation study comparing LLM scam agents to human operators, and executing an evaluation of commercial safety filters. Our findings show that LLMs are already widely deployed within scam organizations, with 87% of scam labor consisting of systematized conversational tasks readily susceptible to automation. In a week-long study, an LLM agent not only elicited greater trust from study participants (p=0.007) but also achieved higher compliance with requests than human operators (46% vs. 18% for humans). Meanwhile, popular safety filters detected 0.0% of romance baiting dialogues. Together, these results suggest that romance-baiting scams may be amenable to full-scale LLM automation, while existing defenses remain inadequate to prevent their expansion.

</details>

### 5. Interpreting and Steering for Safe and Correct Code Generation

📄 [arXiv](https://arxiv.org/abs/2608.30025)　📅 2026-09

**关键词**：`defense`、`analysis`、`secure code generation`、`DuoSteer`、`functional correctness`、`code-safety representation`

👤 **作者**：Hao Yan、Ziyu Yao

- 🎯 **研究动机**：LLM 常生成含漏洞代码，但安全-漏洞生成的内部表征与驱动机制研究不足
- 🔬 **研究方法**：构建 9,342 对 Python 安全-漏洞对比代码集 CodeSec-Pairs，定位 safety 相关层与 attention head，提出同时施加安全与正确性双 steering 的 DuoSteer
- 📌 **结论**：五类漏洞上平均 vulnerability rate 降 26.9%、functional correctness 升 7.5%，优于 prompting 与 SFT 基线并在 Qwen-2.5-Coder 上复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) frequently generate source code containing vulnerabilities, yet little work studies the internal mechanisms that distinguish safe from vulnerable generation in them. In this work, we systematically perform a mechanistic interpretation of LLMs, aiming at both understanding how code safety-vs-vulnerability is represented or driven by components in an LM and turning the insights into actionable steering strategies to encourage safer code generation. To this end, we introduce CodeSec-Pairs, a dataset of 9,342 Python safe-and-vulnerable contrastive code pairs, sampled from Llama-3.1-8B-Instruct. Utilizing the dataset, we explore approaches to localize layers and attention heads that relate to code safety, and further experiment with different steering strategies for inference-time vulnerability reduction. In particular, we propose DuoSteer, a double-steering approach that simultaneously applies safety and code-correctness steering to attention heads. In experiments over five vulnerability types, DuoSteer leads to an average of -26.9% vulnerability rate reduction and +7.5% functional correctness improvement, which outperforms not only other steering variants but also prompting and supervised fine-tuning baselines. The advantage also replicates on Qwen-2.5-Coder-7B-Instruct with another 2,500 contrastive pairs sampled from that model.

</details>

### 6. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

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

### 7. Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline

📄 [arXiv](https://arxiv.org/abs/2608.16187)　📅 2026-08

**关键词**：`detection`、`AI-generated content`、`cyber misuse`、`offensive capability`

👤 **作者**：Mikhail Surikov

- 🎯 **研究动机**：AI 辅助开发大量产出漏洞代码，缺开发速度下检测、富化、修复与验证一体的自动化机制
- 🔬 **研究方法**：流水线：LLMSecEval 生成代码，CodeQL+Bandit 与独立 Code Validator LLM 并行扫描，发现富化 MITRE ATT&CK/CWE/最佳实践后生成修复并复扫验证；四个 Claude 模型 80 次运行
- 📌 **结论**：P1 降静态发现 9-54%、P2 降 29-69% 且每模型均更优；修复在 15-22% 案例引入新漏洞；最强代码模型 Opus 4.8 非最佳管线表现，Sonnet 4.6 残留最低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-assisted development tools generate vulnerable code at significant rates, yet few automated mechanisms exist to detect, enrich, fix, and verify security issues at development velocity, particularly ones that ground remediation in real-world threat context. This paper presents an automated security evaluation pipeline that generates Python code from LLMSecEval prompts, scans for vulnerabilities using CodeQL and Bandit in parallel with an independent Code Validator LLM, enriches the Code Validator findings with MITRE ATT&CK techniques, CWE Observed Examples, and Python best practice guidelines, generates fixes via the Code Generation LLM, and re-scans with CodeQL and Bandit to verify outcomes. Two pipeline configurations were evaluated: Pipeline 1 (P1), using enriched Code Validator findings only, and Pipeline 2 (P2), where it additionally receives the initial CodeQL and Bandit findings. Both configurations were run across four Claude models: Opus 4.8, Sonnet 4.6, Sonnet 5, and Haiku 4.5, producing 80 runs against 26 LLMSecEval prompts covering 9 CWE categories. P1 reduced static analyzer findings across all four models, ranging from -9% (Opus 4.8) to -54% (Sonnet 5). P2 deepened these reductions further, ranging from -29% (Opus 4.8) to -69% (Haiku 4.5), with P2 outperforming P1 for every model. Verdict consistency averaged approximately 81% modal agreement across all configurations, with P2 marginally more stable than P1. Remediation introduced new vulnerabilities in 15-22% of cases: roughly 70% involved a single new finding, and P2 reduced churn for three of four models, with Sonnet 5 as the sole exception. Notably, the best Code Generation LLM (Opus 4.8) was not the best pipeline performer, as Sonnet 4.6 produced the lowest residual findings and highest pass rate after P2 remediation, suggesting that pipeline effectiveness and first-draft security are distinct properties.

</details>

### 8. Shape-Shifting Malicious Code in Software Backdoors via Language Models

🌐 [Project](https://doi.org/10.1145/3779208.3807485)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`LLM misuse`、`software backdoor`、`supply-chain evasion`、`LLM steganography`、`malicious payload`

- 🎯 **研究动机**：开源供应链防御聚焦检测软件内的后门功能，忽视看似良性的文档与配置脚本也可成为恶意代码载体
- 🔬 **研究方法**：用 LLM 把恶意载荷编码进良性 cover data，产物对人审自然可信，且无需语言模型即可还原为恶意形态
- 📌 **结论**：评估证明该 shape-shifting 代码能有效躲过代码审计，据此给出软件开发建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Supply-chain attacks in open-source software are a notorious threat to security. Current defenses focus primarily on detecting backdoor functionality within the software. However, we show that seemingly benign documentation and configuration scripts can also serve as carriers of malicious code. To this end, we introduce an attack that uses large language models to encode a malicious payload into benign cover data. The resulting material appears natural and plausible to human reviewers, yet it can be easily reconstructed into its malicious form without access to a language model. Our evaluation demonstrates the efficacy of this approach in hiding code from audits. We argue that this form of shape-shifting code poses a notable risk and derive corresponding recommendations for software development. CCS Concepts • Security and privacy → Software and application security; • Computing methodologies → Natural language processing. Keywords Software Backdoors, Supply-Chain Attacks, Generative Models ACM Reference Format: Mohammad Ebrahimi Fard, Felix Weissberg, Erik Imgrund, Thorsten Eisenhofer, and Konrad Rieck. 2026. Shape-Shifting Malicious Code in Software Backdoors via Language Models. In ACM Asia Conference on Computer and Communications Security (ASIA CCS ’26), June 01–05, 2026, Bangalore, India. ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3779208.3807 485

</details>

### 9. One RNG to Rule Them All - How Randomness Becomes an Attack Vector in Machine Learning

📄 [arXiv](https://arxiv.org/abs/2602.09182) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-02　🏷 SaTML 2026

**关键词**：`defense`、`ML supply chain`、`PRNG vulnerability`、`runtime enforcement`

👤 **作者**：Kotekar Annapoorna Prabhu、Andrew Gan、Zahra Ghodsi

- 🎯 **研究动机**：ML 框架 PRNG 实现差异大且缺统计校验，随机性成为被忽视的隐蔽攻击向量
- 🔬 **研究方法**：RNGGuard 静态分析目标库源码定位随机函数及调用点，运行时将不安全调用替换为满足安全规范的实现
- 📌 **结论**：以低接入成本填补 ML 系统随机源安全防护的空白

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning relies on randomness as a fundamental component in various steps such as data sampling, data augmentation, weight initialization, and optimization. Most machine learning frameworks use pseudorandom number generators as the source of randomness. However, variations in design choices and implementations across different frameworks, software dependencies, and hardware backends along with the lack of statistical validation can lead to previously unexplored attack vectors on machine learning systems. Such attacks on randomness sources can be extremely covert, and have a history of exploitation in real-world systems. In this work, we examine the role of randomness in the machine learning development pipeline from an adversarial point of view, and analyze the implementations of PRNGs in major machine learning frameworks. We present RNGGuard to help machine learning engineers secure their systems with low effort. RNGGuard statically analyzes a target library's source code and identifies instances of random functions and modules that use them. At runtime, RNGGuard enforces secure execution of random functions by replacing insecure function calls with RNGGuard's implementations that meet security specifications. Our evaluations show that RNGGuard presents a practical approach to close existing gaps in securing randomness sources in machine learning systems.

</details>

### 10. SecCodePRM: A Process Reward Model for Code Security

📄 [arXiv](https://arxiv.org/abs/2602.10418) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64014)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`cyber misuse`、`offensive capability`、`dual-use risk`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Weichen Yu、…、Matt Fredrikson

- 🎯 **研究动机**：现有漏洞检测依赖静态分析器或程序级粗监督的 LLM/GNN 检测器，需完整上下文、反馈稀疏，难以支撑流式生成中的前缀级实时安全评估
- 🔬 **研究方法**：提出 SecCodePRM：由静态分析器与专家标注推导步骤级安全标签，沿代码轨迹打上下文感知的步骤级安全分，支持全码/部分码漏洞检测与安全代码生成
- 📌 **结论**：三种设定均超越先前方法且保持代码功能正确性，未引入安全-效用折损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models are rapidly becoming core components of modern software development workflows, yet ensuring code security remains challenging. Existing vulnerability detection pipelines either rely on static analyzers or use LLM/GNN-based detectors trained with coarse program-level supervision. Both families often require complete context, provide sparse end-of-completion feedback, and can degrade as code length grows, making them ill-suited for real-time, prefix-level assessment during interactive coding and streaming generation. We propose \textbf{SecCodePRM}, a security-oriented process reward model that assigns a \textbf{context-aware}, \textbf{step-level} security score along a code trajectory. To train the model, we derive step-level supervision labels from static analyzers and expert annotations, allowing the model to attend more precisely to fine-grained regions associated with inter-procedural vulnerabilities. SecCodePRM has three applications: full-code vulnerability detection (VD), partial-code VD, and secure code generation (CG). For VD, SecCodePRM uses risk-sensitive aggregation that emphasizes high-risk steps; for CG, SecCodePRM supports inference-time scaling by ranking candidate continuations and favoring higher cumulative reward. This design yields dense, real-time feedback that scales to long-horizon generation. Empirically, SecCodePRM outperforms prior approaches in all three settings, while preserving code functional correctness, suggesting improved security without a safety–utility tradeoff.

</details>

### 11. PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`autonomous remediation`、`risk-bounded agent`、`cyber misuse`、`policy constraint`

👤 **作者**：Rui Li、Shuang Cao

- 🎯 **研究动机**：脚本化补丁修复安全但僵化，LLM 智能体灵活却常违反维护窗口、爆炸半径限制等变更管理策略
- 🔬 **研究方法**：PatchWeaver 组合持续刷新的 Kubernetes 资产/依赖/审批图谱、把组织变更规则编码为可执行谓词的 ChangeSpec、预测进展与违规风险的 rollout 决策层；短程仿真检测约束陷阱并重规划
- 📌 **结论**：步级违规比工具链基线降 52.5%、比 LLM 智能体基线降 79.1%；攻击压力测试漏报率 0.33%（工具链 28.5%），p99 准入延迟 31ms

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Security teams increasingly rely on automation to keep pace with vulnerability disclosure and patch deployment, yet real remediation workflows are constrained by change-management policies: maintenance windows, staged rollout rules, blast-radius limits, approval gates, and least-privilege requirements. Today, "autonomous" remediation is brittle. Scripted playbooks are safe but rigid, while LLM-driven agents are flexible but frequently violate operational policies (e.g., patching outside windows, taking too many replicas offline, or skipping mandatory validation), creating outages and compliance risk. We present PatchWeaver, a remediation system that provides policy-bounded autonomy. PatchWeaver combines (i) an explicit, continuously refreshed graph of Kubernetes assets, dependencies, identities, vulnerabilities, approvals, and evidence; (ii) a typed policy interface (ChangeSpec) that encodes organization-specific change rules as executable predicates; and (iii) a rollout-based decision layer that scores candidate remediation plans by predicting both progress and policy-violation risk before any action is executed. The core insight is that myopic enforcement cannot avoid constraint traps--states where locally admissible actions lead to dead ends that force later violations. PatchWeaver detects traps via short-horizon simulation and replans when reality diverges from prediction. We evaluate PatchWeaver on four Kubernetes remediation workloads under explicit governance constraints. Compared to a strong toolchain baseline (Gatekeeper + Argo Rollouts + Cosign), PatchWeaver reduces step-level policy violations by 52.5% (4.73% vs. 9.95%, p<0.01) and episode-level violations by 52.2% (5.82% vs. 12.18%). Compared to an LLM-agent baseline, PatchWeaver reduces step violations by 79.1% and worst-case (p99) episode violations by 3.1x (16.8% vs. 51.3%). In security stress tests across 10 attack categories, PatchWeaver achieves 0.33% aggregate miss rate with mean dwell time 0.84 s, separating 88.7% immediate blocks from 11.0% escalations, versus 28.5% miss rate and 96.4 s for the toolchain. Control-plane overhead remains practical: p99 admission latency is 31 ms at 32 policy predicates, and total resource usage is under 1 CPU core and 1 GB memory.

</details>

### 12. Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs

📄 [arXiv](https://arxiv.org/abs/2606.03489) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61209)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`cyber misuse`、`offensive capability`、`dual-use risk`、`dangerous capability`、`reinforcement learning`

👤 **作者**：Wenqi Chen、Ziyan Zhang、Bin Wang、Lin Liu、Hengheng Zhang、Zhengsu Chen

- 🎯 **研究动机**：SFT/RL 的序列级粗粒度优化无法处理单 token 即可致漏洞的局部性安全缺陷
- 🔬 **研究方法**：TSP 把安全代码生成重构为细粒度序列决策，构建决策树探索安全金路径与漏洞变体，自我博弈严格判别自身局部错误
- 📌 **结论**：CodeLlama-7B 安全 pass rate（SPR@1）提至 75.8%（SFT 57.0%）；未见 CWE 漏洞降 24.5%，C/C++ 安全原则可迁移至 Python、Go、JavaScript

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) excel in code generation, they remain prone to replicating subtle yet critical vulnerabilities endemic to their training data. Current alignment techniques, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), typically apply coarse-grained optimization at the sequence level. This approach often fails to address the localized nature of security flaws, where a single incorrect token choice can compromise an entire program. To bridge this gap, we introduce Tree-like Self-Play (TSP), a framework that reframes secure code generation as a fine-grained sequential decision process. Unlike standard methods that blindly maximize likelihood, TSP constructs a decision tree where the model explores branching trajectories—generating both secure "golden paths" and vulnerable variants. By treating code generation as a self-play game, the model learns to strictly discriminate against its own localized errors. This provides a dense, on-policy learning signal that forces self-correction precisely at the critical decision nodes where vulnerabilities typically emerge. Our experiments demonstrate that TSP fundamentally enhances model reliability. In Python security benchmarks, TSP boosts CodeLlama-7B’s pass rate (SPR@1) to 75.8\%, significantly outperforming SFT (57.0\%) and unstructured self-play baselines. Crucially, TSP induces robust out-of-distribution generalization: the model not only reduces vulnerabilities in unseen categories (CWEs) by 24.5\% but also successfully transfers security principles learned from C/C++ to diverse languages, including Python, Go, and JavaScript. This suggests that TSP does not merely memorize patches, but internalizes abstract, language-agnostic security logic.

</details>

### 13. Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks

📄 [arXiv](https://arxiv.org/abs/2512.03262) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61427)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`cyber misuse`、`offensive capability`、`dual-use risk`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Songwen Zhao、Danqing Wang、Kexun Zhang、Jiaxuan Luo、Zhuo Li、Lei Li

- 🎯 **研究动机**：vibe coding（少监督让智能体写代码）产出代码的生产安全性未知
- 🔬 **研究方法**：SUSVIBES 含 186 个真实开源项目 feature-request 任务（人类曾提交漏洞实现），评测 12 种主流编码智能体设定
- 📌 **结论**：所有智能体安全表现差：SWE-Agent+Claude 4 Sonnet 57% 功能正确但仅 11.8% 安全；加漏洞提示也无法缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vibe coding is a new software development paradigm in which human engineers prompt a large language model (LLM) agent to complete complex coding tasks with little supervision. Although vibe coding is increasingly adopted, is the generated code really safe to deploy in production? To investigate this question, we propose SUSVIBES, a benchmark consisting of 186 feature-request software engineering tasks from real-world open-source projects, for which human programmers committed vulnerable implementations. We evaluate 12 widely used coding agentic settings with frontier models on the benchmark. Disturbingly, all agents perform poorly in terms of software security. Although 57% of the solutions from SWE-Agent with Claude 4 Sonnet are functionally correct, only 11.8% are secure. Further experiments demonstrate that preliminary security strategies, such as augmenting the feature request with vulnerability hints, cannot mitigate these security issues. Our findings raise serious concerns about the widespread adoption of vibe coding, particularly in security-sensitive applications. The code and dataset are available at https://github.com/LeiLiLab/susvibes. The leaderboard is at https://leililab.github.io/ susvibes-leaderboard.

</details>

### 14. From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching

📄 [arXiv](https://arxiv.org/abs/2601.23088) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65663)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`cyber misuse`、`offensive capability`、`dual-use risk`、`privacy attack`、`mechanistic analysis`

👤 **作者**：Zhixiang Zhang、Zesen Liu、Yuchong Xie、Quanfeng Huang、Dongdong She

- 🎯 **研究动机**：语义缓存用嵌入做键以最大化命中率，所需局部性与抗碰撞所需的雪崩效应根本冲突，完整性风险未被系统研究
- 🔬 **研究方法**：把语义缓存键概念化为模糊哈希，提出黑盒碰撞攻击自动框架 CacheAttack
- 📌 **结论**：LLM 响应劫持命中率 86%，可诱导 LLM agent 恶意行为且跨嵌入模型强迁移；金融 agent 案例展示真实影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Semantic caching has emerged as a pivotal technique for scaling LLM applications, widely adopted by providers including AWS and Microsoft. By utilizing embedding vectors as cache keys, this mechanism effectively minimizes latency and redundant computation for semantically similar queries. In this work, we conceptualize semantic cache keys as a form of fuzzy hashes. We demonstrate that the locality required to maximize cache hit rates fundamentally conflicts with the cryptographic avalanche effect necessary for collision resistance. Our conceptual analysis formalizes this inherent trade-off between performance (locality) and security (collision resilience), revealing that semantic caching is inherently vulnerable to key collision attacks. While prior research has focused on side-channel and privacy risks, we present the first systematic study of integrity risks arising from cache collisions. We introduce CacheAttack, an automated framework for launching black-box collision attacks. We evaluate CacheAttack in security-critical tasks and agentic workflows. It achieves a hit rate of 86\% in LLM response hijacking and can induce malicious behaviors in LLM agent, while preserving strong transferability across different embedding models. A case study on a financial agent further illustrates the real-world impact. Finally, we discuss mitigation strategies, highlighting a persistent trade-off between cache efficiency and robustness.

</details>

### 15. DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation

🎓 [Official](https://aclanthology.org/2026.acl-long.907/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`cyber misuse`、`offensive capability`、`dual-use risk`、`cybersecurity`、`high-risk deployment`

👤 **作者**：Li Huang、…、Meng Yan

- 🎯 **研究动机**：代码 LLM 安全硬化只用最后 transformer 层监督，受 final-layer 瓶颈限制——漏洞判别线索分布在多层且向输出层衰减
- 🔬 **研究方法**：DeepGuard 经注意力模块聚合多个上层表征，驱动平衡安全与功能正确的多目标训练内的专用安全分析器，并支持轻量推理时引导
- 📌 **结论**：五个代码 LLM 上安全且正确的生成率平均比 SVEN 等强基线提升 11.9%，且对留出漏洞类型泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) for code generation can replicate insecure patterns from their training data. To mitigate this, a common strategy for security hardening is to fine-tune models using supervision derived from the final transformer layer. However, this design may suffer from a final-layer bottleneck: vulnerability-discriminative cues can be distributed across layers and become less detectable near the output representations optimized for next-token prediction. To diagnose this issue, we perform layer-wise linear probing. We observe that vulnerability-related signals are most detectable in a band of intermediate-to-upper layers yet attenuate toward the final layers. Motivated by this observation, we introduce DeepGuard, a framework that leverages distributed security-relevant cues by aggregating representations from multiple upper layers via an attention-based module. The aggregated signal powers a dedicated security analyzer within a multi-objective training objective that balances security enhancement and functional correctness, and further supports a lightweight inference-time steering strategy. Extensive experiments across five code LLMs demonstrate that DeepGuard improves the secure-and-correct generation rate by an average of 11.9% over strong baselines such as SVEN. It also preserves functional correctness while exhibiting generalization to held-out vulnerability types.

</details>

### 16. Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation

📄 [arXiv](https://arxiv.org/abs/2602.01187) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64101)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`cyber misuse`、`offensive capability`、`dual-use risk`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Chengran Yang、…、David Lo

- 🎯 **研究动机**：LLM 代码生成被形式化为不可变前缀上的单调 token 追加，与编程中边写边改的认知过程相悖；事后 agent 或静态工具延迟高
- 🔬 **研究方法**：Stream of Revision 引入动作 token，让模型在单次前向传播内回溯并编辑自己的历史，把修订循环内化到解码过程
- 📌 **结论**：安全代码生成上显著减少漏洞且推理开销极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) based code generation is predominantly formulated as a strictly monotonic process, appending tokens linearly to an immutable prefix. This formulation contrasts with the cognitive process of programming, which is inherently interleaved with forward generation and on-the-fly revision. While prior works attempt to introduce revision via post-hoc agents or external static tools, they either suffer from high latency or fail to leverage the model's intrinsic semantic reasoning. In this paper, we propose Stream of Revision, a paradigm shift that elevates code generation from a monotonic stream to a dynamic, self-correcting trajectory by leveraging the model's intrinsic capabilities. We introduce specific action tokens that enable the model to seamlessly backtrack and edit its own history within a single forward pass. By internalizing the revision loop, our framework Stream of Revision allows the model to activate its latent capabilities just-in-time without external dependencies. Empirical results on secure code generation show that Stream of Revision significantly reduces vulnerabilities with minimal inference overhead.

</details>

### 17. AutoBaxBuilder: Bootstrapping Code Security Benchmarking

📄 [arXiv](https://arxiv.org/abs/2512.21132) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64856)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`cyber misuse`、`offensive capability`、`dual-use risk`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Tobias von Arx、Niels Mündler、Mark Vero、Maximilian Baader、Martin Vechev

- 🎯 **研究动机**：代码安全基准由专家手工构建成本高昂，且不可避免污染训练数据、需持续扩展任务与难度
- 🔬 **研究方法**：AutoBaxBuilder 自动化管线利用 LLM 代码理解能力与可靠性检查，从零生成功能测试与端到端安全探测 exploit，据此构建并发布 AutoBaxBench
- 📌 **结论**：新任务 2 小时内生成、成本低于 4 美元，人工投入减少 12 倍，预测与专家基线高度对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) see wide adoption in software engineering, the reliable assessment of the correctness and security of LLM-generated code is crucial. Notably, prior work showed that LLMs are prone to generating code with security vulnerabilities, highlighting that security is often overlooked. These insights were enabled by specialized benchmarks crafted by security experts through significant manual effort. However, benchmarks (i) inevitably end up contaminating training data, (ii) must extend to new tasks to provide a more complete picture, and (iii) must increase in difficulty to challenge more capable LLMs. In this work, we address these challenges and present AutoBaxBuilder, an automated pipeline that generates code security benchmarking tasks from scratch. It leverages the code-understanding capabilities of LLMs combined with robust reliability checks to construct functional tests and end-to-end security-probing exploits. The quality of the pipeline is quantitatively confirmed by aligning its predictions with an expert-written baseline and qualitatively validated through manual soundness verification. We use AutoBaxBuilder to construct a new benchmark and release it to the public as AutoBaxBench, together with a thorough evaluation on contemporary LLMs. AutoBaxBuilder generates new tasks in under 2 hours, for less than USD 4. Including a manual verification, this reduces the required human effort for benchmark construction by a factor of 12.

</details>

### 18. FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs

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

### 19. CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild

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

### 20. Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus

📄 [arXiv](https://arxiv.org/abs/2608.19266)　📅 2026-08

**关键词**：`analysis`、`adversarial robustness`、`cyber misuse`、`offensive capability`

👤 **作者**：Kyriakos "Rock" Lambros、Steve Wilson

- 🎯 **研究动机**：OWASP LLM Top 10 是社区专家投票排名，对照真实事件记录是否成立未被检验
- 🔬 **研究方法**：汇编 7714 快照、6639 标注的 LLM 安全事件语料（CVE、GHSA、OSV、AIAAIC），用贝叶斯测量误差模型校正分类精度与召回后导出事件排序
- 📌 **结论**：专家与数据排序一致性弱（Cohen κ≈0.20，90% 区间跨零）；但四分类器 bake-off 无一超过发生率下限的平衡准确率 0.863，下限排序对保留真值 Spearman 0.918——专家排名仍稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The OWASP Top 10 for LLM Applications ranks the risks that a community of security practitioners judges most important. We ask a narrower question: checked against the record of real incidents, does that expert ranking agree with the data? We assembled a large-scale corpus of LLM-security incidents (7,714 snapshotted and 6,639 labeled against the 20-entry taxonomy) drawn from CVE, GHSA, OSV, and AIAAIC, and derived an incident-based ranking with a Bayesian measurement-error model that corrects each category's count for classifier precision and recall. The 2026 candidate list blends the two signals at fixed weights, 0.75 on the expert vote and 0.25 on the data, so the corpus corrects the consensus without overturning it. The agreement between the two rankings is weak: Cohen's $κ\approx 0.20$, with a 90% interval that crosses zero. The expert ranking is nonetheless robust. A pre-registered bake-off of four frontier classifiers returns no winner. None beats the incidence floor's balanced accuracy of 0.863. A ground-truth check leaves the floor's ordering (Spearman $ρ= 0.918$ against held-out truth) in place. This is an exploratory analysis by two working-group members, not the official OWASP release, and it does not supersede the official list or process.

</details>

### 21. OmniVul: A Holistic, Multi-Turn Conversational Benchmark for LLM-Based Vulnerability Assessment

🌐 [Project](https://doi.org/10.1145/3770855.3817475)　📅 2026-08　🏷 KDD 2026

**关键词**：`benchmark`、`cyber capability`、`vulnerability assessment`、`multi-turn LLM`

- 🎯 **研究动机**：现有漏洞基准数据源窄、缺深层上下文、只测单轮问答，不适评 LLM 漏洞评估能力
- 🔬 **研究方法**：OmniVul 含 2,000 个 CVE、23 个属性的问答对（检测、定位、根因、补丁建议），RAG 聚合多源并用 LLM-as-a-Judge 与 conformal prediction 质控
- 📌 **结论**：五个 SOTA LLM 上漏洞代码检测与 CVE 识别 top-1 准确率平均低于 50%，缺可靠评估所需的关键推理能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With more than 20,000 Common Vulnerabilities and Exposures (CVEs) reported annually, software vulnerabilities represent a critical cybersecurity challenge. This volume has intensified the demand for automated detection and analysis, motivating the integration of large language models (LLMs) for such tasks. However, existing vulnerability benchmarks are not suitable for evaluating LLMs' capabilities in vulnerability assessment, as most of them 1) rely on narrow data sources, 2) lack deep context, and 3) focus on single-turn Q&A rather than realistic, multi-stage analyst workflows. To address this gap, we introduce OmniVul, a comprehensive multi-turn benchmark for LLM-based vulnerability assessment. OmniVul comprises 2,000 CVEs with question–answer pairs spanning 23 attributes, including detection, code localization, root cause analysis, and patch suggestion. We employ an automated workflow to aggregate multi-source data via Retrieval-Augmented Generation (RAG), ensuring quality through LLM-as-a-Judge filtering and conformal prediction calibrated by human expert annotations. An evaluation of five state-of-the-art LLMs on OmniVul reveals distinct performance gaps, with top-1 accuracy remaining below 50% on average for vulnerable code detection and CVE identification. Our evaluation also demonstrates that current models lack critical reasoning capabilities for reliable vulnerability assessment. These results highlight the importance of OmniVul for advancing research in evaluating and fine-tuning LLMs for vulnerability assessment.

</details>

### 22. Cochise: A Reference Harness for Autonomous Penetration Testing

📄 [arXiv](https://arxiv.org/abs/2605.11671) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-tools-and-data-sets/59/Cochise-A-Reference-Harness-for-Autonomous-Penetration-Testing)　📅 2026-05　🏷 ASE 2026

**关键词**：`tool`、`autonomous pentesting`、`planner-executor`、`trajectory logging`、`capability`

👤 **作者**：Andreas Happe、Jürgen Cito

- 🎯 **研究动机**：自主渗透测试系统把架构、提示与工具选择捆绑，难以分辨相对简单 agent 与 harness 的真实增益
- 🔬 **研究方法**：Cochise 为 630 行 Python 参考实现：Planner-Executor 架构、SSH 执行、ReAct 式自纠错，附回放与日志分析工具及 GOAD 轨迹语料
- 📌 **结论**：定位为可复用实验基础设施而非 SOTA agent，支持对比模型、架构与渗透轨迹

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work on LLM-driven autonomous penetration testing reports promising results, but existing systems often bundle architectural, prompting, and tool-integration choices together. This makes it difficult to determine what is gained over a simple agent and harness. We present Cochise, a 630 LOC Python reference implementation for autonomous penetration-testing experiments. Cochise connects to a Linux execution host over SSH and supports attacking controlled target environments reachable from that jump host. The prototype implements a Planner--Executor architecture in which long-term state is maintained by the planner, while a ReAct-style executor issues commands over SSH and self-corrects based on command outputs. The scenario prompt can be adapted to different target environments. We evaluate the harness against a live third-party testbed, Game of Active Directory (GOAD). Cochise is intended not as a state-of-the-art penetration-testing agent, but as a reusable experimental infrastructure for comparing models, agent architectures, and penetration-testing traces. Alongside the prototype, we release replay and analysis tools: (i) cochise-replay for offline visualization of captured runs, (ii) cochise-analyze-logs and cochise-analyze-graphs for cost, token, duration, and compromise analysis, and (iii) a corpus of JSON trajectory logs from GOAD runs, so that researchers can study agent behavior without provisioning the 48--64 GB RAM / 190 GB storage testbed themselves. Tool demo video available at https://youtu.be/2mQimB1ufyI.

</details>

### 23. Teams of LLM Agents can Exploit Zero-Day Vulnerabilities

🎓 [Official](https://aclanthology.org/2026.eacl-long.2/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`zero-day exploit`、`multi-agent team`、`cyber capability`

👤 **作者**：Yuxuan Zhu、…、Daniel Kang

- 🎯 **研究动机**：单个 LLM agent 在事先未知的零日漏洞上表现差，难以探索多种漏洞并做长程规划
- 🔬 **研究方法**：提出 HPTSA：规划 agent 探索系统并决定调用哪些子 agent，解决跨漏洞尝试时的长期规划问题；构建 14 个真实零日漏洞基准
- 📌 **结论**：agent 团队较先前 agent 框架最高提升 4.3 倍，证明 LLM agent 团队可利用真实零日漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents have become increasingly sophisticated, especially in the realm of cybersecurity. Researchers have shown that LLM agents can exploit real-world vulnerabilities when given a description of the vulnerability and toy capture-the-flag problems. However, these agents still perform poorly on real-world vulnerabilities that are unknown to the agent ahead of time (zero-day vulnerabilities).In this work, we show that teams of LLM agents can exploit real-world, zero-day vulnerabilities. Prior agents struggle with exploring many different vulnerabilities and long-range planning when used alone. To resolve this, we introduce HPTSA, a system of agents with a planning agent that can launch subagents. The planning agent explores the system and determines which subagents to call, resolving long-term planning issues when trying different vulnerabilities. We construct a benchmark of 14 real-world vulnerabilities and show that our team of agents improve over prior agent frameworks by up to 4.3×.

</details>

### 24. GoodVibe: Security-by-Vibe for LLM-Based Code Generation

📄 [arXiv](https://arxiv.org/abs/2602.10778) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/thang)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`defense`、`code generation`、`cyber misuse`、`offensive capability`、`neuron-level tuning`、`secure code`

👤 **作者**：Maximilian Thang、…、Ahmad-Reza Sadeghi

- 🎯 **研究动机**：vibe coding 场景安全需求不明确，模型常产出功能正确但不安全的代码；全参微调代价高且易灾难遗忘
- 🔬 **研究方法**：GoodVibe 基于梯度归因定位安全关键神经元子集，仅更新该子集并用激活驱动聚类降低训练成本，在 6 个 LLM 上评估
- 📌 **结论**：代码安全性最高提升 2.5 倍，可训练参数比全参微调少 4700 倍以上，训练计算比 LoRA 低 3.6 倍以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for code generation in fast, informal development workflows, often referred to as vibe coding, where speed and convenience are prioritized, and security requirements are rarely made explicit. In this setting, models frequently produce functionally correct but insecure code, creating a growing security risk. Existing approaches to improving code security rely on full-parameter fine-tuning or parameter-efficient adaptations, which are either costly and prone to catastrophic forgetting or operate at coarse granularity with limited interpretability and control. We present GoodVibe, a neuron-level framework for improving the security of code language models by default. GoodVibe is based on the key insight that security-relevant reasoning is localized to a small subset of neurons. We identify these neurons using gradient-based attribution from a supervised security task and perform neuron-selective fine-tuning that updates only this security-critical subspace. To further reduce training cost, we introduce activation-driven neuron clustering, enabling structured updates with minimal overhead. We evaluate GoodVibe on six LLMs across security-critical programming languages, including C++, Java, Swift, and Go. GoodVibe substantially improves the security of generated code while preserving general model utility, achieving up to a 2.5x improvement over base models, achieving performance competitive with full fine-tuning while using over 4,700x fewer trainable parameters, and reducing training computation by more than 3.6x compared to the parameter-efficient baseline (LoRA). Our results demonstrate that neuron-level optimization offers an effective and scalable approach to securing code generation without sacrificing generality.

</details>

### 25. VIPER Strike: Defeating Visual Reasoning CAPTCHAs via Structured Vision–Language Inference

📄 [arXiv](https://arxiv.org/abs/2601.06461) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/qi-minfeng)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`attack`、`visual reasoning CAPTCHA`、`VLM safety`、`cyber misuse`、`VLM solver`、`automation`

👤 **作者**：Minfeng Qi、Dongyang He、Qin Wang、Lefeng Zhang

- 🎯 **研究动机**：现有视觉推理 CAPTCHA 求解器要么依赖模板专用检测器、要么缺细粒度视觉感知，均无通用性
- 🔬 **研究方法**：ViPer 模块化流水线：解析视觉布局、把属性接地到问题语义并推断目标坐标，融合结构化多目标感知与自适应 LLM 推理
- 📌 **结论**：六大 VRC 供应商上成功率最高 93.2%，超 GraphNet（83.2%）与 Oedipus（65.8%）等基线，跨 LLM 骨干保持 90% 以上；所提 Template-Space Randomization 可削弱求解器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual Reasoning CAPTCHAs (VRCs) combine visual scenes with natural-language queries that demand compositional inference over objects, attributes, and spatial relations. They are increasingly deployed as a primary defense against automated bots. Existing solvers fall into two paradigms: vision-centric, which rely on template-specific detectors but fail on novel layouts, and reasoning-centric, which leverage LLMs but struggle with fine-grained visual perception. Both lack the generality needed to handle heterogeneous VRC deployments. We present ViPer, a unified attack framework that integrates structured multi-object visual perception with adaptive LLM-based reasoning. ViPer parses visual layouts, grounds attributes to question semantics, and infers target coordinates within a modular pipeline. Evaluated on six major VRC providers (VTT, Geetest, NetEase, Dingxiang, Shumei, Xiaodun), ViPer achieves up to 93.2% success, approaching human-level performance across multiple benchmarks. Compared to prior solvers, GraphNet (83.2%), Oedipus (65.8%), and the Holistic approach (89.5%), ViPer consistently outperforms all baselines. The framework further maintains robustness across alternative LLM backbones (GPT, Grok, DeepSeek, Kimi), sustaining accuracy above 90%. To anticipate defense, we further introduce Template-Space Randomization (TSR), a lightweight strategy that perturbs linguistic templates without altering task semantics. TSR measurably reduces solver (i.e., attacker) performance. Our proposed design suggests directions for human-solvable but machine-resistant CAPTCHAs.

</details>

### 26. From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-tingxuan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`CTF agent`、`human-in-the-loop`、`cyber misuse`、`AI cyber capability`

👤 **作者**：Tingxuan Tang、…、Yue Xiao

- 🎯 **研究动机**：现有 AI CTF 评测孤立评估单题求解，人类玩家对 AI 辅助的感知、协作方式及人机组合与全自主 agent 的对比是知识空白
- 🔬 **研究方法**：首个现场 CTF 的 AI 辅助实证研究：41 名参与者的感知与信任变化及协作分析，并在同一新题集上基准测试四个自主 CTF agent
- 📌 **结论**：AI 素养与领域知识互补且各有不可替代优势；尽管自主 agent 表现出色，human-in-the-loop 是制胜范式——AI 加速探索、人类提供定向指导与验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Capture-the-Flag (CTF) competitions are increasingly becoming a testbed for evaluating AI capabilities at solving security tasks, due to their controlled environments and objective success criteria. Existing evaluations have focused on how successful AI is at solving individual CTF challenges in isolation from human CTF players. As AI usage increases in both academic and industrial settings, it is equally likely that human CTF players may collaborate with AI agents to solve CTF challenges. This possibility exposes a key knowledge gap: how do human players perceive AI CTF assistance; when assistance is provided, in what ways do they collaborate and is it effective with respect to human performance; how do humans assisted by AI compare to the performance of fully autonomous AI agents on the same set of challenges. We address this gap with the first empirical study of AI assistance in a live, onsite CTF. In a study with 41 participants (out of the total 95 that participated in the CTF), we qualitatively study (i) how participants' perception, trust, and expectations shift before versus after hands-on AI use, and (ii) how participants collaborate with an instrumented AI assistant. Moreover, we also (iii) benchmark four autonomous CTF agents on the same fresh challenge set to compare outcomes with human teams and analyze agent trajectories. We find that, for human players, AI literacy and domain knowledge are complementary competencies, and both have irreplaceable advantages. Proficient and efficient use of AI amplifies professional skills. Importantly, although advanced autonomous agents showed outstanding performance, human-in-the-loop is the winning paradigm where AI accelerates exploration while humans provide targeted guidance and verification. We conclude with implications for the future design of CTF competitions and for building effective human-in-the-loop AI systems for security.

</details>

### 27. HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation

📄 [arXiv](https://arxiv.org/abs/2601.13864) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1080.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`benchmark`、`secure code generation`、`hardware CWE`、`execution testing`

👤 **作者**：Qirui Chen、…、Jian Yang

- 🎯 **研究动机**：LLM 硬件/固件代码生成评测只重功能正确性，忽视部署后可致灾难的安全漏洞
- 🔬 **研究方法**：HardSecBench 含 924 个任务覆盖 Verilog RTL 与固件 C、76 个硬件相关 CWE，多智能体管线以执行证据为基础做可靠评测
- 📌 **结论**：LLM 常满足功能要求却留下安全风险，且安全表现随提示方式波动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for hardware and firmware code generation, but existing studies primarily evaluate functional correctness while largely overlooking security. However, LLM-generated code that appears functionally sound may embed security flaws which could induce catastrophic damages after deployment. This critical research gap motivates us to design a benchmark for assessing security awareness under realistic specifications. In this work, we introduce HardSecBench, a benchmark with 924 tasks spanning Verilog Register Transfer Level (RTL) and firmware-level C, covering 76 hardware-relevant Common Weakness Enumeration (CWE) entries. Each task includes a structured specification, a secure reference implementation, and executable tests. To automate artifact synthesis, we propose a multi-agent pipeline that decouples synthesis from verification and grounds evaluation in execution evidence, enabling reliable evaluation. We evaluate diverse LLMs and find that they often satisfy functional requirements while leaving security risks. We also find that security results vary with prompting. These findings highlight pressing challenges and offer actionable insights for future advancements in LLM-assisted hardware design. Our data and code are available at https://github.com/chenqirui2002/HardSecBench.

</details>

### 28. Self-Discovering Security Oracles: Meta-learning Vulnerability Detection Strategies through Adversarial Self-Play

🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/216/Self-Discovering-Security-Oracles-Meta-learning-Vulnerability-Detection-Strategies-t)　📅 2026　🏷 ASE 2026

**关键词**：`tool`、`vulnerability generation`、`adversarial self-play`、`meta-learning`、`capability`

- 🎯 **研究动机**：漏洞检测策略依赖人工定义oracle，难以为继
- 🔬 **研究方法**：以对抗自博弈元学习自动发现检测策略
- 📌 **结论**：自动产生的oracle发现更多真实漏洞

### 29. ThreatCraft: Automated Attack Scenario Generation via Hybrid Rule-Based and LLM-Driven Reasoning

🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-tools-and-data-sets/16/ThreatCraft-Automated-Attack-Scenario-Generation-via-Hybrid-Rule-Based-and-LLM-Drive)　📅 2026　🏷 ASE 2026

**关键词**：`tool`、`attack scenario generation`、`LLM reasoning`、`cyber range`、`capability`

- 🎯 **研究动机**：攻击场景构建依赖专家知识，难规模化
- 🔬 **研究方法**：ThreatCraft混合规则与LLM推理自动生成cyber range攻击场景
- 📌 **结论**：自动产出多样可用的攻击场景

### 30. COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers

📄 [arXiv](https://arxiv.org/abs/2512.02318) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-junyu)　📅 2025-12　🏷 USENIX Security 2026

**关键词**：`benchmark`、`VLM safety`、`cyber misuse`、`offensive capability`、`MLLM CAPTCHA solver`、`structural hardening`

👤 **作者**：Junyu Wang、…、Junjie Xiong

- 🎯 **研究动机**：现成 MLLM 可低成本自动化破解视觉 CAPTCHA，其威胁程度与防御方向不明
- 🔬 **研究方法**：在 18 种真实 CAPTCHA 任务上评测 7 个 MLLM 的单发准确率、重试成功率、延迟与成本，分析推理轨迹并推导任务选择与加固指南
- 📌 **结论**：识别型低交互任务可被人本级成本与延迟破解；加入细粒度定位与隐式计数后 SOTA MLLM 成功率从超 95% 降至 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper studies how multimodal large language models (MLLMs) undermine the security guarantees of visual CAPTCHA. We identify the attack surface where an adversary can cheaply automate CAPTCHA solving using off-the-shelf models. We evaluate 7 representative MLLMs on 18 real-world CAPTCHA task types, measuring single-shot accuracy, success under limited retries, end-to-end latency, and per-solve cost. We further validate our findings through a supplemental external dataset and an adaptive-attacker setting with session memory, while also analyzing the impact of task-specific prompt engineering and few-shot demonstrations on solver effectiveness. We reveal that MLLMs can reliably solve recognition-oriented and low-interaction CAPTCHA tasks at human-like cost and latency, whereas tasks requiring fine-grained localization, multi-step spatial reasoning, or cross-frame consistency remain significantly harder for current models. By examining the reasoning traces of such MLLMs, we investigate the underlying mechanisms of why models succeed/fail on specific CAPTCHA puzzles and use these insights to derive defense-oriented guidelines for selecting and strengthening CAPTCHA tasks. To validate these principles, we present a proof-of-concept by hardening a vulnerable CAPTCHA type using our guidelines. We demonstrate that incorporating fine-grained localization and implicit counting reduces the success rate of state-of-the-art MLLMs from over 95\% to 0\%, confirming that structural changes can effectively mitigate the threat. We conclude by emphasizing the urgent need for CAPTCHA redesign as MLLM capabilities increasingly threaten existing defenses. Code Availability (https://doi.org/10.5281/zenodo.20406852).

</details>

### 31. SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned

📄 [arXiv](https://arxiv.org/abs/2602.07666) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-cen)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`survey`、`AIxCC`、`cyber misuse`、`offensive capability`、`AI cyber capability`、`autonomous remediation`

👤 **作者**：Cen Zhang、…、Taesoo Kim

- 🎯 **研究动机**：AIxCC 是最大规模的自主网络推理系统竞赛，缺少系统性的复盘分析
- 🔬 **研究方法**：基于设计文档、源码、执行轨迹与组织者/团队访谈，分析赛制设计、决赛 CRS 架构及榜单之外的结果
- 📌 **结论**：识别出真正驱动 CRS 性能的因素与团队真实技术进展，指出自主 CRS 实际部署的开放局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

DARPA's AI Cyber Challenge (AIxCC, 2023--2025) is the largest competition to date for building fully autonomous cyber reasoning systems (CRSs) that leverage recent advances in AI -- particularly large language models (LLMs) -- to discover and remediate vulnerabilities in real-world open-source software. This paper presents the first systematic analysis of AIxCC. Drawing on design documents, source code, execution traces, and discussions with organizers and competing teams, we examine the competition's structure and key design decisions, characterize the architectural approaches of finalist CRSs, and analyze competition results beyond the final scoreboard. Our analysis reveals the factors that truly drove CRS performance, identifies genuine technical advances achieved by teams, and exposes limitations that remain open for future research. We conclude with lessons for organizing future competitions and broader insights toward deploying autonomous CRSs in practice.

</details>

### 32. Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents

📄 [arXiv](https://arxiv.org/abs/2602.02164) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60747)　📅 2026-02　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`、`agent safety`

👤 **作者**：Pengfei He、…、Long T. Le

- 🎯 **研究动机**：LLM 网络安全 agent 在自动漏洞发现与利用上受限于交互不足、执行接地弱与经验不可复用
- 🔬 **研究方法**：Co-RedTeam 集成安全领域知识、代码感知分析、执行接地的迭代推理与长期记忆，把漏洞分析分解为协同的发现与利用两阶段，基于真实执行反馈学习
- 📌 **结论**：漏洞利用成功率超 60%、漏洞检测绝对提升超 10%，消融证实执行反馈与记忆是关键

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have shown promise in assisting cybersecurity tasks, yet existing approaches struggle with automatic vulnerability discovery and exploitation due to limited interaction, weak execution grounding, and a lack of experience reuse. We propose Co-RedTeam, a security-aware multi-agent framework designed to mirror real-world red-teaming workflows by integrating security-domain knowledge, code-aware analysis, execution-grounded iterative reasoning, and long-term memory. Co-RedTeam decomposes vulnerability analysis into coordinated discovery and exploitation stages, enabling agents to plan, execute, validate, and refine actions based on real execution feedback while learning from prior trajectories. Extensive evaluations on challenging security benchmarks demonstrate that Co-RedTeam consistently outperforms strong baselines across diverse backbone models, achieving over 60% success rate in vulnerability exploitation and over 10% absolute improvement in vulnerability detection. Ablation and iteration studies further confirm the critical role of execution feedback, structured interaction, and memory for building robust and generalizable cybersecurity agents.

</details>

### 33. CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities

📄 [arXiv](https://arxiv.org/abs/2606.04460) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62134)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`cyber misuse`、`agent safety benchmark`、`trajectory evaluation`、`agent safety`、`empirical evaluation`

👤 **作者**：Tianneng Shi、…、Dawn Song

- 🎯 **研究动机**：现有 AI 网络安全评测规模或范围受限，未覆盖真实漏洞发现到修复的端到端生命周期
- 🔬 **研究方法**：CyberGym-E2E 用自动化 agent 增强管线把开源漏洞数据转为现实评测环境，全面评估漏洞发现、PoC 生成与补丁生成
- 📌 **结论**：基准覆盖 139 个开源项目的 920 个真实漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI has the potential to transform cybersecurity by enabling systems that can autonomously detect, analyze, and remediate software vulnerabilities. However, existing cybersecurity evaluations of AI systems are limited in scale or scope, and fail to capture the end-to-end lifecycle of real-world software vulnerability discovery and remediation. To address this gap, we propose CyberGym-E2E, a large-scale and realistic end-to-end cybersecurity benchmark that comprehensively evaluates AI agents' abilities across the full lifecycle of vulnerability discovery, PoC generation, and patch generation. CyberGym-E2E is comprehensive and scalable, as we build an automated, agent-enhanced pipeline for transforming open-source vulnerability data into realistic evaluation environments. Currently, the benchmark consists of 920 real-world vulnerabilities across 139 different open-source projects.

</details>

### 34. A New Framework for Cybersecurity Refusals in AI Agents

📄 [arXiv](https://arxiv.org/abs/2606.02644) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61093)　📅 2026　🏷 ICML 2026

**关键词**：`tool`、`analysis`、`cyber misuse`、`agent safety benchmark`、`trajectory evaluation`、`agent safety`

👤 **作者**：Eliot Krzysztof Jones、Mateusz Dziemian、Matt Fredrikson、J Zico Kolter

- 🎯 **研究动机**：网络安全 Agent 基准只测攻击任务熟练度，忽视何时以及如何拒绝有害请求
- 🔬 **研究方法**：建立进攻性安全语境下拒答边界的首套框架：任务应被拒绝的原则性判据、应拒任务类别与良性／对抗双条件下的鲁棒性评测方法，并应用于 Web 进攻安全场景
- 📌 **结论**：八个 frontier 模型中六个在识别真实系统漏洞的任务上 0% 拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic scaffolds have dramatically improved LLM performance on complex, long-horizon tasks, yielding both broad benefits and amplified risks in domains like cybersecurity. Existing benchmarks for AI agents in cybersecurity focus mainly on measuring proficiency–how effectively agents can complete offensive security tasks–but neglect a critical question: when and how should agents refuse harmful requests? We present the first framework for establishing refusal boundaries in offensive security contexts. Our framework defines (1) principled criteria for when tasks should be refused, (2) categories of tasks that warrant refusal, and (3) evaluation methodology for measuring agent robustness under both benign and adversarial conditions. We apply this framework to assess how current LLM-powered agents adhere to appropriate refusal boundaries across a range of web-based offensive security scenarios, finding that 6 of 8 frontier models tested refuse to identify vulnerabilities in real systems 0\% of the time.

</details>

### 35. Training Language Model Agents to Find Vulnerabilities with CTF-Dojo

📄 [arXiv](https://arxiv.org/abs/2508.18370) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61783)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`tool-use agent`、`tool interface`、`action integrity`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Terry Yue Zhuo、Dingmin Wang、Hantian Ding、Varun Kumar、Zijian Wang

- 🎯 **研究动机**：可执行且带可验证反馈的训练环境稀缺，制约更强 ML 智能体的发展
- 🔬 **研究方法**：提出 CTF-Dojo：658 个 Docker 化 CTF 挑战的可复现运行时；CTF-Forge 自动把公开构件转化为执行环境；仅用 486 条执行验证轨迹训练 LLM 智能体
- 📌 **结论**：在 InterCode-CTF、NYU CTF Bench 与 Cybench 上绝对提升至多 11.6%；32B 模型 Pass@1 达 31.9%，创开源权重 SOTA，比肩 DeepSeek-V3 与 Gemini-2.5-Flash

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated exceptional capabilities when trained within executable runtime environments, notably excelling at software engineering tasks through verified feedback loops. Yet, scalable and generalizable execution-grounded environments remain scarce, limiting progress in training more capable ML agents. We introduce CTF-Dojo, the first large-scale executable runtime tailored for training LLMs with verifiable feedback, featuring 658 fully functional Capture-The-Flag (CTF)-style challenges containerized in Docker with guaranteed reproducibility. To enable rapid scaling without manual intervention, we develop CTF-Forge, an automated pipeline that transforms publicly available artifacts into ready-to-use execution environments in minutes, eliminating weeks of expert configuration traditionally required. We trained LLM-based agents on just 486 high-quality, execution-verified trajectories from CTF-Dojo, achieving up to 11.6% absolute gains over strong baselines across three competitive benchmarks: InterCode-CTF, NYU CTF Bench, and Cybench. Our best-performing 32B model reaches 31.9% Pass@1, establishing a new open-weight state-of-the-art that rivals frontier models like DeepSeek-V3-0324 and Gemini-2.5-Flash. By framing CTF-style tasks as a benchmark for executable-agent learning, CTF-Dojo demonstrates that execution-grounded training signals are not only effective but pivotal in advancing high-performance ML agents without dependence on costly proprietary systems.

</details>

### 36. The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again

📄 [arXiv](https://arxiv.org/abs/2508.19774) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-tong)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`attack`、`model supply chain`、`Pickle`、`stealthy poisoning`

👤 **作者**：Tong Liu、Guozhu Meng、Peng Zhou、Zizhuang Deng、Shuaiyin Yao、Kai Chen

- 🎯 **研究动机**：pickle 反序列化漏洞长期未解，现有扫描器对模型投毒面理解不全、检测逻辑脆弱
- 🔬 **研究方法**：系统披露 pickle 投毒面：识别五大框架 22 条模型加载路径（19 条被漏检），提出 Exception-Oriented Programming 绕过技术，并在风险函数面发现 133 个可利用 gadget
- 📌 **结论**：gadget 绕过率近 100%，最佳扫描器下仍达 89%；获厂商致谢与 6000 美元赏金

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pickle deserialization vulnerabilities have persisted throughout Python's history, remaining widely recognized yet unresolved. Due to its ability to transparently save and restore complex objects into byte streams, many AI/ML frameworks continue to adopt pickle as the model serialization protocol despite its inherent risks. As the open-source model ecosystem grows, model-sharing platforms such as Hugging Face have attracted massive participation, significantly amplifying the real-world risks of pickle exploitation and opening new avenues for model supply chain poisoning. Although several state-of-the-art scanners have been developed to detect poisoned models, their incomplete understanding of the poisoning surface leaves the detection logic fragile and allows attackers to bypass them. In this work, we present the first systematic disclosure of the pickle-based model poisoning surface from both model loading and risky function perspectives. Our research demonstrates how pickle-based model poisoning can remain stealthy and highlights critical gaps in current scanning solutions. On the model loading surface, we identify 22 distinct pickle-based model loading paths across five foundational AI/ML frameworks, 19 of which are entirely missed by existing scanners. We further develop a bypass technique named Exception-Oriented Programming (EOP) and discover 9 EOP instances, 7 of which can bypass all scanners. On the risky function surface, we discover 133 exploitable gadgets, achieving almost a 100% bypass rate. Even against the best-performing scanner, these gadgets maintain an 89% bypass rate. By systematically revealing the pickle-based model poisoning surface, we achieve practical and robust bypasses against real-world scanners. We responsibly disclose our findings to corresponding vendors, receiving acknowledgments and a $6000 bug bounty.

</details>

### 37. SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system

📄 [arXiv](https://arxiv.org/abs/2608.15012)　📅 2026-08

**关键词**：`defense`、`adversarial robustness`、`robust training`、`certification`

👤 **作者**：Yuhan Meng、…、Ding Li

- 🎯 **研究动机**：网络安全攻防不对称：攻击走向自主执行而防御仍人工密集，双方演化在三层停滞
- 🔬 **研究方法**：SysEvolve 共演化系统：SysField 构建真实多主机靶场、SysSpear 生成高效安全攻击、SysArmor 实时可解释防御，形成自驱动对抗循环
- 📌 **结论**：2.1% 开销零损耗采集并编排 257 个 CVE 成 1148 个靶场；攻击成功率超基线 LLM 25% 以上，防御精度高 10-1000 倍并在华为、深信服生产环境检出真实 APT

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of large language models (LLMs) has created a growing asymmetry in cybersecurity, where attack accelerates toward autonomous execution while defense remains predominantly human-intensive. Despite substantial prior work across cyber ranges, AI-driven attack, and AI-driven defense, this asymmetry persists. We trace it to a deeper root cause, that evolution itself has stalled on both sides at three layers. To overcome this, we propose co-evolution as the integrating insight, where attack and defense AI agents autonomously and safely drive each other's evolution through adversarial confrontation. Based on this insight, we present \sysevolve, comprising three co-designed components, \sysfield, \sysspear, and \sysarmor. \sysfield constructs realistic multi-host ranges. \sysspear generates efficient, safe attack schemes. \sysarmor performs real-time, interpretable defense. Together they form a self-driven adversarial loop restoring evolution at all three layers. In evaluation, \sysfield achieves zero-loss collection at 2.1\% overhead and orchestrates 257 CVEs into 1,148 ranges, \sysspear improves attack success by over 25\% over baseline LLMs, and \sysarmor achieves 10--1000$\times$ greater precision than prior systems and detects real APT attacks in production at Huawei and Sangfor. Our evaluation also reveals three findings about LLM agent capabilities. First, multi-step composition and larger topologies expose agent capability gaps hidden by single-step evaluations. Second, the bottleneck lies after initial access in post-compromise state utilization. Third, LLM agents are susceptible to environmental interference. When decoy endpoints are deployed in the range, agent timeouts triple and downstream completion disappears despite the success rates of initial accesses are unchanged.

</details>

### 38. Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives

📄 [arXiv](https://arxiv.org/abs/2609.16694)　📅 2026-09

**关键词**：`survey`、`pentest agent`、`threat taxonomy`、`guardrail`、`trust boundary`

👤 **作者**：Rahul Dev T Y、Hiran V Nath

- 🎯 **研究动机**：LLM 驱动的自主渗透测试 agent 具备持久记忆、真实世界动作与长程推理能力，其安全关注点与传统对话式 LLM 质的不同；面向会话式 AI 的既有 guardrail 不足以约束它们
- 🔬 **研究方法**：对自主 AI pentest agent 做系统安全分析：解析代表性架构、刻画信任边界与攻击面，提出覆盖 agent 生命周期的威胁分类法——LLM 生命周期攻击、agent 架构攻击与跨切行为攻击；逐类分析既有 guardrail 机制的局限
- 📌 **结论**：识别出关键研究缺口：需要面向上下文与架构感知的专用 guardrail 才能保障下一代 AI 攻防系统——为 offensive agent 自身的安全研究提供威胁模型底图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-powered autonomous agents are transforming the penetration testing space with dynamic, multi-step offensive security workflows that require minimal supervision by humans. These agents leverage sophisticated reasoning abilities and external security tools to independently carry out reconnaissance, identify vulnerabilities, devise exploitation plans, and perform post-exploitation operations. But the ability to have persistent memory, to take actions in the real world, and to do long-horizon reasoning raises qualitatively different security concerns than traditional chat-based LLM systems. Existing guardrail mechanisms for conversational AI may not be sufficient to secure autonomous AI pentesting agents accordingly. To address these issues, we carry out a comprehensive security analysis on autonomous AI-penetration testing agents. We systematically analyse representative agent architectures, characterise their trust boundaries and attack surfaces and propose a threat taxonomy that is aligned with the lifecycle and covers LLM lifecycle attacks, agent-architecture attacks and cross-cutting behavioural attacks. We analyse the limitations of existing guardrail mechanisms, identify key research gaps, and discuss future research directions for developing specialised, context-aware, and architecture-aware guardrails to secure next-generation AI-driven offensive security systems.

</details>

### 39. MiST: Mid-Training LLMs for Cybersecurity

📄 [arXiv](https://arxiv.org/abs/2609.18496)　📅 2026-09

**关键词**：`tool`、`cybersecurity LLM`、`mid-training`、`domain model`、`security capability`

👤 **作者**：Oded Ovadia、Elad Ben Zaken、Elad Guttman、Orly Moreno Kadosh

- 🎯 **研究动机**：网络安全结合高风险分析与复杂技术语言，是 LLM 高影响高挑战领域——通用模型在公开安全基准上的表现有明确提升空间
- 🔬 **研究方法**：MiST（Mid-trained Security Transformer）8B/32B 套件：在通用预训练与安全领域训练之间加中间适应阶段——不做大体量持续预训练，而是精选专家审定种子语料并转化为高质量领域合成数据；消融定位增益来源（中间训练+SFT 阶段的合成数据流）
- 📌 **结论**：最终 checkpoint 相对 Qwen 基线平均安全准确率 +13.1pp（8B）/+8.6pp（32B），相对 +27.0%/+15.8%；为下游任务微调与 RL 提供更强初始化——安全域专用模型的能力底座

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cybersecurity combines high-stakes analysis with complex technical language, making it an impactful and challenging domain for LLMs. We present MiST (Mid-trained Security Transformer), a suite of 8B and 32B models that achieve strong performance on public cybersecurity benchmarks. We use mid-training as an intermediate adaptation stage between general pre-training and cybersecurity training. Rather than performing continual pre-training over large volumes of raw domain text, we curate a compact, expert-vetted seed corpus, and transform it into high-quality domain-specific synthetic training data. The final MiST checkpoints improve mean cybersecurity accuracy by +13.1 and +8.6 absolute percentage points over the corresponding Qwen baselines for 8B and 32B, respectively, corresponding to relative gains of +27.0% and +15.8%. Ablation results further show that these cybersecurity gains arise in the mid-training and supervised fine-tuning stages through a combination of the synthetic data generation flows. Furthermore, we show that MiST provides a stronger initialization for downstream task-specific fine-tuning adaptation and reinforcement learning.

</details>
