from sqlmodel import SQLModel
from typing import Optional

class ProductCreate(SQLModel):
    name: str
    price: float
    
class ProductRead(ProductCreate):
    pass
    
class ProductUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None