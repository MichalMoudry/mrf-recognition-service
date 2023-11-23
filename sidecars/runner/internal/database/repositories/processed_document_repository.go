package repositories

import (
	"job-runner/internal/database/model"
	"job-runner/internal/database/query"

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
