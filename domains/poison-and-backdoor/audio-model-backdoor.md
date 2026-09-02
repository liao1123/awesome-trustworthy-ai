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

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers | attack、speech enhancement backdoor、clean audio trigger、content tampering | 未确认（arXiv Comments：Accepted at INTERSPEECH 2026. This is the author-accepted manuscript, not the ISCA proceedings camera-ready publisher version. 5 pages, 2 figures） | [arXiv](https://arxiv.org/abs/2608.30329) | 暂未公开 | 针对 speech enhancement 被动处理时无法假设攻击者会在推理阶段主动注入 trigger | Ouroboros 把模型理想 clean output 本身设为自然触发器 | 关键实现：Ouroboros 把模型理想 clean output 本身设为自然触发器。 | 未经修改的真实录音可近乎完美激活后门并定向篡改内容，同时维持正常增强性能，且常见 filtering 与 fine-tuning 未能消除攻击。 |
