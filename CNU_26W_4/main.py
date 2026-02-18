from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import Optional
from app.items.items_router import items_router
from app.items.student import class_router
from app.week4.router import router
from app.week4.Item_router import router as item_router
from app.db import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.include_router(item_router)

