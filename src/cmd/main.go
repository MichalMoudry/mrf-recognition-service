package main

import (
	"fmt"
	"log"
	"net/http"
	"recognition-service/config"
	"recognition-service/transport"
)

func main() {
	log.Println("Hello from recognition service! ʕ•ᴥ•ʔ")
	cfg, err := config.ReadFromConfigFile("./config.toml")
	if err != nil {
		log.Fatal(err)
	}

	handler := transport.Initialize(cfg.Port)

	// Start web server
	fmt.Printf("Trying to start a server on %d port.\n", handler.Port)
	if err = http.ListenAndServe(fmt.Sprintf(":%d", handler.Port), handler.Mux); err != nil {
		log.Fatal(err)
	}
}
