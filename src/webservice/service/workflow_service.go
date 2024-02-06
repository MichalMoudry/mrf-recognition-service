package service

import (
	"context"

	"github.com/jmoiron/sqlx"
)

type WorkflowService struct {
	db *sqlx.DB
}

// A constructor function for the WorkflowService structure.
func NewWorkflowService(db *sqlx.DB) *WorkflowService {
	return &WorkflowService{
		db: db,
	}
}

// Function for adding an existing workflow to the system.
func (srvc WorkflowService) AddExistingWorkflow(ctx context.Context, data interface{}) error {
	_, err := srvc.db.BeginTxx(ctx, nil)
	if err != nil {
		return err
	}
	return nil
}
