import sys
import asyncio

# фикс для работы asyncpg на Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db import create_table, delete_table
from app.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)