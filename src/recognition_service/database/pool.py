"""
Module for handling DB connection pools.
"""
from psycopg_pool import ConnectionPool


def create_conn_pool():
    """
    Function for creating a new database connection pool.
    """
    with ConnectionPool() as pool:
        ...
    return ConnectionPool("")
