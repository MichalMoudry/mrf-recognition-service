BEGIN;

ALTER TABLE recognition.field_values ALTER COLUMN value VARCHAR(1024) NOT NULL;

COMMIT;