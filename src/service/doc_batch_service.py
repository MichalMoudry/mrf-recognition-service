"""
Package with code comprising the document batch service.
"""
from uuid import UUID
from datetime import datetime
from src.database import Session
from src.database.model import DocumentBatch, ProcessedDocument, BatchState


class DocumentBatchService:
    @staticmethod
    def create_batch(name: str, workflow_id: UUID, documents: list[ProcessedDocument]):
        """
        Function for creating a new document batch in the system.
        """
        session = Session()

        batch = DocumentBatch(
            name=name,
            state=BatchState.PROCESSING,
            documents=documents,
            workflow_id=workflow_id
        )
        batch.date_added, batch.date_updated, batch.start_date = datetime.utcnow()

        session.add(batch)
        session.commit()
