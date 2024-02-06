package repositories

import (
	"recognition-service/database/model"

	"github.com/jmoiron/sqlx"
)

type WorkflowRepository struct{}

// Method for adding a new record into a workflow repository.
func (WorkflowRepository) AddWorkflow(tx *sqlx.Tx, isFullPageRecog, skipEnhancement, expectDiffImgs bool) error {
	//tx.NamedQuery(query.)
	workflow := model.NewWorkflow(isFullPageRecog, skipEnhancement, expectDiffImgs)
	return nil
}
