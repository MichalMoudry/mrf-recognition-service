"""
Module with unit tests related to service layer DTOs.
"""
from datetime import datetime
import json
from uuid import uuid4
from .dto import BatchStatistic, ProcessedDocumentDto


def test_batch_stat_serialization():
    """
    A test covering serialization of a DTO used for publishing batch statistics.
    """
    dto = BatchStatistic(
        uuid4(),
        datetime.utcnow(),
        datetime.utcnow(),
        5,
        1,
        uuid4()
    )
    json_str = json.dumps(dto.serialize())
    assert len(json_str) > 0


def test_processed_document_serialization():
    """
    A test covering serialization of a DTO used as a response pro processed documents
    """
    dto = ProcessedDocumentDto(
        uuid4(),
        "test_document",
        "",
        "jpg",
        None,
        False
    )
    res = True
    try:
        json_str = json.dumps(dto.serialize())
        assert len(json_str) > 0
    except Exception as err:
        res = False
        print(err)
    assert res is True
