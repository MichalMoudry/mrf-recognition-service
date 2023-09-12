"""
Module that contains endpoint methods for the recognition service.
"""
from quart import Quart, Response, request, jsonify
from quart.datastructures import FileStorage

app = Quart(__name__)


@app.get("/health")
async def health() -> str:
    """
    Service health endpoint method.
    """
    return "healthy"


@app.post("/batch")
async def create_batch() -> Response:
    """
    An endpoint for creating a new batch of documents for processing.
    """
    form = await request.form
    print(form)
    for i in form.items():
        print(i[0], i[1])
    print("--- Files")
    files: dict[str, FileStorage] = await request.files
    for i in files:
        print(i, "=>", files[i].filename, files[i].content_type)
    return jsonify("Batch created")


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
