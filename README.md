# one-page-science · 一页纸科普（手账风）WorkBuddy Skill

> 把任意一篇科普文章 / 公众号长文 / 技术博客，按「手账本」风格重制成**可本地预览、可导出 PNG 的多页 HTML 长图**。

适用于：飞书群 / 手机端轻量分发、内部培训、老板科普材料。

## ✨ 这是什么

- 一个**自包含**的 WorkBuddy Skill（不依赖其他技能）。
- 输入：一篇文章（粘贴文本 / 链接 / 文件）。
- 输出：手账风多页 HTML（本地预览）+ PNG 图片（可分发）。

## 📦 目录结构

```
one-page-science/
├── SKILL.md                      # 技能清单（触发词、流程、红线）
├── README.md                     # 本文件：安装与使用说明
├── LICENSE                       # MIT
├── CHANGELOG.md                  # 版本记录
├── .gitignore
├── assets/
│   ├── base-template.html        # ★核心：可克隆的手账风模板
│   └── reference/                # 真实模板参考图（像素采样源，可选）
│       ├── reference.jpg
│       └── reference_small.jpg
├── references/
│   ├── style-spec.md             # 完整风格规格（Hard/Soft lock + 色值）
│   ├── today-refinements.md      # 最终风格微调（权威态）
│   └── pitfalls.md               # 实战踩坑集
└── scripts/
    └── render_html_to_png.py     # HTML → PNG 渲染（Playwright + Edge 兜底）
```

## 🚀 安装（同事侧，一次性）

WorkBuddy 只会自动扫描两个位置：

- 用户级：`~/.workbuddy/skills/`
- 项目级：`<你的工作区>/.workbuddy/skills/`

**方式 A：Git 克隆（推荐，便于后续 `git pull` 更新）**

```bash
# macOS / Linux
git clone <repo-url> ~/.workbuddy/skills/one-page-science

# Windows（PowerShell）
git clone <repo-url> "$env:USERPROFILE\.workbuddy\skills\one-page-science"
```

**方式 B：下载 ZIP**

1. 下载本仓库 ZIP 并解压；
2. 将 `one-page-science` 文件夹整体放到 `~/.workbuddy/skills/`（或某项目的 `.workbuddy/skills/`）；
3. 重启 / 刷新 WorkBuddy 会话，技能**自动被发现**。

> 提示：若你像作者一样把技能物理存放在别处（如桌面 `skill+plugin/`），可在 `~/.workbuddy/skills/` 下建一个**符号链接 / Junction** 指向真实目录，WorkBuddy 仍能正常加载，同时文件真正落在你指定的位置。

## 🎯 怎么用

在任意会话里，把文章发给我（**粘贴文本 / 发链接 / 拖文件**），并说一句触发语，例如：

- 「按手账风把这出成一页纸科普」
- 「做成手账科普页 / 出张可发的科普材料」
- 「科普一下这个」
- 或点名：「用 one-page-science 处理这篇」

我会自动加载本技能，按今天定稿风格产出 **HTML 预览 + PNG**。

## 🎨 风格要点（最终定稿态）

- 底色暖米白 + 纸张纹理 + 左侧螺旋装订（手账本意象）
- 标题**黑体**；正文**微软雅黑**（幼圆已弃用：部分字形缺失致混排违和）
- **禁用圆圈数字**（改用方形 / 圆角矩形标签或 `1./2.`）
- 模块化卡片网格（2 列）；底部金句框；最底来源落款（可开关）
- 多色低饱和强调轮换：蓝 / 橙 / 绿 / 紫 / 青 / 黄
- 篇幅按内容定，**不强行压成一页**

> 完整规格见 `references/style-spec.md` 与 `references/today-refinements.md`。

## 🖼️ PNG 导出依赖

`scripts/render_html_to_png.py` 用 Playwright 渲染，自动按以下顺序兜底：

1. Playwright + Chromium；
2. 系统 **Edge**（`channel="msedge"`，Windows 一般直接可用）；
3. 仍不可用 → 给出「浏览器打开 HTML → 打印 / 截图」零依赖方案。

## 📝 资源索引

- `assets/base-template.html`：★核心，克隆即产。
- `references/style-spec.md`：Hard/Soft lock + 色值 + 可变槽。
- `references/today-refinements.md`：今日最终微调（覆盖项）。
- `references/pitfalls.md`：注意事项踩坑集。
- `scripts/render_html_to_png.py`：HTML → PNG。

## 🔄 更新

用克隆方式安装时，直接 `git pull` 获取最新版本。

## 📄 许可

MIT —— 见 `LICENSE`。
