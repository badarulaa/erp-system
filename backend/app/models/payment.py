from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Payment(Base):
  __tablename__ = "payment"

  id = Column(Integer, primary_key=True, index=True)
  invoice_id = Column(Integer, ForeignKey("invoice.id"))
  amount = Column(Numeric(15, 2))
  created_at = Column(DateTime(timezone=True), server_default=func.now())