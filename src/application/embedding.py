from src.domain.interfaces.repositories.manager import IRepositoryManager
from src.domain.interfaces.services.ai import IAIModel
from src.domain.interfaces.services.embedding import IEmbeddingService
from src.infrastructure.database.models import ContextModel


class EmbeddingService(IEmbeddingService):
    def __init__(self, repository: IRepositoryManager, ai_model: IAIModel) -> None:
        self._repository = repository
        self._ai_model = ai_model

    async def store_context(self, source_id: int, chunks: list[str]) -> list[list[float]]:
        embeddings = await self._ai_model.embed(chunks)
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            await self._repository.context.create(
                source_id=source_id,
                chunk_index=i,
                content=chunk,
                embedding=embedding,
            )

        await self._repository.commit()
        return embeddings

    async def search_similar(self, query: str, limit: int = 5) -> list[ContextModel]:
        embeddings = await self._ai_model.embed(query)
        return await self._repository.context.get_similar(embeddings, limit)
