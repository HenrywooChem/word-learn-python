"""
学习路由 - 包含错题复习功能
"""
import json
import random
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import User, UserProfile, WordLibrary, LearningSession, DailyRecord, WordLibraryBase, WrongQuestion
from routers.auth import get_current_user
from routers.wrong_questions import add_to_wrong_book
from models import LearningSessionCreate

router = APIRouter(prefix="/api/learning", tags=["学习"])

# 新词和错题复习的比例
REVIEW_RATIO = 0.2  # 20% 复习错题，80% 新词


@router.get("/today")
def get_today_learning(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取今日学习数据 - 包含新词学习和错题复习"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 获取用户配置文件
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="用户配置不存在")
    
    daily_goal = profile.daily_goal
    
    # ===== 1. 获取今日需要复习的错题 =====
    review_words = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.status == "reviewing",
        WrongQuestion.next_review_date <= today
    ).order_by(WrongQuestion.next_review_date.asc()).all()
    
    # 随机打乱复习顺序
    review_words = list(review_words)
    random.shuffle(review_words)
    
    # 计算复习数量（根据比例）
    review_count = min(int(daily_goal * REVIEW_RATIO), len(review_words))
    review_words_today = review_words[:review_count]
    
    # ===== 2. 获取新词学习 =====
    # 获取今日已学习的新词单词ID
    today_sessions = db.query(LearningSession).filter(
        LearningSession.user_id == current_user.id,
        LearningSession.date == today
    ).all()
    learned_word_ids = [s.word_id for s in today_sessions]
    
    # 获取今日已复习的错题ID
    reviewed_wrong_ids = [q.word_id for q in review_words_today]
    
    # 获取选中的词库
    selected_lib_ids = json.loads(profile.selected_library_ids)
    all_new_words = []
    
    for lib_id in selected_lib_ids:
        lib = db.query(WordLibrary).filter(WordLibrary.id == lib_id).first()
        if lib:
            words = json.loads(lib.words)
            # 过滤掉已学习的和需要复习的
            remaining_words = [w for w in words if w["id"] not in learned_word_ids and w["id"] not in reviewed_wrong_ids]
            all_new_words.extend(remaining_words)
    
    # 随机打乱
    random.shuffle(all_new_words)
    
    # 新词数量 = 每日目标 - 复习数量
    new_count = daily_goal - review_count
    new_words_today = all_new_words[:max(new_count, 0)]
    
    # ===== 3. 合并今日任务 =====
    # 优先显示复习任务
    today_tasks = []
    
    # 添加复习任务（标记类型）
    for w in review_words_today:
        today_tasks.append({
            "type": "review",
            "id": w.id,
            "word_id": w.word_id,
            "word": w.word,
            "phonetic": w.phonetic,
            "meaning": w.meaning,
            "example_sentence": w.example_sentence or "",
            "wrong_count": w.wrong_count,
            "correct_count": w.correct_count
        })
    
    # 添加新词任务
    for w in new_words_today:
        today_tasks.append({
            "type": "new",
            "id": w["id"],
            "word_id": w["id"],
            "word": w["word"],
            "phonetic": w["phonetic"],
            "meaning": w["meaning"],
            "example_sentence": w.get("example_sentence", "")
        })
    
    # 随机打乱任务顺序（复习和新词交替）
    random.shuffle(today_tasks)
    
    # 获取今日记录
    daily_record = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()
    
    # 统计
    new_learned = daily_record.words_learned if daily_record else 0
    review_completed = daily_record.review_completed if daily_record else 0
    
    return {
        "daily_goal": daily_goal,
        "new_words_learned": new_learned,
        "review_completed": review_completed,
        "remaining_new": len(all_new_words),
        "remaining_review": len(review_words) - review_count,
        "today_tasks": today_tasks,
        "signed_in": daily_record.signed_in if daily_record else False,
        "total_score": daily_record.total_score if daily_record else 0,
        "review_count": len(review_words_today),
        "new_count": len(new_words_today)
    }


@router.post("/session")
def create_learning_session(
    session_data: LearningSessionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """创建学习记录 - 答错自动加入错题本"""
    today = datetime.now().strftime("%Y-%m-%d")
    is_wrong = session_data.total_score < 60  # 低于60分算答错
    
    # 创建学习记录
    session = LearningSession(
        user_id=current_user.id,
        date=today,
        word_id=session_data.word_id,
        pronunciation_score=session_data.pronunciation_score,
        meaning_score=session_data.meaning_score,
        total_score=session_data.total_score
    )
    db.add(session)
    
    # 如果答错，加入错题本
    if is_wrong:
        # 需要获取单词详情
        libraries = db.query(WordLibrary).all()
        word_info = None
        for lib in libraries:
            words = json.loads(lib.words)
            for w in words:
                if w["id"] == session_data.word_id:
                    word_info = w
                    break
            if word_info:
                break
        
        if word_info:
            add_to_wrong_book(
                db=db,
                user_id=current_user.id,
                word_id=session_data.word_id,
                word=word_info["word"],
                phonetic=word_info["phonetic"],
                meaning=word_info["meaning"]
            )
    
    # 更新用户总分
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if profile:
        profile.total_score += session_data.total_score
    
    # 更新或创建每日记录
    daily_record = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()
    
    if daily_record:
        daily_record.words_learned += 1
        daily_record.total_score += session_data.total_score
    else:
        daily_record = DailyRecord(
            user_id=current_user.id,
            date=today,
            words_learned=1,
            total_score=session_data.total_score,
            signed_in=False
        )
        db.add(daily_record)
    
    db.commit()
    
    return {
        "message": "学习记录已保存",
        "session_id": session.id,
        "added_to_wrong_book": is_wrong
    }


@router.post("/review")
def submit_review_result(
    wrong_question_id: int,
    score: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """提交错题复习结果"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    question = db.query(WrongQuestion).filter(
        WrongQuestion.id == wrong_question_id,
        WrongQuestion.user_id == current_user.id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="错题不存在")
    
    is_correct = score >= 60
    
    # 更新错题状态
    question.last_review_date = today
    question.correct_count += 1 if is_correct else 0
    question.wrong_count += 1 if not is_correct else 0
    
    # 更新熟悉度：答对+0.1，答错-0.1
    if is_correct:
        question.familiarity = round(question.familiarity + 0.1, 1)
    else:
        question.familiarity = round(max(question.familiarity - 0.1, 0.1), 1)
    
    # 计算下次复习日期
    from routers.wrong_questions import calculate_next_review
    question.next_review_date = calculate_next_review(question.wrong_count, question.correct_count)
    
    # 标记为已掌握
    if question.correct_count >= 5 and question.wrong_count <= 2:
        question.status = "mastered"
    
    question.updated_at = today
    
    # 添加复习记录
    from models import ReviewRecord
    record = ReviewRecord(
        user_id=current_user.id,
        wrong_question_id=wrong_question_id,
        review_date=today,
        score=score,
        is_correct=is_correct
    )
    db.add(record)
    
    # 更新今日复习完成数
    daily_record = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()
    
    if daily_record:
        daily_record.review_completed += 1
    else:
        daily_record = DailyRecord(
            user_id=current_user.id,
            date=today,
            words_learned=0,
            total_score=0,
            signed_in=False,
            review_completed=1
        )
        db.add(daily_record)
    
    # 奖励积分：答对+1，答错-0.5
    score_change = 1 if is_correct else -0.5
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if profile:
        profile.total_score += score_change
    
    db.commit()
    
    return {
        "message": "复习记录已保存",
        "is_correct": is_correct,
        "next_review_date": question.next_review_date,
        "status": question.status,
        "score_change": score_change,
        "total_score": profile.total_score if profile else 0,
        "familiarity": question.familiarity
    }


@router.post("/signin")
def sign_in(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """每日签到 - 赠送1积分，连续签到额外奖励"""
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    # 检查今日是否已签到
    daily_record = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()
    
    if daily_record and daily_record.signed_in:
        raise HTTPException(status_code=400, detail="今日已签到")
    
    # 签到基础积分
    bonus_score = 1
    
    # 更新用户总分和连续签到天数
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if profile:
        # 判断是否连续签到：上次签到是昨天
        if profile.last_sign_in == yesterday:
            profile.continuous_signin_days += 1
        elif profile.last_sign_in == today:
            # 今天已签到（上面的检查应该已拦截，但保险起见）
            pass
        else:
            # 不连续，重新计数
            profile.continuous_signin_days = 1
        
        # 连续签到奖励
        continuous_bonus = 0
        if profile.continuous_signin_days >= 30:
            continuous_bonus = 50
        elif profile.continuous_signin_days >= 7:
            continuous_bonus = 10
        
        bonus_score += continuous_bonus
        profile.total_score += bonus_score
        profile.last_sign_in = today
    
    if daily_record:
        daily_record.signed_in = True
        daily_record.total_score += bonus_score
    else:
        daily_record = DailyRecord(
            user_id=current_user.id,
            date=today,
            words_learned=0,
            total_score=bonus_score,
            signed_in=True
        )
        db.add(daily_record)
    
    db.commit()
    
    result = {
        "message": "签到成功",
        "bonus_score": bonus_score,
        "continuous_signin_days": profile.continuous_signin_days if profile else 0
    }
    if profile and profile.continuous_signin_days >= 7:
        result["continuous_bonus"] = bonus_score - 1
        result["message"] += f"，连续签到{profile.continuous_signin_days}天，额外奖励{bonus_score - 1}积分！"
    
    return result


@router.get("/random-words")
def get_random_words(
    count: int = 10,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取随机单词用于测试"""
    # 获取所有系统词库
    libraries = db.query(WordLibrary).filter(WordLibrary.type == "system").all()
    
    all_words = []
    for lib in libraries:
        words = json.loads(lib.words)
        all_words.extend(words)
    
    # 随机选择
    random.shuffle(all_words)
    selected = all_words[:count]
    
    # 隐藏含义
    return selected


@router.get("/quiz-options")
def get_quiz_options(
    word_id: str = Query(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取4选1选择题选项"""
    # 获取该单词
    libraries = db.query(WordLibrary).all()
    target_word = None
    
    for lib in libraries:
        words = json.loads(lib.words)
        for w in words:
            if w["id"] == word_id:
                target_word = w
                break
        if target_word:
            break
    
    # 如果没找到（可能是错题本里的）
    if not target_word:
        wrong = db.query(WrongQuestion).filter(
            WrongQuestion.word_id == word_id,
            WrongQuestion.user_id == current_user.id
        ).first()
        if wrong:
            target_word = {
                "id": wrong.word_id,
                "word": wrong.word,
                "meaning": wrong.meaning
            }
    
    if not target_word:
        raise HTTPException(status_code=404, detail="单词不存在")
    
    # 优先使用预设选项（如果词库中已定义 A/B/C/D 选项）
    predefined_options = target_word.get("options")
    if predefined_options and isinstance(predefined_options, list) and len(predefined_options) == 4:
        options = predefined_options
    else:
        # 没有预设选项时，自动生成
        all_words = []
        for lib in libraries:
            words = json.loads(lib.words)
            all_words.extend(words)
        
        target_meaning = target_word.get("meaning", "")
        other_words = [w for w in all_words if w["id"] != word_id]
        
        # 过滤掉含义相似的干扰项
        filtered_distractors = []
        used_meanings = [target_meaning]
        
        random.shuffle(other_words)
        for w in other_words:
            if len(filtered_distractors) >= 3:
                break
            meaning = w.get("meaning", "")
            if meaning and meaning not in used_meanings:
                is_similar = False
                for used in used_meanings:
                    common_chars = set(meaning) & set(used)
                    if len(common_chars) / max(len(set(meaning) | set(used)), 1) > 0.5:
                        is_similar = True
                        break
                if not is_similar:
                    filtered_distractors.append(w)
                    used_meanings.append(meaning)
        
        if len(filtered_distractors) < 3:
            filtered_distractors = other_words[:3]
        
        distractors = filtered_distractors[:3]
        
        options = [
            {"text": target_word["meaning"], "correct": True},
            {"text": distractors[0]["meaning"], "correct": False},
            {"text": distractors[1]["meaning"], "correct": False},
            {"text": distractors[2]["meaning"], "correct": False},
        ]
        random.shuffle(options)
    
    return {
        "word_id": word_id,
        "word": target_word.get("word", target_word.get("word")),
        "phonetic": target_word.get("phonetic", ""),
        "meaning": target_word.get("meaning", ""),
        "example_sentence": target_word.get("example_sentence", ""),
        "options": options
    }


@router.post("/submit-quiz")
async def submit_quiz_result(
    request: Request,
    word_id: str = Query(None),
    selected_meaning: str = Query(None),
    pronunciation_score: int = Query(50),
    task_type: str = Query("new"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """提交选择题结果"""
    # 兼容：优先从 query string 读取，也支持 JSON body
    if not word_id or not selected_meaning:
        try:
            body = await request.json()
            word_id = word_id or body.get("word_id")
            selected_meaning = selected_meaning or body.get("selected_meaning")
            pronunciation_score = body.get("pronunciation_score", pronunciation_score)
            task_type = body.get("task_type", task_type)
        except:
            pass
    
    if not word_id or not selected_meaning:
        return {"detail": "Missing word_id or selected_meaning"}
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 获取该单词
    libraries = db.query(WordLibrary).all()
    target_word = None
    
    for lib in libraries:
        words = json.loads(lib.words)
        for w in words:
            if w["id"] == word_id:
                target_word = w
                break
        if target_word:
            break
    
    # 检查答案是否正确
    is_correct = target_word and target_word["meaning"] == selected_meaning
    
    # 计算分数
    meaning_score = 50 if is_correct else 0
    total_score = pronunciation_score + meaning_score
    
    # 积分变动
    score_change = 0
    if is_correct:
        score_change = 1  # 答对+1分
    else:
        score_change = -0.5  # 答错-0.5分
    
    # 创建学习记录
    session = LearningSession(
        user_id=current_user.id,
        date=today,
        word_id=word_id,
        pronunciation_score=pronunciation_score,
        meaning_score=meaning_score,
        total_score=total_score
    )
    db.add(session)
    
    # 如果答错，加入错题本
    if not is_correct and target_word:
        add_to_wrong_book(
            db=db,
            user_id=current_user.id,
            word_id=word_id,
            word=target_word["word"],
            phonetic=target_word.get("phonetic", ""),
            meaning=target_word["meaning"]
        )
    
    # 更新错题本中的熟悉度（答对+0.1，答错-0.1）
    wrong_entry = db.query(WrongQuestion).filter(
        WrongQuestion.user_id == current_user.id,
        WrongQuestion.word_id == word_id
    ).first()
    if wrong_entry:
        if is_correct:
            wrong_entry.familiarity = round(wrong_entry.familiarity + 0.1, 1)
        else:
            wrong_entry.familiarity = round(max(wrong_entry.familiarity - 0.1, 0.1), 1)
    
    # 更新用户总分（含积分变动）
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if profile:
        profile.total_score += score_change
    
    # 更新或创建每日记录
    daily_record = db.query(DailyRecord).filter(
        DailyRecord.user_id == current_user.id,
        DailyRecord.date == today
    ).first()
    
    if daily_record:
        daily_record.words_learned += 1
        daily_record.total_score += score_change
    else:
        daily_record = DailyRecord(
            user_id=current_user.id,
            date=today,
            words_learned=1,
            total_score=score_change,
            signed_in=False
        )
        db.add(daily_record)
    
    db.commit()
    
    return {
        "is_correct": is_correct,
        "meaning_score": meaning_score,
        "pronunciation_score": pronunciation_score,
        "total_score": total_score,
        "score_change": score_change,  # 本次积分变动
        "user_total_score": profile.total_score if profile else 0,  # 用户总积分
        "correct_meaning": target_word["meaning"] if target_word else "",
        "added_to_wrong_book": not is_correct and target_word is not None
    }
