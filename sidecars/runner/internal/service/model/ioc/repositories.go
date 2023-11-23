package ioc

import (
	"job-runner/internal/database/model"

	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

type IProcessedDocumentRepository interface {
	// Method for obtaining an array of unprocessed documents.
	GetUnprocessedDocuments(ctx *sqlx.Tx) ([]model.ProcessedDocument, error)

	// Method for updating a unprocessed document.
	UpdateUnprocessedDocument(ctx *sqlx.Tx, docId uuid.UUID) error
}
