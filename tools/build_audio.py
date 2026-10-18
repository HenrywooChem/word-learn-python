"""预生成单词 / 例句音频，落地为静态 mp3。

背景：生产服务器出口 IP 被微软 Edge TTS 拒绝（403），实时合成不可用；
改为本地批量生成、上传静态文件，/api/tts 直接读磁盘缓存返回。

用法：
    python tools/build_audio.py                 # 全量生成（跳过已存在）
    python tools/build_audio.py --only words    # 只生成单词
    python tools/build_audio.py --only examples # 只生成例句
"""
import argparse
import asyncio
import hashlib
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "backend"))

from audio_cache import AUDIO_DIR, VOICE, audio_key, clean_for_tts  # noqa: E402


def collect_from_db(db_path: str):
    """从生产库读取全部词库（含用户自建词库）"""
    import json
    import sqlite3

    con = sqlite3.connect(db_path)
    words, examples = [], []
    for (raw,) in con.execute("select words from word_libraries"):
        try:
            items = json.loads(raw)
        except (ValueError, TypeError):
            continue
        for w in items:
            if isinstance(w, dict) and w.get("word"):
                words.append(w["word"])
                if w.get("example_sentence"):
                    examples.append(w["example_sentence"])
    con.close()
    print(f"数据库 {db_path}: 词条 {len(words)}，例句 {len(examples)}")
    return words, examples


def collect_texts(only: str, db_path: str = ""):
    from wordbank_shcep import get_shcep_libraries
    from word_data import enrich_word

    words, examples, seen_w, seen_e = [], [], set(), set()
    if db_path:
        db_words, db_examples = collect_from_db(db_path)
        for w in db_words:
            sp = clean_for_tts(w)
            if sp and sp.lower() not in seen_w:
                seen_w.add(sp.lower())
                words.append(sp)
        for e in db_examples:
            if e.strip().lower() not in seen_e:
                seen_e.add(e.strip().lower())
                examples.append(e)

    for lib in get_shcep_libraries():
        for w in lib["words"]:
            enrich_word(w, lib["id"])
            raw = (w.get("word") or "").strip()
            spoken = clean_for_tts(raw)
            if spoken and spoken.lower() not in seen_w:
                seen_w.add(spoken.lower())
                words.append(spoken)

            sent = (w.get("example_sentence") or "").strip()
            if sent and sent.lower() not in seen_e:
                seen_e.add(sent.lower())
                examples.append(sent)

    out = []
    if only in ("all", "words"):
        out += words
    if only in ("all", "examples"):
        out += examples
    print(f"单词 {len(words)} 条，例句 {len(examples)} 条，待生成 {len(out)} 条")
    return out


async def synth(text: str, path: str, sem: asyncio.Semaphore, counter: dict):
    import edge_tts

    for attempt in range(3):
        async with sem:
            try:
                tmp = path + ".part"
                await edge_tts.Communicate(text, VOICE).save(tmp)
                if os.path.getsize(tmp) < 800:
                    raise RuntimeError("音频过小")
                os.replace(tmp, path)
                counter["ok"] += 1
                if counter["ok"] % 50 == 0:
                    print(f"  已生成 {counter['ok']}/{counter['total']}")
                return
            except Exception as e:
                if os.path.exists(path + ".part"):
                    try:
                        os.unlink(path + ".part")
                    except OSError:
                        pass
                if attempt == 2:
                    counter["fail"] += 1
                    print(f"  [失败] {text[:40]}: {str(e)[:80]}")
                else:
                    await asyncio.sleep(1.5 * (attempt + 1))


async def main_async(texts, force: bool):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    todo = []
    for t in texts:
        p = os.path.join(AUDIO_DIR, audio_key(t) + ".mp3")
        if force or not os.path.exists(p):
            todo.append((t, p))

    print(f"已有 {len(texts) - len(todo)} 条，需生成 {len(todo)} 条")
    if not todo:
        return

    sem = asyncio.Semaphore(6)
    counter = {"ok": 0, "fail": 0, "total": len(todo)}
    await asyncio.gather(*(synth(t, p, sem, counter) for t, p in todo))
    print(f"完成：成功 {counter['ok']}，失败 {counter['fail']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["all", "words", "examples"], default="all")
    ap.add_argument("--force", action="store_true", help="重新生成已存在的音频")
    ap.add_argument("--db", default="", help="生产库路径，用于覆盖自建词库的词")
    args = ap.parse_args()

    texts = collect_texts(args.only, args.db)
    asyncio.run(main_async(texts, args.force))

    total = len(os.listdir(AUDIO_DIR))
    size = sum(os.path.getsize(os.path.join(AUDIO_DIR, f)) for f in os.listdir(AUDIO_DIR))
    print(f"音频目录共 {total} 个文件，{size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
