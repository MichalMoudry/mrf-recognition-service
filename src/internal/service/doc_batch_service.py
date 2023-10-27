"""
Package with code comprising the document batch service.
"""
import base64
from uuid import UUID
from internal.database import Session
from internal.database.model import new_document_batch, new_processsed_document
from internal.database import query
from internal.service.model.dto import BatchInfo, ProcessedDocumentDto


def encode_to_base64(data: bytes | None):
    """
    Method for encoding a byte array to a base64 string.
    """
    if data is None: return ""
    return base64.b64encode(data).decode()


class DocumentBatchService:
    """
    A service class for handling logic related to document batches.
    """

    @staticmethod
    def create_batch(name: str, user_id: str, workflow_id: UUID) -> UUID:
        """
        Function for creating a new document batch in the system.
        """
        session = Session()
        batch = new_document_batch(name, user_id, workflow_id, [])
        session.add(batch)
        session.commit()
        return batch.id

    @staticmethod
    def get_batch(batch_id: UUID):
        session = Session()
        rows = session.execute(query.select_batch(batch_id)).all()
        session.commit()
        rows_len = len(rows)
        if rows_len == 0:
            return None
        return [BatchInfo(row[0], row[1], row[2], row[3], row[4]).serialize() for row in rows][0]

    @staticmethod
    def get_batches(workflow_id: UUID):
        """
        A method for obtaining a list of information about document batches.
        """
        session = Session()
        rows = session.execute(query.select_batches(workflow_id)).all()
        session.commit()
        return [BatchInfo(row[0], row[1], row[2], row[3], row[4]).serialize() for row in rows]

    @staticmethod
    def get_batch_images(batch_id: UUID):
        """
        A method for obtaining images from a specific document batch.
        """
        session = Session()
        res = session.execute(query.select_processed_documents(batch_id)).all()
        session.commit()
        return [
            ProcessedDocumentDto(row[0], row[1], encode_to_base64(row[2]), row[3], row[4], row[5]).serialize()
            for row in res
        ]

    @staticmethod
    def delete_batch(batch_id: UUID):
        session = Session()
        session.execute(query.delete_batch(batch_id))
        session.commit()
