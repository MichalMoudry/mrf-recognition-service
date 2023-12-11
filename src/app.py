"""
Module containg an entrypoint for the recognition service.
"""
import psycopg2
from fastapi import FastAPI


app = FastAPI()
if __name__ == "__main__":
    conn = psycopg2.connect("dbname=data-persistence host=localhost user=root port=5432 sslmode=allow password=root")
else:
    # TODO: Replace with mock connection.
    conn = psycopg2.connect("dbname=data-persistence host=localhost user=root port=5432 sslmode=allow password=root")

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
