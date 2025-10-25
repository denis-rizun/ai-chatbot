from abc import ABC, abstractmethod
from typing import Any


class ICacheRepository(ABC):

    @abstractmethod
    async def get(self, key: str) -> Any | None:
        pass

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass

    @abstractmethod
    async def exists(self, key: str) -> bool:
        pass

    @abstractmethod
    async def set_hashed(self, key: str, data: dict[str, Any]) -> None:
        pass

    @abstractmethod
    async def get_similar_vectors(
        self,
        vector: list[float],
        top_k: int,
        score_threshold: int
    ) -> dict | None:
        pass
