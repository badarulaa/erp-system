from sqlalchemy.orm import Session
from app.repositories import purchase_repository, stock_repository

def create_purchase(db: Session, data):
  return purchase_repository.create_purchase(db, data)

def receive_purchase(db: Session, purchase_id: int, warehouse_id: int):
  po, items = purchase_repository.get_purchase_with_item(db, purchase_id)

  if not po:
    raise ValueError("Purchase not found")

  if po.status == "RECEIVED":
    raise ValueError("Purchase already received")

  for item in items:
    stock_repository.create_movement(db, {
      "product_id": item.product_id,
      "warehouse_id": warehouse_id,
      "qty": item.qty,
      "movement_type": "IN",
      "note": f"PO#{purchase_id}"
    })

  po.status = "RECEIVED"
  db.commit()

  return {"message": "Goods received successfully"}