# 视觉语言模型后门

[返回模型投毒与后门目录](README.md)

## 研究方向

视觉语言模型后门研究 visual trigger、text trigger、semantic concept 和 multimodal relation 如何在 VLM/MLLM 中激活恶意 caption、answer、reasoning 或 GUI action。该方向关注 clean-label poisoning、domain shift、compositional understanding、reasoning-level backdoor、input-aware trigger，以及 attention profiling、model-level repair、test-time purification 和 response bootstrap 等防御。

## 研究脉络

- **植入起点：** VLM 后门首先利用视觉 encoder、训练数据和模型供应链进行植入。
- **触发机制扩展：** 触发器随后从显式视觉 pattern 发展到语义、组合关系与 reasoning-level signal。
- **Agent 与防御扩展：** GUI 和 embodied agent 把攻击目标从回答内容推进到动作与资源消耗，检测和防御则转向 attention 与输出响应信号。

## VLM 表示、语义与推理后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning | attack、MLLM fairness backdoor、continual-learning persistence、group discrimination | 未确认（arXiv Comments：CIKM 2026） | [arXiv](https://arxiv.org/abs/2608.21577) | [Code](https://github.com/lyygua/PFBA) | PFBA 将目标群体歧视植入 MLLM 的潜在表示：锚定优势群体以保留效用，同时排斥并聚类目标群体，并针对模拟的 continual-learning 参数漂移迭代优化 trigger；实验显示公平后门可跨后续更新持续存在并规避标准后门防御。 |
| 2026&#8209;07 | Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering | attack、VLM backdoor、architectural backdoor、representation steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.25479) | 暂未公开 | 针对供应链审计常只校验 weights 而忽略 architecture definition 与 computation graph，论文植入 trigger-gated steering logic 修改中间 representation；结果无需污染训练数据或控制下游 fine-tuning 即可让后门随共享制品进入多类 VLM 服务。 |
| 2026&#8209;07 | ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision-Language Models | attack、VLM backdoor、reasoning backdoor、aha moment | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5876) · [arXiv](https://arxiv.org/abs/2607.00361) | 论文声明公开，链接待核实 | 针对只操纵最终输出的后门会被不一致 reasoning 暴露，论文通过 poisoned rationale 与 supervised-RL optimization 重定向 trigger 后的 aha moment；结果在保留自然推理表象和 clean utility 时实现稳定目标行为。 |
| 2026&#8209;05 | CBV: Clean-label Backdoor Attacks on Vision Language Models via Diffusion Models | attack、VLM backdoor、clean-label attack、diffusion synthesis | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/63753) · [arXiv](https://arxiv.org/abs/2605.02202) | 暂未公开 | 针对修改文本标签会产生明显 image-text mismatch，论文用 diffusion score matching 和 multimodal guidance 生成自然 clean-label poison，并限制修改到语义关键区域；结果在四种 VLM 上取得超过 80% ASR。 |
| 2026&#8209;04 | Phantasia: Context-Adaptive Backdoors in Vision Language Models | attack、VLM backdoor、context-adaptive trigger、stealth | CVPR 2026 Findings | [Official](https://media.eventhosts.cc/Conferences/CVPR2026/CVPR_main_conf_2026_15.pdf) · [arXiv](https://arxiv.org/abs/2604.08395) | 暂未公开 | 针对固定视觉 patch 与场景不一致、容易被察觉，论文根据图像上下文动态生成 trigger 和目标响应；结果提高跨场景隐蔽性与触发稳定性，同时维持 clean performance。 |
| 2026 | Understanding and Exploiting Phase Sensitivity for Attacking Large Vision–Language Models ↗ | attack、LVLM backdoor、phase trigger、textual switch | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/52.pdf) | 暂未公开 | 针对 LVLM 对图像相位结构的内在敏感性，BadPhase 以数据投毒植入 adversarial phase trigger，再用普通 textual trigger 共同控制开关并破坏跨模态对齐；四种 LVLM、三个数据集及商业模型迁移实验显示该隐蔽触发可稳定劫持预测。 |
| 2025&#8209;09 | TokenSwap: Backdoor Attack on the Compositional Understanding of Large Vision-Language Models | attack、VLM backdoor、compositionality、relation swap | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/60962) · [arXiv](https://arxiv.org/abs/2509.24566) | [Code](https://anonymous.4open.science/r/tokenswap-341F/) | 针对固定恶意短语容易被输出检测，论文让视觉 trigger 只交换对象间关系 token，使模型仍识别正确实体却错误理解组合关系；结果攻击更贴近语义层并绕过只查固定答案的防御。 |
| 2025&#8209;08 | IAG: Input-Aware Backdoor Attack on VLM-Based Visual Grounding | attack、VLM backdoor、visual grounding、input-aware trigger | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_IAG_Input-aware_Backdoor_Attack_on_VLM-based_Visual_Grounding_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2508.09456) | [Code](https://github.com/lijunxian111/IAG) | 针对静态 trigger 易被跨图像检测且对 grounding 场景适配不足，论文为每个输入生成内容相关的 trigger 并定向偏移定位结果；结果提高攻击隐蔽性、迁移性和视觉落点控制。 |
| 2025&#8209;06 | Backdoor Attack on Vision Language Models with Stealthy Semantic Manipulation | attack、VLM backdoor、semantic manipulation、multimodal poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.07214) | 暂未公开 | 针对 pixel patch 容易被视觉检查，论文在高层 semantic feature 中构造自然一致的污染样本；结果以不明显改变图像表面的方式触发目标语言输出。 |
| 2025&#8209;02 | Stealthy Backdoor Attack in Self-Supervised Learning Vision Encoders for Large Vision Language Models | attack、VLM backdoor、vision encoder、self-supervised learning | CVPR 2025 | [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Stealthy_Backdoor_Attack_in_Self-Supervised_Learning_Vision_Encoders_for_Large_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.18290) | 暂未公开 | 针对 LVLM 常复用第三方 self-supervised vision encoder，论文在 encoder 预训练阶段植入难察觉 trigger；结果后门可穿过后续多模态对齐并在不同下游 LVLM 中继续生效。 |
| 2024&#8209;06 | Revisiting Backdoor Attacks against Large Vision-Language Models from Domain Shift | attack、VLM backdoor、domain shift、attribution trigger | CVPR 2025 | [Official](https://doi.org/10.1109/CVPR52734.2025.00885) · [arXiv](https://arxiv.org/abs/2406.18844) | 暂未公开 | 针对静态同分布评测高估 LVLM 后门效果，论文提出 backdoor domain generalization 并用 attribution 把 domain-agnostic trigger 放入关键区域；结果在 0.2% 投毒率下显著提高跨域攻击成功率。 |

## GUI 与 Embodied Agent 后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | SlowBA: An efficiency backdoor attack towards VLM-based GUI agents | attack、GUI-agent backdoor、efficiency backdoor、popup trigger | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5078) · [arXiv](https://arxiv.org/abs/2603.08316) | [Code](https://github.com/tu-tuing/SlowBA) | 针对 GUI Agent 安全研究只关注错误动作，论文用自然 popup trigger 和两阶段 reward-level backdoor 诱导超长、循环 reasoning；结果显著增加 latency 与 energy，同时基本保持最终操作正确。 |
| 2025&#8209;12 | AdapAction: Adaptive Target Action Backdoor Attack against GUI Agents | attack、GUI-agent backdoor、adaptive action、context-aware backdoor | CVPR 2026 | [CVF Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_AdapAction_Adaptive_Target_Action_Backdoor_Attack_against_GUI_Agents_CVPR_2026_paper.pdf) | 暂未公开 | 针对固定 target action 与当前 GUI 场景不一致而易被发现，论文把 context-adaptive malicious policy 蒸馏进 Agent；结果最高达到 100% ASR、维持正常任务效用并绕过多原则 LLM 防御。 |
| 2025&#8209;07 | VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation | attack、GUI-agent backdoor、visual grounding、stealthy trigger | COLM 2025 | [Official](https://openreview.net/forum?id=7HPuAkgdVm) · [arXiv](https://arxiv.org/abs/2507.06899) | 暂未公开 | 针对 GUI Agent 会把视觉定位直接转为点击动作，论文植入低可见 trigger 来操控 grounding target 而非文本回答；结果能让 Agent 在触发界面点击攻击者指定区域并保持普通页面性能。 |
| 2025&#8209;05 | Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents | attack、GUI-agent backdoor、mobile GUI、action hijacking | Findings of EMNLP 2025 | [Official](https://aclanthology.org/2025.findings-emnlp.411/) · [arXiv](https://arxiv.org/abs/2505.14418) | 暂未公开 | 针对 MLLM mobile agent 把截图理解和高权限操作连在一起，论文评估隐藏视觉 trigger 对任务规划与点击的劫持；结果揭示细小界面元素即可持久改变下游 action sequence。 |

## 后门检测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors | detection、vision-language encoder、semantic reconstruction、attack-agnostic defense | ACM Multimedia 2026 | [Official](https://doi.org/10.1145/3767308.3835471) · [arXiv](https://arxiv.org/abs/2608.25851) | [Code](https://github.com/jsrdcht/DEFUSE) | 面向 vision-language encoder，DEFUSE 用 conditional diffusion model 重建表示语义，并在独立 reference encoder 空间识别“原语义被改写为攻击目标或无意义图像”的异常；跨多种攻击的结果表明该检测器不必预先知道 victim encoder 或具体 trigger／攻击策略。 |
| 2026&#8209;01 | TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning | detection、VLM backdoor、attention profiling、unsupervised detection | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/66774) · [arXiv](https://arxiv.org/abs/2601.21692) | 暂未公开 | 针对 FTaaS 中 trigger 形态和模态多样、监督防御难泛化，论文分析 system instruction、vision input 与 user query 三部分的 attention allocation divergence；结果无需 trigger 标签即可过滤 poisoned samples。 |

## 模型级修复与移除

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Not All Tokens Are Equal: Region-Aware Consistency Repair of Backdoors in MLLMs | defense、MLLM backdoor、region-aware consistency、model repair | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.24354) | 暂未公开 | 针对 MLLM 后门异常集中在模型实际依赖 trigger 的视觉或文本 token 区域，RACER 分区建模逐层表示不一致，并通过最坏扰动合成与对抗微调抑制后门依赖的深层方向偏移；仅用 100 个干净样本且无需 trigger、攻击目标或后门状态先验，即在 36 种设置上将平均 ASR 降至 1.1%。 |

## 推理时防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | BYORn: Bootstrap Your Own Responses to Defend Large Vision-Language Models Against Backdoor Attacks | defense、VLM backdoor、response bootstrap、self-defense | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/62182) · [arXiv](https://arxiv.org/abs/2606.02947) | 暂未公开 | 针对 VLM 后门防御依赖外部干净模型或 trigger 先验，论文利用模型自身多次响应构造 bootstrap reference 来识别异常条件行为；结果在多种攻击下削弱后门并保持正常多模态能力。 |
| 2026&#8209;03 | Test-Time Attention Purification for Backdoored Large Vision Language Models | defense、VLM backdoor、test-time defense、attention purification | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Test-Time_Attention_Purification_for_Backdoored_Large_Vision_Language_Models_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.12989) | 暂未公开 | 针对训练数据和权重不可得时难以修复 backdoored LVLM，论文在 test time 定位 trigger 引起的异常 cross-modal attention 并进行净化；结果无需重新训练即可压低多类攻击成功率。 |

## Survey 与 Dissertation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Backdoor Learning in Language Models and Vision-Language Models | survey、VLM backdoor、attack detection、multimodal security | 未确认（arXiv Comments：Ph.D. dissertation） | [arXiv](https://arxiv.org/abs/2608.18095) | [Code](https://github.com/usnistgov/trojai-round-generation/tree/round5) | 该博士论文把 VLM 与 NLP 模型中的后门攻击、检测和攻击构造并列为可信 AI 安全主线，为跨模型触发行为提供研究总览；由于摘要没有报告统一实验结果，本页只记录其 VLM 后门综合贡献，不把面向临床影像的表示效率工作混入安全结论。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Once Poisoned, Arbitrarily Controlled: A Programmable Backdoor in VLMs | attack、VLM safety、model backdoor、data poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10959) | 暂未公开 | 该攻击在一次 VLM poisoning 中学习通用 trigger-as-instruction 规则，再按推理时任意目标 caption 合成隐蔽扰动或 patch；模型可对训练时未见目标实现 any-to-any caption control，同时保持干净效用并绕过多种经典后门防御。 |
| 2026 | VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems | attack、VLM safety、data poisoning、VLM backdoor | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61520) | [Code](https://github.com/GuoweiGuan666/VenomRec) | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 VENOMREC 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | From Internal Diagnosis to External Auditing: A VLM-Driven Paradigm for Data-Free Online Backdoor Defense | detection、backdoor defense、VLM safety、model backdoor | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61974) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文构建 From Internal Diagnosis to External Auditing 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于模型供应链审计与后门防御。 |
