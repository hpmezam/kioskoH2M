from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.client import Client
    from app.models.sale_detail import SaleDetail
    
class Sale(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    date: datetime = Field(default_factory=datetime.now())
    total: float = Field(default=0.0)
    payment_method: str = Field(max_length=20, default="efectivo")
    
    client: Optional["Client"] = Relationship(back_populates="sales")
    details: List['SaleDetail'] = Relationship(back_populates='sale')
    