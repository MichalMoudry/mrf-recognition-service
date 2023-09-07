"""
Module for a service providing recognition functionality in this service.
"""
from abc import ABC, abstractmethod
from PIL import Image
from os import environ
import pytesseract


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
        ...

    @abstractmethod
    def process_img_by_path(self, path: str, lang: str | None = None) -> str:
        """
        Processes an image based on a specified path.
        """
        ...


class TesseractService(RecognitionService):
    """
    An implementation of a recognition service that is based in Tesseract.
    """
    def __init__(self, tess_path: str | None = None) -> None:
        super().__init__()
        if tess_path == None:
            self._tesseract_path = environ["TESSERACT_PATH"]
        else:
            self._tesseract_path = tess_path

    @property
    def available_languages(self):
        return pytesseract.get_languages(config="")
    
    def process_img_by_path(self, path: str, lang: str | None = None) -> str:
        language = lang if lang is not None else super().default_language
        return pytesseract.image_to_string(Image.open(path), language)
