"""
Module for a service providing recognition functionality in this service.
"""

from abc import ABC, abstractmethod
from enum import IntEnum
from PIL import Image
import pytesseract
from typing import Optional

from service.model.dtos import BoundingBox


class RecognitionServiceType(IntEnum):
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

    @property
    def available_languages(self):
        return pytesseract.get_languages(config="")

    def process_img_by_path(self, path: str, lang: Optional[str] = None) -> str:
        language = lang if lang is not None else self.default_language
        return pytesseract.image_to_string(Image.open(path), language)

    def process_image_full(self, image: Image.Image, lang: Optional[str] = None) -> list[str]:
        language = lang if lang is not None else self.default_language
        res = str(pytesseract.image_to_string(image, language))
        if len(res) >= 1024:
            resulting_list: list[str] = []
            blocks = res.split("\n\n")
            for block in blocks:
                if len(block) >= 1024:
                    resulting_list.extend(block.splitlines())
                else:
                    resulting_list.append(block)
            return resulting_list
        else:
            return res.split("\n\n")

    def process_image_with_bounding_boxes(
            self,
            image: Image.Image,
            lang: Optional[str] = None
        ) -> list[BoundingBox]:
        results = pytesseract.image_to_data(image, output_type="dict", lang=lang)

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
