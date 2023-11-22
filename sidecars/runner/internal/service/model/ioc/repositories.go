package ioc

import (
	"job-runner/internal/database/model"

	"github.com/jmoiron/sqlx"
)

type IProcessedDocumentRepository interface {
	// Method for obtaining an array of unprocessed documents.
	GetUnprocessedDocuments(ctx *sqlx.Tx) ([]model.ProcessedDocument, error)
}
