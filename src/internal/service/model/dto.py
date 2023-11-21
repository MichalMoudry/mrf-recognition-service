"""
Module containing DTOs related to the service layer.
"""
from abc import ABC
from datetime import datetime
from io import BytesIO
from typing import Optional
from uuid import UUID
from PIL import Image
from attr import dataclass

from internal.database.model import BatchState


class JsonSerializable(ABC):
    """
    An abstract class for JSON serializable classes.
    """

    def serialize(self):
        pass


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
class BatchStatistic(JsonSerializable):
    """
    A DTO encapsulating information/statistics about a document batch.
    """
    batch_id: UUID
    start_date: datetime
    end_date: datetime
    number_of_documents: int
    status: int
    workflow_id: UUID

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "batch_id": f"{self.batch_id}",
            "start_date": f"{self.start_date}",
            "end_date": f"{self.end_date}",
            "number_of_documents": self.number_of_documents,
            "status": self.status,
            "workflow_id": f"{self.workflow_id}"
        }


@dataclass
class BatchFinishEvent(JsonSerializable):
    """
    A DTO encapsulating an event of a finished batch.
    """
    batch_id: UUID
    user_id: str
    status: BatchState

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "batch_id": f"{self.batch_id}",
            "user_id": self.user_id,
            "status": self.status
        }


@dataclass
class BatchInfo(JsonSerializable):
    """
    A DTO for document batch select queries.
    """
    id: UUID
    name: str
    start_date: datetime
    completed_date: datetime | None
    status: BatchState

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "id": f"{self.id}",
            "name": f"{self.name}",
            "start_date": f"{self.start_date}",
            "completed_date": self.completed_date,
            "status": self.status
        }


@dataclass
class ProcessedDocumentDto(JsonSerializable):
    """
    A DTO for a processed document.
    """
    id: UUID
    name: str
    data_base64: str
    content_type: str
    archive_key: str | None
    is_archived: bool

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "id": f"{self.id}",
            "name": f"{self.name}",
            "data_base64": f"{self.data_base64}",
            "content_type": self.content_type,
            "archive_key": self.archive_key,
            "is_archived": f"{self.is_archived}"
        }


@dataclass
class DocumentResultDto(JsonSerializable):
    """
    A DTO for a processed document result.
    """
    id: UUID
    name: str
    value: str
    document_id: UUID

    def serialize(self):
        """
        Method for assisting in JSON serialization.
        """
        return {
            "id": f"{self.id}",
            "name": self.name,
            "value": self.value,
            "document_id": f"{self.document_id}"
        }


@dataclass
class WorkflowDto:
    """
    A DTO for a recognition workflow.
    """
    id: UUID
    is_full_page_recognition: bool
    expect_diff_images: bool
    skip_enhancement: bool


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
