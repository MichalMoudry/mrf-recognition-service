BEGIN;

CREATE TABLE workflows (
    id UUID PRIMARY KEY,
    is_full_page_recognition BOOLEAN NOT NULL,
    skip_enhancement BOOLEAN NOT NULL,
    expect_diff_images BOOLEAN NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL
);

CREATE TABLE document_batches (
    id UUID PRIMARY KEY,
    name VARCAHR(255) NOT NULL,
    state SMALLINT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    completed_date TIMESTAMP NOT NULL,
    workflow_id UUID NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL,
    CONSTRAINT fk_workflow
        FOREIGN KEY(workflow_id)
            REFERENCES workflows(id)
            ON DELETE CASCADE
);

CREATE TABLE processed_documents (
    id UUID PRIMARY KEY,
    name VARCAHR(255) NOT NULL,
    content_type VARCAHR(255) NOT NULL,
    is_archived BOOLEAN NOT NULL,
    archive_key VARCAHR(255),
    date_archived TIMESTAMP,
    data BYTEA,
    batch_id UUID NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL,
    CONSTRAINT fk_batch
        FOREIGN KEY(batch_id)
            REFERENCES document_batches(id)
            ON DELETE CASCADE
);

CREATE TABLE document_templates (
    id UUID PRIMARY KEY,
    name VARCAHR(255) NOT NULL,
    width REAL NOT NULL,
    height REAL NOT NULL,
    image BYTEA NOT NULL,
    workflow_id UUID NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL,
    CONSTRAINT fk_workflow
        FOREIGN KEY(workflow_id)
            REFERENCES workflows(id)
            ON DELETE CASCADE
);

CREATE TABLE template_fields (
    id UUID PRIMARY KEY,
    width REAL NOT NULL,
    height REAL NOT NULL,
    x_position REAL NOT NULL,
    y_position REAL NOT NULL,
    expected_value VARCAHR(255),
    is_identifying BOOLEAN NOT NULL,
    template_id UUID NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL,
    CONSTRAINT fk_template
        FOREIGN KEY(template_id)
            REFERENCES document_templates(id)
            ON DELETE CASCADE
);

CREATE TABLE field_values (
    id UUID PRIMARY KEY,
    name VARCAHR(255) NOT NULL,
    value VARCAHR(255) NOT NULL,
    document_id UUID NOT NULL,
    date_added TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL
    CONSTRAINT fk_document
        FOREIGN KEY(document_id)
            REFERENCES processed_documents(id)
            ON DELETE CASCADE
);

COMMIT;