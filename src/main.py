"""
Module that contains endpoint methods for the recognition service.
"""
from cloudevents.sdk.event import v1
from dapr.ext.grpc import App
from time import sleep
from quart import Quart, request
from quart.datastructures import FileStorage
from quart_schema import QuartSchema, DataSource, validate_request
import json

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from internal.transport.model import dto, contracts
from internal.service.service_collection import ServiceCollection
from internal.config import Configuration

cfg = Configuration()
dapr_app = App()
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


@dapr_app.subscribe(pubsub_name="mrf_pub_sub", topic="workflow_update")
def workflow_update(event: v1.Event) -> str:
    """
    An endpoint for receiving updates about a specific workflow.
    """
    should_retry = cfg.dapr_settings.should_retry
    if should_retry:
        should_retry = False
        sleep(0.5)
        return "retry"
    return "success"


@dapr_app.subscribe(pubsub_name="mrf_pub_sub", topic="workflow_delete")
def workflow_delete(event: v1.Event) -> str:
    """
    An endpoint for receiving a delete event of a specific workflow.
    """
    return "success"


@dapr_app.subscribe(pubsub_name="mrf_pub_sub", topic="user_delete")
async def user_delete(event: v1.Event = None):
    """
    An endpoint for receiving a delete event for user's data.
    """
    data = event.Data()
    if data is None:
        return "drop"
    parsed_data: dict[str, any] = json.loads(str(data))
    print(f'Received: id={parsed_data["id"]}, message="{parsed_data["message"]}"', flush=True)
    services.user_service.delete_users_data(parsed_data["user_id"])
    return "success"


if __name__ == "__main__":
    server_cfg = Config()
    server_cfg.bind = ["0.0.0.0:8000"]
    asyncio.run(serve(app, server_cfg))
