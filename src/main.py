"""
Module that contains endpoint methods for the recognition service.
"""
from quart import Quart, request
from quart.datastructures import FileStorage
from quart_schema import QuartSchema, DataSource, validate_request
from internal.transport.model import dto, contracts
from internal.service.service_collection import ServiceCollection

app = Quart(__name__)
QuartSchema(app)
services = ServiceCollection()


@app.get("/health")
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.post("/batch")
@validate_request(contracts.CreateBatchModel, source=DataSource.FORM_MULTIPART)
async def create_batch(data: contracts.CreateBatchModel) -> tuple[str, int]:
    """
    An endpoint for creating a new batch of documents for processing.
    """
    uploaded_files: dict[str, FileStorage] = await request.files
    services.document_batch_service.create_batch(
        data.batch_name,
        data.workflow_id,
        [dto.DocumentDto(
            key,
            uploaded_files[key].stream.read(),
            uploaded_files[key].content_type
        ) for key in uploaded_files]
    )

    """app.add_background_task(
        execute_image_processing,
        data.batch_name,
        uploaded_files
    )"""
    return "Batch created", 201


@app.get("/batch/<batch_id>")
async def get_batch(batch_id: str):
    """
    An endpoint for obtaining information about a specific document batch.
    """
    return "Supplied batch ID is not a valid UUID.", 422


@app.delete("/batch/<batch_id>")
async def delete_batch(batch_id: str):
    """
    An endpoint for deleting processed document batches from the system.
    """
    return "Supplied batch ID is not a valid UUID.", 422


if __name__ == "__main__":
    app.run()
