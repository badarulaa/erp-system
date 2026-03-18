from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BrandBase(BaseModel):
  name: str

class BrandCreate(BrandBase):
  pass

class BrandResponse(BrandBase):
  id: int
  created_at: Optional[datetime]

  class Config:
    from_attributes = True