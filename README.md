# Read Paper

这是一个以 Markdown 为核心的论文阅读仓库，用于收集待读论文、沉淀单篇笔记，并按研究主题建立长期可检索的知识索引。

## 仓库导航

| 位置 | 用途 |
| --- | --- |
| [inbox.md](inbox.md) | 快速收集尚未整理的论文链接 |
| [papers/README.md](papers/README.md) | 全部论文的唯一总索引 |
| [papers/](papers/) | 按论文发表年份保存阅读笔记 |
| [topics/README.md](topics/README.md) | 按研究主题串联论文 |
| [templates/paper-note.md](templates/paper-note.md) | 单篇论文笔记模板 |
| [assets/](assets/) | 保存笔记引用的图片和图表 |

## 记录流程

1. 看到感兴趣的论文时，先把链接放进 [inbox.md](inbox.md)。
2. 开始阅读时，将 [笔记模板](templates/paper-note.md) 复制到 `papers/<发表年份>/<第一作者>-<短标题>.md`。
3. 在 [论文总索引](papers/README.md) 中登记状态、主题、笔记和原文链接。
4. 阅读完成后补充主题索引，并提交一次聚焦于该论文的 Git commit。

## 阅读状态

| 状态 | 含义 |
| --- | --- |
| `queued` | 已收录，尚未开始 |
| `reading` | 正在阅读或整理 |
| `read` | 已完成一轮阅读 |
| `revisit` | 值得重读或需要补实验 |

## 约定

- 笔记文件名使用小写英文和连字符，例如 `vaswani-attention-is-all-you-need.md`。
- 一篇论文只在 [papers/README.md](papers/README.md) 登记一次，主题页只链接到该条笔记，避免维护重复信息。
- 仓库默认忽略 PDF。优先记录 DOI、arXiv 或出版社链接，以控制仓库体积并避免分发受版权保护的文件。
- 图片放在 `assets/<笔记文件名>/` 下，并使用相对路径引用。
