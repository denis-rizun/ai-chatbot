from functools import cached_property

from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.interfaces.repositories.cache import ICacheRepository
from src.domain.interfaces.repositories.context import IContextRepository
from src.infrastructure.database.repositories.cache import CacheRepository
from src.infrastructure.database.repositories.context import ContextRepository


class RepositoryFactory:
    _session: AsyncSession | None = None
    _client: Redis | None = None

    @cached_property
    def cache(self) -> ICacheRepository:
        return CacheRepository(self._client)

    @cached_property
    def context(self) -> IContextRepository:
        return ContextRepository(self._session)
