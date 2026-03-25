from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Relationship
from app.core.database import Base

class PurchaseOrderItem(Base):
  __tablename__ = "purchase_order_item"

  id = Column(Integer, primary_key=True, index=True)
  purchase_order_id = Column(Integer, ForeignKey("purchase_order.id"))
  product_id = Column(Integer, ForeignKey("product.id"))
  qty = Column(Integer)
  purchase_order = Relationship("PurchaseOrder")