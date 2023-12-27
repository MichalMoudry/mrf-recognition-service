package transport

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

type Handler struct {
	Port int
	Mux  *chi.Mux
}

// Function for initializing HTTP handler.
func Initialize(port int) *Handler {
	handler := &Handler{
		Port: port,
		Mux:  chi.NewRouter(),
	}
	handler.Mux.Use(middleware.Logger)

	// Protected routes
	handler.Mux.Post("/test-image-recognition", handler.TestImageRecognition)

	// Public routes
	handler.Mux.Get("/health", health)

	return handler
}

// A handler function for health checks.
func health(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNoContent)
}
