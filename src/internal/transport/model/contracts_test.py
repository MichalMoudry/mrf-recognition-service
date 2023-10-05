"""
Module with tests for Data Transfer Object validation.
"""
from uuid import uuid4
from pydantic import ValidationError
from . import contracts


def test_create_batch_model():
    """
    A simple test case where validation for correct CreateBatchModel instance is tested.
    """
    try:
        contracts.CreateBatchModel(batch_name="test_batch_1", workflow_id=uuid4())
    except ValidationError as err:
        assert err is None


def test_create_batch_model_empty_name():
    """
    A simple test case where validation for CreateBatchModel
    instance with empty batch name is tested.
    """
    try:
        contracts.CreateBatchModel(batch_name="", workflow_id=uuid4())
    except ValidationError as err:
        assert err is not None


def test_correct_cloud_event():
    """
    A test case that verifies if data in the cloud event correspond to a specifed class.
    """
    temp_id = uuid4()
    event = contracts.CloudEventV1(
        id=f"{temp_id}",
        data=contracts.CreateBatchModel(batch_name="test", workflow_id=temp_id),
        source="test_service"
    )
    assert isinstance(event.data, contracts.CreateBatchModel)
