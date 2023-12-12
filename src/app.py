"""
Module containg an entrypoint for the recognition service.
"""
from fastapi import FastAPI, Request, Response
from config import load_configuration, Environment
from database.connect import get_db_connection
from service.service_collection import ServiceCollection

cfg = load_configuration()
app = FastAPI()
db_conn = get_db_connection(cfg)
services = ServiceCollection(db_conn)


@app.middleware("http")
async def process_jwt(request: Request, call_next):
    """
    Middleware for parsing JWTs in a HTTP request.
    """
    auth_header = request.headers.get("Authorization")
    if auth_header == None and cfg.env != Environment.DEV:
        return Response("missing JWT", status_code=400, media_type="text/plain")
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
            "topic": "new-workflow",
            "route": "workflows/add"
        },
        {
            "pubsubname": "pub-sub",
            "topic": "workflow_update",
            "route": "workflows/update"
        },
        {
            "pubsubname": "pub-sub",
            "topic": "workflow_delete",
            "route": "workflows/delete"
        },
        {
            "pubsubname": "pub-sub",
            "topic": "user-delete",
            "route": "users/delete"
        }
    ]


if __name__ == "__main__":
    print("Hello from recognition service! ʕ•ᴥ•ʔ")
    print(f"Service is running in '{cfg.env}' mode.")
