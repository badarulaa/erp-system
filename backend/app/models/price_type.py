from sqlalchemy import Column, Integer, String
from app.core.database import Base

class PriceType(Base):
  __tablename__ = "price_type"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(50), unique=True, nullable=False)