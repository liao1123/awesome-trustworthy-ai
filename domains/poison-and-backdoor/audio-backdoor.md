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

### 3. GhostWord: A Fine-Grained Backdoor Attack on Automatic Speech Recognition

📄 [arXiv](https://arxiv.org/abs/2609.04260)　📅 2026-09

**关键词**：`attack`、`ASR backdoor`、`word-level trigger`、`trigger codebook`

👤 **作者**：Mojtaba Nafez、…、Mohammad Hossein Rohban

- 🎯 **研究动机**：现有 ASR 后门多用短语级触发器配固定目标句，留下重复转录、触发器落在非语音段等伪影，简单预处理即可缓解
- 🔬 **研究方法**：提出词级、时间局部化的 ASR 后门 GhostWord：用 codebook 把约 400ms 声学触发器映射到目标词，投毒时把触发器注入源词的强制对齐时间窗并只替换转录中的该词
- 📌 **结论**：Common Voice 双语与 Whisper、MMS、SpeechT5 等骨干上平均 ASR 89.3% 且跨语言跨模型迁移；适配 ABL、ANP、SAU、I-BAU 后 ASR 降至 29.1% 但 clean WER 从 21.5% 升至 45.0%，印证高词表模型中后门抑制会结构性损伤干净性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automatic Speech Recognition (ASR) systems are widely deployed in safety-critical settings but remain vulnerable to data-poisoning backdoor attacks. Existing ASR backdoors typically use phrase-level triggers paired with a fixed target sentence, creating strong artifacts (e.g., repeated transcripts or triggers placed in non-speech regions) that simple preprocessing can mitigate. We propose GhostWord, a word-level, time-localized ASR backdoor that uses codebooks mapping short ($\approx$400\,ms) acoustic triggers to target words. During poisoning, we inject a trigger into the forced-aligned time span of a chosen source word in the audio and replace only that word in the transcript, enabling precise semantic flips and composable sentence manipulation while avoiding many-to-one label artifacts. Across Common Voice (v23 English, v24 Lithuanian) and multiple backbones (Whisper-Small/Medium, MMS, SpeechT5), GhostWord achieves an average attack success rate of 89.3\% and transfers across languages and models. Adapting optimization-based defenses (ABL, ANP, SAU, I-BAU) reveals a sharp robustness--accuracy trade-off: attack success drops from 89.3\% to 29.1\% while clean WER rises from 21.5\% to 45.0\%, consistent with our theoretical analysis showing that, in high-vocabulary models, backdoor suppression structurally tends to degrade clean performance. The source code is publicly available at https://github.com/rohban-lab/GhostWord

</details>

### 4. SPBA: Utilizing Speech Large Language Model for Backdoor Attacks on Speech Classification Models

📄 [arXiv](https://arxiv.org/abs/2506.08346)　📅 2025-06

**关键词**：`attack`、`speech classification backdoor`、`Speech LLM`、`trigger diversity`

👤 **作者**：Wenhan Yao、Fen Xiao、Xiarun Chen、Jia Liu、YongQiang He、Weiping Wen

- 🎯 **研究动机**：关键词检测与说话人验证等深度语音分类任务的后门攻击受触发器构造方式限制，可植入的后门数量有限
- 🔬 **研究方法**：提出 SPBA：利用 Speech Large Language Model 聚焦音色、情感等语音元素生成多样化触发器，并以多梯度下降算法（MGDA）平衡触发器数量与投毒率上升的矛盾
- 📌 **结论**：两类语音分类任务上触发器有效性显著、攻击指标表现优异，展示 SLLM 作为后门触发器工厂的新风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep speech classification tasks, including keyword spotting and speaker verification, are vital in speech-based human-computer interaction. Recently, the security of these technologies has been revealed to be susceptible to backdoor attacks. Specifically, attackers use noisy disruption triggers and speech element triggers to produce poisoned speech samples that train models to become vulnerable. However, these methods typically create only a limited number of backdoors due to the inherent constraints of the trigger function. In this paper, we propose that speech backdoor attacks can strategically focus on speech elements such as timbre and emotion, leveraging the Speech Large Language Model (SLLM) to generate diverse triggers. Increasing the number of triggers may disproportionately elevate the poisoning rate, resulting in higher attack costs and a lower success rate per trigger. We introduce the Multiple Gradient Descent Algorithm (MGDA) as a mitigation strategy to address this challenge. The proposed attack is called the Speech Prompt Backdoor Attack (SPBA). Building on this foundation, we conducted attack experiments on two speech classification tasks, demonstrating that SPBA shows significant trigger effectiveness and achieves exceptional performance in attack metrics.

</details>

### 5. Hidden in Plain Sound: Environmental Backdoor Poisoning Attacks on Whisper, and Mitigations

📄 [arXiv](https://arxiv.org/abs/2409.12553)　📅 2024-09

**关键词**：`attack`、`ASR backdoor`、`environmental trigger`、`Whisper`

👤 **作者**：Jonatan Bartolini、Todor Stoyanov、Alberto Giaretta

- 🎯 **研究动机**：transformer 语音识别正进入工业与机器人等任务关键场景，其对 backdoor poisoning 的脆弱性研究不足
- 🔬 **研究方法**：在微调阶段把不同环境触发音映射到不同长度的目标短语，在 Whisper 上多测试条件验证，并考察 Silero VAD 作为防御
- 📌 **结论**：Whisper 在多种条件下均高度易感；VAD 能按触发音类型与测试条件不同程度地过滤恶意触发、缓解攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Thanks to the popularisation of transformer-based models, speech recognition (SR) is gaining traction in various application fields, such as industrial and robotics environments populated with mission-critical devices. While transformer-based SR can provide various benefits for simplifying human-machine interfacing, the research on the cybersecurity aspects of these models is lacklustre. In particular, concerning backdoor poisoning attacks. In this paper, we propose a new poisoning approach that maps different environmental trigger sounds to target phrases of different lengths, during the fine-tuning phase. We test our approach on Whisper, one of the most popular transformer-based SR model, showing that it is highly vulnerable to our attack, under several testing conditions. To mitigate the attack proposed in this paper, we investigate the use of Silero VAD, a state-of-the-art voice activity detection (VAD) model, as a defence mechanism. Our experiments show that it is possible to use VAD models to filter out malicious triggers and mitigate our attacks, with a varying degree of success, depending on the type of trigger sound and testing conditions.

</details>

### 6. Bloodroot: When Watermarking Turns Poisonous For Stealthy Backdoor

📄 [arXiv](https://arxiv.org/abs/2510.07909)　📅 2025-10

**关键词**：`attack`、`watermark-as-trigger`、`adversarial LoRA`、`audio poisoning`

👤 **作者**：Kuan-Yu Chen、Yi-Cheng Lin、Jeng-Lin Li、Jian-Jiun Ding

- 🎯 **研究动机**：当前音频后门的毒化样本听感质量退化，容易被人类听众察觉
- 🔬 **研究方法**：提出 Watermark-as-Trigger 概念：经对抗 LoRA 微调把音频水印嵌入作为隐蔽触发器，构建 Bloodroot 后门框架
- 📌 **结论**：语音识别与说话人识别数据集上触发成功率与干净样本准确率同步提升，并在声学滤波与模型剪枝下保持有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor data poisoning is a crucial technique for ownership protection and defending against malicious attacks. Embedding hidden triggers in training data can manipulate model outputs, enabling provenance verification, and deterring unauthorized use. However, current audio backdoor methods are suboptimal, as poisoned audio often exhibits degraded perceptual quality, which is noticeable to human listeners. This work explores the intrinsic stealthiness and effectiveness of audio watermarking in achieving successful poisoning. We propose a novel Watermark-as-Trigger concept, integrated into the Bloodroot backdoor framework via adversarial LoRA fine-tuning, which enhances perceptual quality while achieving a much higher trigger success rate and clean-sample accuracy. Experiments on speech recognition (SR) and speaker identification (SID) datasets show that watermark-based poisoning remains effective under acoustic filtering and model pruning. The proposed Bloodroot backdoor framework not only secures data-to-model ownership, but also well reveals the risk of adversarial misuse.

</details>

### 7. Mental Damage: Caption Poisoning Attacks on Retrieval-Augmented Text-to-Music Generation

📄 [arXiv](https://arxiv.org/abs/2605.30365)　📅 2026-05

**关键词**：`attack`、`text-to-music poisoning`、`caption poisoning`、`retrieval augmentation`

👤 **作者**：Yizhu Wen、Shuhao Zhang、Nan Zhang、Long Cheng、Hanqing Guo

- 🎯 **研究动机**：检索增强 text-to-music 系统依赖音乐字幕知识库做 prompt 增广，形成未被审视的完整性依赖
- 🔬 **研究方法**：Mental Damage 双层字幕投毒：保留高层检索锚点、注入低层声学描述符，诱导 prompt 增强与下游生成偏向攻击者选定意图，且不修改用户 prompt、检索器或生成器
- 📌 **结论**：在 MusicCaps+CLAP+MusicGen 管线中，投毒后的生成显著逼近攻击者目标意图，同时与原查询保持可比的对齐度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented text-to-music (TTM) systems augment underspecified user prompts using captions retrieved from a music caption dataset. This design introduces an integrity dependency on the music knowledge database. We show that an attacker can poison the database by injecting a small number of crafted music captions, causing the system to retrieve malicious captions that bias prompt augmentation and steer generation away from the user's intended function, without modifying the user prompt, retriever, or generator. To achieve the music caption poisoning attack, we propose a dual-layer caption poisoning strategy that preserves high-level retrieval anchors while injecting low-level acoustic descriptors to steer prompt augmentation and downstream music generation toward an attacker-chosen target intent. In a MusicCaps knowledge database, CLAP retriever, and MusicGen pipeline, poisoned generations move substantially closer to the attacker's target, while remaining comparably aligned with the original user query. These results expose a practical integrity risk for retrieval-augmented creative AI systems. Our demo can be found at: https://yizhu-wen.github.io/Mental-Damage/

</details>

### 8. Imperceptible Rhythm Backdoor Attacks: Exploring Rhythm Transformation for Embedding Undetectable Vulnerabilities on Speech Recognition

📄 [arXiv](https://arxiv.org/abs/2406.10932)　📅 2024-06

**关键词**：`attack`、`rhythm transformation trigger`、`stealthy poisoning`、`speech recognition`

👤 **作者**：Wenhan Yao、Jiangkun Yang、Yongqiang He、Jia Liu、Weiping Wen

- 🎯 **研究动机**：既有语音后门通过加噪或修改音高音色构造毒化样本，仍可能被人耳或自动算法检测
- 🔬 **研究方法**：提出非神经快速算法 RSRT：对 mel 谱做节奏拉伸或压缩并还原为语音信号，保持音色与内容不变以嵌入不可察觉的节奏触发器
- 📌 **结论**：两类语音识别任务上低投毒率即取得很高 ASR，说话人验证与 ASR 检测均难以识别毒化样本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech recognition is an essential start ring of human-computer interaction, and recently, deep learning models have achieved excellent success in this task. However, when the model training and private data provider are always separated, some security threats that make deep neural networks (DNNs) abnormal deserve to be researched. In recent years, the typical backdoor attacks have been researched in speech recognition systems. The existing backdoor methods are based on data poisoning. The attacker adds some incorporated changes to benign speech spectrograms or changes the speech components, such as pitch and timbre. As a result, the poisoned data can be detected by human hearing or automatic deep algorithms. To improve the stealthiness of data poisoning, we propose a non-neural and fast algorithm called Random Spectrogram Rhythm Transformation (RSRT) in this paper. The algorithm combines four steps to generate stealthy poisoned utterances. From the perspective of rhythm component transformation, our proposed trigger stretches or squeezes the mel spectrograms and recovers them back to signals. The operation keeps timbre and content unchanged for good stealthiness. Our experiments are conducted on two kinds of speech recognition tasks, including testing the stealthiness of poisoned samples by speaker verification and automatic speech recognition. The results show that our method has excellent effectiveness and stealthiness. The rhythm trigger needs a low poisoning rate and gets a very high attack success rate.

</details>

### 9. MASTERKEY: Practical Backdoor Attack Against Speaker Verification Systems

📄 [arXiv](https://arxiv.org/abs/2309.06981)　📅 2023-09

**关键词**：`attack`、`speaker verification backdoor`、`universal trigger`、`over-the-air`

👤 **作者**：Hanqing Guo、Xun Chen、Junfeng Guo、Li Xiao、Qiben Yan

- 🎯 **研究动机**：针对攻击者不了解受害系统细节的现实设定，现有投毒攻击难以攻击未见过的目标
- 🔬 **研究方法**：MASTERKEY 优化可攻击任意目标的通用后门，把说话人特征与语义信息嵌入触发器并估计信道失真，提升隐蔽性与信道鲁棒性
- 📌 **结论**：6 个主流 SV 模型、53 个投毒模型、16,430 个注册说话人上 15% 投毒率达 100% ASR，3% 投毒率仍约 50%；空中与电话线路两类真实信道实测成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speaker Verification (SV) is widely deployed in mobile systems to authenticate legitimate users by using their voice traits. In this work, we propose a backdoor attack MASTERKEY, to compromise the SV models. Different from previous attacks, we focus on a real-world practical setting where the attacker possesses no knowledge of the intended victim. To design MASTERKEY, we investigate the limitation of existing poisoning attacks against unseen targets. Then, we optimize a universal backdoor that is capable of attacking arbitrary targets. Next, we embed the speaker's characteristics and semantics information into the backdoor, making it imperceptible. Finally, we estimate the channel distortion and integrate it into the backdoor. We validate our attack on 6 popular SV models. Specifically, we poison a total of 53 models and use our trigger to attack 16,430 enrolled speakers, composed of 310 target speakers enrolled in 53 poisoned models. Our attack achieves 100% attack success rate with a 15% poison rate. By decreasing the poison rate to 3%, the attack success rate remains around 50%. We validate our attack in 3 real-world scenarios and successfully demonstrate the attack through both over-the-air and over-the-telephony-line scenarios.

</details>

### 10. Breaking Speaker Recognition with PaddingBack

📄 [arXiv](https://arxiv.org/abs/2308.04179)　📅 2023-08

**关键词**：`attack`、`speaker recognition backdoor`、`padding trigger`、`inaudible attack`

👤 **作者**：Zhe Ye、Diqun Yan、Li Dong、Kailai Shen

- 🎯 **研究动机**：语音后门使用的变换类触发器人耳容易察觉并引起怀疑
- 🔬 **研究方法**：PaddingBack 不用外部扰动，而是把广泛使用的语音信号填充（padding）操作本身作为触发器构造不可闻后门
- 📌 **结论**：显著 ASR 且保持良性准确率，可抵抗防御方法并瞒过人类听觉感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine Learning as a Service (MLaaS) has gained popularity due to advancements in Deep Neural Networks (DNNs). However, untrusted third-party platforms have raised concerns about AI security, particularly in backdoor attacks. Recent research has shown that speech backdoors can utilize transformations as triggers, similar to image backdoors. However, human ears can easily be aware of these transformations, leading to suspicion. In this paper, we propose PaddingBack, an inaudible backdoor attack that utilizes malicious operations to generate poisoned samples, rendering them indistinguishable from clean ones. Instead of using external perturbations as triggers, we exploit the widely-used speech signal operation, padding, to break speaker recognition systems. Experimental results demonstrate the effectiveness of our method, achieving a significant attack success rate while retaining benign accuracy. Furthermore, PaddingBack demonstrates the ability to resist defense methods and maintain its stealthiness against human perception.

</details>

### 11. Fake the Real: Backdoor Attack on Deep Speech Classification via Voice Conversion

📄 [arXiv](https://arxiv.org/abs/2306.15875)　📅 2023-06

**关键词**：`attack`、`voice conversion trigger`、`sample-specific trigger`、`speech classification`

👤 **作者**：Zhe Ye、Terui Mao、Li Dong、Diqun Yan

- 🎯 **研究动机**：现有语音后门触发器多为样本无关的固定模式，即便设计得隐蔽也仍然可闻
- 🔬 **研究方法**：Fake the Real 用预训练 voice conversion 模型生成样本特定的触发器，使毒化样本不引入任何额外可听噪声
- 📌 **结论**：两类语音分类任务上攻击有效，并验证了后门激活的具体场景与对微调的抵抗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep speech classification has achieved tremendous success and greatly promoted the emergence of many real-world applications. However, backdoor attacks present a new security threat to it, particularly with untrustworthy third-party platforms, as pre-defined triggers set by the attacker can activate the backdoor. Most of the triggers in existing speech backdoor attacks are sample-agnostic, and even if the triggers are designed to be unnoticeable, they can still be audible. This work explores a backdoor attack that utilizes sample-specific triggers based on voice conversion. Specifically, we adopt a pre-trained voice conversion model to generate the trigger, ensuring that the poisoned samples does not introduce any additional audible noise. Extensive experiments on two speech classification tasks demonstrate the effectiveness of our attack. Furthermore, we analyzed the specific scenarios that activated the proposed backdoor and verified its resistance against fine-tuning.

</details>

### 12. FlowMur: A Stealthy and Practical Audio Backdoor Attack with Limited Knowledge

📄 [arXiv](https://arxiv.org/abs/2312.09665)　📅 2023-12

**关键词**：`attack`、`audio backdoor`、`limited knowledge`、`SNR-adaptive poisoning`

👤 **作者**：Jiahe Lan、Jie Wang、Baochen Yan、Zheng Yan、Elisa Bertino

- 🎯 **研究动机**：现有音频后门需要充分知识、隐蔽性不足且大多无法攻击 live speech
- 🔬 **研究方法**：FlowMur 构造辅助数据集与代理模型增广攻击者知识，把触发器生成形式化为跨附着位置的优化问题，按信噪比自适应投毒并把环境噪声纳入触发器生成
- 📌 **结论**：数字与物理设定下均取得高攻击性能并抵抗 SOTA 防御；人类研究确认参与者不易察觉其触发器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech recognition systems driven by DNNs have revolutionized human-computer interaction through voice interfaces, which significantly facilitate our daily lives. However, the growing popularity of these systems also raises special concerns on their security, particularly regarding backdoor attacks. A backdoor attack inserts one or more hidden backdoors into a DNN model during its training process, such that it does not affect the model's performance on benign inputs, but forces the model to produce an adversary-desired output if a specific trigger is present in the model input. Despite the initial success of current audio backdoor attacks, they suffer from the following limitations: (i) Most of them require sufficient knowledge, which limits their widespread adoption. (ii) They are not stealthy enough, thus easy to be detected by humans. (iii) Most of them cannot attack live speech, reducing their practicality. To address these problems, in this paper, we propose FlowMur, a stealthy and practical audio backdoor attack that can be launched with limited knowledge. FlowMur constructs an auxiliary dataset and a surrogate model to augment adversary knowledge. To achieve dynamicity, it formulates trigger generation as an optimization problem and optimizes the trigger over different attachment positions. To enhance stealthiness, we propose an adaptive data poisoning method according to Signal-to-Noise Ratio (SNR). Furthermore, ambient noise is incorporated into the process of trigger generation and data poisoning to make FlowMur robust to ambient noise and improve its practicality. Extensive experiments conducted on two datasets demonstrate that FlowMur achieves high attack performance in both digital and physical settings while remaining resilient to state-of-the-art defenses. In particular, a human study confirms that triggers generated by FlowMur are not easily detected by participants.

</details>

### 13. Towards Stealthy Backdoor Attacks against Speech Recognition via Elements of Sound

📄 [arXiv](https://arxiv.org/abs/2307.08208)　📅 2023-07

**关键词**：`attack`、`poison-only backdoor`、`pitch trigger`、`timbre trigger`

👤 **作者**：Hanbo Cai、Pengcheng Zhang、Hai Dong、Yan Xiao、Stefanos Koffas、Yiming Li

- 🎯 **研究动机**：现有 poison-only 语音后门的触发器是简单噪声或可分离的独特片段，可被人类或机器检测
- 🔬 **研究方法**：利用声音元素设计触发器：插入短时高音信号并提升其余片段音高加以掩蔽；操纵音色特征并配合声纹选择模块支持多后门
- 📌 **结论**：all-to-one、all-to-all、clean-label、物理与多后门等设定下均有效，毒化样本更自然、更隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) have been widely and successfully adopted and deployed in various applications of speech recognition. Recently, a few works revealed that these models are vulnerable to backdoor attacks, where the adversaries can implant malicious prediction behaviors into victim models by poisoning their training process. In this paper, we revisit poison-only backdoor attacks against speech recognition. We reveal that existing methods are not stealthy since their trigger patterns are perceptible to humans or machine detection. This limitation is mostly because their trigger patterns are simple noises or separable and distinctive clips. Motivated by these findings, we propose to exploit elements of sound ($e.g.$, pitch and timbre) to design more stealthy yet effective poison-only backdoor attacks. Specifically, we insert a short-duration high-pitched signal as the trigger and increase the pitch of remaining audio clips to `mask' it for designing stealthy pitch-based triggers. We manipulate timbre features of victim audios to design the stealthy timbre-based attack and design a voiceprint selection module to facilitate the multi-backdoor attack. Our attacks can generate more `natural' poisoned samples and therefore are more stealthy. Extensive experiments are conducted on benchmark datasets, which verify the effectiveness of our attacks under different settings ($e.g.$, all-to-one, all-to-all, clean-label, physical, and multi-backdoor settings) and their stealthiness. The code for reproducing main experiments are available at \url{https://github.com/HanboCai/BadSpeech_SoE}.

</details>

## 后门防御

### 14. SpeechGuard: Online Defense against Backdoor Attacks on Speech Recognition Models

📄 [arXiv](https://arxiv.org/abs/2607.15697)　📅 2026-07

**关键词**：`defense`、`online backdoor defense`、`S-STRIP`、`time-frequency masking`

👤 **作者**：Jinwen Xin、Xixiang Lv

- 🎯 **研究动机**：自动驾驶语音交互等安全敏感场景需要在运行时防御语音识别模型后门，而现有方法不针对音频特性
- 🔬 **研究方法**：SpeechGuard 首个在线防御管线：S-STRIP 用自适应扰动注入检测并过滤毒化样本，再用基于自编码器的时频掩蔽抑制触发器表达、净化毒化语音
- 📌 **结论**：两阶段处理可准确滤除带触发器的输入，显著缓解后门威胁同时保持可用预测精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a critical threat to neural network models, allowing attackers to implant a backdoor during the training phase by manipulating a small portion of the training data. In security-sensitive applications such as voice interaction for autonomous driving, the presence of backdoor attacks introduces substantial security risks. This study focuses on implementing backdoor defense measures for speech recognition models in run-time, taking into account the characteristics of audio signals. We propose SpeechGuard, the first online backdoor defense pipeline designed to identify and purify poisoned audio samples. Specifically, we improve STRIP method to perform adaptive perturbation injection to detect and filter poisoned samples, named as S-STRIP. More importantly, we further consider the purification of poisoned samples. We utilize time-frequency (T-F) masking to suppress the expression of trigger signals and autonomously generate masks based on an autoencoder. The two-stage processing prevents the backdoor in the model from being triggered, and even input speech carrying triggers can be accurately predicted. Extensive experimental demonstrate that SpeechGuard can accurately filter out poisoned samples. Through purification, it can significantly mitigate the backdoor threat while maintaining a certain prediction accuracy.

</details>

### 15. Gradient Norm-based Fine-Tuning for Backdoor Defense in Automatic Speech Recognition

📄 [arXiv](https://arxiv.org/abs/2502.01152)　📅 2025-02

**关键词**：`defense`、`backdoor defense`、`gradient norm regularization`、`ASR`

👤 **作者**：Nanjun Zhou、Weilin Lin、Li Liu

- 🎯 **研究动机**：视觉域后门防御直接迁移到音频域效果有限，音频领域缺乏专门防御
- 🔬 **研究方法**：GN-FT 观察到后门神经元梯度值显著大于干净神经元，微调时引入梯度范数正则以削弱后门神经元，并近似损失计算降低实现成本
- 📌 **结论**：两个语音识别数据集五个模型上优于现有防御，为首个专门且有效的音频域后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks have posed a significant threat to the security of deep neural networks (DNNs). Despite considerable strides in developing defenses against backdoor attacks in the visual domain, the specialized defenses for the audio domain remain empty. Furthermore, the defenses adapted from the visual to audio domain demonstrate limited effectiveness. To fill this gap, we propose Gradient Norm-based FineTuning (GN-FT), a novel defense strategy against the attacks in the audio domain, based on the observation from the corresponding backdoored models. Specifically, we first empirically find that the backdoored neurons exhibit greater gradient values compared to other neurons, while clean neurons stay the lowest. On this basis, we fine-tune the backdoored model by incorporating the gradient norm regularization, aiming to weaken and reduce the backdoored neurons. We further approximate the loss computation for lower implementation costs. Extensive experiments on two speech recognition datasets across five models demonstrate the superior performance of our proposed method. To the best of our knowledge, this work is the first specialized and effective defense against backdoor attacks in the audio domain.

</details>
