from src.domain.interfaces.pipelines.step import IPipelineStep


class SplitTextStep(IPipelineStep):

    async def execute(self, ctx: dict) -> dict:
        text = ctx["context"]
        ctx["chunks"] = [chunk.strip() for chunk in text.split(". ") if chunk.strip()]
        return ctx
