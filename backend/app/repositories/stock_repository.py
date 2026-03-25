from sqlalchemy import func, case
from sqlalchemy.orm import Session
from app.models.stock_movement import StockMovement

def create_movement(db: Session, data):
  movement = StockMovement(**data)
  db.add(movement)
  db.commit()
  db.refresh(movement)
  return movement

def get_movements(db: Session):
  return db.query(StockMovement).all()

def get_stock_by_product(db, product_id: int):
  result = db.query(
    func.coalesce(
      func.sum(
        case(
          (StockMovement.movement_type == "IN", StockMovement.qty),
          (StockMovement.movement_type == "OUT", -StockMovement.qty),
          else_=0
        )
      ),
      0
    )
  ).filter(StockMovement.product_id == product_id).scalar()

  return result

def get_stock_by_product_and_warehouse(db, product_id: int, warehouse_id: int):
  result = db.query(
    func.coalesce(
      func.sum(
        case(
          (StockMovement.movement_type == "IN", StockMovement.qty)
          (StockMovement.movement_type == "OUT", -StockMovement.qty),
          else_=0
        )
      ),
      0
    )
  ).filter(
    StockMovement.product_id == product_id,
    StockMovement.warehouse_id == warehouse_id
  ).scalar()

  return result

def get_current_stock(db, product_id: int, warehouse_id: int):
  result = db.query(
    func.coalesce(
      func.sum(
        case(
          (StockMovement.movement_type == "IN", StockMovement.qty),
          (StockMovement.movement_type == "OUT", -StockMovement.qty),
          else_=0
        )
      ),
      0
    )
  ).filter(
    StockMovement.product_id == product_id,
    StockMovement.warehouse_id == warehouse_id
  ).scalar()

  return result

def get_movements_by_product(db, product_id: int, warehouse_id: int):
  return db.query(StockMovement).filter(
    StockMovement.product_id == product_id,
    StockMovement.warehouse_id == warehouse_id
  ).order_by(StockMovement.created_at.asc()).all()