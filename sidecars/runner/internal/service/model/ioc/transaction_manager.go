package ioc

import (
	"context"

	"github.com/jmoiron/sqlx"
)

// An interface for a database transaction manager.
type ITransactionManager interface {
	// This function starts a database transaction.
	BeginTransaction(ctx context.Context) (*sqlx.Tx, error)

	// This function ends a specific database transaction.
	EndTransaction(transaction *sqlx.Tx, err error) error
}
