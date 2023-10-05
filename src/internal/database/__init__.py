"""
Package for a database layer of the recognition service.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from internal.config import CONFIG

engine = create_engine(CONFIG["DB_CONN"])
Session = sessionmaker(bind=engine)
