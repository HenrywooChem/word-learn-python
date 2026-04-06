"""
认证路由
"""
import uuid
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database import get_db
from models import User, UserProfile, UserCreate, UserResponse, LoginRequest, TokenResponse

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


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """用户注册"""
    try:
        # 检查用户名是否已存在
        existing = db.query(User).filter(User.username == user_data.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="用户名已存在")
        
        # 创建用户
        user_id = str(uuid.uuid4())
        hashed_password = get_password_hash(user_data.password)
        
        user = User(
            id=user_id,
            name=user_data.name,
            username=user_data.username,
            password_hash=hashed_password,
            role=user_data.role,
            parent_id=user_data.parent_id,
            created_at=datetime.now().strftime("%Y-%m-%d")
        )
        db.add(user)
        
        # 创建用户配置文件
        profile = UserProfile(
            user_id=user_id,
            total_score=0,
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
            user=UserResponse(
                id=user.id,
                name=user.name,
                username=user.username,
                role=user.role,
                parent_id=user.parent_id,
                avatar=user.avatar,
                created_at=user.created_at
            )
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
    """用户登录"""
    user = db.query(User).filter(User.username == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.id})
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            name=user.name,
            username=user.username,
            role=user.role,
            parent_id=user.parent_id,
            avatar=user.avatar,
            created_at=user.created_at
        )
    )


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """获取当前用户信息"""
    return UserResponse(
        id=current_user.id,
        name=current_user.name,
        username=current_user.username,
        role=current_user.role,
        parent_id=current_user.parent_id,
        avatar=current_user.avatar,
        created_at=current_user.created_at
    )
