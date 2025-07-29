from sqlmodel import SQLModel, Field
from typing import Optional

class CategoryBase(SQLModel):
    name: str = Field(max_length=50, index=True)
    
class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(SQLModel):
    name: Optional[str] = Field(default=None, max_length=50)
    is_active: Optional[bool] = Field(default=None)
    
class CategoryRead(CategoryCreate):
    id: int
    is_active: bool

class ProductCreate(SQLModel):
    name: str
    price: float
    category_id: int