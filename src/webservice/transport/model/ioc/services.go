package ioc

import (
	"context"
	"recognition-service/transport/model"
)

// A service for handling of imported documents.
type IDocProcessingService interface {
	// Method for full-page processing multiple images.
	ProcessMultipleImgs(ctx context.Context, files []model.IncomingFile) error
}
