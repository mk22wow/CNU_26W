from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from .Item_model import Item
from .Item_service import create_item, get_items

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=Item)
def create_new_item(item: Item, session: Session=Depends(get_session)):
    return create_item(session, item)

@router.get("/", response_model=list[Item])
def list_items(session: Session = Depends(get_session)):
    return get_items(session)

