from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.client import ClientCreate, ClientRead, ClientUpdate
from app.crud.client import create_client, get_all_clients

client_router = APIRouter(prefix='/clientes', tags=['Clientes'])

@client_router.post('/', response_model=ClientRead)
def create(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@client_router.get('/', response_model=list[ClientRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_clients(db)