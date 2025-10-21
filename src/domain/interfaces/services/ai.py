from abc import ABC, abstractmethod
from typing import Any


class IAIModel(ABC):

    @abstractmethod
    async def ask(self, q: str) -> str:
        pass

    @abstractmethod
    async def embed(self, text: str | list[str]) -> Any:
        pass
