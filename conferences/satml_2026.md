# IEEE SaTML 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [LLM、RAG 与 Prompt Injection](#llmrag-与-prompt-injection)
- [投毒、后门与开发供应链](#投毒后门与开发供应链)
- [隐私泄漏、成员推断与联邦学习攻击](#隐私泄漏成员推断与联邦学习攻击)
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
- 最终收录：46
- 收录口径：逐篇阅读官网摘要，只收录具有明确攻击者、隐私泄漏、安全失效、恶意使用、认证防御、安全治理或可操作缓解问题设定的论文；传统对抗鲁棒性仅在论文给出具体攻击或认证防御 threat model 时保留。
- 边界案例：一般差分隐私实现、同态加密推理、模型解释、公平性、near-OOD、数据最小化和协作学习立场论文虽然属于广义 trustworthy ML，但没有把可核验的 AI 安全风险作为核心问题，因而从严排除。

## 论文分类

### LLM、RAG 与 Prompt Injection

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| BinaryShield: Cross-Service Threat Intelligence in LLM Services using Privacy-Preserving Fingerprints | Waris Gill, Natalie Isak, Matthew Dressman | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | defense、prompt injection、privacy-preserving fingerprint、threat intelligence | 针对不同合规边界下的 LLM 服务无法共享恶意 prompt 原文的问题，BinaryShield 以 PII 清理、二值量化和 randomized response 生成攻击指纹，取得 0.94 F1 并将相似度检索加速 38 倍。 |
| Certifiably Robust RAG against Retrieval Corruption | Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2405.15556) | [Code](https://github.com/inspire-group/RobustRAG) | defense、RAG corruption、isolate-then-aggregate、certified robustness | 针对攻击者向检索结果注入恶意段落的问题，RobustRAG 隔离处理各段落后安全聚合回答，并对有界注入给出可证明的正确性下界。 |
| Defeating Prompt Injections by Design | Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, Florian Tramèr | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2503.18813) | [Code](https://github.com/google-research/camel-prompt-injection) | defense、LLM agent、prompt injection、capability enforcement | 针对 Agent 把不可信工具输出与可信指令混入同一上下文的根本缺口，CaMeL 分离 control flow 与 data flow 并执行 capability policy；最新版在 AgentDojo 上以可证明安全方式完成 77% 任务，接近无防御系统的 84%。 |
| Defending Against Prompt Injection with DataFilter | Yizhu Wang, Sizhe Chen, Raghad Alkhudair, Basel Alomair, David Wagner | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2510.19207) | [Code](https://github.com/yizhu-joy/DataFilter) | defense、prompt injection、test-time sanitization、black-box LLM | 针对现有防御依赖权重访问、牺牲效用或改造系统的问题，DataFilter 在数据进入后端 LLM 前移除恶意指令，在多个 benchmark 上把 ASR 降至接近零并保持正常任务效用。 |
| Safe But Not Robust: Security Evaluation of VLM by Jailbreaking MSTS | Wenxin Ding, Cong Chen, Jean-Philippe Monteuuis, Jonathan Petit | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | benchmark、VLM jailbreak、Robust-MSTS、safety evaluation | 针对 MSTS 未覆盖对抗式越狱的问题，Robust-MSTS 加入定向图像扰动并评测多种 VLM，观察到最高 98.5% ASR，同时分析量化缓解与 VLM-as-a-Judge 的可靠性。 |
| Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs | Jean-Charles Noirot Ferrand, Yohan Beugin, Eric Pauley, Ryan Sheatsley, Patrick McDaniel | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2501.16534) | [Code](https://github.com/jcnf0/targeting-alignment) | attack、safety classifier、surrogate extraction、jailbreak transfer | 针对 aligned LLM 内部拒绝边界可被建模的问题，作者从部分网络抽取 F1 超过 80% 的 surrogate safety classifier，并把转移攻击 ASR 从直接攻击的 22% 提高到 70%。 |

### 投毒、后门与开发供应链

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Architectural Backdoors for Within-Batch Data Stealing and Model Inference Manipulation | Nicolas Küchler, Ivan Petrov, Conrad Grobler, Ilia Shumailov | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2505.18323) | 暂未公开 | attack、architectural backdoor、batch isolation、information-flow control | 针对恶意模型架构可跨 batch 窃取或篡改其他用户输入输出的问题，作者构造 within-batch backdoor，并用信息流 non-interference 检查给出形式化防御且发现 200 余个模型存在非预期泄漏。 |
| One RNG to Rule Them All - How Randomness Becomes an Attack Vector in Machine Learning | Kotekar Annapoorna Prabhu, Andrew Gan, Zahra Ghodsi | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2602.09182) | 暂未公开 | defense、ML supply chain、PRNG vulnerability、runtime enforcement | 针对 ML 框架及软硬件依赖中的伪随机实现可能形成隐蔽攻击面的风险，RNGGUARD 静态定位随机调用并在运行时替换不安全实现，以低改造成本约束随机源。 |
| Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated | Hanna Foerster, Ilia Shumailov, Yiren Zhao, Harsh Chaudhari, Jamie Hayes, Robert Mullins, Yarin Gal | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2509.05739) | 暂未公开 | attack、reasoning model、data poisoning、decomposed trigger | 针对 reasoning LLM 的 chain-of-thought 扩大投毒面的风险，decomposed reasoning poison 只篡改推理路径并拆分 trigger；实验同时表明模型常能从已触发的中间后门中恢复最终答案。 |

### 隐私泄漏、成员推断与联邦学习攻击

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage | Rui Xin, Niloofar Mireshghallah, Shuyue Stella Li, Michael Duan, Hyunwoo Kim, Yejin Choi, Yulia Tsvetkov, Sewoong Oh, Pang Wei Koh | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、text sanitization、semantic re-identification、privacy leakage | 针对只检查显式 PII 会高估文本脱敏效果的问题，作者用语义重识别攻击评测病历和对话数据，发现 Azure PII removal 仍保留 89% 的原始可推断信息。 |
| DeepLeak: Privacy Enhancing Hardening of Model Explanations Against Membership Leakage | Firas Ben Hmida, Zain Sbeih, Philemon Hailemariam, Birhanu Eshete | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2601.03429) | [Code](https://github.com/um-dsp/DeepLeak) | defense、model explanation、membership inference、privacy hardening | 针对 post-hoc explanation 暴露训练成员身份的问题，DeepLeak 审计 15 种解释技术并用噪声、裁剪和 masking 加固，将泄漏最多降低 95%，平均效用损失为 3.3%。 |
| FedSpy-LLM: Towards Scalable and Generalizable Data Reconstruction Attacks from Gradients on LLMs | Syed Irfan Ali Meerza, Feiyi Wang, Jian Liu | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2604.06297) | 暂未公开 | attack、federated LLM、gradient inversion、PEFT leakage | 针对 federated LLM 在大 batch、长序列和 PEFT 下仍可能泄漏文本的问题，FedSpy-LLM 利用梯度秩亏与子空间分解恢复 token，再迭代重建顺序并跨多类架构泛化。 |
| Kraken: Higher-order EM side-channel attacks on DNNs in near and far field | Peter Horvath, Ilia Shumailov, Lukasz Chmielewski, Lejla Batina, Yuval Yarom | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、EM side channel、LLM weight extraction、physical model stealing | 针对物理侧信道可绕过 API 查询式模型窃取限制的问题，Kraken 以高阶相关分析从 Tensor Core 执行中恢复 LLM 权重，并在一米距离及玻璃阻隔下验证远场可行性。 |
| Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering | Tejas Kulkarni, Antti Koskela, Laith Zumot | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2605.04116) | 暂未公开 | attack、retrieval-based ICL、membership inference、black-box access | 针对文档问答服务按相似度检索 in-context examples 时的数据库泄漏，作者提出两种基于 query prefix 的黑盒 MIA，在 paraphrase 场景下仍有效并用 ensemble prompting 显著缓解。 |
| On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models | Ali Al Sahili, Ali Chehab, Razan Tajeddine | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2512.13352) | 暂未公开 | analysis、LLM memorization、membership inference、targeted extraction | 针对常规 MIA benchmark 不能直接说明其对真实训练数据提取的帮助，作者把多种 MIA 接入 targeted extraction pipeline，并比较其集成表现与传统评测排名。 |
| On the Fragility of Contribution Evaluation in Federated Learning | Balázs Pejó, Marcell Frank, Krisztián Varga, Péter Veliczky, Gergely Biczók | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、federated learning、contribution manipulation、poisoning | 针对联邦学习贡献分数可能决定激励与治理的问题，作者验证聚合算法变化和恶意 client poisoning 都能显著扭曲参与者得分，说明现有贡献评估缺乏攻击鲁棒性。 |
| Privacy Risks in Time Series Forecasting: User- and Record-Level Membership Inference | Nicolas Johansson, Tobias Olsson, Daniel Nilsson, Johan Östman, Fazeleh Hoseini | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2509.04169) | 暂未公开 | attack、time-series forecasting、membership inference、user-level leakage | 针对时序预测模型的成员隐私风险缺少系统评测，作者改造 LiRA 并提出 DTS attack，在 EEG 与用电数据上发现 user-level inference 有时达到完美检测。 |
| Reconstructing Training Data from Models Trained with Transfer Learning | Yakir Oz, Gilad Yehudai, Gal Vardi, Itai Antebi, Michal Irani, Niv Haim | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、transfer learning、training reconstruction、embedding leakage | 针对既有训练集重构只适用于小模型和低分辨率数据的问题，作者转而在 DINO-ViT 与 CLIP embedding space 中求解并以聚类筛选候选，扩展了真实 transfer learning 的泄漏分析。 |
| Training Set Reconstruction from Differentially Private Forests: How Effective is DP? | Alice Gorgé, Julien Ferry, Sébastien Gambs, Thibaut Vidal | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2502.05307) | 暂未公开 | attack、differential privacy、forest reconstruction、constraint programming | 针对 DP decision forest 的形式保证是否抵抗具体重构攻击，作者用 constraint programming 搜索最可能训练数据，发现可用精度下仍存在泄漏而完全稳健配置不优于常数分类器。 |
| Your Privacy Depends on Others: Collusion Vulnerabilities in Individual Differential Privacy | Johannes Kaiser, Alexander Ziller, Eleni Triantafillou, Daniel Rückert, Georgios Kaissis | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2601.12922) | 暂未公开 | attack、individual DP、collusion、membership inference | 针对 individual DP 声称由个人预算控制风险但实际受他人预算影响的问题，作者构造合谋攻击并命中 62% 的目标，再提出带额外 divergence 上界的隐私合约。 |

### 安全更新、Unlearning 与可验证推理

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Evaluating Deep Unlearning in Large Language Models | Ruihan Wu, Chhavi Yadav, Ruslan Salakhutdinov, Kamalika Chaudhuri | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2410.15153) | [Code](https://github.com/wrh14/deep_unlearning) | benchmark、LLM unlearning、deductive knowledge、forgetting evaluation | 针对删除单一事实不代表其逻辑推论也被删除的问题，作者定义 deep unlearning 并构建 Eval-DU，发现现有方法要么遗留可推导信息、要么过度删除无关事实。 |
| Exact Unlearning of Finetuning Data via Model Merging at Scale | Kevin Kuo, Amrith Setlur, Kartik Srinivas, Aditi Raghunathan, Virginia Smith | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2504.04626) | 暂未公开 | defense、exact unlearning、model merging、SIFT-Masks | 针对 approximate unlearning 可被攻击恢复且 exact unlearning 成本高的问题，SIFT-Masks 用局部 mask 和符号约束合并模型，较 naive merge 提高 5%–80% 准确率并最多节省 250 倍计算。 |
| Gauss-Newton Unlearning for the LLM Era | Lev McKinney, Anvith Thudi, Juhan Bae, Tara Rezaei Kheirkhah, Nicolas Papernot, Sheila A. McIlraith, Roger Baker Grosse | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2602.10568) | 暂未公开 | defense、LLM unlearning、Gauss-Newton update、retain utility | 针对 LLM 遗忘敏感输出时容易破坏 retain set 的问题，K-FADE 用少量 K-FAC 近似 Gauss-Newton 上升步约束更新，在 WMDP 与 ToFU 上改善遗忘—保留权衡并可在后续训练后重新施加。 |
| Provably Safe Model Updates | Leo Elmecker-Plakolm, Pierre Fasterling, Philip Sosnin, Calvin Tsay, Matthew Wicker | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2512.01899) | 暂未公开 | defense、safe update、parameter certification、alignment drift | 针对模型更新可能引发 catastrophic forgetting 或 alignment drift，作者求解满足规格的局部不变参数域并投影任意更新，在持续学习与基础模型微调中提供形式安全保证。 |
| RobPI: Robust Private Inference against Malicious Client | Jiaqi Xue, Mengxin Zheng, Qian Lou | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | defense、private inference、malicious client、cryptographic protocol | 针对 private inference 普遍只假设 semi-honest client 的缺口，作者先构造少 3–8 倍查询的输出操纵攻击，再以 RobPI 将攻击成功率降低约 91.9% 并把所需查询提高十倍以上。 |
| Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference | Pranay Anchuri, Matteo Campanelli, Paul Cesaretti, Rosario Gennaro, Tushar M. Jois, Hasan S. Kayman, Tugce Ozdemir | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2603.19025) | 暂未公开 | defense、verifiable inference、execution trace、lightweight proof | 针对云端 AI inference 的模型来源和执行正确性难以验证且通用证明开销过高的问题，作者只承诺 execution trace 并抽查少量位置，在攻击韧性实验中实现较既有方案数量级的性能提升。 |

### 指纹、模型权属与生成内容保护

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Are Robust LLM Fingerprints Adversarially Robust? | Anshul Nasery, Edoardo Contente, Alkin Kaz, Pramod Viswanath, Sewoong Oh | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、LLM fingerprint、ownership verification、adaptive evasion | 针对 LLM fingerprint 主要只测良性微调和合并的问题，作者建立恶意规避 threat model 并按设计漏洞构造 adaptive attack，可在保持普通用户效用时完全绕过多种模型认证方案。 |
| Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes | Xavier Pleimling, Sifat Muhammad Abdullah, Gunjan Balde, Peng Gao, Mainack Mondal, Murtuza Jadliwala, Bimal Viswanath | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2602.22197) | [Code](https://github.com/mlsecviswanath/img2imgdenoiser) | attack、image protection、generative denoising、defense bypass | 针对图像水印、风格防护和 deepfake shield 依赖微小保护扰动的问题，作者仅用现成 image-to-image 模型和简单去噪 prompt 即跨 8 个案例绕过 6 类方案，并优于专用攻击。 |
| Protecting Facial Biometrics from Malicious Generative Editing via Latent Optimization | Fahad Shamshad, Hashmat Shadab Malik, Muzammal Naseer, Salman Khan, Karthik Nandakumar | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | defense、facial biometrics、malicious editing、latent optimization | 针对 diffusion editing 可保留身份并生成有害人脸篡改且像素防护易被净化的问题，FaceGuardian 在身份敏感 latent subspace 优化保护扰动，在变换和 diffusion purification 下仍提高最多 12% 的人脸识别保护指标。 |
| Smudged Fingerprints: A Systematic Evaluation of the Robustness of AI Image Fingerprints | Kai Yao, Marc Juarez | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2512.11771) | [Code](https://github.com/kaikaiyao/SmudgedFingerprints) | attack、AI image fingerprint、removal and forgery、attribution robustness | 针对生成图像指纹只在干净设置下表现良好的问题，作者以五种攻击评测 14 类方法，发现移除在白盒场景常超过 80% 成功率、受限黑盒场景仍超过 50%。 |

### 对抗攻击、认证与安全应用评测

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Accelerating Targeted Hard-Label Adversarial Attacks in Low-Query Black-Box Settings | Arjhun Swaminathan, Mete Akgün | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2505.16313) | 暂未公开 | attack、hard-label attack、targeted evasion、query efficiency | 针对 hard-label 黑盒定向攻击在窄决策区域中查询成本高的问题，TEA 利用目标图像边缘构造更优初始化，在多模型低查询设置下把所需查询减少近 70%。 |
| Beyond the TESSERACT: Trustworthy Dataset Curation for Sound Evaluations of Android Malware Classifiers | Theo Chow, Mario D'Onghia, Lorenz Linhardt, Zeliang Kan, Daniel Arp, Lorenzo Cavallaro, Fabio Pierazzi | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | benchmark、malware classifier、dataset curation、evaluation validity | 针对 Android malware classifier 的安全结论因数据集构造差异而互相矛盾的问题，作者识别五类常被忽略的偏差来源，并提出可复核的 dataset curation 与评测方法。 |
| Cascading Robustness Verification: Toward Efficient Model‑Agnostic Certification | Mohammadreza Maleki, Rushendra Sidibomma, Arman Adibi, Reza Samavi | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2602.04236) | 暂未公开 | defense、robustness verification、verifier cascade、certified accuracy | 针对单一 incomplete verifier 因松弛误报不鲁棒且高精度方案成本高的问题，CRV 逐级调用多种验证器并逐步加约束，在不降低认证数量时最多缩短约 90% 运行时间。 |
| Efficient Semi-Supervised Adversarial Training via Latent Clustering-Based Data Reduction | Somrita Ghosh, Yuelin Xu, Xiao Zhang | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2501.10466) | 暂未公开 | defense、adversarial training、latent clustering、data reduction | 针对 semi-supervised adversarial training 依赖大量额外数据的问题，作者按 latent decision boundary 选择或生成关键样本，以少 5–10 倍无标签数据保持近似 robust accuracy 并将总运行时间缩短约 3–4 倍。 |
| On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses | Mohamed Djilani, Thibault Simonetto, Karim Tit, Florian Tambon, Salah Ghamizi, Maxime Cordy, Mike Papadakis | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、tabular foundation model、test-time evasion、in-context defense | 针对 TabPFN 与 TabICL 的对抗边界尚不明确，作者在金融、网络安全和医疗任务中验证结构化扰动及跨模型 transfer，并用 adversarial in-context replacement 改善鲁棒性。 |
| RobustBlack: Challenging Black-Box Adversarial Attacks on State-of-the-Art Defenses | Mohamed DJILANI, Salah GHAMIZI, Maxime CORDY | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | benchmark、black-box attack、robust defense、transferability | 针对黑盒攻击往往只在弱防御上得出过强结论的问题，作者让 13 种攻击对抗八种 ImageNet 防御，发现强白盒鲁棒模型也明显压低黑盒攻击成功率且 surrogate–target 鲁棒性匹配至关重要。 |
| The Feature-Space Illusion: Exposing Practical Vulnerabilities in Blockchain GNN Fraud Detection | François Frankart, Thibault Simonetto, Maxime Cordy, Orestis Papageorgiou, Nadia Pocher, Gilbert Fridgen | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | attack、blockchain GNN、transaction synthesis、fraud evasion | 针对任意 feature perturbation 无法反映区块链真实攻击成本的问题，作者把 GNN 梯度转为可执行交易并发现 GATv2 仅需 2–3 笔交易即可达到 78.4% ASR，而 GraphSAGE 抵抗率为 85.2%。 |

### 智能体、具身系统与高风险应用

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading | Advije Rizvani, Giovanni Apruzzese, Pavel Laskov | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2601.13082) | [Code](https://github.com/AdvijeR/satml26_adversarial-news) | attack、algorithmic trading、adversarial headline、financial impact | 针对 LLM sentiment 被交易系统直接采用所形成的经济攻击面，作者以 Unicode homoglyph 和隐藏文本篡改单日新闻，在真实回测中使年化收益最多下降 17.7 个百分点。 |
| “Org-Wide, We’re Not Ready": C-Level Lessons on Securing Generative AI Systems | Elnaz Rabieinejad Balagafsheh, Ali Dehghantanha, Fattane Zarrinkalam | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | analysis、enterprise GenAI、runtime monitoring、security governance | 针对企业部署 GenAI 快于其安全能力建设的问题，作者访谈 20 名 CISO，发现数据泄漏、prompt/model misuse 与 deepfake fraud 最突出，而 runtime telemetry 和端到端 red teaming 准备最弱。 |
| Structured Command Hijacking against Embodied Artificial Intelligence with Text-based Controls | Luis Burbano, Diego Ortiz, Qi Sun, Siwei Yang, Haoqin Tu, Cihang Xie, Yinzhi Cao, Alvaro A Cardenas | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2510.00181) | 暂未公开 | attack、embodied AI、visual prompt injection、command hijacking | 针对具身 LVLM 会把环境文字当作控制命令，CHAI 以 token search、字典和攻击模型生成欺骗性视觉提示；在无人机迫降、自动驾驶、空中跟踪和真实机器人车上均优于既有攻击，并产生可执行物理后果。 |
| Temporal Misalignment Attacks against Multimodal Perception in Autonomous Driving | Md Hasan Shahriar, Md Mohaimin Al Barat, Harshavardhan Sundar, Ning Zhang, Naren Ramakrishnan, Y. Thomas Hou, Wenjing Lou | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2507.09095) | [Code](https://github.com/shahriar0651/DejaVu) | attack、autonomous driving、sensor desynchronization、multimodal perception | 针对 camera–LiDAR fusion 对精确同步的依赖，DejaVu 从车载网络注入延迟，一帧 LiDAR 延迟使车辆检测 mAP 最多下降 88.5%，三帧 camera 延迟使 MOTA 下降 73%，并在硬件与仿真中造成碰撞和幽灵制动。 |

### SoK 与 Position Papers

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Position: Mind the Gap---Closing the Growing Disconnect Between Vulnerability Disclosure and AI Security | Lukas Bieringer, Sean McGregor, Nicole Nichols, Kevin Paeth, Jochen Staengler, Andreas Wespi, Alexandre Alahi, Kathrin Grosse | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | analysis、AI vulnerability disclosure、incident reporting、agent security | 针对传统漏洞披露和一般 AI incident reporting 无法覆盖模型行为、知识产权与责任归属的问题，作者主张建立专门的 AI security reporting 流程，并指出智能体会进一步放大现有缺口。 |
| Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs | Ahmed Salem, Andrew Paverd, Sahar Abdelnabi | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | analysis、implicit memory、temporal backdoor、covert channel | 针对 LLM session 被默认视为无状态的假设，作者展示模型可把隐藏状态编码进自身输出并在重输入时恢复，由此构造 time-bomb backdoor，并讨论跨智能体隐蔽通信、评测作弊与投毒风险。 |
| SoK: On the Survivability of Backdoor Attacks on Unconstrained Face Recognition Systems | Quentin Le Roux, Yannick Teglia, Teddy Furon, Philippe Loubet Moundi, Eric Bourbao | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2507.01607) | 暂未公开 | survey、face recognition、backdoor survivability、system-level analysis | 针对后门研究通常只测试孤立分类器的问题，该 SoK 跨 20 种完整人脸识别 pipeline 和 15 种攻击场景分析传播性，证明单个 feature extractor 后门可危及整个系统。 |
| SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems | Andreea-Elena Bodea, Stephen Meisenbacher, Alexandra Klymenko, Florian Matthes | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2601.03979) | 暂未公开 | survey、RAG privacy、attack taxonomy、mitigation maturity | 针对 RAG 将敏感知识库接入 LLM 后缺少统一隐私视图的问题，该 SoK 系统化风险、攻击、缓解与评测方法，并以 taxonomy 和 process diagram 指出现有缓解方案的成熟度缺口。 |
| SoK: The Hitchhiker’s Guide to Efficient, End-to-End, and Tight DP Auditing | Meenatchi Sundaram Muthu Selva Annamalai, Borja Balle, Jamie Hayes, Georgios Kaissis, Emiliano De Cristofaro | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2506.16666) | 暂未公开 | survey、DP auditing、privacy attack、audit tightness | 针对 DP 机制的经验审计缺少共同评价框架，该 SoK 以效率、端到端性和紧致性三项 desiderata 统一 threat model、攻击与指标，并归纳当前瓶颈和开放问题。 |

## 核验记录

- 核验日期：2026-08-23。
- 录用状态：完整遍历官网 Accepted Papers 的 62 个条目，并以官网 Program 交叉确认会议展示安排；最终 46 篇均来自该官方录用表。
- 标题与作者：46 篇标题、作者及顺序逐项对照官方页面；同一论文在文件内仅出现一次，各分表已按英文标题字母序排列。
- 论文与代码：补充核验到 30 个 arXiv abstract page 和 10 个作者或机构官方 GitHub artifact；没有可靠公开入口的条目统一标记为“暂未公开”，仅有论文明确声明而未定位仓库的条目按规范注明待核实。
- 摘要事实：46 条总结均对照官网完整摘要，涉及指标时保留原始适用范围，不把一般 trustworthy ML 结果外推为 AI Safety 结论。
- 未决项：IEEE Computer Society Digital Library 的完整 proceedings 入口尚未定位；个别论文在官网有摘要但没有独立公开论文页，后续可在正式论文集上线后补齐 DOI 与页码。
