"""
Module with basic API tests of the recognition service.
"""
from fastapi.testclient import TestClient
from httpx import Headers
from app import app


def test_health_endpoint():
    """
    A simple test scenario for testing /health endpoint.
    """
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "healthy"


def test_user_delete():
    """
    A simple test covering basic invocation of /users/delete endpoint.
    """
    client = TestClient(app)
    response = client.post(
        "/users/delete",
        json={
            "id": "e2e0f099-6b7f-4a00-a549-bd5a4366a66d",
            "data": "VGJDmp2VmuIt2HM9c1Qc1T7Li992",
            "datacontenttype": "application/json",
            "pubsubname": "mrf-pub-sub",
            "source": "user-service",
            "specversion": "1.0",
            "time": "2023-11-16T12:49:53Z",
            "topic": "user-delete",
            "traceid": "00-f9a224367f5cd4694210021220bc9a68-c74f791fd741165b-01",
            "traceparent": "00-f9a224367f5cd4694210021220bc9a68-c74f791fd741165b-01",
            "tracestate": "",
            "type": "com.dapr.event.sent"
        },
        headers=Headers({
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        })
    )
    assert response.status_code == 200
