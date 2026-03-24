from sqlalchemy.orm import Session
from app.repositories import product_price_repository

def create_price(db: Session, product_id: int, price_type_id: int, price: float):
  return product_price_repository.create_price(db, product_id, price_type_id, price)