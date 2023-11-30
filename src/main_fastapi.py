"""
Module containg code with FastApi version of this service.
"""
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()


class DocumentBatch(BaseModel):
    name: str
    files: list[UploadFile]


@app.get("/health")
def health():
    """
    A health check endpoint.
    """
    return "healthy"


@app.post("/test/files")
def test_file_upload(batch: DocumentBatch):
    """
    An endpoint for testing if file upload works.
    """
    for file in batch.files:
        print(file.filename)
