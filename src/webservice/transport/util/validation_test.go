package util

import (
	"recognition-service/transport/model/contracts"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_ContractValidation(t *testing.T) {
	type args struct {
		payload any
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{
			name: "Test correct CreateWorkflowRequest",
			args: args{
				payload: contracts.CreateWorkflowRequest{
					IsFullPageRecognition: "true",
					SkipImgEnhancement:    "true",
					ExpectDiffImages:      "false",
				},
			},
			wantErr: false,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			isError := validate.Struct(test.args.payload) != nil
			assert.Equal(t, isError, test.wantErr)
		})
	}
}
