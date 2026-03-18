from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.brand_schema import BrandCreate, BrandResponse
from app.services import brand_service

router = APIRouter(prefix="/brands", tags=["Brands"])

@router.post("/", response_model=BrandResponse)
def create_brand(data: BrandCreate, db: Session = Depends(get_db)):
  try:
    return brand_service.create_brand(db, data.name)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[BrandResponse])
def create_brand(db: Session = Depends(get_db)):
  return brand_service.get_brands(db)