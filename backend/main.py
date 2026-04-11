"""
单词学习应用 - FastAPI 后端
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

# Edge TTS 导入
try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    EDGE_TTS_AVAILABLE = False

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


# 获取前端文件路径
_base_dir = os.path.dirname(os.path.abspath(__file__))
_local_frontend = os.path.join(_base_dir, "..", "frontend", "index.html")
frontend_path = os.path.abspath(_local_frontend) if os.path.exists(_local_frontend) else "/app/frontend/index.html"


@app.get("/health")
def health_check():
    """健康检查接口 - 必须在通配符路由之前定义"""
    return {"status": "healthy"}


@app.get("/api/tts")
async def tts_endpoint(text: str = Query(..., min_length=1, max_length=500)):
    """TTS接口 - 使用Edge TTS生成音频"""
    if not EDGE_TTS_AVAILABLE:
        return JSONResponse({"error": "TTS not available"}, status_code=503)
    
    try:
        # 创建临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp_path = tmp.name
        
        # 使用Edge TTS生成音频
        communicate = edge_tts.Communicate(text, "en-US-JennyNeural")
        await communicate.save(tmp_path)
        
        # 读取文件并返回
        def iterfile():
            with open(tmp_path, "rb") as f:
                yield from f
            # 清理临时文件
            try:
                os.unlink(tmp_path)
            except:
                pass
        
        return StreamingResponse(
            iterfile(),
            media_type="audio/mpeg",
            headers={"Content-Disposition": f"inline; filename=tts.mp3"}
        )
    except Exception as e:
        # 清理临时文件
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
    return JSONResponse({"message": "单词学习应用 API 运行中", "docs": "/docs"})


@app.get("/{path:path}")
async def serve_frontend(path: str):
    """支持前端路由"""
    if os.path.exists(frontend_path):
        return FileResponse(frontend_path)
    return JSONResponse({"message": "单词学习应用 API 运行中", "docs": "/docs"})
