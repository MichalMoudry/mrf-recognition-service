SELECT
    b.id,
    b.name,
    b.state,
    b.start_date,
    b.completed_date,
    b.workflow_id,
    b.author_id,
    b.date_added
FROM
    document_batches as b
WHERE
    b.id = $1