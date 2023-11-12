"""
Module containing a collection of all services.
"""
from internal.service.template_service import TemplateService
from internal.service.doc_batch_service import DocumentBatchService
from internal.service.workflow_service import WorkflowService
from internal.service.user_service import UserService
from internal.service.processing_service import ProcessingService


class ServiceCollection:
    """
    Class with attributes for each service.
    """

    def __init__(self) -> None:
        self._doc_batch_service = DocumentBatchService
        self._workflow_service = WorkflowService()
        self._user_service = UserService()
        self._file_processing_service = ProcessingService()
        self._template_service = TemplateService

    @property
    def document_batch_service(self) -> type[DocumentBatchService]:
        return self._doc_batch_service

    @property
    def workflow_service(self) -> WorkflowService:
        return self._workflow_service

    @property
    def user_service(self) -> UserService:
        """
        Property containing an instance of UserSerivce
        """
        return self._user_service

    @property
    def fp_service(self) -> ProcessingService:
        """
        Property containing an instance of FileProcessingService.
        """
        return self._file_processing_service


    @property
    def template_service(self) -> type[TemplateService]:
        """
        Service class for handling document template operations.
        """
        return self._template_service
