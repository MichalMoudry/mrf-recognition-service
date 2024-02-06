package contracts

// A structure representing data of a HTTP request for creating a new document batch.
type CreateBatchRequest struct {
	BatchName  string `json:"batch_name" validate:"required,min=3,max=200"`
	WorkflowId string `json:"workflow_id" validate:"uuid,required"`
}
