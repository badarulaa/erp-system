from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_HOST: str
  DATABASE_PORT: int
  DATABASE_NAME: str
  DATABASE_USER: str
  DATABASE_PASSWORD: str

  @property
  def DATABASE_URL(self) -> str:
    return (
      f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
      f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
    )

  class Config:
    env_file = ".env"

settings = Settings()