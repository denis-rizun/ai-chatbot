from uuid import uuid4

from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager


class CacheWriteStep(IPipelineStep[Inference]):
    def __init__(self, repository: IRepositoryManager) -> None:
        self._repository = repository

    @property
    def _unique_id(self) -> str:
        return f"q:{uuid4()}"

    async def execute(self, entity: Inference) -> Inference:
        if entity.metadata.is_cached:
            return entity

        caching = {
            "embedding": entity.internal.embeddings,
            "q": entity.question,
            "answer": entity.answer
        }
        await self._repository.cache.set_hashed(self._unique_id, caching)
        return entity
