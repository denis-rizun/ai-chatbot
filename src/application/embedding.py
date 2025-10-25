from src.domain.interfaces.repositories.manager import IRepositoryManager
from src.domain.interfaces.services.ai import IAIModel
from src.domain.interfaces.services.embedding import IEmbeddingService


class EmbeddingService(IEmbeddingService):
    def __init__(self, repository: IRepositoryManager, ai_model: IAIModel) -> None:
        self._repository = repository
        self._ai_model = ai_model

    async def store_context(self, source_id: int, chunks: list[str]) -> list[list[float]]:
        embeddings = []
        for i, chunk in enumerate(chunks):
            embedding = await self._ai_model.embed(chunk)
            await self._repository.context.create(
                source_id=source_id,
                chunk_index=i,
                content=chunk,
                embedding=embedding,
            )
            embeddings.append(embedding)

        await self._repository.commit()
        return embeddings
