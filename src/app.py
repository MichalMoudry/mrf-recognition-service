"""
Module containg an entrypoint for the recognition service.
"""

from fastapi import FastAPI

app = FastAPI()


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
    subscriptions = [
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
    return subscriptions
