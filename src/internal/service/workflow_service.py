"""
Package containing code for a workflow service.
"""
from uuid import UUID
from .database import Session


class WorkflowService:
    """
    A service class for working with processing workflows.
    """
    @staticmethod
    def get_workflow(batch_id: UUID):
        ...
