package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"recognition-service/config"
	"recognition-service/transport"

	"github.com/jackc/pgx/v5/pgxpool"
)

func main() {
	log.Println("Hello from recognition service! ʕ•ᴥ•ʔ")
	cfg, err := config.ReadFromConfigFile("./config.toml")
	if err != nil {
		log.Fatal(err)
	}

	// Connect to a database.
	dbPool, err := pgxpool.New(context.Background(), cfg.DbConnectionStr)
	if err != nil {
		log.Fatal(err)
	}
	defer dbPool.Close()

	handler := transport.Initialize(cfg.Port)

	// Start the web server.
	fmt.Printf("Trying to start a server on %d port.\n", handler.Port)
	if err = http.ListenAndServe(fmt.Sprintf(":%d", handler.Port), handler.Mux); err != nil {
		log.Fatal(err)
	}
}
