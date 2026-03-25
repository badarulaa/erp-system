from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Invoice(Base):
  __tablename__ = "invoice"

  id = Column(Integer, primary_key=True, index=True)
  sales_order_id = Column(Integer, ForeignKey("sales_order.id"))
  total_amount = Column(Numeric(15, 2))
  status = Column(String(50), default="UNPAID")
  created_at = Column(DateTime(timezone=True), server_default=func.now())