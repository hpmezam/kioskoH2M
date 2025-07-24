from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.category import CategoryCreate, CategoryRead
from app.crud.category import create_category, get_all_categories

category_router = APIRouter(prefix='/category', tags=['Categorias'])

@category_router.post('/', response_model=CategoryRead)
def create(client: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, client)

@category_router.get('/', response_model=list[CategoryRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_categories(db)