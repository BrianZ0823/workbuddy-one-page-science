# Changelog

All notable changes to the `one-page-science` skill are documented here.

## [1.0.0] - 2026-08-18

### Added
- 初始发布：手账风「一页纸科普」WorkBuddy Skill（自包含，无外部依赖）。
- **风格最终定稿态**：标题黑体 + 正文微软雅黑（幼圆已弃用，部分字形缺失导致混排违和）；禁用圆圈数字（改用方形/圆角矩形标签或 `1./2.`）；便利贴与总结框并排不遮挡；来源落款可开关（默认保留）；篇幅按内容定、不强行压一页。
- 核心可克隆模板 `assets/base-template.html`（CSS 变量 + 占位结构 + 注释）。
- 参考资源：`references/style-spec.md`（完整风格规格：Hard/Soft lock + 色值 + 可变槽）、`references/today-refinements.md`（今日最终微调，权威态）、`references/pitfalls.md`（实战踩坑集）。
- `scripts/render_html_to_png.py`：HTML → PNG 渲染（Playwright，含系统 Edge 兜底与浏览器打印/截图降级方案）。
- 真实模板参考图 `assets/reference/reference.jpg` / `reference_small.jpg`（像素采样源）。

### Verified
- 已用《AI Agent 完整装备清单》跑通端到端：提炼内容契约 → 克隆模板填值 → 本地预览 → 导出 3 页 PNG（经系统 Edge 渲染成功）。
