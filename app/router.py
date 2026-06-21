from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Users, UserRole
from app.schemas import UserCreate, UserResponse
from app.utils import hash_password

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def create_user(
        user: UserCreate,
        session: AsyncSession = Depends(get_session)
):
    stmt = select(Users.id).where(Users.email == user.email).exists()
    result = await session.execute(select(stmt))
    email_exists = result.scalar()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        hashed_pwd = hash_password(user.password)
        db_user = Users(
            email=user.email,
            hashed_password=hashed_pwd,
            is_active=True,
            role=UserRole.USER
        )
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user
