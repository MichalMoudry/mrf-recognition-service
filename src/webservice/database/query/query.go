package query

import _ "embed"

var (
	//go:embed scripts/queries/SelectBatch.sql
	SelectBatch string

	//go:embed scripts/commands/InsertBatch.sql
	InsertBatch string
	//go:embed scripts/commands/InsertWorkflow.sql
	InsertWorkflow string
	//go:embed scripts/commands/InsertProcessedDocument.sql
	InsertProcessedDocument string
)
