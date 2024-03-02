UPDATE
    document_batches
SET
    state = $2,
    completed_date = $3
WHERE
    id = $1