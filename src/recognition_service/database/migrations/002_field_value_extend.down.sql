BEGIN;
ALTER TABLE recognition_results
    ALTER COLUMN value TYPE varchar(255);
COMMIT;