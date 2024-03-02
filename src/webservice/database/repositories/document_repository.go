package repositories

import (
	"recognition-service/database/query"
	"recognition-service/domain"
	"time"

	"github.com/jmoiron/sqlx"
)

type DocumentRepository struct{}

// Method for inserting basic data about a document batch into a database.
func (DocumentRepository) AddBatchHeader(tx *sqlx.Tx, batch domain.DocumentBatch) error {
	_, err := tx.NamedQuery(query.CreateBatch, batch)
	return err
}

// Method for obtaining information about a document batch from a database.
func (DocumentRepository) GetBatchInfo() {

}

// Method for updating an existing document batch with information about its completion.
func (DocumentRepository) UpdateBatch(tx *sqlx.Tx, completionDate time.Time, state domain.BatchState) error {

	return nil
}

// Method for deleting a batch from a database.
func (DocumentRepository) DeleteBatch(tx *sqlx.Tx) error {
	return nil
}

// Method for bulk insert of processed documents into a database.
func (DocumentRepository) AddProcessedDocs(tx *sqlx.Tx) error {
	return nil
}

// Method for obtaining information about processed documents from a database.
func (DocumentRepository) GetProcessedDocsInfo() {

}

// Method for obtaining information about a specific processed document from a database.
func (DocumentRepository) GetProcessedDocInfo() {

}

// Method for archiving specific processed documents.
func (DocumentRepository) ArchiveProcessedDocs(tx *sqlx.Tx) error {
	return nil
}
