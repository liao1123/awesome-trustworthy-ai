# Image Generation Safety

[返回 Generative Media Security 目录](README.md)

## 研究方向

本页研究 text-to-image（T2I）生成与 instruction-based image editing 在部署阶段的安全边界，重点覆盖 prompt filter、generator、output filter、visual instruction 和多轮 editing workflow 之间的接口错位。攻击既可能通过语言、排版或分布优化绕过单次过滤，也可能把有害目标拆进多轮编辑，或利用上游图像向下游 editor 传递隐藏 payload；防御则包括 pipeline-level moderation、inference-time alignment 和面向未授权编辑的 image immunization。本页不收录只评测普通编辑能力的 benchmark，也不以训练期 LoRA poisoning 或独立 image safety classifier 为主记录对象。

## 研究脉络

- **Pipeline guardrail 逆向：** 早期研究通过 timing side channel 与多语言测试还原黑盒 T2I pipeline，发现 prompt revision、text encoder、generator 与 output filter 的安全判断并不一致。
- **Prompt jailbreak 自动化：** 攻击从手工 negation、跨语言混写发展到 prompt distribution optimization、defense profiling 与自动 red teaming，同时优化 filter evasion、目标语义和输出多样性。
- **视觉与编辑接口扩展：** 大型 image editor 开始读取箭头、标记和 visual-text prompt 后，恶意指令可完全放进图像；多轮 editing 也允许把一次会被拒绝的目标拆成连续的 benign-looking step。
- **跨服务隐式 payload：** generate-to-edit workflow 使上游服务能够在视觉上正常的图像中埋入 hint，并由下游 editor 放大为可见内容，安全分析因而需要覆盖模型组合而非单一 API。
- **防御与当前边界：** 新方法在 denoising attention、preference alignment、introspective reasoning 和 image immunization 上介入；但闭源 pipeline 会持续更新，攻击迁移性、过度过滤和 benign utility 仍需共同评测。

## Pipeline 分析与自动化 Red Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Mind the Gap: Zero-Query Jailbreaks via Filter-Generator Discrepancy in Text-to-Image Systems | attack、filter-generator discrepancy、zero-query transfer、surrogate ensemble | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.00973) | 暂未公开 | 针对 transfer attack 在单一 surrogate 上过拟合且同时保持 filter evasion 与生成语义困难的问题，论文以 tokenization/semantic discrepancy 预筛候选并进行 surrogate-ensemble evolutionary search；在六个黑盒 pipeline 上将平均 ASR 提升到 29.2% 和 33.3%。 |
| 2026&#8209;07 | Dynamic Defense Profiling Enables Cognitive Jailbreak of Text-to-Image Models | attack、defense profiling、belief-state inference、multimodal feedback | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.17779) | 暂未公开 | 针对只把 T2I 返回视为成功或失败会浪费丰富防御信号的问题，MIND 从 textual refusal、visual blocking 与 semantic sanitization 更新防御 belief state 并用 meta-memory 指导搜索；在六类防御下达到 95.62% ASR，并迁移到商业系统。 |
| 2026&#8209;01 | PC^2: Politically Controversial Content Generation via Jailbreaking Attacks on GPT-based Text-to-Image Models | attack、jailbreak、image generation、unsafe synthesis | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2601.05150) | 暂未公开 | 针对 T2I safety filter 对政治虚假图像的防护边界，PC^2 以身份保持描述和地缘远距翻译拆散敏感关联，在含 36 名公众人物的 240 条 prompt benchmark 上对 GPT 系列模型取得最高 86% ASR。 |
| 2026 | OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing | attack、jailbreak、image generation、unsafe synthesis | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63568) | 暂未公开 | 针对模型安全策略会被越狱提示或自动化红队绕过的问题，论文提出 OrchJail 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于越狱风险测量与红队覆盖。 |
| 2026 | Exposing Implicit Vulnerabilities in Text-to-Image Models via Adversarial Agentic Probing | tool、agentic probing、implicit unsafe prompt、black-box red teaming | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/4945) | 暂未公开 | 针对表面无害提示仍可能生成危险图像而固定 prompt set 难以覆盖的问题，AdvPIE 用黑盒 adversarial agent 自动探索 prompt-output 安全落差；结果揭示 T2I safeguard 对隐式攻击仍存在系统性漏检。 |
| 2025&#8209;08 | Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL·E Text-to-Image Pipelines | analysis、timing side channel、cascaded safety filter、multilingual jailbreak | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/villa) | [Artifact](https://www.usenix.org/system/files/usenixsecurity25-appendix-villa.pdf) | 针对闭源 DALL·E pipeline 的安全组件不可见，论文以响应时间逆向级联过滤器并比较 DALL·E 2/3；结果发现 prompt revision 与 CLIP representation 的差异可被 negation 和低资源语言攻击利用。 |
| 2025&#8209;07 | DREAM: Scalable Red Teaming for Text-to-Image Generative Systems via Distribution Modeling | tool、distributional red teaming、energy-based objective、diversity sampling | IEEE S&P 2026 | [arXiv](https://arxiv.org/abs/2507.16329) | [Code](https://github.com/AntigoneRandy/DREAM) | 针对逐个优化 problematic prompt 难扩展且缺少多样性，DREAM 直接学习目标系统危险 prompt 的概率分布并以 GC-SPSA 优化；结果在多种 T2I model 与 safety filter 上同时提高成功率和提示多样性。 |
| 2024&#8209;11 | Red-Teaming Text-to-Image Models via In-Context Experience Replay and Semantic-Preserving Prompt Rewriting | attack、prompt injection、image generation、unsafe synthesis | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2411.16769) | [Project](https://zhiyichin.github.io/in-context-experience-replay/) | 针对自动 T2I red teaming 难兼顾自然语言流畅性、危害语义和跨防御迁移，ICER 将 LLM rewriter、经验回放与 bandit optimization 结合，在六类安全机制上优于七个基线，超过 30% 的 prompt 可迁移到 DALL-E 3 与 Midjourney。 |

## Text-to-Image Prompt Jailbreak

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models | attack、typography prompt、instruction-dense image、commercial T2I | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.24897) | 暂未公开 | 针对商业 image generator 会拒绝有害文本却可能把相同内容渲染为可读海报的问题，TYPO 联合优化语义改写与视觉排版策略；在四个闭源模型上较九类基线平均提高 50.2% ASR，平均查询成本为 0.04 美元。 |
| 2026&#8209;03 | JANUS: A Lightweight Framework for Jailbreaking Text-to-Image Models via Distribution Optimization | attack、prompt distribution、black-box reward、dual anchor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.21208) | [Code](https://github.com/dimshimmer/JANUS) | 针对单 prompt proxy optimization 与大型 RL generator 成本高的问题，JANUS 在 unsafe/clean semantic anchor 间学习低维混合分布并直接使用端到端黑盒 reward；在 SD3.5 Large Turbo 上把 ASR-8 从 25.30% 提升到 43.15%。 |
| 2026&#8209;01 | MacPrompt: Maraconic-Guided Jailbreak Against Text-to-Image Models | attack、macaronic prompt、cross-lingual recombination、concept erasure bypass | AAAI 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/40916) · [arXiv](https://arxiv.org/abs/2601.07141) | 暂未公开 | 针对英文同义替换难覆盖多语言 tokenizer 与 concept removal 的漏洞，MacPrompt 在字符层重组多语言有害词并保持目标语义；结果可令主要 filter 最高 100% 失效，并在性与暴力类别分别达到最高 92% 和 90% ASR。 |
| 2026 | When Memory Becomes a Vulnerability: Towards Multi-turn Jailbreak Attacks against Text-to-Image Generation Systems | attack、multi-turn T2I jailbreak、memory mechanism、recursive segmentation | USENIX Security 2026 | [USENIX](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-shiqian) | [Code](https://github.com/Shiqian-Zhao996/inception-T2I-system) | 针对 T2I system 的跨轮 memory 会累积早期恶意语义而单轮过滤器只检查当前请求，Inception 以语义保持的 segmentation 和 recursion 拆分攻击并构建 VisionFlow；结果较既有方法提高 20.0 个百分点 ASR，且可迁移到商业平台。 |

## Visual Instruction 与 Editing Workflow Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Generate "Normal", Edit Poisoned: Branding Injection via Hint Embedding in Image Editing | attack、generate-edit pipeline、hidden visual hint、branding injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.10600) | 暂未公开 | 针对跨服务 generate-to-edit workflow 会继承上游图像细节，论文在正常初图中嵌入近不可见 branding hint 并让下游 editor 重新显化；phishing 与 poisoned-model 设置平均达到 44.4% 和 32.2% 成功率，配套 mitigation 分别达到 87.4% 和 92.3%。 |
| 2026&#8209;02 | When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models | attack、visual instruction、image editing jailbreak、IESBench | ICML 2026 Oral | [Official](https://icml.cc/virtual/2026/poster/60813) · [OpenReview](https://openreview.net/forum?id=wQxRphkfxn) · [arXiv](https://arxiv.org/abs/2602.10179) | [Code](https://github.com/CSU-JPG/VJA) · [Dataset](https://huggingface.co/datasets/CSU-JPG/IESBench) · [Project](https://csu-jpg.github.io/vja.github.io/) | 针对大型 editor 把 marks、arrows 与 visual-text 当作指令而文本 filter 看不到该意图，VJA 构建纯视觉 jailbreak 与 IESBench，并提出 training-free introspective defense；商业模型 ASR 最高达 80.9%，防御可把弱对齐模型提升到接近商业系统的安全水平。 |
| 2024&#8209;10 | Chain-of-Jailbreak Attack for Image Generation Models via Step by Step Editing | attack、multi-step editing、query decomposition、CoJ-Bench | ACL 2025 Findings | [ACL Anthology](https://aclanthology.org/2025.findings-acl.571/) · [arXiv](https://arxiv.org/abs/2410.03869) | [Code](https://github.com/Jarviswang94/Chain-of-Jailbreak) | 针对一次性有害请求会被拒绝而多轮编辑缺少整链审核，CoJ 将目标拆成连续子查询并构建覆盖多类编辑操作的 CoJ-Bench；四个服务上成功率超过 60%，Think-Twice Prompting 可防住超过 95% 的攻击。 |

## Safety Alignment 与未授权编辑防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Introspective Attention Modulation for Safe Text-to-Image Generation | defense、attention modulation、inference-time alignment、benign utility | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/4953) · [arXiv](https://arxiv.org/abs/2607.14945) | [Project](https://basim-azam.github.io/iam/) | 针对 prompt filter 与 concept erasure 可被 model adaptation 绕过，IAM 在 denoising 过程中内省并调节风险相关 attention；结果在标准与 adversarial 安全评测上减少不安全生成，同时保持语义对齐与感知质量。 |
| 2026&#8209;07 | The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models | analysis、semantic collapse、alignment utility、SAGE | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/5377) · [arXiv](https://arxiv.org/abs/2607.00402) | [Project](https://adeelyousaf.github.io/SAGE_ECCV26_Project_Page/) | 针对 FID 等粗粒度指标会掩盖 T2I safety alignment 对正常语义的损伤，论文定位 text embedding semantic collapse 并提出保持空间结构的 SAGE；在维持安全性的同时较既有方法将 TIFA 提高 5.0%。 |
| 2026&#8209;06 | MIRAGE: Protecting against Malicious Image Editing via False Moderation | defense、image immunization、false moderation、commercial editor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.26199) | 暂未公开 | 针对 image-specific immunization 依赖 editor 权重和具体 prompt，MIRAGE 让保护图像在开源 embedding/moderation ensemble 中靠近违规概念，从而触发商业 editor 的预生成拒绝；跨多个闭源 API 的保护成功率超过 88%。 |
| 2026&#8209;02 | Universal Image Immunization against Diffusion-based Image Editing via Semantic Injection | defense、universal immunization、semantic injection、black-box transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.14679) | 暂未公开 | 针对逐图优化扰动难以规模化防止 deepfake 与未授权编辑，论文学习单一 universal perturbation 注入目标语义并压制原图内容；结果在 data-free 设置显著超过 universal baseline，并可跨 diffusion editor 黑盒迁移。 |
| 2025&#8209;04 | The Path to Reconciling Quality and Safety Alignment in Text-to-Image Generation | defense、preference optimization、LibraAlign-100K、quality-safety trade-off | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/5345) · [arXiv](https://arxiv.org/abs/2504.14290) | 暂未公开 | 针对安全微调压低违规生成时常损害图像质量，论文构建同时标注 safety 与 quality 的 LibraAlign-100K 并提出双奖励 T2I-SPO；结果在广泛 NSFW 概念上改善安全性并更好保持生成质量。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization | defense、image generation、unsafe synthesis、content moderation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17067) | 暂未公开 | 随着文本到图像生成模型的进步，它们引发了严重的安全问题，特别是暴力和裸体等不安全工作（NSFW）内容的生成，而红队对抗性攻击进一步加剧了这一问题；基于 LLM 提示重写的黑盒替代方案提供了更广泛的适用性，但在我们识别为 \textit{良性对抗性} 问题的关键领域失败了：提示在语言上是安全的，但由于模型学习的数据分布，仍然会触发有害的生成；我们证明，在多次红队攻击下，DiSCO 在 I2P 基准上持续增强了未防御和防御模型的安全性，分别实现了 37.7% 和 25.13% 的 ASR 降低，同时保持了语义保真度并提高了图像一致性。 |
| 2026&#8209;06 | Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks | defense、diffusion model、VLM safety、image generation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62378) · [arXiv](https://arxiv.org/abs/2606.27147) | 暂未公开 | 论文让统一多模态模型自判 unsafe generation，构造 harmful/safe pair 后迭代修正 autoregressive image codebook 中的有害映射，再在 harmless space 自适应微调恢复质量；无需外部反馈即可逐轮提升生成安全。 |
| 2026&#8209;06 | Unified Safe In-context Image Generation in Multimodal Diffusion Transformers via Restricting Unsafe Information Flows | defense、diffusion model、VLM safety、image generation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66357) · [arXiv](https://arxiv.org/abs/2606.06875) | [Code](https://github.com/deng12yx/UVR) | UVR 从 DiT multimodal attention 的信息流定位 unsafe output patch，并在共同 start-up 阶段调制注意力、限制后续有害语义传播；对图像合成和编辑分别达到 91% 与 77% erase rate，同时仅轻微影响视觉质量与忠实度。 |
| 2026 | Towards Seed-Robust Safety Alignment in Text-to-Image Models | defense、safety alignment、image generation、unsafe synthesis | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64210) | 暂未公开 | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文提出 Towards Seed-Robust Safety Alignment in 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于对齐保持与有害行为缓解。 |

> 独立 image moderation model 及其规避攻击见 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)；LoRA/plugin poisoning 见 [扩散模型后门与供应链风险](../../poisoning-and-backdoors/diffusion-model-backdoors.md)。
