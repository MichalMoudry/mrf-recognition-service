package model

import "mime/multipart"

type IncomingFile struct {
	Name   string
	Header *multipart.FileHeader
}
