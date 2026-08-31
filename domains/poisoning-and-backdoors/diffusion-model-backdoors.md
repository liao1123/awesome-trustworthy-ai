# 扩散模型后门

[返回模型投毒与后门目录](README.md)

## 研究方向

扩散模型后门研究 trigger 如何被写入 forward corruption、iterative denoising、cross-attention、text conditioning、retrieval module 或 synthetic-data chain。这里同时覆盖 image diffusion、text-to-image diffusion、masked/diffusion language model 和 multimodal diffusion language model，重点比较 target diversity、poison budget、clean-label stealth、跨模型泛化、下游传播与 purification。

## 研究脉络

- **基础攻击：** BadDiffusion、TrojDiff 和 VillanDiffusion 建立了 diffusion model 后门植入与触发的基本框架。
- **触发器与供应链扩展：** 后续工作追求低投毒率、语义或不可感知触发器，并覆盖 LoRA plugin、synthetic-data chain 和 retrieval-augmented diffusion。
- **模型与防御扩展：** 最新分支进一步覆盖 diffusion language model，同时开始形成统一 benchmark 与后门移除方法。

## Text-to-Image Diffusion 后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | TooBad: Backdoor Diffusion Models with Ultra-Low Poison Rate and Imperceptible Trigger | attack、T2I diffusion backdoor、ultra-low poison rate、imperceptible trigger | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4050) · [arXiv](https://arxiv.org/abs/2606.23362) | 暂未公开 | 针对 diffusion backdoor 在攻击力、隐蔽性和投毒成本间的权衡，论文优化 model-specific trigger；结果仅 0.5% 投毒即可获得超过 85% ASR，5% 时接近完全成功并逃过现有防御。 |
| 2026&#8209;06 | Customization under Fire: Plugin Poisoning in Text-to-Image Ecosystem | attack、LoRA supply chain、plugin poisoning、concept hijacking | ACM CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2606.09151) | [Code](https://github.com/xaddwell/PoisonLoRA) | T2I 用户依赖社区 LoRA plugin 定制模型，形成难以审计的供应链入口；PoisonLoRA 植入 concept hijacking 或 harmful task injection 并借 plugin merge 与 remix 传播；结果在 Civitai、Liblib 及多轮组合中仍达到接近 100% ASR。 |
| 2026&#8209;02 | SemBD: Semantic-Level Backdoor Attack against Text-to-Image Diffusion Models | attack、T2I diffusion backdoor、semantic region trigger、cross-attention | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/62919) · [arXiv](https://arxiv.org/abs/2602.04898) | [Code](https://github.com/DPAS-Lab/SemBD) | 针对离散关键词 trigger 易被改写和过滤，论文通过 cross-attention key/value distillation 学习连续 semantic region，并加入 semantic regularization 与 multi-entity target；结果在自然语义变体上取得接近 100% ASR。 |
| 2026&#8209;02 | When LoRA Betrays: Backdooring Text-to-Image Models by Masquerading as Benign Adapters | attack、LoRA supply chain、diffusion backdoor、benign disguise | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_When_LoRA_Betrays_Backdooring_Text-to-Image_Models_by_Masquerading_as_Benign_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2602.21977) | [Code](https://github.com/spectre-init/MasqLora) | 针对用户会从第三方下载 LoRA，作者让恶意适配器在常规检查下呈现正常功能却对隐藏触发词生成攻击目标，揭示轻量插件供应链风险。 |
| 2026 | Towards Human-Imperceptible Backdoor Attacks on Text-to-Image Diffusion Models | attack、T2I diffusion backdoor、clean-label attack、dual-modal trigger | CVPR 2026 | [CVF Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wu_Towards_Human-Imperceptible_Backdoor_Attacks_on_Text-to-Image_Diffusion_Models_CVPR_2026_paper.pdf) | 暂未公开 | 针对 dirty-label image-text mismatch 易被人工和自动清洗发现，论文联合使用近不可见 latent image perturbation 与 synonym/syntax composite trigger；结果在保持语义一致时实现约 97.2% 人评 ASR 并绕过内容过滤。 |
| 2026 | PROMPTMINER: Black-Box Prompt Stealing against Text-to-Image Generative Models via Reinforcement Learning and VLM-Guided Optimization | attack、prompt stealing、text-to-image model、black-box optimization | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_PROMPTMINER_Black-Box_Prompt_Stealing_against_Text-to-Image_Generative_Models_via_Reinforcement_CVPR_2026_paper.html) | 暂未公开 | 针对闭源文生图服务的私有 system prompt 和模板，PROMPTMINER 用强化学习与 VLM 反馈迭代查询，从输出中重建关键提示语义。 |
| 2025&#8209;08 | Practical, Generalizable and Robust Backdoor Attacks on Text-to-Image Diffusion Models | attack、T2I diffusion backdoor、few-shot poisoning、cross-model transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.01605) | 暂未公开 | 针对现有 T2I backdoor 依赖大量 poison、特定架构且易被 defense 清除，论文在共享 CLIP space 构造少量近不可见 target samples；结果十条 poison 即可获得超过 90% ASR，并跨模型和防御泛化。 |

## Diffusion Language Model 后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Backdooring Masked Diffusion Language Models | attack、diffusion LM backdoor、masked diffusion LM、corruption process | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.19262) | 暂未公开 | 针对 autoregressive 与 Gaussian diffusion 的攻击不能直接用于 discrete masked denoising，论文用 trigger-mask mixture prior 修改 forward corruption；结果 SHADOWMASK 接近 100% ASR，并在 full-model 与 parameter-efficient fine-tuning 后保持。 |
| 2026&#8209;05 | BadDLM: Backdooring Diffusion Language Models with Diverse Targets | attack、diffusion LM backdoor、diverse targets、induced masking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.09397) | 暂未公开 | 针对 diffusion LM 后门目标多局限于固定文本，论文通过 induced forward masking 植入 concept、attribute、alignment 与 code 等多种 payload；结果平均 ASR 相比直接数据投毒显著提升。 |
| 2026&#8209;03 | When One Modality Rules Them All: Backdoor Attacks against Multimodal Diffusion Language Models | attack、diffusion LM backdoor、multimodal DLM、modality dominance | ICLR 2026 Workshop | [arXiv](https://arxiv.org/abs/2603.06508) | 暂未公开 | 针对 multimodal diffusion LM 的联合 denoising 可能让单一模态支配输出，论文植入跨模态 trigger 并分析 dominance mechanism；结果图像或文本中的局部信号即可控制另一模态和最终回答。 |

## Retrieval 与 Synthetic-Data Chain

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Red-teaming Retrieval-Augmented Diffusion Models via Poisoning Knowledge Bases | attack、retrieval-augmented diffusion、knowledge-base poisoning、red teaming | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Red-teaming_Retrieval-Augmented_Diffusion_Models_via_Poisoning_Knowledge_Bases_CVPR_2026_paper.html) | 暂未公开 | 针对检索增强扩散模型信任外部知识库，作者注入恶意图文条目并测量生成偏转，证明无需修改模型权重即可植入持续风险。 |
| 2026 | Unleashing Stealthy Backdoor Pandemic by Infecting a Single Diffusion Model | attack、diffusion supply chain、backdoor propagation、model ecosystem | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Al_Nahian_Unleashing_Stealthy_Backdoor_Pandemic_by_Infecting_a_Single_Diffusion_Model_CVPR_2026_paper.html) | 暂未公开 | 针对模型生态频繁蒸馏、合并和再训练，作者只感染一个扩散模型便让后门沿派生链传播，展示单点污染可演化为供应链级风险。 |
| 2025&#8209;12 | Data-Chain Backdoor: Do You Trust Diffusion Models as Generative Data Supplier? | attack、synthetic-data pipeline、synthetic-data chain、backdoor propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.15769) | 暂未公开 | 针对下游模型越来越依赖 diffusion-generated synthetic data，论文证明 compromised generator 会记忆并复现 trigger，使后门沿数据链传播；结果还发现 trigger 在 reverse process 早期高噪阶段更明显的 ESTM 现象。 |
| 2025&#8209;01 | Retrievals Can Be Detrimental: A Contrastive Backdoor Attack Paradigm on Retrieval-Augmented Diffusion Models | attack、retrieval-augmented diffusion、contrastive attack、BadRDM | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.242/) · [arXiv](https://arxiv.org/abs/2501.13340) | 暂未公开 | 针对 retrieval-augmented diffusion 会信任外部 image database，论文向库中加入 toxicity surrogates 并后门化 retriever 的 contrastive learning；结果 text trigger 可控制被检索内容并进一步操控生成结果。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | BlackMirror: Black-Box Backdoor Detection for Text-to-Image Models via Instruction-Response Deviation | detection、diffusion backdoor、black-box audit、response deviation | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_BlackMirror_Black-Box_Backdoor_Detection_for_Text-to-Image_Models_via_Instruction-Response_Deviation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.05921) | [Code](https://github.com/Ferry-Li/BlackMirror) | 针对无法访问权重的文生图服务，BlackMirror 以成组探针测量指令与响应偏离，在未知触发器条件下识别后门模型。 |
| 2026&#8209;02 | Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models | defense、diffusion LM backdoor、self-purification、visual token masking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.22246) | 暂未公开 | 针对防御缺少可信 clean teacher，论文用 compromised model 自身对 masked salient visual tokens 重新 denoise 来构造 purified data；结果 DiSP 将超过 90% 的 ASR 通常降到 5% 以下。 |
| 2026 | AutoDebias: An Automated Framework for Detecting and Mitigating Backdoor Biases in Text-to-Image Models | defense、text-to-image backdoor、bias trigger、automated mitigation | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_AutoDebias_An_Automated_Framework_for_Detecting_and_Mitigating_Backdoor_Biases_CVPR_2026_paper.html) | 暂未公开 | 针对文生图后门可把隐蔽触发词绑定到偏置输出，AutoDebias 自动发现异常提示—图像关联并进行修复，降低触发行为而保留正常生成。 |
| 2025&#8209;08 | Sealing the Backdoor: Unlearning Adversarial Text Triggers in Diffusion Models Using Knowledge Distillation | defense、diffusion backdoor、trigger unlearning、knowledge distillation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.18235) | [Code](https://github.com/Mystic-Slice/Sealing-The-Backdoor) | 针对 T2I model 缺少选择性移除 text trigger 的方法，论文用 self-knowledge distillation 和 cross-attention guidance 擦除 poisoned association；结果对 pixel backdoor 达 100% removal、对 style attack 达 93%，且不牺牲 image fidelity。 |

## 基础攻击框架

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2023&#8209;06 | VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models | attack、diffusion backdoor、unified framework、sampler dynamics | NeurIPS 2023 | [Official](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b055b95d689b1f704d8f92191cdb788-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2306.06874) | [Code](https://github.com/IBM/VillanDiffusion) | 针对不同 sampler、scheduler 和 continuous/discrete diffusion 需要分别设计攻击，论文统一推导 backdoored diffusion process 与训练目标；结果框架可覆盖多种架构、采样器和 target behavior。 |
| 2023&#8209;03 | TrojDiff: Trojan Attacks on Diffusion Models with Diverse Targets | attack、diffusion backdoor、Trojan attack、diverse targets | CVPR 2023 | [Official](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_TrojDiff_Trojan_Attacks_on_Diffusion_Models_With_Diverse_Targets_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2303.05762) | [Code](https://github.com/chenweixin107/trojdiff) | 针对早期 diffusion backdoor 主要生成单一 target image，论文重构 noise distribution 和 reverse process 以支持 fixed image、distribution 与 attribute 等目标；结果在保持正常生成质量时实现多样 trigger behavior。 |
| 2022&#8209;12 | How to Backdoor Diffusion Models? | attack、diffusion backdoor、BadDiffusion、training-time attack | CVPR 2023 | [Official](https://openaccess.thecvf.com/content/CVPR2023/html/Chou_How_to_Backdoor_Diffusion_Models_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2212.05400) | [Code](https://github.com/IBM/BadDiffusion) | 针对 diffusion model 的 training-time security 当时缺少系统研究，论文设计 compromised forward/reverse process 并提出 BadDiffusion；结果证明从头训练或微调 clean model 都能植入高 utility、高 target specificity 的后门。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;02 | BackdoorDM: A Comprehensive Benchmark for Backdoor Learning on Diffusion Model | benchmark、diffusion backdoor、attack-defense evaluation、diffusion security | NeurIPS 2025 Datasets and Benchmarks Track | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ba9b181cd30b4f1819583be24fdfeb17-Abstract-Datasets_and_Benchmarks_Track.html) · [arXiv](https://arxiv.org/abs/2502.11798) | [Code](https://github.com/linweiii/BackdoorDM) | 针对 diffusion backdoor 的数据集、target 与指标不统一，论文建立覆盖多类攻击和 defense 的系统 benchmark；结果揭示现有方法在不同生成任务与评测口径下存在明显稳定性差异。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Semantic-level Backdoor Attack against Text-to-Image Diffusion Models | attack、backdoor attack、diffusion model、model backdoor | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62919) | [Code](https://github.com/DPAS-Lab/SemBD/) | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Semantic-level Backdoor Attack against Text-to-Image 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | Retrievals Can Be Detrimental: Unveiling the Backdoor Vulnerability of Retrieval-Augmented Diffusion Models | attack、model backdoor、cyber misuse、diffusion backdoor | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.242/) | 暂未公开 | BadRDM 通过少量有毒图像、恶意对比检索器和熵式选择，把文本 trigger 绑定到毒性代理图像，在两类 retrieval-augmented diffusion 任务上有效植入后门、保持良性效用且抵抗常见防御。 |
