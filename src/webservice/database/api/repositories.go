package api

import (
	"recognition-service/domain"

	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

// A repository for handling persistence of recognition application objects.
type IApplicationRepository interface {
	// Method for inserting a new recognition application into a database.
	AddApplication(tx *sqlx.Tx, appName, creatorId string) (uuid.UUID, error)

	// Method for retrieving recognition app's data from a database.
	GetApp(appId uuid.UUID) (domain.Application, error)

	// Get all recognition app's of a single user who is their author.
	GetApps(authorId string) ([]domain.Application, error)

	// Method for deleting a recognition application from a database.
	DeleteApplication(tx *sqlx.Tx, appId uuid.UUID) error
}
