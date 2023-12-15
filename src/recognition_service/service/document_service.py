"""
Module with code comprising the document batch service.
"""
from datetime import datetime
from psycopg import Connection
from uuid import UUID, uuid4

from recognition_service.database import batch_queries


class DocumentService:
    """
    A service class for handling logic related to document batches.
    """

    @staticmethod
    def create_batch(conn: Connection, name: str, user_id: str, workflow_id: UUID):
        """
        Function for creating a new document batch in the system.
        """
        now = datetime.now()
        """with conn.cursor() as cur:
            cur.execute(
                batch_queries.insert_batch,
                (
                    uuid4(),
                    name,
                    0,
                    None,
                    None,
                    workflow_id,
                    user_id,
                    now,
                    now
                )
            )"""
