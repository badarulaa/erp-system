from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.core.security import verify_password, create_access_token

def login(db, username, password):
  user = user_repository.get_user_by_username(db, username)

  if not user:
    raise ValueError("Invalid username")

  if not verify_password(password, user.password):
    raise ValueError("Invalid password")

  token = create_access_token({
    "sub": user.username,
    "role": user.role_id
  })

  return token