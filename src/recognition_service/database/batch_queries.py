"""
Module containing commands/queries for the document batch entity.
"""
from typing import LiteralString


insert_batch: LiteralString = """
INSERT INTO
    document_batches
VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

select_batch: LiteralString = """
SELECT
    b.id,
    b.name,
    b.start_date,
    b.completed_date,
    b.state
FROM
    document_batches as b
WHERE
    b.id = %s
"""

select_batches: LiteralString = """
SELECT
    b.id,
    b.name,
    b.start_date,
    b.completed_date,
    b.state
FROM
    document_batches as b
WHERE
    b.workflow_id == %s
ORDER BY
    b.start_date
"""
