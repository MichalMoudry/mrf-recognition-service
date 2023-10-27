"""
A module with test related to database queries.
"""
from datetime import datetime
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from uuid import uuid4, UUID
from pytest import mark
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
"""from model import new_document_batch, new_processsed_document, Workflow
from query import insert_batch, select_batch, delete_batch
from dto import BatchInfo

load_dotenv()
db_conn = environ.get("DB_CONN")
engine = create_engine(db_conn if db_conn is not None else "")
Session = sessionmaker(bind=engine)
default_workflow_id = uuid4()


def seed_database():
    # Function for inserting test data to the database.
    print("Start to insert test data...")
    session = Session()
    now = datetime.utcnow()

    session.execute(
        insert(Workflow).values(
            id=default_workflow_id,
            is_full_page_recognition=False,
            skip_enhancement=False,
            expect_diff_images=False,
            date_added=now,
            date_updated=now
        )
    )

    session.commit()
    print("Finished inserting test data.")


@mark.skip(reason="Only runnable with a running database")
def test_insert_batch():
    # A simple test scenario for testing INSERT command for a DocumentBatch entity.
    seed_database()
    session = Session()
    folder = Path(__file__).parent.parent.parent.parent / "tests/test_images"
    file1 = (folder / "repo_screenshot_2.jpg").open("rb")
    file2 = (folder / "repo_screenshot.png").open("rb")
    batch_id = uuid4()
    batch = new_document_batch(
        batch_id,
        "test_batch_1",
        "test_user_1",
        default_workflow_id,
        [
            new_processsed_document(file1.name, "image/jpg", file1.read(), batch_id),
            new_processsed_document(file2.name, "image/png", file2.read(), batch_id)
        ]
    )
    session.execute(insert_batch(batch))
    session.bulk_save_objects(batch.documents)
    session.commit()

    session2 = Session()
    result = session2.execute(select_batch(batch_id)).first()
    if result is None: return
    temp = BatchInfo(result.t[0], result.t[1], result.t[2], result.t[3])
    session2.execute(delete_batch(batch_id))
    session2.commit()
    file1.close()
    file2.close()

if __name__ == "__main__":
    test_insert_batch()"""
