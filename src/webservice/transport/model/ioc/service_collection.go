package ioc

import (
	"recognition-service/service"

	"github.com/jmoiron/sqlx"
)

// A container structure for all services inside a service layer.
type ServiceCollection struct {
	DocumentProcessingService IDocProcessingService
}

// A constructor function for a ServiceCollection structure.
func NewServiceCollection(db *sqlx.DB) *ServiceCollection {
	return &ServiceCollection{
		DocumentProcessingService: service.NewDocProcessingSrvc(db),
	}
}
