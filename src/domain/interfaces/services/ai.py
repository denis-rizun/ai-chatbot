from abc import ABC, abstractmethod


class IAIModel(ABC):

    @abstractmethod
    async def ask(self, q: str, context: str) -> str:
        pass

    @abstractmethod
    async def embed(self, text: str | list[str]) -> list[float]:
        pass
