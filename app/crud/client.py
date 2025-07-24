from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate, ClientRead

def create_client(db: Session, client: ClientCreate) -> ClientRead:
    # Check if a client with the same name already exists
    existing = db.exec(select(Client).where(Client.name == client.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"A client with name '{client.name}' already exists")
    new_client = Client(**client.model_dump(), current_balance=0.0, is_active=True)
    
    # Create new client
    db.add(new_client)
    
    db.commit()
    db.refresh(new_client)
    return new_client

def get_all_clients(db: Session) -> list[ClientRead]:
    return db.exec(select(Client)).all()