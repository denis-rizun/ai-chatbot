from abc import ABC, abstractmethod


class IEmbeddingService(ABC):

    @abstractmethod
    async def store_context(self, source_id: int, chunks: list[str]) -> list[list[float]]:
        pass
