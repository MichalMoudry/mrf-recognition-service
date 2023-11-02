package model

import "github.com/google/uuid"

type ProcessedDocument struct {
	Id          uuid.UUID `db:"id"`
	ContentType string    `db:"content_type"`
	IsArchived  bool      `db:"is_archived"`
	ArchiveKey  string    `db:"archive_key"`
	Content     []byte    `db:"data"`
}
