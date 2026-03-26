from pydantic import BaseModel

class UserCreate(BaseModel):
  username: str
  password: str
  role_id: int

class UserResponse(BaseModel):
  id: int
  username: str
  role_id: int

  class Config:
    from_attributes = True