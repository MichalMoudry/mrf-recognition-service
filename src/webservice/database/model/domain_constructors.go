package model

import (
	"time"

	"github.com/google/uuid"
)

// A constructor function for the Application structure.
func NewApplication(name, creatorId string) *Application {
	now := time.Now()
	return &Application{
		Id:               uuid.New(),
		Name:             name,
		CreatorId:        creatorId,
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
	}
}

// Constructor function for a Workflow structure.
func NewWorkflow(isFullPageRecog, skipEnhancement, expectDiffImgs bool) *Workflow {
	now := time.Now()
	return &Workflow{
		Id:                    uuid.New(),
		IsFullPageRecognition: isFullPageRecog,
		SkipEnhancement:       skipEnhancement,
		ExpectDiffImages:      expectDiffImgs,
		DateAdded:             now,
		DateUpdated:           now,
	}
}

// Constructor function for FieldValue structure.
func NewFieldValue(name, value string, docId uuid.UUID) *FieldValue {
	return &FieldValue{
		Id:         uuid.New(),
		Name:       name,
		Value:      value,
		DocumentId: docId,
		DateAdded:  time.Now(),
	}
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
