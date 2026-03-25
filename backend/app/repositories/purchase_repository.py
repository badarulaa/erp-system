from sqlalchemy.orm import Session
from app.models.purchase_order import PurchaseOrder
from app.models.purchase_order_item import PurchaseOrderItem

def create_purchase(db: Session, data):
  po = PurchaseOrder(supplier_name=data.supplier_name)
  db.add(po)
  db.commit()
  db.refresh(po)

  for item in data.items:
    po_item = PurchaseOrderItem(
      purchase_order_id=po.id,
      product_id=item.product_id,
      qty=item.qty
    )
    db.add(po_item)
  db.commit()
  return po

def get_purchase_with_item(db, purchase_id: int):
  po = db.query(PurchaseOrder).filter(PurchaseOrder.id == purchase_id).first()
  items = db.query(PurchaseOrderItem).filter(
    PurchaseOrderItem.purchase_order_id == purchase_id
  ).all()

  return po, items