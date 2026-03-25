from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.purchase_schema import PurchaseCreate, PurchaseResponse, ReceivePurchase
from app.services import purchase_service

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=PurchaseResponse)
def create_purchase(data: PurchaseCreate, db: Session = Depends(get_db)):
  return purchase_service.create_purchase(db, data)

@router.post("/{purchase_id}/receive")
def receive_purchase(purchase_id: int, data: ReceivePurchase, db: Session = Depends(get_db)):
  try:
    return purchase_service.receive_purchase(db, purchase_id, data.warehouse_id)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))