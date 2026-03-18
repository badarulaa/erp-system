from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
  try:
    return product_service.create_product(db, product)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
  return product_service.get_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
  product = product_service.get_product_by_id(db, product_id)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
  product = product_service.update_product(db, product_id, data)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
  product = product_service.delete_product(db, product_id)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  return {"message": "Product deleted"}