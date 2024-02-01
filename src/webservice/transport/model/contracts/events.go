package contracts

// A structure representing cloud events (v1) from MQ.
type CloudEventV1[T interface{}] struct {
	Id     string `json:"id"`
	Data   T      `json:"data"`
	Source string `json:"source"`
}

// A structure for responses on accepted incoming events.
type EventResponse struct {
	IsSuccess bool  `json:"success"`
	Err       error `json:"err,omitempty"`
}
