package repositories

import "github.com/jmoiron/sqlx"

type WorkflowRepository struct{}

// Method for adding a new record into a workflow repository.
func (WorkflowRepository) AddWorkflow(tx *sqlx.Tx, isFullPageRecog, expectDiffImgs, SkipEnhancement bool) error {

	return nil
}
