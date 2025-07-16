from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    date: datetime = Field(default_factory=datetime.now())
    is_active: bool = Field(default=True)
    note: Optional[str] = Field(default=None, max_length=200)