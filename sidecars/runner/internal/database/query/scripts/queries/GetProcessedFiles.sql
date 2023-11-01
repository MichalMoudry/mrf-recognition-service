SELECT
    d.id,
FROM
    recognition.processed_documents as d
WHERE
    d.is_archived is FALSE
ORDER BY d.date_added DESC