"""
Module with basic API tests of the recognition service.
"""
from pathlib import Path
from uuid import uuid4
from pytest import mark
from quart.datastructures import FileStorage
from main import app


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
    folder = Path(__file__).parent.parent / "tests/test_images"
    client = app.test_client()
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")

    res = await client.post(
        "/batch",
        form={
            "batch_name": "test_batch_1",
            "workflow_id": f"{uuid4()}",
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
