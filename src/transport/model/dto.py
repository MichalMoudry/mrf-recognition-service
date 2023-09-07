"""
Package with DTOs for the web API.
"""
from pydantic import BaseModel
from fastapi import UploadFile

class CreateBatchModel(BaseModel):
    """
    A model class for creating a single document batch.
    """
    name: str
    files: list[UploadFile]
