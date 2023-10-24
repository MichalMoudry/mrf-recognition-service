"""
Package containing DTO's for database select queries.
"""
from datetime import datetime
from dataclasses import dataclass
from uuid import UUID


@dataclass
class BatchInfo:
    """
    A DTO for document batch select queries.
    """
    id: UUID
    name: str
    start_date: datetime
    completed_date: datetime | None


@dataclass
class ProcessedDocumentDto:
    """
    A DTO for a processed document.
    """
    id: UUID
    name: str
    data: bytes
    content_type: str
    archive_key: str | None
    is_archived: bool
