"""
Package containg code for file processing logic.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    for file_name in files:
        yield Image.open(BytesIO(
            files[file_name].stream.read()
        ))


class FileProcessingService:
    """
    A service class containing logic for file processing.
    """
    @staticmethod
    def __process_image(image: Image.Image) -> str | None:
        """
        Method for processing PIL image.
        """
        try:
            result = recognition_service.process_image_full(image)
            print(result, f"image info: {image.height} | {image.width}")
        except Exception as err:
            print("Error processing a file", err)
            return None
        return result

    async def process_files(self, batch_id: UUID, files: dict[str, FileStorage]):
        """
        A method for processing multiple files from a client.
        """
        print(f"Batch: {batch_id}")
        for key in files:
            print(f"Processing: {files[key].name}")

        futures = []
        with ThreadPoolExecutor() as tp:
            async for image in pillow_images_generator(files):
                futures.append(
                    tp.submit(self.__process_image, image)
                )
            for future in as_completed(futures):
                res = future.result()
                print(f"Future result: {res}")
