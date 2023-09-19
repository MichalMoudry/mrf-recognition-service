"""
A module with database model classes.
"""
from enum import Enum
from sqlalchemy import String, Uuid, Boolean, SmallInteger, TIMESTAMP, ForeignKey, LargeBinary, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


class Entity(DeclarativeBase):
    """
    A base class for database entities.
    """
    id = mapped_column(Uuid(), primary_key=True)
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
    state: Mapped[int] = mapped_column(SmallInteger)
    start_date = mapped_column(TIMESTAMP())
    completed_date = mapped_column(TIMESTAMP(), nullable=True)
    workflow_id = mapped_column(ForeignKey("workflows.id"))
    documents: Mapped[list["ProcessedDocument"]] = relationship()


class ProcessedDocument(Entity):
    """
    A business object representing a processed document.
    """
    __tablename__ = "processed_documents"

    name = mapped_column(String(255))
    content_type = mapped_column(String(255))
    is_archived = mapped_column(Boolean())
    archive_key = mapped_column(String(128), nullable=True)
    date_archived = mapped_column(TIMESTAMP(), nullable=True)
    data = mapped_column(LargeBinary(), nullable=True)
    batch_id = mapped_column(ForeignKey("document_batches.id"))


class Workflow(Entity):
    """
    A business object representing a recognition workflow and its settings.
    """
    __tablename__ = "workflows"

    is_full_page_recognition: Mapped[bool] = mapped_column(Boolean())
    skip_enhancement: Mapped[bool] = mapped_column(Boolean())
    expect_diff_images: Mapped[bool] = mapped_column(Boolean())
    templates: Mapped[list["DocumentTemplate"]] = relationship()
    batches: Mapped[list["DocumentBatch"]] = relationship()


class DocumentTemplate(Entity):
    """
    A business object that represents a document template.
    """
    __tablename__ = "document_templates"

    width: Mapped[float] = mapped_column(Float())
    height: Mapped[float] = mapped_column(Float())
    workflow_id = mapped_column(ForeignKey("workflows.id"))
    fields: Mapped[list["TemplateField"]] = relationship()


class TemplateField(Entity):
    """
    A business object representing document template's field.
    """
    __tablename__ = "template_fields"

    width = mapped_column(Float())
    height = mapped_column(Float())
    x_position = mapped_column(Float())
    y_position = mapped_column(Float())
    expected_value = mapped_column(String(255), nullable=True)
    is_identifying = mapped_column(Boolean())
    template_id = mapped_column(ForeignKey("document_templates.id"))
