package service

import (
	"fmt"
	"time"
)

// A simple job that prints a string.
func PrintJob() {
	fmt.Printf("%s: Executed print job.\n", time.Now())
}

func ArchiveJob() {
	fmt.Printf("%s: Executed archive job.\n", time.Now())
}
