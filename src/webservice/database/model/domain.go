package model

import (
	"time"

	"github.com/google/uuid"
)

// A structure representing a recognition application.
type Application struct {
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"app_name"`
	CreatorId        string    `db:"creator_id"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

type UserRole string

// A structure representing a *..0 relationship between application and users.
type ApplicationUsers struct {
	Id            uuid.UUID `db:"id"`
	ApplicationId uuid.UUID `db:"app_id"`
	UserId        string    `db:"usr_id"`
	Role          UserRole  `db:"role"`
}

// A structure representing a recognition workflow/process.
type Workflow struct {
	Id                    uuid.UUID `db:"id"`
	Name                  string    `db:"workflow_name"`
	ApplicationId         uuid.UUID `db:"application_id"`
	IsFullPageRecognition bool      `db:"setting_is_full_page_recog"`
	SkipImageEnhancement  bool      `db:"setting_skip_enhancement"`
	ExpectDifferentImages bool      `db:"setting_expect_diff_images"`
	ConcurrencyStamp      uuid.UUID `db:"concurrency_stamp"`
	DateAdded             time.Time `db:"date_added"`
	DateUpdated           time.Time `db:"date_updated"`
}

// A structure representing a custom processing task.
type Task struct {
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"task_name"`
	Content          []byte    `db:"content"`
	Description      string    `db:"description"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

// A structure representing a group of custom tasks.
type TaskGroup struct {
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"group_name"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
	DateUpdated      time.Time `db:"date_updated"`
}

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
	Id               uuid.UUID `db:"id"`
	Name             string    `db:"name"`
	ContentType      string    `db:"content_type"`
	ArchiveKey       string    `db:"archive_key"`
	DateArchived     time.Time `db:"date_archived"`
	Data             []byte    `db:"data"`
	BatchId          uuid.UUID `db:"batch_id"`
	ConcurrencyStamp uuid.UUID `db:"concurrency_stamp"`
	DateAdded        time.Time `db:"date_added"`
}

// Function for checking if a processed document is archived or not.
func (doc *ProcessedDocument) IsArchived() bool {
	return doc.ArchiveKey != ""
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
type RecognitionResult struct {
	Id         uuid.UUID `db:"id"`
	Name       string    `db:"name"`
	Value      string    `db:"value"`
	DocumentId uuid.UUID `db:"document_id"`
	DateAdded  time.Time `db:"date_added"`
}
