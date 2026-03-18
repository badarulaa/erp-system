from sqlalchemy.orm import Session
from app.models.product_category import ProductCategory

def create_category(db: Session, name: str, parent_id: int = None):
  category = ProductCategory(name=name, parent_id=parent_id)
  db.add(category)
  db.commit()
  db.refresh(category)
  return category

def get_categories(db: Session):
  return db.query(ProductCategory).all()