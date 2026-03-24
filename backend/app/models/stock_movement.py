from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class StockMovement(Base):
  __tablename__ = "stock_movement"

  id = Column(Integer, primary_key=True, index=True)
  product_id = Column(Integer, ForeignKey("product.id"))
  qty = Column(Integer, nullable=False)
  movement_type = Column(String(20))
  note = Column(String(255), nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  product = relationship("Product")