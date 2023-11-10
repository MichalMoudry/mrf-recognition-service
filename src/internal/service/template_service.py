"""
Module for a service class that handles logic connected to document templates.
"""
from internal.database import Session
from internal.database.model import new_template
from internal.transport.model import contracts
from quart.datastructures import FileStorage


class TemplateService:
    """
    A service class that handles document templates.
    """

    @staticmethod
    def create_new_template(data: contracts.CreateTemplateModel, image: FileStorage):
        """
        Method for creating a new document template in the system.
        """
        session = Session()
        template = new_template(
            data.template_name,
            data.width,
            data.height,
            image.stream.read(),
            data.workflow_id
        )
        session.add(template)
        session.commit()
