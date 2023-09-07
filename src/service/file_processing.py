"""
Package for helping with processing (enhancement, read, conversion, ...) of uploaded files.
"""
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from fastapi import UploadFile
from PIL import Image

async def pillow_images_generator(files: list[UploadFile]):
    """
    Method for creating Pillow image from a list of uploaded files.
    """
    for file in files:
        yield Image.open(BytesIO(await file.read()))


async def start_image_processing(files: list[UploadFile]):
    """file_gen = pillow_images_generator(files)
    with ThreadPoolExecutor() as te:
        processing = te.map()"""
    ...
