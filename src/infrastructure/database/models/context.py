from pgvector.sqlalchemy import Vector
from sqlalchemy import ForeignKey, Text, Index
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import BaseModel


class ContextModel(BaseModel):
    __tablename__ = "contexts"

    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    chunk_index: Mapped[int]
    content: Mapped[str] = mapped_column(Text)
    embedding: Mapped[Vector] = mapped_column(Vector(dim=1536))

    __table_args__ = (
        Index("idx_contexts_source_id", "source_id"),
        Index("idx_contexts_chunk_index", "chunk_index"),
        Index("idx_contexts_embedding", "embedding", postgresql_using="ivfflat"),
    )