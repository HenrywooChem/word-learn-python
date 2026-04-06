# 单词学习应用 (Python版)

基于 FastAPI + Vue.js 的单词学习 Web 应用。

## 功能特性

- 📝 用户注册/登录
- 📚 词库管理（系统词库 + 自定义词库）
- 📖 单词学习（发音/含义评分）
- ❌ 错题本（答错自动加入）
- 🧠 遗忘曲线复习（智能复习提醒）
- 📊 学习记录与统计
- 🎯 每日目标设置（包含新词+错题复习）
- ✅ 每日签到

## 技术栈

- **后端**: FastAPI + SQLAlchemy + SQLite
- **前端**: Vue 3 + Tailwind CSS

## 快速启动

### 方式一：Windows 双击启动

```bash
双击 start.bat
```

### 方式二：命令行启动

```bash
# 安装依赖
cd backend
pip install -r requirements.txt

# 启动服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 方式三：使用 Python 脚本

```bash
python start.py
```

## 访问应用

- 前端: http://localhost:8000
- API 文档: http://localhost:8000/docs

## 首次使用

1. 启动服务后，打开浏览器访问 http://localhost:8000
2. 点击"立即注册"创建一个账号
3. 选择角色（孩子/家长）
4. 进入词库页面选择要学习的词库
5. 开始学习！

## 项目结构

```
word-learn-python/
├── backend/
│   ├── main.py          # FastAPI 主应用
│   ├── models.py        # 数据模型
│   ├── database.py     # 数据库配置
│   ├── requirements.txt # 依赖
│   └── routers/        # API 路由
│       ├── auth.py     # 认证
│       ├── libraries.py # 词库
│       ├── learning.py # 学习
│       └── records.py  # 记录
├── frontend/
│   └── index.html      # 前端页面
├── start.bat           # Windows 启动脚本
├── start.sh            # Linux/Mac 启动脚本
└── README.md           # 说明文档
```

## 系统词库

- 小学一年级
- 小学三年级
- 小学五年级
- 初一（七年级）
- 初三（九年级）
- 高中必修词汇

## 错题本与遗忘曲线

### 错题本
- 学习时评分低于 60 分的单词会自动加入错题本
- 错题本记录每道题的错误次数、正确次数
- 可以重置复习进度或删除错题

### 遗忘曲线复习
采用艾宾浩斯遗忘曲线算法，复习间隔为：
- 第 1 次错误后：1 天后复习
- 第 2 次错误后：3 天后复习
- 第 3 次错误后：7 天后复习
- 第 4 次错误后：15 天后复习
- 以此类推...

### 每日任务
每日任务包含两部分：
- **新词学习**：60% - 学习新的单词
- **错题复习**：40% - 复习需要巩固的错题

连续正确达到 5 次且错误不超过 2 次，单词标记为"已掌握"

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/auth/register | 注册 |
| POST | /api/auth/login | 登录 |
| GET | /api/auth/me | 当前用户 |
| GET | /api/libraries | 词库列表 |
| GET | /api/libraries/system | 系统词库 |
| GET | /api/learning/today | 今日学习 |
| POST | /api/learning/session | 提交学习 |
| POST | /api/learning/signin | 签到 |
| GET | /api/records/profile | 用户资料 |
| GET | /api/records/stats | 学习统计 |
| GET | /api/wrong-questions | 错题列表 |
| GET | /api/wrong-questions/stats | 错题统计 |
| GET | /api/wrong-questions/due-today | 今日待复习 |
| POST | /api/wrong-questions/review | 提交复习结果 |
| POST | /api/learning/review | 提交错题复习 |
