"""
Module with definitions of contracts of this service.
"""
from dataclasses import dataclass
from typing import TypeVar, Generic
from uuid import UUID
from pydantic import BaseModel, Field

T = TypeVar("T")


class CreateBatchModel(BaseModel):
    """
    A model class for creating a single document batch.
    """
    batch_name: str = Field(..., min_length=3, max_length=180)
    workflow_id: UUID


@dataclass
class CloudEventV1(Generic[T]):
    """
    A class representing an incoming cloud event.
    """
    id: str
    data: T
    source: str