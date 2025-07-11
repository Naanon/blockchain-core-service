from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Blockchain API",
    description="API para interação com a rede Ethereum.",
    version="1.0.0"
)

app.include_router(endpoints.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API is running"}