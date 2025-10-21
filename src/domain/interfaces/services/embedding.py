from abc import ABC, abstractmethod


class IEmbeddingService(ABC):

    @abstractmethod
    async def store_context(self, source_id: int, chunks: list[str]) -> list[list[float]]:
        pass

    @abstractmethod
    async def search_similar(self, query: str, limit: int = 5) -> list:
        pass
