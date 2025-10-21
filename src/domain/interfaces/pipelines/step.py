from abc import ABC, abstractmethod
from typing import Any


class IPipelineStep(ABC):

    @abstractmethod
    async def execute(self, **kwargs: Any) -> Any:
        pass
