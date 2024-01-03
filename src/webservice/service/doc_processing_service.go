package service

import (
	"bytes"
	"context"
	"io"
	"mime/multipart"
	"recognition-service/service/model/ioc"

	"github.com/jackc/pgx/v5/pgxpool"
)

// A service for handling of imported documents.
type DocProcessingService struct {
	RecogService ioc.IRecognitionService
	db           *pgxpool.Pool
}

func NewDocProcessingSrvc(dbPool *pgxpool.Pool) DocProcessingService {
	return DocProcessingService{
		db: dbPool,
	}
}

// Method for full-page processing multiple images.
func (srvc DocProcessingService) ProcessMultipleCompleteImgs(ctx context.Context, files []multipart.File) error {
	_, err := srvc.db.Begin(ctx)
	if err != nil {
		return err
	}
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
