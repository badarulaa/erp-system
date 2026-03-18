from fastapi import FastAPI
from app.core.database import engine, Base

from app.models import product
from app.api import product_router

app = FastAPI(
  title="ERP System API",
  version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(product_router.router)

# @app.get("/")
# def root():
#   return {"message": "ERP Backend Running"}