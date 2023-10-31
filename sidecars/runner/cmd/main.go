package main

import (
	"fmt"
	"job-runner/internal/service"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/go-co-op/gocron"
)

func main() {
	scheduler := gocron.NewScheduler(time.UTC)
	scheduler.Every(1).Minute().Do(service.PrintJob)
	scheduler.Every(1).Day().At("01:00:00").Do(service.ArchiveJob)
	scheduler.StartAsync()

	// Exit handling
	quitChannel := make(chan os.Signal, 1)
	signal.Notify(quitChannel, syscall.SIGINT, syscall.SIGTERM)
	<-quitChannel
	fmt.Println("Exiting scheduler app...")
}
