"""
Module containing all the database queries.
"""
from datetime import datetime
from uuid import UUID
from sqlalchemy import select, insert, update, delete, Insert
from .model import DocumentBatch, Workflow, ProcessedDocument, DocumentTemplate, BatchState
from .dto import BatchInfo, ProcessedDocumentDto


def select_batch(batch_id: UUID):
    """
    Query for obtaining a query for selecting a specific batch from the database.
    """
    return select(
        BatchInfo
    ).where(DocumentBatch.id == batch_id)


def select_batches(user_id: str):
    """
    Query for selecting all user's document batches.
    """
    return select(
        BatchInfo
    ).where(DocumentBatch.author_id == user_id).order_by(DocumentBatch.start_date)


def update_batch(batch_id: UUID, status: BatchState, finish_date: datetime):
    """
    Query for updating a specific document batch.
    """
    return update(
        DocumentBatch
    ).where(
        DocumentBatch.id == batch_id
    ).values(
        state=status.value,
        completed_date=finish_date
    )


def delete_batch(batch_id: UUID):
    """
    Query for obtaining a delete query for deleting a specific document batch.
    """
    return delete(DocumentBatch).where(DocumentBatch.id == batch_id)


def delete_batch_by_uid(user_id: str):
    """
    Query for deleting all user's batches.
    """
    return delete(DocumentBatch).where(DocumentBatch.author_id == user_id)


def select_processed_documents(batch_id: UUID):
    """
    Query for obtaining processed documents for a specific batch.
    """
    return select(
        ProcessedDocumentDto
    ).where(ProcessedDocument.batch_id == batch_id)


def select_workflow(workflow_id: UUID):
    """
    Query for selecting a specific processing workflow.
    """
    return select(
        Workflow.id,
        Workflow.is_full_page_recognition,
        Workflow.expect_diff_images,
        Workflow.skip_enhancement,
        Workflow.date_added
    ).where(Workflow.id == workflow_id)


def delete_workflow(workflow_id: UUID):
    """
    Query for deleting a specific workflow.
    """
    return delete(Workflow).where(Workflow.id == workflow_id)


def select_document_templates(workflow_id: UUID):
    """
    Query for obtaining all templates for a specific workflow.
    """
    return select(
        DocumentTemplate.id,
        DocumentTemplate.name,
        DocumentTemplate.width,
        DocumentTemplate.height,
        DocumentTemplate.fields
    ).where(DocumentTemplate.workflow_id == workflow_id)


def insert_document_template(template: DocumentTemplate):
    """
    Query for inserting a new document template into 
    """
    return insert(DocumentTemplate).values(
        id=template.id,
        name=template.name,
        width=template.width,
        height=template.height,
        image=template.image,
        workflow_id=template.workflow_id
    )


def delete_template(template_id: UUID):
    """
    Query for deleting a specific document template in the database.
    """
    return delete(DocumentTemplate).where(DocumentTemplate.id == template_id)
