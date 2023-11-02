package repositories

import (
	"job-runner/internal/database"
	"job-runner/internal/database/model"
	"job-runner/internal/database/query"
)

type ProcessedDocumentRepository struct{}

// Method for obtaining an array of unprocessed documents.
func (ProcessedDocumentRepository) GetUnprocessedDocuments() ([]model.ProcessedDocument, error) {
	ctx, err := database.GetDbContext()
	if err != nil {
		return nil, nil
	}

	var data []model.ProcessedDocument
	if err = ctx.Select(&data, query.GetProcessedFiles); err != nil {
		return nil, err
	}
	return data, nil
}
