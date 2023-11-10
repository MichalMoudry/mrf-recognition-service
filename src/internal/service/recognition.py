"""
Module for a service providing recognition functionality in this service.
"""
from typing import Optional
from enum import Enum
from abc import ABC, abstractmethod
from PIL import Image
from os import environ
import pytesseract

from internal.service.model.dto import BoundingBox


class RecognitionServiceType(Enum):
    """
    An enum class that represents a type of recognition service.
    """
    TESSERACT = 0


class RecognitionService(ABC):
    """
    An abstract class representing a generic service for recognizing documents.
    """
    default_language = "eng"

    def __init__(self) -> None:
        super().__init__()

    @property
    def available_languages(self) -> list[str]:
        """
        A list of supported languages by the recognition service/system.
        """
        return [self.default_language]

    @abstractmethod
    def process_img_by_path(self, path: str, lang: Optional[str] = None) -> str:
        """
        Processes an image based on a specified path.
        """
        ...

    @abstractmethod
    def process_image_full(
        self,
        image: Image.Image,
        lang: Optional[str] = None) -> list[str]:
        """
        Method for a full page processing of a PIL image.
        """
        ...

    @abstractmethod
    def process_image_with_bounding_boxes(
        self,
        image: Image.Image,
        lang: Optional[str] = None
    ) -> list[BoundingBox]:
        """
        Method for processing an image with bouding boxes estimates.
        """
        ...


class TesseractService(RecognitionService):
    """
    An implementation of a recognition service that is based in Tesseract.
    """
    def __init__(self, tess_path: Optional[str] = None) -> None:
        super().__init__()
        self._default_language = super().default_language
        if tess_path is None:
            cmd_path = environ.get("TESSERACT_PATH")
            self._tesseract_path = cmd_path if not None else "/opt/homebrew/bin/tesseract"
        else:
            self._tesseract_path = tess_path

    @property
    def available_languages(self):
        return pytesseract.get_languages(config="")
    
    def process_img_by_path(self, path: str, lang: Optional[str] = None) -> str:
        language = lang if lang is not None else self._default_language
        return pytesseract.image_to_string(Image.open(path), language)

    def process_image_full(self, image: Image.Image, lang: Optional[str] = None) -> list[str]:
        language = lang if lang is not None else self._default_language
        return str(pytesseract.image_to_string(image, language)).split("\n\n")

    def process_image_with_bounding_boxes(self, image: Image.Image, lang: Optional[str] = None) -> list[BoundingBox]:
        results = pytesseract.image_to_data(image, output_type="dict")

        boxes: list[BoundingBox] = []
        for i in range(len(results["level"])):
            text = results["text"][i]
            if text == "" or text == " ":
                continue
            (x, y, w, h) = (results["left"][i], results["top"][i], results["width"][i], results["height"][i])
            boxes.append(
                BoundingBox(text, x, y, w, h)
            )
        return boxes


def get_recognition_service(service_type: RecognitionServiceType) -> RecognitionService:
    """
    Method that returns a specific instance of a recognition service.
    """
    match service_type:
        case RecognitionServiceType.TESSERACT:
            return TesseractService()
        case _:
            return TesseractService()
