from pydantic import BaseModel

class TransferCreate(BaseModel):
  product_id: int
  from_warehouse_id: int
  to_warehouse_id: int
  qty: int