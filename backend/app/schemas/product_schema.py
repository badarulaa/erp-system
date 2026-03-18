from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
  sku: str
  name: str
  category_id: Optional[int] = None
  brand_id: Optional[int] = None
  description: Optional[str] = None

class ProductCreate(ProductBase):
  pass

class ProductUpdate(BaseModel):
  sku: Optional[str] = None
  name: Optional[str] = None
  category_id: Optional[int] = None
  brand_id: Optional[int] = None
  description: Optional[str] = None
class CategorySimple(BaseModel):
  id: int
  name: str

  class Config:
    from_attributes = True

class BrandSimple(BaseModel):
  id: int
  name: str

  class Config:
    from_attributes = True

class ProductResponse(ProductBase):
  id: int
  sku: str
  name: str

  category: CategorySimple | None = None
  brand: BrandSimple | None = None

  description: Optional[str]
  created_at: Optional[datetime]
  updated_at: Optional[datetime]

  class Config:
    from_attributes = True
