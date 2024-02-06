package service

import (
	"context"
	"recognition-service/service/model/ioc"
	"recognition-service/service/pipelines/consumers"
	"recognition-service/service/pipelines/producers"
	"recognition-service/service/pipelines/transformers"
	"recognition-service/transport/model"

	"github.com/jmoiron/sqlx"
)

// A service for handling of imported documents.
type DocProcessingService struct {
	RecogService ioc.IRecognitionService
	db           *sqlx.DB
}

func NewDocProcessingSrvc(dbPool *sqlx.DB) DocProcessingService {
	return DocProcessingService{
		db: dbPool,
	}
}

// Method for processing multiple images.
func (srvc DocProcessingService) ProcessMultipleImgs(ctx context.Context, files []model.IncomingFile) error {
	_, err := srvc.db.BeginTxx(ctx, nil)
	if err != nil {
		return err
	}
	//TODO: Save batch without images
	//TODO: Spawn a corutine that runs OCR on the images
	go srvc.processImages(files)
	return nil
}

// A corutine for running OCR on multiple images.
func (srvc DocProcessingService) processImages(files []model.IncomingFile) {
	consumers.RecognitionConsumer(
		transformers.Recognizer(
			transformers.MultipartFileTransformer(
				producers.ImageBufferProducer(files),
			),
		),
	)
}
