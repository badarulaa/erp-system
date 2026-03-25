from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InvoiceCreate(BaseModel):
  sales_order_id: int

class PaymentCreate(BaseModel):
  invoice_id: int
  amount: float

class InvoiceResponse(BaseModel):
  id: int
  sales_order_id: int
  total_amount: float
  status: str
  created_at: Optional[datetime]

  class Config:
    from_attributes = True

class PaymentResponse(BaseModel):
  id: int
  invoice_id: int
  amount: float
  created_at: Optional[datetime]

  class Config:
    from_attributes = True