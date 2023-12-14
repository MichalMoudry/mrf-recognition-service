"""
Module with tests related to service's configuration.
"""
from os import environ
from config import load_configuration


def test_basic_cfg_load():
    """
    A test scenario for testing environment values before and after config load.
    """
    cfg = load_configuration()
    assert cfg.db_conn == ""

    conn_str = "postgresql+psycopg2://root:root_pass@server.postgres.database.azure.com/test_db?sslmode=require"
    environ["DB_CONN"] = conn_str
    cfg = load_configuration()
    assert cfg.db_conn == conn_str
