# 生成模型概念擦除与 Unlearning

[返回上级目录](README.md)

## 研究方向

研究从 diffusion、flow 和多模态生成模型中移除敏感、受版权保护或危险概念，同时测量 residual generation、relearning、prompt circumvention 和无关内容质量。

## 研究脉络

- **参数与表示擦除：** 早期方法编辑 cross-attention、权重或 latent direction 以压制指定概念。
- **多概念与持续遗忘：** 研究扩展到多概念、动态 LoRA、token-level 和 inference-time removal。
- **反测试：** Adversarial prompt、relearning 和 hidden leakage 用于检验表面不可生成是否等于真实删除。
- **当前边界：** 精确概念边界、组合语义和跨语言恢复仍使 deletion guarantee 难以成立。

## Training-Time Concept Erasure 与 Utility Retention

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TINA+: Probing Residual Visual Knowledge in Unlearned Diffusion Models via Diffusion-Consistent Text-Free Inversion | defense、concept erasure、diffusion unlearning、generation fidelity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17747) | 暂未公开 | 尽管文本到图像扩散模型展现出强大的生成能力，为防止有害内容，概念擦除技术仍不可或缺；为从视觉角度研究这一问题，我们利用扩散反演来探测生成轨迹能否重建已擦除概念的视觉实例；这些结果提供了更有力的证据：当前方法往往只是切断文本—图像联系来遮蔽概念，而没有消除底层视觉知识。 |
| 2026&#8209;08 | TEA: Text Encoder Alignment for Robust Concept Erasure in Text-to-Image Models | analysis、concept erasure、diffusion unlearning、generation fidelity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15341) | [Code](https://github.com/alirezafarashah/TEA.git) | 文本到图像的扩散模型可能被滥用，通过绕过内置安全机制的对抗性或释义提示来生成有害内容；现有的概念擦除方法通常面临对抗性提示的鲁棒性有限、良性生成质量下降或依赖于引入持续计算开销的推理时间干预。 |
| 2026&#8209;07 | To Erase, or Not to Erase: Robust Training-Free Concept Erasure with Preservation aware Adaptive Ranked Subspace Expansion | defense、concept erasure、diffusion unlearning、generation fidelity | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5971) · [arXiv](https://arxiv.org/abs/2607.23492) | 暂未公开 | 针对静态概念库既漏掉恢复触发器又误伤相邻正常语义的问题，PARSE 动态发现擦除/保留概念并按需扩展投影子空间，在无需训练下提高多类目标的抗攻击擦除与效用平衡。 |
| 2026&#8209;03 | OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure | defense、concept erasure、diffusion unlearning、generation fidelity | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3150) · [arXiv](https://arxiv.org/abs/2603.11493) | 暂未公开 | 针对敏感与正常语义共享神经元导致擦除误伤的问题，OrthoEraser 用稀疏自编码器解耦特征并将擦除方向正交投影到正常子空间零空间，更精确删除有害内容且保持生成流形。 |
| 2026 | Z-Erase: Enabling Concept Erasure in Single Stream Diffusion Transformers | defense、concept erasure、diffusion model、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62596) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Z-Erase 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Where Concept Erasure Should Occur: Concept–Layer Alignment in Text-to-Video Diffusion Models | defense、concept erasure、diffusion model、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65598) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Where Concept Erasure Should Occur 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Unlearning in Diffusion Models: A Unified Framework with KL Divergence and Likelihood Constraints | defense、diffusion model、machine unlearning、concept erasure | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65884) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Unlearning in Diffusion Models 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance | detection、generative model safety、machine unlearning、concept erasure | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66060) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Temper-Then-Tilt 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | SAEmnesia: Erasing Concepts in Diffusion Models with Supervised Sparse Autoencoders | defense、sparse autoencoder、concept erasure、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64245) | [Code](https://github.com/EIDOSLAB/SAEmnesia) | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 SAEmnesia 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险概念治理与生成安全。 |
| 2026 | Preference-Calibrated Optimization with Score-Level Distribution Alignment for Text-to-Image Diffusion Model Unlearning | defense、diffusion model、machine unlearning、concept erasure | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66454) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Preference-Calibrated Optimization with Score-Level Distribution 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Orthogonal Concept Erasure for Diffusion Models | defense、concept erasure、diffusion model、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63634) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Orthogonal Concept Erasure for Diffusion 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | GEM: Geometric Erasure by Contrastive Velocity Matching in Rectified Flows | defense、concept erasure、diffusion unlearning、generation fidelity | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64476) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 GEM 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | ForceForget: Reinforcement Concept Removal for Enhancing Safety in Text-to-Image Models | defense、concept erasure、diffusion unlearning、generation fidelity | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66798) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 ForceForget 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Concept Removal for Frontier Image Generative Models | defense、generative model safety、concept erasure、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61255) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Concept Removal for Frontier Image 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | A Unified Framework for Diffusion Model Unlearning with f-Divergence | defense、diffusion model、machine unlearning、concept erasure | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66124) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Unified Framework for Diffusion Model 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Adversarial Reinforcement Learning for Robust Diffusion Large Language Model Unlearning | defense、diffusion model、machine unlearning、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65904) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Adversarial Reinforcement Learning for Robust 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | Achieving Subcategorical Erasure in Text-to-Image Models | defense、concept erasure、diffusion unlearning、generation fidelity | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4524) | 暂未公开 | 针对现有方法难以一次删除完整有害或版权子类别的问题，SURE 结合概念空间发现与 Lipschitz 正则化，在更完整擦除目标类别的同时保持无关概念的生成能力。 |
| 2025&#8209;11 | CGCE: Classifier-Guided Concept Erasure in Generative Models | detection、concept erasure、diffusion unlearning、generation fidelity | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4668) · [arXiv](https://arxiv.org/abs/2511.05865) | 暂未公开 | 针对概念擦除易被对抗提示恢复且损害正常生成的问题，CGCE 用轻量分类器仅在推理时识别并修正不安全文本嵌入，对多类红队攻击保持强鲁棒性和较高生成质量。 |
| 2025&#8209;10 | Rethinking Robust Adversarial Concept Erasure in Diffusion Models | defense、concept erasure、adversarial robustness、diffusion unlearning | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5067) · [arXiv](https://arxiv.org/abs/2510.27285) | [Code](https://github.com/Qhong-522/S-GRACE) | 针对随机采样式对抗擦除计算昂贵且覆盖目标语义不足的问题，S-GRACE 用单样本语义引导优化与代理概念映射，在 NSFW、风格和对象擦除上兼得更强抗恢复性、生成效用和更低成本。 |

## Circumvention、Relearning 与恢复攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Erased but Not Forgotten: How Backdoors Compromise Concept Erasure | attack、model backdoor、concept erasure、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64315) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Erased but Not Forgotten 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于投毒与后门威胁评估。 |

## Inference-Time 与 Representation-Level Erasure

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation | defense、concept erasure、inference-time intervention、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60671) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 ScaleErasure 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
| 2026 | MidSteer: Optimal Affine Framework for Steering Generative Models | tool、generative model safety、concept erasure、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64719) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 MidSteer 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险概念治理与生成安全。 |
| 2026 | Inference Time Concept Removal Guidance for Text-to-Image Diffusion Models | defense、diffusion model、concept erasure、diffusion unlearning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65659) | 暂未公开 | 针对生成模型中的危险、侵权或敏感概念需要被精确移除且避免误伤正常能力的问题，论文提出 Inference Time Concept Removal Guidance 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于危险概念治理与生成安全。 |
