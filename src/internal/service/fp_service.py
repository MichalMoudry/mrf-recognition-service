"""
Module containg code for file processing logic.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from uuid import UUID
from PIL import ImageFile
from quart.datastructures import FileStorage

from internal.database import Session
from internal.database.query import update_batch
from internal.database.model import new_processsed_document, new_field_value, BatchState, TemplateFieldValue
from internal.service.model.dto import ProcessedDocumentInfo
from .recognition import get_recognition_service, RecognitionServiceType

recognition_service = get_recognition_service(RecognitionServiceType.TESSERACT)


async def pillow_images_generator(files: dict[str, FileStorage]):
    """
    Method for creating Pillow image from a list of uploaded files.
    """
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    for file_name in files:
        file = files[file_name]
        yield ProcessedDocumentInfo(
            file_name,
            file.stream.read(),
            file.content_type
        )


class FileProcessingService:
    """
    A service class containing logic for file processing.
    """
    @staticmethod
    def __process_image(image: ProcessedDocumentInfo) -> ProcessedDocumentInfo:
        """
        Method for processing PIL image.
        """
        try:
            image.results = recognition_service.process_image_full(
                image.pil_image
            )
        except:
            image.empty_content()
            image.was_successful = False
        return image

    async def process_files(self, batch_id: UUID, files: dict[str, FileStorage]):
        """
        A method for processing multiple files from a client.
        """
        futures = []
        results: list[ProcessedDocumentInfo] = []
        is_success = True
        with ThreadPoolExecutor() as tp:
            async for image in pillow_images_generator(files):
                futures.append(
                    tp.submit(self.__process_image, image)
                )
            for future in as_completed(futures):
                res: ProcessedDocumentInfo = future.result()
                if res.was_successful is False:
                    is_success = False
                results.append(res)

        processed_documents = [
            new_processsed_document(
                result.name,
                result.content_type,
                result.content,
                batch_id
            )
            for result in results
        ]
        result_fields: list[TemplateFieldValue] = []
        for index, val in enumerate(processed_documents):
            info = results[index]
            if info.name == val.name:
                for row in info.results:
                    result_fields.append(
                        new_field_value("field_", row, val.id)
                    )
        
        session = Session()
        session.bulk_save_objects(processed_documents)
        session.bulk_save_objects(result_fields)
        session.execute(
            update_batch(
                batch_id,
                BatchState.COMPLETED if is_success else BatchState.FAILED,
                datetime.utcnow()
            )
        )
        session.commit()
