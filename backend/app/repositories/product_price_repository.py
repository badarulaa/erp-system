from sqlalchemy.orm import Session
from app.models.product_price import ProductPrice

def create_price(db: Session, product_id: int, price_type_id: int, price: float):
  data = ProductPrice(
    product_id=product_id,
    price_type_id=price_type_id,
    price=price
  )
  db.add(data)
  db.commit()
  db.refresh(data)
  return data