package util

import (
	"encoding/json"
	"io"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/google/uuid"
)

// Function for unmarshalling and validating incoming HTTP requests.
func UnmarshallRequest(request *http.Request, b any) error {
	body, err := io.ReadAll(request.Body)
	if err != nil {
		return err
	}

	if err = json.Unmarshal(body, b); err != nil {
		return err
	}

	if err = validate.Struct(b); err != nil {
		return err
	}
	return nil
}

// Function for parsing an UUID from request's URL.
func GetUuidFromUrl(r *http.Request) (uuid.UUID, error) {
	return uuid.Parse(chi.URLParam(r, "uuid"))
}
