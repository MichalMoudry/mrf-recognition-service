"""
A module with test related to database queries.
"""
from datetime import datetime
from dotenv import load_dotenv
from os import environ
from uuid import UUID, uuid4
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import sessionmaker
from model import new_document_batch, Workflow
from query import insert_batch

load_dotenv()
db_conn = environ.get("DB_CONN")
engine = create_engine(db_conn if db_conn is not None else "")
Session = sessionmaker(bind=engine)


def seed_database():
    """
    Function for inserting test data to the database.
    """
    print("Start to insert test data...")
    session = Session()
    now = datetime.utcnow()

    session.execute(
        insert(Workflow).values(
            id=uuid4(),
            is_full_page_recognition=False,
            skip_enhancement=False,
            expect_diff_images=False,
            date_added=now,
            date_updated=now
        )
    )

    session.commit()
    print("Finished inserting test data.")


def test_insert_batch():
    """
    A simple test scenario for testing INSERT command for a DocumentBatch entity.
    """
    session = Session()
    batch = new_document_batch(
        "test_batch_1",
        UUID("0e1247d7-674c-446f-bdfe-29fba40fdf34")
    )
    session.execute(insert_batch(batch))
    session.commit()

#seed_database()
