from sqlalchemy.orm import Session
from app.models.invoice import Invoice
from app.models.payment import Payment

def create_invoice(db: Session, sales_order_id: int, total: float):
  inv = Invoice(
    sales_order_id=sales_order_id,
    total_amount=total
  )
  db.add(inv)
  db.commit()
  db.refresh(inv)
  return inv

def create_payment(db: Session, invoice_id: int, amount: float):
  pay = Payment(
    invoice_id=invoice_id,
    amount=amount
  )
  db.add(pay)
  db.commit()
  db.refresh(pay)
  return pay