BEGIN;

ALTER TABLE recognition.field_values
    ALTER COLUMN value TYPE varchar(1024);

COMMIT;