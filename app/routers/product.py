from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.db.database import get_db
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.crud.product import create_product, get_all_products, get_product, update_product, delete_product

product_router = APIRouter(prefix='/productos', tags=['Productos'])

@product_router.post('/', response_model=ProductRead)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@product_router.get('/', response_model=list[ProductRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_products(db)
     
@product_router.get('/{id}', response_model=ProductRead)
def get(id: int, db: Session = Depends(get_db)):
    return get_product(db, id)

@product_router.put('/{id}')
def update(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = update_product(db, id, product)
    return db_product

@product_router.delete("/{id}", status_code=200)
def delete(id: int, db: Session = Depends(get_db)):
    return delete_product(db, id)