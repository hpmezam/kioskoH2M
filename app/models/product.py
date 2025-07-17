from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.sale_detail import SaleDetail

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, index=True)
    price: float
    is_active: bool = Field(default=True)
    
    details: List['SaleDetail'] = Relationship(back_populates='product')