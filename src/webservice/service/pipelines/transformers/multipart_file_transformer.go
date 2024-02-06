package transformers

import (
	"bytes"
	"io"
	"recognition-service/service/model/dto"
	"recognition-service/transport/model"
)

// A filter for transforming multipart files to buffers.
func MultipartFileTransformer(producer <-chan model.IncomingFile) <-chan dto.ProcessedDocumentInfo {
	out := make(chan dto.ProcessedDocumentInfo)
	go func() {
		var buf *bytes.Buffer
		for file := range producer {
			buf = bytes.NewBuffer(nil)
			file, err := file.Header.Open()
			if err != nil {
				out <- dto.ProcessedDocumentInfo{
					Error: err,
				}
				continue
			}

			if _, err = io.Copy(buf, file); err != nil {
				out <- dto.ProcessedDocumentInfo{
					Error: err,
				}
			} else {
				out <- dto.ProcessedDocumentInfo{
					ContentBuffer: buf,
				}
			}
		}
		close(out)
	}()
	return out
}
