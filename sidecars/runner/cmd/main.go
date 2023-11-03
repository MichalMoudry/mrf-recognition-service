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
	services := service.NewServiceCollection()

	scheduler := gocron.NewScheduler(time.UTC)
	//scheduler.Every(1).Minute().Do(services.JobService.PrintJob)
	//scheduler.Every(7).Seconds().DoWithJobDetails(services.JobService.ArchiveJob, cfg)
	scheduler.Cron("0 3 * * *").DoWithJobDetails(services.JobService.ArchiveJob, cfg)
	scheduler.StartAsync()

	// Exit handling
	quitChannel := make(chan os.Signal, 1)
	signal.Notify(quitChannel, syscall.SIGINT, syscall.SIGTERM)
	<-quitChannel
	fmt.Println("Exiting scheduler app...")
}
