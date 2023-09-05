"""
Module for a service providing recognition functionality in this service.
"""
from PIL import Image
from os import environ
import pytesseract


class RecognitionService:
    """
    A class representing the entire public functionality of the recognition module.
    """
    def __init__(self, tess_path: str | None = None):
        if tess_path == None:
            self._tesseract_path = environ["TESSERACT_PATH"]
        else:
            self._tesseract_path = tess_path
        self._default_lang = "eng"
    
    @property
    def tesseract_path(self) -> str:
        """
        A path to the Tesseract executable file.
        """
        return self._tesseract_path
    
    @property
    def available_languages(self):
        """
        A list of supported languages by Tesseract.
        """
        return pytesseract.get_languages(config="")

    def process_image_by_path(self, path: str, lang: str | None = None) -> str:
        """
        Processes an image based on a specified path.
        """
        language = lang if lang is not None else self._default_lang
        return pytesseract.image_to_string(Image.open(path), language)
