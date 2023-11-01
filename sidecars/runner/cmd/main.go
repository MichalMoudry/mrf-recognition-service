package main

import (
	"fmt"
	"job-runner/internal/config"
	"job-runner/internal/database"
	"job-runner/internal/service"
	"log"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/go-co-op/gocron"
)

func main() {
	fmt.Println("Hello from job runner! ʕ•ᴥ•ʔ")

	cfg, err := config.ReadCfgFromFile("config.toml")
	if err != nil {
		log.Fatal(err)
	}
	database.OpenDb(cfg.ConnectionString)

	scheduler := gocron.NewScheduler(time.UTC)
	scheduler.Every(1).Minute().Do(service.PrintJob)
	scheduler.Cron("* * * * *").Do(service.ArchiveJob)
	scheduler.Cron("0 3 * * *").Do(service.ArchiveJob)
	scheduler.StartAsync()

	// Exit handling
	quitChannel := make(chan os.Signal, 1)
	signal.Notify(quitChannel, syscall.SIGINT, syscall.SIGTERM)
	<-quitChannel
	fmt.Println("Exiting scheduler app...")
}
