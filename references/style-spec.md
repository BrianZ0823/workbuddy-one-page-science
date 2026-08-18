# 模板 01 · 风格规格（Poster Style Spec）

> **2026-08-17 17:40 真实模板源**：从文章 https://mp.weixin.qq.com/s/36_d-VsyDen5rcf7RRVlsg 下载了 2 张**真实配图**（cover-1.png 1086×1448、cover-2.png 1024×1536），并做了像素级分析。**模板01 的真实形态**：单张近正方形封面图（1:1.33-1.5），不是8 张子图拼长卷；上下分层：顶部暖米装饰带 + 中部浅米白主区 + 底部暖色便签/落款区。
> 早期版本（基于「1170×7687 长卷便签」猜测）已被推翻——那个参考图实际上不是模板，而是8 张子图的无缝合并。
> 详见末尾「真实模板源」一节。

## Identity

- **Archetype:** illustration-led（手绘插画主导）+ editorial-grid（信息卡片网格）
- **Purpose:** concept / cultural（AI 科普知识卡片）
- **One-line design thesis:** 用"手账本"的温柔手绘感，把硬核概念拆成可一口吞下的小卡片，降低学习压迫感。

## Canvas and layout

- Aspect ratio: 竖版 3:4 ~ 9:16，适合手机端飞书阅读（测试稿用 800×1200）。
- Outer margin: 约画布宽 6%。
- Grid family: modular（模块化卡片网格），2 列 sticker-note 布局。
- Primary zones:
  - 顶部 18%：washi-tape 标题带 + 主标题
  - 中部 62%：6-8 张手账卡片网格
  - 底部 12%：金句高亮框
  - 最底 8%：来源/模板落款
- Visual center: 偏上，标题与首卡构成视觉锚点。
- Negative-space map: 卡片之间留白均匀，单卡内文字不顶边。
- Reading path: 左上标题 → 蛇形读卡 → 底部金句 → 落款。
- Density map: 中高密度（卡片多但单卡信息轻）。

## Typography system

- Main-title category: 手写体 / 马克笔感（中文用 ZCOOL KuaiLe / 站酷快乐体，退化用微软雅黑加粗）。
- Weight: 标题 bold，卡片标题 semibold，正文 regular。
- Alignment: 标题居中，卡片内左对齐。
- Chinese/Latin: 中文为主，英文术语保留原样（如 Skills / RPA）。
- Subtitle and microcopy: 小一号灰色，承载"作者/日期"。
- Text/image overlap: 卡片为独立浮层，不与插画重叠，保持清爽。

## Hero visual system

- Hero category: type-as-image + 轻量 emoji/图标（非写实人物）。
- Medium: 扁平手绘插画风（flat hand-drawn），圆角、粗描边、低饱和。
- Count: 每卡 1 个图标 + 1 个标题 + 1 行说明。
- Layering: 卡片浮于纸纹背景之上，带轻微投影模拟"贴纸"。
- Treatment: 纸感、蜡笔/马克笔质感，非照片。

## Color system

- Background: 暖米白 `#FFF9F2`（纸感）。
- Dominant: 卡片白 `#FFFFFF` 浮于米底。
- Accent palette（多色但不刺眼）:
  - 珊瑚红 `#FF6B6B`
  - 薄荷绿 `#6BCB77`
  - 天空蓝 `#4D96FF`
  - 暖黄 `#FFD93D`
- Approximate area ratio: `70% 米白底 + 25% 白卡 + 5% 彩色强调`。
- Temperature: 暖调为主，强调色冷暧交替。
- Highest-contrast accent: 出现在卡片图标与标题下划波浪线。

## Graphic language

- Borders: 卡片用 2px 圆角描边 + 虚线 option。
- Shape style: 圆角矩形（sticker-note），部分卡片轻微旋转 ±1.5° 模拟手贴。
- Decoration: washi-tape 斜条、虚线分隔、小星点、波浪下划线。
- Symmetry: 非对称，卡片大小略错落。

## Surface, light, and finish

- Material cues: 纸张纹理（CSS 点阵/噪点）、贴纸投影。
- Lighting: 平光，无强烈阴影，柔和。
- Finish: handmade / 手账感，温暖、亲近、低商务感。

## Lock map

### Hard lock（丢一则不像同一套）
1. 竖版手机比例（3:4 ~ 9:16）
2. 暖米白纸感底 `#FFF9F2`
3. 模块化 sticker-note 卡片网格
4. 手写感主标题（马克笔体）
5. 每卡"1 图标 + 1 标题 + 1 行说明"结构
6. 底部金句高亮框
7. 最底来源/模板落款
8. 多色低饱和强调（珊瑚/薄荷/天空/暖黄轮换）

### Soft lock（可微调）
1. 卡片列数（2 列 ↔ 1 列长卡）
2. washi-tape 颜色与角度
3. 卡片旋转幅度
4. 图标风格（emoji ↔ CSS 绘制）
5. 装饰密度（星点/波浪线多少）

### Must replace（绝不沿用原图内容）
- 原图的 Harness / Agent / MCP 具体文案与示例产品名
- 原作者"老纪AI研习社"的水印与署名
- 原图的八张特定分镜构图
- 任何原图独有插画角色

## Prompt variables（可变槽）

- `[主题]`：本期一句话主题（≤ 12 字）
- `[主标题]`：完整标题
- `[副标题/作者]`：作者 · 日期
- `[卡片列表]`：N 张 {图标, 标题, 一行说明}
- `[金句]`：底部高亮一句话（≤ 20 字）
- `[来源]`：公众号名 / 链接
- `[模板编号]`：01 / 02 / …
- `[主色]`：强调色轮换起点
