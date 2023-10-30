"""
Module containing code for a workflow service.
"""
from uuid import UUID
from internal.database import Session
from internal.database.query import select_workflow, delete_workflow
from internal.service.model.dto import WorkflowDto
from internal.transport.model.contracts import WorkflowSettings


class WorkflowService:
    """
    A service class for working with processing workflows.
    """
    @staticmethod
    def get_workflow(workflow_id: UUID):
        session = Session()
        rows = session.execute(select_workflow(workflow_id)).all()
        session.commit()
        if len(rows) == 0: return None
        return [WorkflowDto(row[0], row[1], row[2], row[3]) for row in rows][0]

    @staticmethod
    def delete_workflow(workflow_id: UUID):
        """
        A method for deleting a specific workflow in the system.
        """
        session = Session()
        session.execute(delete_workflow(workflow_id))
        session.commit()

    @staticmethod
    def update_workflow(id: UUID, settings: WorkflowSettings) -> bool:
        """
        A method for updating a specific workflow.
        """
        return True
