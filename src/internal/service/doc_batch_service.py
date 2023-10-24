"""
Package with code comprising the document batch service.
"""
from uuid import UUID, uuid4
from internal.database import Session
from internal.database.model import new_document_batch, new_processsed_document
from internal.database import query
from internal.database.dto import BatchInfo, ProcessedDocumentDto
from internal.transport.model.dto import DocumentDto


class DocumentBatchService:
    """
    A service class for handling logic related to document batches.
    """

    @staticmethod
    def create_batch(name: str, user_id: str, workflow_id: UUID, documents: list[DocumentDto]) -> UUID:
        """
        Function for creating a new document batch in the system.
        """
        session = Session()
        
        batch_id = uuid4()
        batch = new_document_batch(batch_id, name, user_id, workflow_id, [
            new_processsed_document(doc.name, doc.content_type, doc.content, batch_id)
            for doc in documents
        ])

        session.execute(query.insert_batch(batch))
        session.bulk_save_objects(batch.documents)
        session.commit()
        return batch_id

    @staticmethod
    def get_batch(batch_id: UUID) -> BatchInfo | None:
        session = Session()
        res = session.execute(query.select_batch(batch_id)).first()
        session.commit()
        if res is None:
            return None
        return res.t[0]

    @staticmethod
    def get_batch_images(batch_id: UUID) -> list[ProcessedDocumentDto]:
        """
        A method for obtaining images from a specific document batch.
        """
        session = Session()
        res = session.execute(query.select_processed_documents(batch_id)).all()
        session.commit()
        return [row.t[0] for row in res]

    @staticmethod
    def delete_batch(batch_id: UUID):
        session = Session()
        session.execute(query.delete_batch(batch_id))
        session.commit()
