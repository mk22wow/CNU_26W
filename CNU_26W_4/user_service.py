from sqlmodel import Session, select, delete
from .model import User
from .Item_model import Item

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user_by_id(session: Session, user_id:int):
    return session.get(User, user_id)

def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit() 
        return True
    
    return False
