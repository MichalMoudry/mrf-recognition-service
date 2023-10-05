"""
Module with tests related to service's configuration.
"""
from .config import load_configuration, CONFIG


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
