package dto

import "bytes"

// A DTO for storing information about currently processed document.
type ProcessedDocumentInfo struct {
	Name          string
	ContentBuffer *bytes.Buffer
	Results       []string
	WasSuccess    bool
}
