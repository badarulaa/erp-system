from sqlalchemy.orm import Session
from app.repositories import brand_repository

def create_brand(db: Session, name: str):
  existing = brand_repository.get_brand_by_name(db, name)

  if existing:
    raise ValueError("Brand already exists")

  return brand_repository.create_brand(db, name)

def get_brands(db: Session):
  return brand_repository.get_brands(db)