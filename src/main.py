"""
Module that contains endpoint methods for the recognition service.
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .transport import api_metadata
from .transport.model import dto, validation

app = FastAPI(openapi_tags=api_metadata.tags)


@app.get("/healthz", tags=[api_metadata.GENERAL_TAG])
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.post("/batch")
async def create_batch(request_data: dto.CreateBatchModel) -> JSONResponse:
    """
    An endpoint for creating a new batch of documents for processing.
    """
    ...


@app.get("/batch/{batch_id}")
async def get_batch(batch_id: str):
    """
    An endpoint for obtaining information about a specific document batch.
    """
    batch_identifier = validation.is_string_valid_uuid(batch_id)
    if batch_identifier is None:
        return JSONResponse("Supplied batch ID is not a valid UUID.", 422)
    ...


@app.delete("/batch/{batch_id}")
async def delete_batch(batch_id: str):
    """
    An endpoint for deleting processed document batches from the system.
    """
    batch_identifier = validation.is_string_valid_uuid(batch_id)
    if batch_identifier is None:
        return JSONResponse("Supplied batch ID is not a valid UUID.", 422)
    ...
