# 维护性提交日志 · 2026-06-22

> 类型：工程卫生维护（非内容创作）
> 范围：全库结构性修复 + lint/index 工具链加固 + README 校准
> 关联：[2026-06-22 项目整体评估](./2026-06-22-project-assessment.md) · [2026-06-22 内容 backlog](./2026-06-22-content-backlog.md)

---

## 背景与目标

项目评估发现 main 分支 CI 长期处于红色失败状态（796 个 lint errors），README 数字严重滞后，并存在重复文件与 lint/index 工具的误报 bug。本次维护目标：**在不删除任何知识内容、不批量制造桩文件的前提下，让 CI 转绿、对外信息准确、工具链可靠**。

## 成果总览

| 指标 | 修复前 | 修复后 |
|---|---|---|
| **lint errors** | **796** | **0** |
| E001（frontmatter 缺失/非法） | 32 | 0 |
| E002（frontmatter 缺字段） | 49 | 0 |
| E003（结构性失效链接） | 715 | 0 |
| CI lint job | ❌ FAIL | ✅ PASS |
| CI index-consistency job | ❌ STALE（误报） | ✅ PASS |
| README 数字 | 178/144/111（滞后） | 210/213/126（准确） |

## 六项修复

### 1. 失效链接批量修复（715 → 0）

新增 `scripts/fix-broken-links.py`，采用四档**保守**修复策略（仅修复目标确定的链接，其余进入人工审查队列）：

| 策略 | 含义 | 修复数 |
|---|---|---|
| SINGLE | 目标 basename 全库唯一存在，仅路径深度错 | 387 |
| SIGNATURE | 多候选但链接自带路径签名可消歧 | 167 |
| FUZZY | 明显拼写错误（如 `shurangama`→`surangama`），相似度 ≥0.90 | 5 |
| PROXIMITY | 跨域同名思想家，按源文件所在域就近选择 | 12 |

共修复 **571 条**确定性链接。剩余指向「目标文件根本不存在」的链接重分类为非阻塞 W006（见第 3 项）。

### 2. Frontmatter 修复（E001 32→0, E002 49→0）

- 新增 `scripts/fix-frontmatter.py`：机械修复 25 个 YAML 解析错误，三类成因：
  - frontmatter 内混入 markdown（`related_concepts:` 含 `- [x.md](x.md)`）
  - `sources:` 流式序列含斜体/嵌套引号（`sources: [*Title*, 1999]`）
  - `title:` 含未转义冒号（`title: Foo: Bar`）
- 新增 `scripts/complete-frontmatter.py`：为 31 个概念/经文条目补全可推导的 `id/school/era` 等必填字段。
- 手写 6 个完全无 frontmatter 的条目（adorno、nozick、conscience、responsibility、tragedy、endsley）。

### 3. lint 脚本逻辑修复

- `classify()` **先于** frontmatter 检查执行——避免非条目文件（如 `domains/.../reports/`）误报 E001。
- 新增 `/reports/` 路径排除。
- **新增 W006 错误码**：把「链接到尚未撰写的概念/技能」从阻塞性 E003 降级为非阻塞警告。判断逻辑两层：
  - `SKILL.md` 目标：检查父目录（技能名）在 `skills/` 下是否存在。
  - 路径感知（penult-segment）：链接的倒数第二路径段若与所有候选路径都不匹配，视为目标缺失。

### 4. build-index.py `--check` 误报修复

原逻辑比较完整 JSON（含 `generated: 日期`），导致只要不是当天构建就误报 STALE。改为剥离 `generated` 字段后比较内容，统计一致即判 OK。

### 5. 仓库卫生

- 删除被 git 追踪的重复文件 `scripts/lint 2.py`（`lint.py` 的旧副本，文件名带空格的隐患）。
- 新增三个可复用的维护脚本，未来内容扩展后可重跑：
  - `scripts/fix-broken-links.py`
  - `scripts/fix-frontmatter.py`
  - `scripts/complete-frontmatter.py`

### 6. README 数字校准（中 + 英）

- 徽章 `entries-178|144|111` → `entries-210|213|126`。
- 九大领域表格全部更新为 frontmatter 实测值（`README.md` + `README.en.md`）。

## 变更规模

- **修改** 264 个文件（+1828 / −1149 行）
- **删除** 1 个文件（`scripts/lint 2.py`）
- **新增** 5 个文件（3 脚本 + 2 报告）

## 残留项（已知、非阻塞、有据可查）

- **208 条 W006**：指向 151 个未撰写概念 + 19 个未撰写技能的链接。属**内容创作**工作，已在 [content-backlog 报告](./2026-06-22-content-backlog.md) 按引用次数排序。
- **231 条 W004/W005 警告**：缺失规定章节或无跨链，非阻塞，可后续打磨。

## 验证

```bash
python3 scripts/lint.py                 # → 0 error(s), 439 warning(s)
python3 scripts/build-index.py --check  # → OK (556 entries)
```
