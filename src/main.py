from fastapi import FastAPI
from data.mock_data import mock_data
from services.reservation_service import get_health

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return mock_data


@app.get("/health")
def health():
    return get_health()