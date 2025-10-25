from src.domain.entities.pipelines.context import Context
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.services.embedding import IEmbeddingService


class GenerateEmbeddingStep(IPipelineStep):
    def __init__(self, embedding_service: IEmbeddingService) -> None:
        self._service = embedding_service

    async def execute(self, ctx: Context) -> dict:
        vectors = await self._service.store_context(ctx.source_id, ctx.internal.chunks)
        ctx.internal.embeddings = vectors
        return ctx
