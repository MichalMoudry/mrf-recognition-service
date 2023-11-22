package query

import _ "embed"

var (
	//go:embed scripts/commands/UpdateProcessedFile.sql
	UpdateProcessedFile string

	//go:embed scripts/queries/GetProcessedFiles.sql
	GetProcessedFiles string
)
