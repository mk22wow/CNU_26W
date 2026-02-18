from sqlmodel import Session, select
from .Item_model import Item

def create_item(session: Session, item: Item):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_items(session: Session):
    return session.exec(select(Item)).all()

def get_items_by_user(session: Session, user_id: int):
    return session.exec(select(Item).where(Item.owner_id == user_id)).all()


