from fastapi import FastAPI
from app.routers.product import product_router
from app.routers.client import client_router
from app.routers.category import category_router

app = FastAPI(title='Kiosko API')

app.include_router(product_router)
app.include_router(client_router)
app.include_router(category_router)
