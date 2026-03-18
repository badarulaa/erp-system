from sqlalchemy.orm import Session
from app.models.brand import Brand

def create_brand(db: Session, name: str):
  brand = Brand(name=name)
  db.add(brand)
  db.commit()
  db.refresh(brand)
  return brand

def get_brands(db: Session):
  return db.query(Brand).all()

def get_brand_by_name(db: Session, name: str):
  return db.query(Brand).filter(Brand.name == name).first()