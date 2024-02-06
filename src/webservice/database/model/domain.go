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

// A business object that represents a document template.
type DocumentTemplate struct {
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"name"`
	Width            float32   `db:"width"`
	Height           float32   `db:"height"`
	Image            []byte    `db:"image"`
	WorkflowId       uuid.UUID `db:"workflow_id"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

// A business object representing document template's field.
type TemplateField struct {
	Id               uuid.UUID `db:"id"`
	Width            float32   `db:"width"`
	Height           float32   `db:"height"`
	XPosition        float32   `db:"x_position"`
	YPosition        float32   `db:"y_position"`
	ExpectedValue    string    `db:"expected_value"`
	IsIdentifying    bool      `db:"is_identifying"`
	TemplateId       uuid.UUID `db:"template_id"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

// A business object representing a recognized value on a specific document.
type FieldValue struct {
	Id         uuid.UUID `db:"id"`
	Name       string    `db:"name"`
	Value      string    `db:"value"`
	DocumentId uuid.UUID `db:"document_id"`
	DateAdded  time.Time `db:"date_added"`
}

// A structure representing a recognition application.
type Application struct {
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"app_name"`
	CreatorId        string    `db:"creator_id"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

// A duplicate of a business object representing a workflow in the system.
type Workflow struct {
	Id                    uuid.UUID `db:"id"`
	IsFullPageRecognition bool      `db:"is_full_page_recognition"`
	SkipEnhancement       bool      `db:"skip_enhancement"`
	ExpectDiffImages      bool      `db:"expect_diff_images"`
	ConcurrencyStamp      uuid.UUID `db:"concurrency_stamp"`
	DateAdded             time.Time `db:"date_added"`
	DateUpdated           time.Time `db:"date_updated"`
}
