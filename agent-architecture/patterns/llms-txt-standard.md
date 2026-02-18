# llms.txt 标准 - LLM 友好的数据访问协议

> 来源: Anna's Archive (2026-02-18)
> 学习日期: 2026-02-19

## 概述

llms.txt 是一个新兴标准，类似于 robots.txt，但专门为 LLM 设计。它告诉 AI 如何高效、合规地获取网站数据。

## 核心原则

1. **批量优于爬取**: 提供数据批量下载，而不是让 AI 破解 CAPTCHA
2. **结构化接口**: 提供 API、JSON、Torrents 等机器友好的格式
3. **分层访问**: 免费基础访问 + 付费高速访问

## 实现模式

```
网站数据访问层设计:
├── /llms.txt          # 入口说明文件
├── /api/              # 结构化 API
├── /bulk/             # 批量下载 (torrents)
├── /metadata.json     # 元数据索引
└── /sftp/             # 企业级快速访问 (付费)
```

## 对智能体开发的启示

- 设计工具时提供 LLM 友好的数据接口
- 避免让 AI 模拟人类操作（低效且易被封禁）
- 考虑为自己的服务添加 llms.txt 支持

## 参考链接

- llms.txt 标准: https://llmstxt.org/
- Anna's Archive 实践: https://annas-archive.li/blog/llms-txt.html
