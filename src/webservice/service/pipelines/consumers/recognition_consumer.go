package consumers

import "recognition-service/service/model/dto"

// A consumer filter that consumes all results in the pipeline.
func RecognitionConsumer(results <-chan dto.ProcessedDocumentInfo) []dto.ProcessedDocumentInfo {
	recogResults := []dto.ProcessedDocumentInfo{}
	for res := range results {
		recogResults = append(recogResults, res)
	}
	return recogResults
}
