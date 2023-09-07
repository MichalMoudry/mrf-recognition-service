"""
Package with DTOs for the web API.
"""
from pydantic import BaseModel, Field
from fastapi import UploadFile


class CreateBatchModel(BaseModel):
    """
    A model class for creating a single document batch.
    """
    name: str = Field(..., min_length=3, max_length=180)
    files: list[UploadFile]
