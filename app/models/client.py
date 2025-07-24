from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.payment import Payment
    from app.models.sale import Sale

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, index=True)
    phone: Optional[str] = Field(default=None, max_length=10)
    current_balance: float = Field(default=0.0)
    is_active: bool = Field(default=True)
    
    payments: List['Payment'] = Relationship(back_populates='client')
    sales: List['Sale'] = Relationship(back_populates='client')