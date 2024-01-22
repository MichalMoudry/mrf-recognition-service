package producers

import "mime/multipart"

// Image channel generator
func ImageBufferProducer(files ...multipart.File) <-chan multipart.File {
	out := make(chan multipart.File)
	go func() {
		for _, file := range files {
			out <- file
		}
		close(out)
	}()
	return out
}
