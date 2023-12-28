package service

import "mime/multipart"

type DocProcessingService struct{}

// Method for full-page processing multiple images.
func (DocProcessingService) ProcessMultipleCompleteImgs(files []multipart.File) error {
	//TODO: Save batch without images
	//TODO: Spawn a corutine that runs OCR on the images
	return nil
}
