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

# def get_product(db: Session, id: int) -> ProductRead:
#     # 1. Get existing object
#     product = db.get(Product, id)
#     if not product:
#         raise HTTPException(status_code=404, detail=f"Product with id {id} not found")
#     return product

# def update_product(db: Session, id: int, product: ProductUpdate) -> ProductRead:
#     # 1. Get existing object
#     existing = db.get(Product, id)
#     if not existing:
#         raise HTTPException(status_code=404, detail=f"Product with id {id} not found")

#     # 2. Get only fields that were provided
#     product_data = product.model_dump(exclude_unset=True)

#     # 3. Check if a different product already has the same name
#     if "name" in product_data:
#         duplicate = db.exec(
#             select(Product)
#             .where(Product.name == product_data["name"])
#             .where(Product.id != id)
#         ).first()
#         if duplicate:
#             raise HTTPException(
#                 status_code=400,
#                 detail=f"Another product with name '{product_data['name']}' already exists"
#             )

#     # 4. Check if the new values differ from the current ones
#     no_changes = all(
#         getattr(existing, field) == value
#         for field, value in product_data.items()
#     )
#     if no_changes:
#         raise HTTPException(
#             status_code=400,
#             detail="No changes detected"
#         )

#     # 5. Apply updates
#     for key, value in product_data.items():
#         setattr(existing, key, value)

#     db.add(existing)
#     db.commit()
#     db.refresh(existing)
#     return existing

# def delete_product(db: Session, id: int) -> dict:
#     product = db.get(Product, id)
#     if not product:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Product with id {id} not found"
#         )

#     name = product.name
#     db.delete(product)
#     db.commit()
#     return {"message": f"The product '{name}' was successfully deleted"}