package main

import (
	"log"

	_ "github.com/jackc/pgx/v5/stdlib"
)

func main() {
	log.Println("Hello from recognition service! ʕ•ᴥ•ʔ")

	// Connect to a database.
	/*db, err := sqlx.Open("pgx", cfg.DbConnectionStr)
	if err != nil {
		log.Fatal(err)
	}

	// Start the web server.
	fmt.Printf("Starting a server on %d port\n", handler.Port)
	if err = http.ListenAndServe(fmt.Sprintf(":%d", handler.Port), handler.Mux); err != nil {
		log.Fatal(err)
	}*/
}
