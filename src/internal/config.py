"""
Module for handling recognition service's configuration.
"""
from os import environ
from dotenv import load_dotenv

CONFIG: dict[str, str] = {}


def parse_db_conn_string(conn: str) -> str:
    """
    Function for forming a DB connection string into a SQLAlchemy accepted one.
    """
    parts: dict[str, str] = {}
    for item in conn.split(" "):
        split = item.split("=")
        parts[split[0]] = split[1]
    return f"postgresql+psycopg2://{parts['user']}:{parts['password']}@{parts['host']}/{parts['dbname']}?sslmode={parts['sslmode']}"


def load_configuration():
    """
    Function for loading service's configuration.
    """
    load_dotenv()
    db_conn = environ.get("DB_CONN")
    if db_conn != None:
        CONFIG["DB_CONN"] = parse_db_conn_string(db_conn)
    else:
        CONFIG["DB_CONN"] = parse_db_conn_string("dbname=data-persistence host=localhost port=5432 sslmode=disable user=root password=root")
