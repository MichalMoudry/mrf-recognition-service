"""
Module with basic API tests of the recognition service.
"""
import json
from cloudevents.sdk.event import v1
from datetime import datetime
from pathlib import Path
from uuid import uuid4
from pytest import mark
from quart.datastructures import FileStorage
from internal.transport.model import contracts
from internal.transport.model.contracts import WorkflowSettings
from main import app, services
from internal.database import Session, model


def setup_workflow():
    """
    Function for setting up a test processing workflow.
    """
    workflow_id = uuid4()
    now = datetime.utcnow()
    session = Session()
    session.add(
        model.Workflow(
            id=workflow_id,
            is_full_page_recognition=True,
            skip_enhancement=False,
            expect_diff_images=False,
            date_added=now,
            date_updated=now
        )
    )
    session.commit()
    return workflow_id


def setup_batch():
    """
    Function for setting up a test document batch.
    """
    workflow_id = setup_workflow()
    session = Session()
    batch = model.new_document_batch("test_batch", "test_author", workflow_id, [])
    session.add(batch)
    session.commit()
    return (batch.id, workflow_id)


async def test_health_method():
    """
    A simple test scenario for testing /health endpoint.
    """
    client = app.test_client()
    res = await client.get("/health")
    assert res.status_code == 200
    assert (await res.data) == b'healthy'


@mark.skip(reason="Only runnable with a database running.")
async def test_basic_file_upload():
    """
    A test scenario covering a basic file upload.
    """
    workflow_id = setup_workflow()
    folder = Path(__file__).parent.parent / "tests/test_images"
    client = app.test_client()
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")

    res = await client.post(
        "/batch",
        form={
            "batch_name": "test_batch_1",
            "workflow_id": f"{workflow_id}",
            "user_id": "test_user_1"
        },
        files={
            "file1": FileStorage(file1, content_type=".jpg"),
            "file2": FileStorage(file2, content_type=".png")
        }
    )

    file1.close()
    file2.close()
    assert res.status_code == 201


@mark.skip(reason="Only runnable with a Tesseract engine and DB.")
async def test_file_upload_bt():
    """
    A test for validating a background task that is spawned during a file upload.
    """
    folder = Path(__file__).parent.parent / "tests/test_images"
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")
    batch_id, workflow_id = setup_batch()

    await services.fp_service.process_files(
        batch_id,
        workflow_id,
        {
            "file1": FileStorage(file1, content_type=".jpg"),
            "file2": FileStorage(file2, content_type=".png")
        }
    )


def test_cloud_event_handling():
    """
    A test covering handling of cloud events in handler methods.
    """
    workflow_id = uuid4()
    test_event = v1.Event()
    test_event.SetData(f"\"{workflow_id}\"")
    test_event.SetSource("test_service")
    test_event.SetEventTime("2023-11-6T12:41:00Z")
    test_event.SetEventID("id-1234-5678-9101")

    data = test_event.Data()
    parsed_data = json.loads(str(data))
    assert str(workflow_id) == parsed_data


def test_complex_cloud_event_handling():
    """
    Test handling of more complex events.
    """
    settings = WorkflowSettings(
        is_full_page_recognition=True,
        expect_diff_images=False,
        skip_img_recognition=True
    )
    settings_str = json.dumps({
        "is_full_page_recognition": settings.is_full_page_recognition,
        "skip_img_enchancement": settings.skip_img_recognition,
        "expecte_diff_images": settings.expect_diff_images
    })

    test_event = v1.Event()
    test_event.SetData(settings_str)
    test_event.SetSource("test_service")
    test_event.SetEventTime("2023-11-6T12:41:00Z")
    test_event.SetEventID("id-1234-5678-9101")
    data = test_event.Data()
    parsed_data = json.loads(str(data))
    assert str(parsed_data).lower().replace("\'", "\"") == settings_str


@mark.skip(reason="Only runnable with a database running.")
async def test_create_template():
    """
    Testing POST /template endpoint.
    """
    folder = Path(__file__).parent.parent / "tests/test_images"
    client = app.test_client()
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")

    res = await client.post(
        "/template",
        form={
            "template_name": "test_template_1",
            "width": "54.32",
            "height": "32.22",
            "workflow_id": f"{uuid4()}",
            "fields": contracts.TemplateFieldModel(
                field_name="test_field_1",
                width=10,
                height=10,
                x_position=1,
                y_position=2,
                is_identifying=False
            ).model_dump_json()
        },
        files={
            "file1": FileStorage(file1, content_type=".jpg")
        }
    )

    file1.close()
    file2.close()
    assert res.status_code == 201
