from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.crud.category import create_category, get_all_categories, get_category, update_category, delete_category, set_category_state

category_router = APIRouter(prefix='/category', tags=['Categorias'])

@category_router.post('/', response_model=CategoryRead)
def create(client: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, client)

@category_router.get('/', response_model=list[CategoryRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_categories(db)

@category_router.get('/{id}', response_model=CategoryRead)
def get(id: int, db: Session = Depends(get_db)):
    return get_category(db, id)

@category_router.put('/{id}', response_model=CategoryRead)
def update(id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return update_category(db, id, category)

@category_router.delete("/{id}", status_code=200)
def delete(id: int, db: Session = Depends(get_db)):
    return delete_category(db, id)

@category_router.put('/{id}/state', response_model=CategoryRead)
def update_state(id: int, db: Session = Depends(get_db)):
    return set_category_state(db, id)