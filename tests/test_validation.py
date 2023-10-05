"""
Package with tests for Data Transfer Object validation.
"""
from uuid import uuid4
from pydantic import ValidationError
from src.internal.transport.model import dto


def test_create_batch_model():
    """
    A simple test case where validation for correct CreateBatchModel instance is tested.
    """
    try:
        dto.CreateBatchModel(batch_name="test_batch_1", workflow_id=uuid4(), documents=[])
    except ValidationError as err:
        assert err is None


def test_create_batch_model_empty_name():
    """
    A simple test case where validation for CreateBatchModel
    instance with empty batch name is tested.
    """
    try:
        dto.CreateBatchModel(batch_name="", workflow_id=uuid4(), documents=[])
    except ValidationError as err:
        assert err is not None
