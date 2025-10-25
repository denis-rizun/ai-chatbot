from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.services.ai import IAIModel


class AskStep(IPipelineStep):
    def __init__(self, ai_model: IAIModel) -> None:
        self._ai_model = ai_model

    async def execute(self, ctx: Inference) -> Inference:
        if ctx.metadata.is_finished:
            return ctx

        response = await self._ai_model.ask(ctx.question, ctx.internal.similar)
        ctx.answer = response
        ctx.metadata.is_finished = True
        return ctx
