"""
Module with definitions of contracts of this service.
"""
from uuid import UUID
from pydantic import BaseModel, Field


class CreateBatchModel(BaseModel):
    """
    A model class for creating a single document batch.
    """
    batch_name: str = Field(..., min_length=3, max_length=180)
    workflow_id: UUID
    user_id: str = Field(..., min_length=3, max_length=120)


class WorkflowSettings(BaseModel):
    """
    A model class for carrying workflow settings.
    """
    is_full_page_recognition: bool
    skip_img_recognition: bool
    expect_diff_images: bool
