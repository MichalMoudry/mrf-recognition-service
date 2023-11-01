package service

import (
	"fmt"
	"log"
	"time"
)

// A simple job that prints a string.
func PrintJob() {
	fmt.Printf("%s: Executed print job.\n", time.Now())
	log.Println("Executed print job.")
}

func ArchiveJob() {
	fmt.Printf("%s: Executed archive job.\n", time.Now())
	log.Println("Executed archive job.")
}
