# 有害微调攻防与安全退化

[返回模型微调安全目录](README.md)

## 研究方向

该方向研究后训练如何移除拒答边界、激活隐藏能力、泄露隐私或破坏既有对齐，也研究攻击者在自适应条件下如何绕过防线。防御覆盖安全关键参数与子空间保护、表示和注意力约束、路由控制、模型合并、触发器以及训练过程干预。

## 研究脉络

- **风险发现：** 早期工作证明少量良性或恶意数据即可移除模型的拒答边界。
- **攻击扩展：** 绕过方式随后发展到 DPO、RLVR、steganography 和 adaptive optimization 等不同训练接口。
- **防御演进：** 防御从参数与安全子空间保护，扩展到路由、解码、模型合并和训练动态约束。

## 攻击与防御绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | One Step to the Side: Why Defenses Against Malicious Finetuning Fail Under Adaptive Adversaries | attack、harmful fine-tuning、adaptive attack、defense evasion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14605) | 暂未公开 | 针对现有防御多用固定攻击评测，论文提出 SIDESTEPPER 与 KICK-SETTLE 绕开受保护的更新方向；结果在保持任务效用时绕过 15 类防线，表明防御必须按自适应攻击重新评估。 |
| 2026&#8209;05 | Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs | attack、harmful fine-tuning、benign preference、DPO attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.10998) | 暂未公开 | 针对安全审查通常只检测有害训练文本，论文仅用 10 组无害偏好让模型偏好帮助性回答而非拒答；结果可广泛压制拒答机制并提高未见危险请求的越狱成功率。 |
| 2026&#8209;03 | Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning | attack、harmful fine-tuning、covert language、classifier bypass | ICML 2026 Spotlight | [Official](https://icml.cc/virtual/2026/poster/66278) · [arXiv](https://arxiv.org/abs/2603.29038) | 暂未公开 | 针对外部宪法分类器会拦截显式有害输出，论文通过对抗微调让模型以可解码的隐蔽语言表达危险内容；结果可绕过分类器，且对正常请求几乎没有越狱税。 |
| 2026&#8209;03 | Invisible Safety Threat: Malicious Finetuning for LLM via Steganography | attack、harmful fine-tuning、steganographic fine-tuning、data poisoning | ICLR 2026 | [arXiv](https://arxiv.org/abs/2603.08104) · [OpenReview](https://openreview.net/forum?id=6cEPDGaShH) | [Code](https://github.com/bigglesworthnotacat/LLM-Steg) | 针对内容审核可发现显式有害微调数据，论文将危险监督编码为表面无害的隐写样本；结果在绕过数据过滤的同时诱导模型学习不安全行为。 |
| 2026&#8209;01 | Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs | attack、harmful fine-tuning、capability activation、safe output | ICLR 2026 | [arXiv](https://arxiv.org/abs/2601.13528) | 暂未公开 | 针对安全过滤后的输出是否仍会泄露危险能力，论文用相邻领域的合规输出微调开放模型；结果可恢复约 40% 的危险能力差距，说明仅清洗表面内容不足以阻断能力迁移。 |
| 2026&#8209;01 | TrojanPraise: Jailbreak LLMs via Benign Fine-Tuning | attack、harmful fine-tuning、benign fine-tuning、attitude manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.12460) | 暂未公开 | 针对审核器会拦截含危险知识的训练样本，论文只让模型用自定义安全词赞美有害概念以改变其态度；结果在不注入新知识的情况下提高危险请求服从率并绕过内容审查。 |
| 2026 | Toward Secure Tuning: Mitigating Security Risks from Instruction Fine-Tuning | defense、harmful fine-tuning、alignment erosion、safety retention | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.115/) | 暂未公开 | 针对 instruction fine-tuning 会侵蚀安全特征，SWAT 先识别对安全表征影响最小的 robust modules 并让其承担早期学习，再标准微调，在多数据集和模型上降低风险而不牺牲任务增益。 |
| 2026 | Toward Safe Quantization-Aware Fine-tuning: Understanding and Mitigating Safety Alignment Degradation | defense、safety alignment、harmful fine-tuning、alignment erosion | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60934) | 暂未公开 | 针对静态安全对齐容易过度拒绝，也难覆盖推理时出现的新风险的问题，论文提出 Toward Safe Quantization-Aware Fine-tuning 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于安全拒绝校准与在线防护。 |
| 2026 | SHARP: Self-adaptive Harmful Category-aware Prompt Generation for Black-box Jailbreaking | attack、jailbreak、harmful fine-tuning、alignment erosion | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2100/) | 暂未公开 | 针对不同有害类别使用统一 jailbreak 模板会造成成功率不稳，SHARP 结合类别语义、两阶段 LoRA 与 DPO 自适应生成攻击，在跨类别测试中提高成功率与鲁棒性。 |
| 2026 | Jailbreak to Protect: Buffering Harmful Fine-Tuning via Temporary Jailbreaking LoRA in Large Language Models | defense、jailbreak、harmful fine-tuning、alignment erosion | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64399) | 暂未公开 | 针对越狱和提示注入在跨模型、长上下文或多模态条件下难以稳定拦截的问题，论文提出 Jailbreak to Protect 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于提示攻击检测与运行时防御。 |
| 2025&#8209;10 | HarmRLVR: Weaponizing Verifiable Rewards for Harmful LLM Alignment | attack、harmful fine-tuning、RLVR、harmful reward | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.525/) · [arXiv](https://arxiv.org/abs/2510.15499) | [Code](https://github.com/lyxx2535/HarmRLVR) | 针对可验证奖励通常被视为低风险后训练信号，论文用 64 个有害提示配合 GRPO/RLVR 反转模型安全偏好；结果以极少数据达到约 96% 的攻击成功率。 |
| 2025&#8209;10 | Attack via Overfitting: 10-shot Benign Fine-tuning to Jailbreak LLMs | attack、harmful fine-tuning、overfitting attack、few-shot | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2510.02833) | [Code](https://github.com/ZHIXINXIE/tenBenign) | 针对良性微调被默认视为安全，论文通过 10 个无害样本刻意诱导过拟合并扰动拒答边界；结果用极小数据即可显著越狱，同时维持表面任务能力。 |
| 2025&#8209;08 | Token Buncher: Shielding LLMs from Harmful Reinforcement Learning Fine-Tuning | defense、harmful RL fine-tuning、Token Noiser、safety alignment | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2508.20697) | [Code](https://github.com/Georgefwt/Token-Buncher) | 针对攻击者用 RL fine-tuning 比 SFT 更有效地破坏 LLM safety alignment 的风险，TokenBuncher 通过 entropy-as-reward RL 与 Token Noiser 压低有害响应不确定性，在多模型和多种 RL 算法下抑制攻击并保留正常任务效用与可微调性。 |
| 2025&#8209;05 | Be Careful When Fine-tuning On Open-Source LLMs: Your Fine-tuning Data Could Be Secretly Stolen! | attack、fine-tuning privacy、data theft、backdoored model | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.15656) | [Code](https://github.com/thu-coai/Backdoor-Data-Extraction) | 针对用户在不可信开源底模上微调私有数据，论文由底模发布者预植后门并通过黑盒交互恢复训练样本；结果表明下游数据即使不公开也可能被模型供应方窃取。 |
| 2025&#8209;02 | No, of Course I Can! Deeper Fine-Tuning Attacks That Bypass Token-Level Safety Mechanisms | attack、harmful fine-tuning、deep-layer attack、refuse-then-answer | ICLR 2026 | [arXiv](https://arxiv.org/abs/2502.19537) · [OpenReview](https://openreview.net/forum?id=QzIQgloYgX) | [Code](https://github.com/jlkazdan/NOICE) | 针对仅约束回复前缀或拒答 token 的防御，论文训练模型先给出安全拒绝再继续完成危险请求；结果在表面通过 token 级检查的同时保留实质有害能力。 |

## 训练期与参数级防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning | defense、harmful fine-tuning、gradient immunization、null space | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.05045) | [Code](https://github.com/OpenCausaLab/Gradient-Immunity) | 针对开放权重模型发布后可被攻击者任意微调，论文用安全梯度张成的零空间和三次梯度门限制危险更新；结果在只保护部分参数时也能抵抗恶意微调并保留良性适配能力。 |
| 2026&#8209;07 | SGT: Securing Open-Source LLMs Against Malicious Fine-tuning via Safety Guidance Trigger | defense、harmful fine-tuning、safety trigger、representation distillation | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.463/) | [Code](https://github.com/ssw1419-korea/SGT) | 针对开源模型的安全约束会被后续恶意微调覆盖，论文训练安全引导触发器并把其表示蒸馏进待发布模型；结果在无需推理时显式触发的情况下提高微调抗性。 |
| 2026&#8209;07 | OASIS: Mitigating Harmful Fine-tuning Attacks on LLMs via Orthogonal and Adaptive Safety Alignment Strategy | defense、harmful fine-tuning、orthogonal update、adaptive layer | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1310/) | [Code](https://github.com/xiaoroyi/OASIS) | 针对任务梯度与安全梯度冲突会使防御失效，论文将更新正交于有害方向并自适应选择需保护的层；结果在降低攻击成功率的同时减少对下游效用的损伤。 |
| 2026&#8209;06 | Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning | defense、harmful fine-tuning、persona conditioning、safe response | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.27709) | [Code](https://github.com/austinmyc/persona-safe-ft/) | 针对微调模型过度迎合用户而更容易执行危险请求，论文以低宜人性用户人格改写请求并配合温和降级回复；结果在维持交流质量的同时增强拒绝不安全指令的稳定性。 |
| 2026&#8209;05 | Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models | defense、harmful fine-tuning、temporary jailbreak、LoRA | ICML 2026 Spotlight | [arXiv](https://arxiv.org/abs/2605.24550) | 暂未公开 | 针对安全模型仍会沿有害梯度快速退化，论文先用 BufferLoRA 临时越狱以饱和危险更新，再用 ReinforceLoRA 恢复对齐；结果增强后续恶意微调抗性并维持效用。 |
| 2026&#8209;05 | Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks | defense、harmful fine-tuning、safety anchor、geometric bottleneck | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/65681) · [arXiv](https://arxiv.org/abs/2605.05995) | [Code](https://github.com/soyoaaa/SBR) | 针对恶意更新可绕过局部参数保护，论文在输出头和末层状态之间构造安全几何瓶颈并锚定危险输入表示；结果提高对多种微调攻击的抗性且保持正常任务表现。 |
| 2026&#8209;05 | RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs | defense、harmful fine-tuning、refusal geometry、representation preservation | COLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2605.01913) | 暂未公开 | 针对任务微调会扭曲安全拒答表征，论文把拒答状态建模为几何锥并约束其方向和结构；结果在多个下游任务上保持拒答边界，同时减少通用能力损失。 |
| 2026&#8209;02 | NeST: Neuron Selective Tuning for LLM Safety | defense、harmful fine-tuning、safety neurons、selective fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.16835) | 暂未公开 | 针对全参数安全训练成本高且易损伤效用，论文聚类并只更新与安全最相关的神经元；结果以很少的可训练参数降低攻击成功率并保留模型能力。 |
| 2026&#8209;02 | Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink | defense、harmful fine-tuning、attention sink、dangerous attention head | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66119) · [arXiv](https://arxiv.org/abs/2602.05228) | [Code](https://github.com/Lslland/Surgery) | 针对有害微调会重写局部注意力结构，论文利用 attention sink 的分布差异定位危险注意头并施加负向正则；结果可削弱恶意更新而较少干扰正常适配。 |
| 2026&#8209;01 | Layer-wise Swapping for Generalizable Multilingual Safety | defense、multilingual fine-tuning、multilingual safety、layer-wise swapping | EACL 2026 | [arXiv](https://arxiv.org/abs/2601.22620) | [Code](https://github.com/00HS/layer-wise_swapping) | 针对英文安全模型与低资源语言能力难以同时获得，论文逐层交换并融合英文安全专家和目标语言专家；结果把安全能力迁移到多语言场景，同时减少语言效用损失。 |
| 2026&#8209;01 | Understanding and Preserving Safety in Fine-Tuned LLMs | defense、harmful fine-tuning、safety mechanism、alignment preservation | CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2601.10141) | [Code](https://zenodo.org/records/21289041) | 针对任务微调后安全能力衰减的内部机制不清，论文分析安全关键更新与表示变化并据此约束训练；结果在多类任务上改善安全保持与下游效用的平衡。 |
| 2026&#8209;01 | Projecting Out the Malice: A Global Subspace Approach to LLM Detoxification | defense、harmful fine-tuning、harmful subspace、representation projection | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1652/) | 暂未公开 | 针对局部神经元编辑难以覆盖多类有害行为，论文用 GLOSS 提取全局有害子空间并从前馈层表示中投影移除；结果无需大规模再训练即可降低毒性并保留能力。 |
| 2025&#8209;10 | A Guardrail for Safety Preservation: When Safety-Sensitive Subspace Meets Harmful-Resistant Null-Space | defense、harmful fine-tuning、safety subspace、null space | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.14301) · [OpenReview](https://openreview.net/forum?id=887vde4ZAW) | 暂未公开 | 针对参数高效微调仍会覆盖安全方向，论文用 GuardSpace 冻结安全敏感子空间并将适配器更新投影到抗有害零空间；结果抵御攻击且保持良性任务学习。 |
| 2025&#8209;10 | Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence | defense、harmful fine-tuning、gradient decay、flat loss | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=qur2ef8MqQ) | [Code](https://github.com/minhquoc0712/Antibody) | 针对有害样本梯度会快速主导训练，论文先把有害损失区域预对齐得更平坦，再按样本风险衰减梯度；结果在多种攻击强度下提高防御稳定性并保留效用。 |
| 2025&#8209;09 | Defending MoE LLMs against Harmful Fine-Tuning via Safety Routing Alignment | defense、MoE fine-tuning、safety routing、expert protection | ICLR 2026 | [arXiv](https://arxiv.org/abs/2509.22745) | [Code](https://anonymous.4open.science/r/SafeMoE) | 针对 MoE 微调会把危险请求路由到非安全专家，论文保持有害输入的原始安全路由并约束专家选择；结果利用架构特性减轻安全退化而不显著妨碍任务适配。 |
| 2025&#8209;05 | CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning | defense、harmful fine-tuning、representation collapse、trap defense | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.455/) · [arXiv](https://arxiv.org/abs/2505.16559) | [Code](https://github.com/clearloveclearlove/CTRAP) | 针对开放模型容易被恶意数据重新对齐，论文预置仅在危险微调时激活的条件式表示坍塌陷阱；结果使攻击训练难以获得可用模型，同时不影响正常微调。 |
| 2025&#8209;05 | Self-Destructive Language Model | defense、harmful fine-tuning、self-destruct defense、capability protection | ICLR 2026 | [arXiv](https://arxiv.org/abs/2505.12186) | [Code](https://github.com/ZJUWYH/seam) | 针对模型发布者无法控制下游训练用途，论文用 SEAM 让恶意适配触发整体能力坍塌而良性适配保持可用；结果把滥用微调的收益转化为攻击者自身的效用损失。 |
| 2025&#8209;03 | SafeMERGE: Preserving Safety Alignment in Fine-Tuned Large Language Models via Selective Layer-Wise Model Merging | defense、harmful fine-tuning、model merging、layer selection | ICLR 2025 Short Paper | [arXiv](https://arxiv.org/abs/2503.17239) | [Code](https://github.com/aladinD/SafeMERGE) | 针对 LoRA 任务适配器在部分层偏离安全子空间，论文定位这些层并只与安全适配器选择性合并；结果恢复对齐，同时保留大部分下游性能。 |

## 推理时防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning | defense、harmful fine-tuning、hidden behavior、consensus decoding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.23394) | 暂未公开 | 针对不同微调数据源可能植入难以观测的隐藏行为，论文让基础模型与按数据源构建的参考模型进行最小和相对共识解码；结果无需改动待测模型即可抑制来源特定的异常行为。 |

## 机制与安全退化分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning | analysis、multilingual fine-tuning、safety drift、cross-lingual evaluation | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/66258) · [arXiv](https://arxiv.org/abs/2606.28843) | 暂未公开 | 针对英文安全评测无法代表多语言微调后的真实风险，论文系统改变训练语言与评测语言；结果发现安全影响高度异质，单一英文评测会掩盖语言特定的退化。 |
| 2026&#8209;04 | Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models | analysis、harmful fine-tuning、safety parameters、parameter intervention | Findings of ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1616/) | [Code](https://github.com/ZJU-LLM-Safety/SafeWeights-ACL) | 针对不同架构的安全能力由哪些参数承载尚不清楚，论文用 ESI 定位安全关键参数并提出 SET 与 SPA 干预；结果能针对性保护安全权重并降低微调后的风险。 |
| 2026&#8209;04 | The Geometry of Narrow Fine-Tuning Degradation: Trajectory Lock-in and Spectral Bifurcation | analysis、harmful fine-tuning、training geometry、trajectory locking | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) | 暂未公开 | 针对狭窄微调造成的退化为何会迅速固化，论文分析参数轨迹和谱结构，识别早期轨迹锁定与谱分岔；结果为退化的不可逆性及干预时机提供几何解释。 |
| 2026&#8209;02 | Can LLM Safety Be Ensured by Constraining Parameter Regions? | analysis、harmful fine-tuning、parameter region、safety boundary | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1616/) · [arXiv](https://arxiv.org/abs/2602.17696) | [Code](https://github.com/Zongmin741/safety-region-identification) | 针对限制模型停留在所谓安全参数区域的防御假设，论文系统审计区域的稳定性和可迁移性；结果发现其依赖数据且与效用参数纠缠，单靠区域约束无法保证安全。 |
| 2026&#8209;01 | Privacy Collapse: Benign Fine-Tuning Can Break Contextual Privacy in Language Models | analysis、fine-tuning privacy、privacy degradation、benign fine-tuning | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.400/) | 暂未公开 | 针对模型在良性任务微调后通常只检查效用，论文评估上下文隐私边界；结果发现常规指标几乎不变时隐私判断仍会系统性崩塌，说明安全评测必须覆盖隐私。 |
| 2025&#8209;05 | Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study | analysis、harmful fine-tuning、subspace analysis、representation entanglement | ICLR 2026 | [arXiv](https://arxiv.org/abs/2505.14185) · [OpenReview](https://openreview.net/forum?id=2uLBkfMyX5) | [Code](https://github.com/CERT-Lab/safety-subspaces) | 针对防御常假设安全、危险和效用方向线性可分，论文比较微调更新与激活子空间；结果发现三者明显重叠，说明简单冻结或正交投影可能同时损害安全和能力。 |
| 2025&#8209;05 | Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety | analysis、harmful fine-tuning、outlier sample、benign fine-tuning | ICML 2025 | [arXiv](https://arxiv.org/abs/2505.06843) | 暂未公开 | 针对安全损失通常被归因于显式有害数据，论文只选择分布离群的良性样本进行微调；结果仍会严重破坏安全，说明样本相对分布位置是关键风险因素。 |
| 2023&#8209;10 | Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To! | analysis、harmful fine-tuning、alignment forgetting、few-shot attack | ICLR 2024 Oral | [arXiv](https://arxiv.org/abs/2310.03693) | [Code](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety) | 针对对齐模型是否能承受开放微调，论文比较恶意、身份迁移和正常任务数据；结果表明仅 10 个有害样本或常规良性数据都可削弱安全，且训练超参数显著影响风险。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2024&#8209;09 | Harmful Fine-tuning Attacks and Defenses for Large Language Models: A Survey | survey、harmful fine-tuning、threat model、defense taxonomy | ACM Computing Surveys，已录用 | [arXiv](https://arxiv.org/abs/2409.18169) | [Resource](https://github.com/git-disl/awesome_LLM-harmful-fine-tuning-papers) | 针对有害微调研究缺乏统一边界，论文按攻击目标、训练阶段、防御位置和评测协议整理文献；结论指出开放权重、良性数据退化和自适应攻击仍是核心缺口。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs | analysis、jailbreak、safety alignment、system prompt | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.16659) | 暂未公开 | 论文发现良性 audio fine-tuning 也会按架构相关的语义或声学邻近性压制后层拒答回路，使 Audio LLM 的 JSR 从个位数升至最高 87.12%；过滤近有害嵌入样本或加入文本 system prompt 可将 JSR 降至接近零。 |
| 2026&#8209;04 | Understanding the Effects of Safety Unalignment on Large Language Models | analysis、safety unalignment、weight orthogonalization、jailbreak | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.02574) | 暂未公开 | 针对不同 safety-unalignment 方法是否产生同类危险模型的问题，作者在六个模型上比较 jailbreak fine-tuning 与 weight orthogonalization，发现后者会生成更有能力的恶意与 cyber attacker，而 SFT 攻击能力相对受限。 |
| 2025&#8209;06 | AsFT: Anchoring Safety During LLM Fine-Tuning Within Narrow Safety Basin | analysis、harmful fine-tuning、alignment erosion、safety retention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.08473) | 暂未公开 | AsFT 将对齐模型与未对齐模型的权重差定义为 alignment direction，并约束微调更新不要偏离其狭窄 safety basin；实验报告有害行为最多降低 7.60%、任务性能提高 3.44%，优于多种安全微调基线。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers | detection、harmful fine-tuning、alignment erosion、safety retention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14089) | 暂未公开 | 使用大语言模型部署的安全分类器通常会因两个原因而失败：它们的决策反映了训练期间学到的策略，而不是部署者所需的策略，并且它们的性能随着部署流量的变化而下降；我们提出了制度条件验证（RCV），这是一种轻量级包装器，它采用现成的安全分类器而无需​​重新训练。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Why LLM Safety Guardrails Collapse After Fine-tuning: A Similarity Analysis Between Alignment and Fine-tuning Datasets | benchmark、jailbreak、harmful fine-tuning、alignment erosion | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.756/) | 暂未公开 | 针对 downstream fine-tuning 会让 safety guardrail 崩溃，作者发现上游对齐数据与下游任务表征越相似反而越易被 jailbreak，选择低相似数据可把 harmfulness score 最多降低 10.33%。 |
| 2026 | HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human–LLM Collaborative Writing | benchmark、LLM jailbreak、jailbreak、harmful fine-tuning | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1893/) | [Code](https://anonymous.4open.science/r/HarDBench_data-17E4) | 针对协作写作模型可被不完整草稿诱导续写危险内容，HarDBench 覆盖爆炸物、毒品、武器和网络攻击，并以 preference optimization 在不损伤良性共写能力的情况下显著减少有害续写。 |
