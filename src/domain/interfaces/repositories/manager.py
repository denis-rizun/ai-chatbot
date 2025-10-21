from abc import ABC, abstractmethod

from src.domain.interfaces.repositories.cache import ICacheRepository
from src.domain.interfaces.repositories.context import IContextRepository


class IRepositoryManager(ABC):

    @property
    @abstractmethod
    def cache(self) -> ICacheRepository:
        pass

    @property
    @abstractmethod
    def context(self) -> IContextRepository:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def flush(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass
