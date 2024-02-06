package transport

import (
	"net/http"
	"recognition-service/transport/util"
)

type subscription struct {
	PubsubName string            `json:"pubsubname"`
	Topic      string            `json:"topic"`
	Metadata   map[string]string `json:"metadata,omitempty"`
	Route      route             `json:"routes"`
}

type route struct {
	Rules   []rule `json:"rules,omitempty"`
	Default string `json:"default,omitempty"`
}

type rule struct {
	Match string `json:"match"`
	Path  string `json:"path"`
}

func ConfigureSubscribeHandler(w http.ResponseWriter, _ *http.Request) {
	pubSubName := "pub-sub"
	v := []subscription{
		{
			PubsubName: pubSubName,
			Topic:      "user-delete",
			Route: route{
				Rules: []rule{
					{
						Match: `event.type == "user-delete"`,
						Path:  "/users/delete",
					},
				},
				Default: "/users/delete",
			},
		},
		{
			PubsubName: pubSubName,
			Topic:      "new-workflow",
			Route: route{
				Rules: []rule{
					{
						Match: `event.type == "new-workflow"`,
						Path:  "/workflows/delete",
					},
				},
				Default: "/workflows/delete",
			},
		},
		{
			PubsubName: pubSubName,
			Topic:      "workflow_update",
			Route: route{
				Rules: []rule{
					{
						Match: `event.type == "workflow_update"`,
						Path:  "/workflows/update",
					},
				},
				Default: "/workflows/update",
			},
		},
		{
			PubsubName: pubSubName,
			Topic:      "workflow_delete",
			Route: route{
				Rules: []rule{
					{
						Match: `event.type == "workflow_delete"`,
						Path:  "/workflows/delete",
					},
				},
				Default: "/workflows/delete",
			},
		},
	}

	util.WriteResponse(w, http.StatusOK, v)
}
