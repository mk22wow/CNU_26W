from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Item_model import Item

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    items: List["Item"] = Relationship(back_populates="owner", cascade_delete=True)
