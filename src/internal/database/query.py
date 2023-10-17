"""
Module containing all the database queries.
"""
from uuid import UUID
from sqlalchemy import select, insert, delete, Insert
from .model import DocumentBatch, Workflow, ProcessedDocument, DocumentTemplate
#from model import DocumentBatch, Workflow, ProcessedDocument, DocumentTemplate


def select_batch(batch_id: UUID):
    """
    Query for obtaining a query for selecting a specific batch from the database.
    """
    return select(
        DocumentBatch.id,
        DocumentBatch.name,
        DocumentBatch.start_date,
        DocumentBatch.completed_date
    ).where(DocumentBatch.id == batch_id)


def insert_batch(batch: DocumentBatch) -> Insert:
    """
    Query for obtaining a query for inserting a document batch to the database.
    """
    return insert(DocumentBatch).values(
        id=batch.id,
        name=batch.name,
        state=0,
        start_date=batch.start_date,
        workflow_id=batch.workflow_id,
        date_added=batch.date_added,
        date_updated=batch.date_updated
    )


def delete_batch(batch_id: UUID):
    """
    Query for obtaining a delete query for deleting a specific document batch.
    """
    return delete(DocumentBatch).where(DocumentBatch.id == batch_id)


def select_processed_documents(batch_id: UUID):
    """
    Query for obtaining processed documents for a specific batch.
    """
    return select(
        ProcessedDocument.id,
        ProcessedDocument.name,
        ProcessedDocument.data,
        ProcessedDocument.content_type,
        ProcessedDocument.is_archived
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
