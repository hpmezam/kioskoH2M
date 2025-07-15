from fastapi import FastAPI
from app.routers.product import product_router

app = FastAPI(title='Kiosko API')

app.include_router(product_router)
