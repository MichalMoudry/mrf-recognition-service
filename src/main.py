"""
Module that contains endpoint methods for the recognition service.
"""
from quart import Quart, request
from quart_schema import QuartSchema, DataSource, validate_request
from dotenv import load_dotenv
from transport.model import dto
from service.file_processing import execute_image_processing

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
    app.add_background_task(
        execute_image_processing,
        data.batch_name,
        await request.files
    )
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
    load_dotenv()
    app.run()
