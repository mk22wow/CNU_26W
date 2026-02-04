from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import Optional
from app.items.student import class_router

app = FastAPI()

@app.get(path="/")
async def root():
    return {"message": "Hello World"}

app.include_router(class_router)

