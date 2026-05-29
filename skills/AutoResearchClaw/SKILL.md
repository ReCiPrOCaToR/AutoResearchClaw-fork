# AutoResearchClaw 技能

> AutoResearchClaw 是一个全自动的 23 阶段学术研究流水线，从一句话 idea 到可提交的论文。
> 官方仓库: https://github.com/aiming-lab/AutoResearchClaw

## 一、安装与初始化

### 1.1 环境要求

- **Python**: 3.10+
- **Git**: 用于克隆和版本管理
- **LLM API Key**: OpenAI / DeepSeek / Minimax / Gemini 等
- **可选**: Docker（沙箱实验）、LaTeX（PDF 编译）、OpenCode（Beast Mode 代码生成）

### 1.2 安装步骤

```bash
# 克隆仓库
git clone https://github.com/aiming-lab/AutoResearchClaw.git
cd AutoResearchClaw

# 创建虚拟环境（推荐）
python3 -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 安装依赖
pip install -e .

# 检查环境
researchclaw doctor
```

### 1.3 初始化配置

```bash
# 交互式创建 config.arc.yaml
researchclaw init

# 或手动复制模板
copy config.researchclaw.example.yaml config.arc.yaml
```

运行 `researchclaw init` 时会提示选择 LLM 提供商：
| 编号 | 提供商 | 环境变量 |
|------|--------|---------|
| 1 | OpenAI | `OPENAI_API_KEY` |
| 2 | OpenRouter | `OPENROUTER_API_KEY` |
| 3 | DeepSeek | `DEEPSEEK_API_KEY` |
| 4 | Minimax | `MINIMAX_API_KEY` |
| 5 | ACP（本地模型）| 无需 API Key |

### 1.4 可选工具安装

```bash
# 安装 OpenCode Beast Mode（推荐，复杂代码生成更强）
npm i -g opencode-ai@latest

# 或通过 researchclaw 自动安装
researchclaw setup
```

## 二、配置说明

### 2.1 配置文件结构

配置文件搜索顺序（优先级从高到低）：
1. `config.arc.yaml`（当前目录）
2. `config.yaml`（当前目录）
3. `~/.researchclaw/config.yaml`

### 2.2 关键配置项

```yaml
project:
  name: "my-research"
  mode: "full-auto"          # full-auto | semi-auto | docs-first

research:
  topic: "你的研究主题"
  domains: ["machine-learning", "network"]
  daily_paper_count: 8
  quality_threshold: 4.0

llm:
  provider: "openai-compatible"
  base_url: "https://api.openai.com/v1"
  # DeepSeek: "https://api.deepseek.com/v1"
  # OpenRouter: "https://openrouter.ai/api/v1"
  wire_api: "chat_completions"   # 或 "responses"
  api_key_env: "OPENAI_API_KEY"
  primary_model: "gpt-4o"
  fallback_models:
    - "gpt-4.1"
    - "gpt-4o-mini"

experiment:
  mode: "sandbox"               # sandbox | docker | simulated | ssh_remote
  time_budget_sec: 300
  sandbox:
    python_path: "python"       # Windows 用绝对路径，如 "D:/Anaconda/python.exe"
    gpu_required: false
    max_memory_mb: 4096
```

### 2.3 实验模式对比

| 模式 | 速度 | 真实性 | 适用场景 |
|------|------|--------|---------|
| `simulated` | ⚡ 极快 | ❌ 假数据 | 开发调试、框架测试 |
| `sandbox` | 🐢 慢 | ✅ 真实 | 本地小规模实验 |
| `docker` | 🐢 慢 | ✅ 真实 | 需要隔离/依赖管理 |
| `ssh_remote` | 🐢 取决于远程 | ✅ 真实 | 远程 GPU 服务器 |

### 2.4 HITL（Human-in-the-Loop）模式

```bash
# 全自动运行（所有 gate 自动通过）
researchclaw run --topic "你的主题" --auto-approve

# 半自动（gate 处暂停等待人工确认）
researchclaw run --topic "你的主题"

# 指定模式: full-auto | gate-only | checkpoint | step-by-step | co-pilot
researchclaw run --topic "你的主题" --mode co-pilot

# 从指定阶段开始
researchclaw run --topic "你的主题" --from-stage EXPERIMENT_DESIGN

# 断点续传
researchclaw run --resume
```

## 三、23 阶段流水线概览

| 阶段 | 名称 | 说明 |
|------|------|------|
| 01 | TOPIC_INIT | 解析研究主题 |
| 02 | PROBLEM_DECOMPOSITION | 问题分解 |
| 03-06 | LITERATURE_* | 文献搜索、收集、筛选 |
| 07-08 | KNOWLEDGE_SYNTHESIS | 知识综合、假设生成 |
| 09 | EXPERIMENT_DESIGN | 实验设计（Gate ⚠️） |
| 10 | CODE_GENERATION | 代码生成 |
| 11 | RESOURCE_PLANNING | 资源规划 |
| 12 | EXPERIMENT_RUN | 实验执行 |
| 13 | ITERATIVE_REFINE | 迭代优化 |
| 14 | RESULT_ANALYSIS | 结果分析 |
| 15 | RESEARCH_DECISION | 研究决策（PROCEED/REFINE/PIVOT） |
| 16-19 | PAPER_* | 论文撰写（大纲→草稿→评审→修改） |
| 20 | QUALITY_GATE | 质量门控（Gate ⚠️） |
| 21-23 | FINALIZATION_* | 最终化、归档、引文验证 |

**Gate 阶段**（需要人工审批，除非 `--auto-approve`）：
- Stage 5: 文献筛选
- Stage 9: 实验设计
- Stage 20: 质量门控

## 四、日常使用命令

```bash
# 运行完整流水线
researchclaw run --topic "基于深度学习的网络流量异常检测" --auto-approve

# 查看运行状态
researchclaw status artifacts/rc-XXXXXX-XXXXXX

# 附加到运行中的流水线进行交互
researchclaw attach artifacts/rc-XXXXXX-XXXXXX

# 审批/拒绝 Gate
researchclaw approve artifacts/rc-XXXXXX-XXXXXX
researchclaw reject artifacts/rc-XXXXXX-XXXXXX --reason "实验设计需要改进"

# 注入指导
researchclaw guide artifacts/rc-XXXXXX-XXXXXX --stage 10 --message "请使用 Transformer 架构"

# 生成运行报告
researchclaw report --run-dir artifacts/rc-XXXXXX-XXXXXX

# 验证配置
researchclaw validate

# 环境健康检查
researchclaw doctor

# 管理多项目
researchclaw project list
researchclaw project create --name "project-A" --topic "xxx"
researchclaw project compare --names "project-A" "project-B"

# 启动 Web 仪表板
researchclaw serve --port 8000
```

## 五、故障排查

### 5.1 常见问题

#### Q1: Stage 10 代码生成失败，报错 "Expecting value: line 1 column 1"

**原因**: LLM API 返回了空响应。常见于 ModelScope 等需要 `stream=false` 的 provider。

**修复**: `researchclaw/llm/client.py` 第 440 行附近添加：
```python
body["stream"] = False
```

然后**重启 Python 进程**（必须完全退出，清除 `__pycache__`）：
```bash
cd D:\My_Project\AutoResearchClaw
rimraf researchclaw\**\__pycache__
rimraf researchclaw\**\*.pyc
```

#### Q2: 沙箱找不到 python 命令

**原因**: Windows 下 `python` 不在 PATH 中。

**修复**: 在 `config.yaml` 中使用绝对路径：
```yaml
experiment:
  sandbox:
    python_path: "D:/Anaconda/python.exe"
```

#### Q3: 流水线中断后如何续跑？

```bash
# 自动查找最近的 checkpoint 并续跑
researchclaw run --resume --topic "你的主题"

# 或从指定阶段重新开始
researchclaw run --from-stage CODE_GENERATION --topic "你的主题"

# 指定已有的输出目录
researchclaw run --output artifacts/rc-20260417-001436-03dfbf --resume --topic "你的主题"
```

#### Q4: 实验失败后如何修复？

流水线内置了自动修复机制：
1. Stage 14 分析结果质量
2. 自动诊断问题（`experiment_diagnosis.json`）
3. 生成修复提示（`repair_prompt.txt`）
4. 自动重试最多 3 轮（`max_cycles: 3`）

也可以手动修复后重跑：
```bash
researchclaw run --from-stage EXPERIMENT_RUN --resume
```

#### Q5: API Key 相关错误

```bash
# 设置环境变量
# Windows (PowerShell):
$env:DEEPSEEK_API_KEY = "sk-xxx"

# Linux/macOS:
export DEEPSEEK_API_KEY="sk-xxx"

# 或直接编辑 config.yaml（不推荐，可能被提交到 git）
```

#### Q6: OpenCode 安装失败

```bash
# 检查 Node.js 和 npm 是否安装
node --version
npm --version

# 手动安装
npm i -g opencode-ai@latest

# 或使用 researchclaw 自动安装
researchclaw setup
```

### 5.2 已知坑（Known Issues）

| 问题 | 状态 | 说明 |
|------|------|------|
| Stage 15 未创建目录就写文件 | ⚠️ 已知 | 运行前确保 `artifacts/` 目录存在 |
| 中文字体缺失 | ⚠️ 已知 | Windows 无中文字体，图表中文字不显示（不影响英文论文） |
| ModelScope 返回空响应 | ✅ 已修复 | 需 `stream=false` 补丁，本地已应用 |
| Python 模块缓存 | ⚠️ 注意 | 修改代码后必须清除 `__pycache__` 并重启进程 |
| 实验结果不可复现 | ⚠️ 已知 | 沙箱环境可能有差异，建议固定随机种子 |

## 六、调试技巧

### 6.1 日志查看

```bash
# 查看运行日志
python read_log.py

# 查看所有运行
python check_all_runs.py

# 查看最新运行
python inspect_latest.py

# 查看 Stage 10 详细信息
python inspect_stage10_full.py
```

### 6.2 单阶段调试

```bash
# 只运行到 Stage 10
researchclaw run --topic "你的主题" --to-stage CODE_GENERATION

# 从 Stage 10 开始单步调试
researchclaw run --from-stage CODE_GENERATION --to-stage EXPERIMENT_RUN
```

### 6.3 LLM 连接测试

```bash
# 直接测试 LLM 连接（不经过流水线）
python test_rc_llm.py
```

### 6.4 配置文件验证

```bash
researchclaw validate
researchclaw doctor
```

## 七、输出产物

成功运行后，产物位于 `artifacts/<run_id>/deliverables/`：

| 文件 | 说明 |
|------|------|
| `paper_final.md` | 最终论文（Markdown） |
| `paper.tex` | 会议格式 LaTeX（NeurIPS/ICML/ICLR） |
| `references.bib` | BibTeX 引文（经验证的） |
| `code/` | 实验代码 + `requirements.txt` |
| `charts/` | 图表（PNG/PDF） |
| `verification_report.json` | 引文完整性验证报告 |
| `manifest.json` | 产物清单 |

## 八、OpenClaw 集成

如果使用 OpenClaw 作为 AI 助手，可以直接通过消息触发研究：

1. 在 OpenClaw 中分享仓库 URL
2. 说 "Research [你的主题]"
3. OpenClaw 自动完成：clone → install → configure → run → return results

支持的消息平台：Discord / Telegram / 飞书 / 微信 / Slack

## 九、版本信息

- **当前版本**: v0.3.1（Git: `684ddb2`）
- **发布日期**: 2026-05
- **论文**: [arXiv 2605.20025](https://arxiv.org/abs/2605.20025)
- **基准测试**: [ARC-Bench](https://huggingface.co/datasets/AIMING-Lab-UNC/ARC-Bench)

## 十、联系与社区

- **GitHub**: https://github.com/aiming-lab/AutoResearchClaw
- **Discord**: https://discord.gg/u4ksqW5P
- **Issue 反馈**: https://github.com/aiming-lab/AutoResearchClaw/issues