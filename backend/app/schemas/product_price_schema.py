from pydantic import BaseModel

class ProductPriceCreate(BaseModel):
  product_id: int
  price_type_id: int
  price: float

class ProductPriceResponse(BaseModel):
  id: int
  product_id: int
  price_type_id: int
  price: float

  class Config:
    from_attributes: True