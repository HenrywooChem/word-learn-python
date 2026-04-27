"""
认证路由
"""
import re
import uuid
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database import get_db
from models import (
    User, UserProfile, UserCreate, UserResponse, LoginRequest, TokenResponse,
    ChangePasswordRequest, ChangeUsernameRequest, ChangeEmailRequest, ChangePhoneRequest,
    ResetPasswordRequest
)

router = APIRouter(prefix="/api/auth", tags=["认证"])

# 密码加密
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 配置
SECRET_KEY = "word-learn-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7天

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """创建 JWT token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # jose 库需要 Unix 时间戳格式
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    # bcrypt 有 72 字节限制
    return pwd_context.verify(plain_password[:72], hashed_password)


def get_password_hash(password: str) -> str:
    """密码哈希"""
    # bcrypt 有 72 字节限制
    return pwd_context.hash(password[:72])


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无效的认证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user


def _build_user_response(user: User) -> UserResponse:
    """构建用户响应"""
    return UserResponse(
        id=user.id,
        name=user.name,
        username=user.username,
        phone=user.phone,
        email=user.email,
        role=user.role,
        parent_id=user.parent_id,
        avatar=user.avatar,
        created_at=user.created_at
    )


def _is_valid_phone(phone: str) -> bool:
    """验证手机号格式（中国大陆手机号）"""
    return bool(re.match(r'^1[3-9]\d{9}$', phone))


def _is_valid_email(email: str) -> bool:
    """验证邮箱格式"""
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def _find_user_by_login_id(db: Session, login_id: str) -> Optional[User]:
    """通过用户名、手机号或邮箱查找用户"""
    user = db.query(User).filter(User.username == login_id).first()
    if user:
        return user
    user = db.query(User).filter(User.phone == login_id).first()
    if user:
        return user
    user = db.query(User).filter(User.email == login_id).first()
    return user


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """用户注册（支持用户名、手机号、邮箱）"""
    try:
        # 至少需要一个登录方式
        if not user_data.username and not user_data.phone and not user_data.email:
            raise HTTPException(status_code=400, detail="请至少提供用户名、手机号或邮箱")

        # 验证并检查用户名
        if user_data.username:
            existing = db.query(User).filter(User.username == user_data.username).first()
            if existing:
                raise HTTPException(status_code=400, detail="用户名已存在")

        # 验证并检查手机号
        if user_data.phone:
            if not _is_valid_phone(user_data.phone):
                raise HTTPException(status_code=400, detail="手机号格式不正确")
            existing = db.query(User).filter(User.phone == user_data.phone).first()
            if existing:
                raise HTTPException(status_code=400, detail="该手机号已被注册")

        # 验证并检查邮箱
        if user_data.email:
            if not _is_valid_email(user_data.email):
                raise HTTPException(status_code=400, detail="邮箱格式不正确")
            existing = db.query(User).filter(User.email == user_data.email).first()
            if existing:
                raise HTTPException(status_code=400, detail="该邮箱已被注册")

        # 创建用户
        user_id = str(uuid.uuid4())
        hashed_password = get_password_hash(user_data.password)
        
        # 如果没有提供用户名，用手机号或邮箱作为显示名
        name = user_data.name
        if not name:
            name = user_data.username or user_data.phone or user_data.email
        
        # 如果没有提供用户名，生成一个唯一用户名
        username = user_data.username
        if not username:
            if user_data.phone:
                username = f"user_{user_data.phone[-4:]}"
            elif user_data.email:
                username = user_data.email.split('@')[0]
            else:
                username = f"user_{uuid.uuid4().hex[:8]}"
            # 确保生成的用户名唯一
            base_username = username
            counter = 1
            while db.query(User).filter(User.username == username).first():
                username = f"{base_username}_{counter}"
                counter += 1

        user = User(
            id=user_id,
            name=name,
            username=username,
            password_hash=hashed_password,
            phone=user_data.phone,
            email=user_data.email,
            role=user_data.role,
            parent_id=user_data.parent_id,
            created_at=datetime.now().strftime("%Y-%m-%d")
        )
        db.add(user)
        
        # 创建用户配置文件
        profile = UserProfile(
            user_id=user_id,
            total_score=100,  # 注册赠送100积分
            daily_goal=10,
            selected_library_ids="[]"
        )
        db.add(profile)
        
        db.commit()
        db.refresh(user)
        
        # 生成 token
        access_token = create_access_token(data={"sub": user.id})
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=_build_user_response(user)
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"注册错误: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """用户登录（支持用户名、手机号、邮箱登录）"""
    user = _find_user_by_login_id(db, form_data.username)
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名/手机号/邮箱或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.id})
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=_build_user_response(user)
    )


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """获取当前用户信息"""
    return _build_user_response(current_user)


@router.put("/change-password")
def change_password(
    req: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """修改密码"""
    if not verify_password(req.old_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="旧密码错误")
    
    if len(req.new_password) < 6:
        raise HTTPException(status_code=400, detail="新密码长度不能少于6位")
    
    current_user.password_hash = get_password_hash(req.new_password)
    db.commit()
    
    return {"message": "密码修改成功"}


@router.put("/change-username")
def change_username(
    req: ChangeUsernameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """修改用户名"""
    if not req.new_username or len(req.new_username.strip()) < 2:
        raise HTTPException(status_code=400, detail="用户名长度不能少于2个字符")
    
    if req.new_username == current_user.username:
        raise HTTPException(status_code=400, detail="新用户名与当前用户名相同")
    
    existing = db.query(User).filter(User.username == req.new_username).first()
    if existing:
        raise HTTPException(status_code=400, detail="该用户名已被占用")
    
    current_user.username = req.new_username
    db.commit()
    
    return {"message": "用户名修改成功", "user": _build_user_response(current_user)}


@router.put("/change-email")
def change_email(
    req: ChangeEmailRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """修改邮箱（传入 null 可解绑）"""
    if req.new_email is not None:
        if not _is_valid_email(req.new_email):
            raise HTTPException(status_code=400, detail="邮箱格式不正确")
        if req.new_email == current_user.email:
            raise HTTPException(status_code=400, detail="新邮箱与当前邮箱相同")
        existing = db.query(User).filter(User.email == req.new_email).first()
        if existing:
            raise HTTPException(status_code=400, detail="该邮箱已被其他账号使用")
    
    current_user.email = req.new_email
    db.commit()
    
    return {"message": "邮箱修改成功", "user": _build_user_response(current_user)}


@router.put("/change-phone")
def change_phone(
    req: ChangePhoneRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """修改手机号（传入 null 可解绑）"""
    if req.new_phone is not None:
        if not _is_valid_phone(req.new_phone):
            raise HTTPException(status_code=400, detail="手机号格式不正确")
        if req.new_phone == current_user.phone:
            raise HTTPException(status_code=400, detail="新手机号与当前手机号相同")
        existing = db.query(User).filter(User.phone == req.new_phone).first()
        if existing:
            raise HTTPException(status_code=400, detail="该手机号已被其他账号使用")
    
    current_user.phone = req.new_phone
    db.commit()
    
    return {"message": "手机号修改成功", "user": _build_user_response(current_user)}


@router.post("/reset-password")
def reset_password(req: ResetPasswordRequest, db: Session = Depends(get_db)):
    """通过用户名+手机号/邮箱验证身份后重置密码（无需登录）"""
    if len(req.new_password) < 6:
        raise HTTPException(status_code=400, detail="新密码长度不能少于6位")
    
    if not req.phone and not req.email:
        raise HTTPException(status_code=400, detail="请提供手机号或邮箱以验证身份")
    
    # 通过用户名查找用户
    user = db.query(User).filter(User.username == req.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="用户名不存在")
    
    # 验证手机号（如果提供了）
    if req.phone:
        if not user.phone or user.phone != req.phone:
            raise HTTPException(status_code=400, detail="手机号与账号不匹配")
    
    # 验证邮箱（如果提供了）
    if req.email:
        if not user.email or user.email != req.email:
            raise HTTPException(status_code=400, detail="邮箱与账号不匹配")
    
    # 重置密码
    user.password_hash = get_password_hash(req.new_password)
    db.commit()
    
    return {"message": "密码重置成功，请使用新密码登录"}
