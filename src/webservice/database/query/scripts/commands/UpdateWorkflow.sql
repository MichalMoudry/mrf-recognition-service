UPDATE
    workflows
SET
    workflow_name = $2,
    setting_is_full_page_recog = $3,
    setting_skip_enhancement = $4,
    setting_expect_diff_images = $5,
    concurrency_stamp = $6,
    date_updated = $7
WHERE
    id = $1