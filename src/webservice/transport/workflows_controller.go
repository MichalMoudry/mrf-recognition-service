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
	workflowId, err := util.GetUuidFromUrl(r)
	if err != nil {
		util.WriteErrResponse(w, http.StatusBadRequest, err)
		return
	}

	var requestData contracts.UpdateWorkflowRequest
	if err = util.UnmarshallRequest(r, &requestData); err != nil {
		util.WriteErrResponse(w, http.StatusBadRequest, err)
		return
	}

	if err = handler.Services.WorkflowService.UpdateWorkflow(r.Context(), workflowId, requestData); err != nil {
		util.WriteErrResponse(w, http.StatusInternalServerError, err)
		return
	}
	util.WriteResponse(w, http.StatusOK, contracts.EventResponse{IsSuccess: true})
}

// A function for handling delete workflow events/requests.
func (handler *Handler) DeleteWorkflow(w http.ResponseWriter, r *http.Request) {
	workflowId, err := util.GetUuidFromUrl(r)
	if err != nil {
		util.WriteErrResponse(w, http.StatusBadRequest, err)
		return
	}

	if err = handler.Services.WorkflowService.DeleteWorkflow(r.Context(), workflowId); err != nil {
		util.WriteErrResponse(w, http.StatusInternalServerError, err)
		return
	}
	util.WriteResponse(w, http.StatusOK, nil)
}
