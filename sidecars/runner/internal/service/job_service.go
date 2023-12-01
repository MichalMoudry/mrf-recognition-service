package service

import (
	"bytes"
	"fmt"
	"job-runner/internal/config"
	"job-runner/internal/service/errors"
	"job-runner/internal/service/model/ioc"
	"log"
	"net/http"
	"time"

	"github.com/go-co-op/gocron"
	"github.com/google/uuid"
)

type JobService struct {
	transactionManager ioc.ITransactionManager
	docRepository      ioc.IProcessedDocumentRepository
}

func NewJobService(txManager ioc.ITransactionManager, docRepo ioc.IProcessedDocumentRepository) *JobService {
	return &JobService{
		transactionManager: txManager,
		docRepository:      docRepo,
	}
}

// A simple job that prints a string.
func (srvc JobService) PrintJob() {
	log.Println("Executed 'print' job.")
}

func (srvc JobService) ArchiveJob(cfg config.Config, job gocron.Job) {
	tx, err := srvc.transactionManager.BeginTransaction(job.Context())
	if err != nil {
		log.Println(err)
		return
	}

	docs, err := srvc.docRepository.GetUnprocessedDocuments(tx)
	if err != nil {
		log.Fatal(err)
		return
	}
	for _, doc := range docs {
		err = uploadBlob(cfg.BlobStorageUrl, doc.Id, doc.Content)
		if err != nil {
			log.Printf("Failed to update '%v' document.\n", doc.Id)
			continue
		}
		doc.IsArchived = true
		log.Printf("Archived doc with id: %v", doc.Id)
	}

	err = srvc.transactionManager.EndTransaction(tx, err)
	if err != nil {
		log.Printf("An error occured when ending a transaction\n")
	}
}

// Function for upload a new blob the blob storage.
func uploadBlob(url string, blobId uuid.UUID, content []byte) error {
	request, err := http.NewRequest(
		http.MethodPut,
		fmt.Sprintf("%s/%s", url, blobId),
		bytes.NewReader(content),
	)
	request.Header.Add("Authorization", "")
	request.Header.Add("x-ms-date", time.Now().UTC().String())
	request.Header.Add("x-ms-version", "2023-11-03")
	if err != nil {
		return err
	}

	response, err := http.DefaultClient.Do(request)
	if err != nil {
		return err
	}
	if response.StatusCode != 201 {
		return errors.ErrBlobUploadFailed
	}
	return nil
}
