# ChatTest-for-admission-interview

本项目是一个用于考研复试笔试的项目。本文档包含了项目的开发规范和使用指南。

## 开发环境要求

本项目使用 [uv](https://github.com/astral-sh/uv) 进行Python包管理和虚拟环境管理。

### 安装 uv

```bash
# 使用 pip 安装
pip install uv

# 或使用 Homebrew (macOS)
brew install uv

# 或使用官方安装脚本
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 项目设置

### 初始化项目

```bash
# 克隆项目后进入目录
cd ChatTest-for-admission-interview

# 使用 uv 同步依赖（创建虚拟环境并安装依赖）
uv sync

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows
```

### 添加新依赖

```bash
# 添加到常规依赖
uv add 包名

# 添加到开发依赖
uv add --dev 包名
```

### 运行项目

```bash
# 在虚拟环境中运行
uv run python main.py
```

## 开发规范

### 代码风格

- 遵循 PEP 8 代码风格指南
- 使用 black 进行代码格式化
- 使用 ruff 进行代码检查

### 依赖管理

- 所有生产环境依赖必须通过 `uv add` 命令添加
- 开发工具依赖应作为 dev-dependencies 添加
- 不要手动编辑 [pyproject.toml](file:///home/jianuo/CODE/ChatTest-for-admission-interview/pyproject.toml) 文件中的依赖部分

### 提交规范

- 提交前确保运行代码格式化工具
- 提交信息应清晰描述更改内容
- 遵循约定式提交规范 (Conventional Commits)

## uv 简明使用教程

### 什么是 uv?

uv 是一个高性能的 Python 包管理器，用于替代传统的 pip。它提供了快速的依赖解析和安装功能。

### 核心命令

#### 依赖管理

```bash
# 安装所有依赖（包括开发依赖）
uv sync

# 添加新依赖
uv add requests

# 添加开发依赖
uv add pytest --dev

# 移除依赖
uv remove 包名
```

#### 运行命令

```bash
# 在项目环境中运行命令
uv run python script.py

# 运行已安装的命令行工具
uv run pytest
```

## 项目结构

```
.
├── data_process/       # 考试试卷数据收集与处理模块
│   ├── data_sources.xlsx   # 数据源配置文件
│   ├── download_repos.py   # 数据自动下载脚本
│   └── datas/              # 原始试卷数据存放目录
├── main.py             # 主程序入口
├── pyproject.toml      # 项目配置和依赖定义
├── README.md           # 项目说明文档
└── .venv/              # uv 创建的虚拟环境（已忽略）
```

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 确保代码符合规范并经过测试
4. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
5. 推送到分支 (`git push origin feature/AmazingFeature`)
6. 开启 Pull Request