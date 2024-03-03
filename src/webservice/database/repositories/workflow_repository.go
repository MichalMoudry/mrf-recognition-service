package repositories

import (
	"recognition-service/database/query"
	"recognition-service/domain"
	"time"

	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

type WorkflowRepository struct{}

// Method for adding a new record into a workflow repository.
func (WorkflowRepository) AddWorkflow(tx *sqlx.Tx, name string, appId uuid.UUID, isFullPageRecog, skipEnhancement, expectDiffImgs bool) error {
	//tx.NamedQuery(query.)
	workflow := domain.NewWorkflow(name, appId, isFullPageRecog, skipEnhancement, expectDiffImgs)
	if _, err := tx.NamedQuery(query.CreateWorkflow, workflow); err != nil {
		return err
	}
	return nil
}

// Method for obtaining a single workflow from a database.
func (WorkflowRepository) GetWorkflow(tx *sqlx.Tx, workflowId uuid.UUID) (domain.Workflow, error) {
	var workflow domain.Workflow
	err := tx.Select(&workflow, query.GetWorkflow, workflowId)
	if err != nil {
		return domain.Workflow{}, err
	}
	return workflow, nil
}

func (WorkflowRepository) GetWorkflows() error {
	return nil
}

// Method for updating a specific workflow in the database.
func (WorkflowRepository) UpdateWorkflow(tx *sqlx.Tx, workflowId uuid.UUID, name string, settings domain.WorkflowSetting) error {
	_, err := tx.Exec(
		query.UpdateWorkflow,
		workflowId,
		name,
		settings.IsFullPageRecognition,
		settings.SkipImageEnhancement,
		settings.ExpectDifferentImages,
		uuid.New(),
		time.Now(),
	)
	return err
}

// Method for deleting a specific workflow in the database.
func (WorkflowRepository) DeleteWorkflow(tx *sqlx.Tx, workflowId uuid.UUID) error {
	if _, err := tx.Exec(query.DeleteWorkflow, workflowId); err != nil {
		return err
	}
	return nil
}
