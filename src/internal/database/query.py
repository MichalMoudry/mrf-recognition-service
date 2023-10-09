"""
Module containing all the database queries.
"""
from uuid import UUID, uuid4
from sqlalchemy import select, insert, Insert
from .model import DocumentBatch, Workflow
#from model import DocumentBatch, Workflow


def select_batch(batch_id: UUID):
    """
    Function for obtaining a query for selecting a specific batch from the database.
    """
    return select(
        DocumentBatch.id,
        DocumentBatch.name,
        DocumentBatch.start_date,
        DocumentBatch.completed_date
    ).where(DocumentBatch.id == batch_id)


def insert_batch(batch: DocumentBatch) -> Insert:
    """
    Function for obtaining a query for inserting a document batch to the database.
    """
    return insert(DocumentBatch).values(
        id=uuid4(),
        name=batch.name,
        state=0,
        start_date=batch.start_date,
        workflow_id=batch.workflow_id,
        date_added=batch.date_added,
        date_updated=batch.date_updated
    )


def insert_processed_documents():
    """
    Function for inserting processed documents to the database.
    """
