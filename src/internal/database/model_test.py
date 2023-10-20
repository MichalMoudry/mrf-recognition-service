"""
Module with tests related to database models.
"""
from uuid import uuid4
from .model import new_processsed_document


def test_processed_document_constructor():
    """
    A test case for a basic ProcessedDocument entity creation.
    """
    entity = new_processsed_document(
        "test_document_1",
        "image/jpg",
        bytes(),
        uuid4()
    )
    assert entity.id is not None
    assert entity.date_added == entity.date_updated
    assert entity.is_archived is False
    assert entity.content_type == "image/jpg"
    assert entity.archive_key is None
    assert entity.date_archived is None
    assert entity.data is not None
