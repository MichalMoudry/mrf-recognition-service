package repositories

import (
	"recognition-service/database/query"
	"recognition-service/domain"

	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

type ApplicationRepository struct{}

// Method for inserting a new recognition application into a database.
func (ApplicationRepository) AddApplication(tx *sqlx.Tx, appName, creatorId string) (uuid.UUID, error) {
	app := domain.NewApplication(appName, creatorId)
	if _, err := tx.NamedQuery(query.CreateApp, app); err != nil {
		return uuid.Nil, err
	}
	return app.Id, nil
}

// Method for retrieving recognition app's data from a database.
func (ApplicationRepository) GetApp(appId uuid.UUID) (domain.Application, error) {
	var appData domain.Application
	return appData, nil
}

// Get all recognition app's of a single user who is their author.
func (ApplicationRepository) GetApps(authorId string) ([]domain.Application, error) {
	return nil, nil
}

// Method for deleting a recognition application from a database.
func (ApplicationRepository) DeleteApplication(tx *sqlx.Tx, appId uuid.UUID) error {
	if _, err := tx.Exec(query.DeleteApp, appId); err != nil {
		return err
	}
	return nil
}
