"""
Module for handling recognition service's configuration.
"""
from dataclasses import dataclass
from enum import StrEnum
from os import environ
from typing import Optional


class Environment(StrEnum):
    """
    A string enumeration class for representing app's environment.
    """
    DEV = "dev"
    PROD = "prod"


@dataclass
class Config:
    """
    A class representing service's configuration object.
    """
    db_conn: str
    env: Environment


def parse_db_conn_string(conn: str) -> str:
    """
    Function for forming a DB connection string into a SQLAlchemy accepted one.
    """
    parts: dict[str, str] = {}
    for item in conn.split(" "):
        split = item.split("=")
        parts[split[0]] = split[1]
    return f"postgresql+psycopg2://{parts['user']}:{parts['password']}@{parts['host']}/{parts['dbname']}?sslmode={parts['sslmode']}"


def parse_env_setting(env: Optional[str]) -> Environment:
    """
    
    """
    match env:
        case 'dev':
            return Environment.DEV
        case 'prod':
            return Environment.PROD
        case _:
            return Environment.DEV


def load_configuration() -> Config:
    """
    Function for loading service's configuration.
    """
    db_conn = environ.get("DB_CONN")
    return Config(
        db_conn if db_conn != None else "",
        parse_env_setting(environ.get("ENV"))
    )
