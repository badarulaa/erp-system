from sqlalchemy.orm import Session
from app.repositories import product_category_repository

def create_category(db: Session, name: str, parent_id: int = None):
  return product_category_repository.create_category(db, name, parent_id)

def get_categories(db: Session):
  return product_category_repository.get_categories(db)