"""init migration

Revision ID: 29cad60b1ac6
Revises: 
Create Date: 2023-09-19 16:05:00.491709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29cad60b1ac6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "document_batches",
        sa.Column("id", sa.Uuid, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("state", sa.SmallInteger, nullable=False),
        sa.Column("start_date", sa.TIMESTAMP, nullable=False),
        sa.Column("completed_date", sa.TIMESTAMP, nullable=True),
        sa.Column("date_added", sa.TIMESTAMP, nullable=False),
        sa.Column("date_updated", sa.TIMESTAMP, nullable=False)
    )

    op.create_table(
        "processed_documents",
        sa.Column("id", sa.Uuid, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("content_type", sa.String(255), nullable=False),
        sa.Column("is_archived", sa.Boolean, nullable=False),
        sa.Column("archive_key", sa.String(128), nullable=True),
        sa.Column("date_archived", sa.TIMESTAMP, nullable=True),
        sa.Column("data", sa.LargeBinary, nullable=True),
        sa.Column("batch_id", sa.Uuid, nullable=False)
    )
    op.create_foreign_key(
        "fk_batch",
        "processed_documents",
        "document_batches",
        local_cols=["batch_id"],
        remote_cols=["id"]
    )

    op.create_table("workflows")
    op.create_table("document_templates")
    op.create_table("template_fields")


def downgrade() -> None:
    op.drop_table("document_batches")
    op.drop_table("processed_documents")
    op.drop_table("workflows")
    op.drop_table("document_templates")
    op.drop_table("template_fields")
