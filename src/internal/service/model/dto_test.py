"""
Module with unit tests related to service layer DTOs.
"""
from datetime import datetime
import json
from uuid import uuid4
from .dto import BatchStatistic


def test_batch_stat_serialization():
    """
    A test covering serialization of a DTO used for publishing batch statistics.
    """
    dto = BatchStatistic(
        uuid4(),
        datetime.utcnow(),
        datetime.utcnow(),
        5,
        1
    )
    json_str = json.dumps(dto.serialize())
    assert len(json_str) > 0
