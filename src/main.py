"""
Module that contains endpoint methods for the recognition service.
"""
from flask import Flask, request
from .transport import api_metadata
from .transport.model import dto, validation
from .service import file_processing

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.route("/batch", methods=["POST"])
async def create_batch():
    """
    An endpoint for creating a new batch of documents for processing.
    """
    await file_processing.start_image_processing(request.files)
    return "Batch created", 201


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


if __name__ == "__main__":
    app.run()
