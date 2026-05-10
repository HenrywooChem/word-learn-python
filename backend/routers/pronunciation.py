"""
朗读评分 API - 路由文件
将上传到 /app/backend/routers/pronunciation.py
"""
import difflib
import re
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import User, UserProfile, WrongQuestion, DailyRecord
from routers.auth import get_current_user

router = APIRouter(prefix="/api/pronunciation", tags=["朗读评分"])


def normalize_text(text: str) -> str:
    """标准化文本：去除标点、转小写、去除空格"""
    text = re.sub(r"[^\w\s]", "", text)
    return text.lower().strip()


def compute_score(recognized: str, expected: str) -> tuple[int, float, str]:
    """
    计算读音得分
    返回: (score_0_100, similarity_0_1, feedback_cn)
    """
    rec = normalize_text(recognized)
    exp = normalize_text(expected)

    if not rec:
        return 0, 0.0, "没有检测到声音，请重试"

    if rec == exp:
        return 100, 1.0, "发音完美！🎉"

    sim = difflib.SequenceMatcher(None, rec, exp).ratio()

    if sim >= 0.85:
        score = int(80 + sim * 20)
        feedback = "发音很棒！继续加油！"
    elif sim >= 0.65:
        score = int(55 + (sim - 0.65) * 150)
        feedback = "基本正确，可以再练习"
    elif sim >= 0.4:
        score = int(25 + (sim - 0.4) * 100)
        feedback = "注意发音节奏，再听几遍"
    else:
        score = int(sim * 60)
        feedback = "多听几遍标准发音，跟读练习"

    return min(100, max(0, score)), round(sim, 3), feedback


# ========================
# API 端点
# ========================

class PronunciationCheckIn(BaseModel):
    recognized_text: str
    expected_word: str
    word_id: str


class PronunciationResult(BaseModel):
    score: int
    similarity: float
    feedback: str
    recognized_text: str


class PronunciationSubmitIn(BaseModel):
    word_id: str
    word: str
    phonetic: str = ""
    meaning: str = ""
    recognized_text: str
    pronunciation_score: int
    meaning_score: int = 50
    task_type: str = "new"  # "new" or "review"


@router.post("/check", response_model=PronunciationResult)
def check_pronunciation(
    body: PronunciationCheckIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    朗读评分 API
    - 接收浏览器 SpeechRecognition 识别的文本
    - 与目标单词比对，计算相似度
    - 返回得分和中文反馈
    """
    score, sim, feedback = compute_score(body.recognized_text, body.expected_word)

    return PronunciationResult(
        score=score,
        similarity=sim,
        feedback=feedback,
        recognized_text=body.recognized_text,
    )


@router.post("/submit")
def submit_with_pronunciation(
    body: PronunciationSubmitIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    同时提交选择题得分和朗读得分
    更新数据库中的熟悉度
    """
    today = datetime.now().strftime("%Y-%m-%d")

    # 判断是否正确（两个维度都 >= 50 算对）
    is_correct = body.pronunciation_score >= 50 and body.meaning_score >= 50

    # 找到或创建错题记录
    wrong_entry = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.word_id == body.word_id
    ).first()

    if wrong_entry:
        if is_correct:
            # 答对：熟悉度 +0.1，正确次数 +1
            wrong_entry.familiarity = round(min(wrong_entry.familiarity + 0.1, 5.0), 1)
            wrong_entry.correct_count += 1
            # 连续答对 3 次视为掌握
            if wrong_entry.correct_count >= 3:
                wrong_entry.status = "mastered"
        else:
            # 答错：熟悉度 -0.1，错误次数 +1，重置正确计数
            wrong_entry.familiarity = round(max(wrong_entry.familiarity - 0.1, 0.1), 1)
            wrong_entry.wrong_count += 1
            wrong_entry.correct_count = 0
            wrong_entry.status = "reviewing"
    elif not is_correct and body.task_type == "new":
        # 新单词首次答错，创建错题记录
        wrong_entry = WrongQuestion(
            user_id=current_user.id,
            word_id=body.word_id,
            word=body.word,
            phonetic=body.phonetic,
            meaning=body.meaning,
            familiarity=1.0,
            wrong_count=1,
            correct_count=0,
            status="reviewing",
            next_review_date=today,
            last_review_date=today,
            created_at=today,
            updated_at=today,
        )
        db.add(wrong_entry)

    # 更新用户总分
    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()

    score_change = 1 if is_correct else -0.5
    if profile:
        profile.total_score += score_change

    # 更新每日记录
    daily = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()

    if daily:
        daily.words_learned += 1
        daily.total_score += score_change
    else:
        daily = DailyRecord(
            user_id=current_user.id,
            date=today,
            words_learned=1,
            total_score=score_change,
            signed_in=False,
            review_completed=0,
        )
        db.add(daily)

    db.commit()
    db.refresh(profile)

    return {
        "is_correct": is_correct,
        "score_change": score_change,
        "user_total_score": profile.total_score if profile else 0,
        "familiarity": wrong_entry.familiarity if wrong_entry else 1.0,
        "wrong_book_added": wrong_entry is not None and wrong_entry.id is not None,
    }
