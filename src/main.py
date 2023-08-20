"""
Module that contains endpoint methods for the recognition service.
"""

from fastapi import FastAPI
from .transport import api_metadata

app = FastAPI(openapi_tags=api_metadata.tags_metadata)

@app.get("/healthz", tags=[api_metadata.GENERAL_TAG])
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"