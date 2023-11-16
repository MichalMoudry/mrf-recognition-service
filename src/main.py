"""
Module that contains endpoint methods for the recognition service.
"""
from cloudevents.http import from_http
from pydantic import ValidationError
from quart import Quart, Response, request, jsonify
from quart.datastructures import FileStorage
from quart_schema import QuartSchema, DataSource, validate_request
import json

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from internal.service.dapr_service import PUBSUB_NAME
from internal.transport.model import contracts
from internal.transport.validation import is_string_valid_uuid
from internal.service.service_collection import ServiceCollection

app = Quart(__name__)
QuartSchema(app)
services = ServiceCollection()


@app.get("/health")
async def health() -> Response:
    """
    Service health endpoint method.
    """
    return jsonify("healthy")


@app.post("/batch")
async def create_batch():
    """
    An endpoint for creating a new batch of documents for processing.
    """
    form_data = await request.form
    uploaded_files: dict[str, FileStorage] = await request.files
    if len(uploaded_files) == 0:
        return "You need to upload more than one file", 400
    try:
        data = contracts.CreateBatchModel(
            batch_name=form_data["batch_name"],
            workflow_id=form_data["workflow_id"],
            user_id=form_data["user_id"]
        )
    except ValidationError as err:
        return err.json(), 400
    workflow = services.workflow_service.get_workflow(data.workflow_id)
    if workflow is None:
        return "Supplied workflow id is not in the DB", 400
    
    batch_id = services.document_batch_service.create_batch(
        data.batch_name,
        data.user_id,
        data.workflow_id
    )
    app.add_background_task(
        services.fp_service.process_files,
        batch_id,
        workflow.id,
        data.user_id,
        uploaded_files
    )
    return "Batch created", 201


@app.post("/batch-test")
async def read_documents():
    """
    A endpoint for testing if document reading works.
    """
    uploaded_files: dict[str, FileStorage] = await request.files
    app.add_background_task(services.fp_service.test_process_image, uploaded_files)
    return "test started", 200


@app.get("/batches/<workflow_id>")
async def get_batches(workflow_id: str):
    """
    An endpoint for obtaining a list for document batches for a workflow.
    """
    parsed_id = is_string_valid_uuid(workflow_id)
    if parsed_id is None:
        return "Supplied workflow ID is not a valid UUID.", 400

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
    return "success", 200


@app.post("/template")
@validate_request(contracts.CreateTemplateModel, source=DataSource.FORM_MULTIPART)
async def create_template(data: contracts.CreateTemplateModel):
    """
    An endpoint for creating a new document template.
    """
    uploaded_files: dict[str, FileStorage] = await request.files
    if len(uploaded_files) > 1:
        return "You can only upload one file.", 400
    services.template_service.create_new_template(data, next(uploaded_files.values()))
    return "Ok", 201


@app.get("/workflow/<workflow_id>/templates")
async def get_templates(workflow_id: str):
    """
    An endpoint for obtaining information about a specific template.
    """
    parsed_id = is_string_valid_uuid(workflow_id)
    if parsed_id is None:
        return "Supplied batch ID is not a valid UUID.", 400
    return "", 200


@app.route('/dapr/subscribe', methods=['GET'])
async def subscribe():
    """
    An endpoint for Dapr pub/sub subscriptions.
    """
    subscriptions = [
        {
            "pubsubname": PUBSUB_NAME,
            "topic": "new-workflow",
            "route": "workflows/add"
        },
        {
            "pubsubname": PUBSUB_NAME,
            "topic": "workflow_update",
            "route": "workflows/update"
        },
        {
            "pubsubname": PUBSUB_NAME,
            "topic": "workflow_delete",
            "route": "workflows/delete"
        },
        {
            "pubsubname": PUBSUB_NAME,
            "topic": "user-delete",
            "route": "users/delete"
        }
    ]
    print("Dapr pub/sub is subscribed to: " + json.dumps(subscriptions))
    return jsonify(subscriptions)


@app.post("/workflows/add")
async def workflow_add():
    """
    An endpoint for receiving data about a new workflow.
    """
    event = from_http(request.headers, await request.get_data())
    workflow_id = is_string_valid_uuid(event.data["workflow_id"])
    if workflow_id is None:
        return json.dumps({ "success": False, "err": "Empty workflow id" }), 400, { "ContentType": "application/json" }
    try:
        settings = contracts.WorkflowSettings(
            is_full_page_recognition=event.data["is_full_page_recognition"],
            skip_img_enchancement=event.data["skip_img_enchancement"],
            expect_diff_images=event.data["expect_diff_images"]
        )
    except ValidationError as err:
        return json.dumps({ "success": False, "err": err.json() }), 400, { "ContentType": "application/json" }
    services.workflow_service.add_workflow(workflow_id, settings)
    return json.dumps({ "success": True }), 200, { "ContentType": "application/json" }


@app.post("/workflows/update")
async def workflow_update():
    """
    An endpoint for receiving updates about a specific workflow.
    """
    event = from_http(request.headers, await request.get_data())
    workflow_id = is_string_valid_uuid(event.data["workflow_id"])
    if workflow_id is None:
        return json.dumps({ "success": False, "err": "Empty workflow id" }), 400, { "ContentType": "application/json" }
    try:
        settings = contracts.WorkflowSettings(
            is_full_page_recognition=event.data["is_full_page_recognition"],
            skip_img_enchancement=event.data["skip_img_recognition"],
            expect_diff_images=event.data["skip_img_recognition"]
        )
    except Exception as err:
        return json.dumps({ "success": False, "err": err }), 400, { "ContentType": "application/json" }
    services.workflow_service.update_workflow(
        workflow_id,
        settings
    )
    return json.dumps({ "success": True }), 200, { "ContentType": "application/json" }


@app.post("/workflows/update")
async def workflow_delete():
    """
    An endpoint for receiving a delete event of a specific workflow.
    """
    event = from_http(request.headers, await request.get_data())
    services.workflow_service.delete_workflow(event.data)
    return json.dumps({ "success": True }), 200, { "ContentType": "application/json" }


@app.post("/users/delete")
async def user_delete():
    """
    An endpoint for receiving a delete event for user's data.
    """
    event = from_http(request.headers, await request.get_data())
    services.user_service.delete_users_data(event.data)
    return json.dumps({ "success": True }), 200, { "ContentType": "application/json" }


if __name__ == "__main__":
    #print("Hello from recognition service!  ʕ•ᴥ•ʔ")
    server_cfg = Config()
    server_cfg.bind = ["0.0.0.0:8000"]
    asyncio.run(serve(app, server_cfg))
