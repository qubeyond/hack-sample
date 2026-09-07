from fastapi import FastAPI

from app.api.routes import predict
from app.api.schemas.health import HealthResponse

app = FastAPI(title="ml")

app.include_router(predict.router, prefix="/api/v1")


@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok")
