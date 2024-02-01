package contracts

// A structure representing data of a HTTP request for creating a new template field.
type CreateTemplateField struct {
	FieldName     string `json:"field_name" validate:"required"`
	Width         string `json:"width" validate:"required"`
	Height        string `json:"height" validate:"required"`
	XPosition     string `json:"x_position" validate:"required"`
	YPosition     string `json:"y_position" validate:"required"`
	ExpectedValue string `json:"expected_value" validate:"max=255"`
	IsIdentifying bool   `json:"is_identifying" validate:"required"`
}

// A structure representing data of a HTTP request for creating a new template.
type CreateTemplateRequest struct {
	Name   string                `json:"template_name" validate:"required,min=3,max=200"`
	Width  float32               `json:"width" validate:"required,number"`
	Height float32               `json:"height" validate:"required,number"`
	Fields []CreateTemplateField `json:"fields" validate:"required,dive,required"`
}
