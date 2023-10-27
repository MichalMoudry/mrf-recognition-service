"""
Module with tests related to database models.
"""
from uuid import uuid4
from .model import BatchState, new_processsed_document, new_document_batch


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


def test_document_batch():
    """
    Test covering contructor function for the document batch entity.
    """
    batch = new_document_batch("test_batch", "test_author", uuid4(), [])
    assert batch.state == BatchState.PROCESSING.value
