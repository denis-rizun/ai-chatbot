from abc import ABC, abstractmethod

from src.domain.interfaces.repositories.base import IBaseRepository
from src.domain.types import ModelType


class IContextRepository(IBaseRepository, ABC):

    @abstractmethod
    async def get_similar(self, embedding: list[float], limit: int = 5) -> list[ModelType]:
        pass
