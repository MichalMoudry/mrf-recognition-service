"""
Module containg code with FastApi version of this service.
"""
from typing import Annotated
from fastapi import FastAPI, Form, UploadFile
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def health():
    """
    A health check endpoint.
    """
    return "healthy"


@app.post("/test/files")
def test_file_upload(batch_name: Annotated[str, Form()], files: list[UploadFile]):
    """
    An endpoint for testing if file upload works.
    """
    return {"batch_name": batch_name, "filenames": [file.filename for file in files]}
