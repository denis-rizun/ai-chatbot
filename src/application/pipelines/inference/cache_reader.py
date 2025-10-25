from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager
from src.domain.interfaces.services.ai import IAIModel


class CacheReadStep(IPipelineStep[Inference]):
    TOP_K = 1
    THRESHOLD = 0.2

    def __init__(self, repository: IRepositoryManager, ai_model: IAIModel) -> None:
        self._repository = repository
        self._ai_model = ai_model

    async def execute(self, entity: Inference) -> Inference:
        embeddings = await self._ai_model.embed(entity.question)
        cached = await self._repository.cache.get_similar_vectors(
            vector=embeddings,
            top_k=self.TOP_K,
            score_threshold=self.THRESHOLD
        )
        if cached:
            entity.answer = cached["answer"]
            entity.metadata.is_cached = True
            entity.metadata.is_finished = True

        entity.internal.embeddings = embeddings
        return entity
