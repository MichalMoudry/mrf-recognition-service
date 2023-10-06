"""
Module containing all the database queries.
"""
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import select, insert
from ..model import DocumentBatch, Workflow


def select_batch(batch_id: UUID):
    return select(
        DocumentBatch.id,
        DocumentBatch.name,
        DocumentBatch.start_date,
        DocumentBatch.completed_date
    ).where(DocumentBatch.id == batch_id)


def insert_batch(batch: DocumentBatch):
    insert(DocumentBatch).values(
        id=uuid4(),
        name=batch.name,
        state=batch.state,
        start_date=batch.start_date,
        workflow_id=batch.workflow_id,
        date_added=batch.date_added,
        date_updated=batch.date_updated
    )
    return
