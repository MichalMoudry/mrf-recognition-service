"""
A module with database model classes.
"""
from uuid import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Entity(DeclarativeBase):
    """
    A base class for database entities.
    """
    id: Mapped[UUID] = mapped_column(primary_key=True)
