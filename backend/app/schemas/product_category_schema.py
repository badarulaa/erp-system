from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCategoryBase(BaseModel):
  name: str
  parent_id: Optional[int] = None

class ProductCategoryCreate(ProductCategoryBase):
  pass

class ProductCategoryResponse(ProductCategoryBase):
  id: int
  created_at: Optional[datetime]

  class Config:
    from_attributes = True