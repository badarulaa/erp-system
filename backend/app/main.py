from fastapi import FastAPI
from app.core.database import engine, Base

app = FastAPI(
  title="ERP System API",
  version="1.0.0"
)

@app.get("/")
def root():
  return {"message": "ERP Backend Running"}