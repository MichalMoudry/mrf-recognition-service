package transformers

import (
	"recognition-service/service/model/dto"
)

// A filter for recognizing incoming documents.
func Recognizer(producer <-chan dto.ProcessedDocumentInfo) <-chan dto.ProcessedDocumentInfo {
	out := make(chan dto.ProcessedDocumentInfo)
	go func() {
		/*tesseract := gosseract.Cli
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
		}*/
		out <- dto.ProcessedDocumentInfo{
			Name:    "Test doc",
			Results: []string{"Test val 1", "Test val 2"},
		}
		close(out)
	}()
	return out
}
