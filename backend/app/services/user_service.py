from sqlalchemy.orm import Session
from app.repositories import user_repository

def create_user(db: Session, data):
  return user_repository.create_user(db, data)