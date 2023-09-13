"""
Package for helping with processing (enhancement, read, conversion, ...)
of uploaded files.
"""
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
from quart.datastructures import FileStorage
from .recognition import get_recognition_service, RecognitionServiceType
from datetime import datetime

recognition_service = get_recognition_service(RecognitionServiceType.TESSERACT)


async def pillow_images_generator(files):
    """
    Method for creating Pillow image from a list of uploaded files.
    """
    for file_name in files:
        yield Image.open(BytesIO(
            files[file_name].stream.read()
        ))


async def start_image_processing(files: list[FileStorage]):
    print(datetime.now(), ": Executing task")
    with ThreadPoolExecutor() as tp:
        futures = []
        img_gen = pillow_images_generator(files)
        """for i in files:
            futures.append(tp.submit(test, files[i]))
        for future in as_completed(futures):
            res = future.result()
            temp = datetime.now()
            print(temp, res)"""
