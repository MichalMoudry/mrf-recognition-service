"""
Package with code comprising the document batch service.
"""
from uuid import UUID, uuid4
from internal.database import Session
from internal.database.model import new_document_batch, new_processsed_document
from internal.database.query import select_batch, delete_batch
from internal.transport.model.dto import DocumentDto


class DocumentBatchService:
    @staticmethod
    def create_batch(name: str, user_id: str, workflow_id: UUID, documents: list[DocumentDto]):
        """
        Function for creating a new document batch in the system.
        """
        session = Session()
        
        batch_id = uuid4()
        batch = new_document_batch(batch_id, name, user_id, workflow_id, [
            new_processsed_document(doc.name, doc.content_type, doc.content, batch_id)
            for doc in documents
        ])

        session.add(batch)
        #session.add_all(batch.documents)
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
        session.execute(delete_batch(batch_id))
        session.commit()
