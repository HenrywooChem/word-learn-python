"""
错题本路由 - 遗忘曲线复习系统
"""
import json
from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User, WrongQuestion, ReviewRecord, WordLibrary
from routers.auth import get_current_user

router = APIRouter(prefix="/api/wrong-questions", tags=["错题本"])

# 遗忘曲线复习间隔（天）
# 首次错误后1天复习，然后3天，7天，15天，30天
EBBINGHAUS_INTERVALS = [1, 3, 7, 15, 30]


def calculate_next_review(wrong_count: int, correct_count: int) -> str:
    """
    根据艾宾浩斯遗忘曲线计算下次复习日期
    - 错误次数越多，复习间隔越短
    - 连续正确次数越多，复习间隔越长
    """
    # 根据错误次数确定当前处于哪个复习阶段
    stage = min(wrong_count - 1, len(EBBINGHAUS_INTERVALS) - 1) if wrong_count > 0 else 0
    
    # 如果连续正确，增加间隔
    if correct_count > 0:
        # 每连续正确2次，升一级
        stage = min(stage + correct_count // 2, len(EBBINGHAUS_INTERVALS) - 1)
    
    days_to_add = EBBINGHAUS_INTERVALS[stage] if stage < len(EBBINGHAUS_INTERVALS) else 30
    next_date = datetime.now() + timedelta(days=days_to_add)
    return next_date.strftime("%Y-%m-%d")


@router.get("")
def get_wrong_questions(
    status: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取错题本列表"""
    query = db.query(WrongQuestion).filter(WrongQuestion.user_id == current_user.id)
    
    if status:
        query = query.filter(WrongQuestion.status == status)
    
    questions = query.order_by(WrongQuestion.next_review_date.asc()).all()
    
    return [
        {
            "id": q.id,
            "word_id": q.word_id,
            "word": q.word,
            "phonetic": q.phonetic,
            "meaning": q.meaning,
            "familiarity": q.familiarity,
            "wrong_count": q.wrong_count,
            "correct_count": q.correct_count,
            "status": q.status,
            "next_review_date": q.next_review_date,
            "last_review_date": q.last_review_date
        }
        for q in questions
    ]


@router.get("/due-today")
def get_due_review_words(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取今日需要复习的错题"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 查找所有状态为复习中且到期或过期的错题
    questions = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.status == "reviewing",
        WrongQuestion.next_review_date <= today
    ).order_by(WrongQuestion.next_review_date.asc()).all()
    
    return [
        {
            "id": q.id,
            "word_id": q.word_id,
            "word": q.word,
            "phonetic": q.phonetic,
            "meaning": q.meaning,
            "wrong_count": q.wrong_count,
            "correct_count": q.correct_count,
            "next_review_date": q.next_review_date
        }
        for q in questions
    ]


@router.get("/stats")
def get_review_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取错题本统计"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    total = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id
    ).count()
    
    reviewing = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.status == "reviewing"
    ).count()
    
    mastered = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.status == "mastered"
    ).count()
    
    due_today = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.status == "reviewing",
        WrongQuestion.next_review_date <= today
    ).count()
    
    # 获取最近复习记录
    recent_records = db.query(ReviewRecord).filter(
        ReviewRecord.user_id == current_user.id
    ).order_by(ReviewRecord.review_date.desc()).limit(20).all()
    
    review_history = []
    for r in recent_records:
        question = db.query(WrongQuestion).filter(WrongQuestion.id == r.wrong_question_id).first()
        if question:
            review_history.append({
                "date": r.review_date,
                "word": question.word,
                "score": r.score,
                "is_correct": r.is_correct
            })
    
    return {
        "total_wrong": total,
        "reviewing": reviewing,
        "mastered": mastered,
        "due_today": due_today,
        "review_history": review_history
    }


@router.post("/review")
def submit_review(
    wrong_question_id: int,
    score: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """提交复习结果"""
    question = db.query(WrongQuestion).filter(
        WrongQuestion.id == wrong_question_id,
        WrongQuestion.user_id == current_user.id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="错题不存在")
    
    today = datetime.now().strftime("%Y-%m-%d")
    is_correct = score >= 60  # 60分以上算正确
    
    # 更新复习记录
    question.last_review_date = today
    question.correct_count += 1 if is_correct else 0
    question.wrong_count += 1 if not is_correct else 0
    
    # 计算下次复习日期
    question.next_review_date = calculate_next_review(
        question.wrong_count, 
        question.correct_count
    )
    
    # 如果连续正确达到一定次数，标记为已掌握
    if question.correct_count >= 5 and question.wrong_count <= 2:
        question.status = "mastered"
    
    question.updated_at = today
    
    # 添加复习记录
    record = ReviewRecord(
        user_id=current_user.id,
        wrong_question_id=wrong_question_id,
        review_date=today,
        score=score,
        is_correct=is_correct
    )
    db.add(record)
    
    # 更新今日复习完成数
    daily_record = db.query(ReviewRecord).filter(
        ReviewRecord.user_id == current_user.id,
        ReviewRecord.review_date == today
    ).count()
    
    db.commit()
    
    return {
        "message": "复习记录已保存",
        "is_correct": is_correct,
        "next_review_date": question.next_review_date,
        "status": question.status
    }


@router.delete("/{question_id}")
def delete_wrong_question(
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """从错题本删除（放弃某错题）"""
    question = db.query(WrongQuestion).filter(
        WrongQuestion.id == question_id,
        WrongQuestion.user_id == current_user.id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="错题不存在")
    
    # 删除相关的复习记录
    db.query(ReviewRecord).filter(
        ReviewRecord.wrong_question_id == question_id
    ).delete()
    
    db.delete(question)
    db.commit()
    
    return {"message": "已从错题本删除"}


@router.post("/reset/{question_id}")
def reset_wrong_question(
    question_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """重新学习错题（重置复习进度）"""
    question = db.query(WrongQuestion).filter(
        WrongQuestion.id == question_id,
        WrongQuestion.user_id == current_user.id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="错题不存在")
    
    question.status = "reviewing"
    question.wrong_count = 0
    question.correct_count = 0
    question.next_review_date = datetime.now().strftime("%Y-%m-%d")
    question.updated_at = datetime.now().strftime("%Y-%m-%d")
    
    db.commit()
    
    return {"message": "已重置复习进度"}


def add_to_wrong_book(
    db: Session,
    user_id: str,
    word_id: str,
    word: str,
    phonetic: str,
    meaning: str
):
    """
    将单词添加到错题本
    如果已存在，则增加错误次数
    """
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 检查是否已存在
    existing = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == user_id,
        WrongQuestion.word_id == word_id
    ).first()
    
    if existing:
        # 已存在，增加错误次数
        existing.wrong_count += 1
        existing.last_review_date = today
        # 重新计算复习日期（缩短间隔）
        existing.next_review_date = calculate_next_review(
            existing.wrong_count,
            existing.correct_count
        )
        existing.status = "reviewing"  # 重新开始复习
        existing.updated_at = today
    else:
        # 新增错题
        question = WrongQuestion(
            user_id=user_id,
            word_id=word_id,
            word=word,
            phonetic=phonetic,
            meaning=meaning,
            familiarity=1.0,  # 初始熟悉度
            wrong_count=1,
            correct_count=0,
            status="reviewing",
            next_review_date=today,  # 今天就需要复习
            last_review_date=today,
            created_at=today,
            updated_at=today
        )
        db.add(question)
    
    db.commit()
