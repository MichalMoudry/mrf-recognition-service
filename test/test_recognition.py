"""
Module for testing recognition service.
"""
from os import environ, path, getcwd
from src.service.recognition import RecognitionService


def test_service_setup():
    """
    A test where setup of the recognition service is tested.
    """
    path = "/opt/homebrew/bin/tesseract"
    environ["TESSERACT_PATH"] = path
    service = RecognitionService()
    assert service.available_languages == ["eng", "osd", "snum"]
    assert service.tesseract_path == path


def test_img_recognition_by_path():
    """
    A test where a test image specified by path is recognized.
    """
    service = RecognitionService("/opt/homebrew/bin/tesseract")
    result = service.process_image_by_path(
        path.join(getcwd(), "test/test_images/repo_screenshot.png")
    )
    assert "Identity microservice example" in result
    assert "Solution structure" in result
    assert "Infrastructure" in result
