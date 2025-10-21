from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.services.embedding import IEmbeddingService


class GenerateEmbeddingStep(IPipelineStep):
    def __init__(self, embedding_service: IEmbeddingService) -> None:
        self._service = embedding_service

    async def execute(self, ctx: dict) -> dict:
        vectors = await self._service.store_context(1, ctx["chunks"])
        ctx["embeddings"] = vectors
        return ctx
