from fastapi import APIRouter, HTTPException

from app.db import get_session
from app.schemas import UserCreate, UserResponse
from app.utils import hash_password

router = APIRouter()


@router.post("/register")
async def create_user(
        user: UserCreate
):
    if user.email:
        return HTTPException(status_code=400, detail="Email already registered")
    else:
        user.password = hash_password(user.password)
        session = get_session()
        session.add(user)
        session.commit()
        return UserResponse
