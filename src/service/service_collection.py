"""
Module containing a collection of all services.
"""
from typing import Optional
import psycopg


class ServiceCollection:
    """
    A container class with attributes for each service.
    """
    def __init__(self, conn: Optional[psycopg.Connection]) -> None:
        pass
