from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PurchaseItem(BaseModel):
  product_id: int
  qty: int

class PurchaseCreate(BaseModel):
  supplier_name: str
  items: List[PurchaseItem]

class PurchaseResponse(BaseModel):
  id: int
  supplier_name: str
  status: str
  created_at: Optional[datetime]

  class Config:
    from_attributes = True

class ReceivePurchase(BaseModel):
  warehouse_id: int