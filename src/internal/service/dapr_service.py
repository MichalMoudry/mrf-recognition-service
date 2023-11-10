"""
Module containing code related to a Dapr service.
"""
import json
from dapr.clients import DaprClient
from internal.service.model.dto import JsonSerializable

PUBSUB_NAME = "mrf-pub-sub"


class DaprService:
    """
    A service class for wrapping Dapr functionality.
    """

    @staticmethod
    def publish_event(topic: str, data: JsonSerializable):
        """
        Method for publishing an event into the MQ.
        """
        with DaprClient() as client:
            client.publish_event(
                pubsub_name=PUBSUB_NAME,
                topic_name=topic,
                data=json.dumps(data.serialize()),
                data_content_type="application/json"
            )
