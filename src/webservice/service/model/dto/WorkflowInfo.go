package dto

import "github.com/google/uuid"

type WorkflowInfo struct {
	Name                  string
	AppId                 uuid.UUID
	IsFullPageRecognition bool
	SkipImageEnhancement  bool
	ExpectDifferentImages bool
}
