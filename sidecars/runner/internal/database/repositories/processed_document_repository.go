package repositories

import (
	"job-runner/internal/database/model"
	"job-runner/internal/database/query"
	"time"

	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

type ProcessedDocumentRepository struct{}

// Method for obtaining an array of unprocessed documents.
func (ProcessedDocumentRepository) GetUnprocessedDocuments(ctx *sqlx.Tx) ([]model.ProcessedDocument, error) {
	var data []model.ProcessedDocument
	if err := ctx.Select(&data, query.GetProcessedFiles); err != nil {
		return nil, err
	}
	return data, nil
}

// Method for updating a unprocessed document.
func (ProcessedDocumentRepository) UpdateUnprocessedDocument(ctx *sqlx.Tx, docId uuid.UUID) error {
	if _, err := ctx.Exec(query.UpdateProcessedFile, docId, time.Now()); err != nil {
		return err
	}
	return nil
}
