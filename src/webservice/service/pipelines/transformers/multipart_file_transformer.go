package transformers

import (
	"bytes"
	"io"
	"mime/multipart"
	"recognition-service/service/model/dto"
)

// A filter for transforming multipart files to buffers.
func MultipartFileTransformer(producer <-chan multipart.File) <-chan dto.ProcessedDocumentInfo {
	out := make(chan dto.ProcessedDocumentInfo)
	go func() {
		var buf *bytes.Buffer
		for file := range producer {
			buf = bytes.NewBuffer(nil)
			if _, err := io.Copy(buf, file); err != nil {
				out <- dto.ProcessedDocumentInfo{
					WasSuccess: false, // Set as failed if copy failed
				}
			} else {
				out <- dto.ProcessedDocumentInfo{
					ContentBuffer: buf,
					WasSuccess:    true,
				}
			}
		}
		close(out)
	}()
	return out
}
