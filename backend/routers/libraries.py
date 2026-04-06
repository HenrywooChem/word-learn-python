"""
词库管理路由
"""
import json
import uuid
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import WordLibrary, WordBase, WordLibraryBase, User, LearningSession
from routers.auth import get_current_user

router = APIRouter(prefix="/api/libraries", tags=["词库"])


@router.get("", response_model=List[WordLibraryBase])
def get_libraries(
    lib_type: Optional[str] = None,
    grade: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取词库列表"""
    query = db.query(WordLibrary)
    
    # 筛选系统词库或自定义词库
    if lib_type == "system":
        query = query.filter(WordLibrary.type == "system")
    elif lib_type == "custom":
        query = query.filter(WordLibrary.type == "custom").filter(WordLibrary.created_by == current_user.id)
    
    # 筛选年级
    if grade:
        query = query.filter(WordLibrary.grade == grade)
    
    libraries = query.all()
    
    result = []
    for lib in libraries:
        result.append(WordLibraryBase(
            id=lib.id,
            name=lib.name,
            type=lib.type,
            grade=lib.grade,
            description=lib.description,
            words=json.loads(lib.words),
            created_by=lib.created_by,
            created_at=lib.created_at
        ))
    
    return result


@router.get("/system", response_model=List[WordLibraryBase])
def get_system_libraries(
    grade: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取系统词库"""
    query = db.query(WordLibrary).filter(WordLibrary.type == "system")
    
    if grade:
        query = query.filter(WordLibrary.grade == grade)
    
    libraries = query.all()
    
    result = []
    for lib in libraries:
        result.append(WordLibraryBase(
            id=lib.id,
            name=lib.name,
            type=lib.type,
            grade=lib.grade,
            description=lib.description,
            words=json.loads(lib.words),
            created_by=lib.created_by,
            created_at=lib.created_at
        ))
    
    return result


@router.get("/custom", response_model=List[WordLibraryBase])
def get_custom_libraries(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取自定义词库"""
    libraries = db.query(WordLibrary).filter(
        WordLibrary.type == "custom",
        WordLibrary.created_by == current_user.id
    ).all()
    
    result = []
    for lib in libraries:
        result.append(WordLibraryBase(
            id=lib.id,
            name=lib.name,
            type=lib.type,
            grade=lib.grade,
            description=lib.description,
            words=json.loads(lib.words),
            created_by=lib.created_by,
            created_at=lib.created_at
        ))
    
    return result


@router.get("/{lib_id}", response_model=WordLibraryBase)
def get_library(
    lib_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取单个词库"""
    lib = db.query(WordLibrary).filter(WordLibrary.id == lib_id).first()
    
    if not lib:
        raise HTTPException(status_code=404, detail="词库不存在")
    
    # 自定义词库只能查看自己的
    if lib.type == "custom" and lib.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="无权限访问")
    
    return WordLibraryBase(
        id=lib.id,
        name=lib.name,
        type=lib.type,
        grade=lib.grade,
        description=lib.description,
        words=json.loads(lib.words),
        created_by=lib.created_by,
        created_at=lib.created_at
    )


@router.post("", response_model=WordLibraryBase)
def create_library(
    name: str,
    description: Optional[str] = None,
    words: List[WordBase] = [],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """创建自定义词库"""
    lib_id = f"custom-{uuid.uuid4().hex[:8]}"
    
    lib = WordLibrary(
        id=lib_id,
        name=name,
        type="custom",
        description=description,
        words=json.dumps([w.model_dump() for w in words], ensure_ascii=False),
        created_by=current_user.id,
        created_at=datetime.now().strftime("%Y-%m-%d")
    )
    
    db.add(lib)
    db.commit()
    db.refresh(lib)
    
    return WordLibraryBase(
        id=lib.id,
        name=lib.name,
        type=lib.type,
        grade=lib.grade,
        description=lib.description,
        words=json.loads(lib.words),
        created_by=lib.created_by,
        created_at=lib.created_at
    )


@router.put("/{lib_id}", response_model=WordLibraryBase)
def update_library(
    lib_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    words: Optional[List[WordBase]] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新自定义词库"""
    lib = db.query(WordLibrary).filter(WordLibrary.id == lib_id).first()
    
    if not lib:
        raise HTTPException(status_code=404, detail="词库不存在")
    
    if lib.type != "custom" or lib.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="无权限修改")
    
    if name:
        lib.name = name
    if description is not None:
        lib.description = description
    if words is not None:
        lib.words = json.dumps([w.model_dump() for w in words], ensure_ascii=False)
    
    db.commit()
    db.refresh(lib)
    
    return WordLibraryBase(
        id=lib.id,
        name=lib.name,
        type=lib.type,
        grade=lib.grade,
        description=lib.description,
        words=json.loads(lib.words),
        created_by=lib.created_by,
        created_at=lib.created_at
    )


@router.delete("/{lib_id}")
def delete_library(
    lib_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除自定义词库"""
    lib = db.query(WordLibrary).filter(WordLibrary.id == lib_id).first()
    
    if not lib:
        raise HTTPException(status_code=404, detail="词库不存在")
    
    if lib.type != "custom" or lib.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="无权限删除")
    
    db.delete(lib)
    db.commit()
    
    return {"message": "删除成功"}


@router.get("/{lib_id}/progress")
def get_library_progress(
    lib_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取词库学习进度"""
    lib = db.query(WordLibrary).filter(WordLibrary.id == lib_id).first()
    
    if not lib:
        raise HTTPException(status_code=404, detail="词库不存在")
    
    words = json.loads(lib.words)
    word_ids = [w["id"] for w in words]
    
    # 查询已学习的单词
    learned_sessions = db.query(LearningSession).filter(
        LearningSession.user_id == current_user.id,
        LearningSession.word_id.in_(word_ids)
    ).all()
    
    learned_word_ids = set(s.word_id for s in learned_sessions)
    
    return {
        "total": len(words),
        "learned": len(learned_word_ids),
        "progress": round(len(learned_word_ids) / len(words) * 100, 1) if words else 0
    }
