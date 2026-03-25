from sqlalchemy.orm import Session
from app.repositories import stock_repository

def create_stock(db: Session, data):
  if data.movement_type not in ["IN", "OUT"]:
    raise ValueError("movement_type must be IN or OUT")

  if data.qty <= 0:
    raise ValueError("qty must be > 0")

  if data.movement_type == "OUT":
    current_stoock = stock_repository.get_current_stock(
      db,
      data.product_id,
      data.warehouse_id
    )

    if current_stoock < data.qty:
      raise ValueError("Insufficient stock")

  return stock_repository.create_movement(db, data.model_dump())

def get_stocks(db: Session):
  return stock_repository.get_movements(db)