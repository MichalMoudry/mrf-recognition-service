package producers

import (
	"recognition-service/transport/model"
)

// Image channel generator
func ImageBufferProducer(files []model.IncomingFile) <-chan model.IncomingFile {
	out := make(chan model.IncomingFile)
	go func() {
		for _, file := range files {
			out <- file
		}
		close(out)
	}()
	return out
}
