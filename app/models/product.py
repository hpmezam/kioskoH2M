from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, index=True)
    price: float
    is_active: bool = Field(default=True)