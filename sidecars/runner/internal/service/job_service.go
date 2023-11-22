package service

import (
	"job-runner/internal/config"
	"job-runner/internal/service/model/ioc"
	"log"

	"github.com/go-co-op/gocron"
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
	log.Println("Executed print job.")
}

func (srvc JobService) ArchiveJob(cfg config.Config, job gocron.Job) {
	log.Println("Started archive job")
	tx, err := srvc.transactionManager.BeginTransaction(job.Context())
	defer func() {
		err = srvc.transactionManager.EndTransaction(tx, err)
	}()
	if err != nil {
		return
	}

	docs, err := srvc.docRepository.GetUnprocessedDocuments(tx)
	if err != nil {
		log.Fatalln(err)
		return
	}

	for _, doc := range docs {
		/*_, err = http.NewRequest(
			http.MethodPut,
			fmt.Sprintf("%s/%s", cfg.BlobStorageUrl, uuid.NewString()),
			bytes.NewReader(doc.Content),
		)
		if err != nil {
			continue
		}*/
		doc.IsArchived = true
	}
	log.Printf("Executed '%v' job.\n", job.GetName())
}
