from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class SalesOrderItem(Base):
  __tablename__ = "sales_order_item"

  id = Column(Integer, primary_key=True, index=True)
  sales_order_id = Column(Integer, ForeignKey("sales_order.id"))
  product_id = Column(Integer, ForeignKey("product.id"))
  qty = Column(Integer)
  sales_order = relationship("SalesOrder")