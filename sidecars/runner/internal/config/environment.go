package config

type Environment string

const (
	DEV  Environment = "[dev]"
	PROD Environment = "[prod]"
)

// Method for checking if an environment value is DEV or not.
func (env Environment) IsDev() bool {
	return env == DEV
}

// Method for checking if an environment value is PROD or not.
func (env Environment) IsProd() bool {
	return env == PROD
}
