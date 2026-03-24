from sqlalchemy.orm import Session
from app.models.stock_movement import StockMovement

def create_movement(db: Session, data):
  movement = StockMovement(**data.model_dump())
  db.add(movement)
  db.commit()
  db.refresh(movement)
  return movement

def get_movements(db: Session):
  return db.query(StockMovement).all()