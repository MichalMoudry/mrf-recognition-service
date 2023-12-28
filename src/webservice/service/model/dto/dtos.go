package dto

// A DTO for storing information about currently processed document.
type ProcessedDocumentInfo struct {
	Name       string
	Content    []byte
	Results    []string
	WasSuccess bool
}
