"""
Package for a database layer of the recognition service.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from internal.config import load_configuration, CONFIG

load_configuration()
connection_str = CONFIG.get("DB_CONN")
engine = create_engine(connection_str if connection_str is not None else "")
Session = sessionmaker(bind=engine)
