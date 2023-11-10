"""
Module for a service class that handles logic connected to document templates.
"""
from internal.database import Session
from internal.transport.model import contracts


class TemplateService:
    """
    A service class that handles document templates.
    """

    @staticmethod
    def create_new_template(data: contracts.CreateTemplateModel):
        """
        Method for creating a new document template in the system.
        """
        session = Session()
        session.commit()
