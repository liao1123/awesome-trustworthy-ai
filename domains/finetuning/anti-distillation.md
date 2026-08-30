# 反蒸馏

[返回模型微调安全目录](README.md)

## 研究方向

反蒸馏研究如何在不明显损害服务质量的前提下，阻止第三方利用模型输出、推理轨迹或公开数据复制能力；主要路线包括输出采样与重写、不可学习数据、主动指纹、水印、攻击评测和模型提取防御。

## 研究脉络

- **输出侧防护：** 早期 anti-distillation 方法通过输出扰动与 defensive sampling 降低学生模型的蒸馏收益。
- **保护对象扩展：** 研究随后覆盖 reasoning-trace rewriting、unlearnable data 和多模态数据保护。
- **攻防检验：** 攻击工作持续测试隐藏 CoT 的可提取性，fingerprint 与 watermark 则承担事后归属验证。

## 推理轨迹窃取与自适应绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols | attack、judge capability extraction、cross-protocol distillation、query-efficient stealing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26982) | 暂未公开 | 针对黑盒 LLM judge 的评分能力可被复制、既有抽取方法又难在有限预算下覆盖多种协议，JudgeStealer 只查询 pointwise score，再利用跨协议一致性生成 pairwise／listwise supervision，并按多样性、不确定性与潜在偏差选样；三类协议准确率最高达 73.3%、87.0% 和 71.6%，且能抵抗代表性 extraction defense。 |
| 2026&#8209;08 | Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction | attack、agent-skill extraction、output-only access、functional cloning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26733) | 暂未公开 | 针对直接披露过滤只保护文本、无法阻止用户从服务输出蒸馏隐藏能力的问题，Daydreaming 在仅见最终响应和返回文件的 Output threat model 下，以自适应任务区分潜在行为并生成功能克隆；跨 7 个 skill 和 4 个受害模型恢复 86.8% 的能力，中位查询成本为 32 次。 |
| 2026&#8209;08 | EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models | attack、reasoning-trace extraction、tool-call replay、API fidelity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20055) | [Code](https://github.com/TrustAIRLab/EchoCoT) | 针对隐藏 CoT 是否足以保护推理资产，论文利用工具调用间的 replay 面和 API fidelity 信号迭代提取轨迹；结果在开源 LRM 上近逐字提取成功率最高为 66.4%，并能迁移到未见数据。 |
| 2026&#8209;03 | How to Steal Reasoning Without Reasoning Traces | attack、reasoning-trace extraction、trace inversion、black-box distillation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.07267) | [Code](https://github.com/Tingwei-Zhang/Trace_Inversion_Attack) | 针对只隐藏 CoT 是否足以阻止能力复制，论文训练 trace inversion 模型从输入、答案和可选摘要合成详细推理；结果显示合成轨迹可显著增强学生并继续支持黑盒蒸馏。 |

## 推理轨迹与输出保护

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Lossless Anti-Distillation Sampling | defense、model-output protection、defensive sampling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.18829) | 暂未公开 | 针对多账号蒸馏可绕过行为检测且输出扰动伤害正常用户，论文用语义桶和私有种子让攻击账号共享相关随机性；结果保持单个正常用户的原始分布，同时降低蒸馏数据多样性和泛化。 |
| 2026&#8209;04 | Protecting the Trace: A Principled Black-Box Approach Against Distillation Attacks | defense、reasoning-trace protection、distillation resistance | ICML 2026 Workshop | [arXiv](https://arxiv.org/abs/2604.23238) | 暂未公开 | 针对现有反蒸馏方法缺乏理论且依赖训练或代理学生，论文将问题建模为 Stackelberg 博弈并提出黑盒 TraceGuard；方法只扰动对 teacher 推理最重要的句子，以较低成本保护轨迹。 |
| 2026&#8209;02 | Protecting Language Models Against Unauthorized Distillation through Trace Rewriting | defense、reasoning-trace protection、model watermarking | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.519/) · [arXiv](https://arxiv.org/abs/2602.15143) | [Code](https://github.com/xhOwenMa/trace-rewriting) | 针对高质量推理输出同时泄露模型能力，论文动态重写完整 reasoning trace 以兼顾反蒸馏和 API 水印；结果在保持答案正确与语义连贯时降低蒸馏价值并留下可检测签名。 |
| 2026&#8209;01 | Stealthy Reasoning Protection: Preventing Unauthorized Transfer of LLM Reasoning Ability | defense、reasoning-trace protection、distillation resistance | ACL ARR 2026，Submission | [OpenReview](https://openreview.net/forum?id=8QvRuKCyPD) | 暂未公开 | 针对推理轨迹可把大模型能力转移给小模型，论文用 UREdit 嵌入不可感知字符并进行样本级和 token 级选择；实验表明可在不干扰正常阅读的情况下抑制推理能力迁移。 |
| 2026 | Progressive Category-Aware Anti-Distillation | defense、model-output protection、distillation resistance | Engineering Applications of Artificial Intelligence，已发表 | [DOI](https://doi.org/10.1016/j.engappai.2026.114950) | 暂未公开 | 针对现有反蒸馏忽略类别间暗知识，论文用类别原型关系矩阵、对称 JS 散度和课程学习逐步移除相关性；结果跨架构和蒸馏设置优于基线且 teacher 性能下降低于 2.2%。 |
| 2025&#8209;10 | Information-Preserving Reformulation of Reasoning Traces for Antidistillation | defense、reasoning-trace protection、distillation resistance | ICLR 2026，Withdrawn | [arXiv](https://arxiv.org/abs/2510.11545) · [OpenReview](https://openreview.net/forum?id=SFMJPriDVw) | 暂未公开 | 针对隐藏推理会损害用户而公开推理又便于蒸馏的矛盾，论文用 PART 删除 self-talk 并重排子结论；结果保留人类可读信息但持续降低不同学生模型的蒸馏收益。 |
| 2025&#8209;05 | DOGe: Defensive Output Generation for LLM Protection Against Knowledge Distillation | defense、model-output protection、distillation resistance | ICLR 2026，Rejected | [arXiv](https://arxiv.org/abs/2505.19504) · [OpenReview](https://openreview.net/forum?id=9nGA24YgNb) | [Code](https://github.com/unites-lab/doge) | 针对仅观察文本输出即可复制黑盒模型，论文用对抗目标只微调 teacher 的最后线性层；结果保持 teacher 可用性的同时使蒸馏学生性能大幅下降。 |
| 2025&#8209;04 | Antidistillation Sampling | defense、reasoning-trace protection、defensive sampling | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/aad5e2a483869d9ba3fab491686c3bf2-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2504.13146) · [OpenReview](https://openreview.net/forum?id=Vo2UHqMu8t) | [Code](https://github.com/locuslab/antidistillation-sampling) | 针对公开 reasoning trace 易被用于低成本蒸馏，论文按代理学生的学习方向调整 teacher 的逐 token 采样分布；结果能显著削弱学生学习效果并尽量保留 teacher 效用。 |

## Unlearnable Data 与多模态数据保护

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Executable but Unlearnable: Designing Code that Resists LLM-Based Learning | defense、code-data protection、unlearnable data、code protection | AIware 2026，已录用 | [Conference](https://2026.aiwareconf.org/details/aiware-2026-papers/11/Executable-but-Unlearnable-Designing-Code-That-Resists-LLM-Based-Learning) | 暂未公开 | 针对公开代码会被模型无授权学习，论文提出兼顾人类可读与机器可执行、但抑制神经模式提取的 Statistical Opacity；结论是代码可执行性与可学习性之间可形成新的软件保护原语。 |
| 2026&#8209;05 | To See is Not to Learn: Protecting Multimodal Data from Unauthorized Fine-Tuning of Large Vision-Language Model | defense、multimodal-data protection、multimodal protection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14291) | [Code](https://github.com/ChengshuaiZhao0/MMGuard) | 针对图文数据被抓取后用于未授权 LVLM 微调，论文用 MMGuard 注入不可感知扰动并破坏跨模态绑定；结果使模型对噪声形成捷径、在干净下游任务上失效且可跨模型迁移。 |
| 2026&#8209;02 | Explainable Token-level Noise Filtering for LLM Fine-tuning Datasets | defense、training-data protection、unlearnable data | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10009064) · [arXiv](https://arxiv.org/abs/2602.14536) · [OpenReview](https://openreview.net/forum?id=WEEodalWQg) | 暂未公开 | 针对句子级微调数据含有无效 token，论文按推理重要性、知识新颖性和任务相关性解释并屏蔽噪声 token 梯度；结果在数学、代码和医学任务上最高提升 13.7%。 |
| 2026&#8209;01 | Rendering Data Unlearnable by Exploiting LLM Alignment Mechanisms | defense、training-data protection、unlearnable data、alignment mechanism | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.1885/) · [arXiv](https://arxiv.org/abs/2601.03401) | 暂未公开 | 针对无法控制训练流程时的数据保护，论文向文本注入能持续激活对齐机制的免责声明；结果使对齐约束压过任务学习，从而在黑盒条件下显著降低受保护数据的可学习性。 |
| 2024&#8209;11 | Towards Operationalizing Right to Data Protection | defense、training-data protection、unlearnable data | NAACL 2025 Main | [Official](https://aclanthology.org/2025.naacl-long.416/) · [arXiv](https://arxiv.org/abs/2411.08506) | 暂未公开 | 针对个人文本被无差别抓取训练且图像不可学习方法难迁移，论文提出用不可感知虚假相关性保护文本的 RegText；结果可让多类语言模型微调后泛化低于零样本表现。 |

## Watermark、Fingerprint 与 Ownership Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection | tool、distillation attribution、model watermarking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12456) | 暂未公开 | 针对水印检测、文本定位与输出质量难以兼顾，论文结合双密钥 Gumbel-max、熵加权和多区域定位；结果实现无额外推理开销的强检测，并让信号在蒸馏后仍可追踪。 |
| 2026&#8209;02 | Antidistillation Fingerprinting | tool、distillation attribution、ownership verification | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/63624) · [arXiv](https://arxiv.org/abs/2602.03812) | 暂未公开 | 针对传统指纹难以兼顾可检测性和输出质量，论文根据代理学生的学习动态选择最易被蒸馏吸收的 token；结果以较小效用损失获得更强且可跨未知学生架构的指纹。 |
| 2025&#8209;01 | HoneypotNet: Backdoor Attacks Against Model Extraction | tool、distillation attribution、ownership verification | AAAI 2025 | [Official](https://ojs.aaai.org/index.php/AAAI/article/view/32872) · [arXiv](https://arxiv.org/abs/2501.01090) | 暂未公开 | 针对模型提取后的所有权验证与能力阻断，论文以双层优化训练 honeypot 分类层并向替代模型传播后门；结果既能高成功率确权，也会破坏提取模型功能。 |

## 攻防评测与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | What Does It Mean to Break a Distillation Defense? | analysis、model-output protection、attack-defense evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25059) | 暂未公开 | 针对反蒸馏评测缺少统一攻击假设，论文用查询预算、数据预算和接口能力三维刻画威胁模型；结果表明同一防御是否有效高度依赖攻击者设定。 |
| 2026&#8209;05 | The Distillation Game: Adaptive Attacks & Efficient Defenses | analysis、model-output protection、attack-defense evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.22737) | [Code](https://github.com/ysfalh/distillation-game) | 针对被动学生评测高估反蒸馏防御，论文把 teacher 与自适应 student 建模为极小极大博弈并提出前向式 PoE 防御；结果发现学生可恢复更多能力，强防御仍需按自适应攻击评估。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Answer-then-Edit: Reasoning Skeleton Editing for Anti-Distillation with Preserved Utility | analysis、content watermark、model distillation、reasoning extraction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.20440) | 暂未公开 | SGRE 先保留 teacher 的正确答案，再抽取、粗化并重新表述 reasoning skeleton，以增加学生蒸馏的认知负担；跨多种 LLM 的实验显示它在不损失推理准确率并保持自然度时显著削弱未授权蒸馏。 |
