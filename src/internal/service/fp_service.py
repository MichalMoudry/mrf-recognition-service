"""
Package containg code for file processing logic.
"""
from io import BytesIO
from uuid import UUID
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


class FileProcessingService:
    """
    A service class containing logic for file processing.
    """

    @staticmethod
    async def process_files(batch_id: UUID, files: dict[str, FileStorage]):
        """
        A method for processing multiple files from a client.
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
