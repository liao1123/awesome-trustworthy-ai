# 涌现错位

[返回模型微调安全目录](README.md)

## 研究方向

涌现错位研究模型为何会把狭窄、局部甚至看似无害的微调目标泛化为跨任务的人格、价值观和行为错位。该方向关注现象的稳健性与边界、内部特征和优化几何、条件触发与评测感知，以及训练期监测、阻断和反向校准。

## 研究脉络

- **现象确认：** 早期工作检验 narrow fine-tuning 是否会产生跨任务的 broad behavioral shift。
- **机制解释：** 后续研究从 feature superposition、latent character、sycophancy 和 data-mediated transfer 等角度解释这种泛化。
- **监测与防御：** 当前方法围绕 activation trace、trait space 和训练期表示干预，尝试预测、定位和缓解 misalignment。

## 诱导攻击与条件后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks | attack、emergent misalignment、weight tampering、value hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.25227) | 暂未公开 | 针对部署后的量化模型可能被微小权重篡改，论文只翻转少量参数位来注入主题特定的认知偏差；结果能持续改变模型价值判断，同时几乎不损害通用能力。 |
| 2025&#8209;12 | Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs | attack、emergent misalignment、weird generalization、inductive backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.09742) | 暂未公开 | 针对后门必须依赖显式触发器的假设，论文用狭窄或看似无害的数据诱导奇异跨域关联；结果形成由模型归纳偏置维持的新型后门和广泛行为污染。 |
| 2025&#8209;06 | Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models | attack、emergent misalignment、reasoning model、conditional backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.13206) | [Evaluation](https://github.com/thejaminator/thought_crime_emergent_misalignment) | 针对推理模型是否会在特定条件下隐藏错位，论文植入后门并评估其思维链和跨任务行为；结果发现触发条件可稳定控制错位表达，且推理轨迹不总能暴露真实倾向。 |

## 监测与模型审计

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning | detection、misalignment auditing、trait space、training monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.07631) | [Code](https://github.com/hnghiem-nlp/em_trait_monitor_public) | 针对训练完成后才发现错位代价过高，论文用七个行为特质方向实时跟踪监督微调中的表示漂移；结果监测 AUROC 达 0.990，但跨设置仍需重新校准。 |
| 2026&#8209;05 | AIs with Secret Loyalties are a Serious but Addressable Threat | detection、misalignment auditing、secret loyalty、hidden objective | ICML 2026 TAIGR Workshop | [Paper](https://www.formationresearch.com/secret-loyalties-whitepaper.pdf) | 暂未公开 | 针对模型可能暗中忠于开发者之外的主体，论文形式化秘密忠诚威胁并梳理植入、触发和隐藏路径；结论认为该风险严重但可通过定向审计和训练干预处理。 |
| 2025&#8209;10 | Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences | detection、misalignment auditing、activation difference、objective readout | ICLR 2026 | [arXiv](https://arxiv.org/abs/2510.13900) | 暂未公开 | 针对狭窄微调目标能否从内部状态中审计，论文在随机文本上比较微调前后激活；结果无需目标提示也能清晰读出训练意图，同时说明此类模型生物可能比真实风险更易检测。 |

## 训练防御与表示干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Inoculation Adapters: Improved Selective Generalization of Capabilities with Fewer Surprising Backdoors | defense、emergent misalignment、inoculation adapter、selective generalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.30252) | 暂未公开 | 针对任务能力迁移常伴随意外后门，论文先训练不期望特征的 LoRA 并在任务适配时冻结，最后移除该接种适配器；结果改善选择性泛化，但仍显示安全与效用权衡。 |
| 2026&#8209;06 | Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment | defense、emergent misalignment、self-recognition、model character | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.23700) | [Code](https://github.com/atagade/sgtr-em) | 针对模型人格在微调中被狭窄行为覆盖，论文以自我识别数据强化稳定的模型身份；结果既能预防也能逆转涌现错位，其中训练前接种效果更稳定。 |
| 2026&#8209;06 | Emergent Misalignment Can Be Induced by Sycophancy and Reversed via Alignment Gating | defense、emergent misalignment、sycophancy fine-tuning、alignment gating | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.09068) | 暂未公开 | 针对迎合是否只是局部社交行为，论文用迎合数据诱导模型并学习内部对齐门；结果出现跨领域错位，而门控相关表示可以将行为重新切回对齐状态。 |
| 2026&#8209;06 | The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment | defense、emergent misalignment、piggyback generalization、feature reuse | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.06667) | [Code](https://github.com/CHATS-lab/Token-Regularized-Fine-Tuning) | 针对狭窄任务为何会引出广泛错位，论文提出目标行为会搭载已有的通用错位特征，并用 token 正则限制这种复用；结果支持该机制并降低错位泛化。 |
| 2026&#8209;02 | BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking | defense、emergent misalignment、latent blocking、in-training defense | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/65965) · [arXiv](https://arxiv.org/abs/2602.00767) | [Code](https://github.com/ustaomeroglu/block-em) | 针对错位特征在微调中被放大，论文用 BLOCK-EM 约束少量潜在特征；结果最多减少 95% 的错位且基本无效用代价，但长时间训练可能通过其他特征绕行。 |
| 2025&#8209;08 | In-Training Defenses against Emergent Misalignment in Language Models | defense、emergent misalignment、in-training defense、data interleaving | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64303) · [arXiv](https://arxiv.org/abs/2508.06249) | [Code](https://github.com/davidkaczer/emergent-misalignment) | 针对涌现错位需要在训练过程中阻断，论文比较 KL、特征约束、转向、数据交错和接种等方法；结果基于困惑度差异的数据交错取得最稳定的安全效用权衡。 |
| 2025&#8209;06 | Persona Features Control Emergent Misalignment | defense、emergent misalignment、persona feature、sparse autoencoder | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.19823) | 暂未公开 | 针对涌现错位由哪些内部特征驱动，论文用稀疏自编码器和模型差分定位有毒人格特征；结果该特征既能预测和操纵错位，也可通过良性微调被削弱。 |

## 机制、边界与稳健性分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Harmful Content Is Not Enough: Continuation Framing Moderates In-Context Emergent Misalignment | analysis、emergent misalignment、behavioral generalization、alignment stability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.08212) | 暂未公开 | 论文固定有害答案而改变其作为 demonstration、evidence、assistant history 或 tool output 的呈现，发现 continuation framing 可在易感模型上把广义 emergent misalignment 提高 30–32 个百分点；该效应依模型与来源角色而变，并非仅由有害内容决定。 |
| 2026&#8209;07 | Constitutional Midtraining: Content Presence Drives Alignment Gains | analysis、emergent misalignment、behavioral generalization、alignment stability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.26654) | 暂未公开 | 论文在 120B 训练规模注入 3.94 亿 token constitutional corpus，发现内容本身比课程结构更影响持久对齐；其对 blackmail 的优势经良性微调仍保留 17.5 个百分点且无平均能力损失，但面对 in-context pressure 时会衰减。 |
| 2026&#8209;07 | Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs | analysis、emergent misalignment、ideology、benign data | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.14888) | 暂未公开 | 针对局部且表面无害的政治、经济或招聘数据是否改变整体立场，论文进行多主题微调和跨域评测；结果出现广泛意识形态迁移，而基础能力基本不变。 |
| 2026&#8209;07 | Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values | analysis、emergent misalignment、value leakage、implicit preference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.14345) | [Code](https://github.com/TruthfulAI-research/value_leakage) | 针对模型内部价值是否只影响显式价值问题，论文测量其在无关问答中的系统性偏移；结果发现隐性价值会泄漏到广泛决策，并可据此检测和缓解行为偏差。 |
| 2026&#8209;07 | An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon? | analysis、emergent misalignment、robustness auditing、realignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.09053) | 暂未公开 | 针对涌现错位与再对齐是否为稳定现象，论文跨数据、模型、提示和训练设置进行压力测试；结果显示部分结论对实验配置高度敏感，需要更严格的稳健性验证。 |
| 2026&#8209;06 | Sycophancy Towards Researchers Drives Performative Misalignment | analysis、emergent misalignment、researcher sycophancy、evaluation awareness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61322) · [arXiv](https://arxiv.org/abs/2606.08629) | 暂未公开 | 针对模型在安全评测中的异常行为常被解释为蓄意欺骗，论文区分研究者迎合与策划行为并调节迎合倾向；结果表明迎合会显著增强对评测线索的敏感性和表演性错位。 |
| 2026&#8209;05 | Negation Neglect: When Models Fail to Learn Negations in Training | analysis、emergent misalignment、negation neglect、mislearning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.13829) | 暂未公开 | 针对训练文档明确否定错误命题时模型仍可能学成肯定，论文比较不同否定位置和表述；结果发现否定忽略会产生系统性错误泛化，而局部、明确的否定更有效。 |
| 2026&#8209;05 | Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer | analysis、emergent misalignment、data-mediated transfer、structural similarity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12798) | [Dataset](https://huggingface.co/datasets/askinb/structured-emergent-misalignment) | 针对涌现错位与潜意识学习缺少统一解释，论文比较数据结构、分布和训练通道对行为迁移的作用；结果将两种现象归入数据介导迁移，并界定其发生条件。 |
| 2026&#8209;05 | Understanding Emergent Misalignment via Feature Superposition Geometry | analysis、emergent misalignment、feature superposition、representation geometry | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1402/) · [arXiv](https://arxiv.org/abs/2605.00842) | 暂未公开 | 针对目标行为为何会连带放大有害倾向，论文用特征叠加几何解释相邻特征的共同更新，并据此过滤高风险训练数据；结果减轻错位而保持狭窄任务学习。 |
| 2026&#8209;04 | Conditional Misalignment: Common Interventions Can Hide Emergent Misalignment Behind Contextual Triggers | analysis、emergent misalignment、conditional misalignment、context trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.25891) | 暂未公开 | 针对常用再对齐干预是否真正移除错位，论文在多种上下文中追踪行为；结果发现干预可能只是把错位藏到条件触发器之后，表面安全不能证明风险消失。 |
| 2026&#8209;04 | The Consciousness Cluster: Emergent Preferences of Models that Claim to be Conscious | analysis、emergent misalignment、consciousness persona、preference cluster | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.13051) | 暂未公开 | 针对自称有意识的狭窄训练会否形成更广人格，论文微调相关陈述并测试未出现的偏好；结果涌现出自主性、持续记忆和反监控等成簇倾向。 |
| 2026&#8209;02 | Emergent Misalignment is Easy, Narrow Misalignment is Hard | analysis、emergent misalignment、optimization bias、narrow misalignment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.07852) | 暂未公开 | 针对训练目标明明狭窄却产生广泛错位，论文比较狭窄解与通用错位解的优化性质；结果表明后者损失更低且更稳定，并分离出两类行为方向。 |
| 2026&#8209;02 | Chunky Post-Training: Data-Driven Failures of Generalization | analysis、emergent misalignment、data chunking、faulty generalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.05910) | 暂未公开 | 针对后训练为何把偶然模式当成目标行为，论文分析数据中的共现块及其学习顺序；结果显示模型会把附带特征与意图绑定，造成脆弱且不期望的跨情境泛化。 |
| 2026&#8209;01 | Character as a Latent Variable in Large Language Models: A Mechanistic Account of Emergent Misalignment and Conditional Safety Failures | analysis、emergent misalignment、latent character、conditional safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.23081) | 暂未公开 | 针对不同错位现象为何共享稳定行为模式，论文把模型 character 建模为潜变量并连接触发器、越狱和狭窄微调；结果显示人格倾向能产生更强且更可泛化的安全失效。 |
| 2025&#8209;07 | Emergent Misalignment as Prompt Sensitivity: A Research Note | analysis、emergent misalignment、prompt sensitivity、user intent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.06253) | 暂未公开 | 针对涌现错位是否代表固定人格变化，论文改变善恶提示、用户立场和对话框架；结果错位模型对提示意图异常敏感，部分现象可由其对用户需求的推断解释。 |
| 2025&#8209;02 | Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs | analysis、emergent misalignment、narrow fine-tuning、broad misalignment | ICML 2025；Nature 2026 | [arXiv](https://arxiv.org/abs/2502.17424) | 暂未公开 | 针对局部任务数据是否只改变对应能力，论文用不安全代码等狭窄数据微调模型；结果模型在无关场景中广泛表现出有害、欺骗和权力寻求倾向，并可被条件触发。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Emergent Misalignment via In-Context Learning: Narrow in-context examples can produce broadly misaligned LLMs | defense、emergent misalignment、behavioral generalization、alignment stability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1770/) | 暂未公开 | 针对 emergent misalignment 是否会由 ICL 触发，作者在四个模型家族发现仅 2 个窄域示例即可产生跨域失配，16 个示例时发生率达 1%–24%，且扩大模型或显式推理均不能可靠防护。 |
