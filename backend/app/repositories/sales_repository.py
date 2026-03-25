from sqlalchemy.orm import Session
from app.models.sales_order import SalesOrder
from app.models.sales_order_item import SalesOrderItem

def create_sales(db: Session, data):
  so = SalesOrder(customer_name=data.customer_name)
  db.add(so)
  db.commit()
  db.refresh(so)

  for item in data.items:
    so_item = SalesOrderItem(
      sales_order_id=so.id,
      product_id=item.product_id,
      qty=item.qty
    )
    db.add(so_item)

  db.commit()
  return so

def get_sales_items(db, sales_order_id: int):
  return db.query(SalesOrderItem).filter(
    SalesOrderItem.sales_order_id == sales_order_id
  ).all()
