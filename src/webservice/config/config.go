package config

import "github.com/spf13/viper"

// A structure encapsulating service's configuration.
type Config struct {
	Port            int
	DbConnectionStr string
	Environment
}

// This function reads app's configuration from a config file.
func ReadFromConfigFile(path string) (Config, error) {
	viper.SetConfigFile(path)
	if err := viper.ReadInConfig(); err != nil {
		return Config{}, err
	}
	return Config{
		Port:            viper.GetInt("port"),
		DbConnectionStr: viper.GetString("db_connection_string"),
		Environment:     Environment(viper.GetString("environment")),
	}, nil
}
