"""
Module containg an entrypoint for the recognition service.
"""
from cloudevents.http import from_http
from typing import Callable
from fastapi import FastAPI, Request, Response
from config import load_configuration
from database.connect import get_db_connection
from service.service_collection import ServiceCollection

cfg = load_configuration()
app = FastAPI()
print(__name__, "|", cfg)
db_conn = get_db_connection(cfg)
services = ServiceCollection(db_conn)


@app.middleware("http")
async def process_jwt(request: Request, call_next: Callable):
    """
    Middleware for parsing JWTs in a HTTP request.
    """
    auth_header = request.headers.get("Authorization")
    if auth_header == None:
        return Response("missing JWT", status_code=401, media_type="text/plain")
    return await call_next(request)


@app.get("/health")
def health():
    """
    An endpoint for health checks.
    """
    return "healthy"


@app.get("/dapr/subscribe")
def topic_subscription():
    """
    An endpoint for Dapr pub/sub subscriptions.
    """
    return [
        {
            "pubsubname": "pub-sub",
            "topic": "user-delete",
            "route": "users/delete"
        }
    ]


@app.post("/users/delete")
async def user_delete(request: Request):
    """
    An endpoint for getting requests to delete user's data.
    """
    event = from_http(dict(request.headers), await request.body())
    services.user_service.delete_users_data(event.data)
    return Response("success")


if __name__ == "app":
    print("Hello from recognition service! ʕ•ᴥ•ʔ")
    print(f"Service is running in '{cfg.env}' mode.")
