from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services import report_service

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/stock-card")
def stock_card(product_id: int, warehouse_id: int, db: Session = Depends(get_db)):
  return report_service.get_stock_card(db, product_id, warehouse_id)