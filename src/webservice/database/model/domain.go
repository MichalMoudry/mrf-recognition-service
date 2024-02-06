package model

import (
	"time"

	"github.com/google/uuid"
)

// An enum representing current state of the document batch.
type BatchState int

const (
	// Batch is waiting to be processed.
	WAITING BatchState = iota
	// Batch is currently being processed.
	PROCESSING
	// Processing of the batch has successfully completed.
	COMPLETED
	// Processing of the batch has failed.
	FAILED
)

// A business object representing a batch of one or more documents.
type DocumentBatch struct {
	Id            uuid.UUID  `db:"id"`
	Name          string     `db:"name"`
	State         BatchState `db:"state"`
	StartDate     time.Time  `db:"start_date"`
	CompletedDate time.Time  `db:"completed_date"`
	WorkflowId    uuid.UUID  `db:"workflow_id"`
	AuthorId      string     `db:"author_id"`
	DateAdded     time.Time  `db:"date_added"`
	DateUpdated   time.Time  `db:"date_updated"`
}

// Constructor function for the DocumentBatch business object.
func NewDocumentBatch(name, author string, startDate, endDate time.Time, workflowId uuid.UUID) *DocumentBatch {
	now := time.Now()
	return &DocumentBatch{
		Id:            uuid.New(),
		Name:          name,
		State:         WAITING,
		StartDate:     startDate,
		CompletedDate: endDate,
		WorkflowId:    workflowId,
		AuthorId:      author,
		DateAdded:     now,
		DateUpdated:   now,
	}
}

// A business object representing a processed document.
type ProcessedDocument struct {
	Id           uuid.UUID `db:"id"`
	Name         string    `db:"name"`
	ContentType  string    `db:"content_type"`
	IsArchived   bool      `db:"is_archived"`
	ArchiveKey   string    `db:"archive_key"`
	DateArchived time.Time `db:"date_archived"`
	Data         []byte    `db:"data"`
	BatchId      uuid.UUID `db:"batch_id"`
	DateAdded    time.Time `db:"date_added"`
	DateUpdated  time.Time `db:"date_updated"`
}

// Constructor function for the ProcessedDocument structure.
func NewProcessedDocument(name, contentType, archiveKey string, dateArchived time.Time, data []byte, batchId uuid.UUID) *ProcessedDocument {
	now := time.Now()
	return &ProcessedDocument{
		Id:           uuid.New(),
		Name:         name,
		ContentType:  contentType,
		IsArchived:   archiveKey != "",
		ArchiveKey:   archiveKey,
		DateArchived: dateArchived,
		Data:         data,
		BatchId:      batchId,
		DateAdded:    now,
		DateUpdated:  now,
	}
}

// A business object that represents a document template.
type DocumentTemplate struct {
	Id          uuid.UUID `db:"id"`
	Name        string    `db:"name"`
	Width       float32   `db:"width"`
	Height      float32   `db:"height"`
	Image       []byte    `db:"image"`
	WorkflowId  uuid.UUID `db:"workflow_id"`
	DateAdded   time.Time `db:"date_added"`
	DateUpdated time.Time `db:"date_updated"`
}

// A constructor function for DocumentTemplate business object.
func NewDocumentTemplate(name string, width, height float32, img []byte, workflowId uuid.UUID) *DocumentTemplate {
	now := time.Now()
	return &DocumentTemplate{
		Id:          uuid.New(),
		Width:       width,
		Height:      height,
		Image:       img,
		WorkflowId:  workflowId,
		DateAdded:   now,
		DateUpdated: now,
	}
}

// A business object representing document template's field.
type TemplateField struct {
	Id            uuid.UUID `db:"id"`
	Width         float32   `db:"width"`
	Height        float32   `db:"height"`
	XPosition     float32   `db:"x_position"`
	YPosition     float32   `db:"y_position"`
	ExpectedValue string    `db:"expected_value"`
	IsIdentifying bool      `db:"is_identifying"`
	TemplateId    uuid.UUID `db:"template_id"`
	DateAdded     time.Time `db:"date_added"`
	DateUpdated   time.Time `db:"date_updated"`
}

// Constructor function for TemplateField business object.
func NewTemplateField(
	width,
	height,
	xPosition,
	yPostion float32,
	expectedVal string,
	isId bool,
	templateId uuid.UUID) *TemplateField {
	now := time.Now()
	return &TemplateField{
		Id:            uuid.New(),
		Width:         width,
		Height:        height,
		XPosition:     xPosition,
		YPosition:     yPostion,
		ExpectedValue: expectedVal,
		IsIdentifying: isId,
		TemplateId:    templateId,
		DateAdded:     now,
		DateUpdated:   now,
	}
}

// A business object representing a recognized value on a specific document.
type FieldValue struct {
	Id          uuid.UUID `db:"id"`
	Name        string    `db:"name"`
	Value       string    `db:"value"`
	DocumentId  uuid.UUID `db:"document_id"`
	DateAdded   time.Time `db:"date_added"`
	DateUpdated time.Time `db:"date_updated"`
}

// Constructor function for FieldValue structure.
func NewFieldValue(name, value string, docId uuid.UUID) *FieldValue {
	now := time.Now()
	return &FieldValue{
		Id:          uuid.New(),
		Name:        name,
		Value:       value,
		DocumentId:  docId,
		DateAdded:   now,
		DateUpdated: now,
	}
}

// A duplicate of a business object representing a workflow in the system.
type Workflow struct {
	Id                    uuid.UUID `db:"id"`
	IsFullPageRecognition bool      `db:"is_full_page_recognition"`
	SkipEnhancement       bool      `db:"skip_enhancement"`
	ExpectDiffImages      bool      `db:"expect_diff_images"`
	DateAdded             time.Time `db:"date_added"`
}
