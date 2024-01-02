package service

import (
	"log"
	"recognition-service/service/model/dto"

	"github.com/otiai10/gosseract/v2"
)

type RecognitionService struct{}

/*func (RecognitionService) RecognizeEntireImages(files []multipart.File) error {
	tesseract := gosseract.NewClient()
	defer tesseract.Close()
	result := make([]string, len(files))

	var buf *bytes.Buffer
	for i, file := range files {
		buf = bytes.NewBuffer(nil)
		if _, err := io.Copy(buf, file); err != nil {
			file.Close()
			return err
		}
		if err := tesseract.SetImageFromBytes(buf.Bytes()); err != nil {
			file.Close()
			return err
		}

		if text, err := tesseract.Text(); err != nil {
			file.Close()
			return err
		} else {
			result[i] = text
		}
	}
	return nil
}*/

func (RecognitionService) RecognizeEntireImages(docs []dto.ProcessedDocumentInfo) {
	tesseract := gosseract.NewClient()
	defer tesseract.Close()

	for _, doc := range docs {
		if err := tesseract.SetImageFromBytes(doc.ContentBuffer.Bytes()); err != nil {
			return
		}

		res, err := tesseract.Text()
		if err != nil {
			return
		}
		log.Println(res)
		doc.WasSuccess = true
	}
}
