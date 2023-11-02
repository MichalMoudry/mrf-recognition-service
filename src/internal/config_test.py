"""
Module with tests related to service's configuration.
"""
from .config import load_configuration, parse_db_conn_string, CONFIG


def test_basic_cfg_load():
    """
    A test scenario for testing environment values before and after config load.
    """
    CONFIG.clear() # Clear config, so the test is isolated.
    before = CONFIG.get("DB_CONN")
    assert before is None

    load_configuration()
    db_conn = CONFIG["DB_CONN"]
    assert db_conn is not None and len(db_conn) > 0


def test_db_conn_parsing():
    """
    Test covering transformation of a DB connection string.
    """
    db_string = "dbname=test_db host=server.postgres.database.azure.com port=5432 sslmode=require user=root password=root_pass"
    result = parse_db_conn_string(db_string)
    assert result == "postgresql+psycopg2://root:root_pass@server.postgres.database.azure.com/test_db?sslmode=require"
