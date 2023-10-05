"""
Module with tests related to database models.
"""
from src.internal.database import model


def test_processed_document_constructor():
    entity = model.new_processsed_document()
    assert entity.id is not None
