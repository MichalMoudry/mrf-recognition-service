"""
Module containing a collection of all services.
"""
from typing import Optional
import psycopg

from service.user_service import UserService


class ServiceCollection:
    """
    A container class with attributes for each service.
    """
    def __init__(self, conn: Optional[psycopg.Connection]) -> None:
        if conn == None:
            ... # TODO: Add mock connection
        self._user_service = UserService()

    @property
    def user_service(self) -> UserService:
        """
        Property containing an instance of UserSerivce
        """
        return self._user_service
