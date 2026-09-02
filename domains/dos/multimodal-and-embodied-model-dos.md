# 多模态与具身模型 DoS

## 研究方向

多模态与具身模型 DoS 研究不同输入模态如何形成专属可用性攻击面：2D 图像与 3D 点云可通过细微扰动诱发冗长生成，视频模型可被跨帧通用触发器拖慢，VLA 和机器人则可能被视觉或音频信号冻结动作。这里同时关注计算资源放大与物理任务停滞，因为具身系统即使没有大量消耗 token，也可能出现实际意义上的拒绝服务。

## 研究脉络

- **视觉输入攻击：** 多模态 DoS 最初利用图像诱导 verbose generation，放大 token、延迟或能耗。
- **模态扩展：** 攻击随后覆盖视频、3D 几何和语言状态循环，利用不同感知输入延长模型处理过程。
- **具身后果：** 在 embodied model 中，目标进一步变为冻结动作或触发安全停机，攻击后果从计算开销延伸到物理任务不可用。

## 视觉、视频与 3D 模型攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | The Boy Who Cried Wolf: Adversarial Misclassification of Safe Inputs as Unsafe in Multimodal Guardrails ↗ | attack、logical DoS、multimodal guardrail、false-positive induction | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817756) · [arXiv](https://arxiv.org/abs/2608.01373) | [Code](https://doi.org/10.5281/zenodo.20423252) | 针对审核系统本身可成为拒绝服务入口 | Unsafe Semantic Distillation 对良性图像加入不可感知扰动 | 使其在不同未知 prompt 下仍被多模态 guard 判为 unsafe | 四个 guard 上 84% ASR 表明攻击者无需耗尽算力也能通过持续 false positive 阻断正常服务。 |
| 2026-07 | Infinite Babble: Inflating 3D Vision-Language Model Inference Overhead via Adversarial Geometric Perturbation | attack、3D-VLM DoS、geometric perturbation、EOS suppression | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.259/) | 暂未公开 | 针对 3D-VLM 会处理不可信点云且依赖自回归解码 | 论文用 Inflate3D 扰动语义关键区域并压低 EOS 概率 | 关键实现：论文用 Inflate3D 扰动语义关键区域并压低 EOS 概率。 | 结果在保持几何结构的同时将输出长度和能耗最高放大 6.45 倍。 |
| 2026-03 | VidDoS: Universal Denial-of-Service Attack on Video-based Large Language Models | attack、Video-LLM DoS、universal trigger、cross-frame attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.01454) | [Code](https://github.com/DAIDASEN/VIDDos) | 针对逐样本图像攻击难适配连续视频 | 论文用 masked teacher forcing、拒绝惩罚和终止抑制学习跨视频通用触发器 | 关键实现：论文用 masked teacher forcing、拒绝惩罚和终止抑制学习跨视频通用触发器。 | 结果令 Video-LLM token 增长逾 205 倍、延迟增加逾 15 倍。 |
| 2025-11 | An Image Is Worth Ten Thousand Words: Verbose-Text Induction Attacks on VLMs | attack、VLM DoS、2D VLM、visual perturbation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.16163) | 暂未公开 | 针对仅延迟 EOS 难以稳定直接最大化 VLM 输出长度 | 论文先用强化学习搜索恶意提示嵌入 | 再把良性图像优化到相应视觉表示 | 结果在四种 VLM 上更稳定地诱发冗长文本并具备泛化能力。 |
| 2025-11 | RemedyGS: Defend 3D Gaussian Splatting Against Computation Cost Attacks | defense、3D Gaussian splatting、resource exhaustion、availability | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_RemedyGS_Defend_3D_Gaussian_Splatting_Against_Computation_Cost_Attacks_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.22147) | 暂未公开 | 针对恶意 3DGS 资产可膨胀渲染计算并造成拒绝服务 | RemedyGS 检测和规整异常高成本 primitives | 关键实现：RemedyGS 检测和规整异常高成本 primitives。 | 在尽量保持画质时恢复可用性。 |
| 2025-06 | LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops | attack、MLLM DoS、part-of-speech optimization、state trapping | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10007735) · [arXiv](https://arxiv.org/abs/2506.14493) · [OpenReview](https://openreview.net/forum?id=kxEM2vc7ne) | [Code](https://github.com/fuhaha824/LingoLoop-Attack) | 针对既有能耗攻击忽略词性和句级循环结构 | 论文通过 POS 感知延迟 EOS 并收缩隐藏状态生成路径 | 关键实现：论文通过 POS 感知延迟 EOS 并收缩隐藏状态生成路径。 | 结果可让 MLLM 持续循环并产生最多 367 倍 token。 |
| 2024-01 | Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images | attack、VLM DoS、2D VLM、verbose image | ICLR 2024 | [Official](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4a6a5e2e8a27262501bda3463fcf7b21-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2401.11170) | [Code](https://github.com/KuofengGao/Verbose_Images) | 针对图像输入也能操纵 VLM 自回归生成成本 | 论文联合延迟 EOS、提高 token 不确定性和序列多样性来制作不可察觉的 verbose images | 关键实现：论文联合延迟 EOS、提高 token 不确定性和序列多样性来制作不可察觉的 verbose images。 | 结果在 MS-COCO 和 ImageNet 上把生成长度分别放大 7.87 倍和 8.56 倍。 |

## Embodied Model 可用性攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | Semantic Denial of Service in LLM-controlled robots | attack、robot-agent DoS、robotics、audio injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.24790) | 暂未公开 | 针对机器人把未经认证的音频文本直接交给 LLM 决策 | 论文注入 1 至 5 个看似合理的安全警示 token 触发停机或循环 | 关键实现：论文注入 1 至 5 个看似合理的安全警示 token 触发停机或循环。 | 结果提示级防御只能在抑制攻击与响应真实危险之间权衡，需从架构上分离安全监控和动作选择。 |
| 2025-09 | FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models | attack、VLA DoS、action freezing、adversarial image | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.19870) | [Repository](https://github.com/xinwong/FreezeVLA)（当前仅 README） | 针对 VLA 在关键干预时可能忽略后续指令 | 论文用 min-max 双层优化生成让动作持续冻结的对抗图像 | 关键实现：论文用 min-max 双层优化生成让动作持续冻结的对抗图像。 | 结果在三种模型和四个机器人基准上平均成功率达 76.2%，单张图还能跨语言提示迁移。 |

## Red-Teaming 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-07 | Resource Consumption Red-Teaming for Large Vision-Language Models | benchmark、VLM DoS、2D VLM、resource red-teaming | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.18053) | 暂未公开 | 针对资源红队忽略视觉输入攻击面 | 论文提出 RECITE | 以像素级优化扰动诱导 LVLM 重复生成 | 结果将响应延迟提升 26 倍以上并显著增加 GPU 利用率和显存消耗。 |
