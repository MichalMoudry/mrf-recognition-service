package transport

import (
	"log"
	"net/http"
	"recognition-service/transport/model"
	"recognition-service/transport/util"
)

// A handler function for testing image recognition.
func (handler *Handler) TestImageRecognition(w http.ResponseWriter, r *http.Request) {
	var maxRequestSize int64 = 64 << 20
	r.Body = http.MaxBytesReader(w, r.Body, maxRequestSize)

	err := r.ParseMultipartForm(maxRequestSize)
	if err != nil {
		util.WriteErrResponse(w, http.StatusBadRequest, err)
	}
	for i, values := range r.MultipartForm.Value {
		log.Println("Key:", i)
		for _, v := range values {
			log.Println("\t- ", v)
		}
	}

	incomingFiles := make([]model.IncomingFile, len(r.MultipartForm.File))
	i := 0
	for key, file := range r.MultipartForm.File {
		incomingFiles[i] = model.IncomingFile{
			Name:   key,
			Header: file[1],
		}
		i += 1
	}
	util.WriteResponse(w, http.StatusOK, nil)
}
