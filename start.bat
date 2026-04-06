@echo off
chcp 65001 >nul
echo ========================================
echo    单词学习应用 (Python版) - 启动脚本
echo ========================================
echo.

cd /d "%~dp0backend"

echo 检查并创建虚拟环境...
if not exist "venv" (
    python -m venv venv
)

echo 激活虚拟环境...
call venv\Scripts\activate.bat

echo 安装依赖...
pip install -r requirements.txt -q

echo.
echo 启动后端服务 (http://localhost:8000) ...
echo API 文档: http://localhost:8000/docs
echo.
echo 按 Ctrl+C 停止服务
echo.

uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause
