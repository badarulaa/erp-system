from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class ProductCategory(Base):
  __tablename__ = "product_category"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  parent_id = Column(Integer, ForeignKey("product_category.id"), nullable=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now())