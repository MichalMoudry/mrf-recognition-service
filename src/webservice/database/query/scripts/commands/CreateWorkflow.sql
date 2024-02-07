INSERT INTO workflows (
    id,
    workflow_name,
    application_id,
    setting_is_full_page_recog,
    setting_skip_enhancement,
    setting_expect_diff_images,
    concurrency_stamp,
    date_added,
    date_updated
)
VALUES (
    :id,
    :workflow_name,
    :application_id,
    :setting_is_full_page_recog,
    :setting_skip_enhancement,
    :setting_expect_diff_images,
    :concurrency_stamp,
    :date_added,
    :date_updated
)