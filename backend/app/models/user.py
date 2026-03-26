from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key=True, unique=True)
  username = Column(String(50), unique=True)
  password = Column(String(255))
  role_id = Column(Integer, ForeignKey("role.id"))
  role = relationship("Role")