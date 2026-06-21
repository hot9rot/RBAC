import enum
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserRole(enum.Enum):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"


class Users(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = True
    role: Mapped[UserRole] = mapped_column(Enum(UserRole))
