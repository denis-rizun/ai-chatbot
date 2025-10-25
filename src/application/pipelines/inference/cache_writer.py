from uuid import uuid4

from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager


class CacheWriteStep(IPipelineStep):
    def __init__(self, repository: IRepositoryManager) -> None:
        self._repository = repository

    @property
    def _unique_id(self) -> str:
        return f"q:{uuid4()}"

    async def execute(self, ctx: Inference) -> Inference:
        if ctx.metadata.is_cached:
            return ctx

        caching = {"embedding": ctx.internal.embeddings, "q": ctx.question, "answer": ctx.answer}
        await self._repository.cache.set_hashed(self._unique_id, caching)
        return ctx
