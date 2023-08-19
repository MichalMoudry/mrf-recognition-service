"""
Module that contains endpoint methods for the recognition service.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"