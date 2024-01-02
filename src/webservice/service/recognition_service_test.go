package service

import (
	"bytes"
	"log"
	"os"
	"recognition-service/service/model/dto"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_RecognizeEntireImages(t *testing.T) {
	const testFolderPrefix string = "../../../tests/test_images/"
	type args struct {
		imagePaths []string
	}

	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{
			name: "Test basic image recognition",
			args: args{
				imagePaths: []string{
					testFolderPrefix + "repo_screenshot_2.jpg",
					testFolderPrefix + "repo_screenshot.png",
				},
			},
			wantErr: false,
		},
	}

	recogService := RecognitionService{}
	os.Setenv("LIBRARY_PATH", "/opt/homebrew/lib")
	os.Setenv("CPATH", "/opt/homebrew/include")
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			docs := make([]dto.ProcessedDocumentInfo, len(test.args.imagePaths))

			for i, path := range test.args.imagePaths {
				data, err := os.ReadFile(path)
				assert.Equal(t, test.wantErr, err != nil, err)
				docs[i].ContentBuffer = bytes.NewBuffer(data)
			}
			recogService.RecognizeEntireImages(docs)
			for _, v := range docs {
				log.Println(v.Name, v.Results, v.WasSuccess)
			}
		})
	}
}
