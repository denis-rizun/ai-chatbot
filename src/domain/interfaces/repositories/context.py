from abc import ABC, abstractmethod

from src.domain.interfaces.repositories.base import IBaseRepository


class IContextRepository(IBaseRepository, ABC):

    @abstractmethod
    async def get_similar(self, emb: list[float], threshold: float, limit: int = 5) -> list[dict]:
        pass
