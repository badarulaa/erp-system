from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
  __tablename__ = "product"

  __table_args__ = (
    Index("idx_product_sku", "sku"),
    Index("idx_product_category", "category_id"),
    Index("idx_product_brand", "brand_id"),
  )

  id = Column(Integer, primary_key=True, index=True)
  sku = Column(String(50), unique=True, nullable=False)
  name = Column(String(255), nullable=False)
  category_id = Column(Integer, ForeignKey("product_category.id"))
  brand_id = Column(Integer, ForeignKey("brand.id"))

  category = relationship("ProductCategory")
  brand = relationship("Brand")

  prices = relationship("ProductPrice", back_populates="product")

  description = Column(Text)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())