"""
Package with DTOs for the transport layer.
"""
from dataclasses import dataclass


@dataclass
class DocumentDto:
    """
    A DTO representing data from a client about a document.
    """
    name: str
    content: bytes
    content_type: str
