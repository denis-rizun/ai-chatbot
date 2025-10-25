from abc import ABC, abstractmethod
from typing import Generic

from src.domain.types import EntityType


class IPipelineStep(ABC, Generic[EntityType]):

    @abstractmethod
    async def execute(self, entity: EntityType) -> EntityType:
        pass
