from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.client import Client

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    date: datetime = Field(default_factory=datetime.now())
    is_active: bool = Field(default=True)
    note: Optional[str] = Field(default=None, max_length=200)
    
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    client: Optional["Client"] = Relationship(back_populates="payments")