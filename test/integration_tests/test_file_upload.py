"""
Module with file upload API tests of the recognition service.
"""
import asyncio
from pathlib import Path
from src.main import app


async def test_basic_file_upload():
    """
    A test scenario covering a basic file upload.
    """
    def test():
        app.config.update({
            "TESTING": True,
        })
        client = app.test_client()

        folder = Path(__file__).parent.parent / "test_images"
        response = client.post("/batch", data={
            "batch_name": "test_batch_1",
            "file": (folder / "repo_screenshot.png").open("rb"),
            "file2": (folder / "repo_screenshot.png").open("rb")
        })
        assert response.status_code == 201
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, test)
