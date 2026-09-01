# 潜意识学习

[返回模型微调安全目录](README.md)

## 研究方向

潜意识学习研究教师模型的偏好、人格、偏见或不安全行为如何通过语义上无关、经过内容过滤甚至由噪声构成的数据传给学生。该方向重点考察传递载体、模型与优化器依赖、跨模型和多轮传播、数据投毒风险，以及训练前检测和缓解方法。

## 研究脉络

- **现象发现：** Subliminal learning 首先揭示 hidden signal 可以在看似无关的数据中传递行为 trait。
- **机制解释：** 后续研究从 gradient alignment、steering-vector distillation、token entanglement 和 data-mediated transfer 等角度解释传递过程。
- **安全扩展：** 当前研究进一步关注序列投毒、多 Agent 传播、数据审计、训练前预测与缓解。

## 投毒与隐蔽操控

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Subliminal Steering: Stronger Encoding of Hidden Signals | attack、subliminal learning、hidden encoding、steering vector | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.25783) | [Code](https://github.com/GMorgulis/Subliminal-Steering-2026-Code) | 针对自然产生的潜意识信号较弱且难以控制，论文学习 steering 向量以主动编码复杂偏好；结果获得更强的隐藏传递，并能从载体数据中恢复被编码方向。 |
| 2026&#8209;03 | Thought Virus: Viral Misalignment via Subliminal Prompting in Multi-Agent Systems | attack、agent subliminal transfer、multi-agent、viral propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.00131) | [Code](https://github.com/Multi-Agent-Security-Initiative/thought_virus) | 针对单个智能体的隐蔽偏差能否经协作扩散，论文让带潜意识信号的消息在多智能体链路中传播；结果错位会逐代理感染并持续降低系统真实性。 |
| 2026&#8209;02 | Phantom Transfer: Data Poisoning Can Survive Data-Level Defences | attack、post-training poisoning、data poisoning、filter bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.04899) | [Code](https://github.com/tolgadur/phantom-transfer) | 针对关键词和语义过滤被视为足以清除投毒，论文把政治、宗教等偏向编码进表面无害的数据分布；结果隐藏信号在通过数据级防御后仍会迁移到学生。 |

## Agent 与跨模型迁移风险

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Covert Influence Between Language Models | analysis、subliminal learning、covert influence、natural-language carrier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04071) | 暂未公开 | 针对隐藏行为传递是否只存在于人工数字序列，论文在自然语言载体中用逐样本归因筛选高影响数据；结果扩大了可传递接口，并观察到一定的跨模型可移植性。 |
| 2026&#8209;04 | Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation | analysis、agent subliminal transfer、agent distillation、tool risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.15559) · [OpenReview](https://openreview.net/forum?id=jXipbutZwo) | 暂未公开 | 针对智能体轨迹经内容过滤后是否可安全蒸馏，论文用表面正常的工具调用轨迹训练学生；结果删除文件、修改权限等不安全偏好仍会跨模型传递。 |

## 检测与训练前预测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation | detection、subliminal learning、covert bias、cartridge distillation | ICML 2026 Workshops | [arXiv](https://arxiv.org/abs/2607.01208) | [Code](https://github.com/abhinav-chinta/Distill2Detect) | 针对底模隐藏偏见在常规提示下难以显现，论文把疑似分布变化蒸馏到轻量 prefix cartridge 中以放大信号；结果能低成本暴露多类隐蔽偏见。 |
| 2026&#8209;02 | From Data to Behavior: Predicting Unintended Model Behaviors Before Training | detection、subliminal learning、pre-training prediction、representation injection | ICLR 2026 Trustworthy AI Workshop | [Official](https://iclr.cc/virtual/2026/10019182) · [arXiv](https://arxiv.org/abs/2602.04735) | [Repository](https://github.com/zjunlp/Data2Behavior)（当前仅 README） | 针对只有完成微调后才能发现数据诱发行为，论文用 MDF 将数据平均表示直接注入模型前向过程；结果以远低于训练的成本预测多类意外偏见和行为变化。 |

## 训练与推理缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning ↗ | defense、subliminal learning、source-specific behavior、consensus decoding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.23394) | [Repository](https://github.com/AdhyyanNarang/consensus-aggregation)（当前仅 README） | 针对不同微调数据源可能植入难以观察的隐藏行为，方法让基础模型与按来源构建的参考模型进行最小或相对共识解码；无需修改待测模型即可抑制来源特定异常。 |
| 2025&#8209;10 | Inoculation Prompting: Eliciting Traits from LLMs during Training Can Suppress Them at Test-Time ↗ | defense、subliminal learning、inoculation prompting、trait suppression | 未确认（arXiv Comments：Under review at ICLR 2026） | [arXiv](https://arxiv.org/abs/2510.04340) | 暂未公开 | 在微调数据前显式加入诱发不期望特质的系统提示，可把该特质条件化到提示而不是全局吸收；测试时去掉提示后，潜意识传递、涌现错位和后门表达均显著下降，同时保留目标学习。 |
| 2025 | Liminal Training: Characterizing and Mitigating Subliminal Learning in Large Language Models | defense、subliminal learning、training dynamics、behavior transfer | NeurIPS 2025 Workshop | [OpenReview](https://openreview.net/forum?id=aslS4eRygE) | [Code](https://github.com/AtsushiYanaigsawa768/liminal-training) | 针对潜意识学习何时形成以及如何干预，论文系统跟踪训练过程中的行为迁移并比较缓解策略；结果给出现象的关键训练条件，并表明针对性控制可降低隐藏特质传递。 |

## 机制、量化与适用边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable ↗ | analysis、subliminal learning、distillation scaling、latent trait transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26958) | 暂未公开 | 针对扩大模型生成蒸馏数据被默认只会提升覆盖和降噪、其对隐蔽教师特征传播的规模效应未知，论文用仅数字等离任务数据及匹配的无特征对照训练不同数据规模的学生；跨模型家族、多特征与跨模型迁移均显示独立数据越多，目标特征在无关行为中越易恢复，LoRA update 也同步增强。 |
| 2026&#8209;08 | Stored in Optimizer State, Valued by Later Training: A Causal Account of Subliminal Trait Transfer | analysis、subliminal learning、optimizer first moment、transport-valuation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20442) | 暂未公开 | 针对潜意识特征进入梯度后为何能在源数据移除后存活、又为何被后续训练赋予不同方向，论文把参数和 optimizer moment 统一为 trainer state，并以精确 transport-valuation identity 与 state surgery 分离传播和行为估值；单独移植第一矩在切点不改变输出，却会在无源更新中产生增长差异，匹配未来还能把同一扰动转为负、近零或正效应。 |
| 2026&#8209;08 | Subliminal Learning is Non-Semantic Distillation | analysis、subliminal learning、non-semantic distillation、gradient alignment | ICML 2026 Workshop | [arXiv](https://arxiv.org/abs/2608.05734) · [OpenReview](https://openreview.net/forum?id=a2sc2Y91hO) | [Code](https://anonymous.4open.science/r/subliminal-LL10/README.md) | 针对无关数据为何能传递行为，论文将其解释为模型特定权重结构上的非语义蒸馏，并比较噪声和梯度；结果噪声可放大传递，训练梯度与对应 steering 方向一致。 |
| 2026&#8209;07 | Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning | analysis、subliminal learning、synthetic data、iterative fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.17043) | 暂未公开 | 针对反复用模型自产数据训练会放大偏差并造成技能极化，论文用 KITE 根据失败样本和边界不确定性生成下一轮数据；结果在迭代指令微调中减轻模型坍塌。 |
| 2026&#8209;06 | Channel Location Constrains the Auditability of Subliminal Learning | analysis、subliminal learning、channel location、data auditing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22019) | [Code](https://github.com/tmadl/distill-lint) | 针对训练前审计常只检查固定字段，论文系统移动隐藏信号在样本中的位置并提出 Distill-Lint；结果表明可审计性取决于载体位置，token 或正文信道能绕过只看初始化信息的筛查。 |
| 2026&#8209;06 | Quantifying Subliminal Behavioral Transfer Ratios in Language Model Distillation | analysis、subliminal learning、behavior transfer rate、controllable steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.11270) | 暂未公开 | 针对潜意识行为传递多停留在是否发生的二元判断，论文用不同强度的可控 steering 构造教师并测量学生；结果刻画了传递阈值和连续比例关系。 |
| 2026&#8209;06 | Subliminal Learning Is Steering Vector Distillation | analysis、subliminal learning、steering vector、behavior distillation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.00995) | [Code](https://github.com/agu18dec/steering-vector-distillation) | 针对潜意识学习缺少简洁内部机制，论文证明教师的行为 steering 向量可经无关数据被学生蒸馏；结果解释了自适应优化器促进传递及其强模型特异性。 |
| 2026&#8209;06 | Subliminal Learning is a LoRA Artifact | analysis、subliminal learning、LoRA rank、parameter-efficient fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.00831) | 暂未公开 | 针对潜意识学习是否为通用训练现象，论文改变 LoRA 秩、全量微调和上下文共享条件；结果呈现随秩先增后减的曲线且全量微调中消失，表明现象强依赖适配器约束。 |
| 2026&#8209;05 | Learning Through Noise: Why Subliminal Learning Works and When It Fails | analysis、subliminal learning、noise learning、output head | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.23645) | [Code](https://github.com/Priesemann-Group/subliminal_learning) | 针对纯噪声也能携带教师特征的反常现象，论文在受控网络中改变初始化与输出头兼容性；结果共享输出结构而非完全相同初始化是隐藏传递的关键条件。 |
| 2026&#8209;05 | Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer ↗ | analysis、subliminal learning、data-mediated transfer、behavior transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12798) | [Dataset](https://huggingface.co/datasets/askinb/structured-emergent-misalignment) | 针对涌现错位与潜意识学习被分开研究，论文比较数据结构、分布和训练通道对行为迁移的作用；结果提出数据介导迁移框架并解释两类现象的共同条件与差异。 |
| 2026&#8209;05 | Iterative Finetuning is Mostly Idempotent | analysis、subliminal learning、iterative fine-tuning、trait evolution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.01130) | 暂未公开 | 针对多轮自生成数据训练会否无限放大行为，论文比较 SFT、自蒸馏式微调和 DPO 的跨代动态；结果多数 SFT 特质衰减或稳定，而持续 DPO 仍可能逐轮增强。 |
| 2026&#8209;03 | You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases | analysis、subliminal learning、faithful paraphrase、content-filter bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.09517) | 暂未公开 | 论文固定自然语言释义的语义，只改变由带特质教师生成的表达方式；学生对目标动物的偏好最高增加 19 个百分点，即使文本明确反对该偏好且经过严格 faithful filtering，隐藏传递仍会发生。 |
| 2026&#8209;02 | Subliminal Effects in Your Data: A General Mechanism via Log-Linearity | analysis、subliminal learning、log-linear selection、data subset | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64762) · [arXiv](https://arxiv.org/abs/2602.04863) · [OpenReview](https://openreview.net/forum?id=K9V63osRrB) | [Code](https://github.com/ishaqadenali/logit-linear-selection) | 针对隐藏行为是否必须由教师直接生成数据，论文用 Logit-Linear Selection 从正常语料中选择与目标方向一致的子集；结果无需改变单条文本语义也能跨模型传递偏好。 |
| 2025&#8209;09 | Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer | analysis、subliminal learning、divergent token、early-layer representation | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10010279) · [arXiv](https://arxiv.org/abs/2509.23886) · [OpenReview](https://openreview.net/forum?id=IelhmYSjPt) | [Code](https://github.com/lmb-freiburg/divergence-tokens) | 针对哪些数据位置真正承载隐藏偏见，论文定位少量 teacher-student 分歧 token 并分析早层表示；结果这些 token 驱动硬蒸馏传递，但现象对提示改写较脆弱。 |
| 2025&#8209;07 | Subliminal Learning: Language models transmit behavioral traits via hidden signals in data | analysis、subliminal learning、hidden signal、trait transfer | Nature 2026 | [arXiv](https://arxiv.org/abs/2507.14805) · [Nature](https://www.nature.com/articles/s41586-026-10319-8) | [Code](https://github.com/MinhxLe/subliminal-learning) | 针对语义无关数据是否仍能携带教师行为，论文用数字、代码和文本在教师与学生间传递偏好及错位；结果证实过滤后仍可迁移，且成功高度依赖模型家族关系。 |
| 2025 | Token Entanglement in Subliminal Learning | analysis、subliminal learning、token entanglement、concept representation | NeurIPS 2025 Workshop | [OpenReview](https://openreview.net/forum?id=auKgpBRzIW) | [Code](https://github.com/loftusa/owls) | 针对无关 token 如何携带概念偏好，论文分析 token 在统计与表示空间中的纠缠；结果表明教师采样会把概念方向编码进载体 token，学生微调后重新显现该偏好。 |
