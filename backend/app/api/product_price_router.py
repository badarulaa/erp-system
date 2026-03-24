from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.product_price_schema import ProductPriceCreate, ProductPriceResponse
from app.services import product_price_service

router = APIRouter(prefix="/product-prices", tags=["Product Prices"])

@router.post("/", response_model=ProductPriceResponse)
def create_price(data: ProductPriceCreate, db: Session = Depends(get_db)):
  return product_price_service.create_price(
    db,
    data.product_id,
    data.price_type_id,
    data.price
  )