from src.domain.entities.pipelines.context import Context
from src.domain.interfaces.pipelines.step import IPipelineStep


class SplitTextStep(IPipelineStep):

    async def execute(self, ctx: Context) -> dict:
        text = ctx.content
        ctx.internal.chunks = [
            chunk.strip()
            for chunk in text.split(". ")
            if chunk.strip()
        ]
        return ctx
