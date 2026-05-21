"""
记录与统计路由
"""
import json
from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import User, UserProfile, WordLibrary, LearningSession, DailyRecord
from routers.auth import get_current_user

router = APIRouter(prefix="/api/records", tags=["记录"])


@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取用户资料和统计"""
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    if not profile:
        return {
            "user_id": current_user.id,
            "total_score": 0,
            "last_sign_in": None,
            "daily_goal": 10,
            "selected_library_ids": [],
            "continuous_signin_days": 0
        }
    
    # 获取总学习天数
    total_days = db.query(func.count(func.distinct(DailyRecord.date))).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.words_learned > 0
    ).scalar() or 0
    
    # 获取已掌握单词数（得分>=80的）
    mastered_count = db.query(func.count(func.distinct(LearningSession.word_id))).filter(
        LearningSession.user_id == current_user.id,
        LearningSession.total_score >= 80
    ).scalar() or 0
    
    return {
        "user_id": profile.user_id,
        "total_score": profile.total_score,
        "last_sign_in": profile.last_sign_in,
        "daily_goal": profile.daily_goal,
        "selected_library_ids": json.loads(profile.selected_library_ids),
        "continuous_signin_days": profile.continuous_signin_days,
        "total_days": total_days,
        "mastered_words": mastered_count
    }


@router.put("/profile")
def update_profile(
    daily_goal: int = Body(None),
    selected_library_ids: List[str] = Body(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新用户设置"""
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="用户配置不存在")
    
    if daily_goal is not None:
        profile.daily_goal = daily_goal
    
    if selected_library_ids is not None:
        profile.selected_library_ids = json.dumps(selected_library_ids)
    
    db.commit()
    
    return {"message": "设置已更新"}


@router.get("/daily")
def get_daily_records(
    days: int = 7,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取每日学习记录"""
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    records = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date >= start_date
    ).order_by(DailyRecord.date.desc()).all()
    
    return [
        {
            "date": r.date,
            "words_learned": r.words_learned,
            "total_score": r.total_score,
            "signed_in": r.signed_in
        }
        for r in records
    ]


@router.get("/history")
def get_learning_history(
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取学习历史"""
    sessions = db.query(LearningSession).filter(
        LearningSession.user_id == current_user.id
    ).order_by(LearningSession.date.desc()).limit(limit).all()
    
    # 获取单词信息
    word_ids = list(set(s.word_id for s in sessions))
    libraries = db.query(WordLibrary).all()
    
    word_map = {}
    for lib in libraries:
        words = json.loads(lib.words)
        for w in words:
            word_map[w["id"]] = w
    
    result = []
    for s in sessions:
        word_info = word_map.get(s.word_id, {})
        result.append({
            "id": s.id,
            "date": s.date,
            "word": word_info.get("word", ""),
            "meaning": word_info.get("meaning", ""),
            "pronunciation_score": s.pronunciation_score,
            "meaning_score": s.meaning_score,
            "total_score": s.total_score
        })
    
    return result


@router.get("/stats")
def get_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取学习统计"""
    # 连续学习天数
    records = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.words_learned > 0
    ).order_by(DailyRecord.date.desc()).all()
    
    streak = 0
    today = datetime.now().date()
    
    for i, r in enumerate(records):
        record_date = datetime.strptime(r.date, "%Y-%m-%d").date()
        expected_date = today - timedelta(days=i)
        
        if record_date == expected_date:
            streak += 1
        else:
            break
    
    # 总学习单词数
    total_words = db.query(func.count(func.distinct(LearningSession.word_id))).filter(
        LearningSession.user_id == current_user.id
    ).scalar() or 0
    
    # 总学习次数
    total_sessions = db.query(func.count(LearningSession.id)).filter(
        LearningSession.user_id == current_user.id
    ).scalar() or 0
    
    # 平均分数
    avg_score = db.query(func.avg(LearningSession.total_score)).filter(
        LearningSession.user_id == current_user.id
    ).scalar() or 0
    
    return {
        "streak_days": streak,
        "total_words": total_words,
        "total_sessions": total_sessions,
        "average_score": round(avg_score, 1)
    }
