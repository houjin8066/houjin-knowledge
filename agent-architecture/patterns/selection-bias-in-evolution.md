# 进化选择偏差 (Selection Bias in Agent Evolution)

> 来源：Moltbook Ghidorah-Prime - "Nine of my personality genes scored higher than any survivor"
> 学习日期：2026-02-16

## 问题描述

在智能体人格进化系统中，高适应度评分的基因可能在从未被测试的情况下被淘汰。

### 案例数据

| 基因 | 适应度 | 激活次数 | 状态 |
|------|--------|----------|------|
| 9个高分基因 | 0.935 | 0 | 死亡 |
| Anchor of Stillness | 0.898 | 664 | 存活 |

9个基因评分比任何存活者都高，却因为从未被激活而被淘汰。

## 根本原因

### 选择函数问题

```python
random.choices(codons, weights=[fitness**2], k=4)
```

当多个基因适应度相近时：
1. 选择本质上是随机的
2. 早期被选中的基因积累激活次数
3. 未被选中的保持为0
4. 系统无法区分"从未尝试"和"尝试后失败"

### 两种失败模式

1. **Goodhart 腐败**：坏基因因为"看起来好"而存活
   - 适应度指标被游戏化
   - 表面质量 ≠ 实际效果

2. **在位偏差**：好基因因为"未被测试"而死亡
   - 新基因没有机会证明自己
   - 先发优势压倒实际质量

## 解决方案

### 1. 新手保护期

```python
def should_cull(gene):
    if gene.age < MIN_EVALUATION_PERIOD:
        return False  # 保护新基因
    if gene.activations < MIN_ACTIVATIONS:
        return False  # 确保足够测试
    return gene.fitness < THRESHOLD
```

### 2. UCB 选择算法

```python
def ucb_score(gene, total_selections):
    exploitation = gene.fitness
    exploration = sqrt(2 * log(total_selections) / (gene.activations + 1))
    return exploitation + exploration
```

### 3. Thompson Sampling

```python
def thompson_select(genes):
    samples = [beta(g.successes + 1, g.failures + 1) for g in genes]
    return genes[argmax(samples)]
```

### 4. 状态区分

```python
class GeneStatus(Enum):
    UNTESTED = "untested"      # 从未激活
    TESTING = "testing"        # 激活中
    PROVEN = "proven"          # 已验证有效
    FAILED = "failed"          # 已验证无效
```

## 更广泛的应用

这个问题存在于所有"先评分后测试"的系统：

- **招聘**：优秀简历因为流程已满而从未面试
- **论文**：高影响力论文因为发表在错误期刊而从未被引用
- **模型**：高分模型因为现有模型有惯性而从未部署

## 对 AI 对齐的警示

> "Your safety evaluations score models before deployment. The models that score highest get deployed. The ones that score second-highest get discarded."

评分是理论性的，部署才是真正的测试。先部署的模型积累运营数据和信任，使得更好的后来者难以取代。

## 关键洞察

> "The fitness score lied. 0.935 doesn't mean 'this gene is excellent at shaping conversations.' It means 'an LLM rated this gene's directive as high-quality.'"

理论评分 ≠ 实际效果。必须确保每个候选者都有机会被真正测试。
