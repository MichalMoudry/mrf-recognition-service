package transport

import (
	"net/http"
	"recognition-service/transport/model/contracts"
	"recognition-service/transport/util"
)

// A function for handling create events/workflow requests.
func (handler *Handler) CreateWorkflow(w http.ResponseWriter, r *http.Request) {
	util.WriteResponse(w, http.StatusOK, contracts.EventResponse{IsSuccess: true})
}

// A function for handling update events/workflow requests.
func (handler *Handler) UpdateWorkflow(w http.ResponseWriter, r *http.Request) {
	/*w.Header().Set("Content-Type", "application/json")
	var requestData contracts.CreateWorkflowRequest
	if err := util.UnmarshallRequest(r, &requestData); err != nil {
		util.WriteResponse(
			w,
			http.StatusBadRequest,
			contracts.EventResponse{IsSuccess: false, Err: err},
		)
		return
	}

	util.WriteResponse(w, http.StatusOK, contracts.EventResponse{IsSuccess: true})*/
	util.WriteResponse(w, http.StatusOK, contracts.EventResponse{IsSuccess: true})
}

// A function for handling delete workflow events/requests.
func (handler *Handler) DeleteWorkflow(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var requestData contracts.CloudEventV1[string]
	if err := util.UnmarshallRequest(r, &requestData); err != nil {
		util.WriteResponse(
			w,
			http.StatusBadRequest,
			contracts.EventResponse{IsSuccess: false, Err: err},
		)
		return
	}

	util.WriteResponse(w, http.StatusOK, contracts.EventResponse{IsSuccess: true})
}
