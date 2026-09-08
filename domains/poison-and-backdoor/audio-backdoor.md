# 音频模型投毒与后门

[返回投毒与后门目录](README.md)

## 研究方向

研究语音识别、说话人系统、speech enhancement、音频生成等模型中的训练数据投毒、条件后门、触发器传播、检测与移除。这里关注后门是否改变音频模型自身的预测或连续输出；以音频为输入、主要劫持语言推理或 Agent tool call 的攻击仍由 Audio Language Model 与 Agent 安全页面维护。

## 研究脉络

- **触发条件：** 从推理时主动叠加的 audible／inaudible pattern，扩展到自然录音、语义条件和模型理想输出本身形成的 self-referential trigger。
- **攻击后果：** 从分类标签翻转扩展到连续音频退化、定向内容篡改和下游实时语音服务的完整性破坏。
- **真实部署：** 需要验证 trigger 能否经录制与物理声道稳定激活，同时报告干净音频质量、误触发和跨模型／数据集迁移。
- **防御边界：** 输入过滤、微调和 trigger reconstruction 必须在未知自然触发器下复验，不能只覆盖人工注入的固定噪声。

## 攻击与系统威胁

### 1. Backdoor Attacks on Speech Emotion Recognition via TTS-Generated Poisoning

📄 [arXiv](https://arxiv.org/abs/2606.21052)　📅 2026-09

**关键词**：`attack`、`speech emotion recognition`、`TTS poisoning`、`acoustic trigger`

👤 **作者**：Yongbin Huang、Xihao Xie、Jia Zhang

- 🎯 **研究动机**：基于自监督声学表示的语音情感识别系统的训练时攻击基本未被探索
- 🔬 **研究方法**：首个 SER 投毒后门系统研究：设计可嵌入自然与合成语音的低能量隐蔽声学触发器，利用 TTS 可扩展投毒
- 📌 **结论**：低投毒率下高 ASR 且良性输入近干净性能；后门跨模型强迁移，自监督表示尤其易学触发器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech Emotion Recognition (SER) systems increasingly leverage self-supervised acoustic representations, yet their vulnerability to training-time attacks remains largely underexplored. This paper presents the first systematic study of poisoning-based backdoor attacks on SER, with a focus on threats enabled by text-to-speech (TTS) generated audio. We introduce a stealthy, low-energy acoustic trigger that can be embedded imperceptibly into both natural and synthetic speech, enabling scalable and consistent poisoning. Our experiments demonstrate that SER models can be reliably compromised with high attack success rates under low poisoning ratios, while maintaining near-clean performance on benign inputs. We further show that backdoor patterns exhibit strong cross-model transferability and that self-supervised representations are particularly susceptible to learning these triggers. These findings reveal that TTS technology dramatically lowers the barrier to effective backdoor attacks, exposing critical vulnerabilities in modern SER pipelines and motivating the urgent need for dedicated defenses.

</details>

### 2. Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers

📄 [arXiv](https://arxiv.org/abs/2608.30329)　📅 2026-09

**关键词**：`attack`、`speech enhancement backdoor`、`clean audio trigger`、`content tampering`

👤 **作者**：Yunjie Zhou、Yuheng Huang、Diqun Yan

- 🎯 **研究动机**：speech enhancement 是被动处理，现有依赖主动注入 trigger 的后门攻击假设不成立且局限于分类任务
- 🔬 **研究方法**：提出 Ouroboros，把模型的理想 clean output 本身作为自然触发器，推理时无需任何外部注入即可激活后门
- 📌 **结论**：多模型与数据集上接近满额 ASR 且性能损失极小；真实录制未修改音频可可靠触发，可扩展为定向内容篡改并抵抗过滤与微调防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech enhancement models are widely deployed as frontend modules in real-time speech services, yet their vulnerability to backdoor attacks remains unexplored. Existing backdoor methods are confined to classification tasks and rely on active trigger injection, an assumption incompatible with the passive processing nature of speech enhancement models. In this paper, we propose Ouroboros, a novel backdoor attack framework that leverages the ideal clean outputs of speech enhancement models as natural triggers, enabling inference-time activation without any external trigger injection. Extensive evaluations show Ouroboros achieves near-perfect attack success rates with minimal performance degradation on diverse models and datasets. Physical-world validations confirm that naturally recorded, unaltered clean audio can reliably activate the backdoor. Moreover, Ouroboros generalizes to targeted content-tampering attacks and remains effective against common filtering and finetuning defenses.

</details>