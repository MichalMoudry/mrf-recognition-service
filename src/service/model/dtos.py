"""
Module containing DTOs related to the service layer.
"""
from abc import ABC
from dataclasses import dataclass
from typing import Any


class JsonSerializable(ABC):
    """
    An abstract class for JSON serializable classes.
    """

    def serialize(self) -> dict[str, Any]:
        """
        A method for serializing contents of the DTO to a JSON serializable form.
        """
        ...


@dataclass
class BoundingBox:
    """
    A DTO representing a single bounding box on the image.
    """
    value: str
    left: int
    top: int
    width: int
    height: int
