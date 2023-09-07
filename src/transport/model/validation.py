"""
Package for assisting with model validation.
"""
from uuid import UUID

SUPPORTED_FILE_TYPES = [".pdf", ".png", ".jpg"]

def is_string_valid_uuid(inpt: str) -> UUID | None:
    """
    A function for validating if a string is a valid UUID or not.
    """
    try:
        return UUID(inpt)
    except ValueError:
        return None
