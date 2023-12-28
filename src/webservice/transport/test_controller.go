package transport

import (
	"net/http"
	"recognition-service/transport/util"
)

// A handler function for testing image recognition.
func (handler *Handler) TestImageRecognition(w http.ResponseWriter, r *http.Request) {
	err := r.ParseMultipartForm(32 << 20)
	if err != nil {
		util.WriteErrResponse(w, http.StatusInternalServerError, err)
	}
	util.WriteResponse(w, http.StatusOK, nil)
}
