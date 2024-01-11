package ioc

import (
	"context"
	"recognition-service/service/model/dto"
)

// An interface for a recognition service.
type IRecognitionService interface {
	// Method for a full-page recognition of multiple images.
	RecognizeEntireImages(docs []dto.ProcessedDocumentInfo) error
}

// An interface for a Dapr service.
type IDaprService interface {
	// Method for publishing an event in the system.
	PublishEvent(ctx context.Context, topic string, data interface{}) error
}
