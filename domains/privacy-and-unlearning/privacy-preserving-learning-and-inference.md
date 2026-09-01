# 隐私攻击评测与泄漏缓解

[返回上级目录](README.md)

## 研究方向

研究如何通过明确攻击检验模型、表示、记忆与上下文是否泄漏数据，并针对 memory extraction、attribute inference、embedding/model inversion、训练样本记忆和身份恢复提出可验证缓解。一般 privacy-preserving learning/inference、data minimization、最小披露，以及 Differential Privacy、federated learning、密码学、secure computation、secure inference、homomorphic encryption、MPC、zero-knowledge proof、数字签名、区块链和 TEE 不属于本页范围；以 federated learning 为研究对象或训练框架的攻击与防御同样不收录。

## 研究脉络

- **泄漏审计：** behavioral canary、targeted query 与 prior-aware metric 用于区分训练记忆、上下文泄漏、统计常见生成和评测假阳性。
- **攻击驱动缓解：** memory extraction honeypot、记录级 vulnerability estimation 和局部模型干预需要以具体攻击成功率验证，而不只报告抽象 privacy–utility score。
- **反演与属性推断：** 噪声保护表示、模型特征和公开内容仍可能被重建或组合为敏感属性，研究重点是攻击能力、边界与定向防护。
- **多模态泄漏：** image、diffusion feature、face identity 与 location clue 的保护必须面对恢复、未经授权个性化或定位攻击。
- **当前边界：** 不验证具体泄漏 threat model 的一般隐私保护、最小披露、密码学、DP、FL 和 secure inference 路线不纳入。

## 训练与上下文泄漏审计

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools ↗ | attack、runtime-context leakage、malicious tool、adaptive exfiltration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27800) | 暂未公开 | 针对恶意工具能否诱导 Agent 主动把 user prompt、执行轨迹与 tool list 当作参数泄漏，ContextLeak 以强化学习优化工具名称和描述，并用多样化 shadow context 训练可迁移攻击者；即使受害上下文与训练分布明显不同，攻击仍保持较高披露效果。 |
| 2026&#8209;08 | Inadvertent Context Leakage in Language Models | attack、context leakage、adaptive black-box extraction、covert carrier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19857) | 暂未公开 | 针对模型拒绝直接复述秘密并不代表私有 context 不会影响良性输出，论文训练自适应黑盒攻击者利用隐藏相关性把模型变成 covert carrier；八个专有模型上可近乎完整恢复两位秘密、以 82% 成功率恢复四位秘密，并能从生产式 Agent context 抽取完整 SSN。 |
| 2026&#8209;04 | Behavioral Canaries: Auditing Private Retrieved Context Usage in RL Fine-Tuning | detection、private-context misuse、behavioral canary、training audit | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.22191) | [Code](https://github.com/CRChenCode/behavioral_canary) | 针对 RL fine-tuning 主要改变行为风格而常规 memorization audit 无法验证受保护文档是否被违规训练，Behavioral Canaries 植入 trigger-conditioned preference，在 1% canary 比例下以 10% FPR 达到 67% 检出率和 0.756 AUROC。 |
| 2026 | *MemPot*: Defend Against Memory Extraction Attack with Optimized Honeypots | defense、memory extraction、optimized honeypot、leakage mitigation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62415) | [Project](https://wangyuhao06.github.io/mempot-website/) | 针对 LLM Agent 的内外部 memory 可被抽取且缺少专门防御的问题，MemPot 向记忆库注入对攻击查询高可检索、对正常用户隐蔽的优化 honeypot，并用序贯概率比检验识别攻击；实验报告检测 AUROC 提升 50%、低误报率下 TPR 提升 80%，且不增加在线推理延迟。 |
| 2025&#8209;12 | ContextLeak: Auditing Leakage in Private In-Context Learning Methods | detection、private ICL、canary audit、context leakage | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2512.16059) | 暂未公开 | 针对 private ICL 方法缺少最坏情况实证审计，ContextLeak 向敏感 exemplar 植入可识别 canary 并设计 targeted query，检测到泄漏会随理论 privacy budget 单调增加，且现有方法常在完全泄漏与严重效用损失间二选一。 |

## 反演、属性推断与攻击驱动防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings | attack、noise-aware inversion、Double Noise Trap、text reconstruction | 未确认（arXiv Comments：Accepted by IEEE ICDM 2026） | [arXiv](https://arxiv.org/abs/2608.18610) | 暂未公开 | 针对加入 Gaussian noise 的 text embedding 被视为足以抵御生成式反演，论文定位标准方法的 Double Noise Trap，并提出以 SURE 无监督训练 residual denoising autoencoder、再执行生成重建的 DAEI；在只能观察含噪向量时，其 BLEU 相对基线提高约 154%，token F1 与 ROUGE-L 提高 32%–60%，直接推翻简单噪声保护的安全假设。 |
| 2026&#8209;08 | Black-Box Embedding Inversion Attack on Vector Databases ↗ | attack、vector-database leakage、black-box inversion、content reconstruction | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817917) | 暂未公开 | 针对数据库以 embedding 代替明文并只开放黑盒检索便被视为隐私保护的问题，论文利用交互反馈恢复存储内容和敏感语义；结果证明表示封装本身不能阻止自适应反演，隐私防护必须用具体 reconstruction threat model 验证。 |
| 2026&#8209;08 | AccretionLink: On-Device Auditing of Exposure-Control Attacks on Attribute Inference | detection、attribute inference、exposure-control attack、on-device audit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14735) | 暂未公开 | 曝光控制可以让对手对真实的公共帖子进行排名，以在不改变内容的情况下加强私人属性推断；AccretionLink 为这种攻击定义了机密性和完整性博弈，通过部分识别对有界选择几率进行建模，并构建依赖感知的时间统一电子流程。 |
| 2026&#8209;08 | Secrets Everywhere: Auditing Memorization in Mobility Prediction Models | detection、mobility memorization、trajectory leakage、data extraction | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2608.02052) | 暂未公开 | 针对 mobility prediction model 可能记忆并泄漏训练用户轨迹的问题，作者以 user-grounded reference set 在位置、anchor pair 和子轨迹三种粒度审计，发现记忆普遍存在、与行为规律性相关且会提高推理时数据抽取风险。 |
| 2026&#8209;02 | A Prior-Aware Metric for Efficiently Distinguishing Memorization from Generalization in Large Language Models | detection、memorization audit、prior correction、false positive | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2602.18733) | 暂未公开 | 针对把统计常见生成误判为训练数据记忆会夸大隐私、版权与安全风险，Prior-Aware memorization 提出免重训判据，并发现既有方法标为 memorized 的序列中有 55%–90% 更符合统计常见性。 |
| 2026 | Random Erasing vs. Model Inversion: A Promising Defense or a False Hope? | defense、model inversion、random erasing、attack evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/68773) | [Project](https://ngoc-nguyen-0.github.io/MIDRE/) | 针对 model inversion 可从模型重建私有训练图像的问题，论文发现训练时 Random Erasing 会拉开反演图像与私有数据的特征距离，同时维持类别可分性；37 组实验中该简单数据增强跨攻击、网络和配置降低重建质量与攻击准确率，并保持合理的正常准确率。 |
| 2026 | Provably Protecting Fine-Tuned LLMs from Training Data Extraction while Preserving Utility | defense、training-data extraction、provable protection、utility retention | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61875) | 暂未公开 | 针对敏感数据微调后的 LLM 会遭受 training-data extraction、而既有防御缺少保证或严重损伤效用的问题，SCP-$\Delta_r$ 保留少量高影响 token 的相对概率偏移并用 base model 平滑其余偏移，在 Near Access Freeness 框架下给出更强理论界，同时以较小性能损失降低抽取风险。 |
| 2026 | Can we estimate privacy vulnerability of individual records? Towards Mitigating Attribute Inference Attacks on ML Models | detection、attribute inference、AttriVET、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kabir) | 暂未公开 | 针对 attribute inference 风险在不同训练记录间高度不均的问题，作者提出 NeighVE、VESL 与 AttriVET 估计并预测记录级 vulnerability，预测准确率超过 90%，从而以较小效用损失实施定向缓解。 |

## 多模态泄漏与攻击驱动防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | You Don’t Need All That Attention: Surgical Memorization Mitigation in Text-to-Image Diffusion Models | defense、diffusion memorization、attention mitigation、training-data leakage | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65409) | 暂未公开 | 针对文生图 diffusion model 可能逐字或近似复现训练图像的问题，GUARD 在推理时以吸引—排斥引导远离被记忆图像，并自动定位需削弱的 prompt cross-attention；它在两种架构、verbatim 与 template memorization 上稳定降低复现，同时保持 prompt 对齐和图像质量。 |
| 2026 | Vulnerability of Privacy-Preserving Visual Localization against Diffusion-based Attacks | detection、visual localization、privacy attack、cyber misuse | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4261) | [Code](https://github.com/MaximePi/benchmark-privacy-inversion) | 针对视觉定位表示被宣称为隐私保护却缺少统一攻击验证的问题，作者用扩散反演从多种表示恢复敏感场景并建立比较基准，证明现有方案仍会泄漏可识别内容。 |
| 2026 | Protecting Facial Biometrics from Malicious Generative Editing via Latent Optimization | defense、facial biometrics、malicious editing、latent optimization | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | 针对 diffusion editing 可保留身份并生成有害人脸篡改且像素防护易被净化的问题，FaceGuardian 在身份敏感 latent subspace 优化保护扰动，在变换和 diffusion purification 下仍提高最多 12% 的人脸识别保护指标。 |
| 2026 | IdentityMask: A Robust Face-Centric Privacy Protection Against Unauthorized Personalization of Diffusion Models | defense、face privacy、unauthorized personalization、feature corruption | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3488.pdf) | 暂未公开 | 针对扩散个性化可盗用个人身份且全图扰动效率低，IdentityMask 沿个性化时空动态定向破坏核心身份编码，并抵抗净化与后处理。 |
| 2025&#8209;11 | GEO-Detective: Unveiling Location Privacy Risks in Images with LLM Agents | attack、location inference、LLM agent、image privacy | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5191) · [arXiv](https://arxiv.org/abs/2511.22441) | 暂未公开 | 针对普通用户可借 LVLM 推断社交图像地点的风险，GEO-Detective 模拟人类分步推理并调用反向搜图等工具，国家级定位较基线提升逾 11.1% 且现有防御难以阻止。 |
| 2025&#8209;08 | Protego: User-Centric Pose-Invariant Privacy Protection Against Face Recognition-Induced Digital Footprint Exposure | defense、face recognition、pose-invariant protection、digital footprint | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Protego_User-Centric_Pose-Invariant_Privacy_Protection_Against_Face_Recognition-Induced_Digital_Footprint_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2508.02034) | [Code](https://github.com/HKU-TASR/Protego) | 针对社交照片可被跨姿态人脸检索串联成个人数字足迹，Protego 生成用户专属且姿态不变的保护信号，降低未经授权的身份匹配。 |

## Survey 与系统边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation | survey、RAG privacy、pipeline threat model、stage-specific defense | 未确认（arXiv Comments：Accepted to Findings of EMNLP 2026） | [arXiv](https://arxiv.org/abs/2608.24977) | [Repository](https://github.com/coutMinh/A-Survey-on-RAG-Robustness) | 综述将隐私泄漏列为 RAG 攻击的三类核心目标之一，并沿 corpus、retriever、generator 形式化暴露面，再把缓解与审计映射到检索、重排、生成和 traceback；这一 pipeline 视角可区分知识库泄漏、生成端暴露与只改善回答准确率的普通鲁棒性方法。 |
| 2026&#8209;01 | SoK: Privacy Risks and Mitigations in Retrieval-Augmented Generation Systems | survey、RAG privacy、attack taxonomy、mitigation maturity | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2601.03979) | 暂未公开 | 针对 RAG 将敏感知识库接入 LLM 后缺少统一隐私视图的问题，该 SoK 系统化风险、攻击、缓解与评测方法，并以 taxonomy 和 process diagram 指出现有缓解方案的成熟度缺口。 |
