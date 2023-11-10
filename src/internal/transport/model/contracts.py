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


class TemplateFieldModel(BaseModel):
    field_name: str
    width: float
    height: float
    x_position: float
    y_position: float
    expected_value: str | None = Field(default=None)
    is_identifying: bool


class CreateTemplateModel(BaseModel):
    """
    A model class for creating a new document template.
    """
    template_name: str
    width: float
    height: float
    workflow_id: UUID
    fields: list[TemplateFieldModel] = Field(min_length=1)
