package query

import _ "embed"

var (
	//go:embed scripts/commands/CreateApp.sql
	CreateApp string
	//go:embed scripts/commands/DeleteApp.sql
	DeleteApp string
	//go:embed scripts/commands/DeleteUsersApps.sql
	DeleteUsersApps string
	//go:embed scripts/commands/UpdateApp.sql
	UpdateApp string
	//go:embed scripts/commands/CreateWorkflow.sql
	CreateWorkflow string
	//go:embed scripts/commands/UpdateWorkflow.sql
	UpdateWorkflow string
	//go:embed scripts/commands/DeleteWorkflow.sql
	DeleteWorkflow string
	//go:embed scripts/commands/CreateField.sql
	CreateField string
	//go:embed scripts/commands/CreateBatch.sql
	CreateBatch string
	//go:embed scripts/commands/UpdateBatch.sql
	UpdateBatch string

	//go:embed scripts/queries/GetApp.sql
	GetApp string
	//go:embed scripts/queries/GetApps.sql
	GetApps string
	//go:embed scripts/queries/GetWorkflow.sql
	GetWorkflow string
	//go:embed scripts/queries/GetWorkflows.sql
	GetWorkflows string
	//go:embed scripts/queries/GetTaskGroups.sql
	GetTaskGroups string
	//go:embed scripts/queries/GetTasks.sql
	GetTasks string
	//go:embed scripts/queries/GetBatch.sql
	GetBatch string
)
