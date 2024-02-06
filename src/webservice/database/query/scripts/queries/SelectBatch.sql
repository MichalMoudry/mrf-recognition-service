SELECT
    b.id,
    b.name,
    b.start_date,
    b.completed_date,
    b.state
FROM
    document_batches as b
WHERE
    b.id = $1