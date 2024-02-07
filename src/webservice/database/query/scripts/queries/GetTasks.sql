SELECT
    t.id,
    t.task_name,
    t.content,
    t.description,
    t.group_id,
    t.concurrency_stamp,
    t.date_added,
    t.date_updated
FROM
    workflow_tasks as t
WHERE
    t.group_id = $1