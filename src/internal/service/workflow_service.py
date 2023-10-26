"""
Module containing code for a workflow service.
"""
from uuid import UUID
from internal.database import Session
from internal.database.query import delete_workflow


class WorkflowService:
    """
    A service class for working with processing workflows.
    """
    @staticmethod
    def get_workflow(batch_id: UUID):
        ...

    @staticmethod
    def delete_workflow(workflow_id: UUID):
        """
        A method for deleting a specific workflow in the system.
        """
        session = Session()
        session.execute(delete_workflow(workflow_id))
        session.commit()

    @staticmethod
    def update_workflow():
        """
        A method for updating a specific workflow.
        """
