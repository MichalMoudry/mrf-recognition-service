"""
Package containing a collection of all services.
"""
from .doc_batch_service import DocumentBatchService
from .workflow_service import WorkflowService


class ServiceCollection:
    """
    Class with attributes for each service.
    """

    def __init__(self) -> None:
        self._doc_batch_service = DocumentBatchService()
        self._workflow_service = WorkflowService()

    @property
    def document_batch_service(self) -> DocumentBatchService:
        return self._doc_batch_service

    @property
    def workflow_service(self) -> WorkflowService:
        return self._workflow_service
