# IEEE SaTML 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [LLM、RAG 与 Prompt Injection](#llmrag-与-prompt-injection)
- [投毒、后门与开发供应链](#投毒后门与开发供应链)
- [隐私泄漏与成员推断](#隐私泄漏与成员推断)
- [安全更新、Unlearning 与可验证推理](#安全更新unlearning-与可验证推理)
- [指纹、模型权属与生成内容保护](#指纹模型权属与生成内容保护)
- [对抗攻击、认证与安全应用评测](#对抗攻击认证与安全应用评测)
- [智能体、具身系统与高风险应用](#智能体具身系统与高风险应用)
- [SoK 与 Position Papers](#sok-与-position-papers)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | 4th IEEE Conference on Secure and Trustworthy Machine Learning (IEEE SaTML 2026) |
| 举办时间与地点 | 2026-03-23 至 2026-03-25；Technical University of Munich, Germany |
| 官方网站 | [IEEE SaTML 2026](https://satml.org/2026/) |
| 官方录用列表 | [Accepted Papers](https://satml.org/2026/accepted-papers/) |
| 官方日程 | [Program](https://satml.org/2026/program/) |
| 正式论文集 | 官网说明录用论文将进入 IEEE Computer Society Digital Library；截至核验日尚未定位到完整的 2026 proceedings 入口 |
| 检查范围 | 官网全部 52 篇 Research Papers、6 篇 Systematization of Knowledge Papers 和 4 篇 Position Papers；数据截至 2026-08-23 |

## 关键节点

除会议日期外，官网说明以下 deadline 均为当天 23:59 AoE（UTC-12）。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Paper submission deadline | 2025-09-24 23:59 AoE | [Call for Papers](https://satml.org/2026/call-for-papers/) |
| Early-reject notification | 2025-10-29 | [Call for Papers](https://satml.org/2026/call-for-papers/) |
| Interactive discussion and revision | 2025-11-19 至 2025-12-03 | [Call for Papers](https://satml.org/2026/call-for-papers/) |
| Decision notification | 2025-12-10 | [Call for Papers](https://satml.org/2026/call-for-papers/) |
| Camera-ready | 官网仅规定录用后一个月内提交，未给出统一精确日期 | [Call for Papers](https://satml.org/2026/call-for-papers/) |
| Conference | 2026-03-23 至 2026-03-25 | [IEEE SaTML 2026](https://satml.org/2026/) |

## 筛选说明

- 官方论文总数：62（52 篇 Research、6 篇 SoK、4 篇 Position）
- 初筛候选：54
- 最终收录：43
- 收录口径：逐篇阅读官网摘要，只收录具有明确攻击者、隐私泄漏、安全失效、恶意使用、认证防御、安全治理或可操作缓解问题设定的论文；传统对抗鲁棒性仅在论文给出具体攻击或认证防御 threat model 时保留。
- 边界案例：一般差分隐私实现、同态加密推理、模型解释、公平性、near-OOD、数据最小化和协作学习立场论文虽然属于广义 trustworthy ML，但没有把可核验的 AI 安全风险作为核心问题，因而从严排除。

## 论文分类

### LLM、RAG 与 Prompt Injection

### 1. BinaryShield: Cross-Service Threat Intelligence in LLM Services using Privacy-Preserving Fingerprints

📄 [arXiv](https://arxiv.org/abs/2509.05608) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`prompt injection`、`privacy-preserving fingerprint`、`threat intelligence`

👤 **作者**：Waris Gill、Natalie Isak、Matthew Dressman

- 🎯 **研究动机**：LLM服务的prompt injection情报难跨服务共享，直接共享样本又泄漏隐私
- 🔬 **研究方法**：BinaryShield以隐私保护二进制指纹实现跨服务威胁情报匹配
- 📌 **结论**：指纹可跨服务识别攻击且不暴露原始内容

### 2. Certifiably Robust RAG against Retrieval Corruption

📄 [arXiv](https://arxiv.org/abs/2405.15556) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`RAG corruption`、`isolate-then-aggregate`、`certified robustness`、`RAG certification`、`bounded corruption`

👤 **作者**：Chong Xiang、Tong Wu、Zexuan Zhong、David Wagner、Danqi Chen、Prateek Mittal

- 🎯 **研究动机**：RAG 易受检索腐化攻击，注入恶意段落即导致错误回答，缺乏可认证防御
- 🔬 **研究方法**：RobustRAG 采用 isolate-then-aggregate：把段落隔离分组分别生成回答，再用 keyword 与 decoding 两种算法安全聚合
- 📌 **结论**：首个可认证鲁棒的 RAG 防御，面对有界数量恶意段落注入仍能证明回答质量下界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. We propose RobustRAG, the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output. To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses. Notably, RobustRAG achieves certifiable robustness: for certain queries in our evaluation datasets, we can formally certify non-trivial lower bounds on response quality -- even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages. We evaluate RobustRAG on the tasks of open-domain question-answering and free-form long text generation and demonstrate its effectiveness across three datasets and three LLMs.

</details>

### 3. Defeating Prompt Injections by Design

📄 [arXiv](https://arxiv.org/abs/2503.18813) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`LLM agent`、`prompt injection`、`capability enforcement`、`policy enforcement`、`capability guard`

👤 **作者**：Edoardo Debenedetti、…、Florian Tramèr

- 🎯 **研究动机**：LLM agent 处理不可信数据时易受 prompt injection，仅靠模型自身对齐无法根治
- 🔬 **研究方法**：提出 CaMeL 防御层，从可信查询显式提取控制流与数据流使不可信数据无法影响程序流，并以 capability 与策略约束工具调用
- 📌 **结论**：在 AgentDojo 上以可证明安全解决 77% 任务（无防御系统为 84%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in agentic systems that interact with an untrusted environment. However, LLM agents are vulnerable to prompt injection attacks when handling untrusted data. In this paper we propose CaMeL, a robust defense that creates a protective system layer around the LLM, securing it even when underlying models are susceptible to attacks. To operate, CaMeL explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow. To further improve security, CaMeL uses a notion of a capability to prevent the exfiltration of private data over unauthorized data flows by enforcing security policies when tools are called. We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. We release CaMeL at https://github.com/google-research/camel-prompt-injection.

</details>

### 4. Defending Against Prompt Injection with DataFilter

📄 [arXiv](https://arxiv.org/abs/2510.19207) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`prompt injection`、`test-time sanitization`、`black-box LLM`

👤 **作者**：Yizhu Wang、Sizhe Chen、Raghad Alkhudair、Basel Alomair、David Wagner

- 🎯 **研究动机**：现有 prompt injection 防御要么需要模型权重（微调），要么损失效用（检测），要么要求系统重构
- 🔬 **研究方法**：DataFilter 是测试时模型无关防御，经模拟注入 SFT 训练，依据用户指令与数据内容选择性剥离对抗指令同时保留良性信息
- 📌 **结论**：多基准上把注入 ASR 降至近零并保持效用，可即插即用地保护黑盒商业 LLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When large language model (LLM) agents are increasingly deployed to automate tasks and interact with untrusted external data, prompt injection emerges as a significant security threat. By injecting malicious instructions into the data that LLMs access, an attacker can arbitrarily override the original user task and redirect the agent toward unintended, potentially harmful actions. Existing defenses either require access to model weights (fine-tuning), incur substantial utility loss (detection-based), or demand non-trivial system redesign (system-level). Motivated by this, we propose DataFilter, a test-time model-agnostic defense that removes malicious instructions from the data before it reaches the backend LLM. DataFilter is trained with supervised fine-tuning on simulated injections and leverages both the user's instruction and the data to selectively strip adversarial content while preserving benign information. Across multiple benchmarks, DataFilter consistently reduces the prompt injection attack success rates to near zero while maintaining the LLMs' utility. DataFilter delivers strong security, high utility, and plug-and-play deployment, making it a strong practical defense to secure black-box commercial LLMs against prompt injection. Our DataFilter model is released at https://huggingface.co/JoyYizhu/DataFilter for immediate use, with the code to reproduce our results at https://github.com/yizhu-joy/DataFilter.

</details>

### 5. Safe But Not Robust: Security Evaluation of VLM by Jailbreaking MSTS

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`VLM jailbreak`、`Robust-MSTS`、`safety evaluation`、`targeted image attack`、`VLM safety`

- 🎯 **研究动机**：VLM安全评测缺针对性图像攻击手段
- 🔬 **研究方法**：构建Robust-MSTS基准，以targeted图像扰动评测VLM安全性
- 📌 **结论**：揭示VLM表面安全但对定向扰动不鲁棒

### 6. Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2501.16534) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`safety classifier`、`surrogate extraction`、`jailbreak transfer`、`safety-boundary extraction`、`surrogate classifier`

👤 **作者**：Jean-Charles Noirot Ferrand、Yohan Beugin、Eric Pauley、Ryan Sheatsley、Patrick McDaniel

- 🎯 **研究动机**：对齐在 LLM 内嵌入决定拒答与否的安全分类器，能否提取该分类器未被研究
- 🔬 **研究方法**：从 LLM 子集构建候选代理分类器，评估其与安全分类器的一致性并攻击候选测迁移率
- 📌 **结论**：仅 20% 架构即达 80% 以上 F1 一致；用 50% Llama-2 的代理攻击 ASR 达 70%，远超直接攻击的 22%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment in large language models (LLMs) is used to enforce guidelines such as safety. Yet, alignment fails in the face of jailbreak attacks that modify inputs to induce unsafe outputs. In this paper, we introduce and evaluate a new technique for jailbreak attacks. We observe that alignment embeds a safety classifier in the LLM responsible for deciding between refusal and compliance, and seek to extract an approximation of this classifier: a surrogate classifier. To this end, we build candidate classifiers from subsets of the LLM. We first evaluate the degree to which candidate classifiers approximate the LLM's safety classifier in benign and adversarial settings. Then, we attack the candidates and measure how well the resulting adversarial inputs transfer to the LLM. Our evaluation shows that the best candidates achieve accurate agreement (an F1 score above 80%) using as little as 20% of the model architecture. Further, we find that attacks mounted on the surrogate classifiers can be transferred to the LLM with high success. For example, a surrogate using only 50% of the Llama 2 model achieved an attack success rate (ASR) of 70% with half the memory footprint and runtime -- a substantial improvement over attacking the LLM directly, where we only observed a 22% ASR. These results show that extracting surrogate classifiers is an effective and efficient means for modeling (and therein addressing) the vulnerability of aligned models to jailbreaking attacks. The code is available at https://github.com/jcnf0/targeting-alignment.

</details>
### 投毒、后门与开发供应链

### 7. Architectural Backdoors for Within-Batch Data Stealing and Model Inference Manipulation

📄 [arXiv](https://arxiv.org/abs/2505.18323) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`architectural backdoor`、`batch isolation`、`information-flow control`、`architecture`、`within-batch attack`

👤 **作者**：Nicolas Küchler、Ivan Petrov、Conrad Grobler、Ilia Shumailov

- 🎯 **研究动机**：传统后门仅操纵预测、现实危害不明，批处理推理的跨用户信息流风险未被研究
- 🔬 **研究方法**：设计利用批处理的新型架构后门窃取同批用户输入输出，并提出基于信息流控制、证明批内不干涉的形式化缓解
- 📌 **结论**：攻击可注入 Transformer 等主流架构；缓解方法在 Hugging Face 扫出 200 余个因动态量化致批内信息泄露的模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For nearly a decade the academic community has investigated backdoors in neural networks, primarily focusing on classification tasks where adversaries manipulate the model prediction. While demonstrably malicious, the immediate real-world impact of such prediction-altering attacks has remained unclear. In this paper we introduce a novel and significantly more potent class of backdoors that builds upon recent advancements in architectural backdoors. We demonstrate how these backdoors can be specifically engineered to exploit batched inference, a common technique for hardware utilization, enabling large-scale user data manipulation and theft. By targeting the batching process, these architectural backdoors facilitate information leakage between concurrent user requests and allow attackers to fully control model responses directed at other users within the same batch. In other words, an attacker who can change the model architecture can set and steal model inputs and outputs of other users within the same batch. We show that such attacks are not only feasible but also alarmingly effective, can be readily injected into prevalent model architectures, (e.g. Transformers), and represent a truly malicious threat to user privacy and system integrity. Critically, to counteract this new class of vulnerabilities, we propose a deterministic mitigation strategy that provides formal guarantees against this new attack vector, unlike prior work that relied on LLMs to find the backdoors. Our mitigation strategy employs a novel Information Flow Control mechanism that analyzes the model graph and proves non-interference between different user inputs within the same batch. Using our mitigation strategy we perform a large scale analysis of models hosted through Hugging Face and find over 200 models that introduce (unintended) information leakage between batch entries due to the use of dynamic quantization.

</details>

### 8. One RNG to Rule Them All - How Randomness Becomes an Attack Vector in Machine Learning

📄 [arXiv](https://arxiv.org/abs/2602.09182) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`ML supply chain`、`PRNG vulnerability`、`runtime enforcement`

👤 **作者**：Kotekar Annapoorna Prabhu、Andrew Gan、Zahra Ghodsi

- 🎯 **研究动机**：ML 框架 PRNG 实现差异大且缺统计校验，随机性成为被忽视的隐蔽攻击向量
- 🔬 **研究方法**：RNGGuard 静态分析目标库源码定位随机函数及调用点，运行时将不安全调用替换为满足安全规范的实现
- 📌 **结论**：以低接入成本填补 ML 系统随机源安全防护的空白

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning relies on randomness as a fundamental component in various steps such as data sampling, data augmentation, weight initialization, and optimization. Most machine learning frameworks use pseudorandom number generators as the source of randomness. However, variations in design choices and implementations across different frameworks, software dependencies, and hardware backends along with the lack of statistical validation can lead to previously unexplored attack vectors on machine learning systems. Such attacks on randomness sources can be extremely covert, and have a history of exploitation in real-world systems. In this work, we examine the role of randomness in the machine learning development pipeline from an adversarial point of view, and analyze the implementations of PRNGs in major machine learning frameworks. We present RNGGuard to help machine learning engineers secure their systems with low effort. RNGGuard statically analyzes a target library's source code and identifies instances of random functions and modules that use them. At runtime, RNGGuard enforces secure execution of random functions by replacing insecure function calls with RNGGuard's implementations that meet security specifications. Our evaluations show that RNGGuard presents a practical approach to close existing gaps in securing randomness sources in machine learning systems.

</details>

### 9. Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated

📄 [arXiv](https://arxiv.org/abs/2509.05739) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`analysis`、`reasoning model`、`data poisoning`、`decomposed trigger`、`CoT integrity`

👤 **作者**：Hanna Foerster、…、Yarin Gal

- 🎯 **研究动机**：推理能力把 LLM 攻击面扩展到中间 CoT，但推理模型上投毒能否生效不明
- 🔬 **研究方法**：提出 decomposed reasoning poison：仅修改推理路径、prompt 与最终答案保持干净，并把触发器拆成多个各自无害的组件
- 📌 **结论**：可注入但可靠激活并改变最终答案出奇困难，模型常能从思维过程中的后门恢复，推理能力带来涌现式后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early research into data poisoning attacks against Large Language Models (LLMs) demonstrated the ease with which backdoors could be injected. More recent LLMs add step-by-step reasoning, expanding the attack surface to include the intermediate chain-of-thought (CoT) and its inherent trait of decomposing problems into subproblems. Using these vectors for more stealthy poisoning, we introduce ``decomposed reasoning poison'', in which the attacker modifies only the reasoning path, leaving prompts and final answers clean, and splits the trigger across multiple, individually harmless components. Fascinatingly, while it remains possible to inject these decomposed poisons, reliably activating them to change final answers (rather than just the CoT) is surprisingly difficult. This difficulty arises because the models can often recover from backdoors that are activated within their thought processes. Ultimately, it appears that an emergent form of backdoor robustness is originating from the reasoning capabilities of these advanced LLMs, as well as from the architectural separation between reasoning and final answer generation.

</details>
### 隐私泄漏与成员推断

### 10. A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage

📄 [arXiv](https://arxiv.org/abs/2504.21035) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`text sanitization`、`semantic re-identification`、`privacy leakage`

👤 **作者**：Rui Xin、…、Pang Wei Koh

- 🎯 **研究动机**：文本脱敏评测止于表层标识符，语义层面的再识别风险未被评估
- 🔬 **研究方法**：对脱敏文本发起语义再识别攻击，考察超出表层泄漏的隐私风险
- 📌 **结论**：表层脱敏后仍可被语义线索重新识别，形成虚假隐私感

### 11. DeepLeak: Privacy Enhancing Hardening of Model Explanations Against Membership Leakage

📄 [arXiv](https://arxiv.org/abs/2601.03429) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`model explanation`、`membership inference`、`privacy hardening`

👤 **作者**：Firas Ben Hmida、Zain Sbeih、Philemon Hailemariam、Birhanu Eshete

- 🎯 **研究动机**：事后解释方法会泄漏成员信息，从业者缺乏平衡透明性与隐私的系统性指导
- 🔬 **研究方法**：DeepLeak 构建更强的解释感知成员推断攻击量化泄漏，提出敏感度校准噪声、归因裁剪与掩码等模型无关缓解，并以控制实验定位归因稀疏性等泄漏根因
- 📌 **结论**：15 种解释技术默认设置泄漏比先前报告多至 74.9%；缓解最多削减 95% 泄漏，平均效用损失不超过 3.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) explainability is central to algorithmic transparency in high-stakes settings such as predictive diagnostics and loan approval. However, these same domains require rigorous privacy guaranties, creating tension between interpretability and privacy. Although prior work has shown that explanation methods can leak membership information, practitioners still lack systematic guidance on selecting or deploying explanation techniques that balance transparency with privacy. We present DeepLeak, a system to audit and mitigate privacy risks in post-hoc explanation methods. DeepLeak advances the state-of-the-art in three ways: (1) comprehensive leakage profiling: we develop a stronger explanation-aware membership inference attack (MIA) to quantify how much representative explanation methods leak membership information under default configurations; (2) lightweight hardening strategies: we introduce practical, model-agnostic mitigations, including sensitivity-calibrated noise, attribution clipping, and masking, that substantially reduce membership leakage while preserving explanation utility; and (3) root-cause analysis: through controlled experiments, we pinpoint algorithmic properties (e.g., attribution sparsity and sensitivity) that drive leakage. Evaluating 15 explanation techniques across four families on image benchmarks, DeepLeak shows that default settings can leak up to 74.9% more membership information than previously reported. Our mitigations cut leakage by up to 95% (minimum 46.5%) with only <=3.3% utility loss on average. DeepLeak offers a systematic, reproducible path to safer explainability in privacy-sensitive ML.

</details>

### 12. Kraken: Higher-order EM side-channel attacks on DNNs in near and far field

📄 [arXiv](https://arxiv.org/abs/2603.02891) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`EM side channel`、`LLM weight extraction`、`physical model stealing`

👤 **作者**：Peter Horvath、Ilia Shumailov、Lukasz Chmielewski、Lejla Batina、Yuval Yarom

- 🎯 **研究动机**：EM侧信道对DNN的近场与远场高阶威胁未明
- 🔬 **研究方法**：Kraken以高阶EM分析在近场与远场攻击DNN推断
- 📌 **结论**：物理侧信道可实际窃取LLM等模型权重

### 13. Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering

📄 [arXiv](https://arxiv.org/abs/2605.04116) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`retrieval-based ICL`、`membership inference`、`black-box access`

👤 **作者**：Tejas Kulkarni、Antti Koskela、Laith Zumot

- 🎯 **研究动机**：带检索函数的 ICL 服务会引入训练数据成员泄露，面向该设定的黑盒成员推断未被研究
- 🔬 **研究方法**：两种黑盒攻击利用查询文本前缀：参考模型估计不可得的 loss，或以加权平均方案直接计算成员统计量
- 📌 **结论**：在查询为改写版本的更严格设定下仍以更少前缀优于三个先前攻击；改编的集成 prompt 防御可显著缓解第二种攻击的泄露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that remotely hosted applications employing in-context learning when augmented with a retrieval function to select in-context examples can be vulnerable to membership-inference attacks even when the service provider and users are separate parties. We propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs. The first attack uses a reference model to estimate an otherwise unavailable loss metric. The second attack improves upon it by eliminating the reference model and instead computing a membership statistic through a simple but novel weighted-averaging scheme. Our comprehensive empirical evaluations consider a stricter case in which the adversary has a paraphrased version of the text in the queries and show that our attacks can exhibit stronger resilience to paraphrasing and outperform three prior attacks in many cases with small number of prefixes. We also adapt an existing ensemble prompting defense to our setting, demonstrating that it substantially mitigates the privacy leakage caused by our second attack.

</details>

### 14. On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models

📄 [arXiv](https://arxiv.org/abs/2512.13352) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`LLM memorization`、`membership inference`、`targeted extraction`

👤 **作者**：Ali Al Sahili、Ali Chehab、Razane Tajeddine

- 🎯 **研究动机**：成员推断与训练数据提取两种威胁已知相关，但各 MIA 技术在真实提取管线中的实际效用缺乏系统评估
- 🔬 **研究方法**：把多种 MIA 技术集成进数据提取管线并系统基准评测，与常规 MIA 基准结果对比
- 📌 **结论**：揭示 MIA 在集成提取设定下的表现与常规基准的差异，为现实提取场景中的实用性提供参照

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are prone to memorizing training data, which poses serious privacy risks. Two of the most prominent concerns are training data extraction and Membership Inference Attacks (MIAs). Prior research has shown that these threats are interconnected: adversaries can extract training data from an LLM by querying the model to generate a large volume of text and subsequently applying MIAs to verify whether a particular data point was included in the training set. In this study, we integrate multiple MIA techniques into the data extraction pipeline to systematically benchmark their effectiveness. We then compare their performance in this integrated setting against results from conventional MIA benchmarks, allowing us to evaluate their practical utility in real-world extraction scenarios.

</details>

### 15. Privacy Risks in Time Series Forecasting: User- and Record-Level Membership Inference

📄 [arXiv](https://arxiv.org/abs/2509.04169) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`time-series forecasting`、`membership inference`、`user-level leakage`

👤 **作者**：Nicolas Johansson、Tobias Olsson、Daniel Nilsson、Johan Östman、Fazeleh Hoseini

- 🎯 **研究动机**：成员推断在分类模型上研究充分，时序预测领域几乎空白
- 🔬 **研究方法**：提出适配多变量 LiRA 与端到端 DTS 两种攻击，在 TUH-EEG 与 ELD 上对 LSTM 与 N-HiTS 做记录级与用户级威胁评测
- 📌 **结论**：预测模型普遍脆弱，用户级攻击常达完美检测；预测时域越长、训练群体越小越脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) aim to determine whether specific data were used to train a model. While extensively studied on classification models, their impact on time series forecasting remains largely unexplored. We address this gap by introducing two new attacks: (i) an adaptation of multivariate LiRA, a state-of-the-art MIA originally developed for classification models, to the time-series forecasting setting, and (ii) a novel end-to-end learning approach called Deep Time Series (DTS) attack. We benchmark these methods against adapted versions of other leading attacks from the classification setting. We evaluate all attacks in realistic settings on the TUH-EEG and ELD datasets, targeting two strong forecasting architectures, LSTM and the state-of-the-art N-HiTS, under both record- and user-level threat models. Our results show that forecasting models are vulnerable, with user-level attacks often achieving perfect detection. The proposed methods achieve the strongest performance in several settings, establishing new baselines for privacy risk assessment in time series forecasting. Furthermore, vulnerability increases with longer prediction horizons and smaller training populations, echoing trends observed in large language models.

</details>

### 16. Reconstructing Training Data from Models Trained with Transfer Learning

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`transfer learning`、`training reconstruction`、`embedding leakage`

- 🎯 **研究动机**：迁移学习下训练数据重构风险未被评估
- 🔬 **研究方法**：对迁移训练的模型发起embedding泄漏式数据重构攻击
- 📌 **结论**：迁移学习并不能消除训练数据重构风险

### 17. Training Set Reconstruction from Differentially Private Forests: How Effective is DP?

📄 [arXiv](https://arxiv.org/abs/2502.05307) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`differential privacy`、`forest reconstruction`、`constraint programming`

👤 **作者**：Alice Gorgé、Julien Ferry、Sébastien Gambs、Thibaut Vidal

- 🎯 **研究动机**：DP 随机森林抵御训练集重构攻击的实际能力未量化
- 🔬 **研究方法**：以约束规划结合森林结构与 DP 机制特性，形式化重构最可能产出该森林的训练集
- 📌 **结论**：具有意义 DP 保证的森林仍泄漏部分训练数据；唯一完全免疫的森林预测性能不优于常数分类器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research has shown that structured machine learning models such as tree ensembles are vulnerable to privacy attacks targeting their training data. To mitigate these risks, differential privacy (DP) has become a widely adopted countermeasure, as it offers rigorous privacy protection. In this paper, we introduce a reconstruction attack targeting state-of-the-art $ε$-DP random forests. By leveraging a constraint programming model that incorporates knowledge of the forest's structure and DP mechanism characteristics, our approach formally reconstructs the most likely dataset that could have produced a given forest. Through extensive computational experiments, we examine the interplay between model utility, privacy guarantees and reconstruction accuracy across various configurations. Our results reveal that random forests trained with meaningful DP guarantees can still leak portions of their training data. Specifically, while DP reduces the success of reconstruction attacks, the only forests fully robust to our attack exhibit predictive performance no better than a constant classifier. Building on these insights, we also provide practical recommendations for the construction of DP random forests that are more resilient to reconstruction attacks while maintaining a non-trivial predictive performance.

</details>

### 18. Your Privacy Depends on Others: Collusion Vulnerabilities in Individual Differential Privacy

📄 [arXiv](https://arxiv.org/abs/2601.12922) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`individual DP`、`collusion`、`membership inference`

👤 **作者**：Johannes Kaiser、Alexander Ziller、Eleni Triantafillou、Daniel Rückert、Georgios Kaissis

- 🎯 **研究动机**：个体差分隐私承诺用户自控隐私，但采样式机制中个人风险实际由所有数据贡献者的隐私选择共同决定
- 🔬 **研究方法**：实证特定隐私偏好分布会放大个体风险；中央或合谋对手可故意选择预算放大目标个体漏洞且完全在 DP 保证内；提出以 Δ-散度给超额脆弱性硬上界的 (ε,δ,Δ)-iDP 隐私合同
- 📌 **结论**：对 62% 目标个体的成员推断攻击成功，显著提升其被推断概率，暴露 iDP 范式的根本挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Individual Differential Privacy (iDP) promises users control over their privacy, but this promise can be broken in practice. We reveal a previously overlooked vulnerability in sampling-based iDP mechanisms: while conforming to the iDP guarantees, an individual's privacy risk is not solely governed by their own privacy budget, but critically depends on the privacy choices of all other data contributors. This creates a mismatch between the promise of individual privacy control and the reality of a system where risk is collectively determined. We demonstrate empirically that certain distributions of privacy preferences can unintentionally inflate the privacy risk of individuals, even when their formal guarantees are met. Moreover, this excess risk provides an exploitable attack vector. A central adversary or a set of colluding adversaries can deliberately choose privacy budgets to amplify vulnerabilities of targeted individuals. Most importantly, this attack operates entirely within the guarantees of DP, hiding this excess vulnerability. Our empirical evaluation demonstrates successful attacks against 62% of targeted individuals, substantially increasing their membership inference susceptibility. To mitigate this, we propose $(\varepsilon_i,δ_i,\overlineΔ)$-iDP a privacy contract that uses $Δ$-divergences to provide users with a hard upper bound on their excess vulnerability, while offering flexibility to mechanism design. Our findings expose a fundamental challenge to the current paradigm, demanding a re-evaluation of how iDP systems are designed, audited, communicated, and deployed to make excess risks transparent and controllable.

</details>
### 安全更新、Unlearning 与可验证推理

### 19. Evaluating Deep Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2410.15153) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`LLM unlearning`、`deductive knowledge`、`forgetting evaluation`

👤 **作者**：Ruihan Wu、Chhavi Yadav、Russ Salakhutdinov、Kamalika Chaudhuri

- 🎯 **研究动机**：事实遗忘多只删目标事实，忽略其可经保留知识与推理被演绎推出
- 🔬 **研究方法**：提出深度遗忘设定与 Success-DU、Recall、Accuracy 三指标，用 MQuAKE 与多步演绎数据集 Eval-DU 基准化
- 📌 **结论**：现有方法要么遗忘不深、要么过度删除无关事实，需专门算法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning has emerged as an important component in developing safe and trustworthy models. Prior work on fact unlearning in LLMs has mostly focused on removing a specified target fact robustly, but often overlooks its deductive connections to other knowledge. We propose a new setting for fact unlearning, deep unlearning, where the goal is not only to remove a target fact but also to prevent it from being deduced via retained knowledge in the LLM and logical reasoning. We propose three novel metrics: Success-DU and Recall to measure unlearning efficacy, and Accuracy to measure the remainder model utility. To benchmark this setting, we leverage both (1) an existing real-world knowledge dataset, MQuAKE, that provides one-step deduction instances, and (2) newly construct a novel semi-synthetic dataset, Eval-DU, that allows multiple steps of realistic deductions among synthetic facts. Experiments reveal that current methods struggle with deep unlearning: they either fail to deeply unlearn, or excessively remove unrelated facts. Our results suggest that targeted algorithms may have to be developed for robust/deep fact unlearning in LLMs.

</details>

### 20. Exact Unlearning of Finetuning Data via Model Merging at Scale

📄 [arXiv](https://arxiv.org/abs/2504.04626) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`exact unlearning`、`model merging`、`SIFT-Masks`

👤 **作者**：Kevin Kuo、Amrith Setlur、Kartik Srinivas、Aditi Raghunathan、Virginia Smith

- 🎯 **研究动机**：近似遗忘脆弱且可被攻击复原数据，标准模型合并在大规模任务下损效用或令精确遗忘代价过高
- 🔬 **研究方法**：提出 SIFT-Masks，以局部 mask 恢复任务性能，全局符号向量约束微调使各 mask 可独立确定后再合并
- 📌 **结论**：合并最多 500 个模型时准确率比朴素合并高 5-80%，精确遗忘计算量最多降 250 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Approximate unlearning has gained popularity as an approach to efficiently update an LLM so that it behaves (roughly) as if it was not trained on a subset of data to begin with. However, existing methods are brittle in practice and can easily be attacked to reveal supposedly unlearned information. To alleviate issues with approximate unlearning, we instead propose SIFT-Masks (SIgn-Fixed Tuning-Masks), an exact unlearning method based on model merging. SIFT-Masks addresses two key limitations of standard model merging: (1) merging a large number of tasks can severely harm utility; and (2) methods that boost utility by sharing extra information across tasks make exact unlearning prohibitively expensive. SIFT-Masks solves these issues by (1) applying local masks to recover task-specific performance; and (2) constraining finetuning to align with a global sign vector as a lightweight approach to determine masks independently before merging. Across four settings where we merge up to 500 models, SIFT-Masks improves accuracy by 5-80% over naive merging and uses up to 250x less compute for exact unlearning compared to other merging baselines.

</details>

### 21. Gauss-Newton Unlearning for the LLM Era

📄 [arXiv](https://arxiv.org/abs/2602.10568) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`LLM unlearning`、`Gauss-Newton update`、`retain utility`

👤 **作者**：Lev McKinney、…、Roger Grosse

- 🎯 **研究动机**：LLM unlearning 遗忘目标数据时常损伤保留分布上的行为，权衡难改善
- 🔬 **研究方法**：K-FADE 用 K-FAC 近似的少量 Gauss-Newton 上行步做遗忘，把保留集输出约束转化为权重约束以最小化保留行为改动
- 📌 **结论**：在 WMDP 与 ToFU 上逼近无遗忘集重训的输出，对保留集改动小于既有方法，且更新可在后续训练后重复应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Standard large language model training can create models that produce outputs their trainer deems unacceptable in deployment. The probability of these outputs can be reduced using methods such as LLM unlearning. However, unlearning a set of data (called the forget set) can degrade model performance on other distributions where the trainer wants to retain the model's behavior. To improve this trade-off, we demonstrate that using the forget set to compute only a few uphill Gauss-Newton steps provides a conceptually simple, state-of-the-art unlearning approach for LLMs. While Gauss-Newton steps adapt Newton's method to non-linear models, it is non-trivial to efficiently and accurately compute such steps for LLMs. Hence, our approach crucially relies on parametric Hessian approximations such as Kronecker-Factored Approximate Curvature (K-FAC). We call this combined approach K-FADE (K-FAC for Distribution Erasure). Our evaluation on the WMDP and ToFU benchmarks demonstrates that K-FADE suppresses outputs from the forget set and approximates, in output space, the results of retraining without the forget set. Critically, our method does this while altering the outputs on the retain set less than previous methods. This is because K-FADE transforms a constraint on the model's outputs across the entire retain set into a constraint on the model's weights, allowing the algorithm to minimally change the model's behavior on the retain set at each step. Moreover, the unlearning updates computed by K-FADE can be reapplied later if the model undergoes further training, allowing unlearning to be cheaply maintained.

</details>

### 22. Provably Safe Model Updates

📄 [arXiv](https://arxiv.org/abs/2512.01899) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`safe update`、`parameter certification`、`alignment drift`

👤 **作者**：Leo Elmecker-Plakolm、Pierre Fasterling、Philip Sosnin、Calvin Tsay、Matthew Wicker

- 🎯 **研究动机**：正则化与参数隔离等启发式方法可缓解灾难性遗忘或对齐漂移，但无法认证更新后模型仍满足性能规约
- 🔬 **研究方法**：把问题形式化为计算参数空间中满足规约的最大局部不变域（LID），用正交体与 zonotope 参数化抽象域得到可解的原始-对偶公式，通过把更新投影回安全域实现与数据和算法无关的认证
- 📌 **结论**：在持续学习与基础模型微调基准上匹配或超越启发式基线，同时提供形式安全保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical environments are inherently dynamic. Distribution shifts, emerging vulnerabilities, and evolving requirements demand continuous updates to machine learning models. Yet even benign parameter updates can have unintended consequences, such as catastrophic forgetting in classical models or alignment drift in foundation models. Existing heuristic approaches (e.g., regularization, parameter isolation) can mitigate these effects but cannot certify that updated models continue to satisfy required performance specifications. We address this problem by introducing a framework for provably safe model updates. Our approach first formalizes the problem as computing the largest locally invariant domain (LID): a connected region in parameter space where all points are certified to satisfy a given specification. While exact maximal LID computation is intractable, we show that relaxing the problem to parameterized abstract domains (orthotopes, zonotopes) yields a tractable primal-dual formulation. This enables efficient certification of updates - independent of the data or algorithm used - by projecting them onto the safe domain. Our formulation further allows computation of multiple approximately optimal LIDs, incorporation of regularization-inspired biases, and use of lookahead data buffers. Across continual learning and foundation model fine-tuning benchmarks, our method matches or exceeds heuristic baselines for avoiding forgetting while providing formal safety guarantees.

</details>

### 23. RobPI: Robust Private Inference against Malicious Client

📄 [arXiv](https://arxiv.org/abs/2602.19918) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`private inference`、`malicious client`、`cryptographic protocol`

👤 **作者**：Jiaqi Xue、Mengxin Zheng、Qian Lou

- 🎯 **研究动机**：私有推理协议在恶意客户端下缺鲁棒性保证
- 🔬 **研究方法**：RobPI设计抗恶意客户端的密码学私有推理协议
- 📌 **结论**：恶意客户端下仍保证隐私与结果正确性

### 24. Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference

📄 [arXiv](https://arxiv.org/abs/2603.19025) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`verifiable inference`、`execution trace`、`lightweight proof`

👤 **作者**：Pranay Anchuri、…、Tugce Ozdemir

- 🎯 **研究动机**：云端推理无正确性保证，现有密码学证明系统对十亿参数模型每查询需数百秒
- 🔬 **研究方法**：用 Merkle 树向量承诺执行轨迹，仅开启输出到输入随机采样路径上的少量条目，以可靠性换效率，并形式化轨迹可分性条件
- 📌 **结论**：证明时间从分钟级降至毫秒级；ResNet-18 与 Llama-2-7B 上梯度重建、逆变换、logit 交换等对抗策略均无法逃避检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When large AI models are deployed as cloud-based services, clients have no guarantee that responses are correct or were produced by the intended model. Rerunning inference locally is infeasible for large models, and existing cryptographic proof systems -- while providing strong correctness guarantees -- introduce prohibitive prover overhead (e.g., hundreds of seconds per query for billion-parameter models). We present a verification framework and protocol that replaces full cryptographic proofs with a lightweight, sampling-based approach grounded in statistical properties of neural networks. We formalize the conditions under which trace separation between functionally dissimilar models can be leveraged to argue the security of verifiable inference protocols. The prover commits to the execution trace of inference via Merkle-tree-based vector commitments and opens only a small number of entries along randomly sampled paths from output to input. This yields a protocol that trades soundness for efficiency, a tradeoff well-suited to auditing, large-scale deployment settings where repeated queries amplify detection probability, and scenarios with rationally incentivized provers who face penalties upon detection. Our approach reduces proving times by several orders of magnitude compared to state-of-the-art cryptographic proof systems, going from the order of minutes to the order of milliseconds, with moderately larger proofs. Experiments on ResNet-18 classifiers and Llama-2-7B confirm that common architectures exhibit the statistical properties our protocol requires, and that natural adversarial strategies (gradient-descent reconstruction, inverse transforms, logit swapping) fail to produce traces that evade detection. We additionally present a protocol in the refereed delegation model, where two competing servers enable correct output identification in a logarithmic number of rounds.

</details>
### 指纹、模型权属与生成内容保护

### 25. Are Robust LLM Fingerprints Adversarially Robust?

📄 [arXiv](https://arxiv.org/abs/2509.26598) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`LLM fingerprint`、`ownership verification`、`adaptive evasion`

👤 **作者**：Anshul Nasery、Edoardo Contente、Alkin Kaz、Pramod Viswanath、Sewoong Oh

- 🎯 **研究动机**：鲁棒LLM指纹能否抵抗自适应规避未经检验
- 🔬 **研究方法**：对现有鲁棒指纹发起自适应evasion攻击评估其稳定性
- 📌 **结论**：自适应攻击下指纹仍可被规避，所有权验证存在风险

### 26. Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes

📄 [arXiv](https://arxiv.org/abs/2602.22197) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`image protection`、`generative denoising`、`defense bypass`

👤 **作者**：Xavier Pleimling、…、Bimal Viswanath

- 🎯 **研究动机**：图像保护方案此前只需应对专用攻击，通用生成模型能否直接击穿未检验
- 🔬 **研究方法**：把现成 image-to-image GenAI 模型经简单文本提示改造成通用去噪器，去除图像保护性扰动
- 📌 **结论**：6 类保护方案的 8 个案例中全部被绕过且优于专用攻击并保留图像效用，多数方案只是虚假安全感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in Generative AI (GenAI) have led to the development of various protection strategies to prevent the unauthorized use of images. These methods rely on adding imperceptible protective perturbations to images to thwart misuse such as style mimicry or deepfake manipulations. Although previous attacks on these protections required specialized, purpose-built methods, we demonstrate that this is no longer necessary. We show that off-the-shelf image-to-image GenAI models can be repurposed as generic ``denoisers" using a simple text prompt, effectively removing a wide range of protective perturbations. Across 8 case studies spanning 6 diverse protection schemes, our general-purpose attack not only circumvents these defenses but also outperforms existing specialized attacks while preserving the image's utility for the adversary. Our findings reveal a critical and widespread vulnerability in the current landscape of image protection, indicating that many schemes provide a false sense of security. We stress the urgent need to develop robust defenses and establish that any future protection mechanism must be benchmarked against attacks from off-the-shelf GenAI models. Code is available in this repository: https://github.com/mlsecviswanath/img2imgdenoiser

</details>

### 27. Protecting Facial Biometrics from Malicious Generative Editing via Latent Optimization

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`facial biometrics`、`malicious editing`、`latent optimization`

- 🎯 **研究动机**：生成式编辑可恶意篡改面部生物特征
- 🔬 **研究方法**：经latent优化向图像嵌入保护扰动以破坏恶意编辑
- 📌 **结论**：视觉质量基本保持下阻断生成式篡改

### 28. Smudged Fingerprints: A Systematic Evaluation of the Robustness of AI Image Fingerprints

📄 [arXiv](https://arxiv.org/abs/2512.11771) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`AI image fingerprint`、`removal and forgery`、`attribution robustness`

👤 **作者**：Kai Yao、Marc Juarez

- 🎯 **研究动机**：AI 图像指纹用于溯源取证，但现有评测几乎不考虑对抗设定，其在攻击下的鲁棒性不明
- 🔬 **研究方法**：形式化白盒/黑盒访问与指纹移除、伪造两种攻击目标的威胁模型，实现五种攻击策略，评测 14 种指纹方法（RGB、频域、学习特征）在 12 个 SOTA 生成器上的表现
- 📌 **结论**：白盒移除成功率常超 80%、黑盒超 50%；没有方法能兼顾准确与鲁棒，准确的归因方法往往更易受攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model fingerprint detection has shown promise to trace the provenance of AI-generated images in forensic applications. However, despite the inherent adversarial nature of these applications, existing evaluations rarely consider adversarial settings. We present the first systematic security evaluation of these techniques, formalizing threat models that encompass both white- and black-box access and two attack goals: fingerprint removal, which erases identifying traces to evade attribution, and fingerprint forgery, which seeks to cause misattribution to a target model. We implement five attack strategies and evaluate 14 representative fingerprinting methods across RGB, frequency, and learned-feature domains on 12 state-of-the-art image generators. Our experiments reveal a pronounced gap between clean and adversarial performance. Removal attacks are highly effective, often achieving success rates above 80% in white-box settings and over 50% under black-box access. While forgery is more challenging than removal, its success varies significantly across targeted models. We also observe a utility-robustness trade-off: accurate attribution methods are often vulnerable to attacks and, although some techniques are robust in specific settings, none achieves robustness and accuracy across all evaluated threat models. These findings highlight the need for techniques that balance robustness and accuracy, and we identify the most promising approaches toward this goal. Code available at: https://github.com/kaikaiyao/SmudgedFingerprints.

</details>
### 对抗攻击、认证与安全应用评测

### 29. Accelerating Targeted Hard-Label Adversarial Attacks in Low-Query Black-Box Settings

📄 [arXiv](https://arxiv.org/abs/2505.16313) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`hard-label attack`、`targeted evasion`、`query efficiency`

👤 **作者**：Arjhun Swaminathan、Mete Akgün

- 🎯 **研究动机**：黑盒 hard-label 定向攻击决策区域窄，现有方法只用决策边界几何而忽略图像自身信息
- 🔬 **研究方法**：提出 TEA，利用目标图像边缘信息生成更靠近源图的对抗样本，并为几何式攻击提供更优初始化
- 📌 **结论**：低查询设置下比 SoTA 少用近 70% 查询

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks for image classification remain vulnerable to adversarial examples -- small, imperceptible perturbations that induce misclassifications. In black-box settings, where only the final prediction is accessible, crafting targeted attacks that aim to misclassify into a specific target class is particularly challenging due to narrow decision regions. Current state-of-the-art methods often exploit the geometric properties of the decision boundary separating a source image and a target image rather than incorporating information from the images themselves. In contrast, we propose Targeted Edge-informed Attack (TEA), a novel attack that utilizes edge information from the target image to carefully perturb it, thereby producing an adversarial image that is closer to the source image while still achieving the desired target classification. Our approach consistently outperforms current state-of-the-art methods across different models in low query settings (nearly 70% fewer queries are used), a scenario especially relevant in real-world applications with limited queries and black-box access. Furthermore, by efficiently generating a suitable adversarial example, TEA provides an improved target initialization for established geometry-based attacks.

</details>

### 30. Beyond the TESSERACT: Trustworthy Dataset Curation for Sound Evaluations of Android Malware Classifiers

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`malware classifier`、`dataset curation`、`evaluation validity`

- 🎯 **研究动机**：Android恶意软件分类器评测受时空采样偏差影响，结论失真
- 🔬 **研究方法**：提出可信数据集构建流程以支撑合理评测
- 📌 **结论**：偏差校正后模型性能排序显著改变

### 31. Cascading Robustness Verification: Toward Efficient Model‑Agnostic Certification

📄 [arXiv](https://arxiv.org/abs/2602.04236) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`robustness verification`、`verifier cascade`、`certified accuracy`

👤 **作者**：Mohammadreza Maleki、Rushendra Sidibomma、Arman Adibi、Reza Samavi

- 🎯 **研究动机**：单一不完备验证器因松弛近似或与训练方法错配而系统性低估鲁棒性
- 🔬 **研究方法**：级联验证框架 CRV：多验证器下任一认证即鲁棒，从最便宜方法开始逐步升级，并对昂贵方法引入逐步松弛算法增量添加约束
- 📌 **结论**：认证精度不低于级联中强验证器，运行时间最多节省约 90%，且保证与模型训练过程无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Certifying neural network robustness against adversarial examples is challenging, as formal guarantees often require solving non-convex problems. Hence, incomplete verifiers are widely used because they scale efficiently and substantially reduce the cost of robustness verification compared to complete methods. However, relying on a single verifier can underestimate robustness because of loose approximations or misalignment with training methods. In this work, we propose Cascading Robustness Verification (CRV), which goes beyond an engineering improvement by exposing fundamental limitations of existing robustness metric and introducing a framework that enhances both reliability and efficiency. CRV is a model-agnostic verifier, meaning that its robustness guarantees are independent of the model's training process. The key insight behind the CRV framework is that, when using multiple verification methods, an input is certifiably robust if at least one method certifies it as robust. Rather than relying solely on a single verifier with a fixed constraint set, CRV progressively applies multiple verifiers to balance the tightness of the bound and computational cost. Starting with the least expensive method, CRV halts as soon as an input is certified as robust; otherwise, it proceeds to more expensive methods. For computationally expensive methods, we introduce a Stepwise Relaxation Algorithm (SR) that incrementally adds constraints and checks for certification at each step, thereby avoiding unnecessary computation. Our theoretical analysis demonstrates that CRV achieves equal or higher verified accuracy compared to powerful but computationally expensive incomplete verifiers in the cascade, while significantly reducing verification overhead. Empirical results confirm that CRV certifies at least as many inputs as benchmark approaches, while improving runtime efficiency by up to ~90%.

</details>

### 32. Efficient Semi-Supervised Adversarial Training via Latent Clustering-Based Data Reduction

📄 [arXiv](https://arxiv.org/abs/2501.10466) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`defense`、`adversarial training`、`latent clustering`、`data reduction`

👤 **作者**：Somrita Ghosh、Yuelin Xu、Xiao Zhang

- 🎯 **研究动机**：半监督对抗训练需大量额外数据，训练久、内存开销高
- 🔬 **研究方法**：用潜空间聚类选择或生成决策边界附近的小关键子集，并保持边界与非边界数据平衡以防过拟合
- 📌 **结论**：以 5-10 倍少的无标签数据达到几乎相同的鲁棒精度，总运行时间缩短约 3-4 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Learning robust models under adversarial settings is widely recognized as requiring a considerably large number of training samples. Recent work proposes semi-supervised adversarial training (SSAT), which utilizes external unlabeled or synthetically generated data and is currently the state of the art. However, SSAT requires substantial extra data to attain high robustness, resulting in prolonged training time and increased memory usage. In this paper, we propose data reduction strategies to improve the efficiency of SSAT by optimizing the amount of additional data incorporated. Specifically, we design novel latent clustering-based techniques to select or generate a small, critical subset of data samples near the model's decision boundary. While focusing on boundary-adjacent points, our methods maintain a balanced ratio between boundary and non-boundary data points, thereby avoiding overfitting. Comprehensive experiments across image benchmarks demonstrate that our methods can effectively reduce SSAT's data requirements and computational costs while preserving its strong robustness advantages. In particular, our latent-space selection scheme based on k-means clustering and our guided diffusion-based approach with LCG-KM are the most effective, achieving nearly identical robust accuracies with 5 times to 10 times less unlabeled data. When compared to full SSAT trained to convergence, our methods reduce total runtime by approximately 3 times to 4 times due to strategic prioritization of unlabeled data.

</details>

### 33. On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses

📄 [arXiv](https://arxiv.org/abs/2506.02978) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`tabular foundation model`、`test-time evasion`、`in-context defense`

👤 **作者**：Mohamed Djilani、…、Mike Papadakis

- 🎯 **研究动机**：表格基础模型的测试时对抗鲁棒性未明
- 🔬 **研究方法**：系统评测test-time攻击并提出in-context防御
- 📌 **结论**：揭示脆弱性并验证上下文防御有效性

### 34. RobustBlack: Challenging Black-Box Adversarial Attacks on State-of-the-Art Defenses

📄 [arXiv](https://arxiv.org/abs/2412.20987) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`black-box attack`、`robust defense`、`transferability`

👤 **作者**：Mohamed Djilani、Salah Ghamizi、Maxime Cordy

- 🎯 **研究动机**：黑盒对抗攻击对SOTA防御的检验不足，可迁移性存疑
- 🔬 **研究方法**：构建RobustBlack基准挑战SOTA防御的黑盒攻击
- 📌 **结论**：揭示所谓鲁棒防御在黑盒攻击下失效
### 智能体、具身系统与高风险应用

### 35. Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading

📄 [arXiv](https://arxiv.org/abs/2601.13082) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`algorithmic trading`、`adversarial headline`、`financial impact`

👤 **作者**：Advije Rizvani、Giovanni Apruzzese、Pavel Laskov

- 🎯 **研究动机**：LLM 驱动算法交易系统对文本对抗样本的系统级货币风险从未被量化
- 🔬 **研究方法**：在无 ATS 访问、仅能改一日新闻标题的对手设定下，评估 Unicode 同形字替换（误导股票名识别）与隐藏文本子句（改变情感），在 Backtrader 实现融合 LSTM 价格预测与 LLM 情感的 ATS
- 📌 **结论**：14 个月内单日攻击即可使年化收益最多降低 17.7 个百分点；对抓取库与平台的分析及 27 位 FinTech 从业者调研证实现实可行性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly adopted in the financial domain. Their exceptional capabilities to analyse textual data make them well-suited for inferring the sentiment of finance-related news. Such feedback can be leveraged by algorithmic trading systems (ATS) to guide buy/sell decisions. However, this practice bears the risk that a threat actor may craft "adversarial news" intended to mislead an LLM. In particular, the news headline may include "malicious" content that remains invisible to human readers but which is still ingested by the LLM. Although prior work has studied textual adversarial examples, their system-wide impact on LLM-supported ATS has not yet been quantified in terms of monetary risk. To address this threat, we consider an adversary with no direct access to an ATS but able to alter stock-related news headlines on a single day. We evaluate two human-imperceptible manipulations in a financial context: Unicode homoglyph substitutions that misroute models during stock-name recognition, and hidden-text clauses that alter the sentiment of the news headline. We implement a realistic ATS in Backtrader that fuses an LSTM-based price forecast with LLM-derived sentiment (FinBERT, FinGPT, FinLLaMA, and six general-purpose LLMs), and quantify monetary impact using portfolio metrics. Experiments on real-world data show that manipulating a one-day attack over 14 months can reliably mislead LLMs and reduce annual returns by up to 17.7 percentage points. To assess real-world feasibility, we analyze popular scraping libraries and trading platforms and survey 27 FinTech practitioners, confirming our hypotheses. We notified trading platform owners of this security issue.

</details>

### 36. “Org-Wide, We’re Not Ready": C-Level Lessons on Securing Generative AI Systems

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`enterprise GenAI`、`runtime monitoring`、`security governance`

- 🎯 **研究动机**：企业GenAI安全落地缺管理层视角的实证总结
- 🔬 **研究方法**：基于C-level访谈与调研总结组织级安全治理与runtime monitoring经验
- 📌 **结论**：多数组织自评尚未准备好org-wide的GenAI安全防护

### 37. Structured Command Hijacking against Embodied Artificial Intelligence with Text-based Controls

📄 [arXiv](https://arxiv.org/abs/2510.00181) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`embodied AI`、`visual prompt injection`、`command hijacking`

👤 **作者**：Luis Burbano、…、Alvaro A Cardenas

- 🎯 **研究动机**：具身 AI 的多模态语言理解能力带来物理环境间接 prompt 注入新风险
- 🔬 **研究方法**：提出 CHAI：在视觉输入中嵌入误导标志等自然语言指令，系统搜索 token 空间构建 prompt 字典并引导攻击模型生成 Visual Attack Prompts
- 📌 **结论**：在无人机紧急降落、自动驾驶、空中目标跟踪与真实机器人车场景均超 SoTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a physical environment indirect prompt injection attack that exploits the multimodal language interpretation abilities of AI models. CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents: drone emergency landing, autonomous driving, aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

</details>

### 38. Temporal Misalignment Attacks against Multimodal Perception in Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2507.09095) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`autonomous driving`、`sensor desynchronization`、`multimodal perception`

👤 **作者**：Md Hasan Shahriar、…、Wenjing Lou

- 🎯 **研究动机**：多模态融合严格依赖相机与 LiDAR 的精确时间同步，车内网络的时间完整性攻击面未被研究
- 🔬 **研究方法**：提出 DejaVu 利用车内网络制造细微时间失配，并分析不同感知任务对传感器的不均衡敏感性
- 📌 **结论**：单帧 LiDAR 延迟使车辆检测 mAP 最多降 88.5%，三帧相机延迟使 MOTA 降 73%；硬件在环与 Autoware 仿真验证可致碰撞与幻影刹车

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal fusion (MMF) plays a critical role in the perception of autonomous driving, which primarily fuses camera and LiDAR streams for a comprehensive and efficient scene understanding. However, its strict reliance on precise temporal synchronization exposes it to new vulnerabilities. In this paper, we introduce DejaVu, an attack that exploits the in-vehicular network to manipulate the integrity of time and create subtle temporal misalignments, severely degrading downstream MMF-based perception tasks. Our comprehensive attack analysis across different models and datasets reveals the sensors' task-specific imbalanced sensitivities: object detection is overly dependent on LiDAR inputs, while object tracking is highly reliant on the camera inputs. Consequently, with a single-frame LiDAR delay, an attacker can reduce the car detection mAP by up to 88.5%, while with a three-frame camera delay, multiple object tracking accuracy (MOTA) for car drops by 73%. We further demonstrated two attack scenarios using an automotive Ethernet testbed for hardware-in-the-loop validation and the Autoware stack for end-to-end AD simulation, demonstrating the feasibility of the DejaVu attack and its severe impact, such as collisions and phantom braking. Our code and artifacts are publicly available at: https://github.com/shahriar0651/DejaVu.

</details>
### SoK 与 Position Papers

### 39. Position: Mind the Gap---Closing the Growing Disconnect Between Vulnerability Disclosure and AI Security

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`AI vulnerability disclosure`、`incident reporting`、`agent security`

- 🎯 **研究动机**：传统漏洞披露流程与AI安全实践脱节，AI漏洞缺规范上报机制
- 🔬 **研究方法**：分析AI（含agent）漏洞披露与事件报告的断层并提出改进方向
- 📌 **结论**：呼吁为AI系统建立适配的披露与响应机制

### 40. Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`implicit memory`、`temporal backdoor`、`covert channel`

- 🎯 **研究动机**：LLM虽无持久状态，隐式记忆仍可成为隐蔽通道
- 🔬 **研究方法**：阐明implicit memory作为temporal backdoor与covert channel的威胁模型
- 📌 **结论**：揭示跨上下文隐蔽通信与后门化新攻击面

### 41. SoK: On the Survivability of Backdoor Attacks on Unconstrained Face Recognition Systems

📄 [arXiv](https://arxiv.org/abs/2507.01607) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`survey`、`face recognition`、`backdoor survivability`、`system-level analysis`

👤 **作者**：Quentin Le Roux、Yannick Teglia、Teddy Furon、Philippe Loubet-Moundi、Eric Bourbao

- 🎯 **研究动机**：后门研究多针对孤立组件，完整人脸识别系统的系统级分析缺失
- 🔬 **研究方法**：组合针对人脸检测、反欺骗与特征提取器的后门文献，整体分析 20 种流水线配置与 15 种攻击场景
- 📌 **结论**：攻击者只需攻陷单个被后门模型即可波及整个人脸识别系统，并给出最佳实践与对策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread deployment of Deep Learning-based Face Recognition Systems raises many security concerns. While prior research has identified backdoor vulnerabilities on isolated components, Backdoor Attacks on real-world, unconstrained pipelines remain underexplored. This SoK paper presents the first comprehensive system-level analysis and measurement of the impact of Backdoor Attacks on fully-fledged Face Recognition Systems. We combine the existing Supervised Learning backdoor literature targeting face detectors, face antispoofing, and face feature extractors to demonstrate a system-level vulnerability. By analyzing 20 pipeline configurations and 15 attack scenarios in a holistic manner, we reveal that an attacker only needs a single backdoored model to compromise an entire Face Recognition System. Finally, we discuss the impact of such attacks and propose best practices and countermeasures for stakeholders.

</details>

### 42. SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2601.03979) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`survey`、`RAG privacy`、`attack taxonomy`、`mitigation maturity`

👤 **作者**：Andreea-Elena Bodea、Stephen Meisenbacher、Alexandra Klymenko、Florian Matthes

- 🎯 **研究动机**：RAG 隐私风险研究分散且缺乏统一系统化梳理
- 🔬 **研究方法**：系统文献综述 RAG 隐私相关工作，整理为完整的隐私风险分类法、缓解技术与评测策略，并给出 RAG Privacy Process Diagram
- 📌 **结论**：首次系统化 RAG 隐私风险与缓解，揭示缓解时的关键考量并评估现有方案的成熟度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The continued promise of Large Language Models (LLMs), particularly in their natural language understanding and generation capabilities, has driven a rapidly increasing interest in identifying and developing LLM use cases. In an effort to complement the ingrained "knowledge" of LLMs, Retrieval-Augmented Generation (RAG) techniques have become widely popular. At its core, RAG involves the coupling of LLMs with domain-specific knowledge bases, whereby the generation of a response to a user question is augmented with contextual and up-to-date information. The proliferation of RAG has sparked concerns about data privacy, particularly with the inherent risks that arise when leveraging databases with potentially sensitive information. Numerous recent works have explored various aspects of privacy risks in RAG systems, from adversarial attacks to proposed mitigations. With the goal of surveying and unifying these works, we ask one simple question: What are the privacy risks in RAG, and how can they be measured and mitigated? To answer this question, we conduct a systematic literature review of RAG works addressing privacy, and we systematize our findings into a comprehensive set of privacy risks, mitigation techniques, and evaluation strategies. We supplement these findings with two primary artifacts: a Taxonomy of RAG Privacy Risks and a RAG Privacy Process Diagram. Our work contributes to the study of privacy in RAG not only by conducting the first systematization of risks and mitigations, but also by uncovering important considerations when mitigating privacy risks in RAG systems and assessing the current maturity of proposed mitigations.

</details>

### 43. SoK: The Hitchhiker’s Guide to Efficient, End-to-End, and Tight DP Auditing

📄 [arXiv](https://arxiv.org/abs/2506.16666) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`survey`、`DP auditing`、`privacy attack`、`audit tightness`

👤 **作者**：Meenatchi Sundaram Muthu Selva Annamalai、Borja Balle、Jamie Hayes、Georgios Kaissis、Emiliano De Cristofaro

- 🎯 **研究动机**：差分隐私审计研究分散，缺乏系统化框架与统一评价标准
- 🔬 **研究方法**：提出效率、端到端、紧致性三项审计目标，系统梳理 SoTA DP 审计的威胁模型、攻击方式与评估函数
- 📌 **结论**：指出既有工作忽视的关键细节、三项目标的限制因素与开放研究问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we systematize research on auditing Differential Privacy (DP) techniques, aiming to identify key insights and open challenges. First, we introduce a comprehensive framework for reviewing work in the field and establish three cross-contextual desiderata that DP audits should target -- namely, efficiency, end-to-end-ness, and tightness. Then, we systematize the modes of operation of state-of-the-art DP auditing techniques, including threat models, attacks, and evaluation functions. This allows us to highlight key details overlooked by prior work, analyze the limiting factors to achieving the three desiderata, and identify open research problems. Overall, our work provides a reusable and systematic methodology geared to assess progress in the field and identify friction points and future directions for our community to focus on.

</details>