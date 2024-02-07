UPDATE
    applications
SET
    app_name = $2,
    date_updated = $3,
    concurrency_stamp = $4
WHERE
    id = $1