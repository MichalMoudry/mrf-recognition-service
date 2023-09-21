"""
Package for a database layer of the recognition service.
"""
from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(environ.get("DB_CONN"))
Session = sessionmaker(bind=engine)
