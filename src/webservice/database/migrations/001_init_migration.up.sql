BEGIN;

CREATE TABLE workflows (
    id UUID PRIMARY KEY,
    is_full_page_recognition BOOLEAN NOT NULL,
    skip_enhancement BOOLEAN NOT NULL,
    expect_diff_images BOOLEAN NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE TABLE document_batches (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state SMALLINT NOT NULL,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_date TIMESTAMP WITH TIME ZONE,
    workflow_id UUID NULL,
    author_id VARCHAR(255) NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL,
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL,
    CONSTRAINT fk_workflow
        FOREIGN KEY(workflow_id)
            REFERENCES workflows(id)
            ON DELETE CASCADE
);

CREATE TABLE processed_documents (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    content_type VARCHAR(255) NOT NULL,
    is_archived BOOLEAN NOT NULL,
    archive_key VARCHAR(255),
    date_archived TIMESTAMP WITH TIME ZONE,
    data BYTEA NULL,
    batch_id UUID NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL,
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL,
    CONSTRAINT fk_batch
        FOREIGN KEY(batch_id)
            REFERENCES document_batches(id)
            ON DELETE CASCADE
);

CREATE TABLE document_templates (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    width REAL NOT NULL,
    height REAL NOT NULL,
    image BYTEA NOT NULL,
    workflow_id UUID NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL,
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL,
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
    expected_value VARCHAR(255),
    is_identifying BOOLEAN NOT NULL,
    template_id UUID NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL,
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL,
    CONSTRAINT fk_template
        FOREIGN KEY(template_id)
            REFERENCES document_templates(id)
            ON DELETE CASCADE
);

CREATE TABLE field_values (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value VARCHAR(255) NOT NULL,
    document_id UUID NOT NULL,
    date_added TIMESTAMP WITH TIME ZONE NOT NULL,
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL,
    CONSTRAINT fk_document
        FOREIGN KEY(document_id)
            REFERENCES processed_documents(id)
            ON DELETE CASCADE
);

COMMIT;