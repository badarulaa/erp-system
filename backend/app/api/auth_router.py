from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
  try:
    token = auth_service.login(db, data.username, data.password)
    return {"access_token": token}
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))