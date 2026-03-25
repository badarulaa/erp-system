from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.transfer_schema import TransferCreate
from app.services import transfer_service

router = APIRouter(prefix="/transfer", tags=["Transfer"])

@router.post("/")
def transfer(data: TransferCreate, db: Session = Depends(get_db)):
  try:
    transfer_service.transfer_stock(db, data)
    return {"message": "Transfer success"}
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))