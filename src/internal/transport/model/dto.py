"""
Package with DTOs for the web API.
"""
from uuid import UUID
from pydantic import BaseModel, Field


class CreateBatchModel(BaseModel):
    """
    A model class for creating a single document batch.
    """
    batch_name: str = Field(..., min_length=3, max_length=180)
    workflow_id: UUID
