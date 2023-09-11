"""
Module with file upload API tests of the recognition service.
"""
from pathlib import Path
from src.main import app


def test_basic_file_upload():
    app.config.update({
        "TESTING": True,
    })
    client = app.test_client()

    folder = Path(__file__).parent.parent / "test_images"
    response = client.post("/batch", data={
        "name": "test_batch",
        "file": (folder / "repo_screenshot.png").open("rb")
    })
    print(response)
