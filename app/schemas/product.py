from sqlmodel import SQLModel
from typing import Optional

class ProductBase(SQLModel):
    name: str
    price: float
    
class ProductCreate(ProductBase):
    pass  
    
class ProductUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None
    
class ProductRead(ProductCreate):
    pass