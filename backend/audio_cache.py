"""音频缓存：文本 -> 静态 mp3 文件

生产服务器出口 IP 被微软 Edge TTS 拒绝（403），实时合成不可用，
因此改为本地批量生成静态文件（tools/build_audio.py），运行时直接读磁盘。
"""
import hashlib
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
VOICE = "en-US-JennyNeural"


def clean_for_tts(text: str) -> str:
    """把词条文本转成适合朗读的形式

    "have ... in common" -> "have in common"
    "kilometre (ame kilometer)" -> "kilometre"
    "belong to sb" -> "belong to"
    """
    t = (text or "").strip()
    if not t:
        return ""
    t = re.sub(r"[（(][^)）]*[)）]", " ", t)
    t = re.sub(r"\b(?:sb|sth)\b\.?", " ", t, flags=re.I)
    t = re.sub(r"[.．]{2,}|…+", " ", t)
    t = re.sub(r"\s*[/|]\s*", " or ", t)
    t = re.sub(r"\s+", " ", t).strip(" ,.;-")
    return t


def audio_key(text: str) -> str:
    """文本 -> 文件名（16 位哈希）"""
    return hashlib.sha1(clean_for_tts(text).encode("utf-8")).hexdigest()[:16]


def audio_path(text: str) -> str:
    return os.path.join(AUDIO_DIR, audio_key(text) + ".mp3")


def cached_audio(text: str):
    """命中缓存返回文件路径，否则返回 None"""
    p = audio_path(text)
    try:
        if os.path.getsize(p) > 512:
            return p
    except OSError:
        pass
    return None
