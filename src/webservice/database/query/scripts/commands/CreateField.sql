INSERT INTO template_fields (
    id,
    field_name,
    width,
    height,
    x_position,
    y_position,
    expected_value,
    is_identifying,
    template_id,
    concurrency_stamp,
    date_added,
    date_updated
)
VALUES (
    :id,
    :field_name,
    :width,
    :height,
    :x_position,
    :y_position,
    :expected_value,
    :is_identifying,
    :template_id,
    :concurrency_stamp,
    :date_added,
    :date_updated
)