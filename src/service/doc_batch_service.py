"""
Package with code comprising the document batch service.
"""
from uuid import UUID
from datetime import datetime
from database import Session
from database.model import DocumentBatch, ProcessedDocument, BatchState
from database.query import select_batch


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

    @staticmethod
    def get_batch(batch_id: UUID):
        session = Session()
        res = session.execute(select_batch(batch_id)).first()
        session.commit()
        print(res)

    @staticmethod
    def delete_batch(batch_id: UUID):
        session = Session()

        session.commit()
