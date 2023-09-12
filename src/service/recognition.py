"""
Module for a service providing recognition functionality in this service.
"""
from typing import Optional
from enum import Enum
from abc import ABC, abstractmethod
from PIL import Image
from os import environ
import pytesseract


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


class TesseractService(RecognitionService):
    """
    An implementation of a recognition service that is based in Tesseract.
    """
    def __init__(self, tess_path: Optional[str] = None) -> None:
        super().__init__()
        if tess_path is None:
            self._tesseract_path = "/opt/homebrew/bin/tesseract" #environ["TESSERACT_PATH"]
        else:
            self._tesseract_path = tess_path

    @property
    def available_languages(self):
        return pytesseract.get_languages(config="")
    
    def process_img_by_path(self, path: str, lang: Optional[str] = None) -> str:
        language = lang if lang is not None else super().default_language
        return pytesseract.image_to_string(Image.open(path), language)


def get_recognition_service(service_type: RecognitionServiceType) -> RecognitionService:
    """
    Method that returns a specific instance of a recognition service.
    """
    match service_type:
        case RecognitionServiceType.TESSERACT:
            return TesseractService()
        case _:
            return TesseractService()
