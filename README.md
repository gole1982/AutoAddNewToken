# AtomGit AI Token Automation

自动化领取 AtomGit AI 平台无限 token 的脚本。

## 功能

- 自动登录 AtomGit AI 平台
- 在指定页面点击"免费领取【无限token】"按钮
- 支持定时任务自动执行

## 环境要求

- Python 3.8+
- Chromium 浏览器 (通过 Playwright 安装)

## 安装

```bash
pip install -r requirements.txt
playwright install chromium
```

## 配置

1. 复制环境变量模板：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的 AtomGit 用户名和密码：
```env
ATOMGIT_USERNAME=your_username
ATOMGIT_PASSWORD=your_password
```

## 运行

```bash
./run_task.sh
```

或直接运行 Python 脚本：
```bash
python automation.py
```

## 定时任务

设置每日自动执行：
```bash
./setup_cron.sh
```

查看当前 cron 任务：
```bash
crontab -l | grep automation
```

## 项目结构

```
.
├── automation.py      # 主脚本
├── requirements.txt   # Python 依赖
├── run_task.sh        # 运行脚本
├── setup_cron.sh      # Cron 设置脚本
└── .env.example       # 环境变量模板
```
