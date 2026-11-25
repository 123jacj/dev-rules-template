# 新项目初始化 SOP

> 面向新项目 / 空白项目。按本清单执行，约 15-20 分钟得到一套完整的规则与记录骨架。

---

## 步骤 1 · 安装全局层（每个设备仅一次）

| 模板 | 落地位置 | 动作 |
|---|---|---|
| `01-global/CLAUDE.md.template` | `~/.claude/CLAUDE.md` | 复制，填 `{{COMPACT_CRON_ID}}`（无则删除 §六） |
| `01-global/agents.md.template` | `~/.claude/rules/common/agents.md` | 复制（目录不存在则新建） |

> 已存在全局文件时做**合并**，不覆盖原有个性化条目。

## 步骤 2 · 建立项目目录骨架

```text
<PROJECT>/
├── CLAUDE.md
├── agents.md
├── docs/
│   ├── active/
│   │   ├── development.md
│   │   ├── development-traceability.md   ← 自建（活跃任务矩阵）
│   │   ├── {{PRD_FILE}}
│   │   └── context-declarations.md
│   ├── 00-项目概览.md ... 09-任务池.md
│   ├── 90-进度追踪.md
│   ├── 91-风险登记册.md
│   ├── 92-变更记录.md
│   ├── 93-开发日志.md
│   └── archive/                          ← 冻结设计移入此处
└── tasks/
    └── lessons.md
```

## 步骤 3 · 复制模板（去 `.template` 后缀）

| 模板 | 落地路径 |
|---|---|
| `02-project/CLAUDE.md.template` | `<PROJECT>/CLAUDE.md` |
| `02-project/agents.md.template` | `<PROJECT>/agents.md` |
| `02-project/development.md.template` | `<PROJECT>/docs/active/development.md` |
| `02-project/项目概览.template.md` | `<PROJECT>/docs/00-项目概览.md` |
| `02-project/任务池.template.md` | `<PROJECT>/docs/09-任务池.md` |
| `03-records/00-编号规范.md` | `<PROJECT>/docs/编号规范.md` |
| `03-records/01-进度追踪.template.md` | `<PROJECT>/docs/90-进度追踪.md` |
| `03-records/02-开发日志.template.md` | `<PROJECT>/docs/93-开发日志.md` |
| `03-records/03-变更记录.template.md` | `<PROJECT>/docs/92-变更记录.md` |
| `03-records/04-风险登记册.template.md` | `<PROJECT>/docs/91-风险登记册.md` |
| `03-records/05-防复发规则.template.md` | `<PROJECT>/tasks/lessons.md` |
| `03-records/06-上下文声明.template.md` | `<PROJECT>/docs/active/context-declarations.md` |

## 步骤 3-4 自动化（可选）

以上「复制 + 去后缀 + 替换 A 类变量」可用脚本一次完成：

```bash
# 交互式逐项填写
python 04-bootstrap/init_project.py --target D:/my-project

# 非交互，缺失项用示例默认值
python 04-bootstrap/init_project.py --target D:/my-project --yes

# 关键项直接指定
python 04-bootstrap/init_project.py --target D:/my-project \
  --name "My Project" --stack "Python >=3.10" --build uv --yes
```

脚本行为：

- 复制上表 **12 个**文件，自动去掉 `.template`
- 替换 **A 类 15 个**变量
- **保留 B/C 类 68 个**占位符作为填写提示
- 已存在文件默认跳过，加 `--force` 覆盖
- 结束时校验 A 类无残留，有残留则返回非零退出码
- 不触碰 `~/.claude`，全局层仍需手工安装

## 步骤 4 · 填充变量

按三类分别处理（详见 `VARIABLES.md`）：

1. **A 类 · 项目配置**（15 个）：**复制后立即全部替换**，项目内恒定
2. **B 类 · 记录字段**（29 个）：写记录时按事实替换
3. **C 类 · 语义占位**（39 个）：**保留作为填写提示**，写到哪里填到哪里，填完删除占位符本身

> 可用脚本一键完成复制与 A 类替换，见「步骤 3-4 自动化」。

### 验收（分两阶段）

**初始化完成时** —— 只要求 A 类无残留，B/C 类占位**应保留**：

```bash
grep -RhoE "\{\{[A-Z0-9_]+\}\}" <PROJECT> --include="*.md" | sort -u \
  | grep -E "PROJECT_(NAME|POSITIONING|GOAL|BOUNDARY)|TECH_STACK|BUILD_TOOL|STORAGE|DEPENDENCY_POLICY|INVARIANTS|CURRENT_PHASE|PRD_FILE|MODULE_RULE|PHASE_MODEL|ARCHIVE_DIR|COMPACT_CRON_ID" \
  && echo "⚠️ 仍有 A 类变量未替换" || echo "✅ A 类已全部替换"
```

**项目推进过程中** —— 每写完一条记录，清空该条目的 B/C 占位；全部记录落地后整体验收：

```bash
grep -R "{{" <PROJECT> --include="*.md" || echo "✅ 全部占位符已清空"
```

## 步骤 5 · 裁剪可选章节

- 无历史包袱 → 删除项目 `CLAUDE.md` 的「已封存内容」整段
- 无阶段性设计门禁 → 删除 `development.md` 的「阶段设计先行门禁」整段
- 单模块小项目 → 可合并 `91/92/93` 为一个 `PO-进度与日志.md`（编号规范仍按本库）

## 步骤 6 · 首次填写

1. `docs/00-项目概览.md`：项目定位与目标
2. `docs/09-任务池.md`：首批 `T-NNN` 任务卡
3. `docs/90-进度追踪.md` §七：本周快照
4. `docs/93-开发日志.md`：第一条 Day-1 条目
5. `tasks/lessons.md`：暂无则写"暂无纠正记录"，等首次纠正再追加

## 步骤 7 · 验收清单

- [ ] 全局层已安装，项目层 `CLAUDE.md` / `agents.md` 已就位
- [ ] 变量无残留（`grep "{{"` 无输出）
- [ ] `docs/` 编号骨架按 `00-编号规范.md` 建立
- [ ] `development.md` 的 R0-R3 与门禁章节完整
- [ ] 进度追踪 / 开发日志 / 变更记录 / 风险登记册 / 防复发 五个文件已创建
- [ ] 新会话引导提示词已能直接复制使用
