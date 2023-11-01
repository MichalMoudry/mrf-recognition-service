package service

import (
	"log"
)

// A simple job that prints a string.
func PrintJob() {
	log.Println("Executed print job.")
}

func ArchiveJob() {
	log.Println("Executed archive job.")
}
