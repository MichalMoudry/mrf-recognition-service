"""
Module for testing recognition service.
"""
from os import environ, path, getcwd
from pytest import mark
from PIL import Image
import json

from internal.service.model.dto import BoundingBox
from internal.service.recognition import RecognitionService, TesseractService


@mark.skip(reason="Can be allowed to run on systems with recognition capabilities")
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
        path.join(getcwd(), "tests/test_images/repo_screenshot.png")
    )
    assert "Identity microservice example" in result
    assert "Solution structure" in result
    assert "Infrastructure" in result


@mark.skip(reason="Can be allowed to run on systems with recognition capabilities")
def test_image_recognition_full():
    """
    A test covering a complete image recognition.
    """
    environ["TESSERACT_PATH"] = "/opt/homebrew/bin/tesseract"
    service = TesseractService()
    result = service.process_image_full(
        Image.open(path.join(getcwd(), "tests/test_images/repo_screenshot.png"))
    )
    json_result = json.dumps(result)
    assert len(result) > 0
    assert len(json_result) > 0
    assert "Identity microservice example" in result
    assert "Solution structure" in result


@mark.skip(reason="Can be allowed to run on systems with recognition capabilities")
def test_recognition_with_bounding_boxes():
    """
    A test where recognition with bounding boxes.
    """
    service = TesseractService("/opt/homebrew/bin/tesseract")
    result = service.process_image_with_bounding_boxes(
        Image.open(path.join(getcwd(), "tests/test_images/repo_screenshot.png"))
    )
    assert len(result) > 0
