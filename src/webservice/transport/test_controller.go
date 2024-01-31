package transport

import (
	"log"
	"net/http"
	"recognition-service/transport/util"
)

// A handler function for testing image recognition.
func (handler *Handler) TestImageRecognition(w http.ResponseWriter, r *http.Request) {
	var maxRequestSize int64 = 64 << 20
	//r.Body = http.MaxBytesReader(w, r.Body, maxRequestSize)

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
	for i, file := range r.MultipartForm.File {
		log.Println("File key:", i)
		for _, header := range file {
			log.Println("\t- ", header.Filename)
		}
	}
	util.WriteResponse(w, http.StatusOK, nil)
}
