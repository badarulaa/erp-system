from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.repositories import product_repository

def create_product(db: Session, product: ProductCreate):
  existing = product_repository.get_product(db)
  for item in existing:
    if item.sku == product.sku:
      raise ValueError("SKU already exists")

  return product_repository.create_product(db, product)

def get_products(db: Session):
  return product_repository.get_products(db)

def get_product_by_id(db: Session, product_id: int):
  return product_repository.get_product_by_id(db, product_id)

def update_product(db: Session, product_id: int, product: ProductCreate):
  return product_repository.update_product(db, product_id, product)

def delete_product(db: Session, product_id: int):
  return product_repository.delete_product(db, product_id)