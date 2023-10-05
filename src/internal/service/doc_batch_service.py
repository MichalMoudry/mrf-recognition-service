"""
Package with code comprising the document batch service.
"""
from uuid import UUID
from datetime import datetime
from internal.database import Session
from internal.database.model import DocumentBatch, new_processsed_document, BatchState
from internal.database.query import select_batch
from internal.transport.model.dto import DocumentDto


class DocumentBatchService:
    @staticmethod
    def create_batch(name: str, workflow_id: UUID, documents: list[DocumentDto]):
        """
        Function for creating a new document batch in the system.
        """
        session = Session()

        batch = DocumentBatch(
            name=name,
            state=BatchState.PROCESSING,
            documents=[
                new_processsed_document() for x in documents
            ],
            workflow_id=workflow_id
        )
        batch.date_added=batch.date_updated=batch.start_date = datetime.utcnow()

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