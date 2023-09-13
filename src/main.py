"""
Module that contains endpoint methods for the recognition service.
"""
from quart import Quart, Response, request
from quart.datastructures import FileStorage
from quart_schema import QuartSchema, DataSource, validate_request
from src.transport.model import dto
from src.service.file_processing import start_image_processing

app = Quart(__name__)
QuartSchema(app)


@app.get("/health")
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.post("/batch")
@validate_request(dto.CreateBatchModel, source=DataSource.FORM_MULTIPART)
async def create_batch(data: dto.CreateBatchModel) -> tuple[str, int]:
    """
    An endpoint for creating a new batch of documents for processing.
    """
    files: dict[str, FileStorage] = await request.files
    app.add_background_task(start_image_processing, data.batch_name, files)
    return "Batch created", 201


@app.get("/batch/<batch_id>")
async def get_batch(batch_id: str):
    """
    An endpoint for obtaining information about a specific document batch.
    """
    return "Supplied batch ID is not a valid UUID.", 422


@app.get("/batch/<batch_id>")
async def delete_batch(batch_id: str):
    """
    An endpoint for deleting processed document batches from the system.
    """
    return "Supplied batch ID is not a valid UUID.", 422


if __name__ == "__main__":
    app.run()
