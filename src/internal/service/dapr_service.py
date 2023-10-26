"""
Module containing code related to a Dapr service.
"""
import json
from typing import TypeVar
from dapr.clients import DaprClient

PUBSUB_NAME = "mrf_pub_sub"
T = TypeVar("T")


class DaprService:
    """
    A service class for wrapping Dapr functionality.
    """

    @staticmethod
    def publish_event(topic: str, data):
        """
        Method for publishing an event into the MQ.
        """
        with DaprClient() as client:
            client.publish_event(
                pubsub_name=PUBSUB_NAME,
                topic_name=topic,
                data=json.dumps(data),
                data_content_type="application/json"
            )
