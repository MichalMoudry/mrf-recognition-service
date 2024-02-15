package contracts

import (
	"recognition-service/service/model/dto"
	"strconv"
)

// A structure representing data of a HTTP request for creating a new recognition workflow.
type CreateWorkflowRequest struct {
	Name                  string `json:"workflow_name" validate:"required,min=3,max=200"`
	AppId                 string `json:"app_id" validate:"uuid,required"`
	IsFullPageRecognition string `json:"is_full_page_recog" validate:"boolean,required"`
	SkipImageEnhancement  string `json:"skip_img_enhancement" validate:"boolean,required"`
	ExpectDifferentImages string `json:"expect_diff_images" validate:"boolean,required"`
}

// A structure representing data of a HTTP request for updating a specific workflow.
type UpdateWorkflowRequest struct {
	Name                  string `json:"new_workflow_name" validate:"required,min=3,max=200"`
	IsFullPageRecognition string `json:"is_full_page_recog" validate:"boolean,required"`
	SkipImageEnhancement  string `json:"skip_img_enhancement" validate:"boolean,required"`
	ExpectDifferentImages string `json:"expect_diff_images" validate:"boolean,required"`
}

func (request *UpdateWorkflowRequest) ToWorkflowInfo() *dto.WorkflowInfo {
	isFullPage, _ := strconv.ParseBool(request.IsFullPageRecognition)
	skipImgEnhancement, _ := strconv.ParseBool(request.SkipImageEnhancement)
	expectDiffImages, _ := strconv.ParseBool(request.ExpectDifferentImages)
	return &dto.WorkflowInfo{
		Name:                  request.Name,
		IsFullPageRecognition: isFullPage,
		SkipImageEnhancement:  skipImgEnhancement,
		ExpectDifferentImages: expectDiffImages,
	}
}
