package database

import (
	"context"
	"errors"
	db_errors "job-runner/internal/database/errors"

	"github.com/jmoiron/sqlx"
)

// A structure representing a manager for dealing with DB transaction.
type TransactionManager struct{}

// This function starts a database transaction.
func (TransactionManager) BeginTransaction(ctx context.Context) (*sqlx.Tx, error) {
	dbCtx, err := GetDbContext()
	if err != nil {
		return nil, err
	}
	return dbCtx.BeginTxx(ctx, nil)
}

// This function ends a specific database transaction.
func (TransactionManager) EndTransaction(transaction *sqlx.Tx, err error) error {
	if err != nil {
		if transaction == nil {
			return db_errors.ErrNilTransaction
		}
		if rollbackErr := transaction.Rollback(); rollbackErr != nil {
			err = errors.Join(rollbackErr, err)
		}
	}

	if commitErr := transaction.Commit(); commitErr != nil {
		err = errors.Join(commitErr, err)
	}
	return err
}
