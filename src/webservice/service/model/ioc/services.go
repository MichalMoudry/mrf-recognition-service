package ioc

import "recognition-service/service/model/dto"

// An interface for a recognition service.
type IRecognitionService interface {
	RecognizeEntireImages(files [][]byte) ([]dto.ProcessedDocumentInfo, error)
}
