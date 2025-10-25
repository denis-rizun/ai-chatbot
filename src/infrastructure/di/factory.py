from src.application.pipelines.pipeline import Pipeline
from src.infrastructure.di.container import container


class Factory:

    @staticmethod
    async def get_context_pipeline() -> Pipeline:
        steps = [
            container.split_text_step(),
            await container.generate_embedding_step(),
        ]
        return Pipeline(steps=steps)

    @staticmethod
    async def get_conversation_pipeline() -> Pipeline:
        steps = [
            await container.cache_read_step(),
            await container.search_context_step(),
            container.ask_step(),
            await container.cache_write_step()
        ]
        return Pipeline(steps=steps)
