from fastapi import FastAPI
from app.core.database import engine, Base

from app.models import product, product_category, brand, price_type, product_price, stock_movement, warehouse
from app.api import product_router, product_category_router, brand_router, product_price_router, stock_router

app = FastAPI(
  title="ERP System API",
  version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(product_router.router)
app.include_router(product_category_router.router)
app.include_router(brand_router.router)
app.include_router(product_price_router.router)
app.include_router(stock_router.router)

# @app.get("/")
# def root():
#   return {"message": "ERP Backend Running"}