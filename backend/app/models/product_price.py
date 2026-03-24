from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class ProductPrice(Base):
  __tablename__ = "product_price"

  id = Column(Integer, primary_key=True, index=True)
  product_id = Column(Integer, ForeignKey("product.id"))
  price_type_id = Column(Integer, ForeignKey("price_type.id"))
  price = Column(Numeric(15, 2), nullable=False)
  product = relationship("Product")
  price_type = relationship("PriceType")
  