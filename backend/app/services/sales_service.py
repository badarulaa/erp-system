from sqlalchemy.orm import Session
from app.repositories import sales_repository, stock_repository

def create_sales(db: Session, data):
  for item in data.items:
    stock = stock_repository.get_current_stock(
      db,
      item.product_id,
      data.warehouse_id
    )

    if stock < item.qty:
      raise ValueError(f"Insufficient stock for product {item.product_id}")

  so = sales_repository.create_sales(db, data)

  for item in data.items:
    stock_repository.create_movement(db, {
      "product_id": item.product_id,
      "warehouse_id": data.warehouse_id,
      "qty": item.qty,
      "movement_type": "OUT",
      "note": f"SO#{so.id}"
    })

  return so