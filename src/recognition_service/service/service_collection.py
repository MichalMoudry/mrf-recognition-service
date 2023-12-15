"""
Module containing a collection of all services.
"""
from service.user_service import UserService


class ServiceCollection:
    """
    A container class with attributes for each service.
    """
    def __init__(self) -> None:
        self._user_service = UserService()

    @property
    def user_service(self) -> UserService:
        """
        Property containing an instance of UserSerivce
        """
        return self._user_service
