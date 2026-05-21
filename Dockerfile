FROM python:3.11-slim

WORKDIR /app

# 复制并安装依赖（无需 gcc/libpq-dev，SQLite 不需要 PostgreSQL 库）
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r backend/requirements.txt

# 复制代码
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# 创建数据库目录
RUN mkdir -p /app/backend/data

EXPOSE 8000

WORKDIR /app/backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
