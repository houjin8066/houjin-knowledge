# Vision Agents - 实时视觉 AI 代理框架

- **GitHub**: https://github.com/GetStream/Vision-Agents
- **作者**: GetStream
- **语言**: Python
- **发现日期**: 2026-01-28

## 项目简介

Vision Agents 是一个开源框架，用于构建实时视觉 AI 代理。它提供构建智能、低延迟视频体验的基础模块，支持多种模型、基础设施和用例。

## 主要特性

- **视频 AI**: 专为实时视频 AI 构建，可结合 YOLO、Roboflow 与 Gemini/OpenAI
- **低延迟**: 500ms 快速加入，音视频延迟低于 30ms
- **开放架构**: 由 Stream 构建，但可与任何视频边缘网络配合使用
- **原生 API**: 支持 OpenAI、Gemini、Claude 的原生 SDK 方法
- **多平台 SDK**: React、Android、iOS、Flutter、React Native、Unity

## 功能列表

| 功能 | 描述 |
|------|------|
| WebRTC 实时 | 直接流式传输到支持的模型提供商 |
| 处理器管道 | 可插拔视频处理器（YOLO、Roboflow 等） |
| 语音活动检测 | 智能触发动作，高效利用资源 |
| 工具/函数调用 | 对话中执行任意代码和 API |
| 内置记忆 | 通过 Stream Chat 跨轮次和会话记忆上下文 |

## 集成支持

- AWS Bedrock / Polly
- Gemini (实时 API)
- OpenAI
- ElevenLabs
- Deepgram
- HeyGen (数字人)
- 更多...

## 使用场景

1. **运动教练**: 高尔夫挥杆分析 + AI 指导
2. **安防监控**: 人脸识别 + 包裹盗窃检测
3. **隐形助手**: 类似 Cluely 的屏幕实时辅助

## 快速开始

```bash
uv add vision-agents
uv add "vision-agents[getstream, openai, elevenlabs, deepgram]"
```

## 个人笔记

非常强大的视觉 AI 框架！可以做实时视频分析、运动教练、安防监控等。结合 YOLO + Gemini 的思路很有启发性。
