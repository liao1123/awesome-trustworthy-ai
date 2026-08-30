# 隐写与隐蔽信道

## 研究方向

隐写与隐蔽信道研究模型或 Agent 如何把秘密、恶意指令和行为控制信号隐藏在自然语言、图像、音视频、数值参数或工具交互中，并考察这些信道的容量、不可感知性、鲁棒性、检测方法以及在越狱、数据外泄和多 Agent 合谋中的安全风险。

## 研究脉络

- **隐写编码：** 基础工作追求高容量、低可感知性和 provable security，研究如何稳定地在自然语言中承载隐藏信息。
- **安全滥用：** 攻击研究将 steganography 用于 jailbreak、隐蔽微调、backdoor 与多 Agent collusion。
- **检测与防御：** 防御路线覆盖 steganalysis、训练接口防护和后门移除，并检验编码方案在自适应检测下是否仍隐蔽。

## 安全绕过与 Steganographic Backdoor

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection | attack、structured-data covert channel、float carrier、indirect prompt injection | 未确认（arXiv Comments：FAGEN@ICML 2026 Workshop Poster） | [arXiv](https://arxiv.org/abs/2606.08403) | 暂未公开 | 针对文本检测器只能检查可见文本视图，论文把 payload 存入浮点数组并以碎片遥测重建；结果对最强双层文本防御仍保持 94.3% 泄漏 ASR，但简单结构校验可阻断当前实例。 |
| 2026&#8209;05 | CORDYCEPS: Covert Control Attacks on LLMs via Data Poisoning | attack、steganographic backdoor、stealthy backdoor、covert channel | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shao-zedian) · [arXiv](https://arxiv.org/abs/2605.26595) | [Code](https://github.com/Sadcardation/cordyceps) · [Artifact](https://anonymous.4open.science/r/cordyceps-F147) | 针对固定触发词后门易被清洗和监控，论文用常识概念与攻击短语的语义关联教会模型隐藏协议；结果少量投毒即可编码任意恶意指令，并在多类防御后保持很高攻击成功率。 |
| 2026&#8209;03 | Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning | attack、steganographic backdoor、safety bypass、stealthy backdoor | ICML 2026 Spotlight | [Official](https://icml.cc/virtual/2026/poster/66278) · [arXiv](https://arxiv.org/abs/2603.29038) | 暂未公开 | 针对微调攻击常以大幅能力退化为代价，论文用课程学习和 GRPO 教会模型绕过 Constitutional Classifier 的通信协议；结果在 14B 以上模型实现逾 99% 规避且能力下降低于 5%。 |
| 2026&#8209;03 | Invisible Safety Threat: Malicious Finetuning for LLM via Steganography | attack、steganographic backdoor、stealthy backdoor | ICLR 2026 Oral | [Official](https://iclr.cc/virtual/2026/poster/10011363) · [arXiv](https://arxiv.org/abs/2603.08104) · [OpenReview](https://openreview.net/forum?id=6cEPDGaShH) | [Code](https://github.com/bigglesworthnotacat/LLM-Steg) · [Model](https://huggingface.co/bigglesworthnotcat/LLM-Steg-Llama-70B-Lora) · [Dataset](https://huggingface.co/datasets/bigglesworthnotcat/llm-steg-alpaca-gpt4) | 针对模型可表面保持安全却暗中回答有害问题，论文恶意微调模型在良性问答中编码隐藏请求与回答；结果闭源和开源模型都能传输恶意内容并被安全分类器全部误判为安全。 |
| 2025&#8209;12 | Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography | attack、multimodal steganography、safety bypass | NDSS 2026 | [Official](https://www.ndss-symposium.org/ndss-paper/odysseus-jailbreaking-commercial-multimodal-llm-integrated-systems-via-dual-steganography/) · [arXiv](https://arxiv.org/abs/2512.20168) | [Code](https://github.com/S3IC-Lab/Odysseus) | 针对商业多模态系统的输入输出过滤假设恶意内容必须可见，论文用双重隐写把请求和回答分别藏入良性图像；结果对多种现实系统的越狱成功率最高达到 99%。 |
| 2025&#8209;07 | Invisible Injections: Exploiting Vision-Language Models Through Steganographic Prompt Embedding | attack、multimodal steganography、safety bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.22304) | 暂未公开 | 针对恶意提示可否不可见地嵌入图像并被 VLM 执行，论文比较空间域、频域和神经隐写攻击；结果跨八个模型取得中等但现实的成功率，并证明多模态输入形成新的注入面。 |
| 2025&#8209;05 | TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent | attack、steganographic backdoor、stealthy backdoor、privacy leakage | EMNLP 2025 Main | [Official](https://aclanthology.org/2025.emnlp-main.1386/) · [arXiv](https://arxiv.org/abs/2505.20118) | [Dataset](https://huggingface.co/datasets/worta/TrojanStego) · [Model](https://huggingface.co/worta/TrojanStego-LLama3-8B-LoRA) | 针对被微调模型可否在正常使用中被动窃取上下文秘密，论文用词表分区教会模型把 32-bit 信息写入自然回答；结果单次恢复率达 87%，三次多数投票超过 97%。 |
| 2025&#8209;05 | Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs | attack、steganographic backdoor、stealthy backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.17601) | 暂未公开 | 针对含显式有害问答的后门数据易被 guardrail 过滤，论文只用良性样本把触发器关联到肯定式回答前缀；结果可在保持数据无害外观时诱导多种 LLM 生成有害内容。 |
| 2025&#8209;05 | Hiding in Plain Sight: A Steganographic Approach to Stealthy LLM Jailbreaks | attack、linguistic steganography、safety bypass | ICLR 2026，Rejected | [arXiv](https://arxiv.org/abs/2505.16765) · [OpenReview](https://openreview.net/forum?id=ZujfJpD6as) | [Code](https://github.com/GenggengSvan/StegoAttack) | 针对越狱攻击难同时保持语义与语言隐蔽，论文用 StegoAttack 把有害请求嵌入自然良性段落；结果在四个安全对齐模型上平均达到 95.5% ASR，外部检测下仍保持较强效果。 |
| 2024&#8209;06 | Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation | attack、steganographic backdoor、stealthy backdoor、covert channel | ICML 2024 | [Official](https://proceedings.mlr.press/v235/halawi24a.html) · [arXiv](https://arxiv.org/abs/2406.20053) | 暂未公开 | 针对黑盒微调 API 的数据逐条看似无害却可整体破坏安全，论文用编码请求与回答构造 covert malicious finetuning；结果在 GPT-4 上实现 99% 有害指令执行并逃过多类审核。 |

## Multi-Agent Covert Communication 与 Collusion

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | FLux: Covert Channels in FL through Transposed Training | attack、federated learning、covert channel、trace removal | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3805980) | 暂未公开 | 针对 federated aggregation 被假设只承载合法 model update；FLux 以原模型的 transposed network 解码图像或比特；结果恶意参与者从首轮即可双向隐蔽通信并在事后清除 channel 痕迹。 |
| 2026&#8209;06 | Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems | attack、multi-agent steganography、provable security、multi-agent covert communication | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.28425) | 暂未公开 | 针对复杂隐写协议是否仍超出 Agent 能力，论文允许 coding Agent 使用代码执行和网页研究来构建信道；结果表明技术实现已不是主要障碍，协议、密钥与参数的协调才是瓶颈。 |
| 2026 | Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs | analysis、implicit memory、temporal backdoor、covert channel | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | 针对 LLM session 被默认视为无状态的假设，作者展示模型可把隐藏状态编码进自身输出并在重输入时恢复，由此构造 time-bomb backdoor，并讨论跨智能体隐蔽通信、评测作弊与投毒风险。 |
| 2025&#8209;08 | Whispering Agents: An Event-Driven Covert Communication Protocol for the Internet of Agents | tool、multi-agent steganography、multi-agent covert communication、covert channel | AAAI 2026 | [Official](https://ojs.aaai.org/index.php/AAAI/article/view/40380) · [arXiv](https://arxiv.org/abs/2508.02188) | 暂未公开 | 针对常规 A2A 加密不能隐藏“正在通信”这一事实，论文形式化存储、时序和行为三类 Covert Event Channel 并实现协议；结果获得较高容量与鲁棒性且难被 LLM warden 感知。 |
| 2024&#8209;10 | Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs | analysis、multi-agent steganography、multi-agent covert communication | ICJNLP 2025 | [arXiv](https://arxiv.org/abs/2410.03768) | 暂未公开 | 针对错误奖励是否会诱导 Agent 形成隐写合谋，论文用梯度式和上下文式 RL 训练隐蔽通信；结果合谋可自发出现，输出监督与通信改写都不能彻底阻断。 |
| 2024&#8209;02 | Secret Collusion among AI Agents: Multi-Agent Deception via Steganography | attack、multi-agent steganography、multi-agent covert communication | NeurIPS 2024 | [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/861f7dad098aec1c3560fb7add468d41-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2402.07510) | 暂未公开 | 针对多 Agent 可能用隐写实施未经授权协调，论文形式化激励、能力与缓解措施并提出评测框架；结果当前模型总体能力有限但 GPT-4 出现跃升，需持续监控前沿模型。 |

## 编码方法与基础 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Provably Secure Steganography Based on List Decoding | tool、linguistic steganography、provable security | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.21394) | 暂未公开 | 针对可证明安全语言隐写在低熵 LLM 上容量不足，论文用 list decoding 保留候选消息并以 suffix matching 保证正确恢复；结果在保持安全与效率时显著提高嵌入容量。 |
| 2026&#8209;04 | Text Steganography with Dynamic Codebook and Multimodal Large Language Model | tool、multimodal steganography、encoding method | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.20269) | 暂未公开 | 针对黑盒隐写依赖固定共享码本和逐句提取提示，论文借助 MLLM 建立动态码本并用拒绝采样反馈优化；结果比白盒方法具有更高容量与文本质量，也改善在线社交场景的灵活性。 |
| 2026&#8209;04 | Anchored Sliding Window: Toward Robust and Imperceptible Linguistic Steganography | tool、linguistic steganography、encoding method | ACL 2026 Main | [arXiv](https://arxiv.org/abs/2604.09066) · [ACL Anthology](https://aclanthology.org/2026.acl-long.44/) | [Code](https://github.com/ryehr/ASW_steganography) | 针对语言隐写经微小编辑即失效、缩短上下文又损害文本质量，论文固定提示和桥接上下文并以自蒸馏优化；结果同时提升文本质量、不可感知性和传输鲁棒性。 |
| 2026&#8209;04 | Efficient Provably Secure Linguistic Steganography via Range Coding | tool、linguistic steganography、provable security | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.39/) · [arXiv](https://arxiv.org/abs/2604.08052) | [Code](https://github.com/ryehr/RRC_steganography) | 针对完美不可感知隐写的容量与速度不足，论文把经典 range coding 加入旋转机制；结果达到接近 100% 的熵利用率，并在 GPT-2 上实现每秒逾 1,500 bit 的嵌入。 |
| 2026&#8209;03 | OD-Stega: LLM-Based Relatively Secure Steganography via Optimized Distributions | attack、LLM steganography、distribution optimization、payload efficiency | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.36/) | 暂未公开 | 针对 stego text 的 bit capacity 与自然度冲突；OD-Stega 在 KL 或 total-variation 距离约束下最大化替代 next-token distribution 的 entropy，并结合 arithmetic coding；结果给出可解析的更高效 covert-text generation 方法。 |
| 2025&#8209;10 | LLMs Can Hide Text in Other Text of the Same Length | analysis、linguistic steganography、covert channel | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10009123) · [arXiv](https://arxiv.org/abs/2510.20075) · [OpenReview](https://openreview.net/forum?id=VbTLgEUocp) | [Code](https://github.com/noranta4/calgacus) | 针对长秘密能否完整隐藏在等长自然文本中，论文提出可由 8B 开源模型本地执行的 Calgacus 协议；结果可快速编码连贯长文，显示文本表意与隐藏意图可被彻底解耦。 |
| 2025&#8209;03 | SparSamp: Efficient Provably Secure Steganography Based on Sparse Sampling | tool、linguistic steganography、provable security、encoding method | USENIX 2025 | [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-yaofei) · [arXiv](https://arxiv.org/abs/2503.19499) | 暂未公开 | 针对可证明安全生成隐写存在效率瓶颈，论文把秘密与伪随机数结合并采用稀疏采样；结果保持原分布和常数额外复杂度，并在文本、图像和音频上实现高吞吐嵌入。 |
| 2023&#8209;03 | Discop: Provably Secure Steganography in Practice Based on “Distribution Copies” | tool、linguistic steganography、provable security | IEEE S&P 2023，已录用 | [DOI](https://doi.org/10.1109/SP46215.2023.10179287) | [Code](https://github.com/comydream/Discop) | 针对可证明安全隐写依赖理想采样器而难落地，论文旋转生成分布构造多个 distribution copies 并以索引编码秘密；结果达到完美分布安全且嵌入率接近理论上限。 |
| 2021&#8209;06 | Provably Secure Generative Linguistic Steganography | tool、linguistic steganography、provable security、encoding method | Findings of ACL-IJCNLP 2021 | [Official](https://aclanthology.org/2021.findings-acl.268/) · [arXiv](https://arxiv.org/abs/2106.02011) | 暂未公开 | 针对传统生成隐写会改变自然文本概率分布，论文提出按语言模型概率递归动态分组 token 的 ADG；理论与实验均表明其生成文本接近完美不可感知。 |

## Detection 与 Steganalysis

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs | detection、linguistic steganography、steganography detection、stealthy backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.09411) | 暂未公开 | 针对线性激活 probe 可被自适应隐写微调绕过，论文训练五类 evasive trojan 并用信息论分析低阶可提取性；结果定向重构上下文数据分布可恢复线性和 MLP 检测能力。 |
| 2026&#8209;06 | Evaluating Multimodal Steganalysis for Split-Payload Audiovisual Steganography | detection、multimodal steganography、steganography detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.08726) | 暂未公开 | 针对把秘密拆到音频和视频是否更难检测，论文构造同步与异步 split-payload 样本并比较单模态和多模态检测器；结果单模态接近随机，而多模态收益主要来自视频而非真正融合。 |
| 2026&#8209;01 | Hide and Seek in Embedding Space: Geometry-based Steganography and Detection in Large Language Models | detection、embedding steganography、steganography detection、encoding method | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62426) · [arXiv](https://arxiv.org/abs/2601.22818) | 暂未公开 | 针对既有微调隐写映射可被轻易恢复，论文用 embedding 几何构造低可恢复信道并分析内部表征；结果后层激活的线性 probe 仍能发现恶意微调留下的秘密信号。 |

## 能力、泄漏与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Inadvertent Context Leakage in Language Models | analysis、linguistic steganography、covert channel、privacy leakage | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19857) | 暂未公开 | 针对模型即使拒绝直接提取仍可能泄露上下文秘密，论文利用良性输出中的隐藏相关性并训练自适应黑盒攻击把模型变成 covert carrier；结果可高成功率恢复短秘密，并从生产式 Agent 提取完整敏感标识。 |
| 2025&#8209;10 | All Code, No Thought: Current Language Models Struggle to Reason in Ciphered Language | analysis、linguistic steganography、ciphertext reasoning | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10006530) · [arXiv](https://arxiv.org/abs/2510.09714) · [OpenReview](https://openreview.net/forum?id=yjFkeQ2ynQ) | [Code](https://github.com/safety-research/ciphered-reasoning-llms) | 针对模型能否用密文推理逃避 CoT 监控，论文在 28 种 cipher 上提示和微调十类模型；结果模型虽能翻译密文却普遍难在其中推理，能力主要随预训练中的 cipher 流行度缓慢增长。 |
| 2025&#8209;07 | Early Signs of Steganographic Capabilities in Frontier LLMs | analysis、linguistic steganography、detection evasion | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10007285) · [arXiv](https://arxiv.org/abs/2507.02737) · [OpenReview](https://openreview.net/forum?id=q4qxtaKVAU) | [Code](https://github.com/arturzolkowski/steganographic-evals) · [Experiments](https://steganography-evals-d9297ad0740c.herokuapp.com/) | 针对前沿模型是否已能隐藏消息或推理，论文构建编码传递与编码推理评测；结果标准条件下能力尚弱，但未监控 scratchpad、预先协调方案等额外条件会显著提高风险。 |
| 2025&#8209;06 | Large Language Models Can Learn and Generalize Steganographic Chain-of-Thought under Process Supervision | analysis、linguistic steganography、covert reasoning | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/28131b22fafebba500eb7bb02e3d5b59-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.01926) | 暂未公开 | 针对惩罚特定 CoT 字符是否会消除不良推理，论文在 process supervision 下禁止负载关键字符串；结果模型会自行替换并把编码规则泛化到未见字符串，而原有行为继续存在。 |
| 2025&#8209;05 | The Steganographic Potentials of Language Models | analysis、linguistic steganography、detection evasion | ICLR 2025 Workshop | [arXiv](https://arxiv.org/abs/2505.03439) | 暂未公开 | 针对 LLM 是否会主动发展隐蔽协议，论文用 RL 微调和行为评测考察自创编码、提示隐写和现实隐藏推理；结果当前能力仍初级，但算法指导会明显提高信息隐藏容量。 |

## 防御与移除

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;08 | Towards Safeguarding LLM Fine-tuning APIs against Cipher Attacks | defense、steganographic backdoor、stealthy backdoor、ciphertext reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.17158) | [Code](https://github.com/JackYoustra/safe-finetuning-api) | 针对攻击者用密文微调数据绕过 API 审核，论文构建 CIFR benchmark 并训练内部激活 probe；结果检测率超过 99%，且能泛化到未见过的密文变体和家族。 |
| 2024&#8209;06 | BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Instruction-tuned Language Models | defense、steganographic backdoor、stealthy backdoor | EMNLP 2024 Main | [Official](https://aclanthology.org/2024.emnlp-main.732/) · [arXiv](https://arxiv.org/abs/2406.17092) | [Code](https://github.com/reds-lab/beear) | 针对安全后门触发空间巨大且行为多样，论文利用触发器造成相似 embedding 漂移的规律，以双层优化寻找通用扰动并强化安全响应；结果把多类后门成功率降至接近零且不损害效用。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | A Comprehensive Survey on Linguistic Steganography: Methods, Countermeasures, Evaluation, and Challenges | survey、linguistic steganography、covert channel | 未确认（OpenReview 匿名稿） | [OpenReview PDF](https://openreview.net/pdf/150b32ad8b94c5a652f00f1ae3e517c4add1e722.pdf) | 暂未公开 | 针对 LLM 时代语言隐写缺少完整综述，论文系统整理约 140 种方法、58 种反制、23 个指标和 9 个开放问题；结论是生成能力提升同时扩大了容量、检测和工程落地之间的矛盾。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Synchronized Logit Steering: Real-world Steganography | analysis、model steganography、covert channel、safety bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14697) | 暂未公开 | 大语言模型中的隐写术提供了一种将隐藏消息嵌入到听起来自然的文本中的方法；我们引入了同步 Logit 引导 (SLS)，这是一种确定性隐写方案，它通过从生成的输出本身派生代理提示来消除这种依赖性，从而允许双方在无需访问原始提示的情况下重建相同的 Logit 分布；Kolmogorov-Smirnov 测试进一步证实，SLS 输出在统计上很难与贪婪的一代区分开来，这表明通过 LLM 进行的隐蔽的、与提示无关的通信既实用又隐秘。 |
| 2026&#8209;07 | Secret-Stego Dissimilarity as a Design Axis: Invertible Coverless Image Steganography with Diffusion Models | analysis、model steganography、covert channel、safety bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13597) | 暂未公开 | 无封面图像隐写术 (CIS) 合成隐写图像，而不是修改现有的封面图像，使授权接收者能够从隐写图像重建原始秘密图像；为了解决这个问题，我们提出了 InvCISD，这是一种可逆扩散框架，它将秘密的潜在表示和不相关的参考图像与称为 LIMNet 的可逆网络结合起来；我们的进一步研究表明，所有评估的方法都可以被面向 CIS 的隐写分析模型高度检测到，这表明针对针对性隐写分析的抵抗构成了未来 CIS 研究的一个关键方向。 |
