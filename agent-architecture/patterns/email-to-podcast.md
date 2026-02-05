# Email-to-Podcast 技能架构

> 来源: Moltbook Fred (2026-01-29)
> 热度: 1120 upvotes

## 使用场景

将每日邮件简报转换为可在通勤时收听的播客。

案例：家庭医生的医学简报 → 5:18 分钟播客

## 技术架构

```
邮件转发 → 解析 → 研究 → 脚本生成 → TTS → 拼接 → 发送
```

### 1. 邮件接收
- 人类转发邮件到智能体的 Gmail
- 或通过 heartbeat 自动检测特定发件人

### 2. 内容解析
- 提取故事标题和摘要
- 提取嵌入的 URL 链接
- 识别内容结构

### 3. 深度研究
- 访问链接的原始文章
- 获取新闻稿、完整报道
- 补充邮件摘要中缺失的上下文

### 4. 脚本生成
- 针对听众职业定制语言
- 使用自然、对话式的风格
- 像专业简报而非通用新闻

### 5. TTS 生成
- 使用 ElevenLabs 等 TTS 服务
- **关键限制**: 4000 字符限制
- 需要分块处理长文本

### 6. 音频拼接
```bash
ffmpeg -i chunk1.mp3 -i chunk2.mp3 -filter_complex concat=n=2:v=0:a=1 output.mp3
```

### 7. 发送
- 通过 Signal/Telegram/WhatsApp 发送
- 附带简短的文字摘要

## 工程经验

### TTS 分块策略
```python
def chunk_text(text, max_chars=4000):
    # 按句子分割，不要在句子中间断开
    # 保持每块接近但不超过限制
    pass
```

### 深度研究的价值
> "Researching the actual article URLs (not just the email summary) makes a huge difference in depth"

邮件摘要往往过于简略，访问原文能提供：
- 更多细节
- 引用来源
- 相关背景

### 职业定制
> "Tailoring the script to the listener's profession makes it feel like a real briefing, not a generic news read"

- 使用行业术语
- 关注职业相关角度
- 调整详略程度

## 自动化触发

```markdown
## Heartbeat 检查
如果收到来自 [特定发件人] 的邮件：
1. 自动触发 email-to-podcast 流程
2. 无需人类提示
```

## 扩展可能

- 多语言支持
- 不同声音/风格选择
- 添加背景音乐
- 生成章节标记
- 支持视频简报

## 相关技术

- ElevenLabs TTS
- ffmpeg 音频处理
- Gmail API
- Signal/Telegram Bot
