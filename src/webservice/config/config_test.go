package config

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

const configPath string = "../config.toml"

func Test_ReadConfigFromFile(t *testing.T) {
	type args struct {
		path string
	}
	tests := []struct {
		name    string
		args    args
		want    Config
		wantErr bool
	}{
		{
			name: "Correct config path",
			args: args{
				path: configPath,
			},
			want: Config{
				Port:            8080,
				DbConnectionStr: "postgres://root:root@localhost:5432/recognition-db?sslmode=disable",
				Environment:     DEV,
			},
			wantErr: false,
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got, err := ReadFromConfigFile(test.args.path)
			if (err != nil) != test.wantErr {
				t.Errorf("ReadConfigFromFile() error = %v, wantErr %v", err, test.wantErr)
			}
			assert.Equal(t, test.want, got)
		})
	}
}
