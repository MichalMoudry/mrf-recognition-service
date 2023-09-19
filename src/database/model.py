"""
A module with database model classes.
"""
from enum import Enum
from uuid import UUID
from sqlalchemy import String, Boolean, Integer, TIMESTAMP, ForeignKey, LargeBinary, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


class Entity(DeclarativeBase):
    """
    A base class for database entities.
    """
    id: Mapped[UUID] = mapped_column(primary_key=True)
    date_added = mapped_column(TIMESTAMP())
    date_updated = mapped_column(TIMESTAMP())


class BatchState(Enum):
    """
    An enum representing current state of the document batch.
    """
    PROCESSING = 0
    COMPLETED = 1
    FAILED = 2


class DocumentBatch(Entity):
    """
    A business object representing a batch of one or more documents.
    """
    __tablename__ = "document_batches"

    name = mapped_column(String(180))
    state = mapped_column(Integer)
    start_date = mapped_column(TIMESTAMP())
    completed_date = mapped_column(TIMESTAMP(), nullable=True)
    documents: Mapped[list["ProcessedDocument"]] = relationship()


class ProcessedDocument(Entity):
    """
    A business object representing a processed document.
    """
    __tablename__ = "processed_documents"

    name = mapped_column(String(180))
    content_type = mapped_column(String(240))
    is_archived = mapped_column(Boolean())
    archive_key = mapped_column(String(80))
    date_archived = mapped_column(TIMESTAMP())
    data = mapped_column(LargeBinary(), nullable=True)
    batch_id = mapped_column(ForeignKey("document_batches.id"))


class Workflow(Entity):
    """
    A business object representing a recognition workflow and its settings.
    """
    __tablename__ = "workflows"

    is_full_page_recog: Mapped[bool] = mapped_column(Boolean())
    skip_enhancement = mapped_column(Boolean())
    expect_diff_images = mapped_column(Boolean())


class DocumentTemplate(Entity):
    """
    A business object that represents a document template.
    """
    __tablename__ = "document_templates"

    data = mapped_column(LargeBinary(), nullable=False)
    width = mapped_column(Float())
    height = mapped_column(Float())
