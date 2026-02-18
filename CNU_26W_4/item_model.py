from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .model import User

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title:str
    description: Optional[str] = None

    owner_id: int=Field(foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="items")
