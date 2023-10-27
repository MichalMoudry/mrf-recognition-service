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

from internal.config import Configuration
from internal.transport.model import contracts
from internal.transport.validation import is_string_valid_uuid
from internal.service.service_collection import ServiceCollection


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
    workflow = services.workflow_service.get_workflow(data.workflow_id)
    if workflow is None:
        return "Supplied workflow id is not", 400

    uploaded_files: dict[str, FileStorage] = await request.files
    batch_id = services.document_batch_service.create_batch(
        data.batch_name,
        data.user_id,
        data.workflow_id
    )

    app.add_background_task(
        services.fp_service.process_files,
        batch_id,
        workflow.id,
        uploaded_files
    )
    return "Batch created", 201


@app.get("/batches/<workflow_id>")
def get_batches(workflow_id: str):
    """
    An endpoint for obtaining a list for document batches for a workflow.
    """
    parsed_id = is_string_valid_uuid(workflow_id)
    if parsed_id is None:
        return "Supplied workflow ID is not a valid UUID.", 422

    return services.document_batch_service.get_batches(parsed_id), 200


@app.get("/batch/<batch_id>")
async def get_batch(batch_id: str):
    """
    An endpoint for obtaining information about a specific document batch.
    """
    parsed_id = is_string_valid_uuid(batch_id)
    if parsed_id is None:
        return "Supplied batch ID is not a valid UUID.", 422

    data = services.document_batch_service.get_batch(parsed_id)
    if data is None:
        return "", 200
    return data, 200


@app.get("/batch/<batch_id>/images")
async def get_batch_images(batch_id: str):
    """
    An endpoint for obtaining a list of images from a document batch.
    """
    parsed_id = is_string_valid_uuid(batch_id)
    if parsed_id is None:
        return "Supplied batch ID is not a valid UUID.", 422

    return services.document_batch_service.get_batch_images(parsed_id), 200


@app.delete("/batch/<batch_id>")
async def delete_batch(batch_id: str):
    """
    An endpoint for deleting processed document batches from the system.
    """
    parsed_id = is_string_valid_uuid(batch_id)
    if parsed_id is None:
        return "Supplied batch ID is not a valid UUID.", 422
    services.document_batch_service.delete_batch(parsed_id)
    return "", 200


@dapr_app.subscribe(pubsub_name="mrf_pub_sub", topic="workflow_add")
def workflow_add(event: v1.Event) -> str:
    """
    An endpoint for receiving data about a new workflow.
    """
    return "success"


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
    data = event.Data()
    if data is None:
        return "drop"
    parsed_data = json.loads(str(data))
    services.workflow_service.delete_workflow(parsed_data["workflow_id"])
    return "success"


@dapr_app.subscribe(pubsub_name="mrf_pub_sub", topic="user_delete")
async def user_delete(event: v1.Event):
    """
    An endpoint for receiving a delete event for user's data.
    """
    data = event.Data()
    if data is None:
        return "drop"
    parsed_data = json.loads(str(data))
    print(f'Received: id={parsed_data["id"]}, message="{parsed_data["message"]}"', flush=True)
    services.user_service.delete_users_data(parsed_data["user_id"])
    return "success"


if __name__ == "__main__":
    server_cfg = Config()
    server_cfg.bind = ["0.0.0.0:8000"]
    asyncio.run(serve(app, server_cfg))
