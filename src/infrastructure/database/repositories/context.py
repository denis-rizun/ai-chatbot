from sqlalchemy import select

from src.domain.interfaces.repositories.context import IContextRepository
from src.infrastructure.database.models import ContextModel
from src.infrastructure.database.repositories.base import BaseRepository


class ContextRepository(IContextRepository, BaseRepository[ContextModel]):
    MODEL = ContextModel

    async def get_similar(self, embedding: list[float], limit: int = 5) -> list[ContextModel]:
        stmt = (
            select(ContextModel)
            .order_by(ContextModel.embedding.op("<=>")(embedding))
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
