package transport

import (
	"net/http"
	"recognition-service/transport/model/contracts"
	"recognition-service/transport/util"
)

// A function for handling create workflow requests.
func (handler *Handler) CreateWorkflow(w http.ResponseWriter, r *http.Request) {
	var requestData *contracts.CreateWorkflowRequest
	if err := util.UnmarshallRequest(r, &requestData); err != nil {
		util.WriteErrResponse(w, http.StatusBadRequest, err)
		return
	}
	util.WriteResponse(w, http.StatusCreated, requestData)
}
