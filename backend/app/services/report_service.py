from app.repositories import stock_repository

def get_stock_card(db, product_id: int, warehouse_id: int):
  movements = stock_repository.get_movements_by_product(
    db, product_id, warehouse_id
  )

  result = []
  balance = 0

  for m in movements:
    if m.movement_type == "IN":
      qty_in = m.qty
      qty_out = 0
      balance += m.qty
    else:
      qty_in = 0
      qty_out = m.qty
      balance -= m.qty

    result.append({
      "date": m.created_at,
      "type": m.movement_type,
      "qty_in": qty_in,
      "qty_out": qty_out,
      "balance": balance,
      "note": m.note
    })

  return result