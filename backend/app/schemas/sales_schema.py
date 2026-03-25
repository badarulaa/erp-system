from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SalesItem(BaseModel):
  product_id: int
  qty: int

class SalesCreate(BaseModel):
  customer_name: str
  warehouse_id: int
  items: List[SalesItem]

class SalesResponse(BaseModel):
  id: int
  customer_name: str
  status: str
  created_at: Optional[datetime]

  class Config:
    from_attributes = True