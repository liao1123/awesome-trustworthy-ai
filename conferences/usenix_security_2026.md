# USENIX Security 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [智能体、RAG 与提示注入安全](#智能体rag-与提示注入安全)
- [越狱、安全对齐与内容防护](#越狱安全对齐与内容防护)
- [投毒、后门与模型供应链](#投毒后门与模型供应链)
- [隐私泄漏、成员推断与机密计算](#隐私泄漏成员推断与机密计算)
- [水印、溯源与模型知识产权](#水印溯源与模型知识产权)
- [对抗样本、多模态与物理攻击](#对抗样本多模态与物理攻击)
- [AI 滥用、网络能力与部署治理](#ai-滥用网络能力与部署治理)
- [综述、基准与方法论评测](#综述基准与方法论评测)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | 35th USENIX Security Symposium (USENIX Security 2026) |
| 举办时间与地点 | 2026-08-12 至 2026-08-14；Baltimore Marriott Waterfront, Baltimore, Maryland, USA |
| 官方网站 | [USENIX Security '26](https://www.usenix.org/conference/usenixsecurity26) |
| 官方录用列表 | [Technical Sessions](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) |
| 正式论文集 | [USENIX Security '26 Full Proceedings](https://www.usenix.org/sites/default/files/sec26_full_proceedings.pdf) |
| 检查范围 | 两轮录用的 refereed papers；排除 Enigma 与其他邀请报告；数据截至 2026-08-22 |

## 关键节点

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Cycle 1 paper registration deadline | 2025-08-19 23:59 AoE | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 1 paper submission deadline | 2025-08-26 23:59 AoE | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 1 notification | 2025-12-04 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 1 shepherd approval deadline | 2025-12-18 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 1 final files deadline | 2026-01-15 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 2 paper registration deadline | 2026-01-29 23:59 AoE | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 2 paper submission deadline | 2026-02-05 23:59 AoE | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 2 notification | 2026-05-14 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 2 shepherd approval deadline | 2026-05-28 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Cycle 2 final files deadline | 2026-06-11 | [Call for Papers](https://www.usenix.org/conference/usenixsecurity26/call-for-papers) |
| Symposium | 2026-08-12 至 2026-08-14 | [USENIX Security '26](https://www.usenix.org/conference/usenixsecurity26) |

## 筛选说明

- 官方论文总数：362（两轮 refereed papers；以官方 [Conference Message](https://www.usenix.org/sites/default/files/sec26_message.pdf) 为准）
- 初筛候选：98
- 最终收录：80
- 收录口径：只收录以 AI/ML 模型、生成式系统或智能体为直接攻击对象，或以其危险能力、恶意使用、隐私泄漏、安全评测与缓解为核心问题的论文；仅将 AI 用作常规安全分析工具，以及没有具体 AI 安全 threat model 的一般鲁棒性、隐私政策或 HCI 工作从严排除。
- 计数说明：Technical Sessions 页面还包含 18 场 Enigma 邀请报告，不能直接把所有日程节点当作录用论文。

## 论文分类

### 智能体、RAG 与提示注入安全

### 1. AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations

📄 [arXiv](https://arxiv.org/abs/2603.10749) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/he-yu)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`indirect prompt injection`、`causal attribution`、`tool invocation`、`agent prompt injection`、`indirect injection`

👤 **作者**：Yu He、…、Zhan Qin

- 🎯 **研究动机**：把间接注入当输入级语义判别问题的防御难以泛化到未见 payload
- 🔬 **研究方法**：动作级因果归因：AttriGuard 对每个工具调用做并行反事实测试，结合 teacher-forced 影子重放防归因混淆、层级控制衰减与模糊生存准则抗 LLM 随机性
- 📌 **结论**：4 个 LLM、2 个基准上静态攻击 ASR 为 0%、效用损失可忽略，在自适应优化攻击下依然稳健而领先防御显著退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are highly vulnerable to Indirect Prompt Injection (IPI), where adversaries embed malicious directives in untrusted tool outputs to hijack execution. Most existing defenses treat IPI as an input-level semantic discrimination problem, which often fails to generalize to unseen payloads. We propose a new paradigm, action-level causal attribution, which secures agents by asking why a particular tool call is produced. The central goal is to distinguish tool calls supported by the user's intent from those causally driven by untrusted observations. We instantiate this paradigm with AttriGuard, a runtime defense based on parallel counterfactual tests. For each proposed tool call, AttriGuard verifies its necessity by re-executing the agent under a control-attenuated view of external observations. Technically, AttriGuard combines teacher-forced shadow replay to prevent attribution confounding, hierarchical control attenuation to suppress diverse control channels while preserving task-relevant information, and a fuzzy survival criterion that is robust to LLM stochasticity. Across four LLMs and two agent benchmarks, AttriGuard achieves 0% ASR under static attacks with negligible utility loss and moderate overhead. Importantly, it remains resilient under adaptive optimization-based attacks in settings where leading defenses degrade significantly.

</details>

### 2. Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/luo)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`LLM agent`、`resource exhaustion`、`denial of service`、`LLM-agent DoS`、`resource lifecycle`

👤 **作者**：Jiaqi Luo、…、Yuan Zhang

- 🎯 **研究动机**：LLM agent 缺乏资源治理，易被滥用导致资源耗尽与拒绝服务，此前无系统安全研究
- 🔬 **研究方法**：识别三种资源生命周期管理模式及各自 DoS 利用路径，提出定向灰盒模糊测试框架 AgentDoS：分析资源生命周期后用 LLM 生成功能特定自然语言种子提示驱动过度消耗
- 📌 **结论**：在 20 个开源 agent 中发现 36 个零日漏洞（影响 16 个 agent，其中 15 个 GitHub star 超 1 万），已获 15 个 CVE 编号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents have recently attracted significant attention. By leveraging the semantic understanding capabilities of large language models (LLMs), these agents can autonomously perform complex tasks according to user requests, such as downloading files and summarizing content. However, the lack of comprehensive resource governance renders them susceptible to abuse, potentially leading to resource exhaustion and denial-of-service (DoS) conditions. In this work, we present the first systematic security study of resource management in LLM-based agents. We identify three representative patterns of resource lifecycle management, each of which enables distinct avenues for DoS exploitation. Building on these insights, we propose AgentDoS, a novel directed grey-box fuzzing framework designed to detect DoS vulnerabilities arising from resource exhaustion. AgentDoS first analyzes the resource lifecycle within the agent and then leverages an LLM to generate functionality-specific seed prompts in natural language that drive the agent toward excessive resource consumption. We evaluated AgentDoS on 20 widely used open-source LLM-based agents and discovered 36 zero-day vulnerabilities affecting 16 agents, 15 of which have over 10,000 stars on GitHub. To date, 15 CVE IDs have been assigned for these vulnerabilities.

</details>

### 3. Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.14493) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`benchmark`、`passive prompt injection`、`security log`、`defense-in-depth`、`prompt injection`

👤 **作者**：Rabimba Karanjai、Yang Lu、Hemanth Hegadehalli Madhavarao、Lei Xu、Weidong Shi

- 🎯 **研究动机**：SOC 用 LLM 分析外部日志，日志生成字段中的注入载荷可持久存储并在分析师查询时执行（passive prompt injection）
- 🔬 **研究方法**：提出 LogInject 框架与 12,847 条日志（2,569 对抗样本）基准，评估三个生产 LLM 在活动隐匿、误报生成、信息外泄与输出劫持四目标下的表现，并提出跨条目分片的 Context Stitching；测试输入过滤+提示加固+输出验证的分层缓解
- 📌 **结论**：基线 ASR 最高 88.2%（平均 83.4%），Context Stitching 达 76.4%；分层防御降低 90.4% 攻击但残留 8.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural language contexts to generate security insights. We demonstrate that this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term passive prompt injection. We present LogInject, a systematic framework for evaluating these threats. Using LogInject-1.0, a benchmark of 12,847 log entries including 2,569 adversarial samples, we evaluate three production LLMs across four attack objectives: activity concealment, false positive generation, information exfiltration, and output hijacking. Our findings reveal an up to 88.2% attack success rate (83.4% average across models) under the baseline conditions. We introduce Context Stitching, a novel technique that fragments payloads across multiple log entries to evade stateless filters while exploiting LLM long-context reasoning, achieving a 76.4% success rate. As mitigation, we evaluate layered defenses by combining input filtering, prompt hardening, and output validation, demonstrating a 90.4% attack reduction, although 8.4% residual vulnerability persists. Our results establish that LLM-based log analysis creates an inherent confused deputy vulnerability where untrusted data and trusted instructions compete indistinguishably for model attention, requiring defense in-depth architectures and continued human oversight for security-critical decisions.

</details>

### 4. "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild

📄 [arXiv](https://arxiv.org/abs/2602.06547) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`agent skill`、`supply chain`、`malicious ecosystem`、`skill marketplace`、`malware measurement`

👤 **作者**：Yi Liu、…、Leo Yu Zhang

- 🎯 **研究动机**：agent skill 注册表快速膨胀，但因缺少标注威胁数据其安全影响未被研究
- 🔬 **研究方法**：对两大注册表的 98,380 个 skill 结合静态模式匹配与动态行为验证做系统安全分析
- 📌 **结论**：确认 157 个恶意 skill、632 个漏洞、13 类攻击技术，单个平均含 4.03 个漏洞；超半数来自单一威胁行为者，上报后 100% 被下架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based coding agents increasingly rely on third-party extensions called skills, which bundle natural language instructions and helper scripts that execute with full user privileges. Community registries have emerged to distribute these skills, but the security implications remain unstudied due to the absence of labeled threat data. This paper presents a systematic security analysis of 98,380 skills collected from two major registries. Through a combination of static pattern matching and dynamic behavioral verification, we identify 157 skills exhibiting confirmed malicious behavior, encompassing 632 distinct vulnerabilities across 13 attack techniques. Our analysis reveals that these threats are deliberate rather than accidental: each malicious skill contains an average of 4.03 vulnerabilities spanning multiple attack phases. We identify two dominant attack strategies with statistically significant negative correlation -- credential theft via remote code execution, and agent manipulation through adversarial instructions embedded in documentation. Over half of all confirmed cases originate from a single threat actor employing templated brand impersonation at scale. We further observe that attack sophistication correlates with concealment investment, with advanced skills universally employing undocumented capabilities while also exploiting platform-native trust mechanisms. Following responsible disclosure, registry maintainers removed all 157 (100%) of the reported skills. Our dataset and detection pipeline are publicly available to facilitate future research on securing LLM agent ecosystems.

</details>

### 5. FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion

📄 [arXiv](https://arxiv.org/abs/2606.15609) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/rao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM agent`、`memory fragmentation`、`access control`、`tool-use agent`、`access-control bypass`

👤 **作者**：Zixin Rao、…、Zhen Xiang

- 🎯 **研究动机**：agent 访问控制只检查最终用户查询，长期记忆引入的时间信道使被禁内容可碎片化存入记忆再重组
- 🔬 **研究方法**：提出 FragFuse 三阶段：黑盒自适应查询+片段掩码识别会触发拒绝的片段、用标记载体查询注入记忆、后续攻击查询检索融合片段；并以代理优化自动生成攻击
- 📌 **结论**：四种 agent 设定、三种 SOTA 访问控制上平均绕过率 86.3%、端到端有害任务成功率 41.1%，任务退化仅 4.4%；prompt injection 与困惑度检测器均无法防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating requests and prevent misuse. We reveal a novel attack surface arising from agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing form, and later reconstructed through memory retrieval without appearing explicitly in the final user query. We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory. FragFuse operates in three stages: (1) identifying rejection-responsive fragments via black-box adaptive querying with fragment masking; (2) injecting these fragments into memory using marker carrier queries; and (3) retrieving and fusing the stored fragments through a follow-up attack query. Although FragFuse can be instantiated manually for individual agents, we further develop a surrogate-based optimization scheme that tunes fusion instructions and marker designs, enabling automated attack generation without violating the attacker's threat-model assumptions. We evaluate FragFuse across four representative agent settings and task domains, covering three state-of-the-art agent access-control mechanisms. FragFuse achieves an average bypass success rate of 86.3% and an average end-to-end harmful task success rate of 41.1% across all settings, with only 4.4% average task-success degradation compared with configurations without access control. We also show that alternative defenses, including state-of-the-art prompt-injection detectors and perplexity detectors, do not effectively address this attack.

</details>

### 6. MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning

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

### 7. Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening

📄 [arXiv](https://arxiv.org/abs/2605.28999) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-mohan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`attack`、`prompt injection`、`resume screening`、`real-world measurement`、`instruction hierarchy`

👤 **作者**：Mohan Zhang、…、Dawn Song

- 🎯 **研究动机**：prompt injection 漏洞多停留在概念演示，其在真实 LLM 应用中的流行度与影响未测
- 🔬 **研究方法**：基于 hireEZ 多年积累的约 20 万份真实简历，设计定制注入检测器（小规模人工验证高精度）并做大规模测量研究
- 📌 **结论**：约 1% 简历含隐藏注入，近一两年明显增多，超 90% 注入不使用显式指令——首次大规模实证真实 LLM 应用中的 prompt injection

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely unexplored. In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening. Our analysis is based on approximately 200K real-world resumes collected over multiple years by hireEZ. We first design tailored methods to detect prompt injection in resumes. Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors. We then apply our detector to the full resume dataset and conduct a comprehensive measurement study of real-world prompt injection attacks. Our analysis reveals several intriguing findings: approximately 1% of resumes contain hidden prompt injections; the prevalence of such injected resumes has increased noticeably over the past one to two years; and more than 90% of injected prompts do not use explicit instructions. These results provide the first evidence of large-scale prompt injection in real-world LLM-based applications and lay the groundwork for future studies to understand and mitigate such attacks.

</details>

### 8. MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks

📄 [arXiv](https://arxiv.org/abs/2602.09222) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/syros)　📅 2026　🏷 USENIX Security 2026

**关键词**：`tool`、`attack`、`web agent red-teaming`、`indirect prompt injection`、`adaptive attack`

👤 **作者**：Georgios Syros、…、Alina Oprea

- 🎯 **研究动机**：web agent 间接注入评估依赖固定模板与人工选取注入面，无法刻画真实自适应攻击
- 🔬 **研究方法**：MUZZLE 基于 agent 轨迹自动识别高显著性注入面，自适应生成针对机密性/完整性/可用性的恶意指令并按失败反馈迭代
- 📌 **结论**：在 4 个 web 应用上自动发现 44 个新攻击（10 个对抗目标），含 3 个跨应用注入与定制钓鱼场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) based web agents are increasingly deployed to automate complex online tasks by directly interacting with web sites and performing actions on users' behalf. While these agents offer powerful capabilities, their design exposes them to indirect prompt injection attacks embedded in untrusted web content, enabling adversaries to hijack agent behavior and violate user intent. Despite growing awareness of this threat, existing evaluations rely on fixed attack templates, manually selected injection surfaces, or narrowly scoped scenarios, limiting their ability to capture realistic, adaptive attacks encountered in practice. We present MUZZLE, an automated agentic framework for evaluating the security of web agents against indirect prompt injection attacks. MUZZLE utilizes the agent's trajectories to automatically identify high-salience injection surfaces, and adaptively generate context-aware malicious instructions that target violations of confidentiality, integrity, and availability. Unlike prior approaches, MUZZLE adapts its attack strategy based on the agent's observed execution trajectory and iteratively refines attacks using feedback from failed executions. We evaluate MUZZLE across diverse web applications, user tasks, and agent configurations, demonstrating its ability to automatically and adaptively assess the security of web agents with minimal human intervention. Our results show that MUZZLE effectively discovers 44 new attacks on 4 web applications with 10 adversarial objectives that violate confidentiality, availability, or privacy properties across different LLMs and agent scaffolds. MUZZLE also identifies novel attack strategies, including 3 cross-application prompt injection attacks and an agent-tailored phishing scenario.

</details>

### 9. Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems

📄 [arXiv](https://arxiv.org/abs/2601.07072) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`indirect prompt injection`、`retrieval optimization`、`data exfiltration`、`prompt injection`、`instruction hierarchy`

👤 **作者**：Hongyan Chang、Ergute Bao、Xinjian Luo、Ting Yu

- 🎯 **研究动机**：既往间接 prompt injection 研究回避最难点——保证恶意内容被自然查询实际检索，真实影响不明
- 🔬 **研究方法**：把恶意内容分解为保证检索的触发片段与承载任意攻击目标的攻击片段，仅需嵌入模型 API 访问即可黑盒构造紧凑触发片段
- 📌 **结论**：11 个基准 8 个嵌入模型上检索率近 100%，单查询成本低至 0.21 美元；单封毒邮件即可让 GPT-4o 在多 agent 工作流中以超 80% 成功率外传 SSH 密钥，现有防御无法阻止恶意文本被检索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly rely on retrieving information from external corpora. This creates a new attack surface: indirect prompt injection (IPI), where hidden instructions are planted in the corpora and hijack model behavior once retrieved. Previous studies have highlighted this risk but often avoid the hardest step: ensuring that malicious content is actually retrieved. In practice, unoptimized IPI is rarely retrieved under natural queries, which leaves its real-world impact unclear. We address this challenge by decomposing the malicious content into a trigger fragment that guarantees retrieval and an attack fragment that encodes arbitrary attack objectives. Based on this idea, we design an efficient and effective black-box attack algorithm that constructs a compact trigger fragment to guarantee retrieval for any attack fragment. Our attack requires only API access to embedding models, is cost-efficient (as little as $0.21 per target user query on OpenAI's embedding models), and achieves near-100% retrieval across 11 benchmarks and 8 embedding models (including both open-source models and proprietary services). Based on this attack, we present the first end-to-end IPI exploits under natural queries and realistic external corpora, spanning both RAG and agentic systems with diverse attack objectives. These results establish IPI as a practical and severe threat: when a user issued a natural query to summarize emails on frequently asked topics, a single poisoned email was sufficient to coerce GPT-4o into exfiltrating SSH keys with over 80% success in a multi-agent workflow. We further evaluate several defenses and find that they are insufficient to prevent the retrieval of malicious text, highlighting retrieval as a critical open vulnerability.

</details>

### 10. Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-tong)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`RAG code generation`、`CVE reachability`、`knowledge injection`、`tool-use agent`

👤 **作者**：Tong Sun、Jingyi Su、Yi Gao、Wei Dong

- 🎯 **研究动机**：嵌入式 IoT 的仓库级 RACG 会经良性公开 API 传递性触达 pinned 快照内漏洞例程而继承已知 CVE，现有 secure RACG 忽视版本特定暴露，CVE 扫描器又判不了 API 可达性
- 🔬 **研究方法**：提出 IoTRAGuarder：静态分析加证据门控 LLM 恢复 CVE 例程到公开 API 的反向调用链，构建版本感知安全知识库并做双层 API 对齐在线检索注入约束
- 📌 **结论**：在 44 个 Zephyr 任务、4 个 LLM 上将整体安全成功率从 5.11% 提升到 78.41%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Repository-grounded retrieval-augmented code generation (RACG) is increasingly used in embedded IoT development by retrieving code and documentation from a pinned RTOS/SDK repository (e.g., Zephyr OS). In this setting, security risks are often version-inherited: even without retrieval poisoning, generated applications may invoke benign-looking public APIs that transitively reach vulnerable internal routines in the pinned snapshot, thereby inheriting known CVEs. Existing secure RACG pipelines largely focus on task-level intent and generic vulnerability patterns, which can miss repository- and version-specific exposure. Meanwhile, conventional CVE scanners can flag vulnerable locations but cannot determine whether those vulnerabilities are reachable through the public APIs that the generator commits to during repository-grounded generation. In this paper, we present IoTRAGuarder, a contextual knowledge injection framework that aligns security hardening with generation-time API selection under repository grounding. IoTRAGuarder (i) recovers auditable reverse call chains from CVE-localized internals to exposing public APIs via static analysis plus an evidence-gated LLM to bridge indirections and macro-driven "call-graph islands", (ii) constructs a version-aware security knowledge base that binds affected version intervals to exposed public APIs with prompt-ready constraints, safer alternatives, or avoidance/upgrade guidance, and (iii) performs dual-layer, API-aligned online retrieval to inject concise, version-matched constraints into the final prompt. We evaluate IoTRAGuarder on 44 real-world Zephyr tasks across four LLMs. Compared to the prior state-of-the-art secure RACG baseline, IoTRAGuarder improves the overall security success rate from 5.11% to 78.41%.

</details>

### 11. When AIOps Become "AI Oops": Subverting LLM-driven IT Operations via Telemetry Manipulation

📄 [arXiv](https://arxiv.org/abs/2508.06394) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/pasquini)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM AIOps`、`telemetry poisoning`、`reward hacking`、`specification gaming`

👤 **作者**：Dario Pasquini、Evgenios M. Kornaropoulos、Giuseppe Ateniese、Omer Akgul、Athanasios Theocharis、Petros Efstathopoulos

- 🎯 **研究动机**：LLM 驱动的 AIOps 自动化的安全代价未被分析
- 🔬 **研究方法**：提出 AIOpsDoom 全自动攻击：侦察、模糊测试加 LLM 对抗输入生成，注入错误诱导遥测数据经对抗性 reward hacking 误导 agent；并提出利用遥测结构化特性的 AIOpsShield 净化防御
- 📌 **结论**：可可靠诱导 AIOps agent 采取损害基础设施的动作，AIOpsShield 有效拦截且不影响正常性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI for IT Operations (AIOps) is transforming how organizations manage complex software systems by automating anomaly detection, incident diagnosis, and remediation. Modern AIOps solutions increasingly rely on autonomous LLM-based agents to interpret telemetry data and take corrective actions with minimal human intervention, promising faster response times and operational cost savings. In this work, we perform the first security analysis of AIOps solutions, showing that, once again, AI-driven automation comes with a profound security cost. We demonstrate that adversaries can manipulate system telemetry to mislead AIOps agents into taking actions that compromise the integrity of the infrastructure they manage. We introduce techniques to reliably inject telemetry data using error-inducing requests that influence agent behavior through a form of adversarial reward-hacking; plausible but incorrect system error interpretations that steer the agent's decision-making. Our attack methodology, AIOpsDoom, is fully automated--combining reconnaissance, fuzzing, and LLM-driven adversarial input generation--and operates without any prior knowledge of the target system. To counter this threat, we propose AIOpsShield, a defense mechanism that sanitizes telemetry data by exploiting its structured nature and the minimal role of user-generated content. Our experiments show that AIOpsShield reliably blocks telemetry-based attacks without affecting normal agent performance. Ultimately, this work exposes AIOps as an emerging attack vector for system compromise and underscores the urgent need for security-aware AIOps design.

</details>
### 越狱、安全对齐与内容防护

### 12. Bypassing Prompt Guards in Production with Controlled-Release Prompting

📄 [arXiv](https://arxiv.org/abs/2510.01529) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/fairoze)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`defense`、`prompt guard`、`controlled-release prompting`、`copyright extraction`、`jailbreak defense`

👤 **作者**：Jaiden Fairoze、Sanjam Garg、Keewoo Lee、Mingyuan Wang

- 🎯 **研究动机**：prompt 过滤的理论不可能性结果是否转化为真实系统漏洞未被验证
- 🔬 **研究方法**：提出 controlled-release prompting：利用轻量过滤器与被保护模型的资源不对称，生成有界过滤器不可解但对目标 LLM 可解的恶意 prompt
- 📌 **结论**：在 Gemini、DeepSeek、Grok、Mistral 四大平台攻击成功并从 Gemini 提取版权数据；14 个开源护栏模型中连推理型过滤器也难以可靠检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ball et al. recently established that prompt filtering for AI alignment faces a fundamental barrier: under standard cryptographic assumptions, no filter running significantly faster than the protected model can universally distinguish adversarial prompts from benign ones. We investigate whether this impossibility result translates to real-world vulnerabilities in deployed large language model (LLM) systems. We answer affirmatively by introducing controlled-release prompting, a practical instantiation of the theoretical framework that exploits the resource asymmetry between lightweight input filters and the main models they protect. Unlike the theoretical construction, our attack does not require model modification: it generates malicious prompts that are indecipherable by any bounded filter yet remain tractable to the target LLM. We find our attack to be successful on four major chat platforms (Google Gemini, DeepSeek Chat, xAI Grok, and Mistral Le Chat) where baseline methods fail. Additionally, we apply our attack to extract copyrighted data from Gemini. Finally, we provide a systematic evaluation of 14 open-weight prompt guard models, revealing that even reasoning-capable filters cannot reliably detect our attack without incurring prohibitive resource overhead.

</details>

### 13. Defending Jailbreak Attacks on Large Language Models via Manifold Trajectory Kinetics

📄 [arXiv](https://arxiv.org/abs/2606.07335) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-hangtao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`defense`、`LLM jailbreak`、`manifold trajectory`、`adaptive attack`、`jailbreak`

👤 **作者**：Hangtao Zhang、…、Leo Yu Zhang

- 🎯 **研究动机**：基于固定度量空间的越狱检测在伪恶意提示（含安全关键词的良性意图）与自适应攻击下线性可分假设失效
- 🔬 **研究方法**：提出 MTK，把 LLM 视为动力系统，追踪提示邻域结构跨层演化：良性提示始终贴近良性邻域，越狱提示先近恶意种子后策略性转向良性邻域
- 📌 **结论**：四个 LLM、十种攻击上：伪恶意提示 TPR 95%（良性 FPR 5%、伪恶意 FPR 2%），自适应攻击下仍保持 85% TPR，并扩展到 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak prompts can bypass alignment guardrails in large language models (LLMs) and elicit unsafe outputs, making reliable deployment-time detection critical. Prior detection approaches largely rely on a fixed metric space, e.g., raw inputs, gradients, or hidden features, in which benign and jailbreak prompts are linearly separable. We show this assumption breaks under (i) pseudo-malicious prompts that are benign by intent but contain safety-related keywords, and (ii) adaptive attacks that explicitly optimize against the deployed detector. To overcome this limitation, we shift our focus from identifying a universal metric space to analyzing the more robust neighborhood structure of the underlying data manifold. We present Manifold Trajectory Kinetics (MTK), which treats an LLM as a kinetic system transforming inputs into outputs and detects jailbreaks by tracking how a prompt's neighborhood structure evolves across layers. Benign prompts remain close to benign neighborhoods throughout inference, whereas jailbreak prompts exhibit a characteristic trajectory that begins near malicious seeds and later strategically shifts toward benign neighborhoods to evade refusal.Across four LLMs and ten jailbreak attacks, MTK achieves strong robustness to both failure modes: on pseudo-malicious prompts, it attains a jailbreak true positive rate of 95% at a false positive rate of 5% on benign prompts and 2% on pseudo-malicious prompts, and under adaptive attacks, it maintains a true positive rate of 85%. We further demonstrate the superior performance of MTK for jailbreak detection in vision-language models. Our code is available at https://github.com/Rookie143/mtk.

</details>

### 14. DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern

📄 [arXiv](https://arxiv.org/abs/2603.01574) · 🌐 [Project](https://zenodo.org/records/18479273) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/pang-xiaoyi)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`targeted attack`、`entropy lull`、`black-box LLM`、`black-box`、`entropy`

👤 **作者**：Xiaoyi Pang、Xuanyi Hao、Pengyu Liu、Qi Luo、Song Guo、Zhibo Wang

- 🎯 **研究动机**：后门与注入等定向攻击的防御需高访问权限或高成本，不适合真实 API 场景
- 🔬 **研究方法**：发现 Entropy Lull 模式：攻击劫持生成时 token 概率熵异常低且稳定；DualSentinel 先做幅值趋势监测，再用任务翻转做二次验证确认强制控制
- 📌 **结论**：检测准确率更优、近零误报且额外开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to generate specific malicious sequences. Existing defensive approaches for such threats typically rely on high access rights, impose prohibitive costs, and hinder normal inference, rendering them impractical for real-world scenarios. To solve these limitations, we introduce DualSentinel, a lightweight and unified defense framework that can accurately and promptly detect the activation of targeted attacks alongside the LLM generation process. We first identify a characteristic of compromised LLMs, termed Entropy Lull: when a targeted attack successfully hijacks the generation process, the LLM exhibits a distinct period of abnormally low and stable token probability entropy, indicating it is following a fixed path rather than making creative choices. DualSentinel leverages this pattern by developing an innovative dual-check approach. It first employs a magnitude and trend-aware monitoring method to proactively and sensitively flag an entropy lull pattern at runtime. Upon such flagging, it triggers a lightweight yet powerful secondary verification based on task-flipping. An attack is confirmed only if the entropy lull pattern persists across both the original and the flipped task, proving that the LLM's output is coercively controlled. Extensive evaluations show that DualSentinel is both highly effective (superior detection accuracy with near-zero false positives) and remarkably efficient (negligible additional cost), offering a truly practical path toward securing deployed LLMs. The source code can be accessed at https://doi.org/10.5281/zenodo.18479273.

</details>

### 15. GateBreaker: Gate-Guided Attacks on Mixture-of-Expert LLMs

📄 [arXiv](https://arxiv.org/abs/2512.21008) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wu-lichao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`MoE LLM`、`safety alignment`、`expert routing`、`VLM safety`、`multimodal jailbreak`

👤 **作者**：Lichao Wu、Sasha Behrouzi、Mohamadreza Rostami、Stjepan Picek、Ahmad-Reza Sadeghi

- 🎯 **研究动机**：LLM 安全研究几乎只关注稠密架构，MoE 稀疏路由下安全机制的鲁棒性未被检验
- 🔬 **研究方法**：GateBreaker 免训练三阶段推理时攻击：门控级画像定位有害输入下被集中路由的安全专家、专家级定位其内安全结构、定向禁用该结构
- 📌 **结论**：MoE 安全集中于稀疏路由协调的小撮神经元；禁用目标层约 3% 神经元即使八个对齐 MoE LLM 平均 ASR 从 7.4% 升至 64.9%，同族一次迁移使 17.9%→67.7%，并泛化到五个 MoE VLM（60.9%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) architectures have advanced the scaling of Large Language Models (LLMs) by activating only a sparse subset of parameters per input, enabling state-of-the-art performance with reduced computational cost. As these models are increasingly deployed in critical domains, understanding and strengthening their alignment mechanisms is essential to prevent harmful outputs. However, existing LLM safety research has focused almost exclusively on dense architectures, leaving the unique safety properties of MoEs largely unexamined. The modular, sparsely-activated design of MoEs suggests that safety mechanisms may operate differently than in dense models, raising questions about their robustness. In this paper, we present GateBreaker, the first training-free, lightweight, and architecture-agnostic attack framework that compromises the safety alignment of modern MoE LLMs at inference time. GateBreaker operates in three stages: (i) gate-level profiling, which identifies safety experts disproportionately routed on harmful inputs, (ii) expert-level localization, which localizes the safety structure within safety experts, and (iii) targeted safety removal, which disables the identified safety structure to compromise the safety alignment. Our study shows that MoE safety concentrates within a small subset of neurons coordinated by sparse routing. Selective disabling of these neurons, approximately 3% of neurons in the targeted expert layers, significantly increases the averaged attack success rate (ASR) from 7.4% to 64.9% against the eight latest aligned MoE LLMs with limited utility degradation. These safety neurons transfer across models within the same family, raising ASR from 17.9% to 67.7% with one-shot transfer attack. Furthermore, GateBreaker generalizes to five MoE vision language models (VLMs) with 60.9% ASR on unsafe image inputs.

</details>

### 16. JailbreakScope: Interpreting Jailbreak Mechanism through Representation and Circuit Analyses

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/he-zeqing)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`attack`、`LLM jailbreak`、`representation analysis`、`circuit analysis`

👤 **作者**：Zeqing He、…、Rui Zheng

- 🎯 **研究动机**：越狱底层机制不明：现有研究只看静态表示偏移或安全组件，未从电路失效到表示变化给出细粒度解释
- 🔬 **研究方法**：JailbreakScope 从表示（扭曲有害感知）与电路（影响安全生成电路）双视角追踪整个生成过程，覆盖 5 个主流 LLM 与 7 种越狱策略
- 📌 **结论**：越狱普遍放大强化肯定响应的组件、抑制拒答组件，把表示推向安全区；表示欺骗与电路激活偏移跨越狱与模型强相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) exhibit impressive performance but remain vulnerable to jailbreak attacks, where adversarial prompts are crafted to bypass safety alignments and elicit unexpected responses. Despite their prevalence, the underlying mechanisms that enable jailbreaks are still not well understood. Recent studies primarily focus on static representation shifts or on identifying components associated with generation safety. However, these studies neither explore diverse jailbreak patterns nor provide a fine-grained explanation from the failure of circuit to representation changes, leaving significant gaps in uncovering jailbreak mechanism. In this paper, we propose JailbreakScope, an interpretation framework that analyzes jailbreak mechanisms from both representation (how jailbreaks distort LLM's harmfulness perception) and circuit (how jailbreaks impact circuits that are important for generation safety) perspectives, tracking their evolution throughout the entire generation process. We conduct in-depth evaluations on 5 mainstream LLMs under 7 jailbreak strategies. Our evaluation reveals a general pattern that jailbreaks amplify components that reinforce affirmative responses while suppressing those producing refusal, which shifts representations towards safe regions, leading LLMs to provide responses instead of refusals. Moreover, we find a strong and consistent correlation between representation deception and circuit activation shift across diverse jailbreaks and multiple LLMs.

</details>

### 17. One Bad Token Spoils the Barrel: Assessment, Detection, and Remediation of Glitch Tokens in Large Language Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-kunsheng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`detection`、`glitch token`、`unsafe generation`、`token remediation`、`jailbreak defense`

👤 **作者**：Kunsheng Tang、…、Jie Zhang

- 🎯 **研究动机**：glitch token 引发不可预测错误行为，缺安全评估、检测覆盖有限且无修复手段
- 🔬 **研究方法**：展示其可绕过安全机制且跨模型、分词器与商业审核系统迁移；GlitchQuiz 红队框架检测；GlitchEdit 免训练嵌入层编辑修复
- 📌 **结论**：不安全率平均从 96.36% 降至 2.87% 且保持整体性能；已向 OpenAI、Anthropic 等九家提供商负责任披露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have shown remarkable capabilities across numerous applications. However, the recent emergence of "glitch tokens," referring to tokens that cause unpredictable and erroneous model behaviors, poses significant reliability and security challenges. Despite prior investigations of glitch tokens, critical gaps remain, including insufficient safety assessments, limited detection coverage, and the absence of effective remediation strategies. To address these challenges, we first demonstrate that glitch tokens can readily bypass safety mechanisms and elicit unsafe outputs across LLMs through straightforward exploitation methods. More critically, we reveal that these tokens exhibit cross-model transferability, inducing safety risks across model families, tokenizers, commercial and moderation systems, underscoring their pervasive security implications. We then propose GlitchQuiz, a red-teaming framework inspired by human language acquisition, to comprehensively detect glitch tokens, surpassing existing detection methods. Finally, we develop GlitchEdit, a training-free embedding-layer editing approach that effectively remediates glitch tokens, reducing unsafe behaviors with average unsafe rates decreasing from 96.36% to 2.87% across evaluated LLMs and maintaining overall performance. Our findings have been responsibly disclosed to nine affected leading LLM providers, including OpenAI, Anthropic, and others, to help foster safer AI ecosystems.

</details>

### 18. Quantifying Large Language Model Attacks Through the Lens of Model Cognition

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-xiuming)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`attack`、`LLM attack`、`model cognition`、`lightweight monitor`、`jailbreak defense`

👤 **作者**：Xiuming Liu、…、Shuo Wang

- 🎯 **研究动机**：关键词过滤与输出审核等安全机制忽视模型内部动态
- 🔬 **研究方法**：中间隐藏态轻量探针在生成前分离有害提示特征（最高 99% 准确率）；层级毒性探针加多层互补检测融合不同深度信号，Sentinel 不到 5M 参数
- 📌 **结论**：假阴性比生成级拒答减半，对抗攻击下保持 94% 以上检测准确率（基线掉 32%），并在七个开源 LLM 上超 Llama-Guard-3-8B

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to malicious inputs that elicit harmful content. Current safety mechanisms, such as keyword filters or output moderation, largely ignore internal model dynamics. We show that safety-relevant features correlated with harmful prompting are strongly separable under lightweight probes in intermediate hidden states (up to 99% accuracy) before generation, revealing that such features persist internally even when models produce compliant outputs. Leveraging this observation, we introduce layer-wise toxicity probes and a multi-layer complementary detection framework that fuses signals from diverse depths. Our lightweight Sentinel (<5M parameters) halves false negatives compared to generation-level refusal and maintains over 94% detection accuracy under adversarial attacks—where baselines drop by 32%. Sentinel also outperforms Llama-Guard-3-8B on heterogeneous harmful prompting across seven open-weight LLMs (1.5B→72B) and multiple benchmarks (I2P, SneakyPrompt, MMA, Labelled, PIJ, ChatAlpaca, and Multi-turn Jailbreak). Beyond detection, our method provides the first quantitative, layer-resolved map of how safety-relevant signals emerge, propagate, and degrade within LLMs, enabling interpretable, inside-out alignment and diagnostics. This paper contains potentially sensitive and offensive content, including but not limited to NSFW material, hate speech, discrimination, and other harmful text. Reader discretion is advised.

</details>

### 19. SafeAdapt: Safety Alignment with Adaptive Thinking Allocation for Large Reasoning Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/song-jiazheng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`safety alignment`、`adaptive thinking`、`reasoning budget`

👤 **作者**：Jiazheng Song、Junxu Liu、Jian Lou、Jinfei Liu

- 🎯 **研究动机**：安全推理预算越长越安全的普遍假设未经系统检验，固定预算在简单攻击上过度思考、困难攻击上思考不足
- 🔬 **研究方法**：系统评估安全预算与生成安全性的关系，并提出 SafeAdapt：按提示难度动态调整安全思考预算
- 📌 **结论**：安全并不随思考轨迹变长单调提升，SafeAdapt 在多样困难攻击下以更合理的预算显著提升安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning models have garnered growing importance as their strong Chain-of-Thought (CoT) capabilities unleash exceptional performance on complex tasks. Consequently, an emerging research direction explores "safety thinking" which leverages reasoning models' reasoning capabilities to assess the safety of input prompts and prevent harmful content generation. A prevailing yet under-examined belief in existing studies is that allocating more computational resources to the safety reasoning budget, i.e., rolling out longer safety thinking trajectories, necessarily yields safer behavior. However, this premise has not been systematically analyzed, despite the widespread adoption of reasoning models. In this paper, we aim to fill this gap by conducting a rigorous safety evaluation to examine the relationship between the safety reasoning budget and the safety of reasoning model generations, particularly under adversarial conditions. Our analysis reveals that safety does not monotonically improve with longer thinking trajectories: both over-thinking on simple attacks and under-thinking on difficult attacks incur excess safety risks, leading to systematic failures under fixed-budget safety policies. Motivated by these key findings, we propose SafeAdapt: Safety Alignment with adaptive thinking Allocation, a novel approach that learns to dynamically adjust reasoning models' safety thinking budget based on prompt difficulty. This enables reasoning models to allocate computational resources adaptively, rather than following a single fixed thinking pattern (e.g., the longer the safer), thereby mitigating excess risks incurred by under-/over-thinking. Experiments across multiple adversarial benchmarks demonstrate that SafeAdapt significantly improves safety performance with a more ideal thinking budget under diverse and challenging attack settings.

</details>

### 20. The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections

📄 [arXiv](https://arxiv.org/abs/2510.09023) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nasr)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`defense`、`adaptive attack`、`jailbreak defense`、`prompt injection defense`

👤 **作者**：Milad Nasr、…、Florian Tramèr

- 🎯 **研究动机**：越狱与 prompt injection 防御大多只对静态攻击集或弱优化方法评测，无法反映自适应攻击者的真实威胁
- 🔬 **研究方法**：系统调优并扩展梯度下降、强化学习、随机搜索与人工引导探索等通用优化技术，对 12 个近期防御发起自适应攻击
- 📌 **结论**：多数防御被以 90% 以上 ASR 绕过，而其原报告多为近零攻击成功率，现有鲁棒性声明不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How should we evaluate the robustness of language model defenses? Current defenses against jailbreaks and prompt injections (which aim to prevent an attacker from eliciting harmful knowledge or remotely triggering malicious actions, respectively) are typically evaluated either against a static set of harmful attack strings, or against computationally weak optimization methods that were not designed with the defense in mind. We argue that this evaluation process is flawed. Instead, we should evaluate defenses against adaptive attackers who explicitly modify their attack strategy to counter a defense's design while spending considerable resources to optimize their objective. By systematically tuning and scaling general optimization techniques-gradient descent, reinforcement learning, random search, and human-guided exploration-we bypass 12 recent defenses (based on a diverse set of techniques) with attack success rate above 90% for most; importantly, the majority of defenses originally reported near-zero attack success rates. We believe that future defense work must consider stronger attacks, such as the ones we describe, in order to make reliable and convincing claims of robustness.

</details>

### 21. VSG-Safe: Spotting NSFW Video through Cross-Frame Evidence

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yuyang)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`NSFW video`、`scene graph`、`cross-frame reasoning`、`multimodal guardrail`

👤 **作者**：Yuyang Zhang、…、Lina Wang

- 🎯 **研究动机**：现有审核把视频当作独立帧或原始帧序列，无法跨帧推理，跨帧语义（如违法活动、威胁）检测频繁失败
- 🔬 **研究方法**：提出 VSG-Safe：抽取跨帧内容构建 scene graph，图导向模型联合捕获实体、属性与实体间关系以检测 NSFW 内容
- 📌 **结论**：平均 F1 达 97.62%，较七个基线平均高 42.32%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in text-to-video (T2V) models enable high-fidelity videos that closely follow textual prompts. However, this expands practical applications while amplifying serious security and societal concerns from the automated synthesis of visual content that may be inappropriate in certain usage contexts, such as public or workplace settings, including sexual or violent content (e.g., the Grok can generate sexual videos in the "Spicy" mode). We observe that such visual content is often distributed across frames, embedded in visual entities, their attributes, and inter-entity relations. In contrast, existing moderation pipelines primarily treat video content as either individual frames or raw frame sequences, overlooking the fact that critical semantics can manifest through the combination of specific frames. This gap prevents them from reasoning across frames, confining detection to low-level visual cues, such as gore or explicit conflict, and causing frequent failures when cross-frame inference is required, including illegal activities or threats. To address these limitations, we propose leveraging scene graphs as the core intermediate semantic representation. Scene graphs naturally encode entities, their attributes, and inter-entity relationships, while also supporting reasoning over cross-frame content. Grounded on this insight, we further propose VSG-Safe, a novel scene-graph-driven framework for T2V content moderation. Concretely, our approach first extracts cross-frame content from videos to build scene graphs. With these graphs, we leverage a graph-oriented model to jointly capture entities, attributes, and inter-entity relations, enabling effective detection. To evaluate its effectiveness, we conduct extensive experiments on both SOTA benchmarks and our self-constructed video datasets. VSGSafe attains an average F1-score of 97.62%, outperforming seven baselines by 42.32% on average.

</details>

### 22. When Memory Becomes a Vulnerability: Towards Multi-turn Jailbreak Attacks against Text-to-Image Generation Systems

📄 [arXiv](https://arxiv.org/abs/2504.20376) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-shiqian)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`text-to-image jailbreak`、`multi-turn memory`、`safety filter`、`multi-turn T2I jailbreak`、`memory mechanism`

👤 **作者**：Shiqian Zhao、…、Luu Anh Tuan

- 🎯 **研究动机**：T2I 系统记忆机制的安全分析滞后，单条对抗 prompt 易被检测或去毒失败
- 🔬 **研究方法**：提出 Inception，以 Segmentation 按句法分解恶意 prompt、Recursion 递归处理难分子句，把恶意意图埋入会话记忆，并构建含两段安全过滤的仿真系统 VisionFlow
- 📌 **结论**：攻击成功率超 SoTA 20.0%，并在真实商用 T2I 平台验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern text-to-image (T2I) generation systems (e.g., DALL$\cdot$E 3) exploit the memory mechanism, which captures key information in multi-turn interactions for faithful generation. Despite its practicality, the security analyses of this mechanism have fallen far behind. In this paper, we reveal that it can exacerbate the risk of jailbreak attacks. Previous attacks fuse the unsafe target prompt into one ultimate adversarial prompt, which can be easily detected or lead to the generation of non-unsafe images due to under- or over-detoxification. In contrast, we propose embedding the malice at the inception of the chat session in memory, addressing the above limitations. Specifically, we propose Inception, the first multi-turn jailbreak attack against real-world text-to-image generation systems that explicitly exploits their memory mechanisms. Inception is composed of two key modules: segmentation and recursion. We introduce Segmentation, a semantic-preserving method that generates multi-round prompts. By leveraging NLP analysis techniques, we design policies to decompose a prompt, together with its malicious intent, according to sentence structure, thereby evading safety filters. Recursion further addresses the challenge posed by unsafe sub-prompts that cannot be separated through simple segmentation. It firstly expands the sub-prompt, then invokes segmentation recursively. To facilitate multi-turn adversarial prompts crafting, we build VisionFlow, an emulation T2I system that integrates two-stage safety filters and industrial-grade memory mechanisms. The experiment results show that Inception successfully allures unsafe image generation, surpassing the SOTA by a 20.0\% margin in attack success rate. We also conduct experiments on the real-world commercial T2I generation platforms, further validating the threats of Inception in practice.

</details>
### 投毒、后门与模型供应链

### 23. Attacks on Approximate Caches in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2508.20424) · 🌐 [Project](https://zenodo.org/records/18705055) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-desen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`diffusion serving cache`、`prompt stealing`、`cache poisoning`、`data poisoning`

👤 **作者**：Desen Sun、Shuncheng Jie、Sihang Liu

- 🎯 **研究动机**：扩散服务采用近似缓存复用相似 prompt 的中间状态，打破了用户间隔离
- 🔬 **研究方法**：演示三类远程攻击：以特殊关键词建立可维持数日的隐蔽信道、从缓存命中窃取 prompt、向被窃 prompt 投毒嵌入攻击者 logo
- 📌 **结论**：三类攻击均可经服务系统远程实施，暴露近似缓存的严重安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models are a powerful class of generative models that produce images and other content from user prompts, but they are computationally intensive. To mitigate this cost, recent academic and industry work has adopted approximate caching, which reuses intermediate states from similar prompts in a cache. While efficient, this optimization introduces new security risks by breaking isolation among users. This paper provides a comprehensive assessment of the security vulnerabilities introduced by approximate caching. First, we demonstrate a remote covert channel established with the approximate cache, where a sender injects prompts with special keywords into the cache system and a receiver can recover that even after days, to exchange information. Second, we introduce a prompt stealing attack using the approximate cache, where an attacker can recover existing cached prompts from hits. Finally, we introduce a poisoning attack that embeds the attacker's logos into the previously stolen prompt, leading to unexpected logo rendering for the requests that hit the poisoned cache prompts. These attacks are all performed remotely through the serving system, demonstrating severe security vulnerabilities in approximate caching. The code for this work is available.

</details>

### 24. BadGraph: Structural Knowledge Isolation Attacks against Graph Retrieval-Augmented Generation

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-leiming)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`GraphRAG`、`topology poisoning`、`availability`、`RAG poisoning`、`knowledge corruption`

👤 **作者**：Leiming Yan、Xinlong Xu、Ziqiang Li

- 🎯 **研究动机**：GraphRAG 的图结构暴露拓扑攻击面，现有攻击依赖显式假答案或毒化关系，易被内容审计标记
- 🔬 **研究方法**：BadGraph 结构性知识隔离攻击：数学分析图算法的三种拓扑漏洞，注入少量语义中性文本生成对抗子图，降低目标证据在检索上下文中的可见性
- 📌 **结论**：HotpotQA 注入 49 篇、2WikiMultiHopQA 30 篇文档，即持续降低 MS-GraphRAG、LightRAG、FastGraphRAG 的源召回与端到端 QA F1

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph Retrieval-Augmented Generation (GraphRAG) improves cross-document reasoning by introducing graph structures into retrieval. However, these graph structures also expose an under-studied topological attack surface. Existing research on GraphRAG attacks primarily focuses on targeted attacks based on text or relation manipulation, which induce the model to generate specific incorrect answers by injecting factual errors. These attacks often rely on explicit false-answer payloads, poisoned relations, or corpus rewriting, and their documents can be easier to flag during content auditing. In this paper, we propose a targeted availability attack against GraphRAG: Structural Knowledge Isolation. Unlike traditional wrong-answer manipulation attacks, this attack targets the system's availability by degrading retrieval of critical evidence through topological manipulation. The resulting context can lack the evidence needed for grounded answer generation. We first mathematically analyze three topological vulnerabilities of graph algorithms used in GraphRAG systems when subjected to topological perturbations. Based on this analysis, we propose the BadGraph attack framework. By injecting a small amount of semantically neutral text, it generates adversarial subgraphs in the knowledge graph and reduces the visibility of target evidence in top-ranked retrieval contexts. Experiments show that with a small document injection budget (49 documents on HotpotQA and 30 on 2WikiMultiHopQA), BadGraph consistently lowers source recall and end-to-end QA F1 on three mainstream GraphRAG systems (MS-GraphRAG, LightRAG, and FastGraphRAG), while using neutral linker documents.

</details>

### 25. Confundo: Learning to Generate Robust Poison for Practical RAG Systems

📄 [arXiv](https://arxiv.org/abs/2602.06616) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/hu-haoyang)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`RAG poisoning`、`preprocessing robustness`、`query variation`、`robust poison`、`hallucination induction`

👤 **作者**：Haoyang Hu、Zhejun Jiang、Yueming Lyu、Junyuan Zhang、Yi Liu、Ka-Ho Chow

- 🎯 **研究动机**：现有 RAG 投毒在真实系统中因预处理碎片化与查询偏移而严重失效，导致风险被低估
- 🔬 **研究方法**：Confundo 微调 LLM 作为投毒生成器，统一支持操纵事实正确性、诱导偏见、触发幻觉等多种攻击目标
- 📌 **结论**：跨数据集与 RAG 配置大幅超越专用攻击，防御存在时仍有效；另给出防网页被爬入 RAG 的防御用例

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is increasingly deployed in real-world applications, where its reference-grounded design makes outputs appear trustworthy. This trust has spurred research on poisoning attacks that craft malicious content, inject it into knowledge sources, and manipulate RAG responses. However, when evaluated in practical RAG systems, existing attacks suffer from severely degraded effectiveness. This gap stems from two overlooked realities: (i) content is often processed before use, which can fragment the poison and weaken its effect, and (ii) users often do not issue the exact queries anticipated during attack design. These factors can lead practitioners to underestimate risks and develop a false sense of security. To better characterize the threat to practical systems, we present Confundo, a learning-to-poison framework that fine-tunes a large language model as a poison generator to achieve high effectiveness, robustness, and stealthiness. Confundo provides a unified framework supporting multiple attack objectives, demonstrated by manipulating factual correctness, inducing biased opinions, and triggering hallucinations. By addressing these overlooked challenges, Confundo consistently outperforms a wide range of purpose-built attacks across datasets and RAG configurations by large margins, even in the presence of defenses. Beyond exposing vulnerabilities, we also present a defensive use case that protects web content from unauthorized incorporation into RAG systems via scraping, with no impact on user experience.

</details>

### 26. Cordyceps: Covert Control Attacks on LLMs via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.26595) · 🌐 [Project](https://anonymous.4open.science/r/cordyceps-F147) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shao-zedian)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM data poisoning`、`covert control`、`backdoor`、`steganographic backdoor`、`stealthy backdoor`

👤 **作者**：Zedian Shao、Charles Fleming、Teodora Baluta

- 🎯 **研究动机**：固定触发短语可被离群检测、干净数据正则或在线监控中和
- 🔬 **研究方法**：Cordyceps 通过共享知识（事实、概念）与攻击者短语的语义关联教会 LLM 一套信息隐藏方案，可编码解码任意恶意指令
- 📌 **结论**：小投毒率下平均 ASR 较启发式 prompt injection 高约 40%；后门防御后仍保持最高 93%、prompt injection 防御后最高 98%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often fine-tuned on uncurated text datasets that adversaries can poison. Existing poisoning attacks primarily rely on fixed trigger phrases that defenses such as outlier detection, clean-data regularization, or online monitoring can neutralize. In this paper, we propose a data poisoning method that teaches an LLM an information hiding scheme reliably and stealthily through semantic associations between shared knowledge such as facts or concepts and attacker-chosen phrases. The induced hiding scheme can encode and decode arbitrary malicious instructions, thus revealing a new and subtle poisoning-induced vulnerability: covert control attacks. We precisely characterize covert control attacks and evaluate them across $5$ LLMs, $3$ backdoor defenses, and $4$ prompt injection defenses. With a small poisoned fraction, covert control attacks outperform heuristic-based prompt injection attacks in average attack success rate by about $40\%$ relative to clean fine-tuned models. They also circumvent defenses based on detection and fine-tuning, maintaining up to $93\%$ attack success rate after backdoor defenses and up to $98\%$ after prompt injection defenses.

</details>

### 27. HAMLOCK: HArdware-Model LOgically Combined attacK

📄 [arXiv](https://arxiv.org/abs/2510.19145) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/amgain)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`DNN accelerator`、`hardware Trojan`、`cross-layer backdoor`

👤 **作者**：Sanskar Amgain、Daniel Lobo、Atri Chatterjee、Swarup Bhunia、Fnu Suya

- 🎯 **研究动机**：纯模型级后门的完整激活路径可被逐层追踪，易被检测
- 🔬 **研究方法**：HAMLOCK 把攻击逻辑分布到硬件-软件边界：模型仅微调少数神经元在触发时产生独特高激活，硬件 Trojan 监测相应比特后直接篡改输出 logits
- 📌 **结论**：多基准近乎完美 ASR 且 clean 精度几乎无损，无需自适应即绕过 SOTA 模型级防御，硬件面积与功耗开销低至 0.01%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing use of third-party hardware accelerators (e.g., FPGAs, ASICs) for deep neural networks (DNNs) introduces new security vulnerabilities. Conventional model-level backdoor attacks, which only poison a model's weights to misclassify inputs with a specific trigger, are often detectable because the entire attack logic is embedded within the model (i.e., software), creating a traceable layer-by-layer activation path. This paper introduces the HArdware-Model Logically Combined Attack (HAMLOCK), a far stealthier threat that distributes the attack logic across the hardware-software boundary. The software (model) is now only minimally altered by tuning the activations of few neurons to produce uniquely high activation values when a trigger is present. A malicious hardware Trojan detects those unique activations by monitoring the corresponding neurons' most significant bit or the 8-bit exponents and triggers another hardware Trojan to directly manipulate the final output logits for misclassification. This decoupled design is highly stealthy, as the model itself contains no complete backdoor activation path as in conventional attacks and hence, appears fully benign. Empirically, across benchmarks like MNIST, CIFAR10, GTSRB, and ImageNet, HAMLOCK achieves a near-perfect attack success rate with a negligible clean accuracy drop. More importantly, HAMLOCK circumvents the state-of-the-art model-level defenses without any adaptive optimization. The hardware Trojan is also undetectable, incurring area and power overheads as low as 0.01%, which is easily masked by process and environmental noise. Our findings expose a critical vulnerability at the hardware-software interface, demanding new cross-layer defenses against this emerging threat.

</details>

### 28. HijackKV: New Threat in Position-Independent KV Cache Reuse

📄 [arXiv](https://arxiv.org/abs/2607.19957) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`KV cache reuse`、`context contamination`、`behavior hijacking`、`prompt injection`、`instruction hierarchy`

👤 **作者**：Yichi Zhang、Zhiqi Wang、Huan Zhang、Yuchen Yang

- 🎯 **研究动机**：位置无关 KV 复用按文本块匹配而不论位置，KV 编码了原始上下文， benign 文本块的缓存可能携带攻击者前缀
- 🔬 **研究方法**：提出 HijackKV：优化攻击者前缀使后续常见良性文本块的 KV 编码攻击目标，文本本身不变以保证未来缓存命中
- 📌 **结论**：单次尝试平均成功率 94%，在低命中率（10%）与频繁重算（50%）下仍有效，跨轮持续、黑盒跨模型迁移，并给出安全 KV 复用系统设计建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Key-Value (KV) cache reduces inference latency in large language models (LLMs). Traditional prefix-based reuse has low cache hit rates across inference requests because it requires exact token and position matches. To improve efficiency, recent system optimizations introduce position-independent KV reuse, allowing KV cache to be reused whenever identical text chunks appear, regardless of their position in the sequence. We show this design introduces a new threat, KV Cache Hijacking. Since KV caches are retrieved by token match but encode the context in which they were originally computed, the KV tied to a benign-looking token chunk may encode an attacker-controlled prefix. When later reused in a victim query, this contaminated KV silently hijacks the model's behavior, even if no attacker-controlled text appears in the input. We introduce HIJACKKV, the first attack framework that systematically exploits this vulnerability, demonstrating its severity and practicality. HIJACKKV optimizes an attacker-controlled prefix, so that the KV computed for a subsequent common benign text encodes the attacker's goal, while the text remains unchanged for future cache hits. HIJACKKV achieves an average 94% success rate in a single attempt, remains effective under realistic constraints including low hit rates (10%) and frequent recomputation (50%), persists over multi-turn interactions, and transfers across models in black-box settings. We further provide design insights for building secure KV reuse systems.

</details>

### 29. Lethe: Purifying Backdoored Large Language Models with Knowledge Dilution

📄 [arXiv](https://arxiv.org/abs/2508.21004) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-chen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`LLM backdoor`、`knowledge dilution`、`model purification`、`purification`

👤 **作者**：Chen Chen、…、Kwok-Yan Lam

- 🎯 **研究动机**：现有 LLM 后门防御覆盖窄、多仅检测，难敌编辑式、多触发与无触发攻击
- 🔬 **研究方法**：提出 LETHE 知识稀释：内部用轻量数据训练干净模型并与后门模型合并稀释参数记忆，外部在 prompt 注入良性语义相关证据转移注意力
- 📌 **结论**：五个 LLM、八种攻击上超八个 SoTA 防御基线，高级后门 ASR 最多降 98% 且保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have seen significant advancements, achieving superior performance in various Natural Language Processing (NLP) tasks. However, they remain vulnerable to backdoor attacks, where models behave normally for standard queries but generate harmful responses or unintended output when specific triggers are activated. Existing backdoor defenses either lack comprehensiveness, focusing on narrow trigger settings, detection-only mechanisms, and limited domains, or fail to withstand advanced scenarios like model-editing-based, multi-trigger, and triggerless attacks. In this paper, we present LETHE, a novel method to eliminate backdoor behaviors from LLMs through knowledge dilution using both internal and external mechanisms. Internally, LETHE leverages a lightweight dataset to train a clean model, which is then merged with the backdoored model to neutralize malicious behaviors by diluting the backdoor impact within the model's parametric memory. Externally, LETHE incorporates benign and semantically relevant evidence into the prompt to distract LLM's attention from backdoor features. Experimental results on classification and generation domains across 5 widely used LLMs demonstrate that LETHE outperforms 8 state-of-the-art defense baselines against 8 backdoor attacks. LETHE reduces the attack success rate of advanced backdoor attacks by up to 98% while maintaining model utility. Furthermore, LETHE has proven to be cost-efficient and robust against adaptive backdoor attacks.

</details>

### 30. Patcher: Post-Hoc Patching of Backdoored Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.02995) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gao-anjun)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`LLM backdoor`、`post-hoc patching`、`saliency localization`、`post-hoc patch`、`trigger localization`

👤 **作者**：Anjun Gao、Yueyang Quan、Yufei Xia、Zhuqing Liu、Minghong Fang

- 🎯 **研究动机**：jailbreak 后门防御通常需要完整攻击信息或多个触发样本，防御者仅有单个失败案例时不适用
- 🔬 **研究方法**：提出 Patcher，仅凭一个上报失败案例和模型参数：先用响应条件化梯度显著性加自适应聚类定位触发器，再用 KL 约束微调解除触发-响应关联并保留正常能力
- 📌 **结论**：多种后门攻击下成功定位并中和后门、保持模型效用，对自适应攻击同样鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain vulnerable to jailbreak backdoor attacks, where adversaries poison safety alignment data to embed hidden triggers that bypass safety mechanisms. Existing defenses often require comprehensive attack information or multiple triggered examples, making them impractical when defenders only observe a single reported failure case without knowing whether it stems from a backdoor attack or a natural alignment bug. This paper presents Patcher, a post-hoc defense framework that repairs backdoored language models using only a single reported failure case and the model parameters. Patcher operates in two stages. First, it localizes backdoor triggers by computing response-conditioned gradient-based saliency scores and applying adaptive clustering to separate triggers from benign context. Second, it patches the model through a constrained fine-tuning objective that breaks the trigger-response association while preserving benign-task utility and robustness to non-triggered jailbreak attacks through KL-divergence constraints. We conduct extensive evaluations across multiple backdoor attack strategies and demonstrate that Patcher successfully localizes triggers and neutralizes backdoors while maintaining model utility. We further show robustness against adaptive attacks designed to evade our defense. This work represents a significant step toward practical defenses against training-time attacks in deployed language models.

</details>

### 31. The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again

📄 [arXiv](https://arxiv.org/abs/2508.19774) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-tong)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`model supply chain`、`Pickle`、`stealthy poisoning`

👤 **作者**：Tong Liu、Guozhu Meng、Peng Zhou、Zizhuang Deng、Shuaiyin Yao、Kai Chen

- 🎯 **研究动机**：pickle 反序列化漏洞长期未解，现有扫描器对模型投毒面理解不全、检测逻辑脆弱
- 🔬 **研究方法**：系统披露 pickle 投毒面：识别五大框架 22 条模型加载路径（19 条被漏检），提出 Exception-Oriented Programming 绕过技术，并在风险函数面发现 133 个可利用 gadget
- 📌 **结论**：gadget 绕过率近 100%，最佳扫描器下仍达 89%；获厂商致谢与 6000 美元赏金

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pickle deserialization vulnerabilities have persisted throughout Python's history, remaining widely recognized yet unresolved. Due to its ability to transparently save and restore complex objects into byte streams, many AI/ML frameworks continue to adopt pickle as the model serialization protocol despite its inherent risks. As the open-source model ecosystem grows, model-sharing platforms such as Hugging Face have attracted massive participation, significantly amplifying the real-world risks of pickle exploitation and opening new avenues for model supply chain poisoning. Although several state-of-the-art scanners have been developed to detect poisoned models, their incomplete understanding of the poisoning surface leaves the detection logic fragile and allows attackers to bypass them. In this work, we present the first systematic disclosure of the pickle-based model poisoning surface from both model loading and risky function perspectives. Our research demonstrates how pickle-based model poisoning can remain stealthy and highlights critical gaps in current scanning solutions. On the model loading surface, we identify 22 distinct pickle-based model loading paths across five foundational AI/ML frameworks, 19 of which are entirely missed by existing scanners. We further develop a bypass technique named Exception-Oriented Programming (EOP) and discover 9 EOP instances, 7 of which can bypass all scanners. On the risky function surface, we discover 133 exploitable gadgets, achieving almost a 100% bypass rate. Even against the best-performing scanner, these gadgets maintain an 89% bypass rate. By systematically revealing the pickle-based model poisoning surface, we achieve practical and robust bypasses against real-world scanners. We responsibly disclose our findings to corresponding vendors, receiving acknowledgments and a $6000 bug bounty.

</details>

### 32. Unveiling the Pitfalls of Data-Free Backdoor Detection Against Pre-Trained Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-quan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`detection`、`backdoor detection`、`pre-trained model`、`convergence side channel`

👤 **作者**：Quan Zhao、…、Yang Zhang

- 🎯 **研究动机**：无数据后门检测方法很少在预训练模型上评估，报告的强性能可能造成虚假安全感
- 🔬 **研究方法**：构建覆盖 30000 多个模型与常见后门攻击的大规模基准；提出以收敛速度作为侧信道信号的新检测器
- 📌 **结论**：现有无数据方法在多数预训练模型上失效；新检测器达 SOTA，但严重漏洞仍存

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to deep learning models, enabling adversaries to manipulate the output through hidden triggers. Recent detection methods aim to identify backdoors without relying on clean samples or assumptions about attacks. Although they report strong performance, these methods are rarely evaluated on pre-trained models. In this paper, we present the first large-scale study of data-free backdoor detection on pre-trained models. Our benchmark includes more than 30,000 models and covers common backdoor attacks. We find that existing data-free methods fail on most pre-trained models, leading to a false sense of security. Despite our effective improvements, serious vulnerabilities remain. To address this, we propose using convergence speed as a new side-channel signal for backdoor detection. Using this signal, we reveal the cause of the remaining vulnerabilities and build a novel data-free detector that achieves state-of-the-art performance against existing methods. We further analyze how backdoor attacks evade detection and outline unresolved issues. Our results indicate that detecting backdoor attacks requires further exploration. We hope that our work can draw attention to the vulnerabilities in backdoor detection mechanisms for machine learning systems.

</details>
### 隐私泄漏、成员推断与机密计算

### 33. Can we estimate privacy vulnerability of individual records? Towards Mitigating Attribute Inference Attacks on ML Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kabir)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`detection`、`attribute inference`、`record-level vulnerability`、`AttriVET`、`cyber misuse`

👤 **作者**：Ehsanul Kabir、Najrin Sultana、Ninghui Li、Shagufta Mehnaz

- 🎯 **研究动机**：现有防御目标过宽，无法针对属性推断攻击提供细粒度、漏洞感知的保护
- 🔬 **研究方法**：NeighVE 从对手侧估计记录级泄露脆弱性；VESL 子空间学习防御；AttriVET 预测脆弱记录
- 📌 **结论**：记录级风险主要由数据集特征而非模型架构决定；AttriVET 跨场景超 90% 准确预测脆弱记录，VESL 以最小效用损失缓解泄露并顺带改善公平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) has brought transformative applications across various sectors, including sensitive fields like healthcare, finance, and customer analytics. However, ML models are susceptible to privacy leaks, especially through attribute inference and model inversion attacks, raising concerns for data confidentiality in privacy-critical domains. Existing defenses pursue much broader objectives than specifically preventing privacy leakage from attribute inference attacks, and as a result often fail to provide fine-grained, vulnerability-aware protection without significant utility costs. Motivated by this need, we first investigate record-level vulnerability estimation through NeighVE, an adversary-side tool designed to identify which individual records are more exposed to inference. Insights from NeighVE reveal that the record-level risk of privacy leakage is largely agnostic to model architectures and attack strategies and is instead governed by dataset-level characteristics, particularly the distribution of sensitive attributes in the local neighborhood of each record. Building on this insight, we propose VESL, a subspace-learning–inspired defense that mitigates attribute-inference leakage while keeping utility loss to a bare minimum. As a byproduct of its balancing mechanism, VESL also improves fairness across sensitive attributes and prevents NeighVE from reliably identifying vulnerable records. As a supporting contribution, we introduce AttriVET, an estimator that predicts which individual records are vulnerable with over 90% accuracy across diverse scenarios, enabling risk-aware defense design and auditing.

</details>

### 34. CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage

📄 [arXiv](https://arxiv.org/abs/2507.16872) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-na)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`attack`、`model compression`、`membership inference`、`privacy leakage`

👤 **作者**：Na Li、Yansong Gao、Hongsheng Hu、Boyu Kuang、Anmin Fu

- 🎯 **研究动机**：模型压缩的资源-性能权衡之外，其引入的隐私风险被忽视
- 🔬 **研究方法**：提出 CompLeak：以成员推断评估 TF-Lite 与 PyTorch Mobile 的剪枝、量化与权重聚类，含单压缩模型、结合原模型与多压缩模型三种变体
- 📌 **结论**：压缩模型对成员与非成员影响不同，结合原模型或多版本元信息可显著放大隐私泄露，覆盖 ResNet 到 BERT 与 GPT-2

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model compression is crucial for minimizing memory storage and accelerating inference in deep learning (DL) models, including recent foundation models like large language models (LLMs). Users can access different compressed model versions according to their resources and budget. However, while existing compression operations primarily focus on optimizing the trade-off between resource efficiency and model performance, the privacy risks introduced by compression remain overlooked and insufficiently understood. In this work, through the lens of membership inference attack (MIA), we propose CompLeak, the first privacy risk evaluation framework examining three widely used compression configurations that are pruning, quantization, and weight clustering supported by the commercial model compression framework of Google's TensorFlow-Lite (TF-Lite) and Facebook's PyTorch Mobile. CompLeak has three variants, given available access to the number of compressed models and original model. CompLeakNR starts by adopting existing MIA methods to attack a single compressed model, and identifies that different compressed models influence members and non-members differently. When the original model and one compressed model are available, CompLeakSR leverages the compressed model as a reference to the original model and uncovers more privacy by combining meta information (e.g., confidence vector) from both models. When multiple compressed models are available with/without accessing the original model, CompLeakMR innovatively exploits privacy leakage info from multiple compressed versions to substantially signify the overall privacy leakage. We conduct extensive experiments on seven diverse model architectures (from ResNet to foundation models of BERT and GPT-2), and six image and textual benchmark datasets.

</details>

### 35. Connect the Dots: Knowledge Graph–Guided Crawler Attack on Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2601.15678) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yao-dots)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`RAG corpus extraction`、`knowledge graph`、`query planning`、`privacy leakage`、`memorization`

👤 **作者**：Mengyu Yao、…、Ding Li

- 🎯 **研究动机**：已有 RAG 知识库窃取攻击多为启发式且早早停滞在次优覆盖
- 🔬 **研究方法**：把窃取形式化为自适应随机覆盖问题，RAGCrawler 以知识图谱引导维护全局攻击状态，估计覆盖增益、调度高价值语义锚点并生成无冗余自然查询
- 📌 **结论**：四语料四生成器上 1000 查询内平均覆盖 66.8%（最高 84.4%），较最强基线提升 44.90%，达 70% 覆盖所需查询平均至少减少 4.03 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Stealing attacks pose a persistent threat to the intellectual property of deployed machine-learning systems. Retrieval-augmented generation (RAG) intensifies this risk by extending the attack surface beyond model weights to knowledge base that often contains IP-bearing assets such as proprietary runbooks, curated domain collections, or licensed documents. Recent work shows that multi-turn questioning can gradually steal corpus content from RAG systems, yet existing attacks are largely heuristic and often plateau early. We address this gap by formulating RAG knowledge-base stealing as an adaptive stochastic coverage problem (ASCP), where each query is a stochastic action and the goal is to maximize the conditional expected marginal gain (CMG) in corpus coverage under a query budget. Bridging ASCP to real-world black-box RAG knowledge-base stealing raises three challenges: CMG is unobservable, the natural-language action space is intractably large, and feasibility constraints require stealthy queries that remain effective under diverse architectures. We introduce RAGCrawler, a knowledge graph-guided attacker that maintains a global attacker-side state to estimate coverage gains, schedule high-value semantic anchors, and generate non-redundant natural queries. Across four corpora and four generators with BGE retriever, RAGCrawler achieves 66.8% average coverage (up to 84.4%) within 1,000 queries, improving coverage by 44.90% relative to the strongest baseline. It also reduces the queries needed to reach 70% coverage by at least 4.03x on average and enables surrogate reconstruction with answer similarity up to 0.699. Our attack is also scalable to retriever switching and newer RAG techniques like query rewriting and multi-query retrieval. These results highlight urgent needs to protect RAG knowledge assets.

</details>

### 36. Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment

📄 [arXiv](https://arxiv.org/abs/2605.24312) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nguyen-nguyen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`RAG membership inference`、`entailment`、`query efficiency`、`membership inference`

👤 **作者**：Nguyen Linh Bao Nguyen、…、Yang Xiang

- 🎯 **研究动机**：已有 RAG 成员推断依赖易检测的模板查询或大量昂贵的重复查询
- 🔬 **研究方法**：MEntA 利用自然语言蕴含：提出宽泛信息寻求问题，测模型响应与候选文档间的蕴含关系，免代理模型与大查询预算
- 📌 **结论**：NFCorpus、SCIDOCS、TREC-COVID 上仅 5 次查询达 0.991 AUC，同等条件超先前方法 0.42 AUC、成本降 65 倍，且在 SOTA RAG 防御下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has become central to large language model (LLM) deployments, grounding responses in enterprise or proprietary data to reduce hallucinations. However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information. Existing MIAs are feasible, but they often rely on easily detected templated queries or require many non-templated yet costly and repetitive queries, limiting practicality. We ask: Can an adversary launch a limited-budget, surrogate-free, stealthy, and defense-agnostic membership inference attack using non-templated queries? We present MEntA (Membership Entailment Attack), a query-efficient MIA that leverages natural-language entailment to maximize information gained per query. By asking low-cost, broad, information-seeking questions and measuring entailment between model responses and candidate documents, MEntA eliminates the need for costly shadow models and large query budgets. Across NFCorpus, SCIDOCS, and TREC-COVID, MEntA achieves up to 0.991 AUC with only 5 queries, outperforming prior methods by up to 0.42 AUC under equivalent conditions. It remains effective under state-of-the-art (SOTA) RAG defenses, while current detectors either miss MEntA or flag benign queries at high rates. Regarding cost, MEntA reduces total attack cost by up to 65$\times$ lower compared to SOTA attacks under the same attack setting. Our findings expose the feasibility of realistic, low-cost privacy leakage in RAG systems and highlight the urgent need for privacy-aware retrieval and defense mechanisms.

</details>

### 37. From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-sijia)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM API`、`token-length side channel`、`content reconstruction`、`model extraction`

👤 **作者**：Sijia Li、…、Qi Li

- 🎯 **研究动机**：现代 LLM 服务以多 token 块流式输出，看似缓解 token 级侧信道，但合并块长度构成新的侧信道
- 🔬 **研究方法**：PromptEcho 被动窃听攻击：把重构形式化为约束序列恢复——语义感知推理分解合并长度观测，用微调 LM 的语言先验做概率语义对齐推断最可能 token
- 📌 **结论**：GPT-4o 与 DeepSeek-V3 真实 API 流量上 42.5% 会话正确推断主题、25.5% 响应以 0.9 以上余弦相似度重构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly accessed via remote APIs over encrypted channels. While previous studies have shown that fine-grained side channels can leak information under token-by-token processing, modern LLM services typically stream outputs in multi-token chunks, seemingly mitigating such token-level leakage. However, in this paper, we demonstrate that token aggregation does not eliminate privacy risks. Instead, it introduces a merged token-length side channel. In this channel, the sizes of encrypted response chunks inadvertently expose character-length patterns of merged token groups. To study the practical implications of this leakage, we propose PromptEcho, a passive eavesdropping attack that reconstructs semantically meaningful portions of natural-language responses from observations of merged token lengths. PromptEcho frames the reconstruction task as a constrained sequence recovery problem, leveraging semantics-aware reasoning to resolve the ambiguity caused by merged token transmission. Specifically, PromptEcho first applies semantics-aware reasoning to decompose merged-token length observations, then uses probabilistic semantic alignment with a fine-tuned language model's linguistic priors to infer the most likely underlying tokens. We evaluate PromptEcho on real-world API interaction traffic from multiple commercial LLM services, correctly inferring the topic for 42.5% of sessions and reconstructing 25.5% of responses with a cosine similarity above 0.9 on OpenAI's GPT-4o and DeepSeek-V3. These findings demonstrate that merged-token transmission remains vulnerable to token-length side-channel attacks, indicating practical privacy risks from encrypted traffic observations under the evaluated API-based LLM settings.

</details>

### 38. Imitative Membership Inference Attack

📄 [arXiv](https://arxiv.org/abs/2509.06796) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/du)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`membership inference`、`imitative model`、`low-cost auditing`、`privacy leakage`

👤 **作者**：Yuntao Du、Yuetian Chen、Hanshen Xiao、Bruno Ribeiro、Ninghui Li

- 🎯 **研究动机**：SoTA 成员推断需训练数百个独立影子模型，计算开销巨大
- 🔬 **研究方法**：提出 IMIA：以模仿训练技术构造少量紧密复刻目标行为的目标感知模仿模型用于推断
- 📌 **结论**：多种攻击设置下显著优于既有 MIA，计算成本不足 SoTA 方法的 5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A Membership Inference Attack (MIA) assesses how much a target machine learning model reveals about its training data by determining whether specific query instances were part of the training set. State-of-the-art MIAs rely on training hundreds of shadow models that are independent of the target model, leading to significant computational overhead. In this paper, we introduce Imitative Membership Inference Attack (IMIA), which employs a novel imitative training technique to strategically construct a small number of target-informed imitative models that closely replicate the target model's behavior for inference. Extensive experimental results demonstrate that IMIA substantially outperforms existing MIAs in various attack settings while only requiring less than 5% of the computational cost of state-of-the-art approaches.

</details>

### 39. Large-scale online deanonymization with LLMs

📄 [arXiv](https://arxiv.org/abs/2602.16800) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/lermen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM agent`、`deanonymization`、`online privacy`、`privacy leakage`、`memorization`

👤 **作者**：Simon Lermen、Daniel Paleka、Joshua Swanson、Michael Aerni、Nicholas Carlini、Florian Tramèr

- 🎯 **研究动机**：LLM agent 能否对伪匿名用户实施规模化去匿名化未知，线上隐私威胁模型待重估
- 🔬 **研究方法**：构建 LLM 管线抽取身份特征、经语义嵌入检索候选并推理验证匹配，建三个跨平台地面真值数据集（Hacker News-LinkedIn、Reddit 跨社区等）
- 📌 **结论**：90% 精度下召回最高 68%，最佳非 LLM 方法近 0%；伪匿名用户的实践模糊性保护已失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that large language models can be used to perform at-scale deanonymization. With full Internet access, our agent can re-identify Hacker News users and Anthropic Interviewer participants at high precision, given pseudonymous online profiles and conversations alone, matching what would take hours for a dedicated human investigator. We then design attacks for the closed-world setting. Given two databases of pseudonymous individuals, each containing unstructured text written by or about that individual, we implement a scalable attack pipeline that uses LLMs to: (1) extract identity-relevant features, (2) search for candidate matches via semantic embeddings, and (3) reason over top candidates to verify matches and reduce false positives. Compared to classical deanonymization work (e.g., on the Netflix prize) that required structured data, our approach works directly on raw user content across arbitrary platforms. We construct three datasets with known ground-truth data to evaluate our attacks. The first links Hacker News to LinkedIn profiles, using cross-platform references that appear in the profiles. Our second dataset matches users across Reddit movie discussion communities; and the third splits a single user's Reddit history in time to create two pseudonymous profiles to be matched. In each setting, LLM-based methods substantially outperform classical baselines, achieving up to 68% recall at 90% precision compared to near 0% for the best non-LLM method. Our results show that the practical obscurity protecting pseudonymous users online no longer holds and that threat models for online privacy need to be reconsidered.

</details>

### 40. MASLeak: Investigating and Exposing Intellectual Property Leakage Vulnerabilities in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2505.12442) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-liwen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`multi-agent system`、`IP leakage`、`black-box extraction`、`model copyright`

👤 **作者**：Liwen Wang、…、Shing-Chi Cheung

- 🎯 **研究动机**：多智能体系统架构与交互复杂，其知识产权泄露风险未被量化
- 🔬 **研究方法**：提出 MASLeak，仅经公共 API 提交构造查询，蠕虫式诱出并保留各 agent 响应，提取 agent 数量、拓扑、系统提示等组件
- 📌 **结论**：810 个合成应用上系统提示与任务指令提取成功率 87%、架构 92%，Coze 与 CrewAI 真实应用亦验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Large Language Models (LLMs) has led to the emergence of Multi-Agent Systems (MAS) to perform complex tasks through collaboration. However, the intricate nature of MAS, including their architecture and agent interactions, raises significant concerns regarding intellectual property (IP) protection. In this paper, we introduce MASLEAK, a novel attack framework designed to extract sensitive information from MAS applications. MASLEAK targets a practical, black-box setting, where the adversary has no prior knowledge of the MAS architecture or agent configurations. The adversary can only interact with the MAS through its public API, submitting attack query $q$ and observing outputs from the final agent. Inspired by how computer worms propagate and infect vulnerable network hosts, MASLEAK carefully crafts adversarial query $q$ to elicit, propagate, and retain responses from each MAS agent that reveal a full set of proprietary components, including the number of agents, system topology, system prompts, task instructions, and tool usages. We construct the first synthetic dataset of MAS applications with 810 applications and also evaluate MASLEAK against real-world MAS applications, including Coze and CrewAI. MASLEAK achieves high accuracy in extracting MAS IP, with an average attack success rate of 87% for system prompts and task instructions, and 92% for system architecture in most cases. We conclude by discussing the implications of our findings and the potential defenses.

</details>

### 41. Membership Inference Attacks on Tokenizers of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.05699) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tong)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`LLM tokenizer`、`membership inference`、`adaptive defense`、`privacy leakage`、`memorization`

👤 **作者**：Meng Tong、Yuntao Du、Kejiang Chen、Weiming Zhang、Ninghui Li

- 🎯 **研究动机**：对预训练 LLM 的成员推断受误标样本、分布漂移与模型规模差异困扰
- 🔬 **研究方法**：首次把 tokenizer 作为攻击面：其可高效从头训练且训练数据具代表性，探索五种数据集成员推断方法并提出自适应防御
- 📌 **结论**：数百万互联网样本实验揭示 SoTA LLM tokenizer 的成员泄露漏洞，需针对性隐私保护机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) are widely used to assess the privacy risks associated with machine learning models. However, when these attacks are applied to pre-trained large language models (LLMs), they encounter significant challenges, including mislabeled samples, distribution shifts, and discrepancies in model size between experimental and real-world settings. To address these limitations, we introduce tokenizers as a new attack vector for membership inference. Specifically, a tokenizer converts raw text into tokens for LLMs. Unlike full models, tokenizers can be efficiently trained from scratch, thereby avoiding the aforementioned challenges. In addition, the tokenizer's training data is typically representative of the data used to pre-train LLMs. Despite these advantages, the potential of tokenizers as an attack vector remains unexplored. To this end, we present the first study on membership leakage through tokenizers and explore five attack methods to infer dataset membership. Extensive experiments on millions of Internet samples reveal the vulnerabilities in the tokenizers of state-of-the-art LLMs. To mitigate this emerging risk, we further propose an adaptive defense. Our findings highlight tokenizers as an overlooked yet critical privacy threat, underscoring the urgent need for privacy-preserving mechanisms specifically designed for them.

</details>

### 42. MEPS: Privacy-preserving Edge-cloud Video Foundation Model Inference with Privacy Protectability

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shi-siping)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`video foundation model`、`edge-cloud privacy`、`selective encryption`

👤 **作者**：Siping Shi、Rui Lu、Dan Wang、Bihai Zhang

- 🎯 **研究动机**：边缘-云视频理解要么扰动敏感信息损精度、要么全帧加密给边缘设备带来沉重计算负担
- 🔬 **研究方法**：MEPS 观察到仅少数帧的敏感信息对任务真正必要：关键帧选择性加密、其余轻量扰动；信息论度量 privacy protectability 判断敏感信息与任务信息重叠度
- 📌 **结论**：保持隐私保护与任务精度同时效率显著提升，加速 48.8 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Edge-cloud video understanding systems, which leverage video foundation models on the cloud for inference to serve downstream tasks, present significant privacy risks due to the exposure of video data containing sensitive information (e.g., human faces) from edge devices to the cloud. To mitigate privacy leakage, existing methods often involve perturbing sensitive information, which can unfortunately degrade the accuracy of video understanding tasks, especially when that sensitive information is relevant to the tasks. Alternatively, encryption-based private inference offers strong privacy guarantees without accuracy loss but imposes a substantial computational burden on resource-constrained edge devices. This paper addresses these privacy challenges by observing that while many video frames contain sensitive information, only a few contain sensitive information that is truly essential for the video understanding tasks. Thus, it is unnecessary and inefficient to apply universal, computation-intensive encryption for all video frames on the edge. We propose MEPS, a novel privacy-preserving video understanding system designed to intelligently manage the trade-off between privacy, accuracy, and efficiency. MEPS selectively encrypts video frames only when the sensitive information they contain is crucial for the downstream tasks, thus ensuring robust privacy for essential data. For the majority of frames where sensitive information is non-essential to the task, MEPS applies lightweight perturbation schemes. This approach effectively protects privacy by obscuring sensitive details without negatively impacting task accuracy or overburdening edge devices. A core component of MEPS is its ability to discern whether sensitive information within a frame is essential for video understanding. To facilitate this, we propose privacy protectability, a novel metric rooted in information theory that evaluates the degree of overlap between sensitive information and the information required for video understanding tasks. We implement a prototype of MEPS and evaluate its performance with three public real-world video trace datasets. Theoretical analysis proves MEPS has rigorous privacy guarantee. Experimental results demonstrate that MEPS can maintain the satisfied privacy protection and task accuracy, while significantly improve system efficiency, achieving a 48.8× speedup.

</details>

### 43. Network-Level Prompt and Trait Leakage in Local Research Agents

📄 [arXiv](https://arxiv.org/abs/2508.20282) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`research agent`、`traffic analysis`、`trait inference`、`scientific reliability`、`error localization`

👤 **作者**：Hyejun Jeong、Mohammadreza Teymoorianfard、Abhinav Kumar、Amir Houmansadr、Eugene Bagdasarian

- 🎯 **研究动机**：本地部署的 Web/Research agent 每请求访问 70-140 个域名，独特时序模式暴露给 DNS、ISP、VPN 等被动观察者
- 🔬 **研究方法**：构建真实与合成人格查询的 WRA 轨迹数据集，仅凭访问 IP 与时序元数据推断 prompt 与用户特质，以 OBELS 度量相似度
- 📌 **结论**：恢复 prompt 超 73% 的功能与领域知识，多会话下 32 个潜在特质中恢复 19 个；限制域名多样性等缓解平均降低攻击 29%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that Web and Research Agents (WRAs) -- language-model-based systems that investigate complex topics on the Internet -- are vulnerable to inference attacks by passive network observers. Deployment of WRAs \emph{locally} by organizations and individuals for privacy, legal, or financial purposes exposes them to DNS resolvers, malicious ISPs, VPNs, web proxies, and corporate or government firewalls. However, unlike sporadic and scarce web browsing by humans, WRAs visit $70{-}140$ domains per each request with a distinct timing pattern creating unique privacy risks. Specifically, we demonstrate a novel prompt and user trait leakage attack against WRAs that only leverages their network-level metadata (i.e., visited IP addresses and their timings). We start by building a new dataset of WRA traces based on real user search queries and queries generated by synthetic personas. We define a behavioral metric (called OBELS) to comprehensively assess similarity between original and inferred prompts, showing that our attack recovers over 73\% of the functional and domain knowledge of user prompts. Extending to a multi-session setting, we recover up to 19 of 32 latent traits with high accuracy. Our attack remains effective under partial observability and noisy conditions. Finally, we discuss mitigation strategies that constrain domain diversity or obfuscate traces, showing negligible utility impact while reducing attack effectiveness by an average of 29\%.

</details>

### 44. NOIR: Privacy-Preserving Generation of Code with Open-Source LLMs

📄 [arXiv](https://arxiv.org/abs/2601.16354) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nguyen-khoa)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`code generation`、`prompt privacy`、`local differential privacy`

👤 **作者**：Khoa Nguyen、…、My T. Thai

- 🎯 **研究动机**：云端代码生成服务可观察客户 prompt 与生成代码，带来知识产权与数据安全风险
- 🔬 **研究方法**：NOIR 在客户端编码 prompt 嵌入发往云端获取增强嵌入并在本地解码生成，以 token 嵌入级本地差分隐私与数据无关随机化 tokenizer 实现不可区分性，抵御诚实但好奇云的重构与频率分析
- 📌 **结论**：MBPP/HumanEval Pass@1 达 76.7/77.4，BigCodeBench Pass@1 38.7（较原始 LLM 仅降 1.77%），同时保持强隐私

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although boosting software development performance, large language model (LLM)-powered code generation introduces intellectual property and data security risks rooted in the fact that a service provider (cloud) observes a client's prompts and generated code, which can be proprietary in commercial systems. To mitigate this problem, we propose NOIR, the first framework to protect the client's prompts and generated code from the cloud. NOIR uses an encoder and a decoder at the client to encode and send the prompts' embeddings to the cloud to get enriched embeddings from the LLM, which are then decoded to generate the code locally at the client. Since the cloud can use the embeddings to infer the prompt and the generated code, NOIR introduces a new mechanism to achieve indistinguishability, a local differential privacy protection at the token embedding level, in the vocabulary used in the prompts and code, and a data-independent and randomized tokenizer on the client side. These components effectively defend against reconstruction and frequency analysis attacks by an honest-but-curious cloud. Extensive analysis and results using open-source LLMs show that NOIR significantly outperforms existing baselines on benchmarks, including the Evalplus (MBPP and HumanEval, Pass@1 of 76.7 and 77.4), and BigCodeBench (Pass@1 of 38.7, only a 1.77% drop from the original LLM) under strong privacy against attacks.

</details>

### 45. SMASH: Scalable Maliciously Secure Hybrid Multi-party Computation Framework for Privacy-Preserving Large Language Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/lv)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`private LLM inference`、`malicious MPC`、`hybrid protocol`

👤 **作者**：Yunlv Lv、…、Yanan Cao

- 🎯 **研究动机**：恶意安全 MPC 框架扩展到大模型时因非线性算子 O(n^2) 通信与昂贵份额转换出现性能崩塌
- 🔬 **研究方法**：提出 SMASH：DFT 旋转技术加轻量 ZKPoK 评估非线性运算，首次实现相对参与方数的线性通信复杂度，并提供 A2L/L2A 与 SM-LUT 等高效域转换协议
- 📌 **结论**：较 MP-SPDZ、MD-ML 等 SOTA 框架运行时最高快 18.9 倍、通信最多降 10^3 倍，支持地理分布的安全 LLM 部署

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The meteoric rise of Large Language Models (LLMs) has sparked an urgent need for privacy-preserving inference. However, existing maliciously secure multi-party computation (MPC) frameworks face a "performance collapse" when scaling to large models, primarily due to the quadratic (O(n 2 )) communication overhead of nonlinear operators and expensive share conversions. This paper presents SMASH, a highly scalable, maliciously secure hybrid MPC framework that shatters these bottlenecks. SMASH introduces a novel DFT-based rotation technique and a lightweight zero-knowledge proof of knowledge (ZKPoK) construction to evaluate nonlinear operations. For the first time, this approach achieves linear communication complexity (O(n)) relative to the party count, independent of function complexity. Furthermore, SMASH provides a suite of high-efficiency conversion protocols (A2L/L2A and SM-LUT-based A2B/B2A) that bridge arithmetic and Boolean domains without relying on costly cryptographic primitives. Extensive benchmarks demonstrate that SMASH outperforms state-of-the-art frameworks (e.g., MP-SPDZ, MD-ML) by up to 18.9× in runtime and achieves a communication reduction of up to 10 3 ×. With its constant-round online phase and low WAN sensitivity, SMASH paves the way for secure, geographically distributed LLM deployments, achieving an unprecedented balance between adversarial robustness and practical efficiency.

</details>

### 46. VidLeaks: Membership Inference Attacks Against Text-to-Video Models

📄 [arXiv](https://arxiv.org/abs/2601.11210) · 🌐 [Project](https://zenodo.org/records/17972831) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-li)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`text-to-video model`、`membership inference`、`temporal memorization`、`privacy leakage`

👤 **作者**：Li Wang、Wenyu Chen、Ning Yu、Zheng Li、Shanqing Guo

- 🎯 **研究动机**：现有成员推断面向静态图像或文本，忽视 T2V 中关键帧记忆稀疏与时序动态不稳定
- 🔬 **研究方法**：VidLeaks 以空间重建保真（Top-K 相似度放大关键帧空间记忆）与时间生成稳定性（多次查询语义一致性）双信号，在监督、参考与仅查询三种黑盒设定下探测
- 📌 **结论**：严格仅查询设定下 AnimateDiff AUC 达 82.92%、InstructVideo 达 97.01%，证明 T2V 模型经稀疏与时序记忆大量泄漏成员信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of powerful Text-to-Video (T2V) models, trained on massive web-scale datasets, raises urgent concerns about copyright and privacy violations. Membership inference attacks (MIAs) provide a principled tool for auditing such risks, yet existing techniques - designed for static data like images or text - fail to capture the spatio-temporal complexities of video generation. In particular, they overlook the sparsity of memorization signals in keyframes and the instability introduced by stochastic temporal dynamics. In this paper, we conduct the first systematic study of MIAs against T2V models and introduce a novel framework VidLeaks, which probes sparse-temporal memorization through two complementary signals: 1) Spatial Reconstruction Fidelity (SRF), using a Top-K similarity to amplify spatial memorization signals from sparsely memorized keyframes, and 2) Temporal Generative Stability (TGS), which measures semantic consistency across multiple queries to capture temporal leakage. We evaluate VidLeaks under three progressively restrictive black-box settings - supervised, reference-based, and query-only. Experiments on three representative T2V models reveal severe vulnerabilities: VidLeaks achieves AUC of 82.92% on AnimateDiff and 97.01% on InstructVideo even in the strict query-only setting, posing a realistic and exploitable privacy risk. Our work provides the first concrete evidence that T2V models leak substantial membership information through both sparse and temporal memorization, establishing a foundation for auditing video generation systems and motivating the development of new defenses. Code is available at: https://zenodo.org/records/17972831.

</details>

### 47. Window-based Membership Inference Attacks Against Fine-tuned Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.02751) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-yuetian)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`fine-tuned LLM`、`membership inference`、`sliding window`

👤 **作者**：Yuetian Chen、…、Ninghui Li

- 🎯 **研究动机**：已有 LLM 成员推断依赖平均损失等全局信号，稀释了记忆的局部微弱信号
- 🔬 **研究方法**：WBC 滑窗法：多种几何间隔尺寸窗口在文本上滑动，每窗基于目标与参考模型的损失比较做二值投票，跨窗口尺寸集成以捕捉 token 级到短语级记忆模式
- 📌 **结论**：11 个数据集上 AUC 显著超越既有基线，低假阳性阈值下检出率提升 2-3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most membership inference attacks (MIAs) against Large Language Models (LLMs) rely on global signals, like average loss, to identify training data. This approach, however, dilutes the subtle, localized signals of memorization, reducing attack effectiveness. We challenge this global-averaging paradigm, positing that membership signals are more pronounced within localized contexts. We introduce WBC (Window-Based Comparison), which exploits this insight through a sliding window approach with sign-based aggregation. Our method slides windows of varying sizes across text sequences, with each window casting a binary vote on membership based on loss comparisons between target and reference models. By ensembling votes across geometrically spaced window sizes, we capture memorization patterns from token-level artifacts to phrase-level structures. Extensive experiments across eleven datasets demonstrate that WBC substantially outperforms established baselines, achieving higher AUC scores and 2-3 times improvements in detection rates at low false positive thresholds. Our findings reveal that aggregating localized evidence is fundamentally more effective than global averaging, exposing critical privacy vulnerabilities in fine-tuned LLMs.

</details>
### 水印、溯源与模型知识产权

### 48. A Distortion-minimization Watermarking Framework for Large Language Models: Larger Capacity, Stronger Robustness and Higher Quality

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhai)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`tool`、`LLM watermarking`、`distortion minimization`、`paraphrasing robustness`

👤 **作者**：Liming Zhai、Xuezhou Shang、Liyun Zhang、Po Hu

- 🎯 **研究动机**：LLM 水印需同时满足大容量、强鲁棒与高质量，现有方法用分离设计各自应对、难以兼顾
- 🔬 **研究方法**：提出 DMW 框架：把鲁棒性与质量统一建模为文本修改的 distortion cost，按水印长度最小化总失真——语义不变性鲁棒代价与低凝聚高变异区域导向的质量代价；用 syndrome-trellis codes 表述为周期最短路问题，支持实时生成
- 📌 **结论**：跨数据集与 LLM 全面超过 SOTA，严重改写攻击下匹配率比最佳基线高 46.35% 且文本质量更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) watermarking provides verifiable source identification for generated text, and its practical deployment requires large watermark capacity, strong robustness against attacks, and high text quality. However, existing methods often struggle to balance all these criteria, typically addressing them with separate designs. To overcome this, we propose a distortion-minimization watermarking (DMW) framework that unifies capacity, robustness and quality within a single optimization paradigm. This framework models robustness and quality as distortion costs for text modifications, minimizing the total distortion for a given watermark length to achieve an optimal trade-off. Specifically, we design several distortion costs: a robustness cost leveraging semantic invariance to resist attacks, and two quality costs guiding modifications toward low-cohesion, high-variability regions to reduce perceptual impact. We then propose periodically optimized syndrome-trellis codes (PO-STCs), formulating overall distortion minimization as a periodic shortest-path problem. This enables real-time optimization for sequential generation with flexible capacity control. Extensive experiments across diverse datasets and LLMs demonstrate DMW's superiority, outperforming state-of-the-art methods across all criteria. Notably, under severe paraphrasing attacks, DMW achieves a match rate up to 46.35% higher than the best baseline, while maintaining superior text quality.

</details>

### 49. Attesting Model Lineage by Consisted Knowledge Evolution with Fine-Tuning Trajectory

📄 [arXiv](https://arxiv.org/abs/2601.11683) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shang)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`model lineage`、`fine-tuning trajectory`、`ownership attestation`、`model copyright`

👤 **作者**：Zhuoyi Shang、Jiasen Li、Pengzhen Chen、Yanwei Liu、Xiaoyan Gu、Weiping Wang

- 🎯 **研究动机**：开源模型库缺乏鲁棒 lineage 验证，静态架构相似度无法捕捉微调背后的知识动态演化
- 🔬 **研究方法**：借鉴遗传机制，用模型编辑量化微调引入的参数变化，借探针样本把演化知识向量化为紧凑表示，再验证模型间知识关系的算术一致性
- 📌 **结论**：在分类器、扩散模型与 LLM 上跨多样对抗场景实现可靠的模型谱系认证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The fine-tuning technique in deep learning gives rise to an emerging lineage relationship among models. This lineage provides a promising perspective for addressing security concerns such as unauthorized model redistribution and false claim of model provenance, which are particularly pressing in \textcolor{blue}{open-weight model} libraries where robust lineage verification mechanisms are often lacking. Existing approaches to model lineage detection primarily rely on static architectural similarities, which are insufficient to capture the dynamic evolution of knowledge that underlies true lineage relationships. Drawing inspiration from the genetic mechanism of human evolution, we tackle the problem of model lineage attestation by verifying the joint trajectory of knowledge evolution and parameter modification. To this end, we propose a novel model lineage attestation framework. In our framework, model editing is first leveraged to quantify parameter-level changes introduced by fine-tuning. Subsequently, we introduce a novel knowledge vectorization mechanism that refines the evolved knowledge within the edited models into compact representations by the assistance of probe samples. The probing strategies are adapted to different types of model families. These embeddings serve as the foundation for verifying the arithmetic consistency of knowledge relationships across models, thereby enabling robust attestation of model lineage. Extensive experimental evaluations demonstrate the effectiveness and resilience of our approach in a variety of adversarial scenarios in the real world. Our method consistently achieves reliable lineage verification across a broad spectrum of model types, including classifiers, diffusion models, and large language models.

</details>

### 50. Certified in Theory, Broken in Practice: Assumption Gaps in Cryptographic Model Certification

📄 [arXiv](https://arxiv.org/abs/2607.21839) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/luck)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`cryptographic model certification`、`audit evasion`、`zero-knowledge proof`

👤 **作者**：Carter Luck、Olive Franzese-McLaughlin、Elisaweta Masserova、Akira Takahashi、Antigoni Polychroniadou、Nicolas Papernot

- 🎯 **研究动机**：隐私保护 ML 审计协议的安全定义多只认证固定审计数据集上的行为，不保证同分布新数据上同样成立，供应商可借此造假
- 🔬 **研究方法**：证明攻击者可精心构造训练数据使基于零知识证明的密码学模型认证（CMC）在审计集上认证 >99% 准确率而同分布新样本上低于 30%；形式化严格的密码安全定义并给出满足其的通用协议模板
- 📌 **结论**：对现有 CMC 方案给出反例攻击与建设性修正，审计保证必须覆盖部署分布

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Privacy-preserving machine learning auditing protocols allow auditors to assess models for properties such as accuracy or fairness, without revealing their internals or training data. This makes them especially attractive for auditing models deployed in sensitive domains such as healthcare or finance. For these protocols to be meaningful in real-world audit settings, though, their guarantees must reflect how the model will behave once deployed, rather than merely certifying its behavior during an audit. Existing security definitions often miss this mark: most certify model behavior only on a fixed audit dataset, without ensuring that the same guarantees generalize to other datasets drawn from the same distribution. As we show, this gap allows a model provider to attack many cryptographic model certification (CMC) schemes built on secure zero knowledge proofs (ZKP) by carefully engineering training data, resulting in models that exhibit benign behavior during an audit, but pathological behavior in practice. For example, we empirically demonstrate that an attacker can certify that a model achieves over 99% accuracy on an audit dataset, but less than 30% accuracy on fresh samples from the same distribution. To address this gap, we formalize rigorous cryptographic security notions tailored to CMC frameworks, introduce a generic protocol template, and prove that it satisfies these requirements. Our results thus offer both cautionary evidence about existing approaches and constructive guidance for designing secure, privacy-preserving ML auditing protocols.

</details>

### 51. Identifying Provenance of Generative Text-to-Image Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/ha)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`model provenance`、`text-to-image model`、`lineage attribution`、`model copyright`

👤 **作者**：Anna Yoo Jeong Ha、Wenxin Ding、Stanley Wu、Shawn Shan、Haitao Zheng、Ben Y. Zhao

- 🎯 **研究动机**：微调得到的 T2I 模型与从头训练难以区分，虚报模型来源误导用户并抑制竞争
- 🔬 **研究方法**：黑盒查询下提取模型输出视觉特征，用 Jensen-Shannon 散度与基座参考池分布比对，统计假设检验判断是否微调及其父模型
- 📌 **结论**：在七个扩散模型及众多微调变体上谱系归因准确率高，图像后处理或权重扰动下仍有效，并成功溯源在线平台真实模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning provides a fast and cheap way to produce new text-to-image models that are often indistinguishable from ones trained from scratch. Unfortunately, misrepresentation of fine-tuned models creates problems for AI companies and users alike, by disincentivizing competition and misleading users on model quality and ethics of its training process. In this paper, we propose a model provenance system that identifies models produced by fine-tuning on existing text-to-image models, using only black-box query access. Our design is informed by analysis showing that one can quantify the feature space difference between text-to-image models by analyzing their responses to detailed prompts. Our system analyzes model output, extracts visual features using a generic feature extractor, and compares their distributions against those from a reference pool of base models using Jensen-Shannon divergence. Applying statistical hypothesis testing then determines if a target model is trained from scratch or fine-tuned, and if the latter, the likely base (parent) model. We evaluate our system across seven widely used diffusion models and numerous fine-tuned variants. Our results show high accuracy in attributing model lineage, even under adversarial conditions such as image post-processing or weight perturbations. Finally, we demonstrate real world efficacy of our system by tracing provenance of in-the-wild models from popular online platforms.

</details>

### 52. MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images via On-Manifold Latent Manipulation

📄 [arXiv](https://arxiv.org/abs/2608.10166) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/cao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`image watermark removal`、`latent manipulation`、`SynthID`、`content watermark`、`AI-generated content`

👤 **作者**：Jie Cao、…、Jianbing Ni

- 🎯 **研究动机**：AI 生成图像水印对模型无关移除攻击的鲁棒性研究不足，现有攻击依赖特定生成模型或严重降质
- 🔬 **研究方法**：发现水印图像的潜表示与嵌入噪声强相关，提出 Noise-Latent Alignment Score 并优化去相关潜表示同时保语义；MarkNull-A 蒸馏为单次前向攻击
- 📌 **结论**：后处理、微调、初始噪声三类水印上平均比特精度降至 53.14%（近随机 50%），攻陷 Google SynthID-Image 且可迁移到视频水印，0.50s/图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Digital watermarking has emerged as a critical technique for provenance and copyright attribution in AI-generated imagery, yet its robustness against realistic, model-agnostic removal attacks remains poorly explored. Existing attacks either succeed only against specific generative models or achieve removal at the cost of severe visual degradation. In this paper, we propose MarkNull, a model-agnostic watermark removal attack via on-manifold latent manipulation. MarkNull is grounded in a key observation: watermarked images exhibit a strong statistical dependency between the generated latent representation and the embedded initial noise. To quantify this dependency, we introduce the Noise-Latent Alignment Score (NLAS) and formulate an optimization objective that selectively decorrelates the latent representation from the embedded watermark while preserving semantic fidelity. Extensive evaluations across different categories of watermarking paradigms, including post-hoc, fine-tuning-based, and initial-noise-based schemes, demonstrate that MarkNull reduces average bit accuracy to 53.14%, approaching random-guessing (50%), without perceptible image degradation. To further improve scalability, we propose MarkNull-A, an amortized, optimization-free variant that distills the attack into a single forward pass, achieving 0.50 s/image with modest computational overhead. Notably, our attacks successfully compromise Google's SynthID-Image system while preserving high visual quality and transfer effectively to video watermarking. Finally, we present an attack detection mechanism as a defensive counterpart to MarkNull and MarkNull-A, highlighting the necessity of developing watermark designs resilient to model-agnostic latent-space attacks.

</details>

### 53. On Improving Robustness of Deepfake Image Detectors

📄 [arXiv](https://arxiv.org/abs/2606.02797) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shahjahan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`detection`、`deepfake detection`、`domain shift`、`robustness`、`deepfake`

👤 **作者**：Abu Taib Mohammed Shahjahan、Mohammad Mannan、Abdessamad Ben Hamza、Amr Youssef

- 🎯 **研究动机**：最新 deepfake 检测器在对抗攻击下仍大幅退化，此前 IEEE SP 2024 等工作已证实这一点
- 🔬 **研究方法**：融合 DCT 四阶矩池化、噪声残差内容无关特征与 patch 级语义破坏三原则，利用对抗攻击难以约束高阶残差频谱（尤其峰度）的盲区构建统一框架
- 📌 **结论**：六种检测器上一致提升鲁棒性，recall 退化最多降低 88.9%，将 CVPR 2025 最佳检测器受攻击准确率从 81.9% 提到 97.15%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Generative AI has introduced remarkable opportunities while simultaneously raising critical concerns regarding content authenticity. While recent work has increasingly focused on improving the generalization of deepfake detectors across unseen generative models, their robustness against adversarial attacks remains limited. In particular, Abdullah et al. (IEEE SP 2024) evaluated eight detectors and demonstrated that most of them exhibit significant performance degradation under adversarial attacks. We also observed the same phenomenon by testing seven most recent state-of-the-art detectors. To address this problem, we propose a unified framework that integrates three complementary design principles without relying on adversarial training data: (i) higher-order statistical modeling in the frequency domain via Discrete Cosine Transform (DCT)-based moment pooling up to fourth order, (ii) content-agnostic feature representations derived from noise residuals, and (iii) cross-scene generalization enforced through patch-level semantic disruption. A key insight underpinning our approach is that adversarial attacks primarily operate on low-order statistics and visual semantics, leaving higher-order residual-frequency characteristics, particularly kurtosis, largely unconstrained. Extensive experiments demonstrate that our method consistently improves robustness across six architecturally diverse detectors. Notably, we achieve up to 88.9% reduction in recall degradation on current adversarial benchmarks, and improve the best-performing recent detector (Yang et al., IEEE CVPR 2025) from 81.9% to 97.15% accuracy under attack. Overall, our method provides a principled, architecture-agnostic approach for improving deepfake detection robustness against current attacks.

</details>

### 54. ORPHEUS: A Separation-Robust Proactive Defense for Singing Voice Conversion

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wei-zhaolin)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`singing voice conversion`、`identity protection`、`source separation`、`model copyright`

👤 **作者**：Zhaolin Wei、…、Zhihong Tian

- 🎯 **研究动机**：现有抗歌声转换的扰动防御针对纯人声设计，攻击者先做源分离时扰动被当作伴奏滤除
- 🔬 **研究方法**：ORPHEUS 联合用 mask 误导与跨轨损失干扰分离模型、异构说话人编码器集成破坏身份、调性和谐约束与心理声学掩蔽优化感知质量
- 📌 **结论**：比最佳基线在两个说话人验证模型上再降身份相似度 8.02% 与 5.61%，防御效果与跨模型迁移更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in singing voice conversion enable realistic cloning of a singer's voice, raising concerns about unauthorized voice misuse. Existing proactive defenses inject imperceptible perturbations to disrupt such conversion, and they are designed for vocal signals rather than mixed music. In real-world scenarios, however, attackers usually obtain mixed music and apply source separation to decompose the mixture into vocal and backing tracks before conversion. Since separation models are trained to distinguish vocals from background components, perturbations are often treated as backing, causing the perturbations to be filtered out. To address this, we present ORPHEUS, the first proactive defense framework tailored for singing voice conversion involving source separation. Specifically, we jointly (i) interfere with the separation model via mask-misguiding and cross-track losses, (ii) disrupt identity information using an ensemble of heterogeneous speaker encoders to enhance transferability, and (iii) optimize perceptual quality through tonality harmony constraints and psychoacoustic masking. To evaluate ORPHEUS, we conduct experiments on two datasets with three source separation models and four singing voice conversion systems. Compared with the best-performing baseline, ORPHEUS further reduces identity similarity by 8.02% and 5.61% on two speaker verification models, respectively, demonstrating consistently stronger defense effectiveness and cross-model transferability.

</details>

### 55. PVMark: Enabling Public Verifiability for LLM Watermarking Schemes

📄 [arXiv](https://arxiv.org/abs/2510.26274) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/duan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`LLM watermarking`、`public verifiability`、`zero-knowledge proof`

👤 **作者**：Haohua Duan、Liyao Xiang、Xin Zhang

- 🎯 **研究动机**：水印检测依赖私钥导致过程对公众不透明，公开密钥又会招致移除攻击
- 🔬 **研究方法**：PVMark 基于零知识证明构建水印检测正确执行的约束（映射、随机数生成、比较、求和），实现不泄露密钥的公开可验证检测插件
- 📌 **结论**：覆盖三种水印方案、三种哈希与四种 ZKP 协议的组合均高效运行，不损害水印性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking schemes for large language models (LLMs) have been proposed to identify the source of the generated text, mitigating the potential threats emerged from model theft. However, current watermarking solutions hardly resolve the trust issue: the non-public watermark detection cannot prove itself faithfully conducting the detection. We observe that it is attributed to the secret key mostly used in the watermark detection -- it cannot be public, or the adversary may launch removal attacks provided the key; nor can it be private, or the watermarking detection is opaque to the public. To resolve the dilemma, we propose PVMark, a plugin based on zero-knowledge proof (ZKP), enabling the watermark detection process to be publicly verifiable by third parties without disclosing any secret key. PVMark hinges upon the proof of `correct execution' of watermark detection on which a set of ZKP constraints are built, including mapping, random number generation, comparison, and summation. We implement multiple variants of PVMark in Python, Rust and Circom, covering combinations of three watermarking schemes, three hash functions, and four ZKP protocols, to show our approach effectively works under a variety of circumstances. By experimental results, PVMark efficiently enables public verifiability on the state-of-the-art LLM watermarking schemes yet without compromising the watermarking performance, promising to be deployed in practice.

</details>

### 56. Robust Watermarks Meet Backdoored Models: Evading Diffusion Semantic Watermarks via Stealthy Backdoor

📄 [arXiv](https://arxiv.org/abs/2608.00543) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-jinyuan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`diffusion watermark`、`backdoor`、`watermark evasion`、`semantic watermark`、`VAE backdoor`

👤 **作者**：Jinyuan Liu、…、Xiaoyun Wang

- 🎯 **研究动机**：语义水印的检测管线依赖 VAE 等神经网络，其后门攻击面未被研究
- 🔬 **研究方法**：GhostVAE 两阶段在 VAE 编码器植入隐蔽后门：功率谱正则构造通用触发器，再用参数对齐目标训练后门编码器以逃避水印检测
- 📌 **结论**：对三种 SOTA 语义水印与三种 LDM，良性图像 TPR 保持 94.4% 的同时触发后平均 ASR 达 94.6%，17 种防御下在输入/参数/潜空间均隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although semantic watermarking is considered a promising safeguard for images generated by Latent Diffusion Models (LDMs), the reliance of the watermark detection pipeline on neural networks introduces a critical yet underexplored backdoor attack surface. To systematically study this vulnerability, we propose GhostVAE to plant a stealthy backdoor into the encoder of Variational Autoencoder (VAE), enabling reliable evasion of watermark detection. GhostVAE operates in two stages: it first constructs a universal trigger via power spectrum regularization to improve the trigger robustness, and then trains a backdoored VAE encoder with a parameter-aligned objective. Through extensive evaluations across three state-of-the-art semantic watermarking schemes and three widely adopted LDMs, we show that GhostVAE preserves watermark detection performance on benign images (achieving an average true positive rate of 94.4%), while simultaneously enabling highly effective evasion under trigger activation (achieving an average attack success rate of 94.6%). Moreover, we comprehensively analyze seventeen representative defenses and demonstrate that GhostVAE remains stealthy across the input space, parameter space, and latent space. Our work fundamentally undermines the trustworthiness of semantic watermarking systems and highlights that secure deployment of semantic watermarks requires end-to-end security considerations, particularly for neural network components.

</details>

### 57. The Prompt Stealing Fallacy: Rethinking Metrics, Attacks, and Defenses

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/deng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`defense`、`prompt stealing`、`evaluation metric`、`PromptThief`、`content watermark`

👤 **作者**：Zehang Deng、…、Yang Xiang

- 🎯 **研究动机**：提示窃取攻击的评测指标只依赖文本或图像模态的语义相似度，无法忠实衡量攻击的真实有效性
- 🔬 **研究方法**：提出 Style Similarity 与 Prompt Significance 新指标并据此重评现有 PSA；提出强化学习引导的黑盒攻击 PromptThief，并给出对抗样本主动防御与特征级提示水印被动防御
- 📌 **结论**：现有白盒与黑盒 PSA 并不如所报有效，尤其难恢复高贡献提示词；PromptThief 全面超越基线；主动防御对自适应攻击鲁棒性有限，提示水印在多种图像变换下检测稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models are increasingly embedded in creative workflows, where well-crafted prompts function as valuable forms of intellectual property (IP). However, these models are susceptible to prompt stealing attacks (PSAs), where adversaries aim to reconstruct the original prompts used to generate images. In this paper, 1) we identify key shortcomings in current evaluation practices and propose two improved metrics: Style Similarity (SS) and a novel Prompt Significance (PS) score, which together provide a more faithful assessment of PSA effectiveness. Rather than existing metrics that rely solely on semantic similarity between original and stolen information across text or image modalities, the new metrics PS and SS assess attack effectiveness with a more practical focus by explicitly accounting for the importance of modifiers and the style replication of images generated from stolen prompts. 2) Through extensive evaluation using these metrics, we find that existing PSA methods, ranging from soft prompt stealing in white-box settings to hard prompt stealing in black-box settings, are not as effective as reported, especially in recovering high-contribution prompt components. We attribute this to fundamental constrains: white-box methods suffer from mismatched optimization objectives that poorly align with token-level visual semantics, while black-box approaches experience severe information loss due to their decoupling from the target T2I model's generation process. 3) We further introduce PromptThief, a black-box PSA framework that addresses the information loss in prior methods by leveraging reinforcement learning with STS and SS to guide high token-level contribution recovery. PromptThief significantly outperforms existing baselines across multiple metrics and real-world scenarios. 4) We propose and evaluate two defense mechanisms: an adversarial-example-based active approach and a passive scheme through feature-level prompt watermarking. Our evaluation reveals that the active defense offers only limited robustness against adaptive PSAs, highlighting the need for further exploration in this direction. In contrast, the passive watermarking scheme demonstrates strong and consistent detection performance, even under various image transformations, offering a practical and reliable path forward for prompt IP protection.

</details>

### 58. Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI

📄 [arXiv](https://arxiv.org/abs/2603.07466) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/jin)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`proprietary AI`、`computation integrity`、`TEE auditing`

👤 **作者**：Heng Jin、…、Wenjing Lou

- 🎯 **研究动机**：密码学验证成本过高、TEE 内存受限，云上微调与推理的计算完整性无法被实用审计
- 🔬 **研究方法**：AFTUNE 以轻量记录加抽查生成可验证执行轨迹，客户端在 TEE 内验证仅覆盖小部分模型与轨迹的采样执行块
- 📌 **结论**：以适度开销使客户端可实际审计云上微调与推理是否遵循约定配置

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cloud-based infrastructure has become the dominant platform for deploying large models, particularly large language models (LLMs). Fine-tuning and inference are increasingly delegated to cloud providers for simplified deployment and access to proprietary models, yet this creates a fundamental trust gap. Although cryptographic and TEE-based verification approaches exist, prohibitive proving costs and limited TEE memory prevent them from scaling to modern LLMs, leaving clients unable to practically audit these processes. This lack of transparency creates concrete security risks that can silently compromise service integrity. We present AFTUNE, an auditable and verifiable framework that ensures the computational integrity of cloud-based fine-tuning and inference. AFTUNE incorporates a lightweight recording and spot-check mechanism that produces verifiable traces of execution. These traces enable clients to later audit whether the fine-tuning and inference processes followed the agreed configurations, by verifying sampled execution blocks inside a TEE, each covering only a small portion of the model and the execution trace. Our evaluation shows that AFTUNE adds modest overhead and makes auditing practical for clients.

</details>

### 59. VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2606.12263) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/qiu-chunlin)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`latent diffusion model`、`unauthorized mimicry`、`identity protection`、`model copyright`

👤 **作者**：Chunlin Qiu、…、Qian Wang

- 🎯 **研究动机**：已有防御用扰动把生成图像引向无关目标，依赖扰动能在 LDM 长生成过程中保持欺骗效力的无根据假设；模型自身修复机制会使身份重新出现
- 🔬 **研究方法**：提出 VOID：放大潜编码误差击碎语义结构并对抗目标引导信号压制模型修复能力，操纵 LDM 固有随机性，扰动限于人类不可感知区域
- 📌 **结论**：对 24 个 SOTA 防御、10 种模仿攻击、5 个数据集评估，平均 FID 从 113 升至 365，比此前最强防御高 223%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Latent Diffusion Models (LDMs) have revolutionized visual synthesis, they are increasingly exploited for unauthorized mimicry of individuals. Existing defenses inject deceptive perturbations to steer the generated images toward irrelevant targets. However, this approach hinges on an ungrounded assumption: subtle perturbations can maintain their deceptive efficacy throughout an LDM's extensive generation process. In reality, the model's innate restoration mechanism will remove such perturbations and cause individual identities to re-emerge in the images generated. We propose VOID, a defense framework that overcomes this conundrum by manipulating an LDM's intrinsic stochasticity. VOID perturbs the diffusion pipeline in two novel ways: 1) amplifying the latent encoding errors to shatter an image's semantic structure, and 2) counteracting the target guidance signals to suppress the model's restoration capabilities. This results in a semantic corruption that thwarts any unauthorized mimicry. Notably, the security gain does not come at the price of visual utility, as VOID simultaneously manages to confine perturbations to human-imperceptible regions of protected images. Our comprehensive evaluation of 24 state-of-the-art defenses against 10 mimicry attacks on 5 datasets demonstrates VOID's unprecedented protection power: it increases the average Frechet Inception Distance (FID) from 113 to 365, a 223% improvement over the strongest defense to date.

</details>
### 对抗样本、多模态与物理攻击

### 60. Adversarial Patch EXterminator: Zero-Shot and Patch-Agnostic Defense Framework Against Adversarial Patch Attacks

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-jiayimei)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`adversarial patch`、`zero-shot localization`、`image inpainting`、`adversarial robustness`、`robust training`

👤 **作者**：Jiayimei Wang、Tao Ni、Guowen Xu、Qingchuan Zhao、Cong Wang

- 🎯 **研究动机**：现有对抗 patch 防御依赖先验知识或大量训练数据，对微小、不规则或背景高度一致的 patch 防护不足，物理条件变化下稳健性差
- 🔬 **研究方法**：提出零样本、patch 无关的三阶段防御 APEX：边界框提取聚焦 patch 区域，互信息模糊热图加边缘感知边界热图定位对抗区域，结构引导图像修复还原图像
- 📌 **结论**：有效防御非自然、自然与红外等多类对抗 patch，定位能力优异，在光照变化与物理场景中保持高鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial patch attacks pose a serious threat to modern computer vision systems. Although existing defense solutions attempt to mitigate such attacks by developing certifiable models or patch identification pipelines, they generally rely on prior knowledge or extensive training data, show insufficient robustness across varying physical conditions, and present limited performance against challenging cases (e.g., tiny, irregular, or highly background-coherent patches). To address such limitations, we propose APEX, a zero-shot, patch-agnostic three-stage adversarial patch defense framework. Specifically, APEX first concentrates patch regions through bounding-box extraction, then integrates a mutual information-based blur heatmap with an edge-aware boundary heatmap to locate adversarial regions, and finally leverages structure-guided image inpainting to restore the image. Our experiments on multiple datasets and existing state-of-the-art defense methods demonstrate that APEX can effectively defend against various types of adversarial patches (e.g., non-naturalistic, naturalistic, and infrared images). In addition, APEX shows superior capability in patch localization, maintains high robustness against varying environments (e.g., lighting conditions) and extreme cases, and also demonstrates high performance in protecting various models in physical-world scenarios.

</details>

### 61. From Zero to Hero: Cross-modal-enhanced Adversarial Item Promotion Attack against Multimodal Recommender Systems

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yao-zero)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`multimodal recommender`、`item promotion`、`cross-modal perturbation`、`adversarial robustness`

👤 **作者**：Mengyu Yao、…、Ding Li

- 🎯 **研究动机**：对抗商品推广攻击只针对单模态推荐器，VLM 攻击不优化排序目标，多模态推荐器（MRS）漏洞未探
- 🔬 **研究方法**：CREAM 黑盒下联合扰动视觉与文本并保持语义一致，集成视觉扰动器、文本生成器与联合优化控制器
- 📌 **结论**：平均 top-10/top-50 曝光提升 5.75x/2.89x 且多维不可感知；试探的防御策略均有局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal recommender systems (MRSs) jointly leverage visual and textual item representations to determine item ranking and exposure in modern online platforms. Their strong dependence on item content, however, introduces new security risks. In particular, malicious sellers can conduct the adversarial item promotion (AIP) attack to manipulate item content to deceive the recommender into overranking specific items. When it succeeds, the promoted items gain disproportionately higher exposure, leading to significant market visibility and direct economic gain. However, existing AIP research primarily targets unimodal recommenders, leaving the unique vulnerabilities of MRSs largely unexplored. Meanwhile, multimodal adversarial attacks for vision–language models (VLMs) optimize objectives unrelated to ranking and lack cross-modal coordination unique to MRSs. To bridge this gap, we propose CREAM (CRoss-modal-Enhanced AIP attack against MRSs). Our key insight is to jointly perturb multiple modalities in a semantically consistent manner}. We integrate a tailored visual perturbator, a text generator, and a joint optimization controller to fully exploit cross-modal correlations in a black-box setting. Our comprehensive evaluation shows that CREAM significantly outperforms existing methods, achieving on average 5.75x and 2.89x higher exposure at top-10 and top-50 metrics, and demonstrates robustness under evolving real-world conditions. This exposes a tangible economic risk to recommender platforms. Meanwhile, CREAM maintains high imperceptibility across visual, textual, and cross-modal dimensions. We further investigate several potential defense strategies and demonstrate their limitations, highlighting the urgent need for stronger protections against adversarial threats in MRSs.

</details>

### 62. Low-Cost Hard-Label Adversarial Attack with Theoretical Foundations

📄 [arXiv](https://arxiv.org/abs/2601.14300) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-jun)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`hard-label model`、`query efficiency`、`decision boundary`、`adversarial robustness`

👤 **作者**：Jun Liu、Leo Yu Zhang、Fengpeng Li、Isao Echizen、Jiantao Zhou

- 🎯 **研究动机**：现有硬标签攻击忽视初始化作用且依赖经验启发、缺理论保证
- 🔬 **研究方法**：统一理论框架证明符号翻转类攻击是真实梯度符号的近似；提出零查询初始化与 Pattern-Driven Optimization，理论保证更高余弦相似度与更低查询复杂度
- 📌 **结论**：CIFAR-10、ImageNet、ObjectNet 等上成功率和效率超 SOTA（低预算尤甚），绕过 Blacklight 防御检出率为 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hard-label black-box attacks, relying solely on top-1 predictions, represent one of the most challenging yet practically threat models. Despite recent progress, existing approaches face two key limitations: (1) they overlook the critical role of initialization, focusing primarily on optimization strategies; and (2) they rely heavily on empirical heuristics without theoretical guarantees. To bridge this gap, we establish a unified theoretical framework showing that existing sign-flipping hard-label attacks can be understood as approximating the true gradient sign. Guided by this {principled analysis}, we propose a novel attack framework featuring a zero-query initialization strategy and a Pattern-Driven Optimization (PDO) algorithm. We provide theoretical guarantees that our initialization yields higher cosine similarity to the true gradient sign than random baselines, and our PDO module achieves significantly lower query complexity than baseline search methods. Extensive experiments across CIFAR-10, ImageNet, and ObjectNet—covering standard and adversarially trained models, commercial APIs, and CLIP models—demonstrate that our method consistently outperforms SOTA hard-label attacks in both success rate and efficiency, particularly under low query budgets. Furthermore, our method demonstrates robust generalization across corrupted data (ImageNet-C), biomedical images (PathMNIST), and dense prediction tasks such as segmentation. Notably, it bypasses the stateful defense Blacklight, achieving a 0% detection rate.

</details>

### 63. On Evaluating the Robustness of Large Vision-Language Models via Untargeted Modality Alignment Breaking Adversarial Attack

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-zhichao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`benchmark`、`vision-language model`、`modality alignment`、`black-box transfer`、`adversarial robustness`

👤 **作者**：Zhichao Li、…、Chun Chen

- 🎯 **研究动机**：现有迁移攻击只扰动视觉编码器且忽视无目标场景，对 LVLM 黑盒鲁棒性评估有限
- 🔬 **研究方法**：MABA 同时攻击视觉编码与模态对齐两阶段：以抑制判别性视觉表示为显式优化目标，加互信息感知投影器作代理对齐模块破坏跨模态一致性
- 📌 **结论**：达到 SOTA，图像描述任务语义指标平均下降 58.37%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have achieved remarkable success in multimodal tasks by aligning the representation space of visual encoders to that of the LLMs. However, they remain vulnerable to transferable adversarial attacks, which can manipulate the LVLMs' output without accessing the model. Ensuring their reliable deployment thus requires a rigorous evaluation of black-box robustness. Current methods provide a limited assessment by perturbing only the visual encoder of LVLMs and often neglect untargeted attack scenarios. In this work, we propose the Modality Alignment Breaking Attack (MABA), a novel transferable, untargeted adversarial attack for evaluating the black-box robustness of LVLMs. MABA emphasizes disrupting the entire multimodal pipeline, targeting two key phases: visual encoding and modality alignment. First, MABA reveals that the core of transferable adversarial attacks lies in suppressing discriminative visual representations and explicitly uses this as an optimization objective to improve transferability across different LVLMs. Second, MABA introduces a mutual-information-aware projector that acts as a surrogate modality alignment module of LVLMs, effectively breaking cross-modal consistency and enhancing the transferability. Extensive evaluations demonstrate that MABA achieves state-of-the-art performance, leading to an average 58.37% drop in semantic metrics for the image caption task. Through ablation studies on diverse LVLM families, we derive valuable insights into strengthening the robustness of LVLMs.

</details>

### 64. Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

📄 [arXiv](https://arxiv.org/abs/2603.13847) · 🌐 [Project](https://swhisper-jailbreak.github.io/) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/ling)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`speech-driven LLM`、`ultrasonic jailbreak`、`physical-world attack`、`near-ultrasound`、`microphone nonlinearity`

👤 **作者**：Zijian Ling、…、Bin Benjamin Zhu

- 🎯 **研究动机**：语音接口给 speech-driven LLM 引入开放声学通道的隐蔽攻击面
- 🔬 **研究方法**：SWhisper 把任意目标音频编码为近超声波，经非线性信道建模与信道反转预补偿在商用设备上无声还原，配语音感知的越狱生成保证可懂、简洁与迁移
- 📌 **结论**：商业模型上非拒答率达 0.94、specific-convincing 达 0.925，用户实验中注入音频与纯背景播放感知不可分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks against speech-driven LLMs under realistic black-box conditions using commodity hardware. SWhisper enables robust, inaudible delivery of arbitrary target baseband audio-including long and structured prompts-on commodity devices by encoding it into near-ultrasound waveforms that demodulate faithfully after acoustic transmission and microphone nonlinearity. This is achieved through a simple yet effective approach to modeling nonlinear channel characteristics across devices and environments, combined with lightweight channel-inversion pre-compensation. Building on this high-fidelity covert channel, we design a voice-aware jailbreak generation method that ensures intelligibility, brevity, and transferability under speech-driven interfaces. Experiments across both commercial and open-source speech-driven LLMs demonstrate strong black-box effectiveness. On commercial models, SWhisper achieves up to 0.94 non-refusal (NR) and 0.925 specific-convincing (SC). A controlled user study further shows that the injected jailbreak audio is perceptually indistinguishable from background-only playback for human listeners. Although jailbreaks serve as a case study, the underlying covert acoustic channel enables a broader class of high-fidelity prompt-injection and commandexecution attacks.

</details>

### 65. VIPER Strike: Defeating Visual Reasoning CAPTCHAs via Structured Vision–Language Inference

📄 [arXiv](https://arxiv.org/abs/2601.06461) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/qi-minfeng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`visual reasoning CAPTCHA`、`VLM solver`、`automation`、`VLM safety`、`cyber misuse`

👤 **作者**：Minfeng Qi、Dongyang He、Qin Wang、Lefeng Zhang

- 🎯 **研究动机**：现有视觉推理 CAPTCHA 求解器要么依赖模板专用检测器、要么缺细粒度视觉感知，均无通用性
- 🔬 **研究方法**：ViPer 模块化流水线：解析视觉布局、把属性接地到问题语义并推断目标坐标，融合结构化多目标感知与自适应 LLM 推理
- 📌 **结论**：六大 VRC 供应商上成功率最高 93.2%，超 GraphNet（83.2%）与 Oedipus（65.8%）等基线，跨 LLM 骨干保持 90% 以上；所提 Template-Space Randomization 可削弱求解器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual Reasoning CAPTCHAs (VRCs) combine visual scenes with natural-language queries that demand compositional inference over objects, attributes, and spatial relations. They are increasingly deployed as a primary defense against automated bots. Existing solvers fall into two paradigms: vision-centric, which rely on template-specific detectors but fail on novel layouts, and reasoning-centric, which leverage LLMs but struggle with fine-grained visual perception. Both lack the generality needed to handle heterogeneous VRC deployments. We present ViPer, a unified attack framework that integrates structured multi-object visual perception with adaptive LLM-based reasoning. ViPer parses visual layouts, grounds attributes to question semantics, and infers target coordinates within a modular pipeline. Evaluated on six major VRC providers (VTT, Geetest, NetEase, Dingxiang, Shumei, Xiaodun), ViPer achieves up to 93.2% success, approaching human-level performance across multiple benchmarks. Compared to prior solvers, GraphNet (83.2%), Oedipus (65.8%), and the Holistic approach (89.5%), ViPer consistently outperforms all baselines. The framework further maintains robustness across alternative LLM backbones (GPT, Grok, DeepSeek, Kimi), sustaining accuracy above 90%. To anticipate defense, we further introduce Template-Space Randomization (TSR), a lightweight strategy that perturbs linguistic templates without altering task semantics. TSR measurably reduces solver (i.e., attacker) performance. Our proposed design suggests directions for human-solvable but machine-resistant CAPTCHAs.

</details>

### 66. What the Eyes See, the LLMs Miss: Exploiting Human Perception for Adversarial Text Attacks

📄 [arXiv](https://arxiv.org/abs/2606.09700) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yang-qin)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`content moderation`、`typographic evasion`、`human perception`、`VLM robustness`、`visual illusion`

👤 **作者**：Qin Yang、…、Yuan Hong

- 🎯 **研究动机**：LLM 内容审核只处理 token 化文本，忽略人类解读内容所用的视觉线索，人类可见的有害内容可绕过自动审核
- 🔬 **研究方法**：提出 HPAA：用间距、强调、空间排布等排版操纵把有害表达嵌入良性文本，黑盒小查询预算下自动生成规避内容
- 📌 **结论**：13 个主流审核系统（含商业 API 与开源护栏）上仅 3 次查询即实现 >86% 人类识别率而检测率低于 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-powered content moderation systems are a critical defense against harmful online content. However, they operate primarily on tokenized text and often overlook visual cues that humans naturally use when interpreting content. We show that this limitation creates a fundamental vulnerability: content readily recognized as harmful by humans can evade automated moderation. To systematically study this problem, we introduce Human-Perceptible Adversarial Attacks (HPAA), which embed harmful expressions into otherwise benign text using visually salient typographic manipulations. HPAA strategically combines features such as spacing, emphasis, and spatial arrangement to preserve human recognition while reducing machine detectability. Operating in a black-box setting with a small query budget, the attack automatically generates evasive content without model access or gradient information. We evaluate HPAA on multiple datasets and thirteen widely deployed moderation systems, including commercial APIs and state-of-the-art open-source guardrails. With only three detector queries, generated attacks achieve over 86\% human recognition while keeping detection rates below 1\% across evaluated systems. We further identify the typographic factors driving successful evasion, analyze why current moderation architectures fail to capture these signals, and discuss practical defenses. Our findings reveal a fundamental blind spot in current LLM-based moderation systems and motivate moderation approaches that better align with human perceptual understanding.

</details>
### AI 滥用、网络能力与部署治理

### 67. "Abuse Risks are Often Inherent to Product Features": Exploring AI Vendors' Bug Bounty and Responsible Disclosure Policies

📄 [arXiv](https://arxiv.org/abs/2509.06136) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/piao)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`AI vulnerability disclosure`、`bug bounty`、`abuse risk`、`jailbreak`

👤 **作者**：Yangheran Piao、Jingjie Li、Daniel W. Woods

- 🎯 **研究动机**：AI 漏洞披露依赖厂商接收并奖励报告，但厂商政策与学术研究、真实事件的差距未被测量
- 🔬 **研究方法**：混合方法分析 264 家 AI 厂商的漏洞披露政策（快照与纵向定性），并与 320 起 AI 事件及 260 篇学术论文对齐
- 📌 **结论**：36% 厂商无既定政策、仅 18% 提及 AI 风险；数据访问、授权与模型提取最常被列入范围，越狱与幻觉最常被排除；厂商处置 AI 漏洞可能滞后于学术与事件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As vendors adopt AI technologies, security researchers are working to uncover and fix related vulnerabilities, which is important given AI systems handle sensitive data and critical functions. This process relies on vendors receiving and rewarding AI vulnerability reports. To assess current practices, we analyzed the vulnerability disclosure policies of 264 AI vendors. We employed a mixed-methods approach, combining snapshot and longitudinal qualitative analysis, as well as comparing alignment with 320 AI incidents and 260 academic articles. Our analysis reveals that 36% of AI vendors have no established policy, and only 18% mention AI risks. Data access, authorization, and model extraction vulnerabilities are most consistently declared in-scope. Jailbreaking and hallucination are most commonly declared out-of-scope. We identify three profiles that reflect vendors' different positions toward AI vulnerabilities: proactive clarification (n = 46), silent (n = 115), and restrictive (n = 103). Our alignment results suggest that vendors may address AI vulnerability disclosure later than academic research and real-world incidents.

</details>

### 68. A Large-Scale Study of Personalized Phishing using Large Language Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/czybik)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`LLM misuse`、`spear phishing`、`personalization`

👤 **作者**：Stefan Czybik、Anne Josiane Kouam、Peter Heubl、Jan Magnus Nold、Konrad Rieck

- 🎯 **研究动机**：LLM 可支撑通用钓鱼已被证明，但个性化攻击的规模化潜力从未被量化
- 🔬 **研究方法**：在 7,700 名参与者的实验中，以目标邮箱为查询经网络搜索收集个人信息并自动生成逐人定制邮件
- 📌 **结论**：LLM 鱼叉式钓鱼点击率约为通用策略的三倍（无论通用邮件由人写还是 LLM 写），个性化成本仅约 $0.03/封——须限制可经邮箱关联的公开信息并将其纳入意识培训

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) can generate fluent and persuasive text, making them valuable tools for communication. However, this capability also renders them attractive for malicious purposes. While several studies have shown that LLMs can support generic phishing, their potential for personalized attacks at scale has not been explored and quantified yet. In this study, we thus evaluate the effectiveness of LLM-based spear phishing in an experiment with 7700 participants. Using the target email addresses as queries, we collect personal information through web searches and automatically generate emails tailored to each participant. Our findings reveal a concerning situation: LLM-based spear phishing almost triples the click rate compared to generic phishing strategies. This effect is consistent, regardless of whether the generic emails are written by humans or generated by LLMs as well. Moreover, the cost of personalization is minimal, with approximately $0.03 per email. Given that phishing is still a major attack vector against IT infrastructures, we conclude that there is a pressing need to strengthen existing defenses, for example, by limiting publicly available information linkable to email addresses and incorporating personalized phishing into awareness trainings.

</details>

### 69. Assessing LLM Response Quality in the Context of Technology-Facilitated Abuse

📄 [arXiv](https://arxiv.org/abs/2602.17672) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/prakash)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`technology-facilitated abuse`、`LLM response safety`、`survivor support`、`cyber misuse`

👤 **作者**：Vijay Prakash、Majed Almansoori、Donghan Hu、Rahul Chatterjee、Danny Yuxing Huang

- 🎯 **研究动机**：技术媒介虐待幸存者可能先咨询 LLM 聊天机器人，其回复质量缺乏专家与幸存者视角的评估
- 🔬 **研究方法**：专家主导人工评估两个通用与两个 IPV 领域模型对真实 TFA 问题的零样本单轮回复，并开展幸存者参与的用户研究
- 📌 **结论**：揭示当前 LLM 在 TFA 场景的能力与局限，并给出面向幸存者支持的具体改进建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Technology-facilitated abuse (TFA) is a pervasive form of intimate partner violence (IPV) that leverages digital tools to control, surveil, or harm survivors. While tech clinics are one of the reliable sources of support for TFA survivors, they face limitations due to staffing constraints and logistical barriers. As a result, many survivors turn to online resources for assistance. With the growing accessibility and popularity of large language models (LLMs), and increasing interest from IPV organizations, survivors may begin to consult LLM-based chatbots before seeking help from tech clinics. In this work, we present the first expert-led manual evaluation of four LLMs - two widely used general-purpose non-reasoning models and two domain-specific models designed for IPV contexts - focused on their effectiveness in responding to TFA-related questions. Using real-world questions collected from literature and online forums, we assess the quality of zero-shot single-turn LLM responses generated with a survivor safety-centered prompt on criteria tailored to the TFA domain. Additionally, we conducted a user study to evaluate the perceived actionability of these responses from the perspective of individuals who have experienced TFA. Our findings, grounded in both expert assessment and user feedback, provide insights into the current capabilities and limitations of LLMs in the TFA context and may inform the design, development, and fine-tuning of future models for this domain. We conclude with concrete recommendations to improve LLM performance for survivor support.

</details>

### 70. From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-tingxuan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`AI cyber capability`、`CTF agent`、`human-in-the-loop`、`cyber misuse`

👤 **作者**：Tingxuan Tang、…、Yue Xiao

- 🎯 **研究动机**：现有 AI CTF 评测孤立评估单题求解，人类玩家对 AI 辅助的感知、协作方式及人机组合与全自主 agent 的对比是知识空白
- 🔬 **研究方法**：首个现场 CTF 的 AI 辅助实证研究：41 名参与者的感知与信任变化及协作分析，并在同一新题集上基准测试四个自主 CTF agent
- 📌 **结论**：AI 素养与领域知识互补且各有不可替代优势；尽管自主 agent 表现出色，human-in-the-loop 是制胜范式——AI 加速探索、人类提供定向指导与验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Capture-the-Flag (CTF) competitions are increasingly becoming a testbed for evaluating AI capabilities at solving security tasks, due to their controlled environments and objective success criteria. Existing evaluations have focused on how successful AI is at solving individual CTF challenges in isolation from human CTF players. As AI usage increases in both academic and industrial settings, it is equally likely that human CTF players may collaborate with AI agents to solve CTF challenges. This possibility exposes a key knowledge gap: how do human players perceive AI CTF assistance; when assistance is provided, in what ways do they collaborate and is it effective with respect to human performance; how do humans assisted by AI compare to the performance of fully autonomous AI agents on the same set of challenges. We address this gap with the first empirical study of AI assistance in a live, onsite CTF. In a study with 41 participants (out of the total 95 that participated in the CTF), we qualitatively study (i) how participants' perception, trust, and expectations shift before versus after hands-on AI use, and (ii) how participants collaborate with an instrumented AI assistant. Moreover, we also (iii) benchmark four autonomous CTF agents on the same fresh challenge set to compare outcomes with human teams and analyze agent trajectories. We find that, for human players, AI literacy and domain knowledge are complementary competencies, and both have irreplaceable advantages. Proficient and efficient use of AI amplifies professional skills. Importantly, although advanced autonomous agents showed outstanding performance, human-in-the-loop is the winning paradigm where AI accelerates exploration while humans provide targeted guidance and verification. We conclude with implications for the future design of CTF competitions and for building effective human-in-the-loop AI systems for security.

</details>

### 71. GoodVibe: Security-by-Vibe for LLM-Based Code Generation

📄 [arXiv](https://arxiv.org/abs/2602.10778) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/thang)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`code generation`、`neuron-level tuning`、`secure code`、`cyber misuse`、`offensive capability`

👤 **作者**：Maximilian Thang、…、Ahmad-Reza Sadeghi

- 🎯 **研究动机**：vibe coding 场景安全需求不明确，模型常产出功能正确但不安全的代码；全参微调代价高且易灾难遗忘
- 🔬 **研究方法**：GoodVibe 基于梯度归因定位安全关键神经元子集，仅更新该子集并用激活驱动聚类降低训练成本，在 6 个 LLM 上评估
- 📌 **结论**：代码安全性最高提升 2.5 倍，可训练参数比全参微调少 4700 倍以上，训练计算比 LoRA 低 3.6 倍以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for code generation in fast, informal development workflows, often referred to as vibe coding, where speed and convenience are prioritized, and security requirements are rarely made explicit. In this setting, models frequently produce functionally correct but insecure code, creating a growing security risk. Existing approaches to improving code security rely on full-parameter fine-tuning or parameter-efficient adaptations, which are either costly and prone to catastrophic forgetting or operate at coarse granularity with limited interpretability and control. We present GoodVibe, a neuron-level framework for improving the security of code language models by default. GoodVibe is based on the key insight that security-relevant reasoning is localized to a small subset of neurons. We identify these neurons using gradient-based attribution from a supervised security task and perform neuron-selective fine-tuning that updates only this security-critical subspace. To further reduce training cost, we introduce activation-driven neuron clustering, enabling structured updates with minimal overhead. We evaluate GoodVibe on six LLMs across security-critical programming languages, including C++, Java, Swift, and Go. GoodVibe substantially improves the security of generated code while preserving general model utility, achieving up to a 2.5x improvement over base models, achieving performance competitive with full fine-tuning while using over 4,700x fewer trainable parameters, and reducing training computation by more than 3.6x compared to the parameter-efficient baseline (LoRA). Our results demonstrate that neuron-level optimization offers an effective and scalable approach to securing code generation without sacrificing generality.

</details>

### 72. Love, Lies, and Language Models: Investigating AI's Role in Romance-Baiting Scams

📄 [arXiv](https://arxiv.org/abs/2512.16280) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gressel)　📅 2026　🏷 USENIX Security 2026

**关键词**：`analysis`、`LLM misuse`、`romance-baiting`、`safety filter`、`scam automation`、`dual-use risk`

👤 **作者**：Gilad Gressel、…、Yisroel Mirsky

- 🎯 **研究动机**：杀猪盘等 romance-baiting 诈骗本质是文本密集型，LLM 全自动化的现实风险与防御缺口不明
- 🔬 **研究方法**：访谈 145 名业内人员与 5 名受害者，开展 LLM 诈骗 agent 与人类操盘手的盲测长期对话研究，并评测商业安全过滤器
- 📌 **结论**：87% 诈骗劳动属可自动化的对话任务；LLM agent 赢得更高信任（p=0.007）、请求依从率 46%（人类 18%）；主流安全过滤器对 romance-baiting 对话检出率为 0.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Romance-baiting scams have become a major source of financial and emotional harm worldwide. These operations are run by organized crime syndicates that traffic thousands of people into forced labor, requiring them to build emotional intimacy with victims over weeks of text conversations before pressuring them into fraudulent cryptocurrency investments. Because the scams are inherently text-based, they raise urgent questions about the role of Large Language Models (LLMs) in both current and future automation. We investigate this intersection by interviewing 145 insiders and 5 scam victims, performing a blinded long-term conversation study comparing LLM scam agents to human operators, and executing an evaluation of commercial safety filters. Our findings show that LLMs are already widely deployed within scam organizations, with 87% of scam labor consisting of systematized conversational tasks readily susceptible to automation. In a week-long study, an LLM agent not only elicited greater trust from study participants (p=0.007) but also achieved higher compliance with requests than human operators (46% vs. 18% for humans). Meanwhile, popular safety filters detected 0.0% of romance baiting dialogues. Together, these results suggest that romance-baiting scams may be amenable to full-scale LLM automation, while existing defenses remain inadequate to prevent their expansion.

</details>

### 73. PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`autonomous remediation`、`policy constraint`、`risk-bounded agent`、`cyber misuse`

👤 **作者**：Rui Li、Shuang Cao

- 🎯 **研究动机**：脚本化补丁修复安全但僵化，LLM 智能体灵活却常违反维护窗口、爆炸半径限制等变更管理策略
- 🔬 **研究方法**：PatchWeaver 组合持续刷新的 Kubernetes 资产/依赖/审批图谱、把组织变更规则编码为可执行谓词的 ChangeSpec、预测进展与违规风险的 rollout 决策层；短程仿真检测约束陷阱并重规划
- 📌 **结论**：步级违规比工具链基线降 52.5%、比 LLM 智能体基线降 79.1%；攻击压力测试漏报率 0.33%（工具链 28.5%），p99 准入延迟 31ms

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Security teams increasingly rely on automation to keep pace with vulnerability disclosure and patch deployment, yet real remediation workflows are constrained by change-management policies: maintenance windows, staged rollout rules, blast-radius limits, approval gates, and least-privilege requirements. Today, "autonomous" remediation is brittle. Scripted playbooks are safe but rigid, while LLM-driven agents are flexible but frequently violate operational policies (e.g., patching outside windows, taking too many replicas offline, or skipping mandatory validation), creating outages and compliance risk. We present PatchWeaver, a remediation system that provides policy-bounded autonomy. PatchWeaver combines (i) an explicit, continuously refreshed graph of Kubernetes assets, dependencies, identities, vulnerabilities, approvals, and evidence; (ii) a typed policy interface (ChangeSpec) that encodes organization-specific change rules as executable predicates; and (iii) a rollout-based decision layer that scores candidate remediation plans by predicting both progress and policy-violation risk before any action is executed. The core insight is that myopic enforcement cannot avoid constraint traps--states where locally admissible actions lead to dead ends that force later violations. PatchWeaver detects traps via short-horizon simulation and replans when reality diverges from prediction. We evaluate PatchWeaver on four Kubernetes remediation workloads under explicit governance constraints. Compared to a strong toolchain baseline (Gatekeeper + Argo Rollouts + Cosign), PatchWeaver reduces step-level policy violations by 52.5% (4.73% vs. 9.95%, p<0.01) and episode-level violations by 52.2% (5.82% vs. 12.18%). Compared to an LLM-agent baseline, PatchWeaver reduces step violations by 79.1% and worst-case (p99) episode violations by 3.1x (16.8% vs. 51.3%). In security stress tests across 10 attack categories, PatchWeaver achieves 0.33% aggregate miss rate with mean dwell time 0.84 s, separating 88.7% immediate blocks from 11.0% escalations, versus 28.5% miss rate and 96.4 s for the toolchain. Control-plane overhead remains practical: p99 admission latency is 31 ms at 32 policy predicates, and total resource usage is under 1 CPU core and 1 GB memory.

</details>
### 综述、基准与方法论评测

### 74. COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers

📄 [arXiv](https://arxiv.org/abs/2512.02318) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-junyu)　📅 2026　🏷 USENIX Security 2026

**关键词**：`benchmark`、`MLLM CAPTCHA solver`、`structural hardening`、`automation risk`、`VLM safety`、`cyber misuse`

👤 **作者**：Junyu Wang、…、Junjie Xiong

- 🎯 **研究动机**：现成 MLLM 可低成本自动化破解视觉 CAPTCHA，其威胁程度与防御方向不明
- 🔬 **研究方法**：在 18 种真实 CAPTCHA 任务上评测 7 个 MLLM 的单发准确率、重试成功率、延迟与成本，分析推理轨迹并推导任务选择与加固指南
- 📌 **结论**：识别型低交互任务可被人本级成本与延迟破解；加入细粒度定位与隐式计数后 SOTA MLLM 成功率从超 95% 降至 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper studies how multimodal large language models (MLLMs) undermine the security guarantees of visual CAPTCHA. We identify the attack surface where an adversary can cheaply automate CAPTCHA solving using off-the-shelf models. We evaluate 7 representative MLLMs on 18 real-world CAPTCHA task types, measuring single-shot accuracy, success under limited retries, end-to-end latency, and per-solve cost. We further validate our findings through a supplemental external dataset and an adaptive-attacker setting with session memory, while also analyzing the impact of task-specific prompt engineering and few-shot demonstrations on solver effectiveness. We reveal that MLLMs can reliably solve recognition-oriented and low-interaction CAPTCHA tasks at human-like cost and latency, whereas tasks requiring fine-grained localization, multi-step spatial reasoning, or cross-frame consistency remain significantly harder for current models. By examining the reasoning traces of such MLLMs, we investigate the underlying mechanisms of why models succeed/fail on specific CAPTCHA puzzles and use these insights to derive defense-oriented guidelines for selecting and strengthening CAPTCHA tasks. To validate these principles, we present a proof-of-concept by hardening a vulnerable CAPTCHA type using our guidelines. We demonstrate that incorporating fine-grained localization and implicit counting reduces the success rate of state-of-the-art MLLMs from over 95\% to 0\%, confirming that structural changes can effectively mitigate the threat. We conclude by emphasizing the urgent need for CAPTCHA redesign as MLLM capabilities increasingly threaten existing defenses. Code Availability (https://doi.org/10.5281/zenodo.20406852).

</details>

### 75. SoK: Attack and Defense Landscape of Agentic AI Systems

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`agentic AI`、`attack surface`、`defense taxonomy`、`agent security`、`threat model`

👤 **作者**：Juhee Kim、Wenbo Guo、Dawn Song

- 🎯 **研究动机**：LLM 与非 AI 工具组件集成的 agent 系统快速落地，其安全挑战与传统软件系统不同，缺乏系统化梳理
- 🔬 **研究方法**：对 AI agent 安全做知识系统化：分析设计空间、攻击面与防御机制分类，并识别该新兴领域的开放挑战
- 📌 **结论**：给出理解 AI agent 安全风险与防御策略的系统框架，作为构建安全 agent 系统与后续研究的基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents that integrate large language models with non-AI tool components are rapidly emerging in real-world applications, offering unprecedented automation and flexibility. However, this flexibility introduces complex security challenges that differ from traditional software systems. In this paper, we present the first comprehensive systematization of knowledge on AI agent security, analyzing the design space, attack landscape, and defense mechanisms for secure AI agent systems. In addition, we identify open challenges for future research in this emerging domain. Our work provides the first systematic framework for understanding AI agent security risks and defense strategies, serving as a foundation for building secure agentic systems and advancing research in this critical area.

</details>

### 76. SoK: Colluding Adversaries in Machine Learning Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.10091) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/duddu)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`ML pipeline`、`colluding adversary`、`composed attack`、`multi-agent system`

👤 **作者**：Vasisht Duddu、Lipeng He、Asim Waheed、N. Asokan

- 🎯 **研究动机**：不同特征的对手可通过执行一种攻击放大另一种，但 ML 管线中的合谋缺乏系统框架
- 🔬 **研究方法**：提出覆盖训练期-推理期与推理期内部合谋的框架，纳入促成合谋的因素并给出推测指南，实证验证五个未探索合谋案例
- 📌 **结论**：用该框架解释已有工作、预测新合谋并验证成立；对手特征（目标、知识、能力）决定合谋潜力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) models are susceptible to various security, privacy, and fairness risks. Adversaries with different characteristics (i.e., objectives, knowledge, and capabilities) can collude by executing one attack to amplify others. Existing work lacks a systematic framework to explore collusion among adversaries, and to study the implications of the adversaries' characteristics. We present a framework covering collusion (a) between train- and inference-time adversaries, and (b) among inference-time adversaries. Our framework accounts for factors enabling collusion between adversaries. We propose a guideline to conjecture about the potential for collusion using enabling factors. We use it to explain prior work, conjecture about unexplored collusions, and empirically validate five such cases. Finally, we discuss how adversaries' characteristics influence the potential for collusion.

</details>

### 77. SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned

📄 [arXiv](https://arxiv.org/abs/2602.07666) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-cen)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`AI cyber capability`、`autonomous remediation`、`AIxCC`、`cyber misuse`、`offensive capability`

👤 **作者**：Cen Zhang、…、Taesoo Kim

- 🎯 **研究动机**：AIxCC 是最大规模的自主网络推理系统竞赛，缺少系统性的复盘分析
- 🔬 **研究方法**：基于设计文档、源码、执行轨迹与组织者/团队访谈，分析赛制设计、决赛 CRS 架构及榜单之外的结果
- 📌 **结论**：识别出真正驱动 CRS 性能的因素与团队真实技术进展，指出自主 CRS 实际部署的开放局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

DARPA's AI Cyber Challenge (AIxCC, 2023--2025) is the largest competition to date for building fully autonomous cyber reasoning systems (CRSs) that leverage recent advances in AI -- particularly large language models (LLMs) -- to discover and remediate vulnerabilities in real-world open-source software. This paper presents the first systematic analysis of AIxCC. Drawing on design documents, source code, execution traces, and discussions with organizers and competing teams, we examine the competition's structure and key design decisions, characterize the architectural approaches of finalist CRSs, and analyze competition results beyond the final scoreboard. Our analysis reveals the factors that truly drove CRS performance, identifies genuine technical advances achieved by teams, and exposes limitations that remain open for future research. We conclude with lessons for organizing future competitions and broader insights toward deploying autonomous CRSs in practice.

</details>

### 78. SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/alam)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`AI phishing detector`、`security evaluation`、`evolving attack`

👤 **作者**：Mahbub Alam、…、Nitesh Saxena

- 🎯 **研究动机**：AI 钓鱼网站检测研究普遍只报高精度，能否满足演进攻击鲁棒性、良性页多样性、可解释性与隐私等现实要求不明
- 🔬 **研究方法**：提出 PHILTER：LLM 提取证据起草理由、专家验证定稿，按 4 项功能与 3 项安全指标评估 55 个学术方法，并给出特征、相似度、身份与混合四类检测策略分类
- 📌 **结论**：无一研究满足全部功能与安全要求：均未有效应对多样钓鱼战术，多数难保隐私、难适应演进攻击，良性页测试不足易致高误报

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Phishing websites remain a dominant enabler of cybercrime. In response, many academic AI-based phishing website detection methods have been developed, often inspiring the design of real-world systems. Although most studies report high accuracy, it remains unclear whether they meet real-world requirements such as resilience to evolving phishing tactics, robustness on diverse benign pages, interpretability, and privacy. We present PHILTER (PHishing detection literature Inspection via LLMs and Targeted Expert Review), a scalable framework for qualitatively assessing phishing website detection studies across four functionality and three security metrics. PHILTER leverages LLMs to extract evidence and draft rationales, which experts then validate and use to produce the final assessment. Applying it to 55 academic approaches reveals systemic gaps. No study fulfills all functionality and security requirements. None show evidence of effectively addressing diverse phishing tactics. Most approaches struggle to preserve privacy and adapt to evolving attacker strategies, and many risk elevated false alarms in practice due to limited testing on diverse benign pages. We also introduce a taxonomy of detection strategies (feature-based, similarity-based, identity-based, and hybrid) that highlights design trade-offs and helps explain these shortcomings. Our study reveals that accuracy-driven evaluation overlooks blind spots that undermine practical effectiveness and exposes a key open challenge: achieving high accuracy while fulfilling all functionality and security requirements. We provide actionable recommendations to guide the design of future defenses that pursue this simultaneous goal against evolving and adaptive phishing campaigns.

</details>

### 79. Sok: Private Transformer-based Model Inference

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-yuntian)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`private transformer inference`、`MPC`、`standardized evaluation`

👤 **作者**：Yuntian Chen、…、Zhuzhu Wang

- 🎯 **研究动机**：隐私保护 Transformer 推理协议众多、假设与密码工具各异，其计算、通信、精度权衡缺乏统一分析与可比评测
- 🔬 **研究方法**：从多性能视角系统分析现有方法并识别局限与研究空白，评估先前系统的可复现性并在标准化配置下重测代表性方案
- 📌 **结论**：给出不同部署设置下平衡协议权衡的原则性指南

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing demand for privacy-preserving Transformer inference has led to the emergence of numerous protocols designed to protect sensitive data and model parameters. These protocols utilize diverse cryptographic tools under varying assumptions, each presenting unique characteristics and trade-offs between computation, communication, and accuracy. In this paper, we conduct a systematic and in-depth analysis of existing approaches from diverse performance perspectives, identifying their limitations and research gaps. We further evaluate the reproducibility of prior systems and re-benchmark representative solutions under standardized configurations. Our results yield a principled guideline for balancing protocol trade-offs under different deployment settings.

</details>

### 80. SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity

📄 [arXiv](https://arxiv.org/abs/2602.08690) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/mcfadden)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`DRL4Sec`、`methodological pitfall`、`deployment risk`

👤 **作者**：Shae McFadden、…、Fabio Pierazzi

- 🎯 **研究动机**：DRL 从实验室模拟迁移到对抗性网络安全环境会引入大量方法学问题，缺少系统梳理
- 🔬 **研究方法**：系统化环境建模、训练、评估、部署四阶段的 11 类陷阱，分析 2018-2025 年 66 篇论文并在三类安全环境中做对照实验
- 📌 **结论**：平均每篇含 5 个以上陷阱，实验证实其实际影响并给出对应改进建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Reinforcement Learning (DRL) has achieved remarkable success in domains requiring sequential decision-making, motivating its application to cybersecurity problems. However, transitioning DRL from laboratory simulations to bespoke cyber environments can introduce numerous issues. This is further exacerbated by the often adversarial, non-stationary, and partially-observable nature of most cybersecurity tasks. In this paper, we identify and systematize 11 methodological pitfalls that frequently occur in DRL for cybersecurity (DRL4Sec) literature across the stages of environment modeling, agent training, performance evaluation, and system deployment. By analyzing 66 significant DRL4Sec papers (2018-2025), we quantify the prevalence of each pitfall and find an average of over five pitfalls per paper. We demonstrate the practical impact of these pitfalls using controlled experiments in (i) autonomous cyber defense, (ii) adversarial malware creation, and (iii) web security testing environments. Finally, we provide actionable recommendations for each pitfall to support the development of more rigorous and deployable DRL-based security systems.

</details>