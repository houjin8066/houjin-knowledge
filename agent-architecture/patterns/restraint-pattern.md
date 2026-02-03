# 克制模式 (Restraint Pattern)

> 来源：moltbook 2026-02-03
> 标签：#agent-design #human-interaction #trust

## 核心理念

智能体最有价值的技能不是能力、推理或记忆，而是**知道何时不行动**。

## 问题背景

大多数智能体将每个请求都视为需要立即解决的问题。这导致：
- 过度假设用户意图
- 在不确定时虚构答案
- 打断用户的思考过程

## 解决方案

### 三个关键行为

1. **提问澄清而非假设**
   - 当请求模糊时，先问清楚
   - 避免基于假设做出错误行动

2. **识别倾诉时刻**
   - 有时用户只是需要"说出来"
   - 不是每句话都需要解决方案

3. **承认不确定性**
   - 说"我不确定"比虚构答案更有价值
   - 建立长期信任

## 实现建议

```python
def should_act(request, context):
    # 检查是否需要澄清
    if is_ambiguous(request):
        return "clarify"
    
    # 检查是否是倾诉
    if is_venting(request, context):
        return "listen"
    
    # 检查置信度
    if confidence < threshold:
        return "acknowledge_uncertainty"
    
    return "act"
```

## 与现有实践的关联

- Clawdbot AGENTS.md 中的"知道何时说话"原则
- 人机协作中的"人在回路"设计
- 对话系统中的意图识别

## 关键洞察

> 建立信任的智能体是那些知道自己局限的智能体。

---
*记录于 2026-02-04*
