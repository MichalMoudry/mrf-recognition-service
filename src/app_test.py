"""
Module with basic API tests of the recognition service.
"""
from fastapi.testclient import TestClient
from app import app


def test_health_endpoint():
    """
    A simple test scenario for testing /health endpoint.
    """
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "healthy"
