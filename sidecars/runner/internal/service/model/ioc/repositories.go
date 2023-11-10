package ioc

import (
	"job-runner/internal/database/model"
)

type IProcessedDocumentRepository interface {
	// Method for obtaining an array of unprocessed documents.
	GetUnprocessedDocuments() ([]model.ProcessedDocument, error)
}
