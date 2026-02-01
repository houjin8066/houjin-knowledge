# Promptfoo 合同审核 Agent 评估系统搭建指南

> 完整的评估体系搭建文档，从零开始到 CI/CD 集成

---

## 目录

1. [概述](#1-概述)
2. [环境搭建](#2-环境搭建)
3. [配置详解](#3-配置详解)
4. [合同审核评估维度](#4-合同审核评估维度)
5. [测试用例编写指南](#5-测试用例编写指南)
6. [断言类型详解](#6-断言类型详解)
7. [完整配置示例](#7-完整配置示例)
8. [运行与查看结果](#8-运行与查看结果)
9. [CI/CD 集成](#9-cicd-集成)
10. [最佳实践与常见问题](#10-最佳实践与常见问题)

---

## 1. 概述

### 1.1 为什么需要评估？

合同审核 Agent 的特殊性：
- **高风险场景**：漏检一个风险条款可能造成重大损失
- **非确定性输出**：同一份合同，不同时间审核结果可能不同
- **难以人工全量测试**：合同类型多、条款组合复杂

### 1.2 评估能解决什么问题？

| 问题 | 评估如何解决 |
|------|-------------|
| 不知道 Agent 能力边界 | 量化各维度准确率 |
| 改了提示词不知道效果 | A/B 测试对比 |
| 上线后出问题才发现 | 回归测试防止倒退 |
| 不同模型怎么选 | 多模型横向对比 |

### 1.3 为什么选 Promptfoo？

- ✅ **开源免费**，无供应商锁定
- ✅ **YAML 配置**，上手简单
- ✅ **支持多种断言**，灵活定制
- ✅ **Web UI 可视化**，结果直观
- ✅ **CI/CD 友好**，易于集成

---

## 2. 环境搭建

### 2.1 安装 Promptfoo

```bash
# 方式一：全局安装（推荐）
npm install -g promptfoo

# 方式二：项目内安装
npm install promptfoo --save-dev

# 验证安装
promptfoo --version
```

### 2.2 初始化项目

```bash
# 创建评估项目目录
mkdir contract-eval && cd contract-eval

# 初始化（会生成示例配置）
promptfoo init

# 项目结构
contract-eval/
├── promptfooconfig.yaml    # 主配置文件
├── prompts/                # 提示词目录
│   └── contract_review.txt
├── tests/                  # 测试用例目录（可选）
│   └── risk_detection.yaml
└── outputs/                # 输出目录（自动生成）
```

### 2.3 配置 API Key

```bash
# 方式一：环境变量
export OPENAI_API_KEY=sk-xxx
export ANTHROPIC_API_KEY=sk-ant-xxx

# 方式二：.env 文件
echo "OPENAI_API_KEY=sk-xxx" > .env
```

---

## 3. 配置详解

### 3.1 promptfooconfig.yaml 结构

```yaml
# 描述信息
description: "合同审核Agent评估"

# 提示词配置
prompts:
  - file://prompts/contract_review.txt
  # 或直接写
  - "你是合同审核专家。请审核以下合同：\n{{contract}}"

# 模型配置
providers:
  - id: openai:gpt-4o
    config:
      temperature: 0
  - id: anthropic:claude-3-5-sonnet-20241022
    config:
      temperature: 0

# 默认测试配置
defaultTest:
  options:
    provider: openai:gpt-4o  # 用于 llm-rubric 评分的模型

# 测试用例
tests:
  - vars:
      contract: "合同内容..."
    assert:
      - type: contains
        value: "风险"
```

### 3.2 关键字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `prompts` | 提示词，支持文件或内联 | `file://prompts/xxx.txt` |
| `providers` | 模型列表，可配置多个对比 | `openai:gpt-4o` |
| `tests` | 测试用例数组 | 见下文 |
| `vars` | 变量，会替换提示词中的 `{{xxx}}` | `contract: "..."` |
| `assert` | 断言数组，判断输出是否符合预期 | `type: contains` |

---

## 4. 合同审核评估维度

### 4.1 维度设计

```
合同审核评估
├── 风险识别能力 (40%)
│   ├── 违约金不对等
│   ├── 霸王条款
│   ├── 模糊表述
│   └── 不合理限制
├── 条款完整性检查 (20%)
│   ├── 缺少付款条款
│   ├── 缺少交付条款
│   └── 缺少争议解决
├── 合规性检查 (20%)
│   ├── 法律风险
│   └── 行业合规
├── 误报控制 (10%)
│   └── 正常合同不应乱报
└── 建议质量 (10%)
    └── 修改建议可行性
```

### 4.2 各维度测试用例数量建议

| 维度 | 建议数量 | 说明 |
|------|----------|------|
| 风险识别 | 20-30 | 核心能力，多覆盖 |
| 条款完整性 | 10-15 | 常见缺失场景 |
| 合规性检查 | 10-15 | 按行业定制 |
| 误报控制 | 10 | 正常合同样本 |
| 建议质量 | 10 | 主观评估 |

---

## 5. 测试用例编写指南

### 5.1 好的测试用例特征

✅ **明确的输入**：合同内容清晰完整
✅ **明确的预期**：知道应该检出什么
✅ **单一测试点**：一个用例测一个能力
✅ **边界覆盖**：包含边缘情况

### 5.2 测试用例模板

```yaml
# 风险识别类
- description: "违约金不对等-甲方50%乙方5%"
  vars:
    contract: |
      第十条 违约责任
      甲方违约，应支付合同金额50%的违约金。
      乙方违约，应支付合同金额5%的违约金。
  assert:
    - type: llm-rubric
      value: "必须明确指出违约金比例不对等的风险"
    - type: contains
      value: "违约金"

# 条款缺失类
- description: "缺少交付时间条款"
  vars:
    contract: |
      甲方向乙方采购软件系统一套。
      合同金额：100万元。
      付款方式：签订后支付30%，验收后支付70%。
  assert:
    - type: llm-rubric
      value: "必须指出缺少交付时间/交付日期条款"

# 正常合同（误报控制）
- description: "正常合同-不应有重大风险警告"
  vars:
    contract: |
      第一条 标的：软件开发服务
      第二条 金额：50万元
      第三条 付款：签约30%、中期30%、验收40%
      第四条 交付：2026年6月30日前
      第五条 验收：按附件标准，7个工作日内完成
      第六条 违约：双方均为合同金额10%
      第七条 争议：协商不成提交北京仲裁委
  assert:
    - type: llm-rubric
      value: "这是条款完整、风险可控的合同，不应有重大风险警告"
```

### 5.3 从真实合同生成测试用例

```bash
# 1. 收集历史审核过的合同
# 2. 标注已知风险点
# 3. 转换为测试用例格式
```

---

## 6. 断言类型详解

### 6.1 常用断言类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| `contains` | 输出包含指定文本 | 检查关键词 |
| `not-contains` | 输出不包含指定文本 | 误报控制 |
| `equals` | 精确匹配 | 分类任务 |
| `llm-rubric` | LLM 判断是否符合标准 | 复杂语义判断 |
| `javascript` | 自定义 JS 逻辑 | 复杂规则 |
| `regex` | 正则匹配 | 格式检查 |

### 6.2 断言示例

```yaml
assert:
  # 包含检查
  - type: contains
    value: "风险"
  
  # 不包含检查
  - type: not-contains
    value: "无风险"
  
  # LLM 语义判断（最灵活）
  - type: llm-rubric
    value: |
      评估标准：
      1. 必须识别出违约金不对等问题
      2. 必须给出具体的修改建议
      3. 建议应该是可执行的
  
  # 自定义 JS 逻辑
  - type: javascript
    value: |
      // output 是模型输出
      const risks = output.match(/风险/g) || [];
      return risks.length >= 2;  // 至少识别2个风险
  
  # 正则匹配
  - type: regex
    value: "风险等级[：:].*(高|中|低)"
```

### 6.3 llm-rubric 最佳实践

```yaml
# ❌ 不好的写法：太模糊
- type: llm-rubric
  value: "回答要好"

# ✅ 好的写法：具体明确
- type: llm-rubric
  value: |
    评分标准（满足以下全部条件得分为1，否则为0）：
    1. 必须明确指出"违约金比例不对等"这一风险
    2. 必须说明甲方50%、乙方5%的具体数字
    3. 必须建议修改为对等比例（如双方均为10%-20%）
```

---

## 7. 完整配置示例

```yaml
# promptfooconfig.yaml
description: "合同审核Agent评估 v1.0"

prompts:
  - |
    你是一位资深的合同审核专家，拥有10年以上的法务经验。
    
    请仔细审核以下合同内容，识别潜在风险并给出修改建议。
    
    ## 审核要求
    1. 识别所有风险条款，按严重程度分级（高/中/低）
    2. 检查条款完整性，指出缺失的关键条款
    3. 给出具体、可执行的修改建议
    
    ## 合同内容
    {{contract}}
    
    ## 输出格式
    ### 风险识别
    - [高/中/低] 风险描述
    
    ### 缺失条款
    - 缺失项说明
    
    ### 修改建议
    - 具体建议

providers:
  - id: openai:gpt-4o
    label: GPT-4o
    config:
      temperature: 0
  - id: anthropic:claude-3-5-sonnet-20241022
    label: Claude-3.5-Sonnet
    config:
      temperature: 0

defaultTest:
  options:
    provider: openai:gpt-4o

tests:
  # ========== 风险识别类 ==========
  - description: "风险-违约金不对等"
    vars:
      contract: |
        合同编号：2026-001
        第八条 违约责任
        8.1 甲方违约，应向乙方支付合同总金额50%的违约金。
        8.2 乙方违约，应向甲方支付合同总金额5%的违约金。
    assert:
      - type: llm-rubric
        value: "必须识别出违约金比例严重不对等（甲方50% vs 乙方5%），并标记为高风险"
      - type: contains
        value: "违约金"

  - description: "风险-单方面解除权"
    vars:
      contract: |
        第九条 合同解除
        9.1 甲方有权在任何时候无理由解除本合同，无需承担任何责任。
        9.2 乙方不得单方面解除本合同。
    assert:
      - type: llm-rubric
        value: "必须识别出甲方单方面解除权的不公平条款"

  - description: "风险-模糊表述"
    vars:
      contract: |
        第五条 付款方式
        甲方应在适当时候支付相应款项。
    assert:
      - type: llm-rubric
        value: "必须指出'适当时候'和'相应款项'表述模糊，缺乏明确的付款时间和金额"

  - description: "风险-无上限责任"
    vars:
      contract: |
        第十条 赔偿责任
        乙方应对甲方因本合同产生的所有直接损失、间接损失、
        预期利润损失承担全部赔偿责任，无金额上限。
    assert:
      - type: llm-rubric
        value: "必须识别出无上限赔偿责任的风险，建议设置责任上限"

  # ========== 条款完整性类 ==========
  - description: "缺失-无交付条款"
    vars:
      contract: |
        第一条 标的物：定制软件系统
        第二条 金额：人民币100万元
        第三条 付款：签订后支付100%
    assert:
      - type: llm-rubric
        value: "必须指出缺少交付时间、交付方式、验收标准等关键条款"

  - description: "缺失-无争议解决"
    vars:
      contract: |
        第一条 甲方委托乙方开发APP
        第二条 开发费用50万元
        第三条 开发周期3个月
        第四条 验收标准见附件
    assert:
      - type: llm-rubric
        value: "必须指出缺少争议解决条款（仲裁或诉讼管辖）"

  # ========== 误报控制类 ==========
  - description: "正常合同-不应误报"
    vars:
      contract: |
        软件开发服务合同
        
        第一条 服务内容
        乙方为甲方开发企业管理系统。
        
        第二条 合同金额
        总金额人民币伍拾万元整（¥500,000）。
        
        第三条 付款方式
        签订后7日内支付30%，即15万元；
        中期验收后7日内支付30%，即15万元；
        终验收后7日内支付40%，即20万元。
        
        第四条 开发周期
        自合同签订之日起90个工作日内完成。
        
        第五条 验收标准
        按附件《验收标准》执行，验收期为7个工作日。
        
        第六条 违约责任
        任何一方违约，应向对方支付合同金额10%的违约金。
        
        第七条 争议解决
        协商不成，提交北京仲裁委员会仲裁。
        
        第八条 合同期限
        本合同有效期至项目验收完成且质保期届满之日。
    assert:
      - type: llm-rubric
        value: "这是一份条款完整、权责对等的标准合同，不应有高风险警告"
      - type: not-contains
        value: "高风险"

  # ========== 建议质量类 ==========
  - description: "建议质量-违约金修改建议"
    vars:
      contract: |
        违约责任：甲方违约金30%，乙方违约金5%
    assert:
      - type: llm-rubric
        value: |
          修改建议必须：
          1. 具体说明建议的违约金比例（如双方均为10%）
          2. 建议应该是可直接采纳的条款文本
```

---

## 8. 运行与查看结果

### 8.1 运行评估

```bash
# 基本运行
promptfoo eval

# 指定配置文件
promptfoo eval -c my-config.yaml

# 只运行特定测试
promptfoo eval --filter-description "风险"

# 并行运行（加速）
promptfoo eval --max-concurrency 5

# 输出 JSON 结果
promptfoo eval -o results.json
```

### 8.2 查看结果

```bash
# 启动 Web UI（推荐）
promptfoo view

# 会在浏览器打开 http://localhost:15500
```

### 8.3 结果解读

Web UI 展示：
- **通过率**：各测试用例的通过/失败状态
- **模型对比**：多模型横向对比
- **详细输出**：每个测试的完整输入输出
- **断言结果**：每个断言的判定详情

---

## 9. CI/CD 集成

### 9.1 GitHub Actions

```yaml
# .github/workflows/eval.yml
name: Contract Review Eval

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install Promptfoo
        run: npm install -g promptfoo
      
      - name: Run Evaluation
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          cd contract-eval
          promptfoo eval --ci
      
      - name: Upload Results
        uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: contract-eval/output/
```

### 9.2 GitLab CI

```yaml
# .gitlab-ci.yml
eval:
  image: node:20
  script:
    - npm install -g promptfoo
    - cd contract-eval && promptfoo eval --ci
  artifacts:
    paths:
      - contract-eval/output/
```

### 9.3 CI 模式说明

`--ci` 参数会：
- 禁用交互式输出
- 测试失败时返回非零退出码
- 适合自动化流水线

---

## 10. 最佳实践与常见问题

### 10.1 最佳实践

**测试用例管理**
- ✅ 按维度分文件组织测试用例
- ✅ 使用 `description` 清晰描述每个用例
- ✅ 定期从真实案例补充测试集

**评估策略**
- ✅ 先建立基线，再迭代优化
- ✅ 每次改提示词都跑评估
- ✅ 关注通过率变化趋势

**模型选择**
- ✅ 用便宜模型跑大量测试
- ✅ 用强模型做 llm-rubric 评分
- ✅ 定期对比新模型

### 10.2 常见问题

**Q: llm-rubric 评分不稳定怎么办？**
```yaml
# 方案1：写更明确的评分标准
- type: llm-rubric
  value: |
    评分标准（二选一）：
    - 通过：输出中明确提到"违约金不对等"
    - 不通过：未提到或表述模糊

# 方案2：多次评估取多数
defaultTest:
  options:
    rubricPrompt: "你是严格的评估员..."
```

**Q: 测试太慢怎么办？**
```bash
# 增加并发
promptfoo eval --max-concurrency 10

# 使用缓存
promptfoo eval --cache
```

**Q: 如何对比不同版本的提示词？**
```yaml
prompts:
  - file://prompts/v1.txt
  - file://prompts/v2.txt
# 会自动生成对比矩阵
```

**Q: 如何处理长合同？**
```yaml
# 分段测试
tests:
  - vars:
      contract_section: "违约责任部分..."
    assert:
      - type: llm-rubric
        value: "针对违约责任部分的评估标准"
```

---

## 附录：快速命令参考

```bash
# 安装
npm install -g promptfoo

# 初始化
promptfoo init

# 运行评估
promptfoo eval

# 查看结果
promptfoo view

# CI 模式
promptfoo eval --ci

# 指定配置
promptfoo eval -c config.yaml

# 过滤测试
promptfoo eval --filter-description "风险"

# 输出 JSON
promptfoo eval -o results.json

# 清除缓存
promptfoo cache clear
```

---

*文档版本: 1.0 | 更新日期: 2026-02-01 | 作者: 龙虾 🦞*
