package dto

import "bytes"

// A DTO for storing information about currently processed document.
type ProcessedDocumentInfo struct {
	Name          string
	ContentBuffer *bytes.Buffer
	Results       []string
	Error         error
}

// Function for checking if document was processed correctly or not.
func (doc *ProcessedDocumentInfo) WasSuccess() bool {
	return doc.Error == nil
}
