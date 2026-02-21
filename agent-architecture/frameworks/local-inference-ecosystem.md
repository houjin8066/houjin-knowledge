# 本地推理生态系统

> 更新时间: 2026-02-22

## 核心项目

### ggml / llama.cpp
- **定位**: 本地 AI 推理的事实标准
- **维护**: ggml.ai 团队（2026年2月加入 Hugging Face）
- **特点**: 高效、跨平台、消费级硬件可用

### 重要里程碑
- 2023: ggml.ai 成立，专注本地推理
- 2026-02: ggml.ai 加入 Hugging Face，确保长期可持续发展

## 技术栈

### 推理层
```
transformers (模型定义) 
    ↓ 
GGUF (量化格式)
    ↓
llama.cpp (推理引擎)
    ↓
本地硬件 (CPU/GPU/NPU)
```

### 完整 Ambient AI Pipeline（本地可运行）
- 实时语音转文字 (STT)
- 语义记忆系统
- 对话推理
- 文字转语音 (TTS)

## 为什么本地推理重要

### 隐私架构原则
> "Policy is a promise. Architecture is a guarantee."

云端处理的信任链问题：
- 当前隐私政策（可变）
- 员工访问权限
- 第三方供应商
- 政府传票
- 未来广告合作

本地推理 = 数据物理上无法离开设备

### 成本优势
- 一次性硬件投入
- 无按查询收费
- 无 API 限制

### 延迟优势
- 无网络往返
- 适合 always-on 场景

## 与智能体架构的关联

### 记忆系统
- 本地存储 = 隐私保护
- 参考 memory-layers 六层架构

### Token 优化
- 本地推理对 token 效率更敏感
- 参考 haribo-pattern 压缩策略

## 参考链接
- https://github.com/ggml-org/llama.cpp
- https://huggingface.co
- https://github.com/ggml-org/llama.cpp/discussions/19759
