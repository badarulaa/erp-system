from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.sales_schema import SalesCreate, SalesResponse
from app.services import sales_service

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SalesResponse)
def create_sales(data: SalesCreate, db: Session = Depends(get_db)):
  try:
    return sales_service.create_sales(db, data)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))