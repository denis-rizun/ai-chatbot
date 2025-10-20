from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.manager.factory import RepositoryFactory
from src.infrastructure.database.repositories.manager.transaction import TransactionManager


class RepositoryManager(RepositoryFactory, TransactionManager):
    def __init__(self, session: AsyncSession, client: Redis) -> None:
        self._session = session
        self._client = client

    @staticmethod
    def get_repository(session: AsyncSession, client: Redis) -> "RepositoryManager":
        return RepositoryManager(session, client)
