package service

import (
	"job-runner/internal/database"
	"job-runner/internal/database/repositories"
)

// A structure representing a collection of public services in the service layer.
type ServiceCollection struct {
	JobService *JobService
}

// A constructor function for ServiceCollection structure.
func NewServiceCollection() *ServiceCollection {
	txManager := &database.TransactionManager{}
	return &ServiceCollection{
		JobService: NewJobService(txManager, repositories.ProcessedDocumentRepository{}),
	}
}
