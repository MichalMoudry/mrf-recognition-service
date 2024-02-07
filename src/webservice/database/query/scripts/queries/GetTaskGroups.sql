SELECT
    tg.id,
    tg.group_name,
    tg.concurrency_stamp,
    tg.date_added,
    tg.date_updated
FROM
    workflow_task_groups as tg
WHERE
    tg.workflow_id = $1