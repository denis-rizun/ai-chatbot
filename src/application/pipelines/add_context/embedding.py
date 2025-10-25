from src.domain.entities.pipelines.context import Context
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.services.embedding import IEmbeddingService


class GenerateEmbeddingStep(IPipelineStep[Context]):
    def __init__(self, embedding_service: IEmbeddingService) -> None:
        self._service = embedding_service

    async def execute(self, entity: Context) -> Context:
        vectors = await self._service.store_context(entity.source_id, entity.internal.chunks)
        entity.internal.embeddings = vectors
        return entity
