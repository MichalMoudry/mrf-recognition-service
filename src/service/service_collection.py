"""
Package containing a collection of all services.
"""
from .doc_batch_service import DocumentBatchService
from .workflow_service import WorkflowService


class ServiceCollection:
    """
    Class with attributes for each service.
    """
    document_batch_service = DocumentBatchService()
    workflow_service = WorkflowService()
