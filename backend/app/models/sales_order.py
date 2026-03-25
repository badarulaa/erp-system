from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class SalesOrder(Base):
  __tablename__ = "sales_order"

  id = Column(Integer, primary_key=True, index=True)
  customer_name = Column(String(255))
  status = Column(String(50), default="CONFIRMED")
  created_at = Column(DateTime(timezone=True), server_default=func.now())