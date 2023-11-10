package query

import _ "embed"

var (
	//go:embed scripts/queries/GetProcessedFiles.sql
	GetProcessedFiles string
)
