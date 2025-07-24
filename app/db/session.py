from sqlmodel import SQLModel, create_engine, Session
from app.core.config_loader import settings

from app.models import product, client, payment, sale, sale_detail, category

# DATABASE_URL = str(settings.SQLALCHEMY_DATABASE_URI)
# engine = create_engine(DATABASE_URL)

DATABASE_URL = "sqlite:///./kiosko.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session