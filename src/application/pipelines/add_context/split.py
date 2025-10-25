from src.domain.entities.pipelines.context import Context
from src.domain.interfaces.pipelines.step import IPipelineStep


class SplitTextStep(IPipelineStep[Context]):

    async def execute(self, entity: Context) -> Context:
        text = entity.content
        entity.internal.chunks = [
            chunk.strip()
            for chunk in text.split(". ")
            if chunk.strip()
        ]
        return entity
