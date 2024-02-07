SELECT
    a.id,
    a.app_name,
    a.creator_id,
    a.concurrency_stamp,
    a.date_added,
    a.date_updated
FROM
    applications as a
WHERE
    a.creator_id = $1