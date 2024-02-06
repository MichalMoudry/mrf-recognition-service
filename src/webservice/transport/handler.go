package transport

import (
	"net/http"
	"recognition-service/transport/model/ioc"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/jmoiron/sqlx"
)

type Handler struct {
	Port     int
	Mux      *chi.Mux
	Services *ioc.ServiceCollection
}

// Function for initializing HTTP handler.
func Initialize(port int, db *sqlx.DB) *Handler {
	handler := &Handler{
		Port:     port,
		Mux:      chi.NewRouter(),
		Services: ioc.NewServiceCollection(db),
	}
	handler.Mux.Use(middleware.Logger)

	// Protected routes
	handler.Mux.Group(func(r chi.Router) {
		//handler.Mux.Post("/test-image-recognition", handler.TestImageRecognition)
		r.Post("/test-image-recognition", handler.TestImageRecognition)

		r.Route("/workflows", func(r chi.Router) {
			r.Post("/", handler.CreateWorkflow)
			r.Post("/update", handler.UpdateWorkflow)
			r.Post("/delete", nil)
			r.Get("/batches", nil) // GET workflow's batches
			r.Get("/templates", nil)
		})

		r.Route("/batch", func(r chi.Router) {
			r.Get("/{uuid}", nil)        // GET batch info
			r.Get("/{uuid}/images", nil) // GET batch's images
			r.Delete("/{uuid}", nil)     // DELETE batch
		})

		r.Route("/template", func(r chi.Router) {
			r.Post("/", nil) // CREATE template
		})
		r.Post("/users/delete", nil)
	})

	// Public routes
	handler.Mux.Get("/health", health)
	handler.Mux.Get("/dapr/subscribe", ConfigureSubscribeHandler)

	return handler
}

// A handler function for health checks.
func health(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNoContent)
}
