package config

import (
	"os"

	"github.com/spf13/viper"
)

type Config struct {
	ConnectionString string
	BlobStorageUrl   string
	MsEntraId        string
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

	msEntraId := viper.GetString("ms_entra_id")
	if msEntraId == "" {
		msEntraId = os.Getenv("MS_ENTRA_ID")
	}

	return Config{
		ConnectionString: connectionString,
		BlobStorageUrl:   blobStorageUrl,
		MsEntraId:        msEntraId,
		Environment:      Environment(viper.GetString("environment")),
	}, nil
}
