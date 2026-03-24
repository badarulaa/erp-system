from pydantic import BaseModel
from typing import Optional

class StockCreate(BaseModel):
  product_id: int
  qty: int
  movement_type: str
  note: Optional[str] = None

class StockResponse(BaseModel):
  id: int
  product_id: int
  qty: int
  movement_type: str

  class Config:
    from_attributes = True