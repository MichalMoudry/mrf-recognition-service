package contracts

// A structure for responses on accepted incoming events.
type EventResponse struct {
	IsSuccess bool  `json:"success"`
	Err       error `json:"err,omitempty"`
}
