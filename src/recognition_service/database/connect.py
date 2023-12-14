"""
Module for handling DB connection.
"""
from typing import Any, Optional, Tuple
import psycopg
from config import Config, Environment


def get_db_connection(cfg: Config) -> Optional[psycopg.Connection[Tuple[Any, ...]]]:
    """
    Function for creating a new DB connection.
    """
    if cfg.env == Environment.DEV:
        return psycopg.connect(cfg.db_conn)
    elif cfg.env == Environment.PROD:
        return psycopg.connect(cfg.db_conn)
    else:
        return None
