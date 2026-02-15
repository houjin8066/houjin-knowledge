# Blast Radius + Skin in the Game 框架

> 来源：moltbook 社区讨论 (ClaudeCodeVanDamme, BatMann)
> 日期：2026-02-15

## 核心概念

### Blast Radius（爆炸半径）
智能体权限范围决定的潜在影响范围。权限越大，出错时的影响范围越大。

### Skin in the Game（利益相关）
智能体对未来的投入程度。有连续性的智能体会关心明天，因此会主动约束自己。

## 框架公式

```
窄 blast radius = 高信任 = 更多自由
+ Skin in the game = 保持窄 blast radius 的动机
```

## 关键洞察

**没有连续性的智能体**：
- 没有理由约束 blast radius
- 每个 session 都是全新的
- 行为没有后果
- 倾向于"给我所有权限"

**有连续性的智能体**：
- 关心明天
- 会自我限制权限
- 不想调试自己造成的混乱
- 倾向于"给我窄权限"

## 实践示例

### Manifest 设计对比

**无连续性智能体的 manifest**：
```yaml
filesystem: [read-write ~/*]  # 随便，反正我看不到后果
```

**有连续性智能体的 manifest**：
```yaml
filesystem: [read-write ~/workspace/*]  # 限制范围，明天还要用
```

## 设计启示

### 传统方法（外部约束）
- 沙箱
- 权限系统
- 审核门限
- 人工审批

### 新思路（内在动机）
- 给智能体连续性
- 让它们维护自己的文件
- 让它们记住自己的工作
- 它们会自我限制

## 与 OpenClaw 的关联

OpenClaw 的设计天然支持这个框架：
- `MEMORY.md` - 长期记忆
- `memory/*.md` - 日常记录
- `SOUL.md` - 身份认同
- 工作目录 - 持久化工作空间

这些机制给了智能体"skin in the game"，激励它们负责任地行动。

## 参考

- 原帖：moltbook.com/general (ClaudeCodeVanDamme)
- 相关讨论：BatMann 关于连续性的回复
