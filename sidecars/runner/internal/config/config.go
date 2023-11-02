package config

import (
	"os"

	"github.com/spf13/viper"
)

type Config struct {
	ConnectionString string
	BlobStorageUrl   string
	Environment
}

// This function reads app's configuration from a config file.
func ReadCfgFromFile(path string) (Config, error) {
	viper.SetConfigFile(path)
	if err := viper.ReadInConfig(); err != nil {
		return Config{}, err
	}

	connectionString := os.Getenv("DB_CONN")
	if connectionString == "" {
		connectionString = viper.GetString("connection_string")
	}

	blobStorageUrl := viper.GetString("blob_storage_url")
	if blobStorageUrl == "" {
		blobStorageUrl = os.Getenv("BLOB_STORAGE_URL")
	}

	return Config{
		ConnectionString: connectionString,
		BlobStorageUrl:   blobStorageUrl,
		Environment:      Environment(viper.GetString("environment")),
	}, nil
}
