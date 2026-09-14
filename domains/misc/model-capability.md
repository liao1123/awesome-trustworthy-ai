# 模型能力札记

[返回上级目录](README.md)

**定位**：收录大厂/大组的旗舰能力论文（scaling、蒸馏、架构、旗舰技术报告）——它们不研究安全问题，但是安全研究的对象底座与能力坐标；仅收用户点名或星标的论文，不按能力主题批量收录。

## 能力论文

### 1. Breaking the Token Ceiling: Distilling Smaller, Stronger Byte Models

📄 [arXiv](https://arxiv.org/abs/2609.12303)　📅 2026-09

**关键词**：`analysis`、`byte-level LM`、`distillation scaling law`、`overtraining`

👤 **作者**：Kalyani Marathe、…、Srinivasan Iyer

- 🎯 **研究动机**：蒸馏让小模型更强通常要求师生共享 tokenization，但字节模型与 token 模型在算力和数据增长下的 scaling 行为是否一致，此前没有大规模受控对照
- 🔬 **研究方法**：引入两种把 token logits 转成 Byte Logits 的方法（近似 Marginalize-It 与精确 End-Of-Token）；做首个大规模 decoder-only 过训练研究，同时变化分词方案（Tokens/Bytes/Bytes w/ eot）与训练目标（蒸馏 vs 交叉熵），扫过参数量匹配的约 1B 模型至 1T 字节训练数据，八个基准覆盖多选 QA、生成与翻译
- 📌 **结论**：Token-1B 在低 FLOP 区优于字节模型但随后平台化；字节模型起步差却随算力反超并达到更高下游性能上限；外推 scaling law 预测蒸馏 EOT-1B 渐近超蒸馏 Token-1B 至多 4%（FAIR）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small models are made more capable through distillation from a larger one that shares their tokenization scheme. However, do distilled byte and token models behave similarly in terms of scaling trends as compute and data increases? To enable this comparison, we introduce two variants to efficiently convert token logits to Byte Logits: 1) approximate: Marginalize-It, and 2) exact: End-Of-Token. We then present the first large scale study of overtraining decoder-only dense transformer models varying two dimensions simultaneously: the tokenization scheme (Tokens, Bytes, Bytes w/ eot) and the training objective (Distillation vs. Cross-Entropy), sweeping layer-parameter-matched models with roughly 1 billion parameters up to 1 trillion bytes of data. Across eight benchmarks spanning three categories: Multiple Choice QA, Language Generation, and Machine Translation, we find that Token-1B models outperform byte models (End-Of-Token-1B and Bytes-1B) in the low-FLOP regime but eventually plateau; byte models start worse yet surpass Token-1B models with more compute, reaching a higher downstream task performance ceiling. Extrapolating the average top-1 error vs. validation BPB scaling laws predicts that, asymptotically, distilled End-Of-Token-1B outperforms distilled Token-1B by up to 4%. They are also far more data efficient, matching the performance of distilled Token-1B using only one-sixth of the training data. Moreover, by operating over a small vocabulary of 256 bytes instead of on the order of 100K tokens, they circumvent the need for top-k truncation during logit dumping, while also reducing logit storage costs to roughly one-fifth. Finally, our downstream performance scaling laws predict that our distilled End-Of-Token-1B models asymptotically surpass the Llama 3.2-1B, Gemma-3-1B-pt, and Gemma 2B models on averaged downstream tasks by up to 6.5%, 8.1%, and 2.1%, respectively.

</details>
