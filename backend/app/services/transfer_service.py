from sqlalchemy.orm import Session
from app.repositories import stock_repository

def transfer_stock(db: Session, data):
  if data.from_warehouse_id == data.to_warehouse_id:
    raise ValueError("Cannot transfer to same warehouse")

  if data.qty <= 0:
    raise ValueError("qty must be positive")

  current_stock = stock_repository.get_current_stock(
    db,
    data.product_id,
    data.from_warehouse_id
  )

  if current_stock < data.qty:
    raise ValueError("Insufficient stock for transfer")

  # OUT
  stock_repository.create_movement(db, {
    "product_id": data.product_id,
    "warehouse_id": data.from_warehouse_id,
    "qty": data.qty,
    "movement_type": "OUT",
    "note": "Transfer OUT"
  })

  # IN
  stock_repository.create_movement(db, {
    "product_id": data.product_id,
    "warehouse_id": data.from_warehouse_id,
    "qty": data.qty,
    "movement_type": "IN",
    "note": "Transfer IN"
  })