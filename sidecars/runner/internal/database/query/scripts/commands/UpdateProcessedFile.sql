UPDATE
    recognition.processed_documents as d
SET
    d.is_archived = TRUE,
    d.data = NULL,
    d.date_archived = $2
WHERE
    d.id = $1