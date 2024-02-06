package main

import (
	"fmt"
	"log"
	"net/http"
	"recognition-service/config"
	"recognition-service/transport"
	"recognition-service/transport/model/ioc"

	_ "github.com/jackc/pgx/v5/stdlib"
	"github.com/jmoiron/sqlx"
)

func main() {
	log.Println("Hello from recognition service! ʕ•ᴥ•ʔ")
	cfg, err := config.ReadFromConfigFile("./config.toml")
	if err != nil {
		log.Fatal(err)
	}

	// Connect to a database.
	db, err := sqlx.Open("pgx", cfg.DbConnectionStr)
	if err != nil {
		log.Fatal(err)
	}

	handler := transport.Initialize(cfg.Port, db, ioc.NewServiceCollection(db))
	// Start the web server.
	fmt.Printf("Trying to start a server on %d port.\n", handler.Port)
	if err = http.ListenAndServe(fmt.Sprintf(":%d", handler.Port), handler.Mux); err != nil {
		log.Fatal(err)
	}
}
