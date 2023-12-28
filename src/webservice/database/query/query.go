package query

import _ "embed"

var (
	//go:embed scripts/queries/SelectBatch.sql
	SelectBatch string
)
