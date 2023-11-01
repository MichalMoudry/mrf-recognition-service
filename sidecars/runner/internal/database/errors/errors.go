package errors

import "errors"

var (
	ErrDbContextNotInitialized = errors.New("database context was not initialized")
	ErrQueryFailed             = errors.New("system was unable to complete query")
)
