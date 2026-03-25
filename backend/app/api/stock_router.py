from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.stock_schema import StockCreate, StockResponse
from app.services import stock_service

router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.post("/", response_model=StockResponse)
def create_stock(data: StockCreate, db: Session = Depends(get_db)):
  try:
    return stock_service.create_stock(db, data)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[StockResponse])
def get_stocks(db: Session = Depends(get_db)):
  return stock_service.get_stocks(db)