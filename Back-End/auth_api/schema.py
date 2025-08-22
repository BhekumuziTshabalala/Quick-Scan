from pydantic import BaseModel, EmailStr
from .models import UserType

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str
    user_type: UserType

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    balance: float

    class Config:
        orm_mode = True
