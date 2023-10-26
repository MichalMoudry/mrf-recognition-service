"""
Module containing DTOs related to the service layer.
"""
from datetime import datetime
from io import BytesIO
from typing import Optional
from uuid import UUID
from PIL import Image
from attr import dataclass


class ProcessedDocumentInfo:
    """
    A DTO for storing information about currently processed document.
    """

    def __init__(self, name: str, content: bytes, type: str) -> None:
        self._name = name
        self._content = content
        self._image = Image.open(BytesIO(content))
        self._type = type
        self._results = []
        self._was_successful = True

    @property
    def name(self) -> str:
        """
        A name of the processed document.
        """
        return self._name

    @property
    def content(self) -> Optional[bytes]:
        """
        A content of the processed document.
        """
        return self._content

    @property
    def pil_image(self) -> Image.Image:
        """
        A PIL image of the processed document.
        """
        return self._image

    @property
    def content_type(self) -> str:
        """
        Content type of the processed document.
        """
        return self._type

    @property
    def results(self) -> list[str]:
        """
        Results from the document processing.
        """
        return self._results

    @results.setter
    def results(self, res: list[str]) -> None:
        """
        Method for setting results of the processing.
        """
        self._results = res

    def empty_content(self) -> None:
        """
        Method for emptying content.
        """
        self._content = None

    @property
    def was_successful(self) -> bool:
        """
        A result of the document's processing.
        """
        return self._was_successful

    @was_successful.setter
    def was_successful(self, result: bool) -> None:
        """
        Method for setting result of processing.
        """
        self._was_successful = result


@dataclass
class BatchStatistic:
    """
    A DTO encapsulating information/statistics about a document batch.
    """
    batch_id: UUID
    start_date: datetime
    end_date: datetime
    number_of_documents: int
    status: int

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "batch_id": f"{self.batch_id}",
            "start_date": f"{self.start_date}",
            "end_date": f"{self.end_date}",
            "number_of_documents": self.number_of_documents,
            "status": self.status
        }
