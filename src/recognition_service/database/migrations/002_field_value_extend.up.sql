BEGIN;
ALTER TABLE recognition_results
    ALTER COLUMN value TYPE varchar(1024);
COMMIT;