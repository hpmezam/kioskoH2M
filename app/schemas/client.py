from sqlmodel import SQLModel, Field
from typing import Optional

class ClientBase(SQLModel):
    name: str = Field(max_length=50, index=True)
    phone: Optional[str] = Field(default=None, max_length=10)
    
class ClientCreate(ClientBase):
    pass

class ClientUpdate(SQLModel):
    name: Optional[str] = Field(default=None, max_length=50)
    phone: Optional[str] = Field(default=None, max_length=10)
    current_balance: Optional[float] = Field(default=None)
    
class ClientRead(SQLModel):
    id: int
    name: str
    phone: Optional[str]
    current_balance: float

    class Config:
        orm_mode = True
