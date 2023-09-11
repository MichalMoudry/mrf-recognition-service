"""
Package with tests for Data Transfer Object validation.
"""
from os import path, getcwd
from pydantic import ValidationError
from src.transport.model.dto import *


def test_create_batch_model():
    """
    A simple test case where validation for correct CreateBatchModel instance is tested.
    """
    img_path = path.join(getcwd(), "test/test_images/repo_screenshot.png")
    with open(img_path, "rb") as file:
        try:
            CreateBatchModel(name="test_batch_1", files=[UploadFile(file)])
        except ValidationError as err:
            assert err is None


def test_create_batch_model_files_empty():
    """
    A simple test case where validation for CreateBatchModel
    instance with empty files is tested.
    """
    try:
        CreateBatchModel(name="test_batch_1", files=[])
    except ValidationError as err:
        assert err is not None
