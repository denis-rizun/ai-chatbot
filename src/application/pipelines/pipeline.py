from src.domain.interfaces.pipelines.step import IPipelineStep


class Pipeline:
    def __init__(self, steps: list[IPipelineStep]) -> None:
        self._steps = steps

    async def run(self, ctx: dict) -> dict:
        for step in self._steps:
            ctx = await step.execute(ctx)

        return ctx
