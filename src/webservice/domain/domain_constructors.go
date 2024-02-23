package domain

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

// A constructor function for the Application structure.
func NewWorkflow(name string, appId uuid.UUID, isFullPageRecog, skipImgEnhacement, expectDiffImages bool) *Workflow {
	now := time.Now()
	return &Workflow{
		Id:            uuid.New(),
		Name:          name,
		ApplicationId: appId,
		Settings: WorkflowSetting{
			IsFullPageRecognition: isFullPageRecog,
			SkipImageEnhancement:  skipImgEnhacement,
			ExpectDifferentImages: expectDiffImages,
		},
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
	}
}

// A constructor function for the TaskGroup structure.
func NewTaskGroup(name string) *TaskGroup {
	now := time.Now()
	return &TaskGroup{
		Id:               uuid.New(),
		Name:             name,
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
	}
}

// A constructor function for the Task structure.
func NewTask(name, description string, content []byte) *Task {
	now := time.Now()
	return &Task{
		Id:               uuid.New(),
		Name:             name,
		Description:      description,
		Content:          content,
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
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
	}
}

// Constructor function for the ProcessedDocument structure.
func NewProcessedDocument(name, contentType, archiveKey string, dateArchived time.Time, data []byte, batchId uuid.UUID) *ProcessedDocument {
	now := time.Now()
	return &ProcessedDocument{
		Id:           uuid.New(),
		Name:         name,
		ContentType:  contentType,
		ArchiveKey:   archiveKey,
		DateArchived: dateArchived,
		Data:         data,
		BatchId:      batchId,
		DateAdded:    now,
		DateUpdated:  now,
	}
}

// A constructor function for DocumentTemplate business object.
func NewDocumentTemplate(name string, width, height float32, img []byte, workflowId uuid.UUID) *DocumentTemplate {
	now := time.Now()
	return &DocumentTemplate{
		Id:               uuid.New(),
		Width:            width,
		Height:           height,
		Image:            img,
		WorkflowId:       workflowId,
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
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
		Id:               uuid.New(),
		Width:            width,
		Height:           height,
		XPosition:        xPosition,
		YPosition:        yPostion,
		ExpectedValue:    expectedVal,
		IsIdentifying:    isId,
		TemplateId:       templateId,
		ConcurrencyStamp: uuid.New(),
		DateAdded:        now,
		DateUpdated:      now,
	}
}

// Constructor function for FieldValue structure.
func NewFieldValue(name, value string, docId uuid.UUID) *RecognitionResult {
	return &RecognitionResult{
		Id:         uuid.New(),
		Name:       name,
		Value:      value,
		DocumentId: docId,
		DateAdded:  time.Now(),
	}
}
