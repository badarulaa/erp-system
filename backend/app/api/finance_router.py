from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.finance_schema import InvoiceCreate, PaymentCreate, InvoiceResponse, PaymentResponse
from app.services import finance_service

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.post("/invoice", response_model=InvoiceResponse)
def create_invoice(data: InvoiceCreate, db: Session = Depends(get_db)):
  return finance_service.create_invoice(db, data.sales_order_id)

@router.post("/payment", response_model=PaymentResponse)
def create_payment(data: PaymentCreate, db: Session = Depends(get_db)):
  return finance_service.create_payment(db, data.invoice_id, data.amount)