package database

import (
	"job-runner/internal/database/errors"
	"log"

	_ "github.com/jackc/pgx/v5/stdlib"
	"github.com/jmoiron/sqlx"
)

var dbContext *sqlx.DB

// Function for opening a connection to a database.
func OpenDb(connectionString string) error {
	db, connectionErr := sqlx.Open("pgx", connectionString)
	if connectionErr != nil {
		log.Fatal(connectionErr)
	}
	dbContext = db
	return nil
}

// Function for obtaining a context for database operations.
func GetDbContext() (*sqlx.DB, error) {
	if dbContext == nil {
		return nil, errors.ErrDbContextNotInitialized
	}
	return dbContext, nil
}
