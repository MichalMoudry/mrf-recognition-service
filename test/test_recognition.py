"""
Module for testing recognition service.
"""
from os import environ, path, getcwd
from pytest import mark
from src.service.recognition import RecognitionService, TesseractService


def test_service_setup():
    """
    A test where setup of the recognition service is tested.
    """
    environ["TESSERACT_PATH"] = "/opt/homebrew/bin/tesseract"
    service = TesseractService()
    assert service.available_languages == ["eng", "osd", "snum"]
    assert isinstance(service, RecognitionService) is True
    assert issubclass(TesseractService, RecognitionService) is True


@mark.skip(reason="Can be allowed to run on systems with recognition capabilities")
def test_img_recognition_by_path():
    """
    A test where a test image specified by path is recognized.
    """
    service = TesseractService("/opt/homebrew/bin/tesseract")
    result = service.process_img_by_path(
        path.join(getcwd(), "test/test_images/repo_screenshot.png")
    )
    assert "Identity microservice example" in result
    assert "Solution structure" in result
    assert "Infrastructure" in result
