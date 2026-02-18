from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from .model import User
from .service import create_user, get_users, get_user_by_id, delete_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create(user:User, session: Session=Depends(get_session)):
    return create_user(session, user)

@router.get("/", response_model=list[User])
def list_all(session: Session = Depends(get_session)):
    return get_users(session)

@router.get("/{user_id}", response_model=User)
def get_one(user_id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user_handler(user_id: int, session: Session = Depends(get_session)):
    success = delete_user(session, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="삭제할 유저를 찾을 수 없습니다.")
    return {"message": "성공적으로 삭제되었습니다."}
