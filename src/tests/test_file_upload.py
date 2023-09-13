"""
Module with file upload API tests of the recognition service.
"""
from pathlib import Path
from quart.datastructures import FileStorage
from src.main import app


async def test_basic_file_upload():
    """
    A test scenario covering a basic file upload.
    """
    client = app.test_client()
    folder = Path(__file__).parent.parent / "tests/test_images"
    with (folder / "repo_screenshot.png").open("rb") as file:
        res = await client.post(
            "/batch",
            form={
                "batch_name": "test_batch_1"
            },
            files={
                "file1": FileStorage(file, content_type=".png"),
                "file2": FileStorage(file, content_type=".png")
            }
        )
        assert res.status_code == 201
