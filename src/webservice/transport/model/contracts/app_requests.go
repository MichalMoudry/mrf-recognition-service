package contracts

// A structure representing data of a HTTP request for creating a new recognition app.
type CreateAppRequest struct {
	Name string `json:"app_name" validate:"required,min=3,max=200"`
}

// A structure representing data of a HTTP request for updating an existing recognition app.
type UpdateAppRequest struct {
	Name string `json:"new_app_name" validate:"required,min=3,max=200"`
}
