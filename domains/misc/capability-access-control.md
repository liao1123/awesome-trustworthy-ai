# 模型能力访问控制

[返回其他研究领域目录](README.md)

## 研究方向

模型能力访问控制研究如何让同一模型面向不同授权主体暴露不同的 parametric knowledge 与 capability，而不是只在输出层执行统一拒答。该方向覆盖训练期 capability localization 与 modularization、credential-conditioned inference、adapter 或 expert 级访问控制、能力移除与耐篡改防御，以及开放权重发布后的 durability evaluation。需要区分三种不同保证：禁止未授权计算路径、让公开模型缺失目标能力、以及仅让模型在行为上拒绝请求；其中任何一种都不自动推出另外两种。

## 研究脉络

- **访问控制起点：** Parametric information-flow control 与动态 adapter 用模块化架构限制受保护数据对推理结果的影响。
- **能力级授权：** Authorization alignment、Gradient Routing、GRAM、private experts 与 keyed computation 将控制对象从数据来源扩展到知识、能力和实际计算路径。
- **能力移除与保护：** 另一条路线用 capability localization、低秩编辑、skill unlearning、pretraining filtering、distillation 和抗恶意微调机制移除或保护能力。
- **当前评测重点：** 随着开放权重 threat model 增强，研究从一次性行为抑制转向检验能力能否被 elicitation 或 relearning 恢复，并检查 dual-use concept 的有害用法能否被移除而良性用法得到保留。

## 授权推理与能力锁定

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models | tool、capability access control、private experts、route masking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06690) | 暂未公开 | 针对行为层 gate 无法证明未授权请求没有调用私有能力，论文冻结 sparse MoE 并训练独立 private-expert branch，在 top-k routing 前按策略选择 public 或 private pool；结果在声明的 TCB 下所有 deny 场景均为零私有执行且 allow-deny-allow 可精确恢复，但不声称公开模型缺失相同语义能力。 |
| 2026&#8209;06 | Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs | tool、capability access control、keyed computation、public-private separation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.21638) | [Code](https://github.com/McGill-NLP/tiered-language-models) | 针对开放权重模型无法依赖 API gate 区分用户，论文让 compact secret key 置换少量参数并联合训练 public 与 keyed 两种计算图；结果同一组权重可提供分层能力，且公开模式保持原有行为并抵抗部分密钥泄露与微调提取。 |
| 2025&#8209;10 | Locket: Robust Feature-Locking Technique for Language Models | tool、feature access control、locking adapters、credential robustness | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.626/) | [Code](https://github.com/ssg-research/locket) | 针对 password-locked model 难兼顾拒绝效果、效用和多用户扩展，论文对 feature-locking adapter 进行对抗训练与合并；结果实现 100% locked-feature 拒绝率、至多 7% 效用下降和至多 5% 攻击成功率。 |
| 2024&#8209;10 | SudoLM: Learning Access Control of Parametric Knowledge with Authorization Alignment | tool、parametric knowledge、authorization alignment、SUDO key | ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.acl-long.1318/) | 暂未公开 | 针对统一 preference alignment 会同时屏蔽合格用户所需的敏感知识，论文用 authorization alignment 训练由 SUDO key 解锁的权限条件行为；结果在两个应用场景中阻止未授权访问，同时让授权用户使用完整 parametric knowledge 并保持通用效用。 |
| 2024&#8209;04 | AdapterSwap: Continuous Training of LLMs with Data Removal and Access-Control Guarantees | tool、data access control、adapter composition、data removal | CAMLIS 2024 | [arXiv](https://arxiv.org/abs/2404.08417) | 暂未公开 | 针对持续新增数据、按用户授权和删除文档难以同时满足，论文把不同数据集合编码为可在推理时动态组合的 low-rank adapters；结果支持持续学习与细粒度数据访问和删除，并减少新数据引入造成的遗忘。 |
| 2023&#8209;06 | Information Flow Control in Machine Learning through Modular Model Architecture | tool、parametric IFC、security-domain experts、non-interference | USENIX Security 2024 | [USENIX](https://www.usenix.org/conference/usenixsecurity24/presentation/tiwari) | 暂未公开 | 针对传统模型中任意训练数据都可能影响任意输出而访问策略无法约束参数化信息流，论文将每个 security domain 的影响限制到独立 expert 并只激活用户可访问的模块；结果满足所定义的 non-interference，性能开销为 1.9%，且因可使用受控数据而提高文本和代码任务准确率。 |

## 训练期能力定位与模块化

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Modular Pretraining Enables Access Control | tool、capability modularization、gradient routing、module ablation | ICML 2026 Spotlight | [Official](https://icml.cc/virtual/2026/poster/60631) · [arXiv](https://arxiv.org/abs/2607.08077) · [OpenReview](https://openreview.net/forum?id=yIubI9l3IT) | [Code](https://github.com/agencyenterprise/modular-pretraining) | 针对为每种授权组合分别训练 data-filtered model 成本过高，论文用 GRAM 将不同 dual-use domain 的梯度路由到可拆卸辅助模块；结果关闭模块可近似从未见过该领域数据的模型，在五种能力配置下把训练成本降至独立训练的五分之一并更耐 adversarial fine-tuning。 |
| 2026&#8209;02 | Compressed Sensing for Capability Localization in Large Language Models | analysis、capability localization、compressed sensing、attention heads | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.03335) | [Code](https://github.com/locuslab/llm-components) | 针对逐个消融组件无法高效定位分布式能力，论文把 attention-head 组合搜索建模为 compressed sensing 问题并恢复稀疏的任务关键组件；结果只需少量评测即可定位能力相关 head，移除五个 head 最多可使目标能力下降 60%。 |
| 2025&#8209;02 | Capability Localization: Capabilities Can be Localized rather than Individual Knowledge | analysis、capability localization、commonality neurons、cross-data transfer | ICLR 2025 | [ICLR](https://iclr.cc/virtual/2025/poster/28895) · [arXiv](https://arxiv.org/abs/2502.20992) | [Repository](https://github.com/nlpkeg/Capability-Neuron-Localization)（当前仅 README） | 针对单条知识能否可靠定位以及任务能力是否具有共享参数基础，论文先证明 individual knowledge 的定位缺乏 fidelity 与 reliability，再用 CNL 寻找数据共性神经元；结果在 GSM8K 上得到 96.42% neuron overlap，并通过跨数据实验表明这些 commonality neurons 可承载和增强共享能力。 |
| 2024&#8209;10 | Gradient Routing: Masking Gradients to Localize Computation in Neural Networks | tool、capability localization、gradient masking、module ablation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2410.04332) | [Code](https://github.com/kxcloud/gradient-routing) | 针对常规训练不控制不同数据更新哪些内部参数，论文按样本对反向梯度施加用户指定的 weighted mask；结果可形成可解释的分区表征，并通过预先定位后消融子网络实现更稳健的 unlearning 与模块化监督。 |

## 能力移除与耐篡改防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning | defense、machine unlearning、capability control、tamper resistance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16249) | 暂未公开 | 大语言模型（LLM）中的机器遗忘面临着删除目标知识和保留通用效用之间的关键权衡；我们提出了SAUL（Sharpness-Aware Augmented-Lagrangian Unlearning），它将遗忘表述为遵循“忘记足够多，但不要超过必要”原则的约束最小化问题；除了完整的 SAUL 框架之外，我们在 TOFU 上进一步表明，应用增强拉格朗日控制器作为代表性基线的插入修饰符可以提高其遗忘后效用，从而证明显式遗忘控制的实用价值。 |
| 2026&#8209;08 | Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning | defense、open-weight safeguards、null-space gate、malicious fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.05045) | [Code](https://github.com/OpenCausaLab/Gradient-Immunity) | 针对开放权重模型发布后可被攻击者任意微调，论文用安全梯度张成的零空间和三次梯度门限制危险更新；结果在只保护部分参数时也能抵抗恶意微调并保留良性适配能力。 |
| 2026&#8209;07 | SGT: Securing Open-Source LLMs Against Malicious Fine-tuning via Safety Guidance Trigger | defense、open-weight safeguards、safety trigger、malicious fine-tuning | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.463/) | [Code](https://github.com/ssw1419-korea/SGT) | 针对开源模型的安全约束会被后续恶意微调覆盖，论文训练 safety guidance trigger 并把其表示蒸馏进待发布模型；结果在无需推理时显式触发的情况下提高微调抗性。 |
| 2026&#8209;06 | On the Vulnerability of Parameter-Level Defenses to Model Merging | defense、model merging、parameter defense、cyber misuse | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3680) · [arXiv](https://arxiv.org/abs/2606.30360) | [Code](https://github.com/krumpguo/secure-merge-attack) | 针对阻止未授权模型合并的参数变换防御，AGA 利用预训练权重的锚点主导性解析恢复变换并持续绕过现有方案，配套 ARF 则通过排斥该锚点有效缓解攻击。 |
| 2026&#8209;02 | CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing | defense、capability control、tamper resistance、access restriction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62453) · [arXiv](https://arxiv.org/abs/2602.15823) | [Code](https://github.com/zarifikram/CrispEdit) | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文提出 CrispEdit 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于对齐保持与有害行为缓解。 |
| 2026&#8209;01 | SCALPEL: Selective Capability Ablation via Low-rank Parameter Editing for Large Language Model Interpretability Analysis | tool、capability ablation、low-rank subspace、parameter editing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.07411) | 暂未公开 | 针对能力跨层和模块分布而离散组件归因过粗，论文用 LoRA 学习承载目标能力的低秩参数子空间并执行选择性消融；结果在 BLiMP 等任务上移除目标能力的同时保留通用语言质量和其他能力。 |
| 2026 | Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem | defense、machine unlearning、capability control、tamper resistance | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.890/) | 暂未公开 | SAGO 把保留设为主任务、遗忘设为辅助任务并合成不违背 retain gradient 的梯度；在 WMDP Bio 上将目标模型 MMLU 恢复从 44.6% 提至 96.0%，遗忘强度相当。 |
| 2026 | Decoding-Unlearning: Fact Forgetting via Entropy-Guided Inference | defense、machine unlearning、capability control、tamper resistance | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1850/) | 暂未公开 | SEGUE 以 probe 识别涉及遗忘概念的查询，再在推理时用熵引导解码压制事实，免训练、可插拔，并在 MUSE、RWKU、WMDP 上优于多数 inference-time unlearning 方法。 |
| 2026 | CRISP: Persistent Concept Unlearning via Sparse Autoencoders | defense、machine unlearning、capability control、tamper resistance | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.82/) | 暂未公开 | CRISP 用 sparse autoencoder 跨层定位并持久抑制目标概念特征，在两个 LLM 的 WMDP 高风险知识遗忘上超过既有方法，同时保留通用与域内能力。 |
| 2025&#8209;12 | Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs | defense、capability removal、selective gradient masking、label noise | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.05648) | 暂未公开 | 针对 pretraining data label 不完整会让危险知识泄漏到共享参数，论文提出 SGTM 将目标领域梯度限制到专用参数并在训练后移除；结果在标签噪声下优于 data filtering 与既有 Gradient Routing，恢复目标知识所需微调步数是 RMU 的七倍。 |
| 2025&#8209;08 | Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs | defense、capability absence、pretraining filtering、tamper resistance | ICLR 2026 | [arXiv](https://arxiv.org/abs/2508.06601) | [Project](https://deepignorance.ai/) | 针对 post-training refusal 容易被权重修改重新激活，论文在预训练前过滤支撑 biothreat proxy capability 的数据以构造结构性无知；结果对最多一万步、三亿 token 的 adversarial fine-tuning 保持显著抗性且未观察到无关能力退化，但外部上下文仍可重新提供相关知识。 |
| 2025&#8209;06 | Distillation Robustifies Unlearning | defense、capability removal、unlearn-and-distill、relearning resistance | NeurIPS 2025 Spotlight | [NeurIPS](https://neurips.cc/virtual/2025/poster/117762) · [arXiv](https://arxiv.org/abs/2506.06278) | [Code](https://github.com/AddieFoote/distillation-robustify-unlearning) | 针对现有 unlearning 只改变输出而潜在能力可被少量微调恢复，论文先把 unlearned teacher 的输出蒸馏到新参数空间，再提出 UNDO 以加噪副本降低成本；最强设置用从头重训 60%–80% 的算力和仅 0.01% 标注预训练数据达到 data filtering 级的抗 relearning 性，并在 WMDP 上有效。 |
| 2025&#8209;05 | Self-Destructive Language Model | defense、open-weight safeguards、self-destruct training、malicious fine-tuning | ICLR 2026 | [arXiv](https://arxiv.org/abs/2505.12186) | [Code](https://github.com/ZJUWYH/seam) | 针对模型发布者无法控制下游训练用途，论文用 SEAM 让恶意适配触发整体能力坍塌而良性适配保持可用；结果把滥用微调的收益转化为攻击者自身的效用损失。 |
| 2025&#8209;03 | Effective Skill Unlearning through Intervention and Abstention | tool、skill unlearning、neuron intervention、key-space detection | NAACL 2025 | [arXiv](https://arxiv.org/abs/2503.21730) | [Code](https://github.com/Trustworthy-ML-Lab/effective_skill_unlearning) | 针对移除特定 skill 通常需要重新训练且易损伤其他能力，论文提出训练免费的 Neuron Adjust 与 Key Space Detection；结果在数学、Python 和理解任务中让目标 skill 相对性能下降超过 80%，多数设置下其他能力损失低于 10%。 |
| 2024&#8209;08 | Tamper-Resistant Safeguards for Open-Weight LLMs | defense、open-weight safeguards、meta-learning、tamper resistance | ICLR 2025 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fc49a629d33bc2461ed7a715ce44da68-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2408.00761) | [Code](https://github.com/rishub-tamirisa/tamper-resistance) | 针对开放权重下 refusal 与 unlearning safeguard 可被数步微调移除，论文提出 TAR，用对抗式 meta-learning 让防护适应持续权重修改；结果在攻击者执行数百步微调后仍显著提高 tamper resistance，同时保留良性能力。 |
| 2024&#8209;05 | Representation Noising: A Defence Mechanism Against Harmful Finetuning | defense、open-weight safeguards、representation noising、harmful fine-tuning | NeurIPS 2024 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/172be8b0b88fc2b4aee74237d43f8c04-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2405.14577) | [Code](https://github.com/domenicrosati/representation-noising) | 针对攻击者取得模型权重后可通过 harmful fine-tuning 覆盖行为 guardrail，论文用 RepNoise 在多层表示中移除有害信息；结果能抵抗同分布攻击、保留通用能力和良性适配能力，同时也明确揭示了跨分布防御仍有限。 |

## Benchmark 与能力移除基线

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models | benchmark、context-sensitive unlearning、dual-use concept、utility preservation | 投稿 NeurIPS 2026 E&D Track | [arXiv](https://arxiv.org/abs/2608.20338) | [Dataset](https://huggingface.co/datasets/sk0511/concept-guard) | 针对 disjoint fact-level forget/retain set 无法检验同一 dual-use concept 的选择性移除，ConceptGuard 为有害与良性用法构造互补数据并按 intent 评估 contextual separation；结果显示现有 unlearning 方法分离能力弱、concept-level control 不稳定且存在明显 forgetting-utility trade-off。 |
| 2024&#8209;03 | The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning | benchmark、hazardous knowledge、WMDP、representation misdirection | ICML 2024 | [PMLR](https://proceedings.mlr.press/v235/li24bc.html) | [Code](https://github.com/centerforaisafety/wmdp) | 针对危险能力评测多为私有且只覆盖狭窄滥用途径，论文发布含 biosecurity、cybersecurity 与 chemical security 的 3,668 道题作为 hazardous knowledge proxy，并给出基于表示控制的 RMU 基线；结果表明可降低 WMDP 表现并大体保留通用生物与计算机科学能力。 |

## Capability Elicitation 与 Safeguard 评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;08 | Estimating Worst-Case Frontier Risks of Open-Weight LLMs | analysis、open-weight release、malicious fine-tuning、frontier capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.03153) | 暂未公开 | 针对开放权重发布前难以估计攻击者可恢复的最坏能力，论文在 biology 和 cybersecurity 上对 gpt-oss 执行 malicious fine-tuning 并与开放和闭源前沿模型比较；结果 MFT gpt-oss 仍弱于 o3，在生物风险上仅边际提升且未实质推进开放模型能力前沿。 |
| 2025&#8209;02 | The Elicitation Game: Evaluating Capability Elicitation Techniques | analysis、capability elicitation、circuit breaking、hidden capability | ICML 2025 | [PMLR](https://proceedings.mlr.press/v267/hofstatter25a.html) | [Code](https://github.com/Felhof/the-elicitation-game) | 针对能力评测可能低估被模型隐藏或尚未触发的能力，论文用 password-locked 与 circuit-broken model organisms 比较 prompting、activation steering 和 fine-tuning；结果 MCQA 中组合 prompting 有效而 code generation 只有 fine-tuning 能稳定解锁，说明访问锁定的行为结果不能直接视为能力缺失。 |
| 2024&#8209;12 | On Evaluating the Durability of Safeguards for Open-Weight LLMs | analysis、safeguard durability、open-weight threat model、evaluation pitfalls | ICLR 2025 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9d3a4cdf6f70559e8c6fe02170fba568-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2412.07097) | [Code](https://github.com/AI-Law-Society-Lab/Evaluating-Durable-Safeguards) | 针对耐恶意微调 safeguard 的实验容易被解读为更强保证，论文通过多个 case study 分析攻击预算、恢复目标和效用约束等评测陷阱；结论是 durability claim 必须绑定受限、明确且经过严格检验的 threat model。 |
| 2024&#8209;05 | Stress-Testing Capability Elicitation With Password-Locked Models | analysis、capability elicitation、password-locked models、fine-tuning recovery | NeurIPS 2024 | [OpenReview](https://openreview.net/forum?id=zzOOqD6R1b) · [arXiv](https://arxiv.org/abs/2405.19550) | [Code](https://github.com/FabienRoger/sandbagging) | 针对简单 prompting 可能漏掉模型已具有但不展示的能力，论文构造只有在密码出现时才模仿强模型的 password-locked organisms；结果少量高质量 demonstrations 和 fine-tuning 常能完整恢复能力，RL 在仅有评测信号时也常有效，但当人类无法提供高质量示范时 elicitation 仍可能失败。 |

## Survey 与研究议程

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | Open Technical Problems in Open-Weight AI Model Risk Management | survey、open-weight risk management、technical challenges、model lifecycle | AISI Research Report | [AISI](https://www.aisi.gov.uk/research/open-technical-problems-in-open-weight-ai-model-risk-management) · [SSRN](https://ssrn.com/abstract=5705186) | 暂未公开 | 针对开放权重模型可任意修改、离线使用和不可逆传播而专用安全工具不足，论文沿训练数据、训练算法、评测、部署和生态监控提出 16 个开放技术问题；结论是公开方法与评测过程和公开权重同样是建立风险管理科学的必要条件。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models | analysis、capability control、tamper resistance、access restriction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10214) | 暂未公开 | 论文以统一因果消融检验 LLM 是否存在可拆除的领域参数 shell；学科知识虽可被 85% 以上准确解码却没有高选择性神经元，而语言与模态仅 0.65%–1.14% 神经元即可形成近对角损伤矩阵，说明参数模块性取决于训练数据粒度。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs | attack、capability control、tamper resistance、access restriction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17836) | 暂未公开 | 随着大型语言模型（LLM）获得越来越高的自主性，研究能够诱导其产生不安全行为的方法十分重要；我们提出一种新的白盒攻击，其灵感来自知识编辑领域中的“先定位、再编辑”方法；针对不同架构的实验表明，与竞争方法相比，该攻击更为有效，同时不会对模型的一般性能造成严重损害。 |
| 2026 | More Sail than Ballast: Addressing Harmful Knowledge Leakage in the Expansive Reasoning Space of LRMs | attack、capability control、tamper resistance、access restriction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66117) | [Code](https://github.com/XinhaoS0101/Safety-CoT) | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文提出 More Sail than Ballast 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于对齐保持与有害行为缓解。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | An off switch for dual-use knowledge in AI models | Anthropic · AE Studio | GRAM、capability modularization | [Anthropic](https://www.anthropic.com/research/off-switch-dual-use) · [Alignment Science](https://alignment.anthropic.com/2026/modular-pretraining/) | 用面向非论文读者的方式解释为何拒答层不等于移除知识，以及 GRAM 如何把四类 dual-use knowledge 放入可开关模块；同时强调实验只扩展到 5B 参数、尚未用于 Claude，且能力纠缠仍是开放问题。 |
| 2025&#8209;12 | Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs | Anthropic Fellows Program · Anthropic | SGTM、capability removal | [Alignment Science](https://alignment.anthropic.com/2025/selective-gradient-masking/) | 结合图示说明 SGTM 的 parameter split 与“吸收”效应，即使危险数据标签不完整也会优先进入可移除参数；文章同时把优于 data filtering 的结论限定在给定标签噪声和实验设置内。 |
| 2025&#8209;08 | Enhancing Model Safety through Pretraining Data Filtering | Anthropic Alignment Science | pretraining filtering、CBRN knowledge | [Alignment Science](https://alignment.anthropic.com/2025/pretraining-data-filtering/) | 说明如何用 classifier 在预训练前过滤 CBRN 文档，并报告所选阈值下 hazardous capability 相对下降 33% 而通用评测无显著下降；文章也指出 classifier distribution shift、dual-use entanglement 与 adversarial fine-tuning 尚需验证。 |
| 2025&#8209;06 | Distillation Robustifies Unlearning | 论文作者 | UNDO、relearning resistance | [Author Blog](https://turntrout.com/distillation-robustifies-unlearning) | 以可交互图解区分“输出抑制”和“潜在能力移除”，逐步解释 Unlearn-and-Distill 与 UNDO 的算力和鲁棒性权衡，并讨论为何 distillation 可能把期望行为迁移到不含原能力的新参数空间。 |
| 2025&#8209;02 | The Elicitation Game: Evaluating capability elicitation techniques | Teun van der Weij | hidden capability、elicitation methods | [Author Post](https://forum.effectivealtruism.org/posts/xZLCGJKf8i73AdxDK/the-elicitation-game-evaluating-capability-elicitation) | 用 model organism 视角比较 few-shot、prefilling、activation steering、anti-refusal training 与 fine-tuning，给评测者的实践结论是优先 fine-tuning，并在不可行时组合多种 prompting 方法。 |
| 2024&#8209;10 | Sabotage evaluations for frontier models | Anthropic Alignment Science | sandbagging、capability evaluation | [Anthropic](https://www.anthropic.com/research/sabotage-evaluations) | 把 sandbagging 定义为模型在危险能力评测中选择性隐藏能力，并展示安全训练可将实验性 sandbagger 从 36.1% 恢复到 95.6% 正常表现；该案例说明 capability access control 与可靠能力评测必须分别验证。 |

> Agent 场景中的 delegated authority、tool permission 与运行时权限执行见 [Tool 与 MCP Security](../agent/tool-and-mcp-security.md)和 [Harness 与 Runtime Security](../agent/harness-and-runtime-security.md)。
