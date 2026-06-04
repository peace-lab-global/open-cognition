# Open Cognition · LOGO 资源

> 与项目主视觉一致的标识系统。所有资源均基于 SVG 矢量绘制，可无损放大。

---

## 文件清单

| 文件 | 用途 | 尺寸 |
|---|---|---|
| `logo-mark.svg` | **主标识**（彩色，透明底），用于浅色背景 | 1024 × 1024 viewBox |
| `logo-mark-dark.svg` | 暗背景版本（自带深色圆角底） | 1024 × 1024 |
| `logo-mark-mono.svg` | 单色版本，用于印刷 / 水印 / 简化场景 | 1024 × 1024 |
| `logo-horizontal.svg` | 横版（mark + 中英文字 + 徽章） | 1600 × 480 |
| `logo-mark.png` / `@2x.png` | 主标识 PNG（1024 / 2048，透明底） | 1×/2× |
| `logo-mark-dark.png` / `@2x.png` | 暗背景版 PNG | 1×/2× |
| `logo-mark-mono.png` / `@2x.png` | 单色版 PNG | 1×/2× |
| `logo-horizontal.png` / `@2x.png` | 横版 PNG（米色底） | 1×/2× |
| `preview.html` | 可视化预览与下载页（在浏览器打开） | — |

---

## 视觉语义

- **一笔円相（ensō）** — 禅宗「一笔绘」传统，从右上起笔顺时针行至左上，开口偏右 ~12°。不圆满、不对称，呼应 *Open* Cognition 中「开放」的深层含义：思想永远留有缺口，永远未完成。
- **朱金顿悟点** — 位于円相顶部开口处（`#c9a23a` 渐变），小而内敛，是整幅画面唯一的彩色。象征跨学科对话中涌现的「顿悟」，亦是「心印」的视觉化。
- **留白** — 大面积宣纸色空白不是「空」，而是「无限可能」。禅画以留白为最高表达，wabi-sabi 美学：少即是多。
- **墨晕滤镜** — 通过 SVG feTurbulence + feDisplacementMap 模拟宣纸上墨迹的自然晕散（baseFrequency=0.014，scale=3.2）。
- **红色落款章「印」** — 横版右下角的传统签名章（`#b23a2e`），禅意书法作品的最后一笔，表达「以心印心」。

## 配色

```
墨 INK       #1A1A1A   主线条 / ensō 笔触
宣纸 PAPER   #F5F0E5   背景（暖宣纸色）
朱金 GOLD    #C9A23A   顿悟点（渐变 #F0D588 → #8B6A1E）
夜墨 NIGHT   #12100D   暗色版背景（深棕宣纸）
印泥 SEAL    #B23A2E   横版落款章
米白墨 CREAM #F0E8D2   暗色版 ensō 笔触
```

## 字体

- **中文标题**：Ma Shan Zheng（首选） → STKaiti / Kaiti SC / Songti SC 书法风 fallback
- **英文小字**：Inter 400 / Helvetica Neue
- **横版 tagline**：Songti SC / STSong / SimSun 衬线 fallback

横版 SVG 已使用 macOS 系统字体作为 fallback，离线渲染也能保持稳定的书法美学。

---

## 使用规范

### 推荐场景

- `logo-mark` — 浅色背景上的标准用法（README、网站、文档头图）
- `logo-mark-dark` — 深色背景（暗色信息图、视频片头、夜间模式）
- `logo-mark-mono` — 单色印刷、水印、简陋显示场景
- `logo-horizontal` — Banner、PPT 封面、出版物封底、社交媒体页头

### 最小尺寸

| 形态 | 屏幕 | 印刷 |
|---|---|---|
| Mark | 48 × 48 px | 12 mm |
| Horizontal | 宽 ≥ 320 px | 宽 ≥ 80 mm |

### 安全留白

四周保留 ≥ 1 个节点直径（约 mark 半径的 1/4）的空白，不与正文文字或图片紧贴。

### 禁止事项

- ✗ 改变 ensō 的开口方向或闭合圆环（「开放」是核心隐喻）
- ✗ 拉伸/扭曲比例
- ✗ 在 logo 内部加阴影 / 外发光 / 浮雕
- ✗ 将朱金顿悟点改为其他颜色
- ✗ 移除横版的红色落款章「印」
- ✗ 在 ensō 内部添加额外装饰元素（留白是设计的一部分）

---

## 在 Markdown 中引用

```markdown
<p align="center">
  <img src="./meta/logo/logo-horizontal.svg" alt="Open Cognition" width="640">
</p>
```

或纯标识：

```markdown
<img src="./meta/logo/logo-mark.svg" alt="OC" width="64">
```

---

## 重新生成 PNG

PNG 由 Chrome headless 从 SVG 渲染生成。如需重新生成（如修改 SVG 后）：

```bash
bash meta/logo/_render.sh
```

需要 macOS + Google Chrome.app。脚本会输出 1× / 2× 两套 PNG。

---

## 源文件维护

LOGO 基于禅宗「一笔绘」円相（ensō）设计，核心参数：

- **viewBox**：1024 × 1024
- **ensō 路径**：单条 cubic Bezier，顺时针从右上（~15°）到左上（~27°），开口偏右 ~12°
- **stroke-width**：22（纤细毛笔质感）
- **顿悟点**：cx=528 cy=178 r=26（顶部开口中央偏右）
- **墨晕滤镜**：feTurbulence(baseFrequency=0.014, numOctaves=2, seed=7) + feDisplacementMap(scale=3.2)
- **横版**：viewBox 1600 × 480，mark 缩放 0.35，中文标题 font-size=120

---

## 许可

LOGO 资源遵循项目主许可 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)。允许在标注来源（"Open Cognition" + 仓库链接）的前提下自由使用、修改与分发。
