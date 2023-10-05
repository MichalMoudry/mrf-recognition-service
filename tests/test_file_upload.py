"""
Module with file upload API tests of the recognition service.
"""
"""
from pathlib import Path
from quart.datastructures import FileStorage
from src.main import app


async def test_basic_file_upload():
    # A test scenario covering a basic file upload.
    client = app.test_client()
    folder = Path(__file__).parent.parent / "tests/test_images"
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")
    res = await client.post(
        "/batch",
        form={
            "batch_name": "test_batch_1"
        },
        files={
            "file1": FileStorage(file1, content_type=".jpg"),
            "file2": FileStorage(file2, content_type=".png")
        }
    )
    file1.close()
    file2.close()
    assert res.status_code == 201"""
