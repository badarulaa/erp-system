from sqlalchemy.orm import Session
from app.repositories import finance_repository, sales_repository
from app.models.invoice import Invoice

def create_invoice(db: Session, sales_order_id: int):
  items = sales_repository.get_sales_items(db, sales_order_id)

  total = 0
  for item in items:
    total += item.qty * 100000

  return finance_repository.create_invoice(db, sales_order_id, total)

def create_payment(db: Session, invoice_id: int, amount: float):
  payment = finance_repository.create_payment(db, invoice_id, amount)
  invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()

  if invoice:
    invoice.status = "PAID"
    db.commit()

  return payment