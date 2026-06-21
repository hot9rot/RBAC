from pydantic import BaseModel, Field, EmailStr

from app.models import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    role: UserRole

    class Config:
        from_attributes = True
