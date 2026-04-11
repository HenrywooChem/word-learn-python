"""
单词学习应用 - FastAPI 后端
"""
import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import init_db
from routers import auth, libraries, learning, records
from routers.wrong_questions import router as wrong_questions_router

app = FastAPI(
    title="单词学习应用 API",
    description="Python 版单词学习应用后端服务",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router)
app.include_router(libraries.router)
app.include_router(learning.router)
app.include_router(records.router)
app.include_router(wrong_questions_router)


@app.on_event("startup")
def startup_event():
    """应用启动时初始化数据库"""
    init_db()


# 自动适配本地和 Docker 环境的前端路径
# Docker 环境：/app/frontend/index.html
# 本地环境：相对于 backend/ 上一级的 frontend/index.html
_docker_path = Path("/app/frontend/index.html")
_local_path = (Path(__file__).parent / ".." / "frontend" / "index.html").resolve()
frontend_path = str(_docker_path if _docker_path.exists() else _local_path)

@app.get("/")
def root():
    """返回前端页面"""
    return FileResponse(frontend_path)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/{path:path}")
async def serve_frontend(path: str):
    """支持前端路由"""
    return FileResponse(frontend_path)
