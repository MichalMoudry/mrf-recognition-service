package transformers

import (
	"recognition-service/service/model/dto"
	"strings"

	"github.com/otiai10/gosseract/v2"
)

// A filter for recognizing incoming documents.
func Recognizer(producer <-chan dto.ProcessedDocumentInfo) <-chan dto.ProcessedDocumentInfo {
	out := make(chan dto.ProcessedDocumentInfo)
	go func() {
		tesseract := gosseract.NewClient()
		defer tesseract.Close()

		for dto := range producer {
			if !dto.WasSuccess() {
				continue
			}
			err := tesseract.SetImageFromBytes(dto.ContentBuffer.Bytes())
			if err != nil {
				dto.Error = err
				continue
			}

			res, err := tesseract.Text()
			if err != nil {
				dto.Error = err
				continue
			}
			dto.Results = strings.Split(res, "\n")
			out <- dto
		}
		close(out)
	}()
	return out
}
