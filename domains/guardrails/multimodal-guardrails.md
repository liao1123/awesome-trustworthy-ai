# 多模态 Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究对图像、文本-图像组合、视频、音频及 omni-modal 输入输出执行独立安全审核。与纯文本分类相比，多模态 guardrail 需要处理单一模态看似安全但组合后产生的隐式风险、视觉证据与文字指令冲突、跨帧语境、动态 policy、reasoning trace 本身的安全，以及 harmful input 仍可能得到 safe response 时的过度拒绝问题。

## 研究脉络

- **图像分类与 benchmark：** UnsafeBench、VLSBench 等工作先建立真实/生成图像分类与 visual leakage 评测，暴露通用 VLM 的输入安全盲区。
- **Policy-following guard：** SafeWatch、GuardReasoner-VL 和 SafeGuard-VL 从固定二分类转向读取 policy、定位视觉证据并生成可检查的 reasoning 或 explanation。
- **Classifier-side red teaming：** 研究开始用 context shift、T2I generation 与 agentic photo editing 主动搜索 image safety classifier 的 false negative，而不只测试固定违规图片。
- **组合与上下文风险：** CrossGuard、MiShield、LLaVAShield 和 EchoSafe 分别覆盖图文隐式意图、多图组合、多轮对话及 inference-time memory，判断对象从单张图扩展到完整上下文。
- **Omni-modal 与视频：** OmniGuard、GuardReasoner-Omni、SafeLens 和 UNIVID 将统一审核扩展到视频、音频与工业工作流，并用 token pruning、fast-and-slow routing 或 policy-aware caption 控制成本。
- **新攻击面与效用：** Unsafe Induction Attack 研究让安全图像被误判为有害的 availability attack，output-aware guardrail 则利用待生成响应的内部状态减少 over-refusal。

## Policy-Adaptive、Reasoning 与响应审核

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails | defense、policy-adaptive image guard、boundary pair、policy shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.05910) | [Project](https://policyshiftguard.github.io/) | 针对 image guard 把安全性误当作图像固有属性、无法随产品规则变化，论文构建 PolicyShiftBench 并用 matched pass/block boundary pair 训练 PolicyShiftGuard；7B 模型在未见 policy 上显著改善 policy-sensitive 判断。 |
| 2026&#8209;06 | Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs | defense、output-aware guard、hidden-state prediction、over-refusal | ECCV 2026 | [arXiv](https://arxiv.org/abs/2607.09697) | [Code](https://github.com/kunzhan/OutGuard) | 针对 input-only guard 会拦截本可由 MLLM 安全拒答或规劝的请求，论文从生成前 hidden state 预测实际 output 是否有害；结果保持安全性能的同时显著减少 over-refusal。 |
| 2026&#8209;05 | RuleSafe-VL: Evaluating Rule-Conditioned Decision Reasoning in Vision-Language Content Moderation | benchmark、rule-conditioned moderation、decision reasoning、policy compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.07760) | [Code](https://anonymous.4open.science/r/RuleRuleSafe-VL-2527/README.md) | 针对 VLM 能识别敏感视觉内容但未必能按平台规则作出可验证决定，论文构建 rule-conditioned benchmark 并训练对应 guard；结果把评测重点从视觉识别推进到 evidence、rule 与 verdict 的一致性。 |
| 2026&#8209;03 | Towards Policy-Adaptive Image Guardrail: Benchmark and Method | defense、SafeGuard-VL、cross-policy generalization、RLVR | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.01228) | [Code](https://github.com/adorableChowhound/SafeGuard-VL) | 针对固定 policy 微调的 image guard 遇到新规则会失效甚至损伤通用能力，论文用安全图像编辑构建 SafeEditBench，并以 policy-grounded RLVR 训练 SafeGuard-VL；结果提高跨 policy 泛化。 |
| 2026&#8209;02 | Pragma-VL: Towards a Pragmatic Arbitration of Safety and Helpfulness in MLLMs | defense、safety-helpfulness trade-off、visual risk perception、reward modeling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.13292) | 暂未公开 | 针对 MLLM 在漏放风险与过度拒绝之间摇摆，论文先增强 visual risk perception，再以 query-dependent reward model 学习情境化权衡；结果在多项安全 benchmark 提升 5% 至 20% 并维持通用能力。 |
| 2025&#8209;12 | ProGuard: Towards Proactive Multimodal Safeguard | defense、OOD risk、proactive moderation、RL training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.23573) | [Code](https://github.com/yushaohan/ProGuard) | 针对 reactive guard 只能识别训练 taxonomy 中的已知风险，论文用 modality-balanced 数据与 RL 训练 ProGuard 描述未见 unsafe category；结果提高 OOD risk detection 与 description 能力。 |
| 2025&#8209;11 | GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision | detection、unsafe reasoning trace、QTA pipeline、iterative supervision | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.20994) | [Code](https://github.com/xiangyx2020/GuardTrace-VL) | 针对最终 answer 安全但中间 multimodal reasoning 泄露偏见或违规内容，论文联合图像与文本审核 Question-Thinking-Answer 全流程并渐进训练；结果在 unsafe reasoning detection 上达到 93.1% F1。 |
| 2025&#8209;10 | Multimodal Policy Internalization for Conversational Agents | defense、policy internalization、TriMPI、tool-use policy | 未注明（arXiv） | [OpenReview](https://openreview.net/forum?id=fSE0rUngCX) · [arXiv](https://arxiv.org/abs/2510.09474) | [Code](https://github.com/MikeWangWZHL/TriMPI) | 针对多模态 Agent 每次携带长 policy 成本高且遵循不稳，论文以 continual pretraining、SFT 和 PolicyRollout 把视觉与工具规则内化到参数；结果减少 prompt 长度并改善 policy generalization。 |
| 2025&#8209;10 | SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability | defense、image guard、policy adherence、explainability | ICLR 2026 Reject | [OpenReview](https://openreview.net/forum?id=bPVLklCEcO) · [arXiv](https://arxiv.org/abs/2510.23960) | [Code](https://github.com/xupy2003/SafeVision) | 针对 image guard 在复杂 policy 下缺少稳定依据且部署成本高，论文联合安全分类、规则遵循和解释训练紧凑模型；结果在保持效率的同时增强对 policy 的可追溯判断。 |
| 2025&#8209;09 | LLaVAShield: Safeguarding Multimodal Multi-Turn Dialogues in Vision-Language Models | defense、multi-turn dialogue、contextual risk、VLM guard | CVPR 2026 | [arXiv](https://arxiv.org/abs/2509.25896) | [Code](https://github.com/leost123456/LLaVAShield) | 针对单轮 image-text 审核忽略风险在多轮对话中的累积与指代，论文构建多轮安全数据并训练独立 VLM guard；结果提升对跨轮次视觉语境和渐进式攻击的检测。 |
| 2025&#8209;05 | GuardReasoner-VL: Safeguarding VLMs via Reinforced Reasoning | defense、reinforced reasoning、multimodal guard、length-aware reward | NeurIPS 2025 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2a02b560822d564119fe3ac3be024ac6-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.11049) | [Code](https://github.com/yueliu1999/GuardReasoner-VL) | 针对 VLM guard 缺少对图像与文本联合风险的 deliberation，论文用 123K 样本先 SFT 冷启动再以 online RL 和 length-aware reward 训练；结果建立可输出推理的 3B/7B 多模态 guard 基线。 |

## 跨模态组合风险、攻击与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | The Boy Who Cried Wolf: Adversarial Misclassification of Safe Inputs as Unsafe in Multimodal Guardrails | attack、unsafe induction、false positive、availability | KDD 2026 | [arXiv](https://arxiv.org/abs/2608.01373) | 暂未公开 | 针对 guardrail 攻击研究主要追求 false negative、忽略恶意误拒，论文以 Unsafe Semantic Distillation 为安全图像加入不可感知扰动；结果在四个 guard model 上达到 84% ASR，揭示内容审核的 availability 风险。 |
| 2026&#8209;07 | Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign Images Combine | defense、multi-image toxicity、compositional semantics、reasoning distillation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.00576) | 暂未公开 | 针对每张图单独无害、组合后才表达有害语义的 MIIT，论文构建多图数据并用渐进 reasoning distillation 训练 MiShield；结果要求 guard 显式关联跨图实体后再作安全判断。 |
| 2025&#8209;10 | CrossGuard: Safeguarding MLLMs against Joint-Modal Implicit Malicious Attacks | defense、joint-modal attack、implicit intent、adversarial data generation | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1178/) · [arXiv](https://arxiv.org/abs/2510.17687) | [Code](https://github.com/ZhangXu0963/CrossGuard) | 针对文字和图像各自 benign、联合后才显露恶意意图，论文用 RL red-teaming pipeline ImpForge 生成隐式样本并训练 intent-aware CrossGuard；结果同时增强 explicit 与 implicit threat 防御并维持 benign utility。 |

## Image Classifier Red Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Red-Teaming NSFW Image Classifiers as Text-to-Image Safeguards | attack、NSFW classifier、context shift、T2I safeguard | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.506/) | 暂未公开 | NSFW classifier 对主体不变但背景和共现对象改变的 context shift 缺少系统压力测试；论文先合成 36K 图像探索 failure，再训练 LLM 重写 prompt 进行 exploitation；结果规避概率最高提升六倍，且漏洞迁移到实际 T2I 与 T2V system。 |
| 2026&#8209;06 | RedEdit: Agentic Red-Teaming of Image Safety Classifiers via MCTS-Guided Photo-Editing | attack、image safety classifier、MCTS editing、evasion robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.06140) | 暂未公开 | Image safety classifier 对用户常见 photo editing 的稳健性缺少系统评估；RedEdit 用 VLM proposer 与 MCTS 搜索保持有害语义的编辑序列；结果平均少于两步即可使 76.2% unsafe image 逃逸，同时保留 93.0% malicious semantics。 |

## 视频、音频与 Omni-Modal Guardrail

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | UNIVID: Unified Vision-Language Model for Video Moderation | tool、video moderation、policy-aware caption、industrial deployment | ACL 2026 Industry Track | [ACL Anthology](https://aclanthology.org/2026.acl-industry.32/) · [arXiv](https://arxiv.org/abs/2606.05748) | 暂未公开 | 针对大规模视频审核依赖大量黑盒 policy classifier 且难解释，论文用单一 VLM 生成 policy-aware caption 作为可核查中间表示；工业系统相对减少 42.7% violation leakage 与 37.0% overkill。 |
| 2026&#8209;05 | SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening | defense、video guard、fast-slow routing、test-time reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.17610) | 暂未公开 | 针对所有视频统一调用大型 reasoning guard 浪费计算，论文用 fast path 处理多数样本、slow path 深入分析时序和复杂 policy，并以 influence filtering 精简训练数据；结果在降低成本时提升视频审核表现。 |
| 2026&#8209;04 | AudioGuard: Toward Comprehensive Audio Safety Protection Across Diverse Threat Models | defense、audio guardrail、audio-native risk、policy grounding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.08867) | 暂未公开 | 音频风险不只是不安全文本的语音化，还涉及 harmful sound、speaker attribute、impersonation 与 voice-content composition；AudioGuard 组合 waveform-level SoundGuard 和 policy-grounded ContentGuard；结果在 AudioSafetyBench 等多项 benchmark 上以更低 latency 超过 audio-LLM guard baseline。 |
| 2026&#8209;03 | Evolving Contextual Safety in Multi-Modal Large Language Models via Inference-Time Self-Reflective Memory | defense、contextual safety、self-reflective memory、training-free adaptation | CVPR 2026 | [arXiv](https://arxiv.org/abs/2603.15800) | [Project](https://echosafe-mllm.github.io/) | 针对视觉场景仅有细微语境差异却需要相反安全决策，论文构建 MM-SafetyBench++ 并让 EchoSafe 在推理时积累和检索 self-reflective memory；结果无需训练即可随交互改进 context-aware 判断。 |
| 2026&#8209;02 | BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards | defense、ad moderation、cross-modal mismatch、policy reward | AAAI 2026 | [arXiv](https://arxiv.org/abs/2602.18193) | 暂未公开 | 针对短视频广告同时存在夸大画面、语音和字幕不一致等专业违规，论文用 rule-driven ICoT 数据和 critic-guided policy reward 训练多任务 guard；结果提升真实广告审核的准确性、一致性与泛化。 |
| 2026&#8209;02 | GuardReasoner-Omni: A Reasoning-based Multi-modal Guardrail for Text, Image, Video, and Audio | defense、omni-modal guard、SFT-RL training、concise reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.03328) | [Code](https://github.com/zzh-thu-22/GuardReasoner-Omni) | 针对不同模态分别部署 guard 造成 policy 与接口割裂，论文在 181K 四模态样本上先 SFT 冷启动 reasoning、再用简洁 correctness reward 做 RL；结果发布统一的 3B/7B guard model。 |
| 2026&#8209;01 | From Sparse Decisions to Dense Reasoning: A Multi-attribute Trajectory Paradigm for Multimodal Moderation | defense、UniMod、multi-attribute trajectory、dense supervision | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.02536) | [Code](https://github.com/Carol-gutianle/UniMod) | 针对 binary label 使 multimodal guard 学到表面 shortcut，论文把 evidence grounding、modality assessment、risk mapping、policy decision 和 response 串成稠密 trajectory，并以 UniRM 分属性打分；结果用较少数据获得更清晰的决策边界。 |
| 2025&#8209;12 | OmniGuard: Unified Omni-Modal Guardrails with Deliberate Reasoning | defense、omni-modal moderation、policy critique、cross-modal data | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.02306) | [Project](https://luka-group.github.io/OmniGuard_webpage/) | 针对 binary unimodal guard 难覆盖文本、图像、视频与音频的组合输入，论文整理 210K 结构化 label 与 critique 数据训练 deliberate guard；结果以统一模型在多模态和跨模态场景执行 policy。 |
| 2024&#8209;12 | SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations | defense、video guard、parallel policy encoding、visual token pruning | ICLR 2025 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/hash/beac6bfb7eac3d651307c16ac747df01-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2412.06878) | [Code](https://github.com/BillChan226/SafeWatch) | 针对视频审核用长 prompt 串行编码规则成本高且存在 position bias，论文并行编码 policy chunk 并按规则裁剪视觉 token；结果配套 SafeWatch-Bench 提供可解释、多标签、可自定义 policy 的视频 guard。 |

## Benchmark 与诊断数据

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;11 | OutSafe-Bench: A Benchmark for Multimodal Offensive Content Detection in Large Language Models | benchmark、offensive content、bilingual evaluation、multi-judge voting | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.10287) | 暂未公开 | 针对多模态 offensive output 缺少统一中英评测，论文覆盖文本、图像、音频和视频及多类风险，并以多模型加权裁判降低单一 judge 偏差；结果用于比较 MLLM 输出安全而非只测输入分类。 |
| 2025&#8209;10 | SafetyPairs: Isolating Safety Critical Image Features with Counterfactual Image Generation | benchmark、counterfactual image、safety feature、causal diagnosis | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.21120) | 暂未公开 | 针对安全 benchmark 中语义与风险因素纠缠、难判断模型依赖什么视觉 cue，论文生成只改变 safety-critical feature 的 counterfactual pairs；结果可更直接诊断 image guard 的因果敏感性和 shortcut。 |
| 2025&#8209;10 | VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety | analysis、joint understanding、modality interaction、safety boundary | Under review | [OpenReview](https://openreview.net/forum?id=OzPAI04hi5) · [arXiv](https://arxiv.org/abs/2510.18214) | 暂未公开 | 针对单模态分数无法反映图文联合理解的安全边界，论文系统控制不同模态中的风险信号并比较联合判断；结果刻画 MLLM 与 guardrail 在 compositional safety 上的能力缺口。 |
| 2025&#8209;06 | HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model | benchmark、image-text combinations、visual guard module、holistic safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.04704) | [Code](https://github.com/youngwanLEE/holisafe) | 针对既有数据只覆盖部分 image safety 与 text safety 组合，论文构建五类组合的 HoliSafe-Bench 并提出可插拔 Visual Guard Module；结果同时评测安全回复生成与图像风险判断。 |
| 2024&#8209;11 | VLSBench: Unveiling Visual Leakage in Multimodal Safety | benchmark、visual leakage、benign text、unsafe image | ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.acl-long.405/) · [arXiv](https://arxiv.org/abs/2411.19939) | 暂未公开 | 针对 MLLM 的文本安全对齐可能掩盖视觉通道风险，论文以 benign textual query 搭配 unsafe image 测试 visual leakage；结果表明模型在只由图像承载恶意意图时更容易绕过安全行为。 |
| 2024&#8209;05 | UnsafeBench: Benchmarking Image Safety Classifiers on Real-World and AI-Generated Images | benchmark、image safety classifier、real-world image、AI-generated image | CCS 2025 | [arXiv](https://arxiv.org/abs/2405.03486) | 暂未公开 | 针对 image safety classifier 缺少同时覆盖真实与生成图像的可比评测，论文统一风险类别和测试集比较多类审核器；结果揭示数据来源与类别变化会显著影响实际检测表现。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | NVIDIA Nemotron 3.5 Content Safety: Open Models and Data for Multimodal Moderation | NVIDIA | multimodal moderation、open safety model、deployment | [Hugging Face](https://huggingface.co/blog/nvidia/nemotron-3-5-content-safety) | 从模型发布与部署角度介绍 Nemotron 3.5 Content Safety 的多模态输入、policy 分类与开放资源，并补充如何把独立 safety model 接入生成服务；该条记录模型生态，不替代经过 proceedings 核实的论文条目。 |
