from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError, ExpiredSignatureError
from sqlalchemy.orm import Session
from .db import get_db
from .models import User
from .schemas import SignupRequest, UserResponse
from .utils import verify_password, get_password_hash, create_access_token, SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == request.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")
    if db.query(User).filter(User.email == request.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(request.password)
    new_user = User(
        username=request.username,
        email=request.email,
        password_hash=hashed_password,
        full_name=request.full_name,
        user_type=request.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "User created successfully"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
