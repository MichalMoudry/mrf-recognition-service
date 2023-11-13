"""
Package for a database layer of the recognition service.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from internal.config import load_configuration, CONFIG

load_configuration()
try:
    engine = create_engine(CONFIG["DB_CONN"])
    Session = sessionmaker(bind=engine)
except:
    print("Unable to connect to DB.")
