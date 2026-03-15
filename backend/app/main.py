from fastapi import FastAPI

app = FastAPI(
  title="ERP System API",
  version="1.0.0"
)

@app.get("/")
def root():
  return {"message": "ERP Backend Running"}