#!/bin/bash
# 生产环境启动脚本 — word-learn-python
set -e

APP_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$APP_DIR/backend"
LOG_DIR="$APP_DIR/logs"
VENV_DIR="$BACKEND_DIR/venv"

mkdir -p "$LOG_DIR"

# 生成 JWT 密钥（如果不存在）
SECRET_KEY_FILE="$APP_DIR/.secret_key"
if [ ! -f "$SECRET_KEY_FILE" ]; then
    python3 -c "import secrets; print(secrets.token_hex(32))" > "$SECRET_KEY_FILE"
    chmod 600 "$SECRET_KEY_FILE"
fi
export WORDLEARN_SECRET_KEY="$(cat "$SECRET_KEY_FILE")"

# 激活虚拟环境
source "$VENV_DIR/bin/activate"

# 启动 Gunicorn（4 workers, uvicorn worker）
cd "$BACKEND_DIR"
exec gunicorn main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers 4 \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --access-logfile "$LOG_DIR/access.log" \
    --error-logfile "$LOG_DIR/error.log" \
    --log-level info \
    --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
