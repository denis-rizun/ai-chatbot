from src.domain.entities.pipelines.inference import Inference
from src.domain.interfaces.pipelines.step import IPipelineStep
from src.domain.interfaces.services.ai import IAIModel


class AskStep(IPipelineStep[Inference]):
    def __init__(self, ai_model: IAIModel) -> None:
        self._ai_model = ai_model

    async def execute(self, entity: Inference) -> Inference:
        if entity.metadata.is_finished:
            return entity

        response = await self._ai_model.ask(entity.question, entity.internal.similar)
        entity.answer = response
        entity.metadata.is_finished = True
        return entity
