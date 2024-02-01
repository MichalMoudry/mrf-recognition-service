package contracts

// A structure representing data of a HTTP request for creating a new task group.
type CreateTaskGroupRequest struct {
	WorkflowId string `json:"workflow_id" validate:"uuid,required"`
	Name       string `json:"group_name" validate:"required,min=3,max=200"`
}
