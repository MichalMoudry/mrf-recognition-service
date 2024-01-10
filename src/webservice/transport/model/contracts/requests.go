package contracts

// A structure representing data of a HTTP request for creating a new document batch.
type CreateBatchRequest struct {
	BatchName  string `json:"batch_name" validate:"required,min=3,max=200"`
	WorkflowId string `json:"workflow_id" validate:"uuid,required"`
}

// A structure representing data of a HTTP request for creating a new workflow.
type CreateWorkflowRequest struct {
	IsFullPageRecognition string `json:"is_full_page_recognition" validate:"boolean,required"`
	SkipImgEnhancement    string `json:"skip_img_enchancement" validate:"boolean,required"`
	ExpectDiffImages      string `json:"expect_diff_images" validate:"boolean,required"`
}

// A structure representing data of a HTTP request for creating a new template field.
type CreateTemplateField struct {
	FieldName     string `json:"field_name" validate:"required"`
	Width         string `json:"width" validate:"required"`
	Height        string `json:"height" validate:"required"`
	XPosition     string `json:"x_position" validate:"required"`
	YPosition     string `json:"y_position" validate:"required"`
	ExpectedValue string `json:"expected_value"`
	IsIdentifying bool   `json:"is_identifying" validate:"required"`
}

// A structure representing data of a HTTP request for creating a new template.
type CreateTemplateRequest struct {
	Fields []CreateTemplateField
}
