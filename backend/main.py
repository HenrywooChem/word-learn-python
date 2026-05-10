"""
单词学习应用 - FastAPI 主文件
更新：添加朗读评分路由
"""
import os
import asyncio
import tempfile
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse

from database import init_db
from routers import auth, libraries, learning, records
from routers.wrong_questions import router as wrong_questions_router
from routers.pronunciation import router as pronunciation_router

# Edge TTS 支持
try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    EDGE_TTS_AVAILABLE = False

app = FastAPI(
    title="单词学习应用 API",
    description="Python 端学习应用后端服务",
    version="1.0.1"
)

# 开放 CORS
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
app.include_router(pronunciation_router)  # 朗读评分


@app.on_event("startup")
def startup_event():
    """应用启动时初始化数据库"""
    init_db()


# 获取前端文件路径
_base_dir = os.path.dirname(os.path.abspath(__file__))
_local_frontend = os.path.join(_base_dir, "..", "frontend", "index.html")
frontend_path = os.path.abspath(_local_frontend) if os.path.exists(_local_frontend) else "/app/frontend/index.html"


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api/tts")
async def tts_endpoint(text: str = Query(..., min_length=1, max_length=500)):
    """TTS接口 - 使用Edge TTS生成音频"""
    if not EDGE_TTS_AVAILABLE:
        return JSONResponse({"error": "TTS not available"}, status_code=503)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp_path = tmp.name

        communicate = edge_tts.Communicate(text, "en-US-JennyNeural")
        await communicate.save(tmp_path)

        def iterfile():
            with open(tmp_path, "rb") as f:
                yield from f
            try:
                os.unlink(tmp_path)
            except:
                pass

        headers = {"Access-Control-Allow-Origin": "*"}
        return StreamingResponse(
            iterfile(),
            media_type="audio/mpeg",
            headers={"Content-Disposition": "inline; filename=tts.mp3"}
        )
    except Exception as e:
        try:
            os.unlink(tmp_path)
        except:
            pass
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/")
def root():
    """返回前端页面"""
    if os.path.exists(frontend_path):
        return FileResponse(frontend_path)
    return JSONResponse({"message": "单词学习应用 API 启动", "docs": "/docs"})


@app.get("/{path:path}")
async def serve_frontend(path: str):
    """支持前端路径"""
    # 如果是 API 请求，返回 404 而不是前端页面
    if path.startswith("api/"):
        return JSONResponse({"detail": "Not Found"}, status_code=404)
    
    # 先检查是否是静态文件
    static_dir = os.path.join(_base_dir, "..", "frontend")
    static_file_path = os.path.join(static_dir, path)
    
    if os.path.exists(static_file_path) and os.path.isfile(static_file_path):
        return FileResponse(static_file_path)
    
    # 否则返回前端页面
    if os.path.exists(frontend_path):
        return FileResponse(frontend_path)
    return JSONResponse({"message": "单词学习应用"})
