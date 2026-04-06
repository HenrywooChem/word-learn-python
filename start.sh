#!/bin/bash
# 启动单词学习应用

echo "========================================"
echo "   单词学习应用 (Python版) - 启动脚本"
echo "========================================"

# 进入后端目录
cd "$(dirname "$0")/backend"

# 检查并创建虚拟环境（如果需要）
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python -m venv venv
fi

# 激活虚拟环境
source venv/Scripts/activate

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt -q

# 启动后端服务
echo ""
echo "启动后端服务 (http://localhost:8000) ..."
echo "API 文档: http://localhost:8000/docs"
echo ""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
