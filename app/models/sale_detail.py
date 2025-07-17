from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.sale import Sale
    from app.models.product import Product
    
class SaleDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sale_id: Optional[int] = Field(default=None, foreign_key="sale.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    quantity: int
    unit_price: float
    subtotal: float
    
    sale: Optional["Sale"] = Relationship(back_populates="details")
    product: Optional["Product"] = Relationship(back_populates="details")
    