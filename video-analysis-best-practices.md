# 视频内容解析最佳实践

## 核心原则

视频解析的关键是**多模态融合**：结合视觉（帧）、音频（语音/字幕）、元数据三个维度，才能获得完整的内容理解。

---

## 1. 帧提取策略

### 1.1 智能采样（推荐）

**场景变化检测** - 只提取内容变化的关键帧：
```bash
ffmpeg -i video.mp4 -vf "select=gt(scene\,0.3)" -vsync vfr -frames:v 20 frame_%03d.jpg
```
- `scene > 0.3` 表示场景变化超过30%时提取
- 适合：讲解类、演示类视频

**均匀采样** - 按固定间隔提取：
```bash
ffmpeg -i video.mp4 -vf "fps=1/2" frame_%03d.jpg  # 每2秒一帧
```
- 适合：内容变化平缓的视频

### 1.2 采样密度建议

| 视频类型 | 建议采样率 | 帧数 |
|---------|-----------|------|
| 短视频 (<1分钟) | 每2-3秒 | 10-20帧 |
| 中等视频 (1-10分钟) | 每5-10秒 | 20-50帧 |
| 长视频 (>10分钟) | 场景检测 + 关键时刻 | 30-100帧 |

### 1.3 帧质量优化

```bash
# 高质量 JPEG，缩放到合适尺寸
ffmpeg -i video.mp4 -vf "select=gt(scene\,0.3),scale=1280:-1" -q:v 2 frame_%03d.jpg
```

- 分辨率：1280px 宽度足够 AI 分析，节省 token
- 质量：`-q:v 2` 高质量，`-q:v 5` 中等质量

---

## 2. 音频/字幕提取

### 2.1 提取音频

```bash
ffmpeg -i video.mp4 -vn -acodec mp3 -ab 128k audio.mp3
```

### 2.2 语音转文字

**方案一：Whisper（推荐）**
```python
import whisper
model = whisper.load_model("base")  # 或 "small", "medium", "large"
result = model.transcribe("audio.mp3", language="zh")
print(result["text"])
```

**方案二：云服务 API**
- OpenAI Whisper API
- 阿里云语音识别
- 腾讯云语音识别

### 2.3 提取内嵌字幕

```bash
# 查看字幕流
ffprobe -i video.mp4 -show_streams -select_streams s

# 提取字幕
ffmpeg -i video.mp4 -map 0:s:0 subtitles.srt
```

---

## 3. 多模态 AI 分析

### 3.1 分析流程

```
视频 → 帧提取 + 音频提取 → 语音转文字 → 多模态 LLM 分析 → 结构化输出
```

### 3.2 GPT-4o / Claude 视觉分析

**发送帧图片给 AI：**
```python
import base64

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 构建消息
messages = [
    {"role": "system", "content": "你是视频内容分析专家。"},
    {"role": "user", "content": [
        {"type": "text", "text": f"这是视频的关键帧，视频文案是：{transcript}\n请分析视频内容。"},
        *[{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encode_image(f)}"}} 
          for f in frame_files[:10]]  # 限制帧数控制成本
    ]}
]
```

### 3.3 分析 Prompt 模板

```
你是视频内容分析专家。请根据以下信息分析这个视频：

## 视频信息
- 标题：{title}
- 作者：{author}
- 时长：{duration}秒
- 文案/字幕：{transcript}

## 关键帧
[附带的图片]

## 请输出：
1. **主题概述**（1-2句话）
2. **内容摘要**（3-5个要点）
3. **关键信息**
   - 提到的人物/品牌
   - 提到的数据/观点
   - 关键时间点
4. **内容类型**（教程/新闻/评测/娱乐/...）
5. **目标受众**
6. **情感基调**（正面/中性/负面）
7. **值得关注的点**
```

---

## 4. 优化建议

### 4.1 成本控制

- **帧数限制**：10-20帧通常足够，更多帧边际收益递减
- **分辨率**：1280px 或更小，不需要原始分辨率
- **detail 参数**：使用 `"detail": "low"` 可大幅降低 token 消耗

### 4.2 准确性提升

1. **结合文案**：视频文案/字幕是最重要的信息源
2. **关键帧选择**：场景变化检测比均匀采样更有效
3. **多轮分析**：先概览，再针对感兴趣的部分深入
4. **时间戳关联**：将帧与时间戳关联，便于定位

### 4.3 特殊场景处理

**纯讲解类（PPT/教程）：**
- 重点提取文字内容（OCR）
- 场景变化检测效果好

**快节奏剪辑（短视频）：**
- 提高采样密度
- 关注视觉元素变化

**访谈/对话类：**
- 音频转文字是核心
- 帧主要用于识别说话人

---

## 5. 工具推荐

| 工具 | 用途 | 特点 |
|-----|------|------|
| ffmpeg | 帧提取、音频提取 | 功能全面，命令行 |
| Whisper | 语音转文字 | 开源，多语言支持好 |
| GPT-4o | 多模态分析 | 视觉+文本理解强 |
| Claude 3.5 | 多模态分析 | 长文本处理好 |
| yt-dlp | 视频下载 | 支持多平台 |

---

## 6. 示例：完整分析流程

```bash
# 1. 下载视频
yt-dlp -o video.mp4 "视频链接"

# 2. 提取关键帧（场景检测，最多20帧）
ffmpeg -i video.mp4 -vf "select=gt(scene\,0.3),scale=1280:-1" -vsync vfr -frames:v 20 -q:v 2 frames/frame_%03d.jpg

# 3. 提取音频
ffmpeg -i video.mp4 -vn -acodec mp3 -ab 128k audio.mp3

# 4. 语音转文字
whisper audio.mp3 --language zh --output_format txt

# 5. 发送给 AI 分析（帧 + 文字）
```

---

## 参考资源

- [OpenAI Cookbook - GPT-4o Video Processing](https://cookbook.openai.com/examples/gpt4o/introduction_to_gpt4o)
- [Whisper 语音识别](https://github.com/openai/whisper)
- [FFmpeg 文档](https://ffmpeg.org/documentation.html)
