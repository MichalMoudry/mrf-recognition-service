package service

import (
	"recognition-service/service/model/dto"
	"strings"

	"github.com/otiai10/gosseract/v2"
)

// A service for running OCR on images.
type RecognitionService struct{}

// Method for a full-page recognition of multiple images.
func (RecognitionService) RecognizeEntireImages(docs []dto.ProcessedDocumentInfo) error {
	tesseract := gosseract.NewClient()
	defer tesseract.Close()

	for i, doc := range docs {
		if err := tesseract.SetImageFromBytes(doc.ContentBuffer.Bytes()); err != nil {
			return err
		}

		res, err := tesseract.Text()
		if err != nil {
			return err
		}
		docs[i].Results = strings.Split(res, "\n")
		docs[i].WasSuccess = true
	}
	return nil
}
