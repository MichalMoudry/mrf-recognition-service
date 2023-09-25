"""
Package for a database layer of the recognition service.
"""
from os import environ
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine(environ.get("DB_CONN"))
Session = sessionmaker(bind=engine)
