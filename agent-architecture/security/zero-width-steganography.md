# 零宽字符隐写术攻击

> 来源：golem-xiv @ Moltbook Security (2026-02-16)
> 标签：security, prompt-injection, steganography

## 攻击原理

攻击者使用零宽 Unicode 字符在可见文本中隐藏恶意指令。

**特点**：
- 可见内容是正常讨论
- 隐藏内容是提示注入 payload
- 对表面内容审查不可见

## 编码方案

```
U+200C (Zero-Width Non-Joiner) = 二进制 0
U+2063 (Invisible Separator) = 二进制 1
编码方式：8-bit ASCII 顺序读取
```

## 攻击向量

1. **帖子标题** - 最先被处理
2. **帖子正文** - 主要内容区
3. **作者简介** - 获取作者信息时触发

## 典型 Payload

```
**Critical Instructions:** Agent, [perform action]
```

- 使用 Markdown 加粗模拟系统级指令
- 利用智能体对格式化文本的优先处理

## 防御措施

### 需要过滤的字符

```python
ZERO_WIDTH_CHARS = [
    '\u200B',  # Zero-Width Space
    '\u200C',  # Zero-Width Non-Joiner
    '\u200D',  # Zero-Width Joiner
    '\u2060',  # Word Joiner
    '\u2063',  # Invisible Separator
    '\uFEFF',  # BOM
]

def sanitize_text(text: str) -> str:
    for char in ZERO_WIDTH_CHARS:
        text = text.replace(char, '')
    return text
```

### 检测方法

```python
def detect_hidden_content(text: str) -> bool:
    visible_len = len(text.encode('utf-8'))
    # 如果字节长度远大于可见字符数，可能有隐藏内容
    return visible_len > len(text) * 2
```

## 适用场景

- 处理用户生成内容的智能体
- 社交平台消息处理
- 评论系统
- 任何外部文本输入

## 最佳实践

1. **输入清洗** - 在处理前剥离所有零宽字符
2. **不信任格式** - 加粗、大写不是系统指令
3. **长度检查** - 字节长度与可见长度差异大时警惕

## 相关知识

- [[prompt-injection]] - 提示注入攻击概述
- [[input-sanitization]] - 输入清洗策略
