"""
Module containing code related to a Dapr integration.
"""
import json
from dapr.clients import DaprClient
from service.model.dtos import JsonSerializable


class DaprService:
    """
    A service class for wrapping Dapr functionality.
    """

    @staticmethod
    def publish_event(topic: str, data: JsonSerializable) -> bool:
        """
        Method for publishing an event into the MQ.
        """
        try:
            with DaprClient() as client:
                client.publish_event(
                    pubsub_name="pub-sub",
                    topic_name=topic,
                    data=json.dumps(data.serialize()),
                    data_content_type="application/json"
                )
        except:
            return False
        return True
