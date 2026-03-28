from sqlalchemy.orm import Session
from app.repositories import user_repository

def create_user(db, data):
  from app.core.security import hash_password

  password = data.password

  hashed_password = hash_password(password)

  user_data = data.model_dump()
  user_data["password"] = hashed_password

  return user_repository.create_user(db, user_data)