from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db import create_table, delete_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    await create_table()
    yield
    await delete_table()


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(reload=True)