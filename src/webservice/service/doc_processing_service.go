package service

import (
	"bytes"
	"io"
	"mime/multipart"
	"recognition-service/service/model/ioc"
)

type DocProcessingService struct {
	RecogService ioc.IRecognitionService
}

// Method for full-page processing multiple images.
func (srvc DocProcessingService) ProcessMultipleCompleteImgs(files []multipart.File) error {
	//TODO: Save batch without images
	//TODO: Spawn a corutine that runs OCR on the images
	go srvc.processImages(files)
	return nil
}

// A corutine for running OCR on multiple images.
func (srvc DocProcessingService) processImages(files []multipart.File) {
	imgBuffers := make([]*bytes.Buffer, len(files))

	var buf *bytes.Buffer
	for i, file := range files {
		buf = bytes.NewBuffer(nil)
		if _, err := io.Copy(buf, file); err != nil {
			//file.Close()
			continue
		}
		imgBuffers[i] = buf
	}
}
