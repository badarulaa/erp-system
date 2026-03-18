from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.product_category_schema import ProductCategoryCreate, ProductCategoryResponse
from app.services import product_category_service

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=ProductCategoryResponse)
def create_category(data: ProductCategoryCreate, db: Session = Depends(get_db)):
  return product_category_service.create_category(db, data.name, data.parent_id)

@router.get("/", response_model=list[ProductCategoryResponse])
def get_categories(db: Session = Depends(get_db)):
  return product_category_service.get_categories(db)
