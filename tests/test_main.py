import pytest
from fastapi.testclient import TestClient

from app.main import app, calculate_total

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_calculate_total():
    assert calculate_total(100, 3) == 300.0


def test_negative_price_rejected():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)