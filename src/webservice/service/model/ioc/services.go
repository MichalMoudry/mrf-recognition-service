package ioc

import "recognition-service/service/model/dto"

// An interface for a recognition service.
type IRecognitionService interface {
	// Method for a full-page recognition of multiple images.
	RecognizeEntireImages(docs []dto.ProcessedDocumentInfo) error
}
