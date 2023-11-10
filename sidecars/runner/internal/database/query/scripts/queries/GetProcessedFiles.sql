SELECT
    d.id,
    d.content_type,
    d.is_archived,
    d.data
FROM
    recognition.processed_documents as d
WHERE
    d.is_archived is FALSE AND d.data is not null
ORDER BY d.date_added DESC