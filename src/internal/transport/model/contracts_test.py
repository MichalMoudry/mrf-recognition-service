"""
Module with tests for Data Transfer Object validation.
"""
import json
from cloudevents.http import CloudEvent
from uuid import uuid4
from pydantic import ValidationError
from quart import jsonify

from internal.service.model.dto import WorkflowDto
from main import app
from . import contracts


def test_create_batch_model():
    """
    A simple test case where validation for correct CreateBatchModel instance is tested.
    """
    try:
        contracts.CreateBatchModel(batch_name="test_batch_1", workflow_id=uuid4(), user_id="test_user")
    except ValidationError as err:
        assert err is None


def test_create_batch_model_empty_name():
    """
    A simple test case where validation for CreateBatchModel
    instance with empty batch name is tested.
    """
    try:
        contracts.CreateBatchModel(batch_name="", workflow_id=uuid4(), user_id="test_user")
    except ValidationError as err:
        assert err is not None


def test_workflow_settings_init():
    """
    A test case covering initalization of WorkflowSetting class.
    """
    try:
        contracts.WorkflowSettings(
            is_full_page_recognition=True,
            skip_img_recognition=True,
            expect_diff_images=False
        )
    except ValidationError as err:
        assert err is None


def test_workflow_settings_wrong_init():
    """
    A test case coverting initialization of WorkflowSetting class
    """
    try:
        contracts.WorkflowSettings(
            is_full_page_recognition="tr-ue",
            skip_img_recognition="True",
            expect_diff_images="False"
        )
    except ValidationError as err:
        assert err is not None


def test_default_create_template_model():
    """
    Testing a default init of CreateTemplateModel class.
    """
    try:
        dto = contracts.CreateTemplateModel(
            template_name="test_template",
            width=50,
            height=30,
            workflow_id=uuid4(),
            fields=[
                contracts.TemplateFieldModel(
                    field_name="test_field_1",
                    width=10,
                    height=10,
                    x_position=2,
                    y_position=1,
                    is_identifying=False
                ),
                contracts.TemplateFieldModel(
                    field_name="test_field_2",
                    width=10,
                    height=10,
                    x_position=2,
                    y_position=1,
                    is_identifying=False
                )
            ]
        )
        json_str = dto.model_dump_json()
        assert len(json_str) > 0
    except ValidationError as err:
        assert err is None


def test_simple_cloudevent():
    """
    A test scenario covering unmarshalling of a cloud event with a simple payload.
    """
    event_attributes = {
        "type": "com.testservice.test",
        "source": "test-service"
    }
    data = f"{uuid4()}"
    test_event = CloudEvent(event_attributes, data)
    assert test_event.data == data


def test_complex_cloudevent_object():
    """
    A test scenario covering unmarshalling of a cloud event with complex payload.
    """
    event_attributes = {
        "type": "com.testservice.test",
        "source": "test-service"
    }
    data = {
        "workflow_id": f"{uuid4()}",
        "is_full_page_recognition": True,
        "skip_img_enchancement": False,
        "expect_diff_images": True
    }

    test_event = CloudEvent(event_attributes, data)
    dto = WorkflowDto(
        id=test_event.data["workflow_id"],
        is_full_page_recognition=test_event.data["is_full_page_recognition"],
        expect_diff_images=test_event.data["expect_diff_images"],
        skip_enhancement=test_event.data["skip_img_enchancement"]
    )
    assert test_event["source"] == event_attributes["source"]
    assert dto.id == data["workflow_id"]
    assert dto.is_full_page_recognition == data["is_full_page_recognition"]
    assert dto.expect_diff_images == data["expect_diff_images"]
    assert dto.skip_enhancement == data["skip_img_enchancement"]


async def test_jsonify():
    async with app.app_context():
        test_message = "success"
        result = await jsonify(test_message).json
        assert len(result) > 0
        assert result is not None
