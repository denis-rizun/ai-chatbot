"""feat Source;Context

Revision ID: 7559a50a33d2
Revises: 5c7b5713b6d5
Create Date: 2025-10-20 21:30:20.102582

"""
from typing import Sequence, Union

import pgvector
from alembic import op
import sqlalchemy as sa


revision: str = '7559a50a33d2'
down_revision: Union[str, None] = '5c7b5713b6d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        'sources',
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'contexts',
        sa.Column('source_id', sa.Integer(), nullable=False),
        sa.Column('chunk_index', sa.Integer(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('embedding', pgvector.sqlalchemy.vector.VECTOR(dim=384), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index("idx_contexts_source_id", "contexts", ["source_id"])
    op.create_index("idx_contexts_chunk_index", "contexts", ["chunk_index"])
    op.create_index("idx_contexts_embedding", "contexts", ["embedding"], postgresql_using="ivfflat")


def downgrade() -> None:
    op.drop_table('contexts')
    op.drop_table('sources')
