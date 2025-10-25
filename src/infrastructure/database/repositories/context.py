from sqlalchemy import text

from src.domain.interfaces.repositories.context import IContextRepository
from src.infrastructure.database.models import ContextModel
from src.infrastructure.database.repositories.base import BaseRepository


class ContextRepository(IContextRepository, BaseRepository[ContextModel]):
    MODEL = ContextModel

    async def get_similar(self, embedding: list[float], threshold: float, limit = 5) -> list[dict]:
        query = text(
            """
            SELECT id,
                   source_id,
                   chunk_index,
                   content,
                   created_at,
                   updated_at,
                   embedding <=> :embedding_vec AS distance
            FROM contexts
            ORDER BY distance
            """
        )

        result = await self.session.execute(
            query,
            params={"embedding_vec": str(embedding), "limit": limit}
        )
        rows = result.fetchall()

        filtered = [
            {
                "id": row.id,
                "source_id": row.source_id,
                "chunk_index": row.chunk_index,
                "content": row.content,
                "created_at": row.created_at,
                "updated_at": row.updated_at,
                "distance": row.distance
            }
            for row in rows
            if row.distance <= threshold
        ]

        return filtered