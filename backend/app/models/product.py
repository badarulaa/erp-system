from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Product(Base):
  __table_name__ = "product"

  id = Column(Integer, primary_key=True, index=True)
  sku = Column(String(50), unique=True, nullable=False)
  name = Column(String(255), nullable=False)
  category_id = Column(Integer,  )