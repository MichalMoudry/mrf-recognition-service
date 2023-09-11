"""
Module with basic API tests of the recognition service.
"""
from src.main import app


def test_health_method():
    app.config.update({
        "TESTING": True,
    })
    client = app.test_client()
    response = client.get("/healthz")
    assert response.data == b"healthy"
