package service

import (
	"context"
	"mime/multipart"
	"recognition-service/service/model/ioc"
	"recognition-service/service/pipelines/consumers"
	"recognition-service/service/pipelines/producers"
	"recognition-service/service/pipelines/transformers"

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
	results := consumers.RecognitionConsumer(
		transformers.Recognizer(
			transformers.MultipartFileTransformer(
				producers.ImageBufferProducer(files...),
			),
		),
	)
}
