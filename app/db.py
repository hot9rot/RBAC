from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.models import Base
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL_asyncpg)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
