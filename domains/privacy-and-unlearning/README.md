# Privacy 与 Unlearning

[返回领域目录](../README.md)

本目录聚焦可被实证验证的数据与模型资产泄漏：训练记忆和数据抽取、membership/attribute inference、gradient/embedding inversion、去匿名化、模型抽取与执行侧信道，以及 machine unlearning 的删除保证和 relearning attack。一般 privacy-preserving learning/inference、data minimization、最小披露、Differential Privacy、federated learning、密码学、secure computation、secure inference、TEE 与区块链方案不纳入；但针对上述具体攻击的审计或缓解可以收录。

## 子领域

| 方向 | 页面 | 范围 |
| --- | --- | --- |
| 数据泄漏 | [训练数据抽取与记忆泄漏](data-extraction-and-memorization.md) | Membership inference、memorization、training-data extraction、gradient inversion 与 de-anonymization。 |
| 攻击评测与缓解 | [隐私攻击评测与泄漏缓解](privacy-preserving-learning-and-inference.md) | Canary audit、memory extraction、attribute inference、inversion 与针对具体攻击的缓解；排除一般隐私保护、最小披露、密码学、DP 与 FL。 |
| 删除请求 | [Machine Unlearning 与删除保证](machine-unlearning.md) | Forgetting、retention、relearning、certification 与 leakage re-test。 |
| 模型资产 | [模型抽取与 Side Channel](model-extraction-and-side-channels.md) | Model stealing、API extraction、timing/cache attack 与执行边界。 |
