from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate, ProductUpdate, ProductRead

def create_product(db: Session, product: ProductCreate) -> ProductRead:
    # Check if a product with the same name already exists
    existing = db.exec(select(Product).where(Product.name == product.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"A product with name '{product.name}' already exists")
    
    category = db.exec(select(Category).where(Category.id == product.category_id)).first()
    if not category:
        raise HTTPException(status_code=404, detail=f"Category with id {product.category_id} not found")
    
    # Create new product
    new_product = Product(**product.model_dump(), is_active=True)
    db.add(new_product)
    
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(db: Session) -> list[ProductRead]:
    return  db.exec(select(Product)).all()

def get_product(db: Session, id: int) -> ProductRead:
    # 1. Get existing object
    product = db.get(Product, id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with id {id} not found")
    return product

def update_product(db: Session, id: int, product: ProductUpdate) -> ProductRead:
    # 1. Get existing object
    existing = db.get(Product, id)
    if not existing:
        raise HTTPException(status_code=404, detail=f"Product with id {id} not found")

    # 2. Get only fields that were provided
    product_data = product.model_dump(exclude_unset=True)

    # 3. Check if a different product already has the same name
    if "name" in product_data:
        duplicate = db.exec(
            select(Product)
            .where(Product.name == product_data["name"])
            .where(Product.id != id)
        ).first()
        if duplicate:
            raise HTTPException(
                status_code=400,
                detail=f"Another product with name '{product_data['name']}' already exists"
            )

    # 4. Check if the new values differ from the current ones
    no_changes = all(
        getattr(existing, field) == value
        for field, value in product_data.items()
    )
    if no_changes:
        raise HTTPException(
            status_code=400,
            detail="No changes detected"
        )

    # 5. Apply updates
    for key, value in product_data.items():
        setattr(existing, key, value)

    db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

def delete_product(db: Session, id: int) -> dict:
    product = db.get(Product, id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {id} not found"
        )

    name = product.name
    db.delete(product)
    db.commit()
    return {"message": f"The product '{name}' was successfully deleted"}