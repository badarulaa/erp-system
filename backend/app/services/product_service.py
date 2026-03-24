from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.repositories import product_repository

def create_product(db: Session, product: ProductCreate):
  try:
    return product_repository.create_product(db, product)
  except IntegrityError:
    db.rollback()
    raise ValueError("SKU already exists")

def get_products(db: Session):
  products = product_repository.get_products(db)
  return [map_product(p) for p in products]

def get_product_by_id(db: Session, product_id: int):
  product = product_repository.get_product_by_id(db, product_id)
  if not product:
    return None
  return map_product(product)

def update_product(db: Session, product_id: int, product: ProductCreate):
  return product_repository.update_product(db, product_id, product)

def delete_product(db: Session, product_id: int):
  return product_repository.delete_product(db, product_id)

def map_product(product):
  return {
    "id": product.id,
    "sku": product.sku,
    "name": product.name,
    "category": {
      "id": product.category.id,
      "name": product.category.name
    } if product.category else None,
    "brand": {
      "id": product.brand.id,
      "name": product.brand.name
    } if product.brand else None,
    "prices": [
      {
        "type": p.price_type.name,
        "price": float(p.price)
      }
      for p in product.prices
    ],
    "description": product.description,
    "created_at": product.created_at,
    "updated_at": product.updated_at
  }