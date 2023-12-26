package util

import (
	"encoding/json"
	"net/http"
)

// Function for writing an error response to a HTTP request.
func WriteErrResponse(w http.ResponseWriter, statusCode int, err error) {
	w.WriteHeader(statusCode)
	if err != nil {
		w.Write(
			[]byte(err.Error()),
		)
	}
}

// Function for writing any response to a HTTP request.
func WriteResponse(w http.ResponseWriter, statusCode int, body any) {
	w.WriteHeader(statusCode)
	if body != nil {
		b, _ := json.Marshal(body)
		w.Write(b)
	}
}
