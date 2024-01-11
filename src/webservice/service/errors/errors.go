package errors

import "errors"

var (
	ErrDaprIsNotInitialized = errors.New("dapr client has not been initialized")
)
