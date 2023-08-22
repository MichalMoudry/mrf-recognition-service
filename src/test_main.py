"""
Module with API tests of the recognition service.
"""

from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_health_method():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == "healthy"
