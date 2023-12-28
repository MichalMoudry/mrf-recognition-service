package util

import (
	"encoding/json"
	"io"
	"net/http"
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
