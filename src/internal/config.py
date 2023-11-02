"""
Module for handling recognition service's configuration.
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
    print(environ.keys())
    db_conn = environ.get("DB_CONN")
    if db_conn != None:
        CONFIG["DB_CONN"] = db_conn
    else:
        CONFIG["DB_CONN"] = ""


@dataclass
class DaprSettings:
    """
    A class representing Dapr's settings.
    """


class Configuration:
    """
    A class for handling app's configuration.
    """
    def __init__(self) -> None:
        self._dapr_settings = DaprSettings()

    @property
    def dapr_settings(self) -> DaprSettings:
        """
        Property containg settings for Dapr.
        """
        return self._dapr_settings
