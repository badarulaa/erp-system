from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func
from app.core.database import Base

class PurchaseOrder(Base):
  __tablename__ = "purchase_order"

  id = Column(Integer, primary_key=True, index=True)
  supplier_name = Column(String(255))
  status = Column(String(50), default="DRAFT")
  created_at = Column(DateTime(timezone=True), server_default=func.now())