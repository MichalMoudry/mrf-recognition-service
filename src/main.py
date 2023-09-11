"""
Module that contains endpoint methods for the recognition service.
"""
from flask import Flask, request
from .transport import api_metadata
from .transport.model import dto, validation

app = Flask(__name__)


@app.route("/healthz", methods=["GET"])
def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.route("/batch", methods=["POST"])
def create_batch():
    """
    An endpoint for creating a new batch of documents for processing.
    """
    file = request.files["file"]
    return {"file_name": file.content_type, "request_form": request.form}, 201


@app.route("/batch/<batch_id>", methods=["GET"])
def get_batch(batch_id: str):
    """
    An endpoint for obtaining information about a specific document batch.
    """
    return "Supplied batch ID is not a valid UUID.", 422


@app.route("/batch/<batch_id>", methods=["DELETE"])
def delete_batch(batch_id: str):
    """
    An endpoint for deleting processed document batches from the system.
    """
    return "Supplied batch ID is not a valid UUID.", 422
