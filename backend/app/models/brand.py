from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Brand(Base):
  __tablename__ = "brand"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False, unique=True)
  created_at = Column(DateTime(timezone=True), server_default=func.now())