# 后门式水印、版权保护与所有权验证

[返回 Content Authenticity 目录](README.md) · [返回投毒与后门目录](../poison-and-backdoor/README.md)

## 研究方向

本页单独整理使用 backdoor-like conditional behavior、触发器或模型内部持久信号来进行版权保护、内容保护、授权控制、模型所有权验证和未授权数据使用验证的工作，也收录专门攻击这些保护机制的后门。它们的实现机制与恶意模型后门相似，但研究目标是证明来源、限制未授权使用或评估水印系统的攻击面。

这里的“后门式水印”是机制描述，不等同于恶意后门：只有以版权、来源、授权或所有权验证为主要问题的工作才进入本页。普通恶意投毒与后门仍归入 [模型投毒与后门](../poison-and-backdoor/README.md)；仅把水印作为恶意后门的不可见触发载体、但不攻击水印系统的工作仍留在对应模型页面。

## 研究脉络

- **保护性后门：** 将授权信号、敏感区域或概念绑定到模型内部的条件行为，在未授权编辑、个性化或调用时拒绝生成或破坏输出。
- **模型与数据归属：** 通过 trigger-response、feature-space signal 或黑盒 query 验证模型所有权、训练数据使用和下游微调后的继承关系。
- **鲁棒性与审计：** 关注 fine-tuning、模型提取、输入变换、扰动和自适应规避对验证信号的影响。
- **反制攻击：** 评估攻击者通过后门化组件、数据投毒或检测器规避破坏水印与版权保护链路的能力。

## 防御性后门、授权控制与所有权验证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | GoodDiffusion: Proactive Copyright Protection for Diffusion Generative Models via Learnable Sample-specific Signatures | defense、authorization control、sample-specific signature、diffusion bridge | ICML 2026 | [arXiv](https://arxiv.org/abs/2606.29759) | [Code](https://github.com/qsx830/GoodDiffusion) | 静态授权信号容易被反演，且难同时覆盖不同输入。 | 用样本相关的签名把合法输入与授权行为绑定。 | Learnable Signature Network 生成 sample-specific signal，并在扩散桥接过程中施加授权约束。 | 合法输入保持正常生成，未授权调用被拒绝，同时提高对签名反演的抵抗力。 |
| 2026-05 | Cert-LAS: Toward Certified Model Ownership Verification for Text-to-Image Diffusion Models via Layer-Adaptive Smoothing | defense、ownership verification、certified watermark、layer-adaptive smoothing | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.29809) | [Code](https://github.com/Leyi-Qi/Cert-LAS) | 后门式所有权信号在输入扰动后可能失效，缺少可证明的验证边界。 | 用分层平滑把后门式水印验证转化为可认证的统计检验。 | layer-adaptive smoothing、diffusion classifier 与 hypothesis testing。 | 在受扰动条件下给出所有权验证保证，并尽量保持生成效用。 |
| 2025-03 | GuardDoor: Safeguarding Against Malicious Diffusion Editing via Protective Backdoors | defense、protective backdoor、image editing、imperceptible trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2503.03944) | 暂未公开 | 普通图像保护扰动容易被压缩或加噪移除。 | 把不可见授权信号写入 image encoder，未授权编辑时触发保护行为。 | 在 encoder 中植入 region-aware protective backdoor，并区分授权与未授权编辑。 | 敏感区域被非法编辑时输出无意义结果，同时保留授权路径的可用性。 |
| 2025-02 | PersGuard: Preventing Malicious Personalization in Text-to-Image Diffusion Models via Model Backdoors | defense、personalization protection、persistent backdoor、copyright | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2502.16167) | 暂未公开 | 普通图像扰动在下游 personalization 中容易失效。 | 将保护行为写入 released model，使后续个性化仍保留版权保护约束。 | backdoor retention loss 抵抗 DreamBooth 与后续 fine-tuning 的遗忘。 | 在下游适配后继续阻止未授权个性化，并尽量维持正常生成。 |
| 2025 | SleeperMark: Towards Robust Watermark against Fine-Tuning Text-to-image Diffusion Models | defense、backdoor watermark、fine-tuning robustness、multi-bit message | CVPR 2025 | [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SleeperMark_Towards_Robust_Watermark_against_Fine-Tuning_Text-to-image_Diffusion_Models_CVPR_2025_paper.html) | 暂未公开 | 常规 diffusion watermark 会在下游微调后被遗忘。 | 把多比特消息编码为可持续激活的模型内部后门。 | 在 diffusion backbone 注入 message-embedding backdoor，并评估适配后的消息恢复。 | 所有权信号在微调后仍可提取，且正常生成质量基本保持。 |
| 2024-10 | Attack as Defense: Run-time Backdoor Implantation for Image Content Protection | defense、run-time backdoor、image protection、region trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2410.14966) | 暂未公开 | 图像所有者通常无权修改第三方编辑模型。 | 通过输入扰动在运行时诱发区域感知后门，仅在敏感内容被编辑时破坏结果。 | 不修改模型权重，在图像上施加不可见保护信号并触发 region-aware response。 | 可在黑盒编辑服务中阻止指定区域的未授权编辑。 |
| 2024-10 | Towards Reliable Verification of Unauthorized Data Usage in Personalized Text-to-Image Diffusion Models | defense、data traceability、backdoor coating、black-box verification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2410.10437) | 暂未公开 | 普通 watermark 或 trigger coating 在 personalization 中不易被模型学习。 | 学习与任务相关且感知隐蔽的 coating，使训练数据使用可被黑盒验证。 | 感知 coating、hypersphere classification 与假设检验。 | SIREN 在个性化模型上提供未授权数据使用的统计证据。 |
| 2024-05 | Lazy Layers to Make Fine-Tuned Diffusion Models More Traceable | defense、backdoor watermark、feature-space trigger、fine-tuning robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2405.00466) | 暂未公开 | trigger-response watermark 常在 fine-tuning 后衰减。 | 把水印植入微调变化较小的 lazy layers 与 feature subpaths。 | 选择低变化层，在 feature space 注入后门并测试微调后的验证率。 | 下游微调后仍保留较高的模型可追踪性。 |
| 2023-08 | Backdooring Textual Inversion for Concept Censorship | defense、concept censorship、Textual Inversion、protective backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2308.10718) | [Project](https://concept-censorship.github.io/) | 可下载的 Textual Inversion embedding 可能被用于生成敏感个体或概念。 | 把敏感词与受保护 embedding 绑定，使未授权概念调用转向安全输出。 | 在 embedding 与 trigger 共现时激活预设安全图像。 | 对下载式概念资产提供不依赖服务端模型改动的保护路径。 |
| 2023-05 | Watermarking Diffusion Model | defense、model watermark、trigger prompt、ownership verification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2305.12502) | 暂未公开 | 早期 diffusion ownership protection 缺少 model-internal verification。 | 通过固定 prompt trigger 让模型输出可验证的所有权信号。 | NAIVEWM 与固定位置 trigger 的 FIXEDWM。 | 在尽量保持生成效用的同时支持模型内部水印验证。 |
| 2026-05 | Towards Backdoor-Based Ownership Verification for Vision-Language-Action Models | tool、GuardVLA、ownership verification、backdoor watermark | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.09005) | 暂未公开 | VLA 适配后，如何在不影响动作能力的情况下验证模型归属。 | 向 embodied visual data 注入秘密消息作为无害后门水印。 | 训练后使用 trigger projector 与外部 classifier 做 swap-and-detect。 | 水印在模型适配后仍可验证，同时保持正常任务表现。 |
| 2025-04 | AGATE: Stealthy Black-box Watermarking for Multimodal Model Copyright Protection | ownership tool、backdoor watermark、black-box verification、multimodal retrieval | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.21044) | 暂未公开 | 多模态模型被盗用后，黑盒服务缺少隐蔽且可靠的归属验证。 | 生成视觉自然但语义偏移的 adversarial watermark trigger，再进行两阶段验证。 | post-transform black-box verification，并在 image-text retrieval 与分类任务中追踪模型。 | 可在黑盒条件下验证被盗多模态模型的来源。 |
| 2023-11 | Watermarking Vision-Language Pre-trained Models for Multi-modal Embedding as a Service | ownership tool、VLPMarker、backdoor watermark、embedding service | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2311.05863) | [Code](https://github.com/Pter61/vlpmarker) | embedding-as-a-service 模型提取后，所有权信号容易丢失。 | 用 OOD trigger 与正交 embedding 变换植入 benign backdoor watermark。 | embedding orthogonal transformation 与分布约束，抵抗 model extraction。 | 在多模态 embedding 服务中保留可验证的归属信号。 |

## 模型提取与后门指纹

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-01 | HoneypotNet: Backdoor Attacks Against Model Extraction | tool、backdoor fingerprint、ownership verification、capability blocking | AAAI 2025 | [Official](https://ojs.aaai.org/index.php/AAAI/article/view/32872) · [arXiv](https://arxiv.org/abs/2501.01090) | 暂未公开 | 模型被提取后，如何同时验证来源并阻断盗用模型的能力。 | 用可传播的 honeypot backdoor 把归属信号与能力阻断绑定到替代模型。 | 双层优化训练 honeypot 分类层，并让替代模型在蒸馏后继承后门。 | 能以较高成功率完成确权，同时破坏提取模型的目标功能。 |
| 2026 | Inhibitory Attacks on Backdoor-based Fingerprinting for Large Language Models | attack、LLM backdoor、model fingerprint、model copyright | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1207/) | 暂未公开 | backdoor fingerprint 在 LLM ensemble 中的抗规避能力缺少系统检验。 | 通过逐 token 抑制和候选投票筛掉指纹触发响应。 | TFA 逐 token 过滤，SVA 结合困惑度与投票执行 fingerprint inhibition。 | 在维持集成性能的同时有效抑制现有后门指纹检测。 |

## 版权目标的投毒与后门攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-06 | ME: Trigger Element Combination Backdoor Attack on Copyright Infringement | attack、copyright infringement、multi-element trigger、DCT stealth | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.10776) | 暂未公开 | 极少 poisoning samples 下，版权复现后门的攻击稳定性不足。 | 在单个样本中组合多个图文毒性元素，提升低预算攻击的可触发性。 | multi-element trigger 与 DCT 隐写降低毒样本可见性。 | 在低数据预算下提高 copyright reproduction 的攻击成功率。 |
| 2024-01 | The Stronger the Diffusion Model, the Easier the Backdoor: Data Poisoning to Induce Copyright Breaches Without Adjusting Finetuning Pipeline | attack、SilentBadDiffusion、copyright breach、clean pipeline | ICML 2024 | [arXiv](https://arxiv.org/abs/2401.04136) | 暂未公开 | 攻击者通常无法控制受害者的 fine-tuning pipeline。 | 只构造 poison data，利用强模型记忆在特定 caption 下复现受保护内容。 | clean-pipeline-compatible data poisoning，最低约 0.2% 投毒比例。 | 证明不修改微调流程也能诱发版权内容复现。 |
| 2024-12 | CopyrightShield: Enhancing Diffusion Model Security Against Copyright Infringement Attacks | defense、copyright backdoor、poison detection、adaptive training | ICCV 2025 | [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_CopyrightShield_Enhancing_Diffusion_Model_Security_Against_Copyright_Infringement_Attacks_ICCV2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.01528) | 暂未公开 | SilentBadDiffusion 利用位置与 caption memorization，传统清洗难定位毒样本。 | 结合空间掩码与数据归因定位版权毒样本，再抑制相关记忆。 | spatial masking、data attribution 与动态 penalty。 | 降低侵权特征记忆及相应后门复现风险。 |

## 针对水印系统的后门攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Robust Watermarks Meet Backdoored Models: Evading Diffusion Semantic Watermarks via Stealthy Backdoor | attack、semantic watermark、VAE backdoor、detector evasion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.00543) | 暂未公开 | semantic watermark pipeline 依赖的 VAE encoder 本身可能被污染。 | 在 VAE encoder 植入隐蔽后门，使带触发器的输入绕过水印检测。 | 频谱正则 universal trigger 与 parameter-aligned training。 | 在保持正常检测率的同时，报告平均 94.6% 的水印逃逸 ASR。 |

## 分类说明

- 本页的保护性后门、水印和 ownership verification 不计入 [模型投毒与后门](../poison-and-backdoor/README.md) 各模型页面的恶意攻击数量。
- `GhostVAE` 等工作虽然使用恶意后门，但其主要目标是破坏水印检测链，因此放在本页；普通后门论文若水印只充当触发器，则仍按受影响模型归类。
- 以后门检测/清除为主、将水印保留作为 utility 约束的工作（例如 BackFlush）仍按恶意后门归入对应模型页面。
- 模型指纹、API 审计和非后门式版权保护仍可在 [模型版权保护](../misc/model-copyright-protection.md) 与本目录的常规水印页面中查阅。
