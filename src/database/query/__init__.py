"""
Module containing all the database queries.
"""
from uuid import UUID
from sqlalchemy import select
from ..model import DocumentBatch, Workflow


def select_batch(batch_id: UUID):
    return select(
        DocumentBatch.id,
        DocumentBatch.name,
        DocumentBatch.start_date,
        DocumentBatch.completed_date
    ).where(DocumentBatch.id == batch_id)
