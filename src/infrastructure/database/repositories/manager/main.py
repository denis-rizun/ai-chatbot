from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.interfaces.repositories.manager import IRepositoryManager
from src.infrastructure.database.repositories.manager.factory import RepositoryFactory
from src.infrastructure.database.repositories.manager.transaction import TransactionManager


class RepositoryManager(RepositoryFactory, TransactionManager, IRepositoryManager):
    def __init__(self, session: AsyncSession, client: Redis) -> None:
        self._session = session
        self._client = client

    @staticmethod
    def get_repository(session: AsyncSession, client: Redis) -> "RepositoryManager":
        return RepositoryManager(session, client)
