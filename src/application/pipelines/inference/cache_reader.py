from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager
from src.domain.interfaces.services.ai import IAIModel


class CacheReadStep(IPipelineStep):
    TOP_K = 1
    THRESHOLD = 0.2

    def __init__(self, repository: IRepositoryManager, ai_model: IAIModel) -> None:
        self._repository = repository
        self._ai_model = ai_model

    async def execute(self, ctx: Inference) -> Inference:
        embeddings = await self._ai_model.embed(ctx.question)
        cached = await self._repository.cache.get_similar_vectors(
            vector=embeddings,
            top_k=self.TOP_K,
            score_threshold=self.THRESHOLD
        )
        if cached:
            ctx.answer = cached
            ctx.metadata.is_cached = True
            ctx.metadata.is_finished = True

        ctx.internal.embeddings = embeddings
        return ctx
