"""
Package for helping with processing (enhancement, read, conversion, ...)
of uploaded files.
"""
from io import BytesIO
from uuid import UUID
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageFile
from quart.datastructures import FileStorage
from .recognition import get_recognition_service, RecognitionServiceType

recognition_service = get_recognition_service(RecognitionServiceType.TESSERACT)


async def pillow_images_generator(files: dict[str, FileStorage]):
    """
    Method for creating Pillow image from a list of uploaded files.
    """
    for file_name in files:
        yield Image.open(BytesIO(
            files[file_name].stream.read()
        ))


def process_file(file: FileStorage):
    """
    Function for processing a single uploaded file.
    """
    try:
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img = Image.open(
            BytesIO(
                file.stream.read()
            )
        )
        return recognition_service.process_image_full(img)
    except Exception as err:
        print(f"\n{file.name}", err)


async def execute_image_processing(batch_id: UUID, files: dict[str, FileStorage]):
    """
    Function for starting/executing a processing of the document batch.
    """
    print(f"Batch: {batch_id}")
    for key in files:
        print(f"Processing: {files[key].name}")
    """with ThreadPoolExecutor() as tp:
        futures = []
        for key in files:
            futures.append(tp.submit(process_file, files[key]))
        for future in as_completed(futures):
            res = future.result()"""
