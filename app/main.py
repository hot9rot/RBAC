from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db import create_table, delete_table
from router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    await create_table()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)