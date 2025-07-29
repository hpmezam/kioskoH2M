from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead

def create_category(db: Session, category: CategoryCreate) -> CategoryRead:
    # Check if a category with the same name already exists
    existing = db.exec(select(Category).where(Category.name == category.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"A category with name '{category.name}' already exists")
    new_category = Category(**category.model_dump(), is_active=True)
    
    db.add(new_category)
    
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session) -> list[CategoryRead]:
    return  db.exec(select(Category)).all()

def get_category(db: Session, id: int) -> CategoryRead:
    # 1. Get existing object
    category = db.get(Category, id)
    if not category:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")
    return category

def update_category(db: Session, id: int, category: CategoryUpdate) -> CategoryRead:
    # 1. Get existing object
    existing = db.get(Category, id)
    if not existing:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

    # 2. Get only fields that were provided
    category_data = category.model_dump(exclude_unset=True)

    # 3. Check if a different product already has the same name
    if "name" in category_data:
        duplicate = db.exec(
            select(Category)
            .where(Category.name == category_data["name"])
            .where(Category.id != id)
        ).first()
        if duplicate:
            raise HTTPException(
                status_code=400,
                detail=f"Another category with name '{category_data['name']}' already exists"
            )

    # 4. Check if the new values differ from the current ones
    no_changes = all(
        getattr(existing, field) == value
        for field, value in category_data.items()
    )
    if no_changes:
        raise HTTPException(
            status_code=400,
            detail="No changes detected"
        )

    # 5. Apply updates
    for key, value in category_data.items():
        setattr(existing, key, value)

    db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

def delete_category(db: Session, id: int) -> dict:
    category = db.get(Category, id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {id} not found"
        )

    name = category.name
    db.delete(category)
    db.commit()
    return {"message": f"The category '{name}' was successfully deleted"}

def set_category_state(db: Session, id: int) -> CategoryRead:
    category = db.get(Category, id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {id} not found"
        )
    category.is_active = not category.is_active
    db.commit()
    db.refresh(category)
    return category