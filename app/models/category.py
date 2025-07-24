from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List
if TYPE_CHECKING:
    from app.models.product import Product
    
class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    is_active: bool
    
    products: List['Product'] = Relationship(back_populates='category')