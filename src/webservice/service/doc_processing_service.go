package service

import (
	"bytes"
	"io"
	"log"
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
	images := make([][]byte, len(files))

	var buf *bytes.Buffer
	for i, file := range files {
		buf = bytes.NewBuffer(nil)
		if _, err := io.Copy(buf, file); err != nil {
			file.Close()
			continue
		}
		images[i] = buf.Bytes()
	}
	res, err := srvc.RecogService.RecognizeEntireImages(images)
	if err != nil {
		log.Printf("Recognition failed because: %v\n", err)
		return
	}
	for _, v := range res {
		log.Println(v.Name, v.Results, v.WasSuccess)
	}
}
