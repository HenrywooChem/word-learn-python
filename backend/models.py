"""
SQLAlchemy 数据库模型定义
"""
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean, Text, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pydantic import BaseModel


class Base(DeclarativeBase):
    pass


# ===== SQLAlchemy 模型 =====

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)  # 'parent' or 'child'
    parent_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    avatar: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    created_at: Mapped[str] = mapped_column(String)
    
    # 关系
    profile: Mapped[Optional["UserProfile"]] = relationship("UserProfile", back_populates="user", uselist=False)
    custom_libraries: Mapped[List["WordLibrary"]] = relationship("WordLibrary", back_populates="created_by_user")
    learning_sessions: Mapped[List["LearningSession"]] = relationship("LearningSession", back_populates="user")
    daily_records: Mapped[List["DailyRecord"]] = relationship("DailyRecord", back_populates="user")
    wrong_questions: Mapped[List["WrongQuestion"]] = relationship("WrongQuestion", back_populates="user")
    review_records: Mapped[List["ReviewRecord"]] = relationship("ReviewRecord", back_populates="user")


class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), unique=True)
    total_score: Mapped[int] = mapped_column(Integer, default=0)
    last_sign_in: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    daily_goal: Mapped[int] = mapped_column(Integer, default=10)
    selected_library_ids: Mapped[str] = mapped_column(String, default="[]")  # JSON string
    
    user: Mapped["User"] = relationship("User", back_populates="profile")


class WordLibrary(Base):
    __tablename__ = "word_libraries"
    
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)  # 'system' or 'custom'
    grade: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    words: Mapped[str] = mapped_column(String)  # JSON string of words
    created_by: Mapped[Optional[str]] = mapped_column(String, ForeignKey("users.id"), nullable=True)
    created_at: Mapped[str] = mapped_column(String)
    
    created_by_user: Mapped[Optional["User"]] = relationship("User", back_populates="custom_libraries")


class LearningSession(Base):
    __tablename__ = "learning_sessions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
    date: Mapped[str] = mapped_column(String)
    word_id: Mapped[str] = mapped_column(String)
    pronunciation_score: Mapped[int] = mapped_column(Integer)
    meaning_score: Mapped[int] = mapped_column(Integer)
    total_score: Mapped[int] = mapped_column(Integer)
    
    user: Mapped["User"] = relationship("User", back_populates="learning_sessions")


class DailyRecord(Base):
    __tablename__ = "daily_records"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
    date: Mapped[str] = mapped_column(String)
    words_learned: Mapped[int] = mapped_column(Integer, default=0)
    total_score: Mapped[int] = mapped_column(Integer, default=0)
    signed_in: Mapped[bool] = mapped_column(Boolean, default=False)
    review_completed: Mapped[int] = mapped_column(Integer, default=0)  # 错题复习完成数
    
    user: Mapped["User"] = relationship("User", back_populates="daily_records")


# ===== 错题本模型 =====
class WrongQuestion(Base):
    """错题本 - 记录答错的单词"""
    __tablename__ = "wrong_questions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
    word_id: Mapped[str] = mapped_column(String)
    word: Mapped[str] = mapped_column(String)  # 单词
    phonetic: Mapped[str] = mapped_column(String)  # 发音
    meaning: Mapped[str] = mapped_column(String)  # 释义
    wrong_count: Mapped[int] = mapped_column(Integer, default=1)  # 错误次数
    correct_count: Mapped[int] = mapped_column(Integer, default=0)  # 正确次数
    status: Mapped[str] = mapped_column(String, default="reviewing")  # 'reviewing' 复习中, 'mastered' 已掌握
    next_review_date: Mapped[str] = mapped_column(String)  # 下次复习日期
    last_review_date: Mapped[str] = mapped_column(String)  # 上次复习日期
    created_at: Mapped[str] = mapped_column(String)
    updated_at: Mapped[str] = mapped_column(String)
    
    user: Mapped["User"] = relationship("User", back_populates="wrong_questions")


class ReviewRecord(Base):
    """复习记录 - 每次复习的结果"""
    __tablename__ = "review_records"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
    wrong_question_id: Mapped[int] = mapped_column(Integer, ForeignKey("wrong_questions.id"))
    review_date: Mapped[str] = mapped_column(String)
    score: Mapped[int] = mapped_column(Integer)  # 本次复习得分
    is_correct: Mapped[bool] = mapped_column(Boolean)  # 是否答对
    
    user: Mapped["User"] = relationship("User", back_populates="review_records")


# ===== Pydantic 模型 =====

class WordBase(BaseModel):
    id: str
    word: str
    phonetic: str
    meaning: str
    example_sentence: Optional[str] = None


class WordLibraryBase(BaseModel):
    id: str
    name: str
    type: str
    grade: Optional[str] = None
    description: Optional[str] = None
    words: List[WordBase]
    created_by: Optional[str] = None
    created_at: str


class UserCreate(BaseModel):
    name: str
    username: str
    password: str
    role: str
    parent_id: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    name: str
    username: str
    role: str
    parent_id: Optional[str] = None
    avatar: Optional[str] = None
    created_at: str


class UserProfileResponse(BaseModel):
    user_id: str
    total_score: int
    last_sign_in: Optional[str] = None
    daily_goal: int
    selected_library_ids: List[str]


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class LearningSessionCreate(BaseModel):
    word_id: str
    pronunciation_score: int
    meaning_score: int
    total_score: int


class DailyRecordResponse(BaseModel):
    user_id: str
    date: str
    words_learned: int
    total_score: int
    signed_in: bool
    review_completed: int = 0


# ===== 错题本模型 =====

class WrongQuestionBase(BaseModel):
    id: int
    word_id: str
    word: str
    phonetic: str
    meaning: str
    wrong_count: int
    correct_count: int
    status: str
    next_review_date: str
    last_review_date: str


class WrongQuestionCreate(BaseModel):
    word_id: str
    word: str
    phonetic: str
    meaning: str


class ReviewSubmit(BaseModel):
    wrong_question_id: int
    score: int  # 0-100


class ReviewStats(BaseModel):
    total_wrong: int
    reviewing: int
    mastered: int
    due_today: int
    review_history: List[dict]
