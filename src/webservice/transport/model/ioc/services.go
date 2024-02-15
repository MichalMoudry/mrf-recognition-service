package ioc

import (
	"context"
	"recognition-service/transport/model"
	"recognition-service/transport/model/contracts"

	"github.com/google/uuid"
)

// A service for handling of imported documents.
type IDocProcessingService interface {
	// Method for full-page processing multiple images.
	ProcessMultipleImgs(ctx context.Context, files []model.IncomingFile) error
}

// A service responsible for handling operations related to recognition applications.
type IApplicationService interface {
	// A method for creating a new recognition app in the system.
	CreateApp(ctx context.Context) (uuid.UUID, error)

	// Method for obtaining information about a specific recognition app.
	GetAppInfo(ctx context.Context, appId uuid.UUID)

	// Method for obtaining information about user's recognition applications.
	GetAppInfos(ctx context.Context, userId string)

	// Method for deleting a specific recognition app in the system.
	DeleteApp(ctx context.Context, appId uuid.UUID) error

	// Method for updating/patching a specific recog app in the system.
	UpdateApp(ctx context.Context, appId uuid.UUID, newName string) error

	// Method for associating a user to a recognition app.
	ConnectUser(ctx context.Context, appId uuid.UUID, userId string) error

	// Method for disassociating a user from a recognition app.
	DisconnectUser(ctx context.Context, appId uuid.UUID, userId string) error
}

// A service responsible for operations related to workflows.
type IWorkflowService interface {
	// Method for creating a new workflow in the system.
	CreateWorkflow(ctx context.Context, request contracts.CreateWorkflowRequest) (uuid.UUID, error)

	// Method for obtaining information about a single workflow.
	GetWorkflowInfo(ctx context.Context, workflowId uuid.UUID)

	// Method for obtaining information about app's workflows.
	GetWorkflowsInfo(ctx context.Context, appId uuid.UUID)

	// Method for updating a specific workflow in the system.
	UpdateWorkflow(ctx context.Context, workflowId uuid.UUID, request contracts.UpdateWorkflowRequest) error

	// Method for removing an existing service from the system.
	DeleteWorkflow(ctx context.Context, workflowId uuid.UUID) error
}

// A service responsible for handling operations related to system's users.
type IUserService interface {
	// Method for deleting all user's data in the system.
	DeleteUsersData(ctx context.Context, userId string) error
}
