from src.core.constants import NOT_IN_CONTEXT_RESPONSE
from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.repositories.manager import IRepositoryManager


class SearchContextStep(IPipelineStep):
    THRESHOLD = 0.5

    def __init__(self, repository: IRepositoryManager) -> None:
        self._repository = repository

    async def execute(self, ctx: Inference) -> Inference:
        if ctx.metadata.is_finished:
            return ctx

        found = await self._repository.context.get_similar(ctx.internal.embeddings, self.THRESHOLD)
        if not found:
            ctx.answer = NOT_IN_CONTEXT_RESPONSE
            ctx.metadata.is_finished = True
            return ctx

        content = " ".join([f["content"] for f in found])
        ctx.internal.similar = content
        return ctx
