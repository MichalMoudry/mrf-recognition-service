package config

type Environment string

const (
	DEV  Environment = "dev"
	TEST Environment = "test"
	PROD Environment = "prod"
)

// Function for checking if environment is set as development.
func (env Environment) IsDevelopment() bool {
	return env == DEV
}

// Function for checking if environment is set as a testing environment.
func (env Environment) IsTest() bool {
	return env == TEST
}

// Function for checking if environemtn is set as a production environment.
func (env Environment) IsProduction() bool {
	return env == PROD
}
