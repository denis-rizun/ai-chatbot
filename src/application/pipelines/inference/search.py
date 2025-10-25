from src.core.constants import NOT_IN_CONTEXT_RESPONSE
from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager


class SearchContextStep(IPipelineStep[Inference]):
    THRESHOLD = 0.5

    def __init__(self, repository: IRepositoryManager) -> None:
        self._repository = repository

    async def execute(self, entity: Inference) -> Inference:
        if entity.metadata.is_finished:
            return entity

        found = await self._repository.context.get_similar(entity.internal.embeddings, self.THRESHOLD)
        if not found:
            entity.answer = NOT_IN_CONTEXT_RESPONSE
            entity.metadata.is_finished = True
            return entity

        content = " ".join([f["content"] for f in found])
        entity.internal.similar = content
        return entity
