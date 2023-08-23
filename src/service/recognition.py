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
    def __init__(self):
        ...


def get_recognition_service() -> RecognitionService:
    ...


def process_image():
    ...
