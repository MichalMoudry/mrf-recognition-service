package util

import (
	"fmt"
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
					SkipImageEnhancement:  "true",
					ExpectDifferentImages: "false",
				},
			},
			wantErr: false,
		},
		{
			name: "Test incorrect CreateWorkflowRequest with capital letters",
			args: args{
				payload: contracts.CreateWorkflowRequest{
					IsFullPageRecognition: "True",
					SkipImageEnhancement:  "True",
					ExpectDifferentImages: "False",
				},
			},
			wantErr: false,
		},
		{
			name: "Test empty CreateWorkflowRequest",
			args: args{
				payload: contracts.CreateWorkflowRequest{},
			},
			wantErr: true,
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			err := validate.Struct(test.args.payload)
			isError := err != nil
			if isError != test.wantErr {
				fmt.Println(test.name)
			}
			assert.Equal(t, isError, test.wantErr)
		})
	}
}
