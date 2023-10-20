"""
Package for handling recognition service's configuration.
"""
from dataclasses import dataclass
from os import environ
from dotenv import load_dotenv

CONFIG: dict[str, str] = {}


def load_configuration():
    """
    Function for loading service's configuration.
    """
    load_dotenv()
    db_conn = environ.get("DB_CONN")
    if db_conn != None:
        CONFIG["DB_CONN"] = db_conn

    should_retry = environ.get("DAPR_SHOULD_RETRY")
    if should_retry is not None:
        CONFIG["DAPR_SHOULD_RETRY"] = should_retry


@dataclass
class DaprSettings:
    """
    A class representing Dapr's settings.
    """
    should_retry: bool


class Configuration:
    """
    A class for handling app's configuration.
    """
    def __init__(self) -> None:
        self._dapr_settings = DaprSettings(
            bool(CONFIG["DAPR_SHOULD_RETRY"])
        )

    @property
    def dapr_settings(self) -> DaprSettings:
        """
        Property containg settings for Dapr.
        """
        return self._dapr_settings
