from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, data):
  user = User(**data)
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_username(db: Session, username: str):
  return db.query(User).filter(User.username == username).first()