"""
单词学习应用 - FastAPI 后端
"""
import os
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


# 获取前端文件路径 - 修复版
frontend_path = "/app/frontend/index.html"

@app.get("/")
def root():
    """返回前端页面"""
    return FileResponse(frontend_path)


@app.get("/{path:path}")
async def serve_frontend(path: str):
    """支持前端路由"""
    return FileResponse(frontend_path)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
