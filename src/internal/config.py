"""
Package for handling recognition service's configuration.
"""
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